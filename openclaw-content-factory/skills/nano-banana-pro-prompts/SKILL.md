---
name: nano-banana-pro-prompts
description: "Библиотека продвинутых промптов для генерации изображений — стили, персонажи, сцены"
triggers:
  - промпты для картинок
  - image prompts
  - библиотека промптов
  - nano banana pro
---

# NanoBanana Pro Prompts — Библиотека

Продвинутые промпты для генерации изображений: готовые шаблоны для разных задач.

## Быстрый старт

```bash
# Промпт для карусели
"Сгенерируй промпт для обложки карусели на тему: [ТЕМА]"

# Промпт для аватара
"Промпт для профессионального портрета {ваш эксперт}"

# Промпт для Reels обложки
"Промпт для обложки reels: [ОПИСАНИЕ]"
```

## Категории промптов

### 1. Портреты и аватары
```
Professional headshot of [PERSON DESCRIPTION], studio lighting, 
shallow depth of field, neutral background, confident expression, 
shot on Canon EOS R5, 85mm f/1.4
```

### 2. Обложки для контента
```
Bold typography overlay mockup, [TOPIC] theme, modern gradient 
background [COLORS], clean minimalist design, social media ready, 
16:9 aspect ratio
```

### 3. Метафоры и концепции
```
Visual metaphor for [CONCEPT], photorealistic style, dramatic 
lighting, cinematic composition, [MOOD] atmosphere, 
high detail, 4K resolution
```

### 4. Продуктовые
```
Product showcase of [PRODUCT], floating in air, soft shadows, 
gradient background, premium feel, commercial photography style
```

### 5. Lifestyle / Behind the scenes
```
Candid shot of [PERSON] working at [LOCATION], natural light 
from window, warm tones, authentic feel, documentary style
```

## Модификаторы

| Модификатор | Эффект |
|-------------|--------|
| `--ar 16:9` | Горизонтальный формат |
| `--ar 9:16` | Вертикальный (Reels/Stories) |
| `--ar 1:1` | Квадрат (Instagram) |
| `cinematic lighting` | Кинематографичность |
| `shot on [camera]` | Фотореализм |
| `minimalist` | Чистый дизайн |
| `dramatic` | Контрастность |

## Стили

| Стиль | Ключевые слова |
|-------|---------------|
| Фотореализм | photorealistic, shot on Canon, 85mm, natural light |
| Кинематограф | cinematic, anamorphic, film grain, color grading |
| Минимализм | minimalist, clean, white space, geometric |
| Неон | neon lights, cyberpunk, vibrant colors, dark background |
| Винтаж | vintage, film photography, faded colors, retro |

## Identity Lock (сохранение лица)

Для серии изображений с одним персонажем:
1. Загрузить референсное фото
2. В промпте указать `[image1]` для привязки
3. Описывать только изменения (одежда, фон, поза)

```
[image1] same person, now wearing business suit, standing in 
modern office, confident pose, same facial features
```

## Частые ошибки

❌ Промпт на русском — модели лучше понимают английский
❌ Слишком длинный промпт — оптимально 30-60 слов
❌ Без указания стиля — результат непредсказуем
❌ Без aspect ratio — получится дефолтный квадрат
❌ Абстрактные описания — нужна конкретика (цвета, материалы, освещение)
