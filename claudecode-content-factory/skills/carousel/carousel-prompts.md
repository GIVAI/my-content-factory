# Carousel Prompts

NanoBanana шаблоны для генерации слайдов карусели.

---

## Общие правила

### Aspect Ratio
**Всегда 4:5** — стандарт Instagram карусели.
```
Aspect ratio 4:5.
```

### 7 категорий NanoBanana
Каждый промпт должен покрывать:
1. **Subject** — кто/что + детали
2. **Environment** — где + контекст
3. **Lighting** — тип + направление + качество
4. **Style** — фотореалистичный/художественный
5. **Camera** — оборудование + настройки
6. **Composition** — кадрирование + перспектива
7. **Quality/Mood** — атмосфера + детализация

### Identity Lock (если референс)
```
[Image1] is reference for person identity.
Must look 1000% identical to person in [Image1].
Preserve exact facial features, proportions, skin texture.
No beauty filters, no smoothing.
```

### Консистентность между слайдами
Зафиксировать для всей карусели:
```
VISUAL STYLE LOCK:
- Color palette: [colors]
- Lighting: [type + direction]
- Mood: [atmosphere]
- Background style: [description]
```

---

## Шаблон: PROMPT CAROUSEL

### Hook слайд
```
A stunning [style] photograph of [subject doing action] in [environment].
[Lighting description] creating [mood].
The image showcases [key visual element].
Shot on [camera], [lens], [aperture].
Photorealistic, ultra-detailed, sharp focus.
Aspect ratio 4:5.

Leave clean space at the bottom 20% of the image for text overlay.
Dark gradient at bottom for text readability.
```

### Body слайды (с промптом overlay)

**Вариант A: Текст в NanoBanana**
```
A [style] photograph of [subject] in [environment].
[Lighting]. [Mood].
Shot on [camera], [lens].
High quality, detailed.
Aspect ratio 4:5.

Include text overlay at the bottom of the image on semi-transparent dark banner:
"[ПОЛНЫЙ ТЕКСТ ПРОМПТА]"
White sans-serif font, readable size.
Text banner should not exceed 25% of image height.
```

**Вариант B: Чистое фото (текст в редакторе)**
```
A [style] photograph of [subject] in [environment].
[Lighting]. [Mood].
Shot on [camera], [lens].
High quality, detailed.
Aspect ratio 4:5.

Leave clean gradient space at the bottom 20-25% of the image.
This zone is for text overlay — no important visual elements here.
Subtle dark gradient from transparent to dark at bottom edge.
```

### Примеры по тематикам

#### Luxury Lifestyle
```
Ultra-luxury lifestyle photograph of [person] relaxing in a private jet cabin.
Soft natural light streaming through oval windows, warm golden hour tones.
Cream leather interior, champagne glasses, premium details visible.
Person wearing designer casual outfit, relaxed confident expression.
Shot on Hasselblad, 80mm lens, f/2.8.
Photorealistic, magazine quality, cinematic color grading.
Aspect ratio 4:5.

Leave clean space at bottom 20% for prompt text overlay.
```

#### Portrait Photography
```
Professional studio portrait of [person description].
Rembrandt lighting setup with key light at 45 degrees.
Dark moody background with subtle gradient.
Subject looking directly at camera, [expression].
Shot on Canon R5, 85mm f/1.4 lens.
Shallow depth of field, sharp focus on eyes.
High-end beauty retouch, natural skin texture preserved.
Aspect ratio 4:5.

Leave clean space at bottom 20% for prompt text overlay.
```

#### Product Photography
```
High-end product photograph of [product] on [surface].
Professional studio lighting: key light with softbox, fill light, rim light.
[Color] seamless background, subtle shadow for depth.
Product positioned at slight angle to show dimensionality.
Shot on Phase One, 120mm macro lens, f/11.
Ultra-sharp focus, every detail visible.
Commercial quality, clean aesthetic.
Aspect ratio 4:5.

Leave clean space at bottom for text overlay.
```

#### Cinematic Scene
```
Cinematic still of [subject] in [dramatic environment].
Atmospheric lighting with [color] key light and [color] accent.
Volumetric haze/fog adding depth and mood.
[Action/pose] conveying [emotion].
Shot on Arri Alexa with anamorphic lens, slight lens flare.
Film grain, cinematic color grade (teal and orange palette).
Aspect ratio 4:5.

Leave clean space at bottom 20% for prompt text overlay.
```

---

## Шаблон: EXPERT CAROUSEL

### Hook слайд (с человеком)

