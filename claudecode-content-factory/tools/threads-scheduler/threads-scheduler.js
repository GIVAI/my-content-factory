#!/usr/bin/env node
// Universal Threads Scheduler via MoreLogin CDP
// v3.0 — Config-driven, no hardcoded profiles
// Usage: node threads-scheduler.js [--config config.json] [--dry-run]

const WebSocket = require('ws');
const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');

// ─── Config ───────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
function getArg(name, def) {
  const i = args.indexOf(`--${name}`);
  return i >= 0 && args[i + 1] ? args[i + 1] : def;
}
const DRY_RUN = args.includes('--dry-run');
const CONFIG_PATH = getArg('config', path.join(__dirname, 'config.json'));

if (!fs.existsSync(CONFIG_PATH)) {
  console.error(`Config not found: ${CONFIG_PATH}`);
  console.error('Copy config.example.json to config.json and fill in your values.');
  process.exit(1);
}

const cfg = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));

const NOTION_TOKEN = cfg.notion?.token || '';
const DB_ID = cfg.notion?.databaseId || '';
const STATUS_PROP = cfg.notion?.statusProperty || 'Status';
const APPROVED_VALUE = cfg.notion?.approvedValue || 'Approved';
const PUBLISHED_VALUE = cfg.notion?.publishedValue || 'Published';
const TITLE_PROPS = cfg.notion?.titleProperties || ['Post', 'Name', 'Title'];

const PORT = cfg.morelogin?.cdpPort || 51830;

const TIMES = cfg.schedule?.times || ['08:23', '10:43', '13:07', '17:36', '20:11'];
const TIMEZONE = cfg.schedule?.timezone || 'Europe/Moscow';
const DAYS = cfg.schedule?.days || 1;
const MAX_POSTS = cfg.schedule?.maxPosts || 10;

const DELAY = {
  afterCompose: cfg.delays?.afterCompose || 4000,
  afterType: cfg.delays?.afterType || 500,
  afterSchedule: cfg.delays?.afterSchedule || 4000,
  betweenPosts: cfg.delays?.betweenPosts || 3000,
  pageLoad: cfg.delays?.pageLoad || 8000,
  refreshEvery: cfg.delays?.refreshEveryNPosts || 5,
};

const MAX_RETRIES = cfg.retries?.maxRetries || 3;
const RETRY_DELAY_MS = cfg.retries?.retryDelayMs || 2000;
const POST_ATTEMPTS = cfg.retries?.postAttempts || 2;

const LOG_DIR = cfg.logging?.directory || './logs';
const ACCOUNT = cfg.logging?.accountName || 'default';

// ─── Globals ──────────────────────────────────────────────────────────────────

let globalCDP = null, globalTabId = null, globalPort = null;
const sleep = ms => new Promise(r => setTimeout(r, ms));

// ─── Logging ──────────────────────────────────────────────────────────────────

function log(msg, level = 'INFO') {
  const ts = new Date().toISOString();
  const line = `[${ts}] [${level}] ${msg}`;
  console.log(line);
  try {
    if (!fs.existsSync(LOG_DIR)) fs.mkdirSync(LOG_DIR, { recursive: true });
    const logFile = path.join(LOG_DIR, `threads-${ACCOUNT}-${new Date().toISOString().split('T')[0]}.log`);
    fs.appendFileSync(logFile, line + '\n');
  } catch {}
}

// ─── Retry wrapper ────────────────────────────────────────────────────────────

async function withRetry(fn, name, maxRetries = MAX_RETRIES) {
  let lastError;
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try { return await fn(); } catch (e) {
      lastError = e;
      log(`${name} failed (attempt ${attempt}/${maxRetries}): ${e.message}`, 'WARN');
      if (attempt < maxRetries) await sleep(RETRY_DELAY_MS * attempt);
    }
  }
  throw lastError;
}

// ─── Time helpers ─────────────────────────────────────────────────────────────

function getCurrentTime() {
  const now = new Date();
  const local = new Date(now.toLocaleString('en-US', { timeZone: TIMEZONE }));
  return { h: local.getHours(), m: local.getMinutes() };
}

function getTimeSlotsWithDays(times, days) {
  const { h, m } = getCurrentTime();
  const nowMin = h * 60 + m;
  const slots = [];
  for (let day = 0; day < days; day++) {
    for (const t of times) {
      const [hh, mm] = t.split(':').map(Number);
      const timeMin = hh * 60 + mm;
      if (day === 0 && timeMin <= nowMin + 15) continue;
      slots.push({ time: t, dayOffset: day });
    }
  }
  return slots;
}

