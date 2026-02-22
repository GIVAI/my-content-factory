# YouTube Shorts Module — {PROJECT}

> **Platform:** YouTube Shorts
> **Format:** Vertical videos (30-60 seconds)
> **Module Status:** ⬜ Not configured

---

## Architecture

> **Inherits from:**
> - `skills/youtube/` → Shorts methodology, hooks
> - `agents/production/vertical-content.md` → Commands, VISP formula
> - `../../brand/` → Voice, expertise

---

## Skills — Автоматическая загрузка

### Скиллы (из skills/)

| Скилл | Путь | Когда загружать |
|-------|------|-----------------|
| **reels** | `reels/SKILL.md` + `reels-methodology.md` | ВСЕГДА при создании shorts |
| **heygen** | `heygen/SKILL.md` + `heygen-rules.md` + `heygen-motion.md` | AI-аватар для видео (озвучка, движение) |
| **selling-meanings** | `selling-meanings/SKILL.md` + нужный модуль | Продающие shorts, CTA, офферы |

### Специфичный модуль YouTube Shorts

| Задача | Модуль |
|--------|--------|
| Методика Shorts | `youtube/youtube-shorts.md` |

### Модули selling-meanings (по задаче)

| Задача | Модуль |
|--------|--------|
| Вытащить смыслы из текста | `selling-meanings/extraction.md` |
| Усилить текст продающими элементами | `selling-meanings/amplification.md` |
| Формулы копирайтинга (PAS, AIDA) | `selling-meanings/formulas.md` |
| Психология продаж | `selling-meanings/psychology.md` |

### Порядок загрузки при создании shorts

```
1. ВСЕГДА:  reels/SKILL.md + reels-methodology.md
2. ВСЕГДА:  youtube/youtube-shorts.md (специфика платформы)
3. ВСЕГДА:  brand/ (голос, экспертиза)
4. АВАТАР:  heygen/SKILL.md (если AI-аватар)
5. ПО ТИПУ: selling-meanings (продающий shorts)
6. ОБУЧЕНИЕ: learning/approved-patterns.md + anti-patterns.md
```

---

## Quick Setup

1. Fill channel settings (same as YouTube Long if shared channel)
2. Configure `hooks.md` with tested hook patterns
3. Update status to ✅ in main CLAUDE.md
4. Generate: `shorts [topic]`

---

## Channel Settings

**Channel:** `{Same as YouTube Long / Separate}`
**Upload Frequency:** `{Daily / 3x week / Weekly}`
**Optimal Length:** 30-45 seconds (under 60 sec)
**Aspect Ratio:** 9:16 (vertical)

---

## Script Structure

### Hook (0-3 sec)
**Goal:** Stop scroll

**Patterns:**
- Bold claim: "{Result} in {timeframe}"
- Question: "Why is {surprising thing}?"
- Pattern break: Unexpected visual + text

### Problem (3-10 sec)
**Goal:** Relate to viewer

"Most people {mistake}. Here's why that's wrong."

### Solution (10-50 sec)
**Goal:** Deliver one clear tactic

```
Instead, do this:
1. {Step}
2. {Step}
3. {Result}
```

### CTA (50-60 sec)
**Goal:** Engagement

"Follow for more. Part 2 tomorrow."

---

## Commands

| Command | Action |
|---------|--------|
| `shorts [topic]` | Generate shorts script |
| `shorts series [topic]` | Generate 3-part series |
| `shorts hook [topic]` | Generate hook variations |

---

## File Structure

```
modules/youtube-shorts/
├── CLAUDE.md           # This file
├── hooks.md            # Tested hook patterns
├── scripts/            # Generated scripts
│   └── YYYY-MM-DD/
└── analytics/
    └── shorts-metrics.md
```

---

## Content Guidelines

**DO:**
- ✅ Hook in first 1 second
- ✅ One idea per short
- ✅ Fast pacing (no dead air)
- ✅ Bold text overlays
- ✅ Pattern breaks every 10 sec

**DON'T:**
- ❌ Slow intros
- ❌ Complex explanations
- ❌ Multiple topics
- ❌ Weak CTAs

---

## Metrics Benchmarks

| Metric | Good | Great | Viral |
|--------|------|-------|-------|
| **Views** | 1000+ | 10K+ | 100K+ |
| **Watch %** | 40-60% | 60-80% | 80%+ |
| **Likes** | 4-6% | 6-10% | 10%+ |
| **Comments** | 0.5-1% | 1-2% | 2%+ |

---

## Related Files

- [[hooks|Hooks]] — Hook patterns
- [[../../templates/script-template|Script Template]] — Shorts section
- [[skills/youtube/youtube-shorts|Shorts Skill]]

---

**Module Version:** 2.0 | **Status:** ⬜ Not configured
