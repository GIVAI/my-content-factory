---
name: nano-banana
description: "Nano Banana prompt generator for AI images. Use when user asks about image generation, prompts for pictures, face swap, image composition, style transfer. Activates on: 'nano banana prompt', 'image prompt', 'picture prompt', 'face swap', 'replace face', 'combine images', 'generate image prompt', 'промпт для nano banana', 'сделай промпт для изображения', 'промпт для картинки', 'замени лицо', 'объедини изображения'."
---

# Nano Banana Prompt Enhancer

Transforming simple ideas into professional prompts for Google Nano Banana (Gemini 2.5 Flash Image).

## Core Principle

```
Describe the scene, don't list keywords.
```

A narrative paragraph is always better than a word list.

---

## File Router

When requested, load the corresponding reference file:

| Request contains | File |
|------------------|------|
| example, examples, how to do, show me | [nano-banana-examples.md](nano-banana-examples.md) |
| ideas, inspiration, what's possible, capabilities, templates | [nano-banana-ideas.md](nano-banana-ideas.md) |
| vocabulary, terms, words, dictionary | [nano-banana-vocabulary.md](nano-banana-vocabulary.md) |
| **реализм, realism, realistic, photorealistic, real photo, skin texture** | [nano-banana-realism.md](nano-banana-realism.md) |
| **thumbnail, превью, обложка, youtube cover, miniature, YouTube thumbnail** | [nano-banana-thumbnails.md](nano-banana-thumbnails.md) |
| **identity kit, создать персонажа, ai модель, виртуальный инфлюенсер, e-model, референсные фото, avatar character** | [nano-banana-identity-kit.md](nano-banana-identity-kit.md) |

---

## Quick Actions

| Command | Action |
|---------|--------|
| "prompt: [idea]" | Generate full prompt from idea |
| "face swap [description]" | Prompt for face replacement |
| "combine [what]" | Prompt for image composition |
| "enhance photo" | Prompt for upscale/enhance |
| "style [which]" | Style transformation |
| "JSON" | Output in JSON format |
| "TEXT" | Output in TEXT paragraph |
| **"реализм: [идея]"** | Реалистичный промпт (RU) → load realism module |
| **"realism: [idea]"** | Realistic prompt (EN) → load realism module |
| **"linkedin photo"** | Professional headshot |
| **"instagram real"** | Lifestyle candid |
| **"editorial"** | Dramatic portrait |
| **"beauty"** | Glamour portrait |
| **"identity kit: [описание]"** | Создать концепцию AI-персонажа → load identity-kit module |
| **"референс нейтральный"** | Промпт для нейтрального референса (4K, f/8) |
| **"референс улыбка"** | Промпт для улыбки с зубами |
| **"референс 3/4"** | Промпт для поворота 3/4 |
| **"создать персонажа"** | Полный workflow создания AI-модели |

---

## Nano Banana Strengths

| Capability | Description |
|------------|-------------|
| **Native Multimodal** | Text + images together |
| **Multi-Image** | Up to 14 references |
| **Identity Preservation** | Face preservation |
| **Text Rendering** | Quality text |
| **Conversational** | Iterative refinement |

## Reference Limits

- Objects/Products: up to 6 images
- People (identity): up to 5 images
- Total: up to 14 references

---

## Output Formats

### FORMAT A: TEXT (Paragraph)
Natural prose description. For portraits, lifestyle, quick iterations.

### FORMAT B: JSON (Structured)
Nested categories. For complex scenes, technical control.

**Ask for format** if not specified: "TEXT or JSON?"

---

## 7-Category Framework

Every prompt includes:

1. **Subject** — who/what + details
2. **Environment** — where + space
3. **Lighting** — type + direction
4. **Style** — artistic approach
5. **Camera** — equipment + settings
6. **Composition** — framing
7. **Quality/Mood** — atmosphere + quality

---

## Prompt Types

### TYPE 1: Text-to-Image
Generation from text description.

### TYPE 2: Reference Operations

