# Veo 3.1 — Best Practices

> Лучшие практики: оптимизация качества, стоимости и стабильности генерации.

---

## Model Selection Strategy

### По сценарию
| Сценарий | Модель | Почему |
|----------|--------|--------|
| Тест промпта | `veo-3.1-fast` | Дешево, быстро |
| Финальное видео | `veo-3.1` | Максимальное качество |
| Таймлапс (быстро) | `veo-3.1-fast-fl` | Кадры + скорость |
| Таймлапс (качество) | `veo-3.1-fl` | Кадры + качество |
| YouTube горизонтальное | `veo-3.1-landscape` | Правильный AR |
| Батч генерация | `veo-3.1-fast` | 70% fast + 30% standard |
| A/B тестирование | `n=2-3` на fast | Выбрать лучший |
| Character consistency | + seed + refs | Использовать одинаковый seed |

### Оптимизация стоимости
- **Тестирование:** fast модели, `n=1`
- **Продакшн:** standard модели, `n=2-3` (выбрать лучший)
- **Батч:** 70% fast + 30% standard для A/B

---

## Sync vs Async API

| Фича | Sync (`/v1/chat/completions`) | Async (`/v1/videos`) |
|------|------|------|
| Workflow | Один запрос, ждать | Создать → поллинг |
| Кадры (image) | URL и Base64 | URL (multipart upload) |
| **Оплата при ошибке** | ❌ Списывает | ⭐ НЕ списывает |
| Стабильность | Зависит от соединения | ⭐⭐⭐⭐⭐ |
| Прогресс | Streaming output | Поллинг % |
| Timeout | Нужен длинный | Задачи независимы |
| **Для чего** | Быстрые тесты | **Продакшн, батч** |

→ Подробности: [async-api.md](async-api.md)

---

## Image-to-Video Best Practices

### Требования к изображениям
- JPEG формат (не PNG — слишком большой)
- Чёткое, хорошо освещённое
- Макс 20 MB
- Консистентный стиль между start/end frame

### Правило "Prompt for Motion Only"
Source image УЖЕ задаёт субъект, сцену, стиль. Промпт — ТОЛЬКО движение.
- ❌ Переописывать персонажа, фон, освещение
- ✅ Camera movement, subject animation, environmental changes

### Общие термины для персонажей
`"the subject"`, `"the woman"`, `"he"`, `"she"`, `"they"`

### Три типа движения
1. **Camera Motion:** `"Slow dolly in on the subject."`
2. **Subject Animation:** `"Hair and clothes flutter in the wind."`
3. **Environmental Animation:** `"Fog rolls in slowly across the landscape."`

---

## Reference Images (Ingredients to Video)

### Когда использовать
- Сохранение внешности персонажа между клипами
- Консистентность продукта/объекта
- Применение конкретного стиля

### Правила
- До 3 изображений
- Лучшие ракурсы: neutral + profile/3/4 + in-action
- Освещение в refs = освещение в промпте
- Только Veo 3.1, только 8s, только 16:9
- reference_type: `"asset"` для объектов/одежды

### Пример
```python
dress_ref = types.VideoGenerationReferenceImage(
    image=dress_image, reference_type="asset")
woman_ref = types.VideoGenerationReferenceImage(
    image=woman_image, reference_type="asset")
```

---

## Video Extension

### Когда использовать
- Длинные сцены (до 148 секунд)
- Продолжение действия из текущего клипа
- Удлинение с фоновым аудио

### Правила
- Только Veo-сгенерированные видео
- Только 720p
- Продление на 7 сек, до 20 раз
- Input макс: 141 сек
- Output макс: 148 сек
- Голос передаётся из последней 1 секунды
- Новый промпт для каждого продления

### Ограничения
- Голос не продлевается если его нет в последней 1 сек
- Видео должно быть из предыдущей генерации (не загруженное извне)
- Aspect ratio: 9:16 или 16:9 only

---

## Character & Voice Consistency

