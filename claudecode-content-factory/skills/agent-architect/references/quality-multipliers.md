# Quality Multipliers

Build quality assurance into skills.

---

## Three Multiplier Types

1. **Critics System** — Multiple perspectives evaluate output
2. **Pattern Library** — What works vs what doesn't
3. **Learning Loop** — Skill improves with use

---

## 1. Critics System

### Concept

Instead of one review, apply 3 distinct critic perspectives. Each critic asks different questions about the same output.

### For Content Skills

| Critic | Focus | Questions |
|--------|-------|-----------|
| **Sales Critic** | Conversion | Does it drive action? Clear CTA? Addresses objections? |
| **Creative Critic** | Memorability | Strong hook? Unique angle? Stands out? |
| **Structure Critic** | Clarity | Logical flow? Easy to follow? Right length? |

### For Technical Skills

| Critic | Focus | Questions |
|--------|-------|-----------|
| **Correctness Critic** | Accuracy | Does it work? Edge cases handled? |
| **Maintainability Critic** | Quality | Is it readable? Well-structured? |
| **Performance Critic** | Efficiency | Fast enough? Resource-efficient? |

### For Business Skills

| Critic | Focus | Questions |
|--------|-------|-----------|
| **Impact Critic** | Value | Solves the problem? Measurable result? |
| **Feasibility Critic** | Practicality | Can be implemented? Resources available? |
| **Risk Critic** | Safety | What could go wrong? Mitigations? |

### Implementation in Skills

Add to SKILL.md:

```markdown
## Critics Review

After generating output, evaluate through 3 lenses:

### Critic 1: [Name]
**Focus:** [What they evaluate]
**Questions:**
- [Question 1]
- [Question 2]
- [Question 3]
**Score:** [0-100] based on [criteria]

### Critic 2: [Name]
...

### Critic 3: [Name]
...

### Decision Rules

| Scenario | Action |
|----------|--------|
| Any critic < 40 | Revise that aspect |
| Average < 60 | Consider rewriting |
| All critics > 80 | Approve |
```

### Critic Template for references/critics.md

```markdown
# Critics Evaluation Criteria

## [Critic Name] Critic

**Purpose:** [What this critic cares about]

### Scoring Criteria

| Score | Meaning | Indicators |
|-------|---------|------------|
| 90-100 | Excellent | [What excellent looks like] |
| 70-89 | Good | [What good looks like] |
| 50-69 | Needs work | [What needs improvement] |
| <50 | Revise | [Critical issues] |

### Evaluation Checklist

- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]
- [ ] [Check 4]

### Common Issues

| Issue | How to Fix |
|-------|------------|
| [Issue 1] | [Fix] |
| [Issue 2] | [Fix] |
```

---

## 2. Pattern Library

### Concept

Capture what works and what doesn't. Two files:
- `approved-patterns.md` — Proven approaches
- `anti-patterns.md` — Mistakes to avoid

### Approved Patterns Structure

```markdown
# Approved Patterns

## Pattern: [Name]

**What:** [Brief description]
**Why it works:** [Explanation]
**When to use:** [Context/triggers]

### Example

**Input:** [What user asked]
**Output:** [What worked]

### Variations

- [Variation 1]
- [Variation 2]

---

## Pattern: [Name 2]
...
```

### Anti-Patterns Structure

```markdown
# Anti-Patterns

## Anti-Pattern: [Name]

**What:** [What people do wrong]
**Why it fails:** [Explanation]
**Signs you're doing it:** [How to recognize]

### Bad Example

**Input:** [What user asked]
**Output:** [What didn't work]
**Problem:** [Why it failed]

### What to Do Instead

[Better approach with example]

---

## Anti-Pattern: [Name 2]
...
```

### Implementation in Skills

Add to SKILL.md:

```markdown
## Pattern Library

Before generating, check applicable patterns:

### Approved Patterns
See: references/patterns/approved-patterns.md

Key patterns for this skill:
- **[Pattern 1]:** [When to apply]
- **[Pattern 2]:** [When to apply]

### Anti-Patterns to Avoid
See: references/patterns/anti-patterns.md

Common mistakes:
- **[Anti-pattern 1]:** [Why to avoid]
- **[Anti-pattern 2]:** [Why to avoid]
```

### Pattern Discovery Process

How to find patterns:

