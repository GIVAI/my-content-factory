# Veo 3.1 — Async API Guide

> Полный гайд по Async API для продакшн-генерации видео. Рекомендуемый метод.

---

## Почему Async?

| Преимущество | Описание |
|-------------|----------|
| ⭐ Не списывает деньги при ошибке | Sync — списывает! |
| ⭐ Стабильность | Не зависит от long connection |
| ⭐ Задачи живут 24 часа | Можно забрать позже |
| ⭐ Бесплатный поллинг | Проверять статус — бесплатно |
| ⭐ Batch support | Много задач параллельно |

---

## API Flow

```
1. POST /v1/videos → получить task_id
2. GET /v1/videos/{task_id} → поллить статус
3. GET /v1/videos/{task_id}/content → получить URL видео
4. Скачать mp4
```

---

## Endpoint: LaoZhang.ai

**Base URL:** `https://api.laozhang.ai/v1`
**Auth:** `Authorization: Bearer {VEO_API_KEY}`

---

## Step 1: Create Task

### Text-to-Video (JSON)
```bash
curl -s -X POST "https://api.laozhang.ai/v1/videos" \
  -H "Authorization: Bearer $VEO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "veo-3.1-fast",
    "prompt": "A cinematic shot of a majestic lion in the savannah."
  }'
```

### Image-to-Video (multipart/form-data)
```bash
curl -s -X POST "https://api.laozhang.ai/v1/videos" \
  -H "Authorization: Bearer $VEO_API_KEY" \
  -F "model=veo-3.1-fast-fl" \
  -F "prompt=Smooth timelapse transition between frames" \
  -F "input_reference=@start_frame.jpg" \
  -F "input_reference=@end_frame.jpg"
```

### Response
```json
{
  "id": "task_abc123",
  "status": "queued",
  "created_at": "2026-01-31T12:00:00Z"
}
```

---

## Step 2: Poll Status

```bash
curl -s "https://api.laozhang.ai/v1/videos/{task_id}" \
  -H "Authorization: Bearer $VEO_API_KEY"
```

### Статусы задачи

| Статус | Описание | Действие |
|--------|----------|----------|
| `queued` | В очереди | Поллить дальше (5-10 сек) |
| `processing` | Генерируется | Поллить дальше |
| `completed` | Готово | Забрать контент |
| `failed` | Ошибка | Проверить error. **НЕ списывает деньги** |

### Response (processing)
```json
{
  "id": "task_abc123",
  "status": "processing",
  "progress": 45
}
```

### Response (completed)
```json
{
  "id": "task_abc123",
  "status": "completed",
  "output": {
    "url": "https://..../video.mp4",
    "duration": 8,
    "resolution": "1080p"
  }
}
```

---

## Step 3: Get Content

```bash
curl -s "https://api.laozhang.ai/v1/videos/{task_id}/content" \
  -H "Authorization: Bearer $VEO_API_KEY"
```

Response содержит URL для скачивания.

---

## Step 4: Download

```bash
curl -s -o output.mp4 "{video_url}"
```

⚠️ **Видео хранятся 24 часа** → скачивать сразу!

---

## Batch Processing

### Стратегия
1. Создать N задач параллельно (POST /v1/videos × N)
2. Собрать все task_id
3. Поллить все одновременно
4. Скачивать по мере готовности

### Пример batch JSON для `async-video.py`
```json
[
  {
    "prompt": "Smooth timelapse: leather being stripped",
    "start_frame": "frames/frame-1.jpg",
    "end_frame": "frames/frame-2.jpg",
    "output": "segment-1-2.mp4"
  },
  {
    "prompt": "Smooth timelapse: foam being replaced",
    "start_frame": "frames/frame-2.jpg",
    "end_frame": "frames/frame-3.jpg",
    "output": "segment-2-3.mp4"
  }
]
```

### Запуск
```bash
python3 scripts/async-video.py --batch batch.json --output-dir ./videos/
```

---

## Gemini API Async Pattern (для справки)

Если работаем напрямую с Gemini API (не через LaoZhang):

```python
from google import genai
from google.genai import types

client = genai.Client()

# Create task
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="A cinematic shot of a majestic lion.",
    config=types.GenerateVideosConfig(
        negative_prompt="cartoon, drawing, low quality",
        aspect_ratio="16:9",
        resolution="1080p"
    ),
)

# Poll
import time
while not operation.done:
    time.sleep(10)
    operation = client.operations.get(operation)

# Download
video = operation.response.generated_videos[0]
client.files.download(file=video.video)
video.video.save("output.mp4")
```

### First/Last Frame через Gemini API
```python
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="Smooth transition between scenes",
    image=first_frame,
    config=types.GenerateVideosConfig(
        last_frame=last_frame,
    ),
)
```

### Reference Images через Gemini API
```python
ref1 = types.VideoGenerationReferenceImage(
    image=dress_image, reference_type="asset")
ref2 = types.VideoGenerationReferenceImage(
    image=woman_image, reference_type="asset")

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="The woman walks through the garden...",
    config=types.GenerateVideosConfig(
        reference_images=[ref1, ref2],
    ),
)
```

### Video Extension через Gemini API
```python
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    video=previous_operation.response.generated_videos[0].video,
    prompt="The character continues walking toward the sunset...",
    config=types.GenerateVideosConfig(
        number_of_videos=1,
        resolution="720p"
    ),
)
```

---

## Timeouts & Retry

| Параметр | Значение |
|----------|----------|
| Poll interval | 5-10 сек |
| Max timeout | 600 сек (10 мин) |
| Request latency | 11s — 6 min |
| Task lifetime | 24 часа |
| Video retention | 2 дня |

### Retry Strategy
```
При failed → проверить error message
При timeout → увеличить timeout, проверить prompt complexity
При 413 → конвертировать PNG→JPEG, уменьшить размер
При 429 → backoff, подождать 30 сек
```

---

## Script: async-video.py

Полный скрипт в `scripts/async-video.py`. Поддерживает:

- Text-to-Video
- Image-to-Video (single frame)
- First/Last Frame (timelapse)
- Batch mode (JSON file)

```bash
# Text-to-Video
python3 scripts/async-video.py --prompt "A cat playing" \
  --model veo-3.1-fast --output cat.mp4

# First/Last Frame
python3 scripts/async-video.py --prompt "Smooth transition" \
  --model veo-3.1-fast-fl \
  --start-frame start.jpg --end-frame end.jpg \
  --output transition.mp4

# Batch
python3 scripts/async-video.py --batch batch.json \
  --output-dir ./videos/
```
