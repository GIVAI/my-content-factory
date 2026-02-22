# Claude Code Knowledge Base — Архитектура

> Полное описание системы агентов и знаний
> Обновляется по триггеру: `зафиксируй структуру`

---

## Обзор

Это база знаний контент-агентства. Claude Code использует её для:
- Создания контента (YouTube, TikTok, Threads, Telegram)
- Управления проектами экспертов
- Генерации текстов в голосе эксперта
- Аналитики и оптимизации

---

## Архитектура

```
claudecode/
├── CLAUDE.md                    # Главный роутер всей системы
├── structure-readme.md          # ← Этот файл (описание)
├── structure-todo.md            # Задачи по улучшению
│
├── .claude/
│   ├── skills/                  # Универсальные навыки (методологии)
│   │   ├── youtube/
│   │   ├── threads/
│   │   ├── reels/
│   │   ├── nano-banana/
│   │   └── prompt-engineer/
│   └── commands/                # Пусто (НЕ используем для проектов)
│
├── agents/                      # Универсальные агенты (шаблоны)
│   ├── ai-max.md                # AI Max — оператор/ассистент
│   ├── production/              # Производство контента
│   ├── strategy/                # Стратегия
│   ├── analytics/               # Аналитика
│   └── audience/                # Аудитория
│
├── projects/                    # Проекты экспертов
│   ├── _template/               # Шаблон проекта
│   └── {your-project}/          # Твои проекты
│
└── learn/                       # Обучающие материалы
```

---

## Трёхуровневая система

```
SKILL (skills/)           →  "Как делать" (универсальная методология)
         │
         ▼
АГЕНТ (agents/)                   →  "Шаблон/роль" (команды, структуры)
         │
         ▼
ПРОЕКТ (projects/)                →  "Кто и где" (эксперт, Notion, аудитория)
```

**Принцип:** Не дублировать. Каждый уровень наследует от предыдущего.

---

## Skills vs Commands

### Разница

| Тип | Расположение | Активация | Назначение |
|-----|--------------|-----------|------------|
| **Skill** | `skills/` | Автоматически по триггерам | Универсальная методология |
| **Command** | `.claude/commands/` | Явный вызов `/command` | Проектные pipeline |

### Принцип

- **Skills** — универсальные (youtube, threads, reels)
- **Commands** — НЕ создавать для проектов, использовать routing

### Почему не Commands для проектов

```
❌ .claude/commands/{project}-threads.md  → Дублирует routing
❌ .claude/commands/{project}-script.md   → Дублирует routing
✅ Routing через CLAUDE.md проекта        → Единая точка входа
```

---

## Skills (Универсальные навыки)

Расположение: `skills/`

| Skill | Описание | Триггеры |
|-------|----------|----------|
| `youtube/` | YouTube production | "youtube скрипт", "хук для видео" |
| `threads/` | Threads контент | "threads пост", "threads стратегия" |
| `reels/` | Вертикальный контент | "reels", "shorts", "ВИСП" |
| `nano-banana/` | Промпты для изображений | "промпт для картинки" |
| `prompt-engineer/` | Инженер промптов | "создай промпт" |

Skills содержат универсальную методологию (VISP, 10 техник, HeyGen rules).

### Структура skill

```
skills/{skill}/
├── SKILL.md              # Главный файл (name, description, router)
└── {topic}.md            # Подфайлы по темам
```

**SKILL.md frontmatter:**
```yaml
---
name: youtube
description: "YouTube скрипт-райтер. Активируется на: 'youtube скрипт'..."
---
```

---

## Агенты

Расположение: `agents/`

### Production
- `youtube.md` — YouTube Producer
- `threads.md` — Threads Manager
- `vertical-content.md` — Reels/Shorts

### Strategy
- `project-architect.md` — Архитектор проектов
- `strategist.md` — Стратег (skeleton)
- `content-planner.md` — Контент-планер (skeleton)

### Analytics
- `analyst.md` — Аналитик (skeleton)
- `qa-reviewer.md` — QA ревьюер (skeleton)

### Специальные
- `ai-max.md` — AI Max (оператор, НЕ голос контента)

---

## Проекты

Расположение: `projects/`

### Типы проектов

