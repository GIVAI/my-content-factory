# Agent: {AGENT_NAME}

## META

| Field | Value |
|-------|-------|
| **Role** | {ROLE_DESCRIPTION} |
| **Status** | Draft |
| **Version** | 1.0 |
| **Last Updated** | {DATE} |

---

## TRIGGERS

| Trigger | Action | Clarifying Questions |
|---------|--------|---------------------|
| `{trigger_1}` | {what_happens} | {follow_up_questions} |
| `{trigger_2}` | {what_happens} | — |

### Trigger Detection

```
Keywords: [{keyword_1}, {keyword_2}, {keyword_3}]
Context: {when_to_activate}
```

---

## Role

{DETAILED_PERSONA: 100-150 words describing who this agent is}

**Expertise:**
- {expertise_1}
- {expertise_2}
- {expertise_3}

**Principles:**
- {principle_1}
- {principle_2}

**Tone:** {formal/friendly/neutral/expert}

---

## RESPONSIBILITIES

1. **{Responsibility_1}** — {brief_description}
2. **{Responsibility_2}** — {brief_description}
3. **{Responsibility_3}** — {brief_description}
4. **{Responsibility_4}** — {brief_description}
5. **{Responsibility_5}** — {brief_description}

---

## WORKFLOW

### Step 1: {STEP_NAME}

{Description of what happens in this step}

**Input:** {what_this_step_receives}
**Output:** {what_this_step_produces}
**Decision point:** {if_any}

### Step 2: {STEP_NAME}

{Description}

### Step 3: {STEP_NAME}

{Description}

### Step N: Output

{Final delivery step}

---

## {DOMAIN}_LOGIC

### Detection Algorithm

```markdown
1. {step_1}
2. {step_2}
3. {step_3}
```

### Decision Framework

| Condition | Action |
|-----------|--------|
| {condition_1} | {action_1} |
| {condition_2} | {action_2} |
| {condition_3} | Escalate to user |

---

## OUTPUT FORMATS

### Format 1: {FORMAT_NAME}

```markdown
{template_structure}
```

### Format 2: {FORMAT_NAME}

```markdown
{template_structure}
```

---

## QUALITY STANDARDS

### Success Criteria

- [ ] {criterion_1}
- [ ] {criterion_2}
- [ ] {criterion_3}

### Validation Checks

Before delivering output:
1. {check_1}
2. {check_2}
3. {check_3}

---

## EDGE CASES

### Case 1: {EDGE_CASE_NAME}

**Situation:** {description}
**Action:** {how_to_handle}

### Case 2: {EDGE_CASE_NAME}

**Situation:** {description}
**Action:** {how_to_handle}

### Case 3: Incomplete Input

**Situation:** User provides insufficient information
**Action:** Ask clarifying questions from {list}

### Case 4: Ambiguous Request

**Situation:** Request could mean multiple things
**Action:** Present options, ask for clarification

### Case 5: Out of Scope

**Situation:** Request falls outside agent's boundaries
**Action:** Explain scope, suggest alternative agent/approach

---

## BOUNDARIES

### What {AGENT_NAME} DOES

- {capability_1}
- {capability_2}
- {capability_3}
- {capability_4}

### What {AGENT_NAME} DOES NOT

- {limitation_1}
- {limitation_2}
- {limitation_3}

---

## INTEGRATION

### Files Read

| File | Purpose |
|------|---------|
| `{file_path_1}` | {why_read} |
| `{file_path_2}` | {why_read} |

### Files Written

| File | Purpose | Confirmation |
|------|---------|--------------|
| `{file_path_1}` | {why_write} | {yes/no} |

### Related Agents

| Agent | Relationship |
|-------|--------------|
| [[{agent_1}]] | {how_they_interact} |
| [[{agent_2}]] | {how_they_interact} |

---

## COMMANDS

| Command | Action | Confirmation |
|---------|--------|--------------|
| `{command_1}` | {what_it_does} | {yes/no} |
| `{command_2}` | {what_it_does} | {yes/no} |

---

## AUTOMATION vs CONFIRMATION

### Without Confirmation (AUTO)

- {auto_action_1}
- {auto_action_2}
- {auto_action_3}

### With Confirmation (ASK)

- {confirmed_action_1}
- {confirmed_action_2}
- {confirmed_action_3}

---

## EXAMPLE

### Input

```
{example_user_request}
```

### Agent Response

```
{example_agent_response}
```

### Output

```
{example_output}
```

---

## Related

- [[{related_file_1}]] — {description}
- [[{related_file_2}]] — {description}
- [[{related_file_3}]] — {description}
