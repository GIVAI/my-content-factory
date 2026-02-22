# Skills Routing

> Компактная таблица skills → paths для Claude

---

## Skills Table

| Skill | Trigger Keywords | Files to Load |
|-------|------------------|---------------|
| **threads** | "threads", "threads post", "пост" | `skills/threads/` |
| **youtube** | "youtube", "youtube script", "сценарий" | `skills/youtube/` |
| **reels** | "reels", "shorts", "tiktok" | `skills/reels/` |
| **carousel** | "carousel", "карусель" | `skills/carousel/` + `skills/nano-banana/` |
| **telegram** | "telegram", "тг пост", "tg post" | `skills/telegram/` |
| **selling-meanings** | Auto: "продающий", "CTA", "продающие смыслы" | `skills/selling-meanings/` |
| **storytelling** | Auto: "история", "story", "кейс" | `skills/storytelling/` |
| **launch** | "launch", "запуск", "PLF", "прогрев" | `skills/launch/` |
| **nano-banana** | "image prompt", "картинка", "обложка" | `skills/nano-banana/` |
| **prompt-engineer** | "create prompt", "improve prompt" | `skills/prompt-engineer/` |
| **skill-creator** | "create skill", "new skill" | `skills/skill-creator/` |
| **agent-architect** | "создай агента", "new agent" | `skills/agent-architect/` |
| **offer-core** | "оффер", "offer", "ядро оффера", "tripwire" | `skills/offer-core/` |
| **customer-research** | "кастдев", "custdev", "распаковка", "исследование ЦА" | `skills/customer-research/` |
| **learning-processor** | "обработай", "обучи" | `skills/learning-processor/` |

---

## Auto-Loading Rules

### selling-meanings (Auto-loads for selling content)

**Keywords:**
- "продающий", "selling", "оффер", "offer"
- "CTA", "закреп", "pinned"
- "конверсия", "продажи"

### storytelling (Auto-loads for story content)

**Keywords:**
- "история", "story", "кейс", "case"
- "сторителлинг", "storytelling"

---

## Skill Combinations

| Content Type | Skills |
|--------------|--------|
| Продающая карусель | carousel + selling-meanings + nano-banana |
| Threads запуск | threads + launch + selling-meanings |
| YouTube история | youtube + storytelling |
| Selling Threads | threads + selling-meanings |
| Создание оффера | offer-core + customer-research |
| Запуск продукта | launch + offer-core + selling-meanings |

---

## Usage

**When user triggers format:**
1. Match trigger → find skill
2. Load files from skill folder
3. Check auto-loading (selling-meanings, storytelling)
4. Load project context (brand/, learning/)

**Example:**
```
User: "продающий пост"
    ↓
Skills:
1. threads (format)
2. selling-meanings (auto: "продающий")
    ↓
Files:
- skills/threads/
- skills/selling-meanings/
```

---

*Skills Routing v2.0 — Content Factory*
