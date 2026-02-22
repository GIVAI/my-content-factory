# Agents Index — Content Factory Team

## Overview

AI agent network = content factory team. Each agent is a specialist with a clear role.

---

## Team Structure

```
agents/
│
├── ai-operator.md              ✅ AI Operator (decisions, management)
├── _index.md                   📋 This file
├── _template.md                📋 Agent template
│
├── production/                  # Content creation
│   ├── youtube.md              ✅ YouTube Producer
│   ├── threads.md              ✅ Threads Manager
│   ├── vertical-content.md     ✅ Reels/Shorts/TikTok
│   ├── thumbnail-generator.md  ✅ Thumbnail generator
│   └── content-pipeline.md     ✅ Universal Content Pipeline
│
├── strategy/                    # Planning
│   ├── project-architect.md    ✅ Project Architect
│   ├── selling-meanings.md     ✅ Selling Meanings Agent (NEW)
│   ├── strategist.md           🔲 Marketing Strategist
│   ├── content-planner.md      🔲 Content Planner
│   └── researcher.md           🔲 Researcher
│
├── analytics/                   # Feedback
│   ├── analyst.md              ✅ Analyst (metrics + learning loop)
│   ├── qa-reviewer.md          🔲 QA Reviewer
│   └── critics/                ✅ Three critics (sales, creative, structure)
│
└── audience/                    # Templates (audience lives in projects/)
    └── audience-template.md    📋 Template for audience.md
```

**Legend:** ✅ Complete | 🔲 Skeleton | 📋 Template/Index

---

## Agent Cards

### Core

| Agent | Role | File |
|-------|------|------|
| **AI Operator** | Decisions and management | `agents/ai-operator.md` |

### Production (Content Creation)

| Agent | Role | Triggers | File |
|-------|------|----------|------|
| **YouTube Producer** | Scripts, packaging | youtube, script, video, скрипт, видео | `production/youtube.md` |
| **Threads** | Posts, hooks, series | threads, post, hook, пост, хук | `production/threads.md` |
| **Vertical Content** | Reels, Shorts, TikTok | reels, shorts, vertical, вертикалка | `production/vertical-content.md` |
| **Thumbnail Generator** | YouTube thumbnails | thumbnail, превью | `production/thumbnail-generator.md` |

### Strategy (Planning)

| Agent | Role | Triggers | Status |
|-------|------|----------|--------|
| **Project Architect** | Project creation and setup | new project, create project, новый проект, создай проект | ✅ |
| **Selling Meanings** | Extract, formulate, amplify selling meanings | смысл, meaning, продающий, positioning | ✅ |
| **Strategist** | Funnels, positioning | strategy, funnel, стратегия, воронка | 🔲 |
| **Content Planner** | Calendars, categories | content plan, calendar, контент-план, календарь | 🔲 |
| **Researcher** | Competitor analysis, trends | research, competitors, исследование, конкуренты | 🔲 |

### Analytics (Feedback)

| Agent | Role | Triggers | Status |
|-------|------|----------|--------|
| **Analyst** | Metrics, learning loop | analytics, metrics, аналитика, метрики | ✅ |
| **QA Reviewer** | Quality control | review, check, проверь, ревью | 🔲 |
| **Critics** | Sales, Creative, Structure | critique, review, критика | ✅ |

### Production Pipeline

| Agent | Role | Triggers | Status |
|-------|------|----------|--------|
| **Content Pipeline** | 10-stage universal pipeline | pipeline start, pipeline status | ✅ |

### Audience (Templates)

> **Note:** Audience and personas are stored in each project separately:
> `projects/{project}/strategy/audience.md`

| File | Purpose |
|------|---------|
| `persona-template.md` | Template for creating personas in projects |

---

## Interaction Flow

```
                         ┌─────────────┐
                         │ AI OPERATOR │ ◄── Decisions, management
                         │   (core)    │
                         └──────┬──────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
       ┌──────────┐     ┌──────────┐     ┌──────────┐
       │ YOUTUBE  │     │ THREADS  │     │ VERTICAL │
       │ PRODUCER │     │          │     │ CONTENT  │
       └────┬─────┘     └────┬─────┘     └────┬─────┘
            │                │                │
            └────────────────┼────────────────┘
                             ▼
                      ┌─────────────┐
                      │  THUMBNAIL  │
                      │  GENERATOR  │
                      └──────┬──────┘
                             │
                             ▼
                      ┌─────────────┐
                      │  QA         │
                      │  REVIEWER   │
                      └──────┬──────┘
                             │
                             ▼
                      ┌─────────────┐
                      │  ANALYST    │
                      └─────────────┘
```

---

## How to Use

1. **Identify the task** → find agent by triggers
2. **Load the agent** → production/strategy/etc.
3. **Load the project** → your project settings
4. **Execute the task** → follow agent pipeline

---

## Projects Integration

| Project | Path | Agents Used |
|---------|------|-------------|
| **Your Project** | `projects/{your-project}/` | YouTube, Threads, Vertical, etc. |

> Copy `projects/_template/` to create your first project

---

## Skills Integration

Claude Code skills are located in `skills/`:
- `nano-banana/` — prompt enhancer for images
- `prompt-engineer/` — prompting techniques
- `threads/` — Threads methodology
- `selling-meanings/` — psychology, extraction, formulas, templates, amplification

---

## Training Status

### Fully Trained
- YouTube Producer — from courses, methodologies
- Threads — from courses, patterns
- Vertical Content — from Velizhanin's course
- Thumbnail Generator — from CTR patterns
- Project Architect — inheritance rules
- Analyst — metrics benchmarks, learning loop
- Content Pipeline — 10-stage universal workflow
- Critics — Sales, Creative, Structure
- Selling Meanings — psychology, formulas, templates

### Need Training
| Agent | What's Needed |
|-------|---------------|
| Strategist | Funnel experience |
| Content Planner | Planning experience |
| Researcher | Methodologies, tools |
| QA Reviewer | Checklists |

---

*Фабрика Контента v2.0*  
*Макс Галсон • [galson.pro](https://galson.pro)*
