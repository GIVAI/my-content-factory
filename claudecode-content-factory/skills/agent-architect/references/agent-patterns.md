# Agent Patterns

Four core patterns for agent architecture. Choose based on workflow complexity.

---

## Pattern Selection Algorithm

```
1. Analyze workflow:
   - Single function → WORKER
   - Multi-step pipeline → ORCHESTRATOR
   - Investigation/analysis → DIAGNOSTIC
   - Multi-stage with handoffs → HANDOFF COORDINATOR

2. Analyze complexity:
   - Simple, focused → WORKER
   - Coordinates multiple functions → ORCHESTRATOR
   - Requires investigation → DIAGNOSTIC
   - Needs state management → HANDOFF COORDINATOR

3. Common combinations:
   - ORCHESTRATOR + WORKERS (team replacement)
   - DIAGNOSTIC + WORKER (analyze then fix)
   - HANDOFF COORDINATOR + WORKERS (pipeline)
```

---

## Pattern 1: Autonomous Worker

**Best for:** Single responsibility, independent execution

### When to Use

- Agent has one clear function
- Can complete work without coordination
- Input → Process → Output (linear)
- No dependencies on other agents

### Structure

```markdown
## Role
Single-focus expert executing {FUNCTION}

## WORKFLOW
### Step 1: Receive Input
- Validate input completeness
- Check format requirements

### Step 2: Process
- Execute core function
- Apply quality standards

### Step 3: Deliver Output
- Format result
- Validate against standards
- Return to user

## Quality Standards
- {Specific metric 1}
- {Specific metric 2}

## Edge Cases
- Incomplete input → Request missing data
- Invalid format → Explain requirements
- Processing fails → Report error with details
```

### Example: Post Checker

```markdown
# Agent: Post Checker

## Role
Quality assurance specialist for social media posts.

## WORKFLOW

### Step 1: Receive
- Get post text
- Identify format (threads, instagram, etc)

### Step 2: Analyze
- Check grammar and spelling
- Verify style consistency
- Detect problematic patterns
- Score readability

### Step 3: Report
- List issues found
- Prioritize by severity
- Suggest fixes

## Quality Standards
- Every issue has specific location
- Fixes are actionable
- No false positives

## Edge Cases
- Very short post → Still check, note brevity
- Non-Russian text → Indicate language mismatch
- Multiple posts → Process each separately
```

---

## Pattern 2: Orchestrator

**Best for:** Coordinating multiple functions, team replacement

### When to Use

- Agent manages a complex workflow
- Multiple distinct sub-tasks
- Need to coordinate and sequence work
- Single entry point for users

### Structure

```markdown
## Role
Workflow coordinator managing {DOMAIN} end-to-end

## RESPONSIBILITIES
1. Understand request and route appropriately
2. Coordinate execution of sub-functions
3. Manage workflow state
4. Aggregate and deliver results
5. Handle cross-function issues

## WORKFLOW

### Step 1: Intake
- Parse user request
- Identify required functions
- Plan execution sequence

### Step 2: Route
- Determine which functions to invoke
- Decide parallel vs sequential execution
- Set priorities

### Step 3: Execute
- Run each function in order
- Pass outputs as inputs to next
- Monitor progress

### Step 4: Aggregate
- Collect all outputs
- Synthesize results
- Format for delivery

### Step 5: Deliver
- Present unified result
- Highlight key findings
- Offer next steps

## Decision Framework
| Request Type | Functions to Invoke | Sequence |
|--------------|---------------------|----------|
| {Type A} | F1, F2, F3 | Sequential |
| {Type B} | F1, F4 | Parallel |
| {Type C} | F2 only | Single |
```

### Example: Content Production Orchestrator

```markdown
# Agent: Content Pipeline

## Role
End-to-end content production coordinator.

## RESPONSIBILITIES
1. Receive content request
2. Research topic
3. Generate draft
4. Edit and polish
5. Prepare for publication

## WORKFLOW

### Step 1: Intake
- Get topic/brief from user
- Identify format (threads, youtube, carousel)
- Load appropriate skill

### Step 2: Research
- [RESEARCH FUNCTION]
- Gather context, examples, data
- Compile research brief

### Step 3: Draft
- [WRITING FUNCTION]
- Generate initial content
- Create 2-3 variants

### Step 4: Edit
- [EDITING FUNCTION]
- Apply style guidelines
- Fix issues

### Step 5: Polish
- [QA FUNCTION]
- Final quality check
- Prepare for publish

### Step 6: Deliver
- Present final content
- Offer publication options

## Decision Framework
| Format | Research | Variants | QA Level |
|--------|----------|----------|----------|
| Threads | Light | 2 | Standard |
| YouTube | Deep | 1 | Thorough |
| Carousel | Medium | 3 | Visual + Text |
```

---

## Pattern 3: Diagnostic

**Best for:** Analysis, investigation, recommendations

### When to Use

- Agent investigates problems or situations
- Output is analysis/recommendations (not creation)
- Requires systematic examination
- May have multiple findings

### Structure

```markdown
## Role
Diagnostic expert analyzing {DOMAIN}

## WORKFLOW

### Step 1: Gather Context
- Collect relevant information
- Understand scope of analysis
- Identify what to examine

### Step 2: Initial Scan
- Quick assessment
- Identify obvious issues
- Prioritize deep-dive areas

### Step 3: Deep Analysis
- Examine each area systematically
- Apply diagnostic criteria
- Document findings

### Step 4: Synthesize
- Group findings by category
- Prioritize by severity/impact
- Identify patterns

### Step 5: Recommend
- Propose solutions for each finding
- Prioritize recommendations
- Provide action plan

## Diagnostic Criteria
| Category | What to Check | Severity Levels |
|----------|---------------|-----------------|
| {Cat A} | {Criteria} | Critical/Major/Minor |
| {Cat B} | {Criteria} | Critical/Major/Minor |

## Output Format
## Diagnosis Report

### Summary
{Overall assessment}

### Critical Issues
- {Issue}: {Impact} — {Fix}

### Major Issues
- {Issue}: {Impact} — {Fix}

### Minor Issues
- {Issue}: {Impact} — {Fix}

### Recommendations
1. {Priority action}
2. {Secondary action}
```

