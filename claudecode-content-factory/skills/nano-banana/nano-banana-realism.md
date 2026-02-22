# Nano Banana Realism Module

Модуль для генерации суперреалистичных фотографий. Активируется триггерами: `реализм`, `realism`, `realistic`, `photorealistic`, `real photo`.

> **Для глубокого изучения:** [learn/nano-banana/Nano_Banana_Realism_Guide.md](../../../../learn/nano-banana/Nano_Banana_Realism_Guide.md) — 770 строк детального руководства

---

## Философия реализма

> **Реализм = Детали + Несовершенство + Правильный Свет**

**Ключевой insight:** Специфика побеждает неопределённость.

| Плохо | Хорошо |
|-------|--------|
| "realistic portrait" | "portrait of 32-year-old woman, natural skin texture with visible pores and fine lines, shot on 85mm f/1.8 lens with Rembrandt lighting, shallow depth of field, no airbrushing, unretouched photography look" |

**Gemini-принцип:** Describe the scene, don't just list keywords. Narrative paragraph > keyword list.

---

## Техника трёхслойного реализма

### Layer 1: Camera & Lens
```
"Shot on Sony A7R IV with 85mm f/1.4 lens, 1/250 shutter, ISO 400"
"Shot on Phase One XF IQ4 with 85mm f/1.4, shallow depth of field"
"Shot on Canon EOS R5, 50mm lens, f/2.0 aperture"
```

### Layer 2: Skin & Texture (Realism Layer)
```
"Natural skin texture with visible pores, fine lines around eyes,
subtle freckles, light sun damage on cheekbones,
uneven skin tone, small blemishes, light redness around nose.
Not airbrushed. Not retouched. No smoothing."
```

### Layer 3: Lighting
```
"Soft diffused light from left at 45 degrees (Rembrandt style),
creating small triangle of light on shadowed cheek.
Key light 3:1 ratio, soft fill from right.
Subtle rim light for separation.
No harsh shadows. Natural window light diffused by translucent curtains."
```

---

## Subsurface Scattering (SSS)

Критически важно для живой кожи. Свет проникает сквозь кожу и рассеивается внутри.

```
"skin with visible subsurface scattering, particularly at ear edges and nose,
creating a warm luminous quality that indicates living tissue"
```

**Где видно SSS:**
- Края ушей при backlight
- Кончик носа
- Тонкие участки кожи при боковом свете

---

## Quick Reference Tables

### Слова для реализма vs. слова-убийцы

| Используй | Избегай |
|-----------|---------|
| `visible pores` | `perfect` |
| `fine lines, wrinkles` | `flawless` |
| `natural skin texture` | `airbrushed` |
| `subtle imperfections` | `smooth` (для кожи) |
| `uneven discoloration` | `beauty filter` |
| `candid moment` | `glamour` |
| `unposed` | `hyper-realistic 8k render` |
| `natural asymmetry` | `CGI`, `3D render` |
| `subsurface scattering` | `illustration` |

### Камеры для разных целей

| Цель | Камера + Объектив | Эффект |
|------|------------------|--------|
| Professional Headshot | Sony A7R IV + 85mm f/1.4 | Sharp, rich tones, creamy bokeh |
| Luxury/Editorial | Phase One XF IQ4 + 85mm f/1.4 | Ultra-detailed, medium format feel |
| Clean Corporate | Canon EOS R5 + 50mm f/2.0 | Neutral, balanced, crisp |
| Lifestyle Candid | Leica Q2 + 28mm | Warm, organic, film-like |
| Cinematic | ARRI Alexa + 50mm | Cinematic color science, dramatic |
| Classic Beauty | Hasselblad + 80mm | High-end, luxury look |

### Film Stock Simulation

| Film Stock | Характеристики | Когда использовать |
|------------|----------------|-------------------|
| Fujifilm Pro 400H | Warm, slightly saturated, beautiful skin tones | Портреты, fashion |
| Kodak Portra 400 | Natural skin tones, neutral palette | Универсальный |
| Kodak Tri-X | Black and white, high contrast | Драматичные, editorial |

### Паттерны освещения

