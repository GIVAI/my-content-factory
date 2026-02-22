# HeyGen AI Voiceover Rules

## Why These Rules Matter

HeyGen AI avatars require extra-strong engagement techniques because:
- Non-human delivery lacks natural charisma cues
- Viewers decide faster whether to stay or leave
- Opening must compensate with compelling content immediately
- AI cannot convey drama through pauses — must use content

---

## Forbidden Symbols

These symbols cause lag, mispronunciation, or errors in HeyGen:

| Symbol | Problem | Solution |
|--------|---------|----------|
| `" "` (quotation marks) | Lag, mispronunciation | Remove entirely or rephrase |
| `...` (ellipsis) | Unnatural pause, cuts off | Use period or comma |
| `—` (em dash) | Mispronounced or skipped | Use period or comma |
| `–` (en dash) | Mispronounced | Write out "to" |
| `*` (asterisk) | Read as word or skipped | Remove entirely |
| `" "` (curly quotes) | Same as straight quotes | Remove entirely |
| `&` (ampersand) | May read as "and" or skip | Write "and" |
| `#` (hash) | Read as "hash" or "number" | Write "number" |
| `@` (at symbol) | Read as "at" | Write "at" |
| `%` (percent sign) | May mispronounce | Write "percent" |
| `/` (forward slash) | Read as "slash" | Write "or" or "to" |
| `( )` parentheses | Creates awkward pauses | Rephrase without |
| `[ ]` brackets | Same as parentheses | Rephrase without |

---

## Quotation Marks — Specific Replacements

### For Emphasis
**BAD:** This is the "secret" method
**GOOD:** This is the secret method

### For Quoting Research
**BAD:** The study says "fifty percent improvement"
**GOOD:** The study shows fifty percent improvement
**GOOD:** According to research, fifty percent of men improved

### For Patient Quotes
**BAD:** My patient said "I feel so much better"
**GOOD:** My patient told me he feels so much better
**GOOD:** One patient reported feeling significantly better

### For Technical Terms
**BAD:** What doctors call "chronic pelvic pain syndrome"
**GOOD:** What doctors call chronic pelvic pain syndrome
**GOOD:** The medical term is chronic pelvic pain syndrome

### For So-Called
**BAD:** These "miracle" cures
**GOOD:** These so called miracle cures
**GOOD:** These supposed miracle cures

---

## All Numbers as Words

AI voiceover mispronounces numbers, creates wrong emphasis, or lags.

| Wrong | Correct |
|-------|---------|
| 500 mg | five hundred milligrams |
| 3 times | three times |
| 15% | fifteen percent |
| 5-alpha reductase | five alpha reductase |
| 10 min | ten minutes |
| 40% | forty percent |
| 3-5 | three to five |
| 2x/day | twice daily |
| 24/7 | twenty four seven |
| 1 in 3 | one in three |
| $50 | fifty dollars |
| 8 AM | eight AM |
| 100+ | more than one hundred |
| 2,500 | two thousand five hundred |
| 1.5 | one point five |
| 2-3 weeks | two to three weeks |

---

## Medical Abbreviations

| Wrong | Correct |
|-------|---------|
| BPH | B P H or benign prostatic hyperplasia |
| ED | E D or erectile dysfunction |
| PSA | P S A or prostate specific antigen |
| DHT | D H T or dihydrotestosterone |
| T | testosterone (never just T) |
| mg | milligrams |
| cc | cubic centimeters |
| mL | milliliters |
| ng/mL | nanograms per milliliter |
| Dr. | Doctor |
| vs. | versus |
| etc. | and so on |
| e.g. | for example |
| i.e. | that is |

---

## Sentence Structure

### Keep Sentences Simple

**GOOD:**
> Do this exercise every morning. It takes five minutes. You will see results in two weeks.

**BAD:**
> This exercise, which you should do every morning for about five minutes, will show results within a couple of weeks.

### Maximum Sentence Length
**20 words maximum per sentence**

### Avoid
- Parenthetical phrases
- Complex punctuation
- Lists within sentences
- Medical jargon without explanation
- Nested clauses

---

## No Hypophora

**Hypophora:** Rhetorical question immediately followed by your answer.

