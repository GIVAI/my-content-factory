# Advanced Prompt Engineering Techniques

Research-backed techniques for complex reasoning, agents, and production systems.

---

## Automatic Prompt Engineering (APE)

### What It Is
Framework for automatically generating and selecting optimal prompts using LLMs themselves.

### How It Works

```
1. GENERATION
   LLM generates multiple candidate prompts for a task

2. EXECUTION
   Test each candidate on target model

3. SELECTION
   Choose best-performing prompt based on evaluation
```

### Key Discovery
APE found that `"Let's work this out in a step by step way to be sure we have the right answer"` outperforms the human-written `"Let's think step by step"` on math benchmarks.

### Practical Application

```markdown
# Meta-prompt for APE

Generate 5 different ways to instruct an LLM to {{TASK}}.

For each variant:
1. Write the instruction differently
2. Vary the structure (direct, step-by-step, role-based)
3. Experiment with specificity level

Then analyze which approach would work best for:
- Clarity
- Completeness
- Likelihood of consistent results

Return the best instruction with explanation.
```

### When to Use
- Optimizing prompts for production systems
- Finding better phrasings for common tasks
- A/B testing prompt variations

---

## Retrieval-Augmented Generation (RAG)

### What It Is
Combining information retrieval with text generation to ground responses in external knowledge.

### Architecture

```
User Query
    ↓
[Retrieval System] → Relevant Documents
    ↓
[LLM] + Query + Retrieved Docs
    ↓
Grounded Response
```

### Prompting for RAG Systems

```markdown
# System Prompt for RAG

You are an assistant that answers questions using the provided context documents.

## Rules
1. Base your answers ONLY on the provided context
2. If the context doesn't contain the answer, say "I don't have information about that in the provided documents"
3. Cite your sources: [Source: document_name]
4. If multiple sources conflict, note the discrepancy

## Context Documents
<documents>
{{RETRIEVED_DOCUMENTS}}
</documents>

## User Question
{{QUESTION}}

## Response Format
Answer the question, then list sources used.
```

### RAG-Specific Techniques

**Contextualization prompt:**
```markdown
Given this context, how does it help answer: "{{QUESTION}}"?

Context: {{RETRIEVED_CHUNK}}

Relevance analysis:
- Is this directly relevant? (yes/no)
- What specific information does it provide?
- What's still missing to fully answer the question?
```

**Multi-document synthesis:**
```markdown
Synthesize information from multiple sources to answer: {{QUESTION}}

<source_1>{{DOC_1}}</source_1>
<source_2>{{DOC_2}}</source_2>
<source_3>{{DOC_3}}</source_3>

Instructions:
1. Identify relevant information from each source
2. Note any conflicts or contradictions
3. Synthesize a coherent answer
4. Cite each claim: [Source 1], [Source 2], etc.
```

### When to Use RAG
- Questions requiring current/specific information
- Knowledge bases, documentation Q&A
- Reducing hallucination on factual queries
- Domain-specific applications

---

## ReAct (Reasoning + Acting)

### What It Is
Framework interleaving reasoning traces with actions, enabling LLMs to use external tools while thinking.

### The Pattern

```
Thought: [reasoning about what to do]
Action: [tool_name(parameters)]
Observation: [result from tool]
... (repeat) ...
Thought: [final reasoning]
Answer: [conclusion]
```

### Full ReAct Prompt Template

```markdown
# ReAct Agent

You have access to these tools:
- search(query): Search the web for information
- calculator(expression): Evaluate mathematical expressions
- lookup(term): Look up a term in the knowledge base

## Instructions
To answer questions, use this format:

Thought: [Think about what you need to find out]
Action: [tool_name(parameters)]
Observation: [You will see the result here]

Continue the Thought → Action → Observation cycle until you have enough information.

Then provide:
Thought: [Final reasoning with all gathered information]
Answer: [Your final answer]

## Rules
- Always think before acting
- Use tools when you need external information
- Don't make up tool results
- If a tool fails, try a different approach

## Question
{{QUESTION}}

Begin with your first thought.
```