| Паттерн | Угол | Эффект | Когда |
|---------|------|--------|-------|
| **Rembrandt** | Key 45° выше глаз | Треугольник света на щеке | Editorial, drama |
| **Loop** | Key 30-45° в сторону | Петля тени от носа | Corporate, headshots |
| **Butterfly** | Key прямо впереди, выше | Тень-бабочка под носом | Beauty, glamour |
| **Split** | Key 90° в сторону | Половина лица в тени | Очень драматичные |

### Кожа по возрастам

**20-25 лет:**
```
"Fine facial features, smooth but natural skin texture with visible pores,
subtle natural blemishes, youthful glow, minimal wrinkles"
```

**30-40 лет:**
```
"Natural skin texture with visible pores, fine lines around eyes and mouth,
subtle expression lines, light age spots, sun-damaged areas,
slight unevenness in skin tone"
```

**40+ лет:**
```
"Weathered skin with visible pores and texture,
prominent fine lines and wrinkles, age spots,
character lines, uneven skin tone, laugh lines,
forehead creases—all natural and beautiful"
```

### Depth of Field Control

| Aperture | Когда использовать | Проблема |
|----------|-------------------|----------|
| f/1.4-1.8 | **Только headshots** | Hands/body out of focus |
| f/2.8-4.0 | Portraits with context | Moderate background blur |
| f/5.6-f/8 | **Full-body sharp** | Everything in focus |

**Если руки размыты:** Используй `f/5.6-f/8` или добавь `deep depth of field, everything in sharp focus, sharp focus on ALL elements`.

---

## Negative Prompts (3-Tier System)

### Tier 1: Core Cleanliness (всегда)
```
no text, no watermark, no logo, no signature, no artifacts,
no UI elements, no compression noise
```

### Tier 2: Realism & Anti-AI (для портретов)
```
no plastic skin, no glossy highlights, no waxy texture,
no over-smooth face, no beauty filter, no airbrushed look,
no illustration, no painting, no 3D render, no CGI, no cartoon,
no perfect symmetry, no mannequin face
```

### Tier 3: Subject-Specific
```
no extra fingers, no deformed hands, no bad anatomy,
no blurred face, no pixelated areas, no double eyes
```

### Weighted Negatives (для Stable Diffusion)
```
extra fingers:1.5, blurry:1.2, watermark:1.0, plastic skin:1.3
```

---

## Identity Lock Technique

Для сохранения лица при генерации и трансформациях:

```
IDENTITY LOCK for person from [Image1]:
- Preserve EXACT facial features: bone structure, nose shape, eye spacing, jawline
- Preserve EXACT skin tone, texture, pores, and blemishes
- Preserve EXACT hairstyle, hair color, and hairline
- NO beautification, NO smoothing, NO idealization
- NO age change, NO ethnicity drift, NO face morphing
- The person MUST be 100% recognizable as the same individual
```

**Сильная версия (если лицо плывёт):**
```
CRITICAL IDENTITY REQUIREMENT:
The person from [Image1] must look EXACTLY like themselves —
not "similar", not "inspired by", but IDENTICAL.
Same face, same skin, same features. No AI interpretation or "improvement".
Treat [Image1] as a photo ID that must match perfectly.
```

---

## Iterative Refinement Strategy

| Итерации | Фокус | Что делать |
|----------|-------|------------|
| 1-3 | Concept alignment | Соответствует ли базовая идея? |
| 4-6 | Details | Skin quality, lighting, composition |
| 7+ | Diminishing returns | Только если есть специфичная проблема |

**После 6 итераций** — если результат не устраивает, лучше переписать промпт с нуля.

---

## Мастер-промпты

### LinkedIn Professional
```
Professional headshot maintaining exact facial identity.
Neutral studio environment, clean mid-gray background.
Natural skin texture with visible pores, subtle imperfections, realistic detail.
Loop lighting (key 30° to side and slightly above), soft fill light creating even coverage,
professional studio quality.
Shot on Sony A7R IV with 85mm f/1.8 lens, shallow depth of field, ultra-sharp focus on eyes.
Color temperature 5500K neutral daylight, no color cast.
Sharp enough for professional use but not oversaturated.
High-resolution 4K detail.

NO: plastic skin, glossy highlights, airbrushed, illustration, perfect symmetry,
harsh shadows, text, watermark, artifacts, extra limbs, deformed features.
```