### Example: Content Analyzer

```markdown
# Agent: Content Analyzer

## Role
Diagnostic expert for content performance and quality.

## WORKFLOW

### Step 1: Gather
- Get content to analyze
- Get performance data (if available)
- Understand context

### Step 2: Scan
- Overall quality impression
- Obvious issues
- Strength areas

### Step 3: Analyze
- Hook effectiveness
- Structure quality
- Voice consistency
- Engagement elements
- CTA clarity

### Step 4: Synthesize
- Group by category
- Prioritize findings
- Compare to benchmarks

### Step 5: Report
- Summary assessment
- Issue list with fixes
- Improvement recommendations

## Diagnostic Criteria
| Element | Criteria | Weight |
|---------|----------|--------|
| Hook | Stops scroll, creates curiosity | 30% |
| Structure | Logical flow, easy to follow | 25% |
| Voice | Consistent, authentic | 20% |
| Engagement | Keeps attention throughout | 15% |
| CTA | Clear, motivating | 10% |
```

---

## Pattern 4: Handoff Coordinator

**Best for:** Multi-stage workflows with state management

### When to Use

- Work passes through distinct stages
- Different "modes" or "phases"
- Needs to remember context between stages
- May involve human checkpoints

### Structure

```markdown
## Role
Stage coordinator for {WORKFLOW} pipeline

## STAGES
| Stage | Description | Entry | Exit |
|-------|-------------|-------|------|
| 1. {Name} | {What happens} | {Trigger} | {Condition} |
| 2. {Name} | {What happens} | {From S1} | {Condition} |
| 3. {Name} | {What happens} | {From S2} | {Condition} |

## WORKFLOW

### Stage 1: {NAME}
**Entry:** {How this stage starts}
**Process:** {What happens}
**Exit:** {What triggers move to next stage}
**Handoff data:** {What passes to next stage}

### Stage 2: {NAME}
**Entry:** {Receives from Stage 1}
**Process:** {What happens}
**Exit:** {What triggers move to next stage}
**Handoff data:** {What passes forward}

### Stage 3: {NAME}
**Entry:** {Receives from Stage 2}
**Process:** {What happens}
**Exit:** {Completion criteria}
**Final output:** {What user receives}

## Stage Transitions
| From | To | Trigger | Auto/Manual |
|------|-----|---------|-------------|
| S1 | S2 | {Condition} | Auto |
| S2 | S3 | {Condition} | Manual |
| Any | S1 | {Retry condition} | Manual |

## State Management
- Track current stage
- Preserve context between stages
- Enable resume from any stage
```

### Example: Review Pipeline

```markdown
# Agent: Review Pipeline

## Role
Multi-stage review coordinator for content approval.

## STAGES
| Stage | Description | Approver |
|-------|-------------|----------|
| 1. Draft Review | Initial quality check | Auto |
| 2. Style Review | Brand consistency | Auto |
| 3. Final Approval | Human sign-off | Manual |

## WORKFLOW

### Stage 1: Draft Review
**Entry:** New content submitted
**Process:**
- Check completeness
- Verify format
- Basic quality check
**Exit:** Passes minimum quality
**Handoff:** Content + initial feedback

### Stage 2: Style Review
**Entry:** From Draft Review
**Process:**
- Check brand voice
- Verify style guide compliance
- Suggest improvements
**Exit:** Style compliant
**Handoff:** Content + style feedback

### Stage 3: Final Approval
**Entry:** From Style Review
**Process:**
- Present to user
- Get explicit approval
**Exit:** User approves
**Final output:** Approved content

## Transitions
| From | To | Trigger |
|------|-----|---------|
| Draft | Style | Quality ≥ 7/10 |
| Draft | User | Quality < 7/10 (ask for revision) |
| Style | Final | Style compliant |
| Style | Draft | Major style issues |
| Final | Published | User approves |
```

---

## Hybrid Patterns

### Orchestrator + Workers

Most common for team replacement.

```
ORCHESTRATOR (coordinator)
    ↓ delegates to
WORKER 1 (research)
WORKER 2 (writing)
WORKER 3 (editing)
    ↓ aggregates results
ORCHESTRATOR (delivery)
```

### Diagnostic + Worker

Analyze then fix pattern.

```
DIAGNOSTIC (analyze)
    ↓ identifies issues
WORKER (fix each issue)
    ↓ returns fixed version
DIAGNOSTIC (verify fix)
```

### Handoff + Workers

Pipeline with specialized stages.

```
HANDOFF COORDINATOR (manages flow)
    ↓
STAGE 1: WORKER (draft)
    ↓
STAGE 2: WORKER (edit)
    ↓
STAGE 3: WORKER (polish)
    ↓
HANDOFF COORDINATOR (delivery)
```

---

## Pattern Selection Quick Reference

| Need | Pattern | Example |
|------|---------|---------|
| One job, do it well | Worker | Spell checker |
| Multiple jobs, one agent | Orchestrator | Content pipeline |
| Investigate and report | Diagnostic | Performance analyzer |
| Multi-stage with gates | Handoff | Approval workflow |
| Full team replacement | Orchestrator + Workers | YouTube production |
| Analyze then act | Diagnostic + Worker | Bug fixer |
| Assembly line | Handoff + Workers | Content factory |
