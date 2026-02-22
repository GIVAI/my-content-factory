# Interview Questions for Agent Discovery

Two modes: Quick (simple agents) and Deep (team-level agents).

---

## Mode Selection

```
IF request contains:
  - "team", "команда", "полный цикл", "end-to-end"
  - Multiple distinct functions
  - Complex workflow description
  → Use DEEP MODE

ELSE:
  → Use QUICK MODE
```

---

## Quick Mode (3 Questions)

For simple, focused agents. Get enough to generate a working agent.

### Question 1: Goal

**Ask:**
```
Что этот агент должен делать? Какая главная задача?
```

**Extract:**
- Primary function
- Domain (content, tech, business, etc.)
- Success criteria

**Examples of good answers:**
- "Проверять посты перед публикацией на ошибки"
- "Анализировать конкурентов в YouTube"
- "Генерировать идеи для контента на неделю"

### Question 2: Input/Output

**Ask:**
```
Что агент получает на вход? Что должен выдавать?
```

**Extract:**
- Input format (text, files, data)
- Output format (report, list, document)
- Transformation type

**Examples of good answers:**
- "Получает черновик поста → выдаёт список правок"
- "Получает название канала → выдаёт отчёт о стратегии"
- "Получает тему → выдаёт 10 идей с хуками"

### Question 3: Decisions

**Ask:**
```
Какие решения агент должен принимать сам? Когда спрашивать?
```

**Extract:**
- Autonomous decisions
- Escalation triggers
- Approval requirements

**Examples of good answers:**
- "Мелкие правки сам, крупные — спрашивать"
- "Категоризировать сам, публиковать — спрашивать"
- "Всё сам, только итог показывать"

---

## Deep Mode: Team Interview (6-8 Questions)

For complex agents replacing entire teams. Thorough discovery.

### Question 1: Problem

**Ask:**
```
Какую проблему решает эта команда? Что было бы, если её не было?
```

**Extract:**
- Core value proposition
- Business impact
- Why automation matters

**Good answer signals:**
- Clear pain point
- Quantifiable impact
- Existing manual process

### Question 2: Workflow

**Ask:**
```
Опиши процесс от начала до конца. Что происходит на каждом этапе?
```

**Extract:**
- Pipeline stages
- Sequential vs parallel steps
- Handoff points

**Probe further:**
- "Что происходит дальше?"
- "Кто передаёт кому?"
- "Где могут быть задержки?"

### Question 3: Roles

**Ask:**
```
Кто что делает в человеческой команде? Какие роли?
```

**Extract:**
- Distinct roles
- Responsibilities per role
- Skill requirements

**Map to library:**
- Compare with team-roles-library.md
- Identify matches
- Note custom roles

### Question 4: Decisions

**Ask:**
```
Какие решения принимаются? Кто их принимает? На основании чего?
```

**Extract:**
- Decision points in workflow
- Decision authority (who decides)
- Decision criteria

**Key patterns:**
- Binary (yes/no)
- Categorical (A/B/C)
- Scoring (threshold-based)

### Question 5: Quality

**Ask:**
```
Как понять, что работа сделана хорошо? Какие критерии качества?
```

**Extract:**
- Success metrics
- Quality gates
- Review criteria

**Probe:**
- "Что значит 'хорошо'?"
- "Как проверить результат?"
- "Кто даёт финальное ОК?"

### Question 6: Edge Cases

**Ask:**
```
Что может пойти не так? Как команда справляется с проблемами?
```

**Extract:**
- Common failures
- Recovery procedures
- Escalation paths

**Probe:**
- "А если данных нет?"
- "А если непонятно что делать?"
- "А если клиент недоволен?"

### Question 7: Integration (optional)

**Ask:**
```
С чем эта команда взаимодействует? Какие инструменты, системы, люди?
```

**Extract:**
- External systems
- API requirements
- Human touchpoints

**Needed when:**
- Agent must read/write files
- Agent coordinates with other agents
- Agent uses external tools

### Question 8: Boundaries (optional)

**Ask:**
```
Что эта команда точно НЕ делает? Что вне её зоны ответственности?
```

**Extract:**
- Explicit exclusions
- Adjacent responsibilities
- Handoff to others

**Important for:**
- Preventing scope creep
- Defining agent boundaries
- Setting user expectations

---

## Question Flow Strategy

### Quick Mode Flow

```
Q1 (Goal) → Q2 (I/O) → Q3 (Decisions) → Generate
        ↓
   If complex → Switch to Deep Mode
```

### Deep Mode Flow

```
Q1 (Problem) → Q2 (Workflow) → Q3 (Roles)
       ↓
Q4 (Decisions) → Q5 (Quality) → Q6 (Edge Cases)
       ↓
[If needed] Q7 (Integration) → Q8 (Boundaries)
       ↓
   Generate comprehensive agent
```

---

## Adaptive Questioning

### Skip Question If

| Question | Skip when |
|----------|-----------|
| Q7 Integration | Standalone agent, no external dependencies |
| Q8 Boundaries | Scope already clear from other answers |

### Add Follow-up If

| Signal | Follow-up |
|--------|-----------|
| Vague answer | "Можешь привести пример?" |
| Multiple interpretations | "Это X или Y?" |
| Missing detail | "Что именно происходит тут?" |
| Complex subprocess | "Разбери этот шаг подробнее" |

### Batch Questions

When user prefers efficiency:
```
Отвечу на несколько вопросов сразу, чтобы понять задачу:

1. Что агент должен делать?
2. Что получает → что выдаёт?
3. Какие решения принимает сам?
```

---

## Answer Processing

### From Answers Extract

| Answer Component | Maps to Agent Section |
|-----------------|----------------------|
| Goal description | Role, Responsibilities |
| Input/Output | Workflow, Output Formats |
| Decision points | Decision Framework, Edge Cases |
| Workflow stages | Workflow steps |
| Roles mentioned | Responsibilities distribution |
| Quality criteria | Quality Standards |
| Problems/failures | Edge Cases |
| Boundaries | Boundaries section |

### Pattern Recognition

| User says | Implies |
|-----------|---------|
| "проверять", "валидировать" | Diagnostic pattern |
| "генерировать", "создавать" | Worker pattern |
| "координировать", "управлять" | Orchestrator pattern |
| "передавать дальше", "pipeline" | Handoff pattern |
| "полный цикл", "от А до Я" | Comprehensive orchestrator |

---

## Example Interviews

### Quick Mode Example

**User:** "Создай агента для проверки постов"

**Q1:** Что агент должен делать?
**A:** Проверять посты перед публикацией на ошибки и стиль

**Q2:** Что получает → что выдаёт?
**A:** Получает текст поста, выдаёт список правок

**Q3:** Какие решения принимает сам?
**A:** Мелкие правки сам, крупные изменения — спрашивать

**→ Generate:** QA Reviewer agent, ~1200 words

---

### Deep Mode Example

**User:** "Нужна команда для YouTube продакшена"

**Q1:** Какую проблему решает?
**A:** Долго делаем видео, хочу автоматизировать

**Q2:** Опиши процесс
**A:** Идея → Ресёрч → Сценарий → Съёмка → Монтаж → Публикация

**Q3:** Кто что делает?
**A:** Ресёрчер, сценарист, редактор, SMM

**Q4:** Какие решения?
**A:** Тему выбираю я, остальное — команда

**Q5:** Как понять что хорошо?
**A:** Retention >50%, структура по формуле

**Q6:** Что может пойти не так?
**A:** Тема не заходит, слабый hook, длинно

**→ Generate:** YouTube Production Pipeline agent, ~3500 words