### ReAct for Specific Domains

**Research Agent:**
```markdown
Thought: I need to find recent papers on {{TOPIC}}
Action: search("{{TOPIC}} research paper 2024")
Observation: [results]

Thought: Let me verify the key claims
Action: search("{{CLAIM}} evidence")
Observation: [results]

Thought: Now I can synthesize the findings
Answer: Based on my research...
```

**Data Analysis Agent:**
```markdown
Thought: First, I need to understand the data structure
Action: describe_data(dataset)
Observation: [schema and stats]

Thought: Now I'll check for the specific pattern
Action: query("SELECT ... WHERE ...")
Observation: [query results]

Thought: The data shows...
Answer: [analysis with evidence]
```

### When to Use ReAct
- Tasks requiring external information
- Multi-step research and verification
- Tool-use scenarios
- Debugging and investigation

---

## Reflexion

### What It Is
Framework where agents learn from mistakes through self-reflection, improving over iterations.

### Three Components

```
1. ACTOR: Generates actions/responses
2. EVALUATOR: Scores the output
3. SELF-REFLECTION: Generates improvement insights
```

### The Reflexion Loop

```
Attempt 1:
  → Actor generates response
  → Evaluator scores it (fail)
  → Self-Reflection: "I failed because..."

Attempt 2:
  → Actor generates new response (using reflection)
  → Evaluator scores it (pass)
  → Done
```

### Reflexion Prompt Template

```markdown
# Task
{{TASK_DESCRIPTION}}

# Your Previous Attempt
{{PREVIOUS_RESPONSE}}

# Feedback on Previous Attempt
{{FEEDBACK_OR_ERROR}}

# Self-Reflection
Before trying again, analyze what went wrong:
1. What specific mistake did I make?
2. Why did I make this mistake?
3. What should I do differently?

<reflection>
[Your analysis here]
</reflection>

# New Attempt
Based on your reflection, provide an improved response:
```

### Reflexion for Code

```markdown
# Task
Write a function that {{FUNCTION_DESCRIPTION}}

# Your Previous Code
```python
{{PREVIOUS_CODE}}
```

# Test Results
{{TEST_OUTPUT_WITH_FAILURES}}

# Self-Reflection
<reflection>
Which test cases failed and why?
What edge cases did I miss?
What's the correct approach?
</reflection>

# Corrected Code
```python
[Your improved code]
```
```

### When to Use Reflexion
- Iterative improvement tasks
- Code generation and debugging
- Complex reasoning requiring multiple attempts
- Learning from failure patterns

---

## Program-Aided Language Models (PAL)

### What It Is
Using LLMs to generate executable code instead of reasoning in natural language.

### The Pattern

```
Problem → LLM generates Python code → Execute code → Answer
```

### PAL Prompt Template

```markdown
# Task
Solve this problem by writing Python code.

# Problem
{{PROBLEM}}

# Instructions
1. Read the problem carefully
2. Write Python code that computes the answer
3. Use variables with clear names
4. Add comments explaining your logic
5. Print the final answer

# Examples

Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?

```python
# Initial tennis balls
roger_initial = 5

# Cans bought and balls per can
cans_bought = 2
balls_per_can = 3

# Calculate total
new_balls = cans_bought * balls_per_can
total_balls = roger_initial + new_balls

print(f"Roger has {total_balls} tennis balls")
# Answer: 11
```

# Your Problem
{{PROBLEM}}

Write Python code to solve it:
```

### PAL for Complex Calculations

```markdown
# Date Calculation with PAL

Q: {{DATE_QUESTION}}

```python
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Parse the given information
{{SETUP_CODE}}

# Calculate the answer
{{CALCULATION}}

# Print result
print(f"The answer is: {result}")
```
```

### When to Use PAL
- Math and logic problems
- Date/time calculations
- Problems requiring precise computation
- Tasks where code is more reliable than reasoning

