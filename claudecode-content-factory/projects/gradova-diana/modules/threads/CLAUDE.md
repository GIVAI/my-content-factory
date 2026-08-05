# Threads Module — {PROJECT}

> **Platform:** Threads (Meta)
> **Format:** Text posts (max 500 characters)
> **Module Status:** ⬜ Not configured

---

## Quick Setup

1. **Fill integration settings** below (Notion DB, n8n webhook)
2. **Configure playbook.md** with your specific formats
3. **Update module status** to ✅ in main CLAUDE.md
4. **Start generating:** `threads post [topic]`

---

## Architecture

> **This module inherits from:**
> - `skills/threads/` — Threads methodology (VISP, hooks, techniques)
> - `agents/production/threads.md` — Commands and workflow
> - `../../brand/` — Expert voice and constraints

**Loading order:**
```
1. User: "threads post about AI"
2. Main router (../../CLAUDE.md) → routes to this module
3. Skill (skills/threads/) → methodology
4. Universal agent (agents/production/threads.md) → commands
5. Brand (../../brand/) → voice
6. This file → project integrations
```

---

## Skills — Автоматическая загрузка

### Скиллы (из skills/)

| Скилл | Путь | Когда загружать |
|-------|------|-----------------|
| **threads** | `threads/SKILL.md` + `threads-copywriting.md` + `threads-hooks.md` | ВСЕГДА при написании поста |
| **selling-meanings** | `selling-meanings/SKILL.md` + нужный модуль | Продающие посты, CTA, офферы |
| **storytelling** | `storytelling/SKILL.md` + `slippery-slide.md` | Истории, кейсы, личный опыт |

### Дополнительные модули threads (по задаче)

| Задача | Модуль |
|--------|--------|
| Стратегия контент-плана | `threads/threads-strategy.md` |
| Контент-план | `threads/threads-content-plan.md` |
| Вовлечение аудитории | `threads/threads-engagement.md` |
| Аналитика | `threads/threads-analytics.md` |
| Исследование ниши | `threads/threads-research.md` |

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
1. ВСЕГДА:  threads/SKILL.md + threads-copywriting.md + threads-hooks.md
2. ВСЕГДА:  brand/ (голос, аудитория)
3. ПО ТИПУ: selling-meanings (продажа) / storytelling (история)
4. ОБУЧЕНИЕ: learning/approved-patterns.md + anti-patterns.md
```

---

## Module Purpose

**What this module adds to the system:**
- Notion integration (optional)
- n8n webhook automation (optional)
- Project-specific post formats
- Drafts management workflow

**What it does NOT duplicate:**
- ❌ VISP technique (in skill)
- ❌ Hook formulas (in skill)
- ❌ Voice and tone (in brand/)
- ❌ Commands (in universal agent)

---

## Integration Settings

### Notion (Optional)

If using Notion for content management:

**Database ID:** `{your_notion_database_id}`

**Fields mapping:**
```
Content (Text) → Post text
Platform (Select) → "Threads"
Status (Select) → "Draft" / "Review" / "Published"
Published Date (Date) → Auto-fill on publish
Metrics (Number) → Likes, comments, shares
```

**Auto-publish:** ☐ Yes / ☐ No

### n8n Webhook (Optional)

If using n8n for automation:

**Webhook URL:** `{your_n8n_webhook_url}`

**Trigger:** On content generation
**Action:** Auto-add to Notion database
**Payload:**
```json
{
  "text": "{post_content}",
  "platform": "Threads",
  "status": "Draft",
  "generated_at": "{timestamp}"
}
```

---

## Workflow

### Phase 1: Generate
```
User: "threads post about {topic}"

Claude:
1. Loads methodology from skill
2. Loads voice from brand/
3. Loads formats from playbook.md
4. Generates post
5. (Optional) Sends to Notion/n8n
```

### Phase 2: Review
```
Location: drafts/{date}.md

User reviews post:
- Edit in file
- Check audience fit
- Verify voice compliance
```

### Phase 3: Publish
```
User publishes to Threads