// ─── Notion API ───────────────────────────────────────────────────────────────

function notionRequest(method, urlPath, body) {
  return new Promise((resolve, reject) => {
    const data = body ? JSON.stringify(body) : null;
    const req = https.request({
      hostname: 'api.notion.com', path: `/v1/${urlPath}`, method,
      headers: {
        'Authorization': `Bearer ${NOTION_TOKEN}`,
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
        ...(data ? { 'Content-Length': Buffer.byteLength(data) } : {})
      },
      timeout: 30000
    }, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(d);
          parsed.object === 'error' ? reject(new Error(`Notion API: ${parsed.message}`)) : resolve(parsed);
        } catch (e) { reject(new Error(`Notion parse error: ${d.substring(0, 200)}`)); }
      });
    });
    req.on('error', reject);
    req.on('timeout', () => { req.destroy(); reject(new Error('Notion request timeout')); });
    if (data) req.write(data);
    req.end();
  });
}

async function getApprovedPosts() {
  const r = await withRetry(
    () => notionRequest('POST', `databases/${DB_ID}/query`, {
      filter: { property: STATUS_PROP, select: { equals: APPROVED_VALUE } },
      page_size: MAX_POSTS
    }), 'Fetch Approved posts'
  );
  const posts = [];
  for (const page of (r.results || [])) {
    const id = page.id;
    const blocks = await withRetry(() => notionRequest('GET', `blocks/${id}/children?page_size=100`), `Fetch blocks for ${id}`);
    const textBlocks = [];
    for (const b of (blocks.results || [])) {
      if (b.type === 'code') {
        const text = (b.code?.rich_text || []).map(rt => rt.text?.content || '').join('');
        if (text.trim()) textBlocks.push(text);
      }
    }
    if (textBlocks.length > 0) {
      let title = textBlocks[0].substring(0, 50);
      for (const prop of TITLE_PROPS) {
        const t = page.properties?.[prop]?.title?.[0]?.text?.content;
        if (t) { title = t; break; }
      }
      const imageUrl = page.properties?.['Image URL']?.url || null;
      posts.push({ id, title, blocks: textBlocks, imageUrl });
    }
  }
  return posts;
}

async function updatePostStatus(pageId, status) {
  try {
    await withRetry(
      () => notionRequest('PATCH', `pages/${pageId}`, {
        properties: { [STATUS_PROP]: { select: { name: status } } }
      }), `Update status to ${status}`
    );
    log(`  Status updated to ${status}`);
  } catch (e) { log(`  Failed to update Notion status: ${e.message}`, 'ERROR'); }
}

// ─── CDP helpers ──────────────────────────────────────────────────────────────

async function checkBrowserAvailable(port) {
  return new Promise(resolve => {
    const req = http.get(`http://127.0.0.1:${port}/json/version`, { timeout: 5000 }, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try { resolve({ ok: true, browser: JSON.parse(d).Browser || 'unknown' }); }
        catch { resolve({ ok: false, error: 'Invalid response' }); }
      });
    });
    req.on('error', () => resolve({ ok: false, error: 'Connection refused' }));
    req.on('timeout', () => { req.destroy(); resolve({ ok: false, error: 'Timeout' }); });
  });
}