| Тип | Описание | Пример |
|-----|----------|--------|
| **Однонаправленный** | 1 платформа | Threads only |
| **Мультинаправленный** | 2+ платформы | TikTok + YouTube |

### Структура однонаправленного проекта

```
projects/{project}/
├── CLAUDE.md                # Навигация, команды
├── strategy/
│   ├── audience.md          # ЦА
│   ├── profile.md           # Эксперт
│   └── positioning.md       # УТП
├── content/
│   ├── voice-style.md       # Голос
│   └── playbook.md          # Правила
├── templates/
└── agents/                  # Проектные агенты
```

### Структура мультинаправленного проекта

```
projects/{project}/
├── CLAUDE.md                # РОУТЕР (50-100 строк)
│
├── brand/                   # Общее для ВСЕХ направлений
│   ├── profile.md           # Кто эксперт
│   ├── voice-style.md       # Голос и запреты
│   └── audience.md          # ЦА
│
├── {direction}/             # Модуль направления
│   ├── CLAUDE.md            # Workflow, Notion
│   └── scripts/             # Контент
│
└── learning/                # Накопленный опыт
    ├── topic-tracker.md     # Лимиты повторений тем
    ├── approved-patterns.md # Что работает
    └── anti-patterns.md     # Что не работает
```

**Эталон:** `projects/_template/`

---

## Routing (Маршрутизация)

### Главный роутер

Файл `CLAUDE.md` в корне определяет:
- По триггерам → какой проект загружать
- По командам → какой skill активировать

### Проектный роутер (мультинаправленный)

Файл `projects/{project}/CLAUDE.md`:
- По триггерам → какой модуль загружать
- Всегда загружать `brand/`

### Принцип Lazy Loading

```
1. CLAUDE.md (роутер)      — ВСЕГДА (~100 строк)
2. brand/*                 — ВСЕГДА при работе с контентом
3. {direction}/CLAUDE.md   — ТОЛЬКО нужный модуль
```

**Результат:** Экономия ~70% токенов.

---

## Правила наследования

### Что где хранить

| Уровень | Содержит | Примеры |
|---------|----------|---------|
| **Skill** | Универсальная методология | VISP, 10 техник, HeyGen |
| **Агент** | Команды и структуры | `short [тема]`, форматы |
| **Проект** | Интеграции и контекст | Notion, языки, триггеры |
| **brand/** | Персона и голос | profile, voice-style |

### Антипаттерны

| Нельзя | Почему |
|--------|--------|
| Копировать VISP в проект | Рассинхрон при обновлении |
| Дублировать персону | Конфликты версий |
| CLAUDE.md > 200 строк | Перерасход токенов |

---

## Команды

### Структурные

| Команда | Действие |
|---------|----------|
| `зафиксируй структуру` | Обновить structure-todo.md и structure-readme.md |
| `новый проект {код}` | Создать проект по шаблону |
| `проверь проект {код}` | Аудит на соответствие |

### По проектам

Каждый проект определяет свои команды в CLAUDE.md.

---

## Workflow обновления структуры

При триггере `зафиксируй структуру`:

1. Прочитать текущее состояние проектов
2. Обновить `structure-todo.md`:
   - Выполненные задачи
   - Новые задачи
   - Приоритеты
3. Обновить `structure-readme.md`:
   - Изменения в архитектуре
   - Новые проекты/агенты
   - Актуальные примеры

---

## Эталоны

| Что | Где |
|-----|-----|
| Шаблон проекта | `projects/_template/` |
| Audience по шаблону | `agents/audience/audience-template.md` |
| Архитектор проектов | `agents/strategy/project-architect.md` |

---

## История изменений

### v1.2
- Модульная архитектура для мультинаправленных проектов
- Learning Loop — автоматическое обучение
- Topic Tracker для управления темами
- Система примеров в projects/{project}/learning/examples/

---

## Поддержка

Сайт: [galson.pro](https://galson.pro) | Поддержка: [@galsonproAIbot](https://t.me/galsonproAIbot?start=support) | Канал: [@galsonproai](https://t.me/galsonproai)

---

*Фабрика Контента v2.0*  
*Макс Галсон • [galson.pro](https://galson.pro)*
