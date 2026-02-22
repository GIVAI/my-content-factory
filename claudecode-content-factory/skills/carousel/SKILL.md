---
name: carousel
description: "Instagram Carousel Generator via NanoBanana. Activates on: 'carousel', 'instagram slides', 'make carousel', 'prompt carousel', 'карусель', 'инста слайды', 'сделай карусель'."
---

# Carousel Skill

Generating Instagram carousels with NanoBanana prompts for each slide.

## Core Principle

**Carousel formula:**
```
HOOK (slide 1) → BODY (slides 2-N) → CTA (last slide)
```

**Rules:**
1. **1 idea = 1 slide** — don't overload
2. **Consistency** — unified style across all slides
3. **Identity lock** — if there's a reference, preserve identity
4. **Aspect ratio: 3:4** — Instagram carousel standard (1080×1350px)

---

## File Router

| Request contains | Load file |
|------------------|-----------|
| "structure", "hook", "body", "cta" | carousel-structure.md |
| "type", "which format", "prompt carousel", "expert", "minimalist" | carousel-types.md |
| "prompt", "nanoBanana", "template" | carousel-prompts.md |
| "cta", "call to action", "follow", "comment link" | carousel-cta.md |

---

## Context Loading

При генерации контента загрузи из проекта:

1. `projects/{project}/brand/voice-style.md` — стиль
2. `projects/{project}/learning/patterns.md` — что работает
3. `projects/{project}/learning/examples/` — референсы

**Используй примеры пользователя как образец стиля.**

---

## Workflow

### Phase 1: Collect Input Data

```
REQUIRED:
├── TOPIC: [what the carousel is about]
├── PROJECT: [for Brand Kit] or "universal"
└── TYPE: [auto / prompt / expert / minimalist / viral / grid]

OPTIONAL:
├── REFERENCE: [Image1] for identity lock
├── CHARACTER: [description if no reference]
├── SLIDES: [5-10, default: 7]
├── LANGUAGE: [RU / EN]
└── TEXT OVERLAY: [NanoBanana / Editor]
```

**If reference NOT provided but character needed:**
```
Ask:
- Gender, age
- Appearance (ethnicity, hair, style)
- Clothing/look
- Mood/expression
```

### Phase 2: Content Structure

1. **Generate HOOK** (slide 1)
   - Headline: max 7 words
   - Subheadline/intrigue
   - "Swipe for details"

2. **Break down BODY** (slides 2-N)
   - 1 idea = 1 slide
   - Text: max 20 words/slide
   - Visual concept for each

3. **CTA slide** (last)
   - Call to action
   - Badge with avatar/account

### Phase 3: Generate NanoBanana Prompts

For **each slide** generate a separate prompt:

```
Slide N:
├── Full NanoBanana prompt (7 categories)
├── Aspect ratio: 3:4
├── Consistent style (colors, lighting, mood)
├── Identity lock (if reference)
└── Text overlay instruction (optional)
```

### Phase 4: Output

**CRITICAL: Output ONLY NanoBanana prompts. NO duplicate text descriptions.**

NanoBanana generates slides FULLY — text is embedded IN the prompt, not separate.

```markdown
## Carousel: [Title]

## Slide 1 — Hook

```
[Full NanoBanana prompt with embedded text + Style Lock]
```

## Slide 2 — [Name]

```
[Full NanoBanana prompt with embedded text + Style Lock]
```

[... for each slide]

---

## Caption
[ready description text]

## Hashtags
[relevant hashtags]
```

**DO NOT:**
- Add separate "Text on slide:" sections
- Duplicate content that's already in the prompt
- Create "visual concept" descriptions outside prompts
- Waste tokens on redundant information

---

## Quick Actions

| Command | Action | Files |
|---------|--------|-------|
| "carousel [topic]" | Full carousel with prompts | structure + types + prompts |
| "prompt carousel [topic]" | Carousel with prompts on photo | types + prompts |
| "expert carousel [topic]" | Carousel with expert | types + prompts |
| "carousel structure" | Structure only without prompts | structure |
| "carousel cta options" | CTA slide variations | cta |

---

## Carousel Types (overview)

| Type | When to use | Features |
|------|-------------|----------|
| **Prompt** | AI prompts, generation training | Photo + prompt overlay |
| **Expert** | Tips, instructions, lists | Expert photo + text |
| **Minimalist** | Quotes, thoughts, clean content | Monochrome + typography |
| **Viral** | Hype, news, intrigue | Dark background + neon |
| **Grid** | Many points, reviews | Card grid |

→ Details: `carousel-types.md`

---

## Consistency Between Slides

**Fix for the entire carousel:**
```
VISUAL STYLE:
├── Color palette (from Brand Kit or specified)
├── Lighting (type + direction)
├── Mood/atmosphere
└── Background (consistent or connected)

CHARACTER (if present):
├── Identity lock: "Must look 1000% identical"
├── Clothing (same or from one collection)
└── Facial expression (connected to slide topic)

TEXT (if overlay):
├── Font (from Brand Kit)
├── Size (consistent)
├── Position (bottom/top — same)
└── Badge style
```