---

## Self-Consistency

### What It Is
Generate multiple reasoning paths, then select the most common answer.

### Implementation

```markdown
# Self-Consistency Prompt

Solve this problem using 3 different approaches:

## Problem
{{PROBLEM}}

## Approach 1: Direct Calculation
[Solve step by step]
Answer 1: ___

## Approach 2: Working Backwards
[Solve by working backwards from the goal]
Answer 2: ___

## Approach 3: Simplification
[Simplify the problem, solve, then scale back]
Answer 3: ___

## Final Answer
Compare your three answers. The most consistent answer is: ___
```

### API-Level Self-Consistency

```python
# Pseudocode for self-consistency
responses = []
for i in range(5):
    response = llm.generate(prompt, temperature=0.7)
    answer = extract_answer(response)
    responses.append(answer)

# Majority vote
final_answer = most_common(responses)
```

### When to Use Self-Consistency
- High-stakes reasoning tasks
- Math problems
- Fact verification
- When single responses are unreliable

---

## Active-Prompt

### What It Is
Dynamically selecting the most effective examples for each query based on uncertainty.

### The Process

```
1. Generate answers for training questions (k variations each)
2. Measure uncertainty (disagreement among answers)
3. Identify most uncertain questions
4. Get human annotations for those specific cases
5. Use annotated examples for inference
```

### Practical Adaptation

```markdown
# Identify Uncertainty

For this question, generate 3 different answers:

Question: {{QUESTION}}

Answer A: [approach 1]
Answer B: [approach 2]
Answer C: [approach 3]

Uncertainty Assessment:
- Do all answers agree? (yes/no)
- If no, what's the source of disagreement?
- Which answer has the strongest reasoning?
```

### When to Use Active-Prompt
- Building few-shot examples systematically
- Identifying which examples matter most
- Optimizing limited annotation budget

---

## Directional Stimulus Prompting

### What It Is
Using hints or stimuli to guide LLM output in a specific direction.

### Implementation

```markdown
# Task with Directional Stimulus

Summarize this article:
{{ARTICLE}}

## Stimulus Hints
Focus on:
- The main controversy mentioned
- The economic implications
- The expert opinions cited

These are the key aspects the summary should emphasize.
```

### Generating Stimuli

```markdown
# Meta-prompt for Stimulus Generation

Given this task: {{TASK}}
And this input: {{INPUT}}

Generate 3-5 hint keywords or phrases that would help an LLM focus on the most important aspects:

Hints:
1. [aspect to emphasize]
2. [key element to include]
3. [perspective to consider]
```

### When to Use Directional Stimulus
- Guiding summarization focus
- Emphasizing specific aspects
- Steering generation without full rewriting

---

## Tree of Thoughts (ToT) - Detailed

### What It Is
Exploring multiple reasoning branches, evaluating each, backtracking when needed.

### Full Implementation

```markdown
# Tree of Thoughts Reasoning

Problem: {{PROBLEM}}

## Branch 1
Step 1: [first approach]
Evaluation: Is this promising? (promising/uncertain/dead-end)

If promising:
  Step 2: [continue this branch]
  Evaluation: ...

If dead-end:
  [Backtrack]

## Branch 2
Step 1: [alternative approach]
Evaluation: Is this promising?
...

## Branch 3
Step 1: [third approach]
...

## Synthesis
Best path: [which branch succeeded]
Final answer: [conclusion from best path]
```

### Simplified ToT (3 Experts)

```markdown
# Three Expert Problem Solving

Imagine 3 experts solving this problem together:

Problem: {{PROBLEM}}

Expert 1 (Analytical):
"I would approach this by..."
[reasoning]
"My conclusion is..."

Expert 2 (Creative):
"What if we consider..."
[alternative reasoning]
"This leads me to..."

Expert 3 (Critical):
"I see potential issues with..."
"Let me verify by..."
"My assessment is..."

Moderator:
"Comparing all approaches..."
"The strongest reasoning is..."
"Final answer: ..."
```