function connectCDP(port, tabId) {
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(`ws://127.0.0.1:${port}/devtools/page/${tabId}`, { handshakeTimeout: 10000 });
    let id = 0;
    const pnd = {};

    ws.on('message', raw => {
      const d = JSON.parse(raw.toString());
      if (d.id && pnd[d.id]) { pnd[d.id](d); delete pnd[d.id]; }
      if (d.method === 'Page.javascriptDialogOpening') {
        const msg = d.params?.message || '';
        const isLeave = msg.includes('Changes you made may not be saved') || msg.includes('Leave site') || d.params?.type === 'beforeunload';
        const accept = !isLeave;
        log(`  Dialog: "${msg.substring(0, 50)}..." — ${accept ? 'accepting' : 'dismissing'}`, 'WARN');
        ws.send(JSON.stringify({ id: ++id, method: 'Page.handleJavaScriptDialog', params: { accept } }));
      }
    });

    ws.on('open', () => {
      ws.send(JSON.stringify({ id: ++id, method: 'Page.enable' }));
      resolve({
        eval(expr, timeout = 30000) {
          return new Promise((res, rej) => {
            const myId = ++id;
            const timer = setTimeout(() => { delete pnd[myId]; rej(new Error('eval timeout')); }, timeout);
            pnd[myId] = r => { clearTimeout(timer); res(r); };
            ws.send(JSON.stringify({ id: myId, method: 'Runtime.evaluate', params: { expression: expr } }));
          }).then(r => r.result?.result?.value);
        },
        mouse(x, y) {
          const m1 = ++id, m2 = ++id;
          pnd[m1] = () => {}; pnd[m2] = () => {};
          ws.send(JSON.stringify({ id: m1, method: 'Input.dispatchMouseEvent', params: { type: 'mousePressed', x: Math.round(x), y: Math.round(y), button: 'left', clickCount: 1 } }));
          ws.send(JSON.stringify({ id: m2, method: 'Input.dispatchMouseEvent', params: { type: 'mouseReleased', x: Math.round(x), y: Math.round(y), button: 'left', clickCount: 1 } }));
          return new Promise(r => setTimeout(r, 200));
        },
        type(text) {
          const myId = ++id; pnd[myId] = () => {};
          ws.send(JSON.stringify({ id: myId, method: 'Input.insertText', params: { text } }));
          return new Promise(r => setTimeout(r, 200));
        },
        navigate(url) {
          return new Promise(res => {
            const myId = ++id;
            const timer = setTimeout(() => { delete pnd[myId]; res(); }, 15000);
            pnd[myId] = () => { clearTimeout(timer); res(); };
            ws.send(JSON.stringify({ id: myId, method: 'Page.navigate', params: { url } }));
          });
        },
        key(k, c, kc) {
          const m1 = ++id, m2 = ++id;
          pnd[m1] = () => {}; pnd[m2] = () => {};
          ws.send(JSON.stringify({ id: m1, method: 'Input.dispatchKeyEvent', params: { type: 'keyDown', key: k, code: c, windowsVirtualKeyCode: kc } }));
          ws.send(JSON.stringify({ id: m2, method: 'Input.dispatchKeyEvent', params: { type: 'keyUp', key: k, code: c, windowsVirtualKeyCode: kc } }));
          return new Promise(r => setTimeout(r, 150));
        },
        close() { ws.close(); },
        closeTab() {
          return new Promise(res => {
            const req = http.get(`http://127.0.0.1:${port}/json/close/${tabId}`, { timeout: 5000 }, response => {
              let data = ''; response.on('data', chunk => data += chunk); response.on('end', () => res());
            });
            req.on('error', () => res());
            req.on('timeout', () => { req.destroy(); res(); });
          });
        },
        async setFileInput(filePath) {
          const myId1 = ++id;
          return new Promise((res, rej) => {
            const timer = setTimeout(() => { delete pnd[myId1]; rej(new Error('setFileInput timeout')); }, 10000);
            pnd[myId1] = r => {
              clearTimeout(timer);
              if (r.result?.result?.objectId) {
                const myId2 = ++id;
                pnd[myId2] = () => res();
                ws.send(JSON.stringify({ id: myId2, method: 'DOM.setFileInputFiles', params: { files: [filePath], objectId: r.result.result.objectId } }));
              } else { rej(new Error('File input not found')); }
            };
            ws.send(JSON.stringify({ id: myId1, method: 'Runtime.evaluate', params: { expression: `document.querySelector('input[type="file"]')`, objectGroup: 'file', returnByValue: false } }));
          });
        }
      });
    });

    ws.on('error', reject);
    ws.on('close', () => log('WebSocket closed', 'WARN'));
  });
}

function findCoords(c, expr) {
  return c.eval(expr).then(r => r ? JSON.parse(r) : null).catch(() => null);
}

async function cleanDialogs(c) {
  for (let i = 0; i < 8; i++) { await c.key('Escape', 'Escape', 27); await sleep(200); }
  await sleep(500);
  await c.eval(`(function(){var b=document.querySelectorAll('[role="button"]');for(var i=0;i<b.length;i++){var t=b[i].textContent.trim();if(t==="Don't save"||t==="Discard"){b[i].click()}}})() || ''`);
  await sleep(2000);
}

