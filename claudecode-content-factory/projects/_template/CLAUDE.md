# {PROJECT_NAME} — Content Factory

> **Expert:** {EXPERT_NAME}
> **Type:** Multi-direction project
> **Version:** 2.0 (Modular)

---

## Quick Start

1. **Rename this file header** — replace `{PROJECT_NAME}` and `{EXPERT_NAME}`
2. **Fill brand files** → `brand/profile.md`, `brand/voice-style.md`, `brand/audience.md`
3. **Choose your modules** → Enable only modules you need (see Modules table below)
4. **Configure module** → Open `modules/{module}/CLAUDE.md` and fill settings
5. **Generate content** → Use commands from the table below

---

## Modules

Select and configure only the content formats you need:

| Module | Status | Description | Load |
|--------|--------|-------------|------|
| **Threads** | ⬜ Not configured | Text posts for Threads | `modules/threads/CLAUDE.md` |
| **YouTube Long** | ⬜ Not configured | Long-form videos (10+ min) | `modules/youtube-long/CLAUDE.md` |
| **YouTube Shorts** | ⬜ Not configured | Vertical videos (30-60 sec) | `modules/youtube-shorts/CLAUDE.md` |
| **Instagram Carousel** | ⬜ Not configured | Multi-slide posts | `modules/instagram-carousel/CLAUDE.md` |
| **Instagram Reels** | ⬜ Not configured | Vertical video content | `modules/instagram-reels/CLAUDE.md` |
| **Telegram** | ⬜ Not configured | Telegram channel posts | `modules/telegram/CLAUDE.md` |

**Status legend:**
- ⬜ Not configured — module folder exists but not set up
- 🔧 In setup — brand filled, module in progress
- ✅ Active — ready for content generation

**To enable a module:**
1. Open `modules/{module}/CLAUDE.md`
2. Fill required settings (Notion DB, webhooks, templates)
3. Change status from ⬜ to ✅ in table above

---

## Routing

When you request content, Claude loads files in this order:

| Trigger | Module Loaded | Always Load |
|---------|---------------|-------------|
| `threads post [topic]` | modules/threads/ | brand/ + learning/ |
| `youtube script [topic]` | modules/youtube-long/ | brand/ + learning/ |
| `shorts [topic]` | modules/youtube-shorts/ | brand/ + learning/ |
| `carousel [topic]` | modules/instagram-carousel/ | brand/ + learning/ |
| `reels [topic]` | modules/instagram-reels/ | brand/ + learning/ |
| `telegram post [topic]` | modules/telegram/ | brand/ + learning/ |

**Lazy loading:** Only active modules are loaded (~70% token savings).

---

## Architecture

> **This project inherits from:**
> - `skills/{format}/` — Universal methodology (VISP, hooks, formulas)
> - `agents/production/{format}.md` — Commands and workflow
> - `brand/` — Expert voice, audience, constraints
> - `modules/{format}/` — Project-specific integrations

**Loading order:**
```
1. Routing → This file determines which module to load
2. Skill → Universal methodology from skills/
3. Universal Agent → Commands and workflow from agents/production/
4. Brand → Voice, tone, forbidden words from brand/
5. Module → Project-specific settings from modules/{format}/
```

**Result:** `Content = Skill methodology + Expert voice + Module integrations`

---

## Skills — Автоматическая загрузка

Скиллы лежат в `skills/`. Каждый модуль загружает СВОИ скиллы автоматически.

### Маппинг модулей на скиллы

| Модуль | Основной скилл | Дополнительные скиллы |
|--------|----------------|----------------------|
| **threads** | `threads/SKILL.md` + `threads-copywriting.md` + `threads-hooks.md` | `selling-meanings/SKILL.md`, `storytelling/SKILL.md` |
| **telegram** | `telegram/SKILL.md` + `telegram-copywriting.md` + `telegram-hooks.md` | `selling-meanings/SKILL.md`, `storytelling/SKILL.md` |
| **instagram-carousel** | `carousel/SKILL.md` + `carousel-structure.md` + `carousel-types.md` | `nano-banana/SKILL.md`, `selling-meanings/SKILL.md` |
| **instagram-reels** | `reels/SKILL.md` + `reels-methodology.md` | `nano-banana/SKILL.md`, `selling-meanings/SKILL.md`, `heygen/SKILL.md` |
| **youtube-long** | `youtube/SKILL.md` + нужные модули | `storytelling/SKILL.md`, `selling-meanings/SKILL.md` |
| **youtube-shorts** | `reels/SKILL.md` + `reels-methodology.md` | `heygen/SKILL.md`, `selling-meanings/SKILL.md` |