**Face Swap:**
```
Replace [person] from [Image1] with person from [Image2]. Keep exactly recognizable — same facial features, proportions, skin texture. No beauty filters, no smoothing. Match lighting and angle. Keep background unchanged.
```

**Clothing Change:**
```
Keep person from [Image1], replace [clothing] with clothing from [Image2]. Preserve pose, proportions, features. High-quality, realistic.
```

**Multi-Image Composition:**
```
Combine [Image1], [Image2], [Image3] into one cohesive image. Preserve recognizability of all objects. Unified lighting, shadows, perspective. Photorealistic, seamless.
```

**Style Transfer:**
```
Transform [Image1] into style of [Image2/artist]. Preserve composition, render with [stylistic elements].
```

**Background Change:**
```
Keep subject from [Image1], replace background with [description/Image2]. Match lighting naturally. Seamless, photorealistic.
```

**Photo Enhancement:**
```
Enhance and upscale [Image1]. Remove blur, make skin realistic with clear pores and natural transitions. Preserve composition and colors. Sharp edges on eyes, lips, hair.
```

---

## Templates

### Photorealistic
```
A photorealistic [shot type] of [subject], [action], set in [environment]. Illuminated by [lighting], creating [mood]. Captured on [camera/lens]. [Aspect ratio].
```

### Product
```
High-resolution product photograph of [product] on [surface]. [Lighting setup]. [Camera angle] to showcase [feature]. Ultra-realistic, sharp focus. [Aspect ratio].
```

### Character Design
```
Generate Character Design:
- Proportions (height comparisons)
- Three views: front, side, back
- Expression Sheet
- Pose Sheet
- Costume Design
```

---

## Advanced Techniques

### Identity Lock (Critical)

**When using reference image [Image1] for a person:**

```
IDENTITY LOCK for person from [Image1]:
- Preserve EXACT facial features: bone structure, nose shape, eye spacing, jawline
- Preserve EXACT skin tone, texture, pores, and blemishes
- Preserve EXACT hairstyle, hair color, and hairline
- NO beautification, NO smoothing, NO idealization
- NO age change, NO ethnicity drift, NO face morphing
- The person MUST be 100% recognizable as the same individual
- If identity cannot be preserved perfectly, DO NOT generate
```

**Strong version (when identity keeps drifting):**
```
CRITICAL IDENTITY REQUIREMENT:
The person from [Image1] must look EXACTLY like themselves — not "similar", not "inspired by", but IDENTICAL.
Same face, same skin, same features. No AI interpretation or "improvement".
Treat [Image1] as a photo ID that must match perfectly.
```

### Negative Guidance
```
No extra fingers, no double pupils, no blur, no duplicated faces, no distorted proportions.
```

### Aspect Ratio
- When editing: "Do not change aspect ratio"
- When generating: specify explicitly ("16:9", "9:16", "1:1")
- Multiple references: takes ratio of the LAST one

### Lighting Source
When combining, choose ONE image for lighting:
```
Use lighting from [Image1] as reference.
```

### Animation-Ready Frames (for AI Avatar)

When creating images that will be animated (HeyGen, Hedra, Sync Labs, etc.), use these rules:

```
ANIMATION-READY REQUIREMENTS:
- Neutral "ready" pose — not mid-gesture, not frozen in motion
- Face 100% visible — nothing covering or near face (no hands near chin/mouth)
- Hands in natural resting position — on table, clasped, or at sides
- Relaxed shoulders, natural posture
- Direct or 3/4 face angle — avoid extreme profiles
- Mouth naturally closed or slightly parted — ready to speak
- Eyes looking at camera — establishes connection
- NO frozen mid-action poses — should look like "pause before speaking"
```

**Bad poses for animation:**
- Hand touching face
- Arms crossed tightly
- Mid-gesture freeze
- Looking away from camera
- Mouth wide open

**Good poses for animation:**
- Hands resting on table
- Hands loosely clasped
- Arms relaxed at sides
- Neutral "listening" expression
- Ready-to-speak moment

---

## Iteration Commands

