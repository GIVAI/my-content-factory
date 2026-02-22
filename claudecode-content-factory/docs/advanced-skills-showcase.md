# Advanced Skills Showcase

> Как agent-architect и skill-creator заменяют целые команды

---

## Agent Architect — Создание Production-Ready Агентов

### Что это

Genius creator агентов из простых запросов. Превращает "создай агента для X" в полноценного специалиста за 5 минут.

**Файл:** `skills/agent-architect/SKILL.md`

### Триггеры

```
создай агента для X
агент для X
новый агент
команда для X
automate X
AI team для X
```

### Возможности

- **3 паттерна агентов:**
  - **Worker** — выполняет конкретную задачу (Threads Writer, Email Creator)
  - **Orchestrator** — управляет командой агентов (Content Pipeline)
  - **Diagnostic** — анализирует и находит проблемы (Code Reviewer)

- **Два режима работы:**
  - **Quick Mode** — 3 вопроса, 5 минут
  - **Deep Mode** — Team Interview, полное интервью

- **20+ team roles library** — готовые роли (Strategist, Writer, Critic, Publisher)
- **Quality checklist** — production-ready критерии
- **Auto-detection complexity** — сам определяет сложность задачи

---

## Примеры использования Agent Architect

### Пример 1: Threads Writer за 5 минут

**Запрос:**
```
создай агента для написания threads постов
```

**Что делает Agent Architect:**

1. **Анализирует intent:**
   - Domain: content creation
   - Function: write threads posts
   - Complexity: medium

2. **Задаёт 3 вопроса (Quick Mode):**
   ```
   Кто твоя аудитория?
   Какой tone of voice (формальный/неформальный)?
   Какие темы чаще всего?
   ```

3. **Генерирует полного агента с:**
   - Workflow (voice → skill → generation → critics)
   - Auto-loading rules (threads skill + selling-meanings если продающий)
   - Integration points (brand/voice-style.md, learning/)
   - Quality checklist

**Результат:** Production-ready агент `agents/production/threads-writer.md`

**Файл содержит:**
```markdown
# Threads Writer

## Workflow
1. Load voice-style.md (твой tone)
2. Load threads skill (VISP, hooks, structure)
3. Generate posts
4. Run critics (if enabled)

## Auto-loading
- threads skill (always)
- selling-meanings (if "продающий" detected)
- storytelling (if "история" detected)

## Integration
- Reads: brand/voice-style.md
- Learns from: learning/threads/patterns.md
- Saves to: content/threads/

## Triggers
"threads post", "threads 5", "пост для threads"
```

**Время создания:** 5 минут

---

### Пример 2: Content Pipeline Orchestrator

**Запрос:**
```
создай команду для создания контента от идеи до публикации
```

**Что делает Agent Architect:**

1. **Определяет complexity:** complex (multi-step workflow)
2. **Переключается в Deep Mode** (Team Interview)
3. **Раскладывает на роли:**
   - **Strategist** — выбирает тему, определяет цель
   - **Writer** — пишет черновик
   - **Critic** — проверяет качество (3 критика: Sales, Creative, Structure)
   - **Publisher** — форматирует и готовит к публикации

4. **Генерирует orchestrator с:**
   - Handoff механизмами (как передавать работу между ролями)
   - State management (tracking прогресса)
   - Error recovery (что если Writer застрял)
   - Quality gates (не пускать дальше если Critic rejected)

**Результат:** Orchestrator агент `agents/pipelines/content-pipeline.md`

**Workflow:**
```
Idea → Strategist → Writer → Critic → (if approved) → Publisher → Done
                        ↑           ↓
                        └── (if rejected) ──┘
```

**Заменяет:** Команду из 4 человек

**Время создания:** 15 минут (Deep Mode)

---

### Пример 3: Email Campaign Agent

**Запрос:**
```
агент для email рассылок
```

**Что делает Agent Architect:**

1. **Quick Mode** (3 вопроса):
   - Тип рассылок (продающие/обучающие/новости)?
   - Частота (ежедневно/еженедельно)?
   - Стиль (формальный/casual)?

2. **Генерирует Email Agent с:**
   - Subject line formulas (8 проверенных формул)
   - Email structure (hook → value → CTA)
   - A/B testing support (генерирует варианты)
   - Segmentation logic (разные письма для разных сегментов)

**Результат:** Email agent готовый к использованию

---

## Skill Creator — Создание Модульных Skills

### Что это

Фреймворк для создания эффективных, переиспользуемых skills. Превращает domain expertise в модули.

**Файл:** `skills/skill-creator/SKILL.md`

### Когда использовать

- Нужно стандартизировать процесс
- Команда повторяет одни и те же действия
- Хочешь сохранить domain expertise
- Создаёшь skill ecosystem для команды

### Принципы

1. **Concise is key** — контекст это public good (экономь токены)
2. **Lazy loading** — загружай только нужное (references on demand)
3. **No duplication** — reference вместо копирования
4. **Appropriate freedom** — от жёстких скриптов до гибких workflows

---

## Примеры использования Skill Creator

### Пример 1: Threads Skill

**Цель:** Методология создания вирусных Threads постов

