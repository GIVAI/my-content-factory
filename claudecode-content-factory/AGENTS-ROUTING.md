# Agents Routing

> Компактная таблица agents → paths для Claude

---

## Agents Table

| Agent | Trigger Keywords | File Path |
|-------|------------------|-----------|
| **AI Operator** | (автоматически) | `agents/ai-operator.md` |
| **Threads Writer** | "threads", "пост" | `agents/production/threads.md` |
| **YouTube Producer** | "youtube", "сценарий" | `agents/production/youtube.md` |
| **Vertical Content** | "reels", "shorts", "tiktok" | `agents/production/vertical-content.md` |
| **Thumbnail Generator** | "thumbnail", "обложка" | `agents/production/thumbnail-generator.md` |
| **Content Pipeline** | "content pipeline" | `agents/production/content-pipeline.md` |
| **Analyst** | "инсайты", "что сработало" | `agents/analytics/analyst.md` |
| **Learning Agent** | "это сработало", "глобальное обучение" | `agents/analytics/learning-agent.md` |
| **Critics** | "review", "critique" | `agents/analytics/critics/` |
| **Selling Meanings** | "продающие смыслы", "почему купят" | `agents/strategy/selling-meanings.md` |
| **Project Architect** | "создать проект", "новый проект" | `agents/strategy/project-architect.md` |
| **Transcription Processor** | "транскрипт", "transcription" | `agents/production/transcription-processor.md` |
| **Memory System** | "настрой память", "memory setup", "проверь память", "memory check" | `skills/memory-system/SKILL.md` |

---

## Agent Categories

### Production (создание контента)
- `agents/production/threads.md` — Threads посты
- `agents/production/youtube.md` — YouTube сценарии
- `agents/production/vertical-content.md` — Reels/Shorts/TikTok
- `agents/production/thumbnail-generator.md` — обложки
- `agents/production/content-pipeline.md` — универсальный пайплайн
- `agents/production/transcription-processor.md` — обработка транскрибаций видео

### Analytics (аналитика)
- `agents/analytics/analyst.md` — метрики, инсайты
- `agents/analytics/learning-agent.md` — обучение, паттерны (Level 2: глобальное)
- `agents/analytics/critics/` — критики (Sales, Creative, Structure)

### Strategy (стратегия)
- `agents/strategy/project-architect.md` — создание проектов
- `agents/strategy/selling-meanings.md` — продающие смыслы

---

## Agent + Skill Relationships

| Agent | Uses Skills |
|-------|-------------|
| Threads Writer | threads, selling-meanings (auto), storytelling (auto) |
| YouTube Producer | youtube, storytelling (auto), selling-meanings (auto) |
| Vertical Content | reels, storytelling |
| Thumbnail Generator | nano-banana |
| Selling Meanings | selling-meanings |

---

## Usage

**When user triggers agent:**
1. Match trigger → find agent
2. Load agent file
3. Agent loads required skills
4. Execute task

**Example:**
```
User: "threads 10"
    ↓
Agent: Threads Writer
    ↓
Skills loaded:
- threads
- selling-meanings (if "продающий" detected)
    ↓
Result: 10 posts
```

---

*Agents Routing v2.0 — Content Factory*
