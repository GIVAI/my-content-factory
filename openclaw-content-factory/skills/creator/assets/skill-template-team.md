# Team-Replacing Skill Template

> © Фабрика Контента | OpenClaw Content Factory | Макс Галсон | https://t.me/galsonproai | galson.pro

Use this template for skills that replace entire teams.

---

## Template

```markdown
---
name: {skill-name}
description: "{Team function} skill — {what it does}. Use when: {trigger conditions}. Activates on: {keyword list}."
---

# {Skill Title}

> {One-liner value proposition}

## What This Skill Does

{2-3 sentences describing the skill's core function}

---

## Team Replaced

| Human Role | This Skill Handles | What Stays Human |
|------------|-------------------|------------------|
| {Role 1} | {Automated tasks} | {Human tasks} |
| {Role 2} | {Automated tasks} | {Human tasks} |
| {Role 3} | {Automated tasks} | {Human tasks} |

---

## Workflow

```
[Input] → [Stage 1] → [Stage 2] → [Stage 3] → [Output]
             ↓            ↓            ↓
         {Action}     {Action}     {Action}
```

### Stage 1: {Name}
**Input:** {What comes in}
**Process:** {What happens}
**Output:** {What goes out}
**Automation Level:** {L1-L5}

### Stage 2: {Name}
...

### Stage 3: {Name}
...

---

## File Router

| Request Contains | Load File |
|-----------------|-----------|
| {keywords for topic 1} | references/{file1}.md |
| {keywords for topic 2} | references/{file2}.md |
| {keywords for topic 3} | references/{file3}.md |

---

## Commands

| Command | Action | Requires Confirmation |
|---------|--------|----------------------|
| `/{skill} {action1}` | {Description} | No |
| `/{skill} {action2}` | {Description} | No |
| `/{skill} {action3}` | {Description} | Yes |

---

## Quality Gates

### Gate 1: After {Stage Name}

**Criteria:**
- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}

**If fails:** {What to do}

### Gate 2: After {Stage Name}

**Criteria:**
- [ ] {Criterion 1}
- [ ] {Criterion 2}

**If fails:** {What to do}

---

## Critics

### {Critic 1 Name} Critic
**Focus:** {What they evaluate}
**Questions:**
- {Question 1}
- {Question 2}
- {Question 3}

### {Critic 2 Name} Critic
**Focus:** {What they evaluate}
**Questions:**
- {Question 1}
- {Question 2}
- {Question 3}

### {Critic 3 Name} Critic
**Focus:** {What they evaluate}
**Questions:**
- {Question 1}
- {Question 2}
- {Question 3}

### Evaluation Rules

| Scenario | Action |
|----------|--------|
| Any critic < 40% | Revise that aspect |
| Average < 60% | Major revision needed |
| All critics > 80% | Approve |

---

## Patterns

### Approved Patterns

See: references/approved-patterns.md

Key patterns:
- **{Pattern 1}:** {Brief description}
- **{Pattern 2}:** {Brief description}

### Anti-Patterns

See: references/anti-patterns.md

Avoid:
- **{Anti-pattern 1}:** {Why it fails}
- **{Anti-pattern 2}:** {Why it fails}

---

## Learning Loop

### Quick Commands

| User Says | Action |
|-----------|--------|
| "это сработало" | Add to approved-patterns |
| "это не сработало" | Add to anti-patterns |
| "запомни пример" | Save to examples/ |

### Auto-Learning

After generating output:
- If user edits → ask to record as pattern
- If user approves → optionally save as example

---

## Edge Cases

### {Edge Case 1}

**Trigger:** {When this happens}
**Response:** {What to do}

### {Edge Case 2}

**Trigger:** {When this happens}
**Response:** {What to do}

---

## Integration

### With Project Context

Load from project:
- `projects/{project}/brand/voice-style.md` — Voice and tone
- `projects/{project}/learning/patterns.md` — Project-specific patterns

### With Other Skills

| Skill | When to Use Together |
|-------|---------------------|
| {skill-1} | {Condition} |
| {skill-2} | {Condition} |

---

*{Skill Name} v1.0*
```

---

## Usage Instructions

1. Copy template above
2. Replace all `{placeholders}` with actual content
3. Remove sections that don't apply
4. Add skill-specific sections as needed
5. Keep SKILL.md under 500 lines — move details to references/

---

## Example: Content Manager Skill

```markdown
---
name: content-manager
description: "Content team replacement — handles ideation, creation, and quality review for threads and posts. Use when: need to create content pipeline, manage content workflow. Activates on: контент, content, pipeline, идеи, создать пост."
---

# Content Manager

> One skill to replace your content team's routine work.

## What This Skill Does

Manages the full content creation pipeline from ideation to final review. Handles topic research, content generation, and quality checks. Human approves final output before publish.

---

## Team Replaced

| Human Role | This Skill Handles | What Stays Human |
|------------|-------------------|------------------|
| Content Strategist | Topic ideas, trends | Strategy direction |
| Writer | Draft creation | Voice approval |
| Editor | Grammar, structure | Final approval |

---

## Workflow

```
[Topic] → [Research] → [Draft] → [Review] → [Approved Content]
             ↓            ↓          ↓
         L4 (rules)   L3 (guided)  L4 (critics)
```

### Stage 1: Research
**Input:** Topic or theme
**Process:** Find angles, examples, data
**Output:** Research brief
**Automation Level:** L4

### Stage 2: Draft
**Input:** Research brief + voice guide
**Process:** Generate content following patterns
**Output:** Draft content
**Automation Level:** L3

### Stage 3: Review
**Input:** Draft content
**Process:** Run through 3 critics
**Output:** Reviewed content with scores
**Automation Level:** L4

---

## File Router

| Request Contains | Load File |
|-----------------|-----------|
| threads, пост, thread | references/threads-format.md |
| youtube, видео, script | references/youtube-format.md |
| carousel, карусель | references/carousel-format.md |

---

## Commands

| Command | Action | Requires Confirmation |
|---------|--------|----------------------|
| `/content ideas [тема]` | Generate 10 ideas | No |
| `/content draft [тема]` | Full draft with research | No |
| `/content review` | Run critics on last draft | No |
| `/content publish` | Mark as ready | Yes |

---

## Quality Gates

### Gate 1: After Research

**Criteria:**
- [ ] 3+ angles found
- [ ] Supporting data/examples
- [ ] Matches project themes

**If fails:** Expand research

### Gate 2: After Draft

**Criteria:**
- [ ] Matches voice-style.md
- [ ] Has strong hook
- [ ] Clear CTA

**If fails:** Revise with critics feedback

---

## Critics

### Sales Critic
**Focus:** Conversion potential
**Questions:**
- Does it drive to action?
- Is the CTA clear?
- Are objections addressed?

### Creative Critic
**Focus:** Memorability
**Questions:**
- Is the hook strong?
- Is the angle unique?
- Will people remember?

### Structure Critic
**Focus:** Clarity
**Questions:**
- Is the flow logical?
- Is it the right length?
- Easy to scan?

---

*Content Manager v1.0*
```
