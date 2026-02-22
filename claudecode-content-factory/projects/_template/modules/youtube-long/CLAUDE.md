# YouTube Long Module — {PROJECT}

> **Platform:** YouTube
> **Format:** Long-form videos (10-20+ minutes)
> **Module Status:** ⬜ Not configured

---

## Quick Setup

1. **Fill channel settings** below (Channel ID, upload settings)
2. **Configure methodology.md** with your niche adaptations
3. **Update module status** to ✅ in main CLAUDE.md
4. **Start generating:** `youtube script [topic]`

---

## Architecture

> **This module inherits from:**
> - `skills/youtube/` — YouTube methodology (VHF, TOP-5, retention)
> - `agents/production/youtube.md` — Commands and pipeline
> - `../../brand/` — Expert voice and constraints

**Loading order:**
```
1. User: "youtube script about {topic}"
2. Main router → this module
3. Skill → methodology (VHF, hooks, structure)
4. Universal agent → pipeline stages
5. Brand → voice, expertise
6. This file → channel-specific settings
```

---

## Skills — Автоматическая загрузка

### Скиллы (из skills/)

| Скилл | Путь | Когда загружать |
|-------|------|-----------------|
| **youtube** | `youtube/SKILL.md` + нужные модули | ВСЕГДА при создании сценария |
| **storytelling** | `storytelling/SKILL.md` + `slippery-slide.md` | Истории, кейсы, нарративная структура |
| **selling-meanings** | `selling-meanings/SKILL.md` + нужный модуль | Продающие вставки, CTA, офферы |

### Модули youtube (по задаче)

| Задача | Модуль |
|--------|--------|
| Структура сценария | `youtube/youtube-structure.md` |
| ДНК сценария | `youtube/youtube-script-dna.md` |
| Хуки и открывашки | `youtube/youtube-hooks.md` |
| Удержание аудитории | `youtube/youtube-retention.md` |
| Заголовки | `youtube/youtube-titles.md` |
| Обложки | `youtube/youtube-thumbnails.md` |
| CTA-вставки | `youtube/youtube-cta.md` |
| SEO оптимизация | `youtube/youtube-seo.md` |
| Исследование темы | `youtube/youtube-research.md` |
| Съёмка | `youtube/youtube-filming.md` |
| Монтаж | `youtube/youtube-editing.md` |
| Публикация | `youtube/youtube-publishing.md` |
| Настройка канала | `youtube/youtube-channel-setup.md` |
| AI-промпты для видео | `youtube/youtube-ai-prompts.md` |

### Модули storytelling (по задаче)

| Задача | Модуль |
|--------|--------|
| Скользкая горка (затягивающий текст) | `storytelling/slippery-slide.md` |
| Психологические триггеры | `storytelling/psychological-triggers.md` |
| Продающая статья | `storytelling/selling-article.md` |

### Модули selling-meanings (по задаче)

| Задача | Модуль |
|--------|--------|
| Вытащить смыслы из текста | `selling-meanings/extraction.md` |
| Усилить текст продающими элементами | `selling-meanings/amplification.md` |
| Формулы копирайтинга (PAS, AIDA) | `selling-meanings/formulas.md` |
| Офферы по Хормози | `selling-meanings/hormozi-offers.md` |

### Порядок загрузки при создании сценария

```
1. ВСЕГДА:  youtube/SKILL.md + youtube-structure.md + youtube-hooks.md
2. ВСЕГДА:  brand/ (голос, экспертиза)
3. НАРРАТИВ: storytelling/SKILL.md (истории, кейсы)
4. ПО ТИПУ: selling-meanings (продающие вставки, CTA)
5. ДОВОДКА:  youtube/youtube-seo.md + youtube-titles.md + youtube-thumbnails.md
6. ОБУЧЕНИЕ: learning/approved-patterns.md + anti-patterns.md
```

---

## Module Purpose

**What this module adds:**
- Channel-specific settings (branding, SEO)
- Custom script templates
- Production workflow (filming, editing)
- Publishing checklist

**What it does NOT duplicate:**
- ❌ VHF formula (in skill)
- ❌ Hook patterns (in skill)
- ❌ TOP-5 structure (in skill)
- ❌ Pipeline stages (in universal agent)

---

## Channel Settings

### Channel Info

**Channel Name:** `{Your Channel Name}`
**Channel ID:** `{your_channel_id}`
**Target Length:** {10-15 / 15-20 / 20-30} minutes
**Upload Schedule:** {Day/frequency}

### Branding

**Intro:** ☐ Use intro (specify file)
**Outro:** ☐ Use outro (specify file)
**End Screen:** ☐ Subscribe + Video suggestion
**Watermark:** ☐ Channel logo (specify file)

### SEO Defaults

**Primary Keywords:** {keyword 1}, {keyword 2}, {keyword 3}
**Default Tags:** {tag1}, {tag2}, {tag3}
**Playlists:** {playlist names}

---

## Production Pipeline

### Stage 1: Script (Use this module)
```
Command: "youtube script [topic]"

Output: scripts/YYYY-MM-DD-{title}.md
Contains: Full script with TOP-5 structure, CTAs, open loops
```

### Stage 2: Pre-production
```
From script, create:
- Filming notes (key points, B-roll needs)
- Props list
- Location requirements
```

### Stage 3: Filming
```
Record according to filming notes

Capture:
- A-roll (main content)
- B-roll (supporting visuals)
- Thumbnail photos (3-5 options)
```

### Stage 4: Editing
```
Edit in preferred software

Follow:
- Pacing guidelines from methodology.md
- Brand style (cuts, transitions, effects)
- Retention tactics (pattern breaks, hooks)
```