### Универсальные скиллы (подключать по задаче)

| Скилл | Путь | Когда |
|-------|------|-------|
| **selling-meanings** | `selling-meanings/SKILL.md` + модули | Продающие посты, CTA, офферы |
| **storytelling** | `storytelling/SKILL.md` + модули | Истории, кейсы, прогревы |
| **nano-banana** | `nano-banana/SKILL.md` + модули | Генерация изображений, обложки |
| **heygen** | `heygen/SKILL.md` + модули | AI-аватары для видео |
| **launch** | `launch/SKILL.md` | Запуски и прогревы |
| **prompt-engineer** | `prompt-engineer/SKILL.md` | Промпт-инженерия |
| **learning-processor** | `learning-processor/SKILL.md` | Обучение из материалов |

### Порядок загрузки при генерации контента

```
1. РОУТИНГ   → Этот CLAUDE.md определяет модуль по команде
2. СКИЛЛ     → skills/{формат}/SKILL.md (методика)
3. БРЕНД     → brand/ (голос, аудитория)
4. МОДУЛЬ    → modules/{формат}/CLAUDE.md (настройки)
5. ДОП.СКИЛЛ → selling-meanings / storytelling (по типу контента)
6. ОБУЧЕНИЕ  → learning/ (паттерны, анти-паттерны)
```

---

## Brand (Always Load)

Core files loaded for ALL content generation:

| File | Purpose | When to Update |
|------|---------|----------------|
| `brand/profile.md` | Who is the expert (bio, credentials, story) | On project start |
| `brand/voice-style.md` | Voice constraints, forbidden words, tone | When refining voice |
| `brand/audience.md` | Target audience, pain points, demographics | When audience shifts |
| `brand/expertise.md` | Core topics, specializations, unique angle | On positioning change |

---

## Learning Loop

System tracks what works and what doesn't:

| File | Purpose |
|------|---------|
| `learning/approved-patterns.md` | Successful hooks, structures, formats |
| `learning/anti-patterns.md` | What failed, mistakes to avoid |

**Commands:**
- `это сработало` → Add pattern to approved-patterns.md
- `это не сработало` → Add to anti-patterns.md
- `запомни пример` → Save content to module's examples/

---

## Templates

Reusable templates for common content types:

```
templates/
├── post-template.md      # Universal social post structure
├── script-template.md    # YouTube script skeleton
└── email-template.md     # Email sequence format
```

**Usage:** Each module can reference these or have its own in `modules/{module}/templates/`.

---

## Project Structure

```
{PROJECT}/
├── CLAUDE.md                    # This file (router)
│
├── brand/                       # Core identity (always load)
│   ├── profile.md
│   ├── voice-style.md
│   ├── audience.md
│   └── expertise.md
│
├── strategy/
│   ├── positioning.md           # Market position, competitors
│   └── products.md              # Offers, pricing, CTAs
│
├── learning/                    # Accumulated knowledge
│   ├── approved-patterns.md
│   └── anti-patterns.md
│
├── templates/                   # Reusable templates
│   ├── post-template.md
│   └── script-template.md
│
└── modules/                     # Content modules (6 formats)
    ├── threads/
    │   ├── CLAUDE.md
    │   ├── playbook.md
    │   ├── templates/
    │   └── drafts/
    │
    ├── youtube-long/
    │   ├── CLAUDE.md
    │   ├── methodology.md
    │   ├── templates/
    │   └── scripts/
    │
    ├── youtube-shorts/
    │   ├── CLAUDE.md
    │   ├── hooks.md
    │   └── scripts/
    │
    ├── instagram-carousel/
    │   ├── CLAUDE.md
    │   ├── design-rules.md
    │   └── carousels/
    │
    ├── instagram-reels/
    │   ├── CLAUDE.md
    │   ├── visp-rules.md
    │   └── reels/
    │
    └── telegram/
        ├── CLAUDE.md
        ├── strategy.md
        └── posts/
```