Post-publish:
- Move to published/ folder
- Track metrics in analytics/
- Update learning/approved-patterns.md if successful
```

---

## Commands

| Command | Action |
|---------|--------|
| `threads post [topic]` | Generate single post |
| `threads series [topic]` | Generate 5-7 post series |
| `threads analyze [screenshot]` | Analyze competitor post |
| `threads review` | Review drafts/ folder |

---

## Post Formats

Configure your preferred formats in `playbook.md`:

**Default formats:**
1. **Story** — Personal experience or client story
2. **List** — Numbered tips or insights
3. **Hook + Value** — Attention-grabbing opener + quick value
4. **Question** — Engaging question + perspective
5. **Myth-busting** — "Everyone thinks X, but Y"

**Threads-specific constraints:**
- Max 500 characters
- 1-2 line breaks max
- Soft CTAs only ("What's your experience?")
- No hard product links (use bio link)

---

## File Structure

```
modules/threads/
├── CLAUDE.md           # This file
├── playbook.md         # Post formats and rules
├── templates/          # Reusable post templates
│   ├── story.md
│   ├── list.md
│   └── hook-value.md
├── drafts/             # Generated posts awaiting review
│   └── YYYY-MM-DD.md
├── published/          # Archive of published posts
│   └── YYYY-MM/
└── analytics/          # Performance tracking
    ├── metrics-YYYY-MM.md
    └── insights.md
```

---

## Content Guidelines

### DO:
- ✅ Start with strong hook (first 10 words)
- ✅ One clear idea per post
- ✅ Line breaks for readability (1-2 max)
- ✅ End with engagement question
- ✅ Use voice from brand/voice-style.md

### DON'T:
- ❌ Generic advice
- ❌ Multiple ideas in one post
- ❌ Salesy language
- ❌ Links (use bio)
- ❌ Hashtags (Threads doesn't need them)

---

## Learning Loop

After posting:

**If post performed well:**
```
Command: "это сработало"

Action: Claude saves pattern to ../../learning/approved-patterns.md

Track: Hook type, topic, engagement
```

**If post underperformed:**
```
Command: "это не сработало"

Action: Claude saves to ../../learning/anti-patterns.md

Analyze: Why it failed, what to avoid
```

---

## Metrics Tracking

### Key Metrics (track in analytics/)

| Metric | What to Track | Benchmark |
|--------|---------------|-----------|
| **Likes** | Total likes per post | Baseline: {YOUR_AVG} |
| **Comments** | Engagement quality | Goal: 5% of likes |
| **Shares** | Virality indicator | Goal: 2% of likes |
| **Saves** | Value indicator | Goal: 10% of likes |
| **Profile Visits** | Interest indicator | Track trend |

### Monthly Review

At month end, update `analytics/metrics-YYYY-MM.md`:
- Top 5 posts (by engagement)
- Bottom 5 posts (learn from)
- Pattern insights
- Next month adjustments

---

## Module Maintenance

### Weekly
- [ ] Review drafts/ folder
- [ ] Archive published posts to published/YYYY-MM/
- [ ] Update playbook.md with new patterns

### Monthly
- [ ] Full metrics review in analytics/
- [ ] Update ../../learning/ with insights
- [ ] Clean up old drafts

---

## Troubleshooting

### "Posts feel generic"
→ Check brand/voice-style.md — use specific language
→ Check brand/expertise.md — lean into unique angle

### "Low engagement"
→ Check playbook.md — test different formats
→ Check analytics/ — what worked before?

### "Notion not syncing"
→ Verify Database ID
→ Check n8n webhook URL
→ Test with manual curl

---

## Related Files

- [[../../brand/voice-style|Voice & Style]] — How to write
- [[../../brand/audience|Audience]] — Who you write for
- [[playbook|Playbook]] — Formats and rules
- [[../../learning/approved-patterns|Approved Patterns]] — What works
- [[skills/threads/SKILL|Threads Skill]] — Full methodology

---

## Version

**Module Version:** 2.0
**Last Updated:** 2026-01-22
**Status:** ⬜ Not configured (update after setup)

---

*Threads Module — Inherits methodology, adds project integrations*
