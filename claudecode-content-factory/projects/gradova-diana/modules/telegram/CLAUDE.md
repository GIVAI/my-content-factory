# Telegram Module — {PROJECT}

> **Platform:** Telegram Channel
> **Format:** Text posts (no character limit)
> **Module Status:** ⬜ Not configured

---

## Architecture

> **Inherits from:**
> - `skills/telegram/` → Telegram best practices
> - `agents/production/threads.md` → Content structure (adapted for longer form)
> - `../../brand/` → Voice, expertise

---

## Skills — Автоматическая загрузка

### Скиллы (из skills/)

| Скилл | Путь | Когда загружать |
|-------|------|-----------------|
| **telegram** | `telegram/SKILL.md` + `telegram-copywriting.md` + `telegram-hooks.md` | ВСЕГДА при написании поста |
| **selling-meanings** | `selling-meanings/SKILL.md` + нужный модуль | Продающие посты, CTA, офферы |
| **storytelling** | `storytelling/SKILL.md` + `slippery-slide.md` | Истории, кейсы, личный опыт |

### Модули selling-meanings (по задаче)

| Задача | Модуль |
|--------|--------|
| Вытащить смыслы из текста | `selling-meanings/extraction.md` |
| Усилить текст продающими элементами | `selling-meanings/amplification.md` |
| Формулы копирайтинга (PAS, AIDA) | `selling-meanings/formulas.md` |
| Офферы по Хормози | `selling-meanings/hormozi-offers.md` |
| Психология продаж | `selling-meanings/psychology.md` |

### Модули storytelling (по задаче)

| Задача | Модуль |
|--------|--------|
| Скользкая горка (затягивающий текст) | `storytelling/slippery-slide.md` |
| Психологические триггеры | `storytelling/psychological-triggers.md` |
| Продающая статья | `storytelling/selling-article.md` |

### Порядок загрузки при написании поста

```
1. ВСЕГДА:  telegram/SKILL.md + telegram-copywriting.md + telegram-hooks.md
2. ВСЕГДА:  brand/ (голос, аудитория)
3. ПО ТИПУ: selling-meanings (продажа) / storytelling (история)
4. ОБУЧЕНИЕ: learning/approved-patterns.md + anti-patterns.md
```

---

## Quick Setup

1. Fill channel settings (channel link, posting schedule)
2. Configure `strategy.md` with content mix and CTAs
3. Update status to ✅ in main CLAUDE.md
4. Generate: `telegram post [topic]`

---

## Channel Settings

**Channel Name:** `{Your Channel Name}`
**Channel Link:** `t.me/{your_channel}`
**Subscriber Count:** `{current count}`
**Posting Frequency:** `{Daily / 3x week / Weekly}`
**Subscription:** ☐ Free / ☐ Paid (${PRICE}/month)

---

## Post Structure

### Hook (1 sentence)
**Goal:** Grab attention

Bold opener or provocative question

### Context (2-3 sentences)
**Goal:** Set up value

Why this matters, who it's for

### Value (Main body)
**Goal:** Deliver insight

**Options:**
- Story format (narrative)
- List format (bullets)
- Framework (numbered steps)
- Case study (example + lesson)

### Takeaway (1-2 sentences)
**Goal:** Actionable conclusion

What to do with this information

### CTA (Optional)
**Goal:** Drive action

- Soft: "What's your experience?"
- Hard: "Link to full course: {URL}"

---

## Commands

| Command | Action |
|---------|--------|
| `telegram post [topic]` | Generate single post |
| `telegram series [topic]` | Generate 5-7 post series |
| `telegram newsletter` | Generate weekly digest |

---

## File Structure

```
modules/telegram/
├── CLAUDE.md           # This file
├── strategy.md         # Content mix, CTAs
├── posts/              # Generated posts
│   ├── YYYY-MM-DD.md
│   └── archive/
└── analytics/
    └── channel-metrics.md
```

---

## Content Guidelines

**DO:**
- ✅ Strong first line (shows in preview)
- ✅ Line breaks for readability (every 2-3 lines)
- ✅ Mix of formats (stories, lists, frameworks)
- ✅ Bold key phrases for scanning
- ✅ Links when relevant (Telegram-friendly)

**DON'T:**
- ❌ Walls of text (use line breaks)
- ❌ Generic advice
- ❌ Too many posts per day (fatigue)
- ❌ Only promotional content

---

## Content Mix

| Content Type | Percentage | Purpose |
|--------------|------------|---------|
| **Value posts** | 70% | Free insights, tips, stories |
| **Product CTAs** | 20% | Paid offers, services |
| **Personal** | 10% | Behind-scenes, updates |

---

## Formatting

**Bold:** Use `**bold**` for key phrases
**Italic:** Use `*italic*` for emphasis
**Code:** Use \`code\` for formulas/terms
**Links:** Use [text](URL) for clickable links
**Lists:** Use • or – for bullet points

---

## Metrics Benchmarks

| Metric | Good | Great | Viral |
|--------|------|-------|-------|
| **Views** | 30-50% of subs | 50-70% | 70%+ |
| **Reactions** | 3-5% | 5-10% | 10%+ |
| **Forwards** | 1-3% | 3-5% | 5%+ |
| **Link Clicks** | 5-10% of views | 10-20% | 20%+ |

---

## Subscriber Growth

**Track in analytics/channel-metrics.md:**
- New subscribers per week
- Unsubscribe rate
- Best-performing posts (by views)
- Link click patterns

**Growth tactics:**
- Cross-promote from other platforms
- Collaborate with channels
- Exclusive content for subscribers
- Value-first approach

---

## Related Files

- [[strategy|Strategy]] — Content mix, CTAs
- [[../../brand/voice-style|Voice]] — Writing style
- [[../../templates/post-template|Post Template]] — Universal structure

---

**Module Version:** 2.0 | **Status:** ⬜ Not configured