1. **After successful output:** Ask "What made this work?"
2. **After failed output:** Ask "What went wrong?"
3. **After user correction:** Ask "What pattern emerges?"
4. **After multiple sessions:** Look for repeated fixes

---

## 3. Learning Loop

### Concept

Skill improves based on real usage. Track what works, update patterns.

### Fast-Track Commands

Build into skills:

| User says | Action | Target |
|-----------|--------|--------|
| "это сработало" | Add to approved | approved-patterns.md |
| "это не сработало" | Add to anti | anti-patterns.md |
| "запомни как пример" | Save output | examples/ |
| "запомни паттерн" | Extract and save | patterns.md |

### Learning Loop Implementation

Add to SKILL.md:

```markdown
## Learning Loop

### Quick Learning

User feedback:
- **"это сработало"** → Записываю в approved-patterns
- **"это не сработало"** → Записываю в anti-patterns
- **"запомни"** → Сохраняю как пример

### Auto-Learning Triggers

After generating content:
```
Контент готов. Сохранить как пример для будущих генераций?
```
→ Yes → Save to examples/

After user edits:
```
Вижу правки. Записать как паттерн?
```
→ Yes → Extract pattern, save to patterns.md

### Pattern Update Process

1. Identify what changed
2. Formulate as pattern/anti-pattern
3. Add to appropriate file
4. Confirm with user
```

### Learning File Structure

```
skill/
├── SKILL.md
└── references/
    ├── patterns/
    │   ├── approved-patterns.md
    │   └── anti-patterns.md
    └── examples/
        ├── good/
        │   ├── example-1.md
        │   └── example-2.md
        └── bad/
            └── example-1.md (with fix notes)
```

---

## Combining Multipliers

### Full Quality Stack

```
[Generate output]
       ↓
[Check against patterns]
       ↓
[Run through critics]
       ↓
[If all pass] → Output
[If any fail] → Revise → Re-check
       ↓
[User feedback]
       ↓
[Update patterns/examples]
```

### Minimal Quality Stack

For simpler skills:

```
[Generate output]
       ↓
[Check against 2-3 key patterns]
       ↓
[One critic perspective]
       ↓
[Output with confidence note]
```

---

## Quality Gates

### Gate Types

| Gate Type | When | What |
|-----------|------|------|
| **Pre-generation** | Before creating | Check patterns, gather context |
| **Post-generation** | After creating | Run critics, check anti-patterns |
| **Pre-output** | Before delivering | Final sanity check |

### Gate Template

```markdown
## Quality Gate: [Name]

**Stage:** [Pre/Post-generation, Pre-output]

### Checklist

- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

### Pass Criteria

All items checked OR:
- [Exception 1]
- [Exception 2]

### Fail Action

If gate fails:
1. [What to do]
2. [How to fix]
3. [When to escalate]
```

---

## Examples for Different Skill Types

### Content Skill

```markdown
## Quality Multipliers

### Critics
- **Sales:** Hook strength, CTA clarity, objection handling
- **Creative:** Uniqueness, memorability, voice match
- **Structure:** Flow, length, format compliance

### Key Patterns
- **Approved:** Open loop hooks, specific numbers, contrast
- **Anti-pattern:** Generic openings, vague promises, walls of text

### Learning
- Save good posts to examples/threads/
- Track which hooks get best engagement
- Update patterns monthly
```

### Technical Skill

```markdown
## Quality Multipliers

### Critics
- **Correctness:** Tests pass, edge cases handled
- **Maintainability:** Readable, documented, modular
- **Performance:** Efficient, no obvious bottlenecks

### Key Patterns
- **Approved:** Error handling at boundaries, clear naming
- **Anti-pattern:** Silent failures, magic numbers

### Learning
- Save tricky solutions to examples/
- Track common bugs, add to anti-patterns
- Review patterns quarterly
```

### Business Skill

```markdown
## Quality Multipliers

### Critics
- **Impact:** Solves real problem, measurable outcome
- **Feasibility:** Actionable, resources available
- **Risk:** Downsides identified, mitigations planned

### Key Patterns
- **Approved:** Data-backed recommendations, clear next steps
- **Anti-pattern:** Vague suggestions, ignored constraints

### Learning
- Track recommendation outcomes
- Update patterns based on what gets implemented
- Review annually
```