---

## Text Overlay (NanoBanana ONLY)

**ALWAYS embed text directly in the NanoBanana prompt.**

NO "add in editor later" workflow — NanoBanana generates the complete slide.

```
TEXT at [position] (white Montserrat Bold, large):
"[HEADLINE TEXT]"

Below (white Montserrat Regular):
"[SUBHEADLINE TEXT]"
```

**Include in prompt:**
- Exact text content in quotes
- Font (from project Brand Kit)
- Position (top/center/bottom)
- Colors (white, gold accent, etc.)

---

## Brand Kit Integration

### Style Loading Algorithm

```
1. IF project specified:
   a. CHECK for projects/{project}/brand/carousel-style.md
   b. IF found: LOAD and apply to all prompts
   c. IF not found: proceed to step 2

2. IF no carousel-style.md:
   ASK user:
   - "What font for text overlays?" (e.g., Montserrat, Inter)
   - "Accent color hex?" (e.g., #ecb00a)
   - "Background preference?" (dark/light/specific hex)
   - "Any style rules?" (e.g., only dark backgrounds)

3. APPLY style to NanoBanana prompts (see below)
```

### How to Apply carousel-style.md to Prompts

When generating NanoBanana prompts, inject style parameters:

**Background:**
```
Replace generic: "dark moody background"
With project value: "[hex] [color name]" from carousel-style.md
Example: "#2d2d2d charcoal gray background"
```

**Text Overlay:**
```
Replace generic: "white sans-serif font"
With project value: "white [font] font, bold"
Example: "white Montserrat font, bold"
```

**Color Palette (in Style Lock):**
```
Add: "Color palette: [accent] accent, [background] background"
Example: "Color palette: #ecb00a accent, #2d2d2d background"
```

**Use Ready Snippets:**
If carousel-style.md has "Ready Prompt Snippets" section — use them directly.

### Also Load (optional):

```
projects/{project}/brand/
├── voice-style.md     → text tone for captions
└── carousel-refs/     → style references (if present)
```

---

## Quality Checklist

Before output, check:

- [ ] Topic covered sequentially
- [ ] Hook intrigues and stops scroll
- [ ] 1 idea = 1 slide (not overloaded)
- [ ] Text on slides: max 20 words
- [ ] All prompts in NanoBanana format (7 categories)
- [ ] Aspect ratio: 3:4 specified
- [ ] Identity lock (if reference)
- [ ] Consistent style between slides
- [ ] CTA slide with call to action
- [ ] Caption ready
- [ ] Prompts in English
- [ ] Output clean, ready to copy

---

## Anti-patterns

| Bad | Why | Fix |
|-----|-----|-----|
| Too much text on slide | People don't read | Max 20 words |
| Different slide styles | Looks unprofessional | Fix the style |
| Weak hook | They don't swipe | Hook formulas from structure |
| No CTA | Lose conversion | Always last slide |
| Keywords instead of prompt | NanoBanana generates poorly | Descriptive paragraphs |
| Identity drift | Person looks different | Identity lock in every prompt |
| No Style Lock | Inconsistent slides | Style Lock REQUIRED at end of every prompt |
| **Duplicate text + prompt** | **Wastes tokens** | **ONLY prompts, text embedded inside** |
| "Text:" + "Prompt:" sections | Redundant, confusing | Single prompt block per slide |
| "Added in editor" workflow | Extra steps, inconsistency | NanoBanana generates FULLY |

---

## Style Lock (REQUIRED)

**Every NanoBanana prompt MUST end with a Style Lock block.**

Style Lock ensures visual consistency across all carousel slides.

### What to include in Style Lock:

```
=== STYLE LOCK ===
CANVAS: [Aspect ratio, full-bleed requirement]
BACKGROUNDS: [Color codes, explicit restrictions]
COLOR PALETTE: [Accent colors, usage rules]
TEXT BADGES: [Badge styles with exact specs]
TYPOGRAPHY: [Font, weights, colors]
RENDER: [Visual style, quality level]
=== END STYLE LOCK ===
```

### Loading Project Style:

```
1. CHECK projects/{project}/brand/carousel-style.md
2. IF found: USE Style Lock Template from that file
3. IF not found: ASK user for:
   - Accent color (hex)
   - Background preference (dark/light)
   - Font family
   - Badge style
4. BUILD Style Lock from answers
```

---

## Explicit Negatives

NanoBanana sometimes adds unwanted elements. Use explicit negatives:

| Risk | Add to prompt |
|------|---------------|
| Light backgrounds appearing | `NEVER white, light gray, or any light colors` |
| Headers/title bars | `NO separate header or title bar` |
| Text duplicating | `ONLY ONE instance...Do NOT duplicate` |
| UI elements | `No UI elements, no progress bars` |
| Wrong aspect ratio | `Full-bleed [ratio]...fills entire frame edge to edge` |