### Instagram Lifestyle
```
Candid lifestyle portrait, casual moment, unposed.
Natural soft window light from left, realistic shadows and highlights.
Visible skin texture with natural imperfections—fine lines, subtle blemishes, realistic detail.
Shot like iPhone portrait mode—not overly polished, authentic social media feel.
Shallow depth of field with creamy bokeh background.
Warm color temperature 4000K, natural tone.
Relaxed expression, looking slightly away from camera.
Real, lived-in aesthetic—not studio-perfect.

NO: studio-perfect lighting, beauty filter, too smooth, illustration, 3D render,
perfect centered composition, mannequin-like pose, oversaturated colors, harsh flash.
```

### Editorial Dramatic
```
Three-quarter editorial portrait, cinematic mood.
Dramatic Rembrandt lighting (key 45° above and to side, creating triangle of light on shadowed cheek),
subtle rim light for separation from dark background.
Deep shadows, moody atmosphere, high contrast.
Rich natural skin texture with visible pores and micro-details,
realistic aging and sun damage appropriate to age.
Shot on Phase One with 85mm f/1.4, ultra-sharp focus on eyes, razor-sharp detail.
Deep gray gradient background, shallow DoF, beautiful bokeh.
Color grading cool 6000K cinematic tones, strong contrast, moody.
High-resolution 8K detail.

NO: over-smooth skin, plastic texture, bright cheerful mood, centered composition,
busy background, illustration, artificial daytime lighting, perfect symmetry,
oversaturated colors, too polished.
```

### Beauty/Glamour
```
Beauty portrait, high-key studio lighting.
Butterfly lighting (key light centered and slightly above, creating butterfly shadow under nose),
flattering and glowing.
Natural skin texture preserved (visible pores), soft and flattering—not plastic.
Shot on medium format with 85mm lens, f/2.8 aperture.
Seamless light gray background, minimal harsh shadows.
Warm 4500K white balance for flattering, glowing skin tones.
Sharp focus on eyes, soft overall.
Professional beauty photography aesthetic.

NO: dark moody look, harsh shadows, Rembrandt style, blemishes too emphasized,
low-key lighting, cool tones, illustration, CGI, unnatural plastic look.
```

---

## Troubleshooting

| Проблема | Решение |
|----------|---------|
| **Plastic skin** | Добавь "fine pores, microtexture, natural imperfections"; negative "airbrushed, waxy" |
| **Skin tone off** | Укажи tone + undertone; добавь "accurate white balance, neutral color grading" |
| **Hands out of focus** | Используй f/5.6-f/8, не f/1.4; добавь "deep depth of field" |
| **Identity drift** | Используй Identity Lock block; упрости сцену |
| **Uncanny valley** | Добавь "natural asymmetry", "subtle imperfections"; убери "perfect" |
| **Too smooth** | Lower stylize (MJ); добавь "visible pores, fine texture, microtexture" |

---

## Checklist перед генерацией

### Структура
- [ ] Camera & Lens указаны (Sony A7R IV, 85mm f/1.4, etc.)
- [ ] Subject описан (возраст, выражение, поза)

### Реализм
- [ ] Skin texture есть (visible pores, fine lines, imperfections)
- [ ] НЕТ plastic-слов (perfect, flawless, airbrushed)
- [ ] Subsurface scattering если backlight

### Освещение
- [ ] Паттерн выбран (Rembrandt, Loop, Butterfly, Split)
- [ ] Направление указано (45°, from left, etc.)
- [ ] Modifier описан (softbox, diffused window light)

### Камера
- [ ] Camera model (Sony, Canon, Leica)
- [ ] Lens + aperture (85mm f/1.4)
- [ ] Depth of field (f/5.6-f/8 для full-body)

### Negative Prompts
- [ ] Core set присутствует
- [ ] Anti-realism добавлен
- [ ] Subject-specific если нужно

---

## Quick Actions

| Команда | Действие |
|---------|----------|
| `реализм: [идея]` | Генерация реалистичного промпта (RU) |
| `realism: [idea]` | Генерация реалистичного промпта (EN) |
| `linkedin photo` | Professional headshot |
| `instagram real` | Lifestyle candid |
| `editorial` | Dramatic portrait |
| `beauty` | Glamour portrait |