### 4-шаговый метод
1. **Карточка персонажа** — зафиксировать: возраст, волосы, одежда, определяющие черты
2. **Copy-paste** в каждый промпт — менять ТОЛЬКО действие/сцену
3. **Один seed** для всех сцен — визуальная + голосовая стабильность
4. **Reference images** — до 3 для идентичности через Ingredients to Video

### Голосовая консистентность
Описать голос в каждом промпте: `"In a voice that is crisp and clear, with a thoughtful analytical tone and a standard American accent"`

### Gemini как помощник
- Дать Gemini character card → попросить сгенерировать scene prompts
- Использовать Gemini для обогащения простых промптов
- Gemini может оценить результат на соответствие бренд-гайдлайнам

---

## 1080p Quality Optimization

### Чеклист для максимальной чёткости
1. `resolution: "1080p"` + `durationSeconds: "8"` (1080p только при 8s)
2. Одно движение камеры (не комбинировать)
3. Описать освещение конкретно и однозначно
4. Не стакать конфликтующие стили
5. 1-3 reference images для identity
6. Start/end frames для smoother motion
7. Минимальный постпродакшн (Veo уже high-fidelity)

### Troubleshooting 1080p
| Симптом | Причина | Решение |
|---------|---------|---------|
| Identity drift | Inconsistent refs/lighting | 3 refs + seed + карточка |
| Flicker/stutter | Conflicting camera | Static camera или 1 movement |
| Soft frames | Overloaded prompt | Убрать лишние стили |
| Smeary fast action | Too much motion | Разбить на beats, anchor frames |

---

## Workflow Patterns

### Pattern 1: Quick Test → Final
```
fast модель (n=1) → проверить → standard (n=2) → выбрать лучший
```

### Pattern 2: Timelapse Chain
```
Nano Banana keyframes → Veo fast-fl (пары) → CapCut assembly
```

### Pattern 3: Multi-Shot Story
```
Character card → Reference images → Veo 3.1 per-shot → Edit
```

### Pattern 4: Long Video (Extension)
```
Initial 8s → Extend ×5 → Extend ×5 → 80+ seconds
```

---

## Aspect Ratios & Platforms

| Платформа | Ratio | Модель |
|-----------|-------|--------|
| YouTube | 16:9 | `veo-3.1-landscape` |
| Shorts / Reels / TikTok | 9:16 | `veo-3.1` (default portrait) |
| Instagram Feed | 9:16 or 16:9 | По контексту |
| Stories | 9:16 | `veo-3.1` |
| Twitter/X | 16:9 | `veo-3.1-landscape` |

---

## Batch Generation

### Параметр `n` (1-4)
```json
{"n": 4, "model": "veo-3.1-fast"}
```
Стоимость: `n × цена_модели`

### Concurrent Requests (Async)
Создать несколько задач параллельно, поллить все одновременно.
→ См. `scripts/async-video.py`

---

## Типичные ошибки

| # | Ошибка | Фикс |
|---|--------|------|
| 1 | Размытый промпт | Камера + субъект + действие + контекст |
| 2 | Противоречия в стиле | Один intent на ось |
| 3 | Нет камеры | Shot type + movement + lens |
| 4 | Нет аудио | SFX + ambient + music level |
| 5 | Длинный диалог | ≤ 8 секунд речи |
| 6 | Сложная сцена | Разбить на 8-сек клипы |
| 7 | Нет техпараметров | AR + resolution + duration |
| 8 | Один проход | generate → extend → refine |
| 9 | Переописание в i2v | Prompt for motion only! |
| 10 | Нет seed для consistency | Один seed для всех сцен |

---

## Pricing через LaoZhang.ai

| Модель | Цена | С $100 пополнением |
|--------|------|---------------------|
| Standard | $0.25/запрос | ≈ ¥1.7/запрос |
| Fast | $0.15/запрос | ≈ ¥1.0/запрос |

**Billing:**
- ✅ Async: оплата только при успехе
- ❌ Sync: оплата даже при ошибке
- ✅ Поллинг бесплатно