**Структура:**
```
skills/threads/
├── SKILL.md                    # Core workflow + hooks (200 строк)
├── references/
│   ├── visp-structure.md      # ВИСП framework
│   ├── psychological-triggers.md
│   ├── tone-formulas.md
│   └── hooks-library.md       # 30+ готовых хуков
└── assets/
    └── post-template.md       # Шаблон для вывода
```

**Что включает:**

**SKILL.md (core):**
```markdown
# Threads Skill

## Workflow
1. Определить цель поста (обучить/продать/вовлечь)
2. Выбрать hook из библиотеки
3. Построить по VISP
4. Добавить psychological triggers
5. Закрыть CTA

## When to load references
- visp-structure.md → если нужна детальная структура
- hooks-library.md → если нужны варианты хуков
- tone-formulas.md → если нужна помощь с tone

## Output
Use assets/post-template.md для форматирования
```

**Token efficiency:** ~70% экономии vs monolithic prompt

**Lazy loading:**
- Core SKILL.md загружается всегда (~200 строк)
- References загружаются по требованию (~500 строк каждый)
- Если нужен только базовый пост → экономия 1500 строк!

---

### Пример 2: Nano Banana Skill

**Цель:** Генерация промптов для AI-изображений (Midjourney, DALL-E)

**Структура:**
```
skills/nano-banana/
├── SKILL.md                      # Core prompt generator
├── references/
│   ├── realism-guide.md         # Фотореализм
│   ├── character-prompts.md     # Персонажи
│   ├── composition-rules.md     # Композиция
│   └── lighting-vocabulary.md   # Освещение
├── assets/
│   └── identity-kit-template.md # Постоянное лицо
└── scripts/
    └── batch-generate.py        # Batch операции
```

**Особенность:** Scripts для deterministic операций

**Когда использовать scripts:**
- Batch генерация (100+ промптов)
- Deterministic output (точные параметры)
- Token efficiency (скрипт вместо промпта = 90% экономии)

**Example usage:**
```bash
python scripts/batch-generate.py \
  --theme "winter landscape" \
  --variations 10 \
  --style photorealistic
```

**Результат:** 10 вариантов промптов за 2 секунды

---

### Пример 3: Selling Meanings Skill

**Цель:** Формулы продающих смыслов

**Структура:**
```
skills/selling-meanings/
├── SKILL.md                # Core framework
├── references/
│   ├── psychology.md      # Психология покупки
│   ├── formulas.md        # AIDA, PAS, BAB, 4U
│   ├── hormozi-offers.md  # Grand Slam Offer
│   └── templates.md       # 30+ шаблонов
```

**Что умеет:**
- Извлекать selling meanings из продукта
- Усиливать через триггеры
- Генерировать оффер-стеки (а-ля Hormozi)
- Создавать прогревающие последовательности

**Use case:**
```
User: "усиль продающий смысл: экономия времени"

Skill:
1. Загружает psychology.md (триггеры)
2. Применяет amplification techniques
3. Output:
   "Не просто экономия времени.
   3 часа в день = 15 часов в неделю = 60 часов в месяц.
   Это полторы рабочих недели. Каждый месяц."
```

---

## Когда использовать что

| Задача | Инструмент | Почему |
|--------|------------|--------|
| Создать агента для конкретной задачи | **Agent Architect** | Быстро (5 мин), production-ready |
| Стандартизировать процесс | **Skill Creator** | Переиспользуемый модуль |
| Команда агентов (orchestration) | **Agent Architect** (Deep Mode) | Handoff механизмы |
| Сохранить domain expertise | **Skill Creator** | Модульная база знаний |
| Автоматизировать рутину | **Agent Architect** → Worker pattern | Специализированный исполнитель |
| Создать ecosystem модулей | **Skill Creator** | Lazy loading, no duplication |

---

## Сравнение

| Критерий | Agent Architect | Skill Creator |
|----------|-----------------|---------------|
| **Что создаёт** | Агента (who) | Skill (how) |
| **Время создания** | 5-15 минут | 30-60 минут |
| **Сложность** | Средняя | Высокая |
| **Переиспользование** | Низкое (специфичный агент) | Высокое (универсальный skill) |
| **Best for** | Быстрая автоматизация | Долгосрочная база знаний |

---

## Комбинации (Advanced)

### Combo 1: Agent + Skill

**Сценарий:** Создать агента для LinkedIn постов

**Workflow:**
1. **Сначала:** Создать LinkedIn Skill (методология, формулы)
   ```
   skill-creator → linkedin skill
   ```
2. **Затем:** Создать LinkedIn Agent (использует skill)
   ```
   agent-architect → linkedin writer
   (auto-loads linkedin skill)
   ```

**Результат:**
- LinkedIn Skill — переиспользуемая методология
- LinkedIn Writer Agent — использует skill + добавляет voice

### Combo 2: Orchestrator + Multiple Skills

**Сценарий:** Полный content pipeline

**Workflow:**
1. Создать skills для каждого формата (threads, youtube, email)
2. Создать Orchestrator agent:
   ```
   agent-architect → content orchestrator
   (uses: threads skill + youtube skill + email skill)
   ```

