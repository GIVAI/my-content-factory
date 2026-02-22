# Veo 3.1 — Prompting Guide

> Как режиссировать видео через промпты. Полная анатомия промпта и все техники.

---

## Формула промпта

### Официальная (Google, 5 элементов)
```
[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]
```

### Расширенная (8 элементов)
```
[Camera/Shot] + [Subject] + [Action] + [Setting] + [Style] + [Lighting] + [Audio] + [Constraints]
```

### Принцип "Директор, не описатель"

> 🎬 Думай как режиссёр, дающий указания съёмочной группе.

**Плохо:** `Person working on computer.`
**Хорошо:**
```
30-year-old woman in business casual attire typing on laptop at modern
wooden desk, side angle medium shot, natural window lighting from left,
focused expression, contemporary office with plants visible in background.
```

---

## Анатомия промпта

### 1. Subject (Субъект)

Кто/что в центре. Конкретность = качество.

- Люди: `"a seasoned detective"`, `"a joyful baker"`
- Животные: `"a playful Golden Retriever puppy"`
- Объекты: `"a vintage typewriter"`, `"a classic 1960s muscle car"`
- Фантастика: `"a miniature dragon with iridescent scales"`
- Комбинации: `"friends laughing around a campfire while a fox watches"`

**Character card** для постоянства:
```
John, a man in his 40s with short brown hair, wearing a blue jacket
and glasses, looking thoughtful
```
Copy-paste дословно в каждый промпт!

### 2. Action (Действие)

- Базовые: `walking, running, jumping, dancing, spinning`
- Взаимодействия: `talking, laughing, cooking, building`
- Эмоции: `smiling, frowning, showing excitement`
- Тонкие: `a gentle breeze ruffling hair`, `fingers tapping impatiently`
- Трансформации: `a flower blooming in fast-motion`, `ice melting`

### 3. Context / Scene

- Локация: `"a cozy living room with a crackling fireplace"`
- Время: `golden hour`, `midday`, `twilight`, `deep night`
- Погода: `clear blue sky`, `heavy thunderstorm`, `gentle snowfall`
- Эпоха: `"a medieval castle courtyard"`, `"a roaring 1920s jazz club"`
- Детали: `floating dust motes in a sunbeam`, `reflections on wet pavement`

### 4. Camera

**Самый мощный инструмент** для передачи тона и эмоций.

#### Углы камеры

| Термин | Описание |
|--------|----------|
| `Eye-level shot` | Нейтральная перспектива |
| `Low-angle shot` | Снизу вверх — мощь |
| `High-angle shot` | Сверху вниз — уязвимость |
| `Bird's-eye view` | Прямо сверху, карта |
| `Worm's-eye view` | С земли вверх |
| `Dutch angle` | Наклон — тревога |
| `Over-the-shoulder` | Через плечо — диалоги |
| `POV shot` | Глазами персонажа |

#### Движения камеры

| Термин | Описание |
|--------|----------|
| `Static shot` | Камера неподвижна |
| `Slow pan` | Горизонтальное вращение |
| `Tilt (up/down)` | Вертикальное вращение |
| `Dolly (in/out)` | Камера приближается/удаляется |
| `Tracking shot` | Следует за субъектом |
| `Truck (left/right)` | Горизонтальное движение параллельно |
| `Crane shot` | Подъём камеры вверх |
| `Aerial / drone` | С высоты |
| `Handheld` | Эффект ручной камеры |
| `Whip pan` | Сверхбыстрое панорамирование |
| `Arc shot` | Камера по дуге вокруг субъекта |

#### Оптика

| Термин | Эффект |
|--------|--------|
| `Shallow DOF` | Размытый фон, bokeh |
| `Deep DOF` | Всё в фокусе |
| `Wide-angle lens` | Широкий угол |
| `Telephoto lens` | Сжатие перспективы |
| `Lens flare` | Блики от света |
| `Rack focus` | Перевод фокуса |
| `Macro lens` | Экстремальный close-up |
| `Vertigo effect` | Dolly zoom — дезориентация |

**Пример комбинации:**
```
Medium eye-level shot with gentle dolly-in ~10% over 4 seconds,
shallow depth of field, 35mm lens look
```

### 5. Visual Style

#### Освещение
- Натуральное: `"soft morning sunlight"`, `"golden hour glow"`
- Искусственное: `"warm fireplace glow"`, `"pulsating neon signs"`
- Кинематограф: `"Rembrandt lighting"`, `"film noir deep shadows"`, `"high-key"`, `"low-key"`
- Спецэффекты: `"volumetric lighting"`, `"backlighting silhouette"`

