# Instagram Carousel Module — {PROJECT}

> **Platform:** Instagram
> **Format:** Multi-slide posts (2-10 slides)
> **Module Status:** ⬜ Not configured

---

## Architecture

> **Inherits from:**
> - `skills/carousel/` → Carousel methodology, design rules
> - `agents/production/threads.md` → Content structure (adapted)
> - `../../brand/` → Voice, visual style

---

## Skills — Автоматическая загрузка

### Скиллы (из skills/)

| Скилл | Путь | Когда загружать |
|-------|------|-----------------|
| **carousel** | `carousel/SKILL.md` + `carousel-structure.md` + `carousel-types.md` | ВСЕГДА при создании карусели |
| **nano-banana** | `nano-banana/SKILL.md` + нужный модуль | Генерация слайдов, обложек, визуалов |
| **selling-meanings** | `selling-meanings/SKILL.md` + нужный модуль | Продающие карусели, CTA, офферы |

### Дополнительные модули carousel (по задаче)

| Задача | Модуль |
|--------|--------|
| CTA-слайды | `carousel/carousel-cta.md` |
| Промпты для генерации слайдов | `carousel/carousel-prompts.md` |

### Модули nano-banana (по задаче)

| Задача | Модуль |
|--------|--------|
| Реалистичные фото | `nano-banana/nano-banana-realism.md` |
| Identity Kit (сохранение лица) | `nano-banana/nano-banana-identity-kit.md` |
| Словарь промптов | `nano-banana/nano-banana-vocabulary.md` |
| Обложки/thumbnails | `nano-banana/nano-banana-thumbnails.md` |
| Примеры промптов | `nano-banana/nano-banana-examples.md` |
| Идеи для визуалов | `nano-banana/nano-banana-ideas.md` |

### Модули selling-meanings (по задаче)

| Задача | Модуль |
|--------|--------|
| Вытащить смыслы из текста | `selling-meanings/extraction.md` |
| Усилить текст продающими элементами | `selling-meanings/amplification.md` |
| Формулы копирайтинга (PAS, AIDA) | `selling-meanings/formulas.md` |
| Офферы по Хормози | `selling-meanings/hormozi-offers.md` |

### Порядок загрузки при создании карусели

```
1. ВСЕГДА:  carousel/SKILL.md + carousel-structure.md + carousel-types.md
2. ВСЕГДА:  brand/ (голос, визуальный стиль)
3. ВИЗУАЛЫ: nano-banana/SKILL.md (если нужна генерация слайдов)
4. ПО ТИПУ: selling-meanings (продающая карусель)
5. ОБУЧЕНИЕ: learning/approved-patterns.md + anti-patterns.md
```

---

## Quick Setup

1. Fill account settings (IG username, design style)
2. Configure `design-rules.md` with brand colors/fonts
3. Update status to ✅ in main CLAUDE.md
4. Generate: `carousel [topic]`

---

## Account Settings

**Instagram Handle:** `@{your_handle}`
**Design Tool:** Figma / Canva / Adobe Express
**Brand Colors:** {Primary}, {Secondary}, {Accent}
**Fonts:** {Heading font}, {Body font}

---

## Carousel Structure

### Slide 1: Hook
**Goal:** Stop scroll

**Elements:**
- Bold headline (3-7 words)
- Eye-catching visual
- Swipe indicator

### Slides 2-8: Value
**Goal:** Deliver insights

**Options:**
- Numbered tips (1 per slide)
- Story progression
- Before/After comparison
- Problem → Solution flow

### Slide 9-10: CTA
**Goal:** Engagement

- Recap key points
- Call to action
- Follow prompt

---

## Commands

| Command | Action |
|---------|--------|
| `carousel [topic]` | Generate carousel content |
| `carousel outline [topic]` | Generate structure only |
| `carousel series [topic]` | Generate 3-carousel series |

---

## File Structure

```
modules/instagram-carousel/
├── CLAUDE.md           # This file
├── design-rules.md     # Visual guidelines
├── templates/          # Slide templates
├── carousels/          # Generated content
│   └── YYYY-MM-DD/
└── analytics/
    └── carousel-metrics.md
```

---

## Content Guidelines

**DO:**
- ✅ One clear idea per carousel
- ✅ 5-10 slides optimal
- ✅ Consistent design system
- ✅ Strong slide 1 hook
- ✅ Recap on final slide

**DON'T:**
- ❌ Too much text per slide (3-4 lines max)
- ❌ Complex visuals
- ❌ Inconsistent fonts/colors
- ❌ Weak first slide

---

## Design Rules

**Text per slide:** 15-30 words maximum
**Font size:** 40-60pt for mobile readability
**Contrast:** High contrast text/background
**Branding:** Logo on slide 1 only (subtle)

---

## Metrics Benchmarks

| Metric | Good | Great | Viral |
|--------|------|-------|-------|
| **Reach** | 2-3x followers | 3-5x | 5x+ |
| **Saves** | 5-10% | 10-20% | 20%+ |
| **Shares** | 2-5% | 5-10% | 10%+ |
| **Swipe Rate** | 60-80% | 80-90% | 90%+ |

---

## Related Files

- [[design-rules|Design Rules]] — Visual guidelines
- [[../../brand/voice-style|Voice]] — Caption style
- [[skills/carousel/SKILL|Carousel Skill]]

---

**Module Version:** 2.0 | **Status:** ⬜ Not configured