// ─── Schedule a single post ──────────────────────────────────────────────────

async function schedulePost(c, post, time, dayOffset, idx, total) {
  log(`\n${'='.repeat(60)}`);
  const dayLabel = dayOffset === 0 ? 'today' : `+${dayOffset}d`;
  log(`POST ${idx + 1}/${total} — Schedule for ${time} (${dayLabel}) (${post.blocks.length} parts)`);
  log(`  Title: ${post.title}`);

  if (DRY_RUN) { log('  [DRY RUN] Would schedule this post'); return { success: true, dryRun: true }; }

  try {
    // 1. Open compose
    let composeOpened = false;
    for (let attempt = 0; attempt < 3; attempt++) {
      const r = await c.eval(`(function(){var b=document.querySelectorAll('[role="button"]');for(var i=0;i<b.length;i++){if(b[i].textContent.includes("What's new")||b[i].textContent.includes("What")||b[i].textContent.includes("Что нового")){b[i].click();return 'ok'}}return 'not found'})()`);
      if (r?.startsWith('ok')) {
        await sleep(DELAY.afterCompose);
        if (await c.eval(`document.querySelector('[role="dialog"]') ? 'open' : 'closed'`) === 'open') { composeOpened = true; break; }
      }
      await sleep(2000);
    }
    if (!composeOpened) { log('  ✗ Failed to open compose dialog', 'ERROR'); return { success: false, error: 'Compose not opened' }; }

    // 2a. Upload image if present
    if (post.imageUrl) {
      try {
        const photoBtn = await c.eval(`(function(){var d=document.querySelector('[role="dialog"]');if(!d)return 'no dialog';var els=d.querySelectorAll('[aria-label]');for(var i=0;i<els.length;i++){var label=(els[i].getAttribute('aria-label')||'').toLowerCase();if(label.includes('attach')||label.includes('photo')||label.includes('media')){var cl=els[i].closest('div');if(cl){cl.click();return 'ok'}els[i].dispatchEvent(new MouseEvent('click',{bubbles:true}));return 'ok'}}return 'not found'})()`);
        if (photoBtn?.startsWith('ok')) {
          await sleep(1000);
          let imgPath;
          if (post.imageUrl.startsWith('/') || post.imageUrl.startsWith('~')) {
            imgPath = post.imageUrl.replace(/^~/, process.env.HOME);
          } else if (post.imageUrl.startsWith('http')) {
            imgPath = `/tmp/threads-img-${Date.now()}.jpg`;
            const data = await new Promise((resolve, reject) => {
              (post.imageUrl.startsWith('https') ? https : http).get(post.imageUrl, res => {
                const chunks = []; res.on('data', c => chunks.push(c)); res.on('end', () => resolve(Buffer.concat(chunks)));
              }).on('error', reject);
            });
            fs.writeFileSync(imgPath, data);
          }
          if (imgPath) { await c.setFileInput(imgPath); await sleep(2000); log('  ✓ Image uploaded'); if (imgPath.startsWith('/tmp/')) fs.unlinkSync(imgPath); }
        }
      } catch (e) { log(`  ⚠️ Image upload failed: ${e.message}`, 'WARN'); }
    }

    // 2b. Type first block
    const focus = await c.eval(`(function(){var e=document.querySelector('[contenteditable="true"][role="textbox"]');if(e){e.focus();return 'ok'}return 'not found'})()`);
    if (focus !== 'ok') { log('  ✗ Textbox not found', 'ERROR'); return { success: false, error: 'Textbox not found' }; }
    await sleep(300);
    await c.type(post.blocks[0]);
    await sleep(DELAY.afterType);
    log('  ✓ First block typed');

    // 3. Add thread replies
    for (let i = 1; i < post.blocks.length; i++) {
      const add = await c.eval(`(function(){var b=document.querySelectorAll('[role="button"]');for(var i=0;i<b.length;i++){if(b[i].textContent.trim()==='Add to thread'){b[i].click();return 'ok'}}return 'not found'})()`);
      if (add !== 'ok') { log(`  ⚠️ Could not add thread part ${i + 1}`, 'WARN'); break; }
      await sleep(1500);
      await c.eval(`(function(){var e=document.querySelectorAll('[contenteditable="true"][role="textbox"]');if(e.length>0){e[e.length-1].focus();return 'ok'}return 'not found'})()`);
      await sleep(300);
      await c.type(post.blocks[i]);
      await sleep(300);
      log(`  ✓ Block ${i + 1}/${post.blocks.length} typed`);
    }

    // 4. Click "..." (More)
    let moreClicked = false;
    for (let attempt = 0; attempt < 3; attempt++) {
      const pos = await findCoords(c, `(function(){var d=document.querySelector('[role="dialog"]');if(!d)return null;var b=d.querySelectorAll('[role="button"]');for(var i=0;i<b.length;i++){var btn=b[i];var hasSvg=btn.querySelector('svg');var r=btn.getBoundingClientRect();if(hasSvg&&r.width>0&&r.width<50&&r.height<50&&(btn.textContent.trim()===''||btn.textContent.trim()==='More'||btn.getAttribute('aria-label')==='More')){return JSON.stringify({x:r.x+r.width/2,y:r.y+r.height/2})}}return null})()`);
      if (pos) { await c.mouse(pos.x, pos.y); await sleep(2000); moreClicked = true; break; }
      await sleep(1000);
    }
    if (!moreClicked) { log('  ✗ "..." button not found', 'ERROR'); return { success: false, error: 'More button not found' }; }
    log('  ✓ Clicked "..."');

    // 5. Click Schedule...
    let calendarOpen = false;
    for (let attempt = 0; attempt < 3; attempt++) {
      const pos = await findCoords(c, `(function(){var spans=document.querySelectorAll('span,div');for(var i=0;i<spans.length;i++){var text=(spans[i].innerText||spans[i].textContent||'').trim();if(text==='Schedule...'&&spans[i].offsetWidth>0){var r=spans[i].getBoundingClientRect();if(r.width>0)return JSON.stringify({x:r.x+r.width/2,y:r.y+r.height/2})}}return null})()`);
      if (!pos) { await sleep(1000); continue; }
      await c.mouse(pos.x, pos.y);
      await sleep(3000);
      if (await c.eval(`document.querySelector('input[placeholder="hh"]')?'open':'closed'`) === 'open') { calendarOpen = true; break; }
      await sleep(1000);
    }
    if (!calendarOpen) { log('  ✗ Calendar not opened', 'ERROR'); return { success: false, error: 'Calendar not opened' }; }
    log('  ✓ Calendar opened');

    // 5.5. Select date if dayOffset > 0
    if (dayOffset > 0) {
      await sleep(1500);
      const targetDay = new Date(Date.now() + dayOffset * 86400000).getDate();
      const dateResult = await c.eval(`(function(){var targetDay=${targetDay};var picker=document.querySelector('[role="dialog"]');if(!picker)return'no-picker';var els=picker.querySelectorAll('*');var candidates=[];for(var i=0;i<els.length;i++){var el=els[i];if(el.textContent.trim()===String(targetDay)){var hasChild=false;for(var j=0;j<el.children.length;j++){if(el.children[j].textContent.trim()===String(targetDay)){hasChild=true;break}}if(!hasChild&&el.offsetWidth>0){var r=el.getBoundingClientRect();if(r.width>20&&r.width<80&&r.height>20&&r.height<80)candidates.push({el:el,top:r.top,left:r.left,clickable:el.closest('[role="button"]')||el})}}}if(!candidates.length)return'no-candidates';candidates.sort((a,b)=>(a.top-b.top)||(a.left-b.left));candidates[candidates.length-1].clickable.click();return'clicked-'+targetDay})()`);
      log(`  Date selection (+${dayOffset}d): ${dateResult}`);
      await sleep(1500);
    }

    // 6. Set time
    const [hours, minutes] = time.split(':');
    await c.eval(`(function(){var hh=document.querySelector('input[placeholder="hh"]');var mm=document.querySelector('input[placeholder="mm"]');var setter=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;setter.call(hh,'${hours}');hh.dispatchEvent(new Event('input',{bubbles:true}));hh.dispatchEvent(new Event('change',{bubbles:true}));setter.call(mm,'${minutes}');mm.dispatchEvent(new Event('input',{bubbles:true}));mm.dispatchEvent(new Event('change',{bubbles:true}))})() || ''`);
    await sleep(300);

    // Keyboard input for visual update
    for (const [placeholder, val] of [['hh', hours], ['mm', minutes]]) {
      const pos = await findCoords(c, `(function(){var el=document.querySelector('input[placeholder="${placeholder}"]');if(!el)return null;var r=el.getBoundingClientRect();return JSON.stringify({x:r.x+r.width/2,y:r.y+r.height/2})})()`);
      if (pos) { await c.mouse(pos.x, pos.y); await sleep(100); await c.eval(`document.querySelector('input[placeholder="${placeholder}"]').select()`); await sleep(100); await c.type(val); await sleep(200); }
    }
    const vals = await c.eval(`(function(){return document.querySelector('input[placeholder="hh"]')?.value+':'+document.querySelector('input[placeholder="mm"]')?.value})()`);
    log(`  ✓ Time set: ${vals}`);

    // 7. Click Done
    const donePos = await findCoords(c, `(function(){var b=document.querySelectorAll('[role="button"]');for(var i=0;i<b.length;i++){if(b[i].textContent.trim()==='Done'&&b[i].offsetWidth>0){var r=b[i].getBoundingClientRect();return JSON.stringify({x:r.x+r.width/2,y:r.y+r.height/2})}}return null})()`);
    if (donePos) { await c.mouse(donePos.x, donePos.y); log('  ✓ Clicked Done'); }
    else { log('  ✗ Done not found', 'ERROR'); return { success: false, error: 'Done not found' }; }
    await sleep(2000);

    // 8. Click Schedule
    const schedPos = await findCoords(c, `(function(){var ds=document.querySelectorAll('[role="dialog"]');for(var d=ds.length-1;d>=0;d--){var bs=ds[d].querySelectorAll('[role="button"]');for(var i=0;i<bs.length;i++){if(bs[i].textContent.trim()==='Schedule'&&bs[i].offsetWidth>50){var r=bs[i].getBoundingClientRect();return JSON.stringify({x:r.x+r.width/2,y:r.y+r.height/2})}}}return null})()`);
    if (schedPos) { await c.mouse(schedPos.x, schedPos.y); log(`  ✓ Scheduled for ${time}`); }
    else { log('  ✗ Schedule button not found', 'ERROR'); return { success: false, error: 'Schedule button not found' }; }
    await sleep(DELAY.afterSchedule);

    const dialogsLeft = await c.eval(`document.querySelectorAll('[role="dialog"]').length`);
    if (dialogsLeft > 0) log('  ⚠️ Dialog still open, may have failed', 'WARN');

    return { success: true };
  } catch (e) {
    log(`  ✗ Error: ${e.message}`, 'ERROR');
    return { success: false, error: e.message };
  }
}

