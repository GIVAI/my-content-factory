# LaoZhang — Генерация изображений через Gemini 3 Pro

> Настройка и использование генерации картинок через LaoZhang API
> **Триггеры:** "laozhang", "настроить генерацию", "nano banana api", "картинки api", "генерация картинок"

---

## Что это

LaoZhang API — доступ к генерации изображений через Gemini 3 Pro за $0.05/картинка. Фотореалистичные изображения до 4K, face swap, референсы.

Альтернатива: SYNTX — агрегатор нейросетей.

---

## Настройка (5 минут)

### Шаг 1: Получи API ключ

**Вариант A — LaoZhang ($0.05/картинка):**
1. Зарегистрируйся: https://api.laozhang.ai/register/
2. Пополни баланс (минимум $1 = 20 картинок)
3. Скопируй API ключ (начинается с `sk-`)

**Вариант B — SYNTX (агрегатор нейросетей):**
1. Перейди: https://t.me/syntxaibot
2. Следуй инструкциям бота

### Шаг 2: Сохрани ключ

Создай файл `.env` в корне проекта:

```
LAOZHANG_API_KEY=sk-твой-ключ-здесь
```

⚠️ `.env` уже в `.gitignore` — ключ не попадёт в репозиторий.

### Шаг 3: Готово

Скажи Claude: `Сгенерируй картинку: предприниматель в офисе`

---

## Как генерировать (инструкция для Claude Code)

### ⚠️ ВАЖНО: Правильный endpoint

**Используй ТОЛЬКО этот endpoint для Gemini 3 Pro:**

```
POST https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent
```

❌ НЕ используй `/v1/chat/completions` — это другой формат, даёт низкое качество.

### Базовая генерация

```bash
curl -X POST "https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LAOZHANG_API_KEY" \
  --max-time 180 \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate an image: ПРОМПТ НА АНГЛИЙСКОМ"}]
    }],
    "generationConfig": {
      "responseModalities": ["IMAGE"],
      "imageConfig": {
        "aspectRatio": "16:9",
        "imageSize": "4K"
      }
    }
  }'
```

### Парсинг ответа

Ответ содержит base64 в `candidates[0].content.parts[].inlineData.data`:

```python
import json, base64

response = json.loads(raw_response)
for part in response["candidates"][0]["content"]["parts"]:
    if "inlineData" in part:
        img_data = base64.b64decode(part["inlineData"]["data"])
        with open("result.png", "wb") as f:
            f.write(img_data)
        print(f"✅ Сохранено: result.png ({len(img_data)} байт)")
```

### Генерация с референсом (face swap, стиль)

```bash
curl -X POST "https://api.laozhang.ai/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LAOZHANG_API_KEY" \
  --max-time 180 \
  -d '{
    "contents": [{
      "parts": [
        {
          "inline_data": {
            "mime_type": "image/png",
            "data": "BASE64_ЗАКОДИРОВАННОЕ_ИЗОБРАЖЕНИЕ"
          }
        },
        {"text": "Using the person from [image1] as reference, create: ПРОМПТ"}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["IMAGE"],
      "imageConfig": {
        "aspectRatio": "16:9",
        "imageSize": "4K"
      }
    }
  }'
```

---

## Параметры

### Соотношение сторон (aspectRatio)

| Значение | Для чего | Разрешение 4K |
|----------|----------|---------------|
| `"16:9"` | YouTube обложки, баннеры | 5504×3072 |
| `"3:4"` | Карусели Instagram | 2880×3840 |
| `"4:3"` | Горизонтальные фото | 3840×2880 |
| `"9:16"` | Stories, Reels обложки | 3072×5504 |
| `"1:1"` | Аватарки, посты | 4096×4096 |

### Качество (imageSize)

| Размер | Качество | Время генерации |
|--------|----------|-----------------|
| `"1K"` | Черновик | 15-25 сек |
| `"2K"` | Хорошее | 25-45 сек |
| `"4K"` | Максимальное | 40-70 сек |

**Рекомендация:** Всегда используй `"4K"` — разница в цене нулевая ($0.05).

---

## Критичные правила (из опыта отладки)

1. **Endpoint** — ТОЛЬКО `/v1beta/models/gemini-3-pro-image-preview:generateContent`
2. **Таймаут** — минимум 180 секунд (`--max-time 180`). 4K генерация до 70 сек
3. **imageConfig обязателен** — без него изображение будет маленьким и некачественным
4. **responseModalities: ["IMAGE"]** — без этого получишь текст вместо картинки
5. **Промпт на английском** — Gemini лучше понимает английские промпты
6. **Один запрос = одна картинка** — не пытайся генерировать пакетом

---

## Примеры промптов

### Обложка YouTube
```
Professional YouTube thumbnail: confident man pointing at camera 
with surprised expression, dramatic studio lighting with rim light, 
bold contrasting colors, text space on the right side, 
cinematic composition, shot on Canon R5 with 35mm lens
```

### Портрет эксперта
```
Professional headshot portrait of a 35-year-old woman psychologist,
warm smile, natural skin texture with visible pores, 
shot on Sony A7IV with 85mm f/1.4 lens, Rembrandt lighting,
soft neutral background, business casual attire
```

### Карусель Instagram
```
Clean modern slide design for Instagram carousel,
white background with subtle gradient, 
large bold typography in dark gray,
minimal geometric accent elements in coral color #FF6B35,
professional and elegant, no photos
```

### UGC контент
```
Young woman 25 years old recording herself on iPhone in a cozy cafe,
natural window lighting, casual outfit, genuine smile,
candid moment, slightly messy table with coffee cup,
shot on iPhone 15 Pro, natural colors, no filters
```

---

## Проверка баланса

```bash
curl -s "https://api.laozhang.ai/v1/user/balance" \
  -H "Authorization: Bearer $LAOZHANG_API_KEY" | python3 -m json.tool
```

---

## Доступные модели

| Модель | Endpoint | Качество | Цена |
|--------|----------|----------|------|
| **gemini-3-pro-image-preview** | `/v1beta/...generateContent` | 4K, референсы, лучшее | $0.05 |
| gemini-2.5-flash-image | `/v1/chat/completions` | Базовое, быстрее | Дешевле |
| sora_image | `/v1/chat/completions` | Простое | $0.01 |

**Рекомендация:** Всегда используй `gemini-3-pro-image-preview` — качество несравнимо.

---

## Troubleshooting

| Проблема | Причина | Решение |
|----------|---------|---------|
| Маленькое/размытое | Нет `imageConfig` | Добавь `imageSize: "4K"` |
| Текст вместо картинки | Нет `responseModalities` | Добавь `["IMAGE"]` |
| Timeout | Таймаут < 180 сек | Увеличь `--max-time 180` |
| 429 ошибка | Rate limit | Подожди 30 сек, повтори |
| Invalid token | Неправильный ключ | Проверь API ключ в `.env` |
| Нет баланса | $0 на счёте | Пополни на api.laozhang.ai/dashboard |

### Нет API ключа?
- LaoZhang: https://api.laozhang.ai/register/
- SYNTX: https://t.me/syntxaibot

---

## Связанные скиллы

- **nano-banana/** — методология промптов, Identity Kit, face swap
- **nano-banana-pro-prompts/** — продвинутые промпты для реализма

---

*Фабрика Контента • LaoZhang Onboarding v1.0*
