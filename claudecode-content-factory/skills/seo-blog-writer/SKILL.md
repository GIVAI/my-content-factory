---
name: seo-blog-writer
description: "Write SEO-optimized blog articles. Research, screenshots, brand voice, publish-ready content."
triggers:
  - статья
  - блог
  - SEO
  - написать статью
  - article
  - blog post
  - тема для блога
---

# SEO Blog Writer

Write SEO-optimized articles in brand voice with research, screenshots, and proper structure.

---

## Principle

Every article is a **slippery slide**: first sentence pulls to the second, each paragraph to the next. Not an information dump — a story with a position.

---

## REQUIRED: Load Before Writing

| Файл | Зачем |
|------|-------|
| `brand/voice-style.md` | Голос, тон, фирменные выражения |
| `learning/approved-patterns.md` | Что работает в контенте |
| `learning/anti-patterns.md` | Что ЗАПРЕЩЕНО |
| `brand/beliefs.md` | Убеждения, контрарианные мнения |

**Не читал эти файлы = не пиши статью.**

---

## Pipeline

```
1. ТЕМА
   ├── Google Trends research
   ├── Client brief
   ├── Industry news/events
   └── Competitor analysis

2. RESEARCH
   ├── web_search: 3-5 sources
   ├── web_fetch: extract facts, quotes, data
   ├── Verify facts (authoritative sources)
   └── Save: specific numbers, dates, names, quotes

3. SCREENSHOTS & IMAGES
   ├── microlink.io API (for websites):
   │   curl "https://api.microlink.io/?url=URL&screenshot=true"
   ├── Convert: sips -s format jpeg input.png --out output.jpg
   ├── Save to: content/blog/{slug}/
   └── Minimum 2-3 images per article

4. WRITING
   ├── Load ALL brand files
   ├── Structure: see "Article Structure" below
   ├── Style: match voice-style.md
   └── SEO: see "SEO Checklist" below

5. PUBLISH
   ├── Save to: content/articles/{slug}.md
   └── Notify client for review

6. OPTIONAL: Auto-deploy
   └── git add && git commit && git push
```

---

## Article Structure

### For News/Trend Articles:

```
1. HOOK (1-3 sentences)
   └── Fact/stat/situation that grabs attention
   └── NOT a question, NOT "hello", NOT an intro

2. CONTEXT (2-3 paragraphs)
   └── What happened, when, who's involved
   └── Specific numbers, dates, names

3. BREAKDOWN (main part, 3-5 sections with H2/H3)
   └── Each section = one aspect
   └── Screenshots between sections
   └── Quotes from sources (blockquote)
   └── Expert's position: what they think

4. WHY IT MATTERS (1-2 paragraphs)
   └── Connection to reader's reality
   └── Concrete implications

5. WHAT TO DO (numbered list)
   └── Practical steps
   └── No fluff, each item actionable

6. FINALE (2-3 sentences)
   └── Final thought with emotion
   └── Italic for closing (*welcome to...*)
   └── NO explicit CTA like "subscribe"
```

### For Expert/Review Articles:

```
1. HOOK — provocative thesis or contrarian opinion
2. PROBLEM — what's wrong with current approach
3. TECHNOLOGY/SOLUTION — how it works (with proof)
4. PERSONAL EXPERIENCE — "I tried it and here's what happened"
5. PRACTICE — concrete steps for reader
6. FINALE — position + question
```

---

## Writing Style

### Yes ✅
- First person: "I tried", "I discovered"
- Specific numbers: "1.5 million in 5 days", not "a lot"
- Conversational tone
- Have a POSITION, not neutral retelling
- Self-irony acceptable
- Short paragraphs: 1-3 sentences
- Сurrency on the right: 100$, 1490₽

### No ❌
- "Today I want to talk about..." — get to the point
- Passive voice
- Long introductions
- Exclamation marks (overuse)
- Made-up facts and numbers
- "By the way..." before CTA

---

## SEO Checklist

### Frontmatter

```yaml
---
title: "Title ≤60 chars with keyword"
description: "Description ≤160 chars with keywords"
date: YYYY-MM-DD
readingTime: "X min"
tags: ["tag1", "tag2", "tag3"]
cover: "/blog/{slug}/cover.jpg"
---
```

### In Text

- [ ] H2 headings contain keywords
- [ ] First paragraph contains main keyword
- [ ] Internal links to other articles (1-3)
- [ ] External links to sources (2-5)
- [ ] Alt-text on images (`![description](path)`)
- [ ] Meta-description is unique and compelling
- [ ] URL slug is short and clear (no dates, no junk)

### Tags

- 3-5 tags maximum
- One tag = one topic (not "AI agents and automation")

---

## Screenshots

### microlink.io (primary method)

```bash
# Website screenshot
curl -s "https://api.microlink.io/?url=https://example.com&screenshot=true&meta=false&waitForTimeout=5000" \
  | python3 -c "import sys,json,base64,urllib.request; d=json.load(sys.stdin); urllib.request.urlretrieve(d['data']['screenshot']['url'], '/tmp/screenshot.png')"

# Convert to JPEG (required — PNG too heavy)
sips -s format jpeg /tmp/screenshot.png --out ./content/blog/{slug}/screenshot.jpg
```

### Alternatives

- Images from source articles (web_fetch → find img URL)
- Generate cover via Nano Banana (if custom banner needed)
- Client sends screenshots

### Rules

- Minimum 2 images per article
- JPEG, not PNG (file size)
- Descriptive alt-texts

---

## File Paths

| What | Where |
|------|-------|
| Articles | `content/articles/{slug}.md` |
| Images | `content/blog/{slug}/` |
| Patterns | `learning/` |
| Brand | `brand/` |

---

## Verification Before Publish

```bash
# 1. Check anti-patterns
grep -n "forbidden_phrase" content/articles/{slug}.md

# 2. Images exist
ls content/blog/{slug}/

# 3. Frontmatter valid
head -20 content/articles/{slug}.md
```

---

## Related Skills

| Skill | When to use |
|-------|-------------|
| `storytelling` | For long stories, warm-ups |
| `selling-meanings` | If article is sales-focused |
| `nano-banana` | For generating covers/banners |

---

*SEO Blog Writer v1.0 — Content Factory*