// ─── Main ─────────────────────────────────────────────────────────────────────

(async () => {
  log(`\n🔗 ${ACCOUNT} — Threads Scheduler v3.0`);
  log(`  Port: ${PORT}, DB: ${DB_ID}, Status: ${STATUS_PROP}`);
  log(`  Max: ${MAX_POSTS}, Days: ${DAYS}, Timezone: ${TIMEZONE}`);
  if (DRY_RUN) log('  [DRY RUN MODE]');

  // Check browser
  log('\n🌐 Checking browser...');
  const browser = await checkBrowserAvailable(PORT);
  if (!browser.ok) { log(`  ✗ Browser not available: ${browser.error}`, 'ERROR'); process.exit(1); }
  log(`  ✓ Browser: ${browser.browser}`);

  // Time slots
  const slots = getTimeSlotsWithDays(TIMES, DAYS);
  log(`  Slots: ${slots.length} — ${slots.map(s => s.dayOffset ? `${s.time}(+${s.dayOffset}d)` : s.time).join(', ')}`);
  if (!slots.length) { log('  ⚠️ No time slots available'); process.exit(0); }

  // Fetch posts
  log('\n📦 Fetching posts from Notion...');
  let posts;
  try { posts = await getApprovedPosts(); } catch (e) { log(`  ✗ ${e.message}`, 'ERROR'); process.exit(1); }
  log(`  Found ${posts.length} posts`);
  if (!posts.length) { log('  ⚠️ No posts to schedule'); process.exit(0); }

  const count = Math.min(posts.length, slots.length, MAX_POSTS);
  log(`  Will schedule ${count} posts`);

  // Connect CDP
  log('\n🌐 Connecting...');
  let newTab, c;
  try {
    newTab = await new Promise((res, rej) => {
      const req = http.request({ hostname: '127.0.0.1', port: PORT, path: '/json/new?about:blank', method: 'PUT', timeout: 10000 }, r => {
        let d = ''; r.on('data', ch => d += ch); r.on('end', () => { try { res(JSON.parse(d)); } catch (e) { rej(e); } });
      });
      req.on('error', rej); req.on('timeout', () => { req.destroy(); rej(new Error('timeout')); }); req.end();
    });
    c = await connectCDP(PORT, newTab.id);
    globalCDP = c; globalTabId = newTab.id; globalPort = PORT;
    log(`  ✓ Connected, tab: ${newTab.id}`);
  } catch (e) { log(`  ✗ ${e.message}`, 'ERROR'); process.exit(1); }

  await c.navigate('https://www.threads.net');
  await sleep(DELAY.pageLoad);
  log(`  Page: ${await c.eval('document.title')}`);
  try { await cleanDialogs(c); } catch {}

  // Schedule
  let success = 0, failed = 0;
  const scheduled = [], errors = [];

  for (let i = 0; i < count; i++) {
    const post = posts[i], slot = slots[i];
    let result = { success: false };

    for (let attempt = 1; attempt <= POST_ATTEMPTS; attempt++) {
      result = await schedulePost(c, post, slot.time, slot.dayOffset, i, count);
      if (result.success) break;
      if (attempt < POST_ATTEMPTS) {
        log('  🔄 Retrying...'); await cleanDialogs(c); await sleep(3000);
        await c.navigate('https://www.threads.net'); await sleep(DELAY.pageLoad);
        try { await cleanDialogs(c); } catch {}
      }
    }

    if (result.success) {
      success++;
      scheduled.push({ title: post.title, time: slot.time, dayOffset: slot.dayOffset, id: post.id });
      if (!DRY_RUN) await updatePostStatus(post.id, PUBLISHED_VALUE);
      await sleep(DELAY.betweenPosts);
      if ((i + 1) % DELAY.refreshEvery === 0 && i + 1 < count) {
        log('  🔄 Refreshing...'); await c.navigate('https://www.threads.net'); await sleep(DELAY.pageLoad);
        try { await cleanDialogs(c); } catch {}
      }
    } else {
      failed++;
      errors.push({ title: post.title, error: result.error });
      for (let j = 0; j < 5; j++) { await c.key('Escape', 'Escape', 27); await sleep(300); }
      await c.eval(`(function(){var b=document.querySelectorAll('[role="button"]');for(var i=0;i<b.length;i++){var t=b[i].textContent.trim();if(t==="Discard"||t==="Don't save"){b[i].click();return}}})() || ''`);
      await sleep(1500); await cleanDialogs(c); await sleep(2000);
      await c.navigate('https://www.threads.net'); await sleep(DELAY.pageLoad);
      try { await cleanDialogs(c); } catch {}
    }
  }

  // Summary
  log(`\n${'='.repeat(60)}`);
  log(`✅ ${ACCOUNT}: ${success} scheduled, ${failed} failed`);
  for (const s of scheduled) log(`  ✓ ${s.time}${s.dayOffset ? ` (+${s.dayOffset}d)` : ''} — ${s.title}`);
  for (const e of errors) log(`  ✗ ${e.title}: ${e.error}`);

  console.log(`\n__RESULT__${JSON.stringify({ account: ACCOUNT, success, failed, scheduled, errors })}`);

  // Cleanup
  try {
    await cleanDialogs(c); await sleep(1000);
    await c.closeTab(); c.close();
  } catch {}
  process.exit(failed > 0 ? 1 : 0);
})().catch(e => { log(`Fatal: ${e.message}`, 'ERROR'); process.exit(1); });

// Graceful shutdown
async function cleanup() {
  log('Cleanup...');
  if (globalCDP) { try { for (let i = 0; i < 5; i++) { await globalCDP.key('Escape', 'Escape', 27); await sleep(200); } globalCDP.close(); } catch {} }
  if (globalTabId && globalPort) { try { http.get(`http://127.0.0.1:${globalPort}/json/close/${globalTabId}`).on('error', () => {}); } catch {} }
  process.exit(1);
}
process.on('SIGINT', () => cleanup());
process.on('SIGTERM', () => cleanup());
process.on('uncaughtException', e => { log(`Uncaught: ${e.message}`, 'ERROR'); cleanup(); });
process.on('unhandledRejection', e => { log(`Unhandled: ${e}`, 'ERROR'); cleanup(); });
