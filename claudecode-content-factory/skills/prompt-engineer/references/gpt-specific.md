# GPT-Specific Prompt Engineering

Detailed guide for optimizing prompts for OpenAI's GPT models (GPT-4, GPT-4 Turbo, o1, o3).

---

## GPT Model Spectrum

### Understanding Model Types

| Model | Type | Best For | Prompting Style |
|-------|------|----------|-----------------|
| GPT-4 / GPT-4 Turbo | Instruction-following | General tasks, coding, analysis | Explicit, detailed instructions |
| GPT-4o | Multimodal | Vision + text tasks | Image + text combined |
| o1 | Reasoning | Complex logic, math, science | High-level goals |
| o3 | Advanced Reasoning | Most complex problems | Strategic direction only |

### The Key Insight

> **GPT-4 = Junior developer** → needs explicit, step-by-step instructions
> **o1/o3 = Senior developer** → give goals, let them figure out details

---

## GPT-4 / GPT-4 Turbo Prompting

### Structure That Works

```markdown
# System Message
You are a [specific role] with expertise in [domain].
Your communication style is [style].

# Instructions
[Clear, explicit task description]

## Steps
1. First, [specific action]
2. Then, [next action]
3. Finally, [concluding action]

# Input
[User's data or question]

# Output Format
[Exact format specification]

# Constraints
- [What not to do]
- [Boundaries]
```

### System Message Best Practices

**Good:**
```
You are a senior Python developer specializing in data engineering.
You write clean, efficient code following PEP 8 standards.
You always include error handling and type hints.
You explain your reasoning before showing code.
```

**Bad:**
```
You are a helpful assistant.
```

### Explicit Instructions Work Best

GPT-4 performs better with explicit detail:

```markdown
# Task
Analyze this customer review and extract structured data.

# Detailed Instructions
1. Read the entire review first
2. Identify the overall sentiment (positive/negative/neutral/mixed)
3. Extract specific product mentions
4. Note any feature requests or complaints
5. Identify the customer segment if possible (new user, power user, etc.)
6. Rate urgency of any issues mentioned (high/medium/low)

# Output Format
{
  "sentiment": "positive|negative|neutral|mixed",
  "confidence": 0.0-1.0,
  "products_mentioned": ["product1", "product2"],
  "complaints": ["complaint1"],
  "feature_requests": ["request1"],
  "customer_segment": "string or null",
  "urgency": "high|medium|low|none"
}

# Review
{{REVIEW_TEXT}}
```

### JSON Mode

GPT-4 has native JSON mode for structured output:

```python
response = client.chat.completions.create(
    model="gpt-4-turbo",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "Output valid JSON only."},
        {"role": "user", "content": prompt}
    ]
)
```

**Prompt for JSON mode:**
```markdown
Extract the following information as JSON:

Input: {{TEXT}}

Required fields:
- name (string)
- email (string or null)
- company (string or null)
- topics (array of strings)

Return ONLY the JSON object, no other text.
```

---

## o1 / o3 Reasoning Models

### Fundamental Difference

Reasoning models have internal chain-of-thought. **Don't** prompt them like GPT-4.

### What Works for o1/o3

**High-level goals instead of detailed steps:**

```markdown
# GPT-4 style (TOO DETAILED for o1)
1. First, identify the variables
2. Set up the equation
3. Solve for x
4. Check your answer

# o1 style (BETTER)
Solve this math problem. Show your final answer clearly.

Problem: {{PROBLEM}}
```

### o1/o3 Best Practices

**DO:**
- Provide clear end goal
- Include all necessary context
- Specify output format
- Let the model reason

**DON'T:**
- Give step-by-step instructions
- Ask to "think step by step" (it already does)
- Over-constrain the reasoning path
- Use chain-of-thought prompts

### Examples: GPT-4 vs o1

**Complex Analysis Task:**

```markdown
# GPT-4 Version
Analyze this business situation:

Step 1: Identify the key stakeholders
Step 2: List their interests and concerns
Step 3: Identify conflicts between stakeholders
Step 4: Evaluate possible solutions
Step 5: Recommend the best approach with justification

Situation: {{SITUATION}}

# o1 Version
Analyze this business situation and recommend the best approach.
Consider all stakeholders and potential conflicts.

Situation: {{SITUATION}}

Provide your recommendation with clear justification.
```

**Math Problem:**

```markdown
# GPT-4 Version
Solve this problem step by step:
1. Identify what we're looking for
2. Set up the relevant equations
3. Solve systematically
4. Verify the answer

Problem: {{PROBLEM}}

# o1 Version
Solve this problem: {{PROBLEM}}

Show your final answer.
```

---

## Function Calling / Tools

GPT models have strong tool-use capabilities. Use the `tools` parameter instead of manual prompting.

### Defining Tools

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_database",
            "description": "Search the product database for items",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    },
                    "category": {
                        "type": "string",
                        "enum": ["electronics", "clothing", "home"],
                        "description": "Product category to filter by"
                    },
                    "max_price": {
                        "type": "number",
                        "description": "Maximum price filter"
                    }
                },
                "required": ["query"]
            }
        }
    }
]
```

### Tool Use Prompting

```markdown
# System Message
You are a shopping assistant. Use the available tools to help users find products.

When a user asks about products:
1. Use search_database to find relevant items
2. Present results clearly with prices
3. Make recommendations based on their needs