---

## Common Issues & Fixes

| Problem | Cause | Solution |
|---------|-------|----------|
| Image squeezed/margins | No full-bleed | `"fills entire frame edge to edge"` |
| Text duplicated | NanoBanana quirk | `"ONLY ONE instance...Do NOT duplicate"` |
| Light header appeared | Had title text | Remove title + `"NO separate header"` |
| Badge corners differ | Not specified | `"border-radius: Xpx"` in Style Lock |
| Random UI elements | Mentioned count | `"no UI elements"` |
| Style drift mid-carousel | No Style Lock | Style Lock in EVERY prompt |
| **Identity drift (face changes)** | Weak identity lock | Use full Identity Lock block (see below) |
| Person looks different | Generic descriptors | Remove "handsome", "beautiful" — they override identity |

**Regeneration Note:** NanoBanana is stochastic. Even perfect prompts may need 2-3 generations.

---

## Identity Lock (for reference images)

**When carousel uses person from reference [Image1]:**

```
IDENTITY LOCK for person from [Image1]:
- Preserve EXACT facial features: bone structure, nose shape, eye spacing, jawline
- Preserve EXACT skin tone, texture, pores, and blemishes
- NO beautification, NO smoothing, NO idealization
- NO age change, NO ethnicity drift, NO face morphing
- The person MUST be 100% recognizable as the same individual
```

**If identity keeps drifting, use STRONG version:**
```
CRITICAL IDENTITY REQUIREMENT:
The person from [Image1] must look EXACTLY like themselves — not "similar", not "inspired by", but IDENTICAL.
Same face, same skin, same features. No AI interpretation.
Treat [Image1] as a photo ID that must match perfectly.
```

**Common causes of identity drift:**
- Too complex scene → simplify
- Celebrity comparisons → remove celebrity name, describe pose only
- Generic descriptors ("handsome", "attractive") → remove completely
- Lighting mismatch → add "Match lighting from [Image1]"

---

## Stylized Avatar (for CTA slides)

**When you need a stylized avatar, NOT photorealistic:**

```
STYLIZED AVATAR based on [Image1]:
- Convert to clean vector/illustrated style (like Notion avatars or Bitmoji)
- Flat colors, smooth gradients, minimal details
- Recognizable likeness but NOT photorealistic
- Keep the same face shape, hairstyle, and general appearance
- Style: modern, clean, tech-forward illustration
```

**IMPORTANT:** Identity Lock = photorealistic. Stylized Avatar = illustration.
Don't mix them — NanoBanana will generate creepy results.

---

## Photo Insert (no changes)

**When you need to insert a photo AS-IS without any modifications:**

```
Place [Image1] inside a circular frame with golden (#ecb00a) ring border (3px thickness).
- Crop [Image1] to circle, centered on face
- DO NOT modify, stylize, or regenerate the photo
- Keep the original photo exactly as provided
- Only add the frame/border around it
```

**Use cases:**
- CTA slides with user's existing avatar
- Profile photos that shouldn't be AI-touched
- Brand photos that must stay unchanged

---

## Reference Examples

Location: `learn/carousel examples/`

| File | Type | What to study |
|------|------|---------------|
| `prompt format...` | Prompt | Prompt overlay on photo |
| `beautiful first slide.PNG` | Expert | Hook with photo + text |
| `bright first slide.PNG` | Viral | Badge + intrigue |
| `step by step.PNG` | Expert | Steps with visuals |
| `CTA with badge.PNG` | CTA | Badge + follow |

---

## Learning Integration

### Где искать паттерны

| Источник | Путь |
|----------|------|
| **Global** | `skills/carousel/` |
| **Project** | `projects/{project}/learning/skill-learning/carousel/patterns.md` |
| **Anti-patterns** | `projects/{project}/learning/skill-learning/carousel/anti-patterns.md` |
| **Examples** | `projects/{project}/learning/skill-learning/carousel/examples/` |

### Команды обучения

| Команда | Куда пишет |
|---------|-----------|
| `это сработало: [что]` | `skill-learning/carousel/patterns.md` |
| `это не сработало: [что]` | `skill-learning/carousel/anti-patterns.md` |
| `запомни пример` | `skill-learning/carousel/examples/` |

---

## Critics System

После генерации карусели — 3 критика.

### Visual Expert
- ✅ Консистентный стиль между слайдами
- ✅ Identity lock работает
- ❌ Стиль "плывёт" к концу

### Hook Expert
- ✅ Первый слайд останавливает скролл
- ✅ Интрига → свайп
- ❌ Слабый хук, не цепляет

### Structure Expert
- ✅ 1 идея = 1 слайд
- ✅ CTA на последнем слайде
- ❌ Перегруженные слайды

---

*Carousel Skill v1.1 — Learning + Critics*