**BAD:**
> Cooked tomatoes have ten times more available lycopene than raw tomatoes. Ten.

**GOOD:**
> Cooked tomatoes have ten times more available lycopene than raw tomatoes.

**BAD:**
> What does this mean? It means you should cook your tomatoes.

**GOOD:**
> This means you should cook your tomatoes.

**BAD:**
> Why does this matter? Because your prostate needs lycopene.

**GOOD:**
> Your prostate needs lycopene, which is why this matters.

---

## No Fragmented Sentences

AI voiceover cannot convey dramatic pauses. Short fragments sound robotic.

**BAD:**
> Warm water. Not hot. Not cold. Warm.

**GOOD:**
> Use warm water, somewhere between room temperature and hot.

**BAD:**
> This works. It really works.

**GOOD:**
> This protocol genuinely works for most men who follow it consistently.

**BAD:**
> Simple. Effective. Proven.

**GOOD:**
> The method is simple, effective, and backed by research.

### Rule
If sentence is shorter than 5 words and followed by another short sentence with contrast or repetition — combine into one flowing phrase.

---

## Punctuation That Works

| Use | For |
|-----|-----|
| Period (.) | End of sentences, natural pauses |
| Comma (,) | Brief pauses, lists |
| Question mark (?) | Direct questions only (use sparingly) |

### Avoid or Replace

| Avoid | Replace With |
|-------|-------------|
| Semicolon (;) | Period, start new sentence |
| Colon (:) | Rephrase as complete sentence |
| Exclamation mark (!) | Use sparingly, can sound artificial |

---

## Formatting Checklist

Before delivering any script, verify:

- [ ] NO quotation marks anywhere (`"`, `"`, `"`, `'`)
- [ ] NO ellipsis (`...`)
- [ ] NO em dashes (`—`) or en dashes (`–`)
- [ ] NO asterisks (`*`)
- [ ] NO parentheses or brackets (`()`, `[]`)
- [ ] NO ampersands (`&`)
- [ ] NO percent signs (`%`) — write "percent"
- [ ] NO forward slashes (`/`)
- [ ] ALL numbers written as words
- [ ] ALL medical abbreviations spelled out
- [ ] ALL sentences under 20 words
- [ ] NO hypophora (rhetorical Q + immediate answer)
- [ ] NO fragmented dramatic sentences (under 5 words)
- [ ] Medical disclaimer NOT in voiceover (description only)

---

## Quick Find and Replace

Run these replacements before finalizing:

```
"  →  [delete]
"  →  [delete]
"  →  [delete]
'  →  [delete]
'  →  [delete]
... →  .
—  →  .
–  →  to
&  →  and
%  →  percent
/  →  or (or "to" for ranges)
```

### Regex Patterns

```
Numbers: \d+ → spell out
Percentages: \d+% → [number] percent
Dosages: \d+\s*mg → [number] milligrams
Ranges: \d+-\d+ → [number] to [number]
```

---

## Common Corrections

### Before → After Examples

**Dosages:**
> Take 400mg twice daily
> → Take four hundred milligrams twice daily

**Percentages:**
> 73% of men over 50
> → Seventy three percent of men over fifty

**Ranges:**
> Wait 3-5 days
> → Wait three to five days

**Abbreviations:**
> BPH affects millions
> → B P H, or benign prostatic hyperplasia, affects millions

**Quotes:**
> The study concluded "significant improvement"
> → The study concluded there was significant improvement

**Fragments:**
> Fast. Effective. Simple.
> → This method is fast, effective, and simple.

**Hypophora:**
> What's the solution? The solution is exercise.
> → The solution is exercise.

---

## Testing Script for HeyGen

Before finalizing, search the script for these patterns:

```
Search for: " ' ... — – % ( ) [ ] & / Dr. vs.
Search for: 0 1 2 3 4 5 6 7 8 9
Search for: mg mL cc ng
Search for: BPH ED PSA DHT
```

Any matches = needs correction.

---

## Medical Disclaimer

**NOT in voiceover.** Only in YouTube description.

Standard disclaimer for description:
> This video is for educational purposes only and is not intended to replace professional medical advice. Always consult your physician before starting any new health protocol or making changes to existing treatments.