#### Стили
- Фотореализм: `"ultra-realistic"`, `"shot on 8K camera"`
- Кинематограф: `"cinematic film look"`, `"shot on 35mm film"`
- Анимация: `"Japanese anime"`, `"Pixar-like 3D"`, `"claymation"`, `"stop-motion"`
- Veo хорошо понимает: `LEGO`, `Claymation`, `South Park`, `Pixar`, `8-bit retro`, `Origami`, `Anime`, `Marble`

### 6. Audio

#### Принцип Audio-First
> Если не задать аудио — модель угадает. Часто плохо.

1. **Диалог** — двоеточие (НЕ кавычки → субтитры!):
   ```
   A woman says: We have to leave now.
   ```

2. **SFX:**
   ```
   SFX: thunder cracks in the distance
   ```

3. **Ambient:**
   ```
   Ambient noise: the quiet hum of a starship bridge
   ```

4. **Музыка:**
   ```
   Soft lo-fi beat, low in the mix. Urban ambience evolves.
   ```

#### Правила диалогов
- Реплика помещается в ~8 секунд естественной речи
- Именуй говорящего: `The woman wearing pink says: ...`
- Фонетика для сложных слов: `"Shreedar"` вместо `"Shridar"`

#### Борьба с субтитрами
1. Диалог через двоеточие, НЕ кавычки
2. `(no subtitles)` в промпте
3. Если не помогает: `No subtitles. No subtitles!`

### 7. Negative Prompts

**Формат:** Описывай отсутствие, не запрещай.
```
✅ negative prompt: cartoon, drawing, low quality, text overlays, subtitles
❌ negative prompt: no cartoon, don't draw, no text
```

Можно также через API-параметр `negativePrompt`.

### 8. Constraints (Technical)
В конце промпта:
```
9:16, 1080p, 8s.
```

---

## Timestamp Prompting

Мульти-шотовая последовательность внутри одного клипа:

```
[00:00-00:02] Medium shot from behind a young explorer pushing aside
jungle vines to reveal a hidden path.

[00:02-00:04] Reverse shot of her freckled face, expression of awe,
ancient ruins in background. SFX: rustling leaves, exotic bird calls.

[00:04-00:06] Tracking shot, she runs her hand over intricate carvings
on a crumbling stone wall. Emotion: wonder and reverence.

[00:06-00:08] Wide crane shot revealing the vast temple complex.
SFX: swelling gentle orchestral score.
```

**Правила:**
- 2-секундные сегменты для максимального контроля
- Каждый сегмент = отдельный shot с камерой
- Аудио-кью к конкретным сегментам
- Описание персонажа повторять во всех сегментах

---

## Image-to-Video: Особые правила

### Prompt for Motion Only
Source image уже задаёт субъект, сцену и стиль. Фокус промпта — на ДВИЖЕНИИ.

**Плохо:** переописывать персонажа/фон/освещение из картинки.
**Хорошо:** описать камеру, анимацию субъекта, изменения среды.

### Три типа движения

1. **Camera Motion** — камера движется, сцена статична:
   `"Slow dolly in on the subject."`

2. **Subject Animation** — персонаж/объект двигается:
   `"Hair and clothes flutter gently in the wind."`

3. **Environmental Animation** — фон оживает:
   `"Fog rolls in slowly across the landscape."`

### Общие термины для персонажей
В image-to-video: `"the subject"`, `"the woman"`, `"he"`, `"she"`, `"they"`.

---

## Тайм-лапс: Особенности промптинга

1. **Зафиксируй камеру:** `"static tripod"`, `"locked-off"`, `"fixed CCTV angle"`
2. **Описывай ПРОЦЕСС**, не начало/конец
3. **Укажи масштаб времени:** `"over the course of a day"`
4. **8 секунд = весь процесс**
5. **Ключевая фраза:** `"Every change should appear as physical build-up, never as dissolve"`

---

## Чеклист перед генерацией

- [ ] Один intent на ось — стиль/движение/свет не противоречат
- [ ] Camera grammar — shot type + motion verb
- [ ] Аудио задано — ambient, SFX, музыка, голос
- [ ] Субъект конкретен — возраст, одежда, выражение
- [ ] Действие описано — глаголы
- [ ] Контекст/сеттинг — где, когда, атмосфера
- [ ] Стиль — cinematic, documentary, anime...
- [ ] Негативный промпт — что исключить
- [ ] Технические параметры — AR, resolution, duration
- [ ] Промпт на английском
- [ ] Длина диалога ≤ 8 секунд
- [ ] Image-to-video: prompt for motion only

---

## Источники

- [Veo prompt guide (Vertex AI)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)
- [Best practices (Vertex AI)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice)
- [Ultimate prompting guide (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- [Gemini API video docs](https://ai.google.dev/gemini-api/docs/video)
- [Veo 3.1 introduction (Developers Blog)](https://developers.googleblog.com/en/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/)