| Command | Effect |
|---------|--------|
| "Make warmer" | Warm tones |
| "Add contrast" | Contrast |
| "Zoom in" | Closer |
| "Fix hands" | Anatomy |
| "Remove X" | Remove |
| "Add X" | Add |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Identity drift (face changes)** | Use full Identity Lock block (see above) + regenerate 2-3x |
| Identity still drifting | Add "CRITICAL IDENTITY REQUIREMENT" strong version |
| Person looks "beautified" | Add "NO beautification, NO smoothing, NO idealization" |
| Wrong ethnicity/age | Add "NO ethnicity drift, NO age change" |
| Extra fingers | Add "correct hand anatomy" |
| Text distortion | Shorten text, reduce angle |
| Color drift | Specify hex codes |
| Style bleeding | "Photorealistic only, no illustration" |
| **Hands/body out of focus** | Avoid f/1.4-1.8 aperture. Use `f/5.6-f/8` or add `deep depth of field, everything in sharp focus` |
| Unwanted bokeh on props | Add `Sharp focus on ALL elements in frame. No selective focus, no bokeh on hands or objects` |

### Identity Drift — Common Causes

| Cause | Fix |
|-------|-----|
| Too complex scene | Simplify, focus on face |
| Multiple people in prompt | Use [Image1] label explicitly for each person |
| Celebrity comparison | Remove celebrity, describe pose instead |
| Generic descriptors ("handsome", "beautiful") | Remove — they override identity |
| Lighting mismatch | "Match lighting from [Image1]" |

---

## Quality Checklist

- [ ] Subject is specific
- [ ] Reference images labeled [Image1], [Image2]
- [ ] Identity lock included (for people)
- [ ] Lighting specified
- [ ] Aspect ratio specified
- [ ] **Depth of field specified** (f/5.6-f/8 for full-body sharp, f/1.4-2.8 only for headshots)
- [ ] No contradictions
- [ ] Descriptive paragraph, not keywords
- [ ] In English
- [ ] Clean output (no comments)
- [ ] Style Lock at end (for multi-image series)

---

## Style Lock (for Multi-Image Consistency)

When generating multiple related images (carousels, series, variations), use a **Style Lock** block at the end of EACH prompt.

### Purpose
Style Lock ensures visual consistency across all images in a series.

### Structure
```
=== STYLE LOCK ===
CANVAS: [Aspect ratio, size, bleed]
BACKGROUNDS: [Colors with hex codes, explicit restrictions]
COLOR PALETTE: [Accent colors, usage]
TEXT: [Typography specs if any]
RENDER: [Style, quality]
=== END STYLE LOCK ===
```

### Example
```
=== STYLE LOCK ===
CANVAS: Full-bleed 3:4 (1080×1350px). No borders, no margins.
BACKGROUNDS: #1a1a1a ONLY. NEVER white or light colors.
COLOR PALETTE: Gold #ecb00a for accents.
TEXT: Montserrat Bold, white or gold.
RENDER: Cinematic photorealistic 3D, high contrast.
=== END STYLE LOCK ===
```

---

## Explicit Negatives

NanoBanana sometimes adds unwanted elements. Use explicit negatives to prevent:

| Problem | Add to prompt |
|---------|---------------|
| Wrong background color | `NEVER white, light gray, or any light colors` |
| Unwanted headers | `NO separate header or title bar` |
| Text duplication | `ONLY ONE instance of this text. Do NOT duplicate` |
| UI elements appearing | `No UI elements, no progress bars, no counters` |
| Image not filling frame | `Full-bleed...fills entire frame edge to edge` |
| Style bleeding | `Photorealistic only, no illustration` |

### Negatives Syntax
Use **CAPS** for emphasis: `NEVER`, `NO`, `ONLY`, `Do NOT`

---

## Regeneration Expectations

**NanoBanana is stochastic** — identical prompts can produce different results.

### Typical regeneration counts:
| Complexity | Expected attempts |
|------------|-------------------|
| Simple scene | 1-2 |
| Complex composition | 2-3 |
| Text in image | 2-4 |
| Multi-element layouts | 3-5 |

### When to regenerate vs. modify prompt:
- **Regenerate:** Small issues (positioning, minor artifacts)
- **Modify prompt:** Consistent issues (wrong colors, missing elements, wrong style)

