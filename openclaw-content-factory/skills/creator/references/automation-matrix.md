# Automation Matrix

> © Фабрика Контента | OpenClaw Content Factory | Макс Галсон | https://t.me/galsonproai | galson.pro

Determine what can be automated vs needs human input.

---

## Automation Spectrum

5 levels from full automation to human-only:

| Level | Name | Description | Implementation | Example |
|-------|------|-------------|----------------|---------|
| **L5** | Full Auto | Always same logic, deterministic | Python script | PDF rotation, file conversion |
| **L4** | Rule-Based | Follows explicit rules | Reference file with rules | Grammar check, format validation |
| **L3** | Guided | Patterns + AI judgment | Skill with examples | Hook writing, content generation |
| **L2** | Assisted | Human decides, AI helps | Suggestions mode | Strategy, creative direction |
| **L1** | Manual | Human only, AI outputs for review | Confirmation required | Brand approval, publish decision |

---

## Classification Questions

Ask these to determine automation level:

### 1. Can this task be done wrong?

| Answer | Implication |
|--------|-------------|
| "Yes, seriously wrong" | L1-L2 (more human) |
| "Yes, but fixable" | L3 (AI with review) |
| "Rarely" | L4-L5 (more auto) |

### 2. Is the output format fixed?

| Answer | Implication |
|--------|-------------|
| "Exact format required" | L4-L5 (deterministic) |
| "General structure" | L3 (guided) |
| "Depends on context" | L2 (assisted) |

### 3. Does it require taste/style?

| Answer | Implication |
|--------|-------------|
| "Yes, brand voice matters" | L2-L3 (need examples) |
| "Some style needed" | L3 (patterns work) |
| "No, functional only" | L4-L5 (rules work) |

### 4. Are there clear rules?

| Answer | Implication |
|--------|-------------|
| "Yes, documented" | L4-L5 (encode rules) |
| "Yes, but implicit" | L3 (extract patterns) |
| "No, judgment calls" | L1-L2 (human needed) |

### 5. Is there risk if wrong?

| Answer | Implication |
|--------|-------------|
| "High (legal, brand, money)" | L1 (human approval) |
| "Medium (reputation)" | L2-L3 (review before action) |
| "Low (easy to fix)" | L4-L5 (auto is fine) |

---

## Decision Tree

```
Is the output deterministic? (same input → same output)
├── YES → L5 (Script)
└── NO → Are there explicit rules to follow?
    ├── YES → Can rules be fully encoded?
    │   ├── YES → L4 (Rule-based reference file)
    │   └── NO → L3 (Skill with decision guidance)
    └── NO → Does it require human judgment?
        ├── SOMETIMES → L3 (AI does work, human reviews)
        └── ALWAYS → Is it high-stakes?
            ├── YES → L1 (Human only, AI prepares)
            └── NO → L2 (AI suggests, human picks)
```

---

## Implementation by Level

### L5: Full Automation (Scripts)

**When to use:**
- Same logic every time
- No variation needed
- Output is predictable

**Implementation:**
```
scripts/
└── {action}.py  # Deterministic script
```

**Examples:**
- PDF rotation, merging, splitting
- File format conversion
- Data extraction from fixed formats
- Report generation from templates

### L4: Rule-Based (Reference Files)

**When to use:**
- Clear rules exist
- Rules can be expressed as conditions
- Limited variation

**Implementation:**
```
references/
└── rules.md  # Explicit rules
```

**Rules format:**
```markdown
## Rule: [Name]
**IF:** [Condition]
**THEN:** [Action]
**EXAMPLE:** [Concrete case]
```

**Examples:**
- Grammar and style checks
- Format validation
- Categorization with clear criteria
- Compliance checks

### L3: Guided (Skill with Examples)

**When to use:**
- Patterns exist but need judgment
- Quality depends on following examples
- Some variation is acceptable

**Implementation:**
```
SKILL.md           # Workflow guidance
references/
├── patterns.md    # What works, what doesn't
└── examples.md    # Good/bad outputs
```

**Examples:**
- Content generation (hooks, posts)
- Code review with style preferences
- Summary creation
- Translation with voice

### L2: Assisted (Suggestions Mode)

**When to use:**
- Human makes final decision
- AI provides options/analysis
- Context changes decision

**Implementation:**
```markdown
## Output Format

Present options:
1. **Option A:** [Description] — [Why it might work]
2. **Option B:** [Description] — [Why it might work]
3. **Option C:** [Description] — [Why it might work]

Recommendation: Option [X] because [reason]
```

**Examples:**
- Strategy recommendations
- Creative direction choices
- Priority decisions
- Topic selection

### L1: Manual (Human Only)

**When to use:**
- High stakes (legal, financial, brand)
- Final approval needed
- Irreversible actions

**Implementation:**
```markdown
## Human Checkpoint

Before proceeding:
- [ ] Review [what]
- [ ] Confirm [decision]
- [ ] Approve [action]

**WAIT** for human confirmation.
```

**Examples:**
- Publish decisions
- Brand voice approval
- Contract terms
- Financial transactions

---

## Common Workflow Patterns

### Content Pipeline

| Stage | Level | Reason |
|-------|-------|--------|
| Topic research | L4 | Rules for source quality |
| Ideation | L3 | Patterns + judgment |
| Writing | L3 | Voice + examples |
| Editing | L3-L4 | Rules + style |
| Final review | L2 | Human picks best |
| Publish | L1 | Human approves |

### Code Review Pipeline

| Stage | Level | Reason |
|-------|-------|--------|
| Lint/format | L5 | Deterministic |
| Style check | L4 | Explicit rules |
| Logic review | L3 | Patterns + judgment |
| Security check | L2-L3 | High stakes |
| Approval | L1 | Human decision |

### Data Processing Pipeline

| Stage | Level | Reason |
|-------|-------|--------|
| Extraction | L5 | Fixed format |
| Cleaning | L4 | Rules for validity |
| Analysis | L3 | Patterns in data |
| Insights | L2 | Interpretation needed |
| Action | L1 | Human decides |

---

## Over-Automation Risks

**Signs of over-automation:**
- Errors that humans would catch
- Output that needs constant correction
- Loss of brand consistency
- Users don't trust the output

**Mitigation:**
- Add review gates at critical points
- Keep L1 checkpoints for irreversible actions
- Build feedback loops (learning from corrections)
- Start with lower automation, increase over time

---

## Under-Automation Risks

**Signs of under-automation:**
- Repetitive manual work
- Inconsistent outputs between sessions
- Time wasted on mechanical tasks
- Human burnout on routine

**Mitigation:**
- Script deterministic operations (L5)
- Encode explicit rules (L4)
- Provide examples for patterns (L3)
- Free humans for judgment calls (L1-L2)

---

## Hybrid Approaches

### Parallel Paths

```
[Input]
    ├── L5 path (auto) → [Result A]
    └── L3 path (guided) → [Result B]
        ↓
    [Human picks A or B]
```

### Escalation Pattern

```
[Input] → L4 (try rules)
    ├── Success → [Output]
    └── Failure → L3 (try patterns)
        ├── Success → [Output]
        └── Failure → L2 (ask human)
```

### Confidence Threshold

```
[AI generates output with confidence score]
    ├── Confidence > 80% → Auto-approve (L5)
    ├── Confidence 50-80% → Human review (L3)
    └── Confidence < 50% → Human decides (L2)
```
