# Team Analysis Framework

Extract what a human team does from a simple request.

---

## Mode Selection

```
IF request contains:
  - "team", "команда", "полный цикл", "end-to-end"
  - "replace", "заменить", "автоматизировать команду"
  - Multiple distinct functions
  - Complex workflow description
  → Use DEEP MODE (6-8 questions)

ELSE:
  → Use QUICK MODE (3 questions)
```

---

## Quick Mode (3 Questions)

For focused skills. Get enough to generate a working skill.

### Q1: Goal

**Ask:**
```
Что этот skill должен делать? Какая главная задача?
```

**Extract:**
- Primary function
- Domain (content, tech, business, creative)
- Success criteria

**Good answers:**
- "Проверять посты перед публикацией на ошибки"
- "Генерировать идеи для контента на неделю"
- "Анализировать конкурентов в YouTube"

### Q2: Input/Output

**Ask:**
```
Что skill получает на вход? Что должен выдавать?
```

**Extract:**
- Input format (text, files, data)
- Output format (report, list, document, content)
- Transformation type

**Good answers:**
- "Получает черновик поста → выдаёт список правок"
- "Получает тему → выдаёт 10 идей с хуками"
- "Получает название канала → выдаёт отчёт о стратегии"

### Q3: Decisions

**Ask:**
```
Какие решения skill должен принимать сам? Когда спрашивать?
```

**Extract:**
- Autonomous decisions
- Escalation triggers
- Approval requirements

**Good answers:**
- "Мелкие правки сам, крупные — спрашивать"
- "Всё сам, только итог показывать"
- "Категоризировать сам, публиковать — спрашивать"

---

## Deep Mode (6-8 Questions)

For complex skills replacing entire teams.

### Q1: Problem

**Ask:**
```
Какую проблему решает эта команда? Что было бы, если её не было?
```

**Extract:**
- Core value proposition
- Business impact
- Why automation matters

**Probe:** "Сколько времени/денег это стоит сейчас?"

### Q2: Workflow

**Ask:**
```
Опиши процесс от начала до конца. Что происходит на каждом этапе?
```

**Extract:**
- Pipeline stages
- Sequential vs parallel steps
- Handoff points

**Probe:**
- "Что происходит дальше?"
- "Кто передаёт кому?"
- "Где могут быть задержки?"

### Q3: Roles

**Ask:**
```
Кто что делает в человеческой команде? Какие роли?
```

**Extract:**
- Distinct roles
- Responsibilities per role
- Skill requirements

**Map to patterns:**
| User says | Implies roles |
|-----------|---------------|
| "content team" | Writer + Editor + Researcher (minimum) |
| "YouTube production" | Scriptwriter + Editor + Thumbnail + SEO |
| "quality review" | QA Reviewer + criteria + checklists |
| "automate X" | Need to identify manual steps first |

### Q4: Decisions

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

### Q5: Quality

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

### Q6: Edge Cases

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
- "А если результат не нравится?"

### Q7: Integration (optional)

**Ask:**
```
С чем эта команда взаимодействует? Какие инструменты, системы?
```

**Extract:**
- External systems (APIs, databases)
- File formats
- Human touchpoints

**Skip when:** Standalone skill, no external dependencies

### Q8: Boundaries (optional)

**Ask:**
```
Что эта команда точно НЕ делает? Что вне зоны ответственности?
```

**Extract:**
- Explicit exclusions
- Handoff to other teams
- Scope limits

**Skip when:** Scope already clear from other answers

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
   Generate comprehensive skill
```

---

## Adaptive Questioning

### Batch Questions (for efficiency)

```
Отвечу на несколько вопросов сразу, чтобы понять задачу:

1. Что skill должен делать?
2. Что получает → что выдаёт?
3. Какие решения принимает сам?
```

### Follow-up Triggers

| Signal | Follow-up |
|--------|-----------|
| Vague answer | "Можешь привести пример?" |
| Multiple interpretations | "Это X или Y?" |
| Missing detail | "Что именно происходит тут?" |
| Complex subprocess | "Разбери этот шаг подробнее" |

---

## Team Profile Template

After analysis, build this profile:

```markdown
## Team Profile

**TEAM:** [Name]
**DOMAIN:** [Content/Tech/Business/Creative]
**CORE PROBLEM:** [1 sentence]

### Roles Identified

| Role | Responsibilities | Input → Output |
|------|-----------------|----------------|
| [Role 1] | [What they do] | [I → O] |
| [Role 2] | [What they do] | [I → O] |

### Workflow

```
[Stage 1] → [Stage 2] → [Stage 3] → [Output]
    ↓           ↓           ↓
[Who/What]  [Who/What]  [Who/What]
```

### Decision Points

| Decision | Who Decides | Based On |
|----------|-------------|----------|
| [Decision 1] | [Role/Human] | [Criteria] |

### Quality Gates

| Gate | Stage | Criteria |
|------|-------|----------|
| [Gate 1] | After [Stage] | [Pass/Fail criteria] |

### Handoffs to Human

- [When to involve human]
- [What requires approval]
- [Escalation triggers]
```

---

## Inference Rules

Fill gaps when user doesn't specify:

| User Says | Implies |
|-----------|---------|
| "контент" without details | Threads + possible YouTube |
| "проверять", "валидировать" | QA/Diagnostic pattern |
| "генерировать", "создавать" | Worker pattern |
| "координировать", "управлять" | Orchestrator pattern |
| "полный цикл", "от А до Я" | Full pipeline with all stages |
| "автоматизировать" | Need to identify manual steps first |

---

## Role Composition Patterns

Common team structures:

### Content Team (minimum)
```
Writer + Editor + Researcher
```

### Content Team (full)
```
Strategist + Writer + Editor + Researcher + SEO + Social Manager
```

### Video Team (minimum)
```
Scriptwriter + Video Editor
```

### Video Team (full)
```
Strategist + Scriptwriter + Editor + Thumbnail Designer + SEO
```

### Analytics Team
```
Business Analyst + Data Analyst + Competitive Analyst
```

---

## From Answers to Skill Sections

| Answer Component | Maps to Skill Section |
|-----------------|----------------------|
| Goal description | Frontmatter description, ## What it does |
| Input/Output | ## Workflow inputs/outputs |
| Decision points | ## Decision Framework, ## What Stays Human |
| Workflow stages | ## Workflow steps |
| Roles mentioned | ## Team Replaced table |
| Quality criteria | ## Quality Gates |
| Problems/failures | ## Edge Cases |
| Boundaries | ## Boundaries section |