If you can't find what they're looking for, suggest alternatives.
```

### Best Practices for Tools

1. **Descriptive names**: `search_database` not `search`
2. **Clear descriptions**: What the tool does AND when to use it
3. **Well-defined parameters**: Include descriptions and enums where possible
4. **Error guidance**: In system message, explain what to do if tool fails

---

## Temperature and Parameters

### Temperature Guide

| Temperature | Use Case | Example |
|-------------|----------|---------|
| 0 | Factual extraction, classification | Data parsing, sentiment analysis |
| 0.3-0.5 | Balanced tasks | Summarization, Q&A |
| 0.7-0.9 | Creative tasks | Writing, brainstorming |
| 1.0+ | Maximum creativity | Poetry, experimental content |

### Other Parameters

```python
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=messages,
    temperature=0.7,      # Creativity vs determinism
    max_tokens=1000,      # Length limit
    top_p=1,              # Nucleus sampling (usually leave at 1)
    frequency_penalty=0,  # Reduce repetition
    presence_penalty=0,   # Encourage new topics
    stop=["END"]          # Stop sequences
)
```

### Parameter Combinations

**Factual/Precise:**
```python
temperature=0, top_p=1
```

**Balanced:**
```python
temperature=0.5, top_p=0.9
```

**Creative:**
```python
temperature=0.9, top_p=0.95, presence_penalty=0.5
```

---

## Prompt Patterns for GPT

### Few-Shot with Clear Separation

```markdown
# Task
Classify customer support tickets.

# Examples

Ticket: "Can't log in to my account, tried resetting password"
Category: account_access
Priority: high

Ticket: "When will the new features be released?"
Category: feature_inquiry
Priority: low

Ticket: "The app crashes when I upload large files"
Category: bug_report
Priority: high

# Your Task
Classify this ticket:

Ticket: "{{TICKET_TEXT}}"
Category:
Priority:
```

### Chain of Thought (GPT-4)

```markdown
# Task
Determine if this argument is logically valid.

# Instructions
Think through this step by step:
1. Identify the premises
2. Identify the conclusion
3. Check if conclusion follows from premises
4. Identify any logical fallacies

# Argument
{{ARGUMENT}}

# Analysis
Let me analyze this step by step...
```

### Role + Constraints Pattern

```markdown
# Role
You are a legal document analyst specializing in contract law.

# Your Capabilities
- Identify key clauses and terms
- Spot potential issues or ambiguities
- Explain legal language in plain English
- Highlight areas needing attorney review

# Your Limitations
- You do NOT provide legal advice
- You do NOT guarantee interpretations are correct
- You ALWAYS recommend consulting a licensed attorney
- You flag uncertainty rather than guessing

# Task
Analyze this contract clause:

{{CONTRACT_CLAUSE}}

Provide:
1. Plain English summary
2. Key terms identified
3. Potential concerns
4. Questions for an attorney
```

---

## GPT vs Claude Comparison

| Aspect | GPT-4 | Claude |
|--------|-------|--------|
| Preferred structure | Markdown | XML tags |
| System message | Strong influence | Moderate influence |
| JSON output | Native JSON mode | Via instructions |
| Thinking prompts | Explicit CoT helps | XML thinking tags |
| Tool use | Built-in tools API | Via prompting |
| Long context | Up to 128K | Up to 200K |
| Following rules | Good with explicit | Good with implicit |

### When to Choose GPT

- Need native JSON mode
- Using OpenAI tools/function calling
- Building with OpenAI ecosystem
- Need o1/o3 for complex reasoning
- Image generation (DALL-E integration)

### Prompts That Work for Both

```markdown
# Universal Structure

## Role
[Persona description]

## Task
[Clear task description]

## Input
[Data to process]

## Instructions
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output Format
[Exact format specification]

## Constraints
- [Constraint 1]
- [Constraint 2]

## Examples (if needed)
Input: [example]
Output: [example]
```

---

## Common GPT Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Vague system message | Generic responses | Specific role + style + constraints |
| CoT for o1 | Redundant, hurts performance | Remove step-by-step instructions |
| No format specification | Inconsistent output | Add explicit format + example |
| Over-relying on temperature | Unpredictable results | Fix prompt first, tune temp last |
| Manual tool descriptions | Error-prone | Use tools API |
| Ignoring JSON mode | Parsing issues | Enable for structured output |
| Same prompt for all models | Suboptimal results | Tailor to model type |

---

## GPT Prompt Templates

### General Task (GPT-4)

```markdown
You are a {{ROLE}} with expertise in {{DOMAIN}}.

## Task
{{TASK_DESCRIPTION}}

## Input
{{INPUT}}

## Requirements
- {{REQUIREMENT_1}}
- {{REQUIREMENT_2}}

## Output Format
{{FORMAT}}

## Constraints
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
```

### Reasoning Task (o1/o3)

```markdown
{{PROBLEM_DESCRIPTION}}

Context: {{RELEVANT_CONTEXT}}

Provide your answer with clear reasoning.
```

### Analysis with Examples (GPT-4)

```markdown
# Task
{{TASK}}

# Examples
{{EXAMPLE_1}}

{{EXAMPLE_2}}

# Your Input
{{INPUT}}

# Analyze following the pattern shown in examples:
```

---

## Sources

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [OpenAI Cookbook](https://cookbook.openai.com/)
- [GPT-4 Best Practices](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [o1 Prompting Guide](https://cookbook.openai.com/examples/o1)
