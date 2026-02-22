---
name: veo-video
description: "Veo 3.1 video generation — timelapse pipeline, text-to-video, image-to-video, reference images, video extension. Use when user asks to create video, timelapse, animation, video transition, animate an image, extend a video. Covers full pipeline: keyframes → approval → video generation → delivery."
triggers:
  - таймлапс
  - timelapse
  - видео
  - video
  - анимация
  - animate
  - оживить картинку
  - image to video
  - переход между кадрами
  - veo
  - сгенерировать видео
  - продлить видео
  - extend video
---

# Veo 3.1 Video Generator

Full pipeline for AI video generation: text-to-video, image-to-video, reference images, first/last frame, video extension, timelapse.

## Core Principle

```
Direct the scene like a filmmaker — don't describe it like a bystander.
```

Every prompt = camera + subject + action + context + style + audio + constraints.

---

## File Router

| Запрос содержит | Файл |
|-----------------|------|
| промпт-гайд, prompting, как писать промпт | [references/prompting-guide.md](references/prompting-guide.md) |
| best practices, лучшие практики, оптимизация | [references/best-practices.md](references/best-practices.md) |
| async api, async, батч, polling | [references/async-api.md](references/async-api.md) |
| библиотека промптов, примеры, prompt library | [references/prompt-library.md](references/prompt-library.md) |
| таймлапс, timelapse, пайплайн кадров | See [Timelapse Pipeline](#timelapse-pipeline) |

---

## Quick Actions

| Команда | Действие |
|---------|----------|
| `"таймлапс: [идея]"` | Запуск полного пайплайна таймлапса |
| `"видео: [описание]"` | Text-to-video генерация |
| `"оживи: [описание]"` | Image-to-video (одна картинка) |
| `"переход: [описание]"` | First→Last frame transition |
| `"продли: [описание]"` | Extend video (продлить на 7 сек) |
| `"референс: [описание]"` | Ingredients-to-video (до 3 ref images) |

---

## API Configuration

> **⚠️ НАСТРОЙ API КЛЮЧИ перед использованием!**
> 
> Добавь в `.env` или `settings.local.json`:
> - `VEO_API_KEY` — для генерации видео (Veo 3.1)
> - `NANO_API_KEY` — для генерации кадров (Nano Banana Pro)
>
> Провайдер: [LaoZhang.ai](https://api.laozhang.ai) или Google AI Studio

### Два API формата

| API | Endpoint | Когда использовать |
|-----|----------|-------------------|
| **Sync** | `/v1/chat/completions` | Быстрые тесты, одиночные генерации |
| **Async** ⭐ | `/v1/videos` | Продакшн, батч, стабильность |

### Преимущества Async API
- ⭐ **Не списывает деньги при ошибке** (Sync — списывает!)
- ⭐ Стабильнее (не зависит от long connection)
- ⭐ Задачи живут 24 часа
- ⭐ Бесплатный поллинг статуса

Подробности: [references/async-api.md](references/async-api.md)

---

## Model Selection

| Модель | Цена | Скорость | Кадры | Ориентация | Когда |
|--------|-------|----------|-------|------------|-------|
| `veo-3.1-fast` | ~$0.15 | Быстро | ❌ | Портрет | Тесты, итерации |
| `veo-3.1` | ~$0.25 | Стандарт | ❌ | Портрет | Финальное качество |
| `veo-3.1-fast-fl` | ~$0.15 | Быстро | ✅ | Портрет | **Для таймлапсов** |
| `veo-3.1-fl` | ~$0.25 | Стандарт | ✅ | Портрет | Качественные таймлапсы |
| `veo-3.1-landscape` | ~$0.25 | Стандарт | ❌ | Пейзаж | YouTube горизонтальное |
| `veo-3.1-landscape-fl` | ~$0.25 | Стандарт | ✅ | Пейзаж | Горизонтальные переходы |

**Суффиксы:**
- `-fast` = быстрее, дешевле, ~85-90% качества
- `-fl` = поддержка first/last frame (image-to-video)
- `-landscape` = горизонтальная ориентация (16:9)

---

## Technical Specs

| Параметр | Значение |
|----------|----------|
| Разрешение | 720p (default), 1080p (только 8s) |
| Aspect Ratio | 16:9 (landscape), 9:16 (portrait). Нет 1:1 |
| Длительность | 4, 6, 8 секунд |
| FPS | 24 fps |
| Макс input image | 20 MB |
| Язык промптов | English only |
| Request latency | 11s – 6 min (peak hours) |
| Video retention | **2 дня** на сервере → скачивать сразу! |

---

## Capabilities Overview

### 1. Text-to-Video
Промпт → видео. Базовая генерация.

### 2. Image-to-Video
Одно изображение → анимация. Модель с `-fl`. **Правило: prompt for motion only!** Не переописывать изображение.

### 3. First & Last Frame (Interpolation)
Два кадра → плавный переход. Идеально для таймлапсов. Обязательно 8s.

### 4. Reference Images (до 3 шт.)
Для сохранения идентичности персонажа/объекта/стиля. Только Veo 3.1, только 8s, только 16:9.

### 5. Video Extension
Продлить Veo-видео на 7 сек, до 20 раз (макс 148 сек). Только 720p.

### 6. Timestamp Prompting
Мульти-шотовая последовательность:
```
[00:00-00:02] Medium shot, character enters...
[00:02-00:04] Close-up of hands...
[00:04-00:06] Tracking shot...
[00:06-00:08] Wide crane shot...
```

---

## Timelapse Pipeline

### Полный пайплайн

```
ИДЕЯ → KEYFRAMES (Nano Banana) → СОГЛАСОВАНИЕ → VIDEO (Veo 3.1-fl) → ДОСТАВКА mp4
```

### Phase 1: Идея
Брейнштормим: что трансформируется, из чего в что, сколько шагов (4-5 кадров).

### Phase 2: Keyframes (Nano Banana Pro)

**Правила:**
1. **ANCHOR PROMPT** — идентичный для ВСЕХ кадров (камера, локация, освещение)
2. **VARIABLE PART** — уникальный для каждого кадра (состояние трансформации)
3. **Формат:** 9:16 вертикальный, 2K
4. **Промпты на английском**
5. **PNG→JPEG** перед отправкой (4K PNG > 8MB → 413)
6. **Seed** — одинаковый для всех кадров

**Шаблон:**
```
[ANCHOR — identical for all frames]
Interior of a workshop, [object] centered in frame, shot from
[angle] at [distance]. [Lighting description]. Same setup throughout.

[VARIABLE — unique per frame]
Frame 1: The [object] shows [state 1]...
Frame 2: The [object] has been [state 2]...
Frame 3: The [object] is being [state 3]...
Frame 4: The [object] is [final state]...
```

### Phase 3: Согласование
Отправить кадры на ревью. Проверить консистентность и прогрессию.

### Phase 4: Video (Veo 3.1)

**Правила:**
1. Первое изображение = START, второе = END
2. Генерировать пары: frame1→2, frame2→3, frame3→4
3. Промпт описывает ПРОЦЕСС трансформации
4. **Ключевая фраза:** `Every change should appear as a physical build-up, never as a dissolve or crossfade.`
5. **Камера:** `static tripod, locked-off, no camera movement`

**Шаблон видео-промпта:**
```
Smooth realistic timelapse of [process]. Fixed camera angle,
no camera movement. Continuous physical transformation, realistic
lighting changes. No dissolves, no crossfades — only physical
build-up and assembly.
```

### Phase 5: Доставка
1. Сохранить mp4 в `content/videos/{project-name}/`
2. Отправить клиенту
3. Опционально: сборка в CapCut (ускоряет 8s→2-3s на сегмент)

---

## Prompt Formula

### 8-элементная формула (полная)
```
[Camera/Shot] + [Subject] + [Action] + [Setting] + [Style] + [Lighting] + [Audio] + [Constraints]
```

### Быстрая формула (минимум)
```
[Subject] + [Action] + [Setting] + [Camera] + [Lighting]
```

### DO ✅
- Камера конкретно: `"medium tracking shot, 35mm lens, slow dolly-in"`
- Аудио явно: `"SFX: thunder, ambient: rain, music: soft piano"`
- Негативный промпт: `"negative prompt: no subtitles, no text overlays"`
- Таймлапсы: `"static tripod"`, `"locked-off camera"`
- Диалог через двоеточие: `He says: Hello there`
- Image-to-video: **prompt for motion only**

### DON'T ❌
- Абстрактные описания: ~~"cool city scene"~~
- Противоречия: ~~"bright sunny film noir"~~
- Забывать камеру (случайный ракурс)
- Забывать аудио (модель угадает плохо)
- Цитаты для диалога — используй двоеточие
- Переописывать изображение в image-to-video

---

## Character Consistency

### Метод: Карточка персонажа + Seed

1. **Создать текстовую карточку:**
```
Clara, a historian in her early 30s, with observant dark brown eyes.
Chin-length black hair in a classic bob. Dark navy-blue wool coat
with a silk scarf with gold and cream designs.
```

2. **Copy-paste дословно** в каждый промпт
3. **Один seed** для всех сцен
4. **Reference images** (до 3) для сохранения внешности

---

## Cost Summary

### Таймлапс проект (4-5 кадров)
| Item | Qty | Price | Total |
|------|-----|-------|-------|
| Keyframes (Nano) | 4-5 | ~$0.05 | $0.20-0.25 |
| Video clips (Veo fast) | 3-4 | ~$0.15 | $0.45-0.60 |
| **TOTAL** | | | **~$0.70-0.85** |

---

## Troubleshooting

| Проблема | Решение |
|----------|---------|
| Камера дрифтит | `"static tripod, locked-off, no camera movement"` |
| Dissolve вместо трансформации | `"no dissolves, no crossfades, only physical build-up"` |
| Субтитры на видео | `"(no subtitles)"` + двоеточие для диалога |
| Нет аудио | Явно описать: `"SFX: ..., ambient: ..."` |
| 413 при отправке | PNG→JPEG перед отправкой |
| Sync timeout | Перейти на Async (`/v1/videos`) |
| Identity drift | Reference images + seed + карточка персонажа |
| Flicker / micro-stutter | Одно движение камеры, static camera |
| Inconsistent между клипами | Anchor prompt идентичен + один seed |

---

*Veo Video Skill v1.0 — Content Factory*