**Без референса (AI персонаж):**
```
Professional photo of a [age] year old [gender] [ethnicity] expert.
[Hair description], [clothing: business casual/professional].
Standing/sitting in [environment: modern office/studio/outdoor].
Confident, approachable expression, slight smile, looking at camera.
Natural daylight from large window, soft shadows.
Shot on Sony A7IV, 35mm lens, f/2.8.
Clean, modern aesthetic.
Aspect ratio 4:5.

Leave space at bottom 30% for large title text:
"[NUMBER] [TOPIC] TIPS"
```

**С референсом [Image1]:**
```
[Image1] is reference for person identity.
Must look 1000% identical to person in [Image1].

Professional photo of this exact person in [environment].
[Clothing description], [pose: standing confidently/gesturing].
[Expression: friendly, engaging, confident].
Natural lighting from [direction], soft and flattering.
Shot on Sony A7IV, 35mm lens, f/2.8.
Aspect ratio 4:5.

Leave space at bottom for title text overlay.
```

### Content слайды
Expert carousel часто не требует AI для content слайдов:
- Скриншоты интерфейсов
- Логотипы/иконки сервисов
- Простая графика в Canva

Если нужен AI:
```
Clean mockup/illustration representing [concept/tool].
Minimalist style, [brand colors if known].
Central composition, clear focal point.
Modern, professional aesthetic.
Soft even lighting, no harsh shadows.
Aspect ratio 4:5.
```

### CTA слайд
```
[Image1] is reference for person identity (if available).

Photo of [person] in casual professional setting.
Friendly, inviting expression, slight smile.
Looking at camera, open body language.
Soft natural lighting.
Shot on Sony A7R, 50mm lens.
Aspect ratio 4:5.

Leave space for:
- Username handle at top
- "Follow for more" text at bottom
- Social media icons
```

---

## Шаблон: VIRAL/BRIGHT CAROUSEL

### Hook слайд
```
Dramatic portrait of [person description] facing camera directly.
Dark moody environment with [smoke/particles/bokeh] effects.
[Neon color: cyan/magenta/lime] accent lighting from side.
Intense, knowing expression — like sharing a secret.
High contrast, deep shadows, selective highlights.
Shot on Sony A7SIII, 85mm lens, f/1.4.
Cinematic color grading, slight film grain.
Aspect ratio 4:5.

Space at top for "SECRET" or "BREAKING" badge.
Space at bottom for intriguing headline.
```

### Body слайды
```
[Subject/concept] visualized in dark dramatic style.
Black background (#0a0a0a) with [color] neon accents.
[Relevant visual element] highlighted with glow effect.
Moody, mysterious atmosphere.
High contrast, selective lighting.
Aspect ratio 4:5.
```

### CTA слайд
```
Photo of [person/avatar] with dramatic lighting.
Dark background with subtle [color] glow.
Expression: friendly but mysterious.
Looking at camera.
Shot with portrait lens, shallow depth of field.
Aspect ratio 4:5.

Clean space for:
- "Was this helpful?" text
- "Follow @handle for more"
- Social engagement icons
```

---

## Шаблон: MINIMALIST CAROUSEL

Minimalist карусели обычно создаются в дизайн-инструментах (Canva, Figma).

Если нужен AI для фона:
```
Abstract minimalist background.
Subtle gradient from [color1 hex] to [color2 hex].
Clean, modern aesthetic.
No objects, no patterns, just smooth color transition.
Aspect ratio 4:5.
```

Или текстурный фон:
```
Minimalist textured background.
Soft [color] with subtle noise/grain texture.
Paper-like quality, elegant simplicity.
No objects or distracting elements.
Aspect ratio 4:5.
```

---

## Text Overlay техники

### Вариант 1: Текст внутри NanoBanana
```
Include text overlay: "[YOUR TEXT HERE]"
Position: bottom of image
Style: white text on semi-transparent dark banner (#000000, 70% opacity)
Font: bold sans-serif (like Helvetica or Inter)
Size: easily readable, not too small
Banner height: 20-25% of image
Padding: 16px
```

### Вариант 2: Чистая зона для редактора
```
Leave clean space at the bottom 20-25% of the image.
This zone is reserved for text overlay to be added later.
No important visual elements in this zone.
Subtle gradient: transparent at top → dark at bottom edge.
This creates natural text readability zone.
```

### Вариант 3: Плашка/карточка
```
Include a clean white/dark card at [position] of image.
Card size: approximately 60% width, 30% height.
Rounded corners (16px radius).
Subtle shadow for depth.
Leave card interior empty for text overlay.
```

---

## Консистентность: Style Lock

Перед генерацией серии слайдов, определить и зафиксировать:

```markdown
## CAROUSEL STYLE LOCK

### Visual Constants
- Color palette: [primary], [secondary], [accent]
- Background: [description]
- Lighting: [type], [direction], [quality], [color temperature]
- Mood: [atmosphere description]

### Person Identity (if applicable)
- Reference: [Image1] или [character description]
- Clothing: [outfit description]
- Expression range: [neutral → excited → thoughtful]

### Technical Settings
- Camera: [model]
- Lens: [focal length + aperture]
- Style: [photorealistic/cinematic/editorial]
- Color grading: [warm/cool/neutral/teal-orange]

### Text Overlay Style
- Method: [NanoBanana/Editor]
- Position: [bottom/top/card]
- Banner style: [dark transparent/light/none]
- Font style: [bold sans-serif/serif/display]
```

### Пример Style Lock
```markdown
## CAROUSEL STYLE LOCK: Luxury Prompts

### Visual Constants
- Color palette: gold (#D4AF37), cream (#FFFDD0), black (#0a0a0a)
- Background: luxury interiors (private jet, yacht, penthouse)
- Lighting: golden hour, soft natural light, warm tones
- Mood: aspirational, exclusive, refined

### Person Identity
- Reference: [Image1] — must match exactly
- Clothing: designer casual, earth tones
- Expression range: relaxed → confident → contemplative

### Technical Settings
- Camera: Hasselblad
- Lens: 80mm, f/2.8
- Style: editorial fashion photography
- Color grading: warm, lifted shadows, rich midtones

### Text Overlay Style
- Method: NanoBanana (промпт на фото)
- Position: bottom 20%
- Banner: semi-transparent black
- Font: white, bold sans-serif
```

---

## Генерация серии слайдов

### Workflow

1. **Определить Style Lock** (один раз для всей карусели)

2. **Генерировать Hook** (слайд 1)
   - Самый впечатляющий визуал
   - Место для заголовка

3. **Генерировать Body** (слайды 2-N)
   - Применять Style Lock
   - Каждый с уникальным контентом
   - Консистентный стиль

4. **Генерировать CTA** (последний слайд)
   - Место для призыва
   - Фото автора (если есть референс)

### Пример серии промптов

**Слайд 1 (Hook):**
```
Ultra-luxury editorial photograph of a confident woman in late 20s
relaxing in a private jet cabin with cream leather interior.
Soft golden hour light through oval windows, warm champagne tones.
She wears an elegant cream cashmere sweater, looking pensively out window.
Shot on Hasselblad, 80mm lens, f/2.8.
Editorial fashion style, magazine quality.
Aspect ratio 4:5.
Leave bottom 25% for title: "LUXURY PROMPTS"
```

**Слайд 2:**
```
Same woman from [Image1/previous], now on yacht deck at sunset.
Golden hour backlighting creating warm rim light on hair and shoulders.
Wearing flowing white linen outfit, champagne glass in hand.
Looking at camera with confident, knowing smile.
Mediterranean sea in background, soft bokeh.
Shot on Hasselblad, 80mm lens, f/2.8.
Same editorial style as carousel hook.
Aspect ratio 4:5.
Bottom 20% for prompt text overlay on dark transparent banner.
```

**Слайд 3:**
```
Same woman, penthouse apartment with floor-to-ceiling windows.
City skyline at twilight as background.
Standing by window in elegant black dress.
Soft ambient interior lighting with city lights.
Sophisticated, urban luxury mood.
Shot on Hasselblad, 80mm lens, f/2.8.
Consistent editorial style.
Aspect ratio 4:5.
Bottom zone for prompt text overlay.
```

---

## Troubleshooting

| Проблема | Решение |
|----------|---------|
| Слайды выглядят по-разному | Добавить Style Lock, повторять ключевые описания |
| Человек выглядит иначе | Усилить Identity Lock: "1000% identical", детали лица |
| Текст нечитаемый | Указать "dark gradient at bottom for text readability" |
| Фон слишком активный | Добавить "clean, uncluttered background" |
| Не тот aspect ratio | Явно указать "Aspect ratio 4:5" в конце промпта |
| Промпт на фото плохо читается | Уменьшить промпт, увеличить banner height |

---

## Quick Reference: Базовый шаблон

```
[STYLE] photograph of [SUBJECT] in [ENVIRONMENT].
[LIGHTING description] creating [MOOD].
[Additional details, props, actions].
Shot on [CAMERA], [LENS], [APERTURE].
[Quality descriptors].
Aspect ratio 4:5.

[TEXT OVERLAY INSTRUCTIONS IF NEEDED]
```