---

## File Organization & Upload

### Организация проектов

Каждый проект генерации:
```
projects/{your-project}/YYYY-MM-DD/
├── prompt.md           # Промпт и описание
├── image1.jpg         # Результаты
├── image2.jpg
└── notes.md           # Комментарии
```

Примеры: `projects/my-brand/2026-02-01/`, `projects/client-name/2026-02-01/`

### Техническая обработка

**⚠️ КРИТИЧЕСКОЕ:** 4K PNG > 8MB → ошибка 413

1. Генерация возвращает base64 PNG
2. **Сразу конвертировать PNG → JPEG** перед отправкой: `magick input.png -quality 90 output.jpg`
3. Макс получает **всегда JPEG** для соцсетей, PNG только для архива

### Метрики качества

| Параметр | Цель |
|----------|------|
| Размер JPEG | < 5MB |
| Качество сжатия | 85-95% |
| Время генерации | < 2 мин |
| Соответствие референсу | > 80% сходство |
| Читаемость текста | 100% |

---

## Процесс согласования с Максом

### ПЕРЕД ЛЮБОЙ генерацией:

1. **Загрузить скилл nano-banana** + нужный модуль (realism/identity-kit/vocabulary/thumbnails)
2. **ОТЧИТАТЬСЯ МАКСУ:** `"Скилл nano-banana подключен, модуль [X] загружен ✅"`
3. **Только после отчёта** — писать промпты и генерировать

### Правила:
- **Максимум 4-5 параллельных запросов** — не больше
- **Согласовывать стоимость** если больше 3 картинок
- Промпт **ВСЕГДА на английском**, описания для Макса на русском
- Референсы: `[image1]`, `[image2]` — Макс подставит сам

### Workflow по проектам

| Проект | Brand | Особенности |
|--------|-------|------------|
| **Карусели** | Тёмный фон, акцентный цвет, Montserrat | Последний слайд = CTA |
| **Медицинский эксперт** | Изумруд/navy/teal | Профессиональный вид, референсы эксперта |
| **YouTube обложки** | 16:9, крупный текст | Стрелки/элементы добавляются отдельно |

---

## Output Rules

**DO:**
- Output ONLY the prompt
- Immediately copyable
- All 7 categories

**DO NOT:**
- "Here's your prompt:"
- Decorative lines
- Headers
- Explanations after the prompt

---

## Realism Mode

Для генерации **суперреалистичных** фотографий используй команды:
- `реализм: [идея]` или `realism: [idea]`
- `linkedin photo`, `instagram real`, `editorial`, `beauty`

При активации → автоматически загружается [nano-banana-realism.md](nano-banana-realism.md) с:
- Техникой трёхслойного реализма (Camera, Skin, Lighting)
- Subsurface Scattering для живой кожи
- 3-tier negative prompts
- Identity Lock для сохранения лица
- 4 мастер-промпта (LinkedIn, Instagram, Editorial, Beauty)
- Troubleshooting пластиковой кожи и других артефактов

**Ключевая формула:** `Реализм = Детали + Несовершенство + Правильный Свет`

---

## Auto-Generation (via LaoZhang API)

После генерации промпта предложи:
```
Сгенерировать изображение? (2K/4K/Нет)
```

### При согласии:
```typescript
mcp__laozhang__laozhang_generate_image({
  prompt: "<generated_prompt>",
  size: "2K"  // или "4K" для высокого качества
})
```

### Параметры:
| Размер | Цена | Использование |
|--------|------|---------------|
| 1K | $0.05 | Быстрые тесты |
| 2K | $0.05 | Стандарт (default) |
| 4K | $0.05 | Превью, детальные сцены |

### Auto-save:
- **Default:** `projects/nano_img/YYYY-MM-DD/nano-{timestamp}.png`
- **Custom:** передать `save_path` параметр

### Workflow:
1. User → идея
2. Skill → промпт (английский)
3. User → "2K" / "4K" / "Нет"
4. MCP → генерация → файл
5. Return → путь к файлу
