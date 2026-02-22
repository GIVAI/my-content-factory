---
name: timelapse-creator
description: "Generate AI timelapse videos from idea to final clips. Full pipeline: keyframe generation → frame approval → video generation → delivery."
triggers:
  - таймлапс
  - timelapse
  - переход между кадрами
  - трансформация
  - видео-переход
---

# Timelapse Creator

Generate timelapse-style videos through a structured pipeline: idea → keyframes → approval → video clips → delivery.

## Pipeline Overview

```
IDEA → KEYFRAMES (Nano Banana) → APPROVAL → VIDEO (Veo 3.1-fl) → DELIVER mp4
```

---

## Phase 1: Ideation

When user says "давай таймлапс" or similar — brainstorm the concept:
- What transforms? (object, room, vehicle, food, etc.)
- From what state to what state? (broken→fixed, empty→decorated, raw→cooked)
- How many intermediate steps? (usually 4-5 total keyframes)
- Setting/environment? (workshop, kitchen, studio, outdoor)

Propose 4-5 keyframe descriptions, get approval before generating.

---

## Phase 2: Keyframes (Nano Banana Pro)

### Rules
1. **ANCHOR PROMPT** — write once, reuse for ALL frames. Describes: camera angle, location, lighting. Must be identical.
2. **VARIABLE PART** — unique per frame. Describes the current state of transformation.
3. **Format:** 9:16 vertical, 2K (or 4K if requested)
4. **Prompts ALWAYS in English**
5. **Convert PNG→JPEG** before sending (4K PNG > 8MB → 413 error)
6. **Save all frames** to `content/timelapse/{project-name}/`

### Template
```
[ANCHOR — identical for all frames]
Interior of a workshop, [object] centered in frame, shot from 
[angle] at [distance]. [Lighting description]. Same setup throughout.

[VARIABLE — unique per frame]  
Frame 1: The [object] shows [damaged state description]...
Frame 2: The [object] has been [intermediate state]...
Frame 3: The [object] is being [process description]...
Frame 4: The [object] is [final state description]...
```

---

## Phase 3: Approval

Send all keyframes to user. Check:
- Consistency (same scene, same angle?)
- Logical progression (does transformation make sense?)
- Quality (any artifacts, weird details?)

If approved → Phase 4. If not → regenerate specific frames.

---

## Phase 4: Video (Veo 3.1-fl)

### Rules
1. First image = START frame, second = END frame
2. Use **base64** encoding (no need for public URL hosting)
3. Generate pairs: frame1→frame2, frame2→frame3, frame3→frame4
4. Prompt describes the PROCESS of transformation
5. Model: `veo-3.1-fast-fl` for tests, `veo-3.1-fl` for final

### Video Prompt Template
```
Smooth realistic timelapse of [process description]. Fixed camera angle, 
no camera movement. Continuous physical transformation, realistic lighting 
changes. No dissolves, no crossfades — only physical build-up and assembly.
```

### Request Format (Sync API)
```json
{
  "messages": [{"role": "user", "content": [
    {"type": "text", "text": "Smooth timelapse transition..."},
    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,{START}"}},
    {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,{END}"}}
  ]}],
  "model": "veo-3.1-fast-fl",
  "stream": true
}
```

---

## Phase 5: Delivery

1. Save all mp4 clips to `content/videos/{project-name}/`
2. Send to client
3. Client assembles in CapCut (speeds up 8s→2-3s per segment)

---

## Cost Summary

| Item | Qty | Price | Total |
|------|-----|-------|-------|
| Keyframes | 4-5 | ~$0.05 | $0.20-0.25 |
| Video clips | 3-4 | ~$0.15 | $0.45-0.60 |
| **TOTAL** | | | **~$0.70-0.85** |

---

## Transition Prompt Templates

### Time of Day
```
Smooth transition from day to night, realistic lighting changes,
maintaining the same camera angle and composition
```

### Construction/Growth
```
Timelapse showing gradual construction progress,
realistic materials appearing, smooth continuous motion
```

### Nature Changes
```
Natural progression showing seasonal change,
realistic weather transition, maintaining landscape composition
```

### Space Transformation
```
Smooth transformation of the space,
realistic material changes, maintaining perspective and scale
```

---

## Troubleshooting

| Проблема | Действие |
|----------|----------|
| **Перепутал API ключи** | Nano = кадры, Veo = видео. Разные ключи! |
| **Видео не соответствует кадрам** | Проверить суффикс `-fl` в модели |
| **Переход неестественный** | Переделать кадры — больше сходства |
| **Качество низкое** | Переключиться с `fast-fl` на `fl` |
| **API ошибка** | Проверить размер кадров < 8MB |

---

## Video Output Specs

| Параметр | Значение |
|----------|----------|
| Длительность | 5-10 секунд |
| Качество | HD/4K |
| Формат | MP4 |
| FPS | 24-30 |
| Кадры вход | JPG < 8MB, идентичный aspect ratio |

---

## Output Structure

```
content/timelapse/{project-name}/
├── frames/
│   ├── frame-1.jpg
│   ├── frame-2.jpg
│   ├── frame-3.jpg
│   └── frame-4.jpg
├── videos/
│   ├── segment-1-2.mp4
│   ├── segment-2-3.mp4
│   └── segment-3-4.mp4
├── prompts.md
└── notes.md
```

---

*Timelapse Creator v1.0 — Content Factory*