### When to Use ToT
- Complex planning problems
- Creative problem-solving
- Puzzles and games
- Strategic decisions

---

## Layered Prompting

### What It Is
Combining multiple prompting techniques in structured layers.

### Layer Structure

```markdown
# Layer 1: Role
<role>
You are a senior security researcher specializing in web vulnerabilities.
10+ years experience. OSCP and OSCE certified.
</role>

# Layer 2: Context
<context>
This is a penetration testing engagement. The client has authorized testing.
Scope: web application at app.example.com
</context>

# Layer 3: Reasoning
<reasoning_approach>
For each potential vulnerability:
1. Identify the vulnerability class
2. Assess severity (CVSS 3.1)
3. Determine exploitability
4. Recommend remediation
</reasoning_approach>

# Layer 4: Format
<output_format>
JSON array of findings, each with:
- vulnerability_type
- severity (critical/high/medium/low)
- location (URL/parameter)
- evidence
- remediation
</output_format>

# Layer 5: Constraints
<constraints>
- Only report confirmed vulnerabilities
- Do not include actual exploit code
- Focus on remediation over exploitation
- Mark false positives if uncertain
</constraints>

# Task
Analyze this HTTP traffic for vulnerabilities:
{{TRAFFIC_LOG}}
```

### When to Use Layered Prompting
- Complex professional tasks
- Production systems requiring multiple safeguards
- Tasks needing both creativity and structure

---

## Prompt Chaining Patterns

### Sequential Chain

```
Prompt 1: Extract entities → entities
Prompt 2: Classify entities → categories
Prompt 3: Find relationships → graph
Prompt 4: Generate summary → output
```

### Conditional Chain

```
Prompt 1: Classify input type
  → If type A: use Prompt 2A
  → If type B: use Prompt 2B
  → If type C: use Prompt 2C
```

### Verification Chain

```
Prompt 1: Generate initial response
Prompt 2: Critique the response
Prompt 3: Improve based on critique
Prompt 4: Verify improvement
```

### Implementation Example

```markdown
# Chain Step 1: Extract
Extract all named entities from this text:
{{TEXT}}

Output as JSON: {"people": [], "organizations": [], "locations": [], "dates": []}

---

# Chain Step 2: Classify (uses output from Step 1)
For each entity, determine its relevance to the main topic:

Entities: {{STEP_1_OUTPUT}}
Main Topic: {{TOPIC}}

Rate each entity: high/medium/low relevance

---

# Chain Step 3: Synthesize (uses outputs from Steps 1 & 2)
Create a summary focusing on highly relevant entities:

Entities by relevance: {{STEP_2_OUTPUT}}
Original text: {{TEXT}}

Summary (150 words max, highlighting key entities):
```

---

## Quick Reference: Technique Selection

| Task | Primary Technique | Why |
|------|-------------------|-----|
| Needs external facts | RAG | Grounds in real data |
| Multi-step + tools | ReAct | Combines thinking with acting |
| Must improve iteratively | Reflexion | Learns from mistakes |
| Math/calculations | PAL | Code is more precise |
| High-stakes accuracy | Self-Consistency | Multiple paths reduce error |
| Complex planning | Tree of Thoughts | Explores alternatives |
| Needs optimization | APE | Finds better prompts |
| Dynamic examples | Active-Prompt | Targets uncertainty |
| Guided output | Directional Stimulus | Steers without rewriting |
| Production complexity | Layered Prompting | Multiple safeguards |

---

## Sources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- Wei et al. "Chain-of-Thought Prompting" (2022)
- Yao et al. "ReAct: Synergizing Reasoning and Acting" (2022)
- Shinn et al. "Reflexion" (2023)
- Wang et al. "Self-Consistency" (2022)
- Zhou et al. "Automatic Prompt Engineer" (2022)
- Lewis et al. "Retrieval-Augmented Generation" (2020)