### Stage 5: Packaging
```
Create:
- Title (5-7 words, keyword-rich)
- Thumbnail (use thumbnail generator agent)
- Description (SEO optimized)
- Tags (15-20 relevant)
- Timestamps (chapters)
```

### Stage 6: Publishing
```
Upload with settings:
- Visibility: Public / Scheduled
- Category: {your default category}
- End screens: Auto-apply template
- Comments: Enabled / Moderated
```

---

## Commands

| Command | Action |
|---------|--------|
| `youtube script [topic]` | Generate full script |
| `youtube hook [topic]` | Generate hook variations |
| `youtube package [script]` | Generate title/description/tags |
| `youtube review [script]` | Check script against VHF |

---

## Script Structure (TOP-5)

### Block 1: Opening (0:00-2:00)
- **Hook** (0:00-0:15): VHF-loaded opener
- **Validation** (0:15-0:30): Establish authority
- **Problem Setup** (0:30-2:00): Agitate + promise

### Block 2: Content (2:00-15:00)
- **Chapter 1**: First major insight
- **CTA: Like** (after emotional peak)
- **Chapter 2**: Second insight
- **Chapter 3**: Third insight
- **CTA: Product** (50-60% mark, optional)
- **Chapters 4-5**: Additional insights

### Block 3: Climax (15:00-17:00)
- **Biggest Value**: Most important insight saved for end
- **Complete Protocol**: Step-by-step implementation

### Block 4: Closing (17:00-18:00)
- **Recap**: 3 key points
- **Action Step**: What to do today
- **CTA: Subscribe**: With next video tease

---

## File Structure

```
modules/youtube-long/
├── CLAUDE.md           # This file
├── methodology.md      # Niche-specific adaptations
├── templates/          # Script templates
│   ├── tutorial.md
│   ├── case-study.md
│   └── deep-dive.md
├── scripts/            # Generated scripts
│   ├── YYYY-MM-DD-title.md
│   └── archive/
├── filming/            # Production notes
│   └── filming-checklist.md
└── analytics/          # Performance tracking
    ├── video-metrics.md
    └── insights.md
```

---

## Content Guidelines

### DO:
- ✅ Hook grabs in first 3 seconds
- ✅ VHF elements throughout (Value, Intrigue, Urgency, Relevance)
- ✅ Mini-hooks every 2-3 minutes
- ✅ Specific protocols with exact steps
- ✅ Strong close, no trailing off

### DON'T:
- ❌ Greetings at start ("Hey guys, welcome back")
- ❌ Rambling without value
- ❌ Generic advice without specifics
- ❌ Weak CTAs
- ❌ Leaving open loops unclosed

---

## AI Voiceover Formatting

If using AI voices (HeyGen, ElevenLabs):

### DO:
- ✅ Numbers as words (500 → five hundred)
- ✅ Spell out abbreviations (CEO → C E O)
- ✅ Short sentences (under 20 words)
- ✅ Simple punctuation (, . ?)

### DON'T:
- ❌ Quotation marks (" ' « »)
- ❌ Dashes (— –)
- ❌ Ellipsis (...)
- ❌ Parentheses ()
- ❌ Percent symbol (% → "percent")

---

## Learning Loop

### After Publishing

**Track in analytics/video-metrics.md:**
- CTR (Click-Through Rate)
- AVD (Average View Duration)
- Retention graph shape
- Engagement (likes, comments, shares)
- Subscriber gain

**If video performed well:**
```
Command: "это сработало"

Save patterns:
- Hook type
- Topic angle
- Structure variations
- CTA placement
```

**If video underperformed:**
```
Command: "это не сработало"

Analyze:
- Where did viewers drop off?
- Was hook weak?
- Value delivery slow?
- CTA placement off?
```

---

## Metrics Benchmarks

| Metric | Good | Great | Viral |
|--------|------|-------|-------|
| **CTR** | 4-6% | 6-10% | 10%+ |
| **AVD** | 40-50% | 50-60% | 60%+ |
| **Watch Time** | {your baseline} | +50% | +100% |
| **Engagement** | 4-6% | 6-8% | 8%+ |
| **Sub Rate** | 1-2% | 2-4% | 4%+ |

*Adjust benchmarks based on your niche and channel size*

---

## Module Maintenance

### Per Video
- [ ] Script generated and reviewed
- [ ] Filmed and edited
- [ ] Packaged (title/thumbnail/SEO)
- [ ] Published with checklist

### Weekly
- [ ] Review analytics for latest videos
- [ ] Update methodology.md with learnings
- [ ] Plan next week's content

### Monthly
- [ ] Full channel audit
- [ ] Update benchmarks
- [ ] Archive old scripts
- [ ] Update learning/approved-patterns.md

---

## Troubleshooting

### "Low CTR (below 4%)"
→ Check title + thumbnail
→ Review title formulas in skill
→ Test A/B variations

### "High drop-off in first 30 seconds"
→ Hook too weak
→ Review VHF formula
→ Study high-retention openings

### "Good start, poor retention after 50%"
→ Value delivery too slow
→ Not enough mini-hooks
→ Open loops closed too early

---

## Related Files

- [[../../brand/voice-style|Voice & Style]] — Delivery tone
- [[../../brand/expertise|Expertise]] — Topic authority
- [[methodology|Methodology]] — Niche adaptations
- [[skills/youtube/SKILL|YouTube Skill]] — Full methodology
- [[../../templates/script-template|Script Template]] — Universal structure

---

## Version

**Module Version:** 2.0
**Last Updated:** 2026-01-22
**Status:** ⬜ Not configured

---

*YouTube Long Module — Inherits methodology, adds channel specifics*
