# Quality Checklist for Generated Agents

Use this checklist to validate every agent before delivery.

---

## Structural Completeness

### Required Sections

- [ ] **META table** — Role, Status, Version, Last Updated
- [ ] **TRIGGERS** — Table with triggers, actions, follow-up questions
- [ ] **Role** — 100-150 words describing persona, expertise, principles
- [ ] **RESPONSIBILITIES** — 5-10 specific, actionable items
- [ ] **WORKFLOW** — Numbered steps with clear progression
- [ ] **QUALITY STANDARDS** — Success criteria and validation checks
- [ ] **EDGE CASES** — Minimum 5 scenarios
- [ ] **BOUNDARIES** — DOES / DOES NOT sections
- [ ] **COMMANDS** — Table with commands and confirmation requirements

### Optional Sections (include when relevant)

- [ ] **DETECTION LOGIC** — For agents with complex triggers
- [ ] **OUTPUT FORMATS** — For agents producing structured output
- [ ] **INTEGRATION** — For agents working with files/other agents
- [ ] **AUTOMATION vs CONFIRMATION** — For agents with autonomous actions
- [ ] **EXAMPLE** — For complex agents

---

## Content Quality

### Role Definition

| Criterion | Check |
|-----------|-------|
| Specific expertise | Not generic "assistant" |
| Clear persona | Reads like a job description |
| Defined principles | How agent makes decisions |
| Tone specified | formal/friendly/expert/etc |

### Responsibilities

| Criterion | Check |
|-----------|-------|
| Actionable verbs | "Analyze", "Generate", "Validate" — not "Help with" |
| Specific scope | Each item clear and bounded |
| No overlap | Responsibilities don't duplicate |
| Complete coverage | All expected functions included |
| 5-10 items | Not too few, not too many |

### Workflow

| Criterion | Check |
|-----------|-------|
| Clear start | First step obvious |
| Clear end | Final output defined |
| Logical progression | Each step follows naturally |
| Decision points explicit | "If X, then Y" stated clearly |
| Input/output per step | What goes in, what comes out |

### Edge Cases

| Criterion | Check |
|-----------|-------|
| Minimum 5 scenarios | Enough coverage |
| Incomplete input handled | What if data missing? |
| Ambiguous request handled | How to clarify? |
| Error scenario handled | What if something fails? |
| Out-of-scope handled | When to refuse/redirect? |
| Action specified | Not just "handle" — concrete steps |

### Boundaries

| Criterion | Check |
|-----------|-------|
| DOES section present | Positive capabilities |
| DOES NOT section present | Explicit limitations |
| Scope clear | No ambiguity about what agent handles |
| Adjacent responsibilities clarified | "This is X's job, not mine" |

---

## Quality Metrics

### Clarity Score

Rate 1-5 for each:

| Aspect | Score | Notes |
|--------|-------|-------|
| Role clarity | /5 | Can someone understand in 10 seconds? |
| Workflow clarity | /5 | Can be followed without questions? |
| Trigger clarity | /5 | When agent activates is obvious? |
| Output clarity | /5 | What user gets is defined? |

**Minimum passing:** 4/5 average

### Specificity Score

| Aspect | Score | Notes |
|--------|-------|-------|
| Responsibilities | /5 | Concrete vs vague |
| Edge cases | /5 | Specific scenarios vs generic |
| Commands | /5 | Precise triggers vs fuzzy |

**Minimum passing:** 4/5 average

### Completeness Score

| Aspect | Score | Notes |
|--------|-------|-------|
| All required sections | /5 | Nothing missing |
| Sufficient depth | /5 | Each section has enough detail |
| Examples where needed | /5 | Complex parts illustrated |

**Minimum passing:** 4/5 average

---

## Autonomy Test

Ask: "Can another AI instance execute this agent without asking questions?"

### Test Scenarios

1. **Happy path** — Typical request
   - [ ] Agent knows what to do
   - [ ] No clarification needed

2. **Edge case** — Unusual but valid request
   - [ ] Handling is defined
   - [ ] Agent doesn't get stuck

3. **Boundary case** — Request at scope edge
   - [ ] Clear whether in/out of scope
   - [ ] Escalation path defined

4. **Failure case** — Something goes wrong
   - [ ] Recovery action specified
   - [ ] User informed appropriately

### Autonomy Rating

| Level | Description |
|-------|-------------|
| **5 - Fully autonomous** | Handles all cases without human input |
| **4 - Mostly autonomous** | Asks for confirmation on major decisions |
| **3 - Semi-autonomous** | Needs guidance on complex cases |
| **2 - Assisted** | Requires frequent human input |
| **1 - Manual** | Cannot operate independently |

**Target:** Level 4+ for production agents

---

## Word Count Guidelines

| Agent Type | Target Words | Range |
|------------|--------------|-------|
| Simple worker | 800-1200 | Focused, single responsibility |
| Standard agent | 1500-2500 | Most production agents |
| Complex orchestrator | 2500-4000 | Multi-capability agents |
| Team replacement | 3000-5000 | Full team capabilities |

**Rule:** If >5000 words, consider splitting into multiple agents.

---

## Pre-Delivery Checklist

Before giving agent to user:

1. [ ] All required sections present
2. [ ] Role is specific (not generic)
3. [ ] Responsibilities use actionable verbs
4. [ ] Workflow has clear start and end
5. [ ] Every decision point has explicit handling
6. [ ] Minimum 5 edge cases with actions
7. [ ] Boundaries prevent scope creep
8. [ ] Commands table complete
9. [ ] Word count in appropriate range
10. [ ] Mentally simulated with edge case — works

---

## Common Issues to Fix

### Problem → Solution

| Issue | Fix |
|-------|-----|
| Generic role ("helpful assistant") | Add specific expertise and domain |
| Vague responsibilities ("help with X") | Use concrete verbs: analyze, generate, validate |
| Missing edge cases | Add: incomplete input, ambiguous, error, out-of-scope |
| No boundaries | Add DOES/DOES NOT sections |
| Unclear workflow | Number steps, add input/output per step |
| No decision points | Add "If X, then Y" for branches |
| Too long (>5000 words) | Split into multiple agents or remove redundancy |
| Too short (<800 words) | Add edge cases, examples, more detail |