---

## Setup Checklist

Before generating content:

### 1. Brand Setup (Required)
- [ ] Fill `brand/profile.md` with expert bio
- [ ] Define voice in `brand/voice-style.md`
- [ ] Describe audience in `brand/audience.md`
- [ ] List expertise in `brand/expertise.md`

### 2. Choose Modules (Select what you need)
- [ ] Threads — Text posts
- [ ] YouTube Long — Long-form videos
- [ ] YouTube Shorts — Vertical shorts
- [ ] Instagram Carousel — Multi-slide posts
- [ ] Instagram Reels — Reels content
- [ ] Telegram — Channel posts

### 3. Configure Each Active Module
- [ ] Open `modules/{module}/CLAUDE.md`
- [ ] Fill module-specific settings
- [ ] Set up integrations (Notion, n8n, webhooks)
- [ ] Update status in Modules table above

### 4. Optional Enhancements
- [ ] Fill `strategy/positioning.md`
- [ ] Add `strategy/products.md` with offers
- [ ] Create templates in `templates/`

---

## Commands Reference

### Content Generation

| Command | Module | Action |
|---------|--------|--------|
| `threads post [topic]` | Threads | Generate single Threads post |
| `youtube script [topic]` | YouTube Long | Generate video script |
| `shorts [topic]` | YouTube Shorts | Generate shorts script |
| `carousel [topic]` | Instagram Carousel | Generate carousel content |
| `reels [topic]` | Instagram Reels | Generate reels script |
| `telegram post [topic]` | Telegram | Generate Telegram post |

### Learning

| Command | Action |
|---------|--------|
| `это сработало` | Add to approved-patterns.md |
| `это не сработало` | Add to anti-patterns.md |
| `запомни пример` | Save to module examples/ |

### Analysis

| Command | Action |
|---------|--------|
| `инсайты` | Analyze metrics, extract patterns |
| `что сработало` | Review approved patterns |
| `разбери метрики` | Deep metrics analysis |

---

## Integration Options

### Notion
Add Notion database IDs to module CLAUDE.md files:
```markdown
## Notion Integration

- **Database ID:** `{your_database_id}`
- **Status field:** Draft → Review → Published
- **Auto-publish:** Yes/No
```

### n8n Webhooks
Configure webhooks in module CLAUDE.md for automation:
```markdown
## n8n Webhook

- **URL:** `{your_webhook_url}`
- **Trigger:** On content generation
- **Action:** Auto-add to Notion
```

### Analytics
Track performance in `modules/{module}/analytics/`:
```
analytics/
├── metrics-YYYY-MM.md    # Monthly metrics
└── insights.md           # Key learnings
```

---

## Maintenance

### Weekly Review
1. Review `learning/approved-patterns.md`
2. Update `brand/voice-style.md` if voice evolved
3. Check module metrics in `modules/{module}/analytics/`
4. Archive old drafts to keep folders clean

### Monthly Audit
1. Update `brand/audience.md` if targeting shifted
2. Review `strategy/positioning.md`
3. Clean up unused templates
4. Archive completed content

---

## Support

**Documentation:**
- [docs/USER-GUIDE.md](../../docs/USER-GUIDE.md) — Full setup guide
- [docs/inheritance-architecture.md](../../docs/inheritance-architecture.md) — How agents work
- [structure-readme.md](../../structure-readme.md) — System architecture

**Modules:**
- Each module has its own README in `modules/{module}/README.md`

**Getting Help:**
- Read module-specific CLAUDE.md for detailed setup
- Check [docs/troubleshooting.md](../../docs/troubleshooting.md) for common issues
- Review [agents/README.md](../../agents/README.md) for agent guide

---

## Version

**Template Version:** 2.0 (Modular)
**Last Updated:** 2026-01-22
**Architecture:** Inheritance-based (Skills → Agents → Projects)

---

*Фабрика Контента v2.0*  
*Макс Галсон • [galson.pro](https://galson.pro)*