**Результат:** Единая точка входа для всех форматов

---

## Ресурсы

### Agent Architect

**Файлы:**
- **Skill:** `skills/agent-architect/SKILL.md`
- **References:**
  - `agent-patterns.md` — 3 паттерна (Worker, Orchestrator, Diagnostic)
  - `team-roles-library.md` — 20+ ролей для команд
  - `interview-questions.md` — вопросы для discovery
  - `quality-checklist.md` — production-ready критерии
- **Assets:**
  - `agent-template.md` — базовый шаблон агента

**Команды:**
```
создай агента для X          → Quick Mode (3 вопроса)
создай команду для X         → Deep Mode (Team Interview)
агент для X                  → Quick Mode
automate X                   → Quick Mode
```

### Skill Creator

**Файлы:**
- **Skill:** `skills/skill-creator/SKILL.md`
- **References:**
  - `workflows.md` — процессы создания skill
  - `output-patterns.md` — структуры skills
- **Scripts:**
  - `init_skill.py` — scaffold новый skill
  - `package_skill.py` — упаковка для раздачи
  - `quick_validate.py` — валидация структуры

**Команды:**
```
create skill for X           → полный workflow
new skill                    → интерактивный wizard
skill template               → показать шаблон
```

---

## Learning Path

### Начинающий уровень

1. **Попробуй Agent Architect:**
   ```
   создай агента для threads постов
   ```
   Результат: Готовый агент за 5 минут

2. **Используй созданного агента:**
   ```
   threads post про AI
   ```
   Агент загрузит threads skill автоматически

### Средний уровень

3. **Создай свой skill:**
   ```
   create skill for Instagram captions
   ```
   Skill Creator проведёт через процесс

4. **Интегрируй skill с агентом:**
   Созданный skill теперь доступен всем агентам

### Продвинутый уровень

5. **Создай orchestrator:**
   ```
   создай команду для контента от идеи до публикации
   ```
   Deep Mode → multi-agent система

6. **Построй skill ecosystem:**
   - Несколько skills (threads, youtube, email)
   - Orchestrator agent использует все
   - Learning loop обогащает skills

---

## Metrics

### Agent Architect

- **Время создания агента:** 5-15 минут (vs 2-3 часа вручную)
- **Quality:** Production-ready с первого раза
- **Token efficiency:** Lazy loading = 70% экономии
- **Maintenance:** Minimal (skills обновляются отдельно)

### Skill Creator

- **Время создания skill:** 30-60 минут (vs 4-6 часов вручную)
- **Reusability:** Используется множеством агентов
- **Token efficiency:** References on demand = 80% экономии
- **Scalability:** Ecosystem растёт модульно

---

## FAQ

**Q: Когда использовать Agent Architect вместо написания промпта вручную?**
A: Когда задача повторяющаяся или требует production-ready качества. Agent Architect добавляет workflow, integration, quality checks.

**Q: Skill Creator это то же что prompt engineering?**
A: Нет. Prompt engineering создаёт prompt. Skill Creator создаёт модульную систему (core + references + assets + scripts) с lazy loading.

**Q: Можно ли использовать agent-architect без skill-creator?**
A: Да. Agent Architect использует существующие skills. Skill Creator нужен только если хочешь создать НОВЫЙ skill.

**Q: Сколько агентов можно создать?**
A: Сколько угодно. Agent Architect генерирует markdown файл. Создавай агентов под каждую задачу.

**Q: Как обновлять созданных агентов?**
A: Редактируй markdown файл вручную ИЛИ пересоздай через agent-architect с новыми требованиями.

---

## Примеры из реальной практики

### Case 1: Content Factory Constructor

**Проблема:** Нужна система для создания контента (threads, youtube, carousel)

**Решение:**
1. Создали skills: threads, youtube, carousel, selling-meanings, storytelling
2. Создали агентов через agent-architect: Threads Writer, YouTube Producer, Vertical Content
3. Добавили Orchestrator: Content Pipeline (управляет всеми)

**Результат:**
- 11 skills
- 14 agents
- Полная фабрика контента
- 70% token efficiency через lazy loading

### Case 2: Customer Support Automation

**Проблема:** Автоматизировать поддержку клиентов

**Решение:**
1. Skill Creator → customer-support skill (FAQ, escalation rules, tone guidelines)
2. Agent Architect → Support Agent (uses customer-support skill)
3. Agent Architect → Escalation Manager (orchestrates difficult cases)

**Результат:**
- 80% запросов автоматизированы
- Escalation только для сложных случаев

---

## Next Steps

**Хочешь попробовать?**

```
создай агента для [твоя задача]
```

Agent Architect спросит детали и сгенерирует production-ready агента.

**Хочешь глубже?**

Изучи:
- [Agent Patterns](skills/agent-architect/references/agent-patterns.md) — 3 паттерна агентов
- [Team Roles Library](skills/agent-architect/references/team-roles-library.md) — 20+ ролей
- [Skill Creation Workflows](skills/skill-creator/references/workflows.md) — как создавать skills

---

*Фабрика Контента v2.0*
*Макс Галсон • [galson.pro](https://galson.pro)*
