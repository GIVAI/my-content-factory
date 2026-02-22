---
name: youtube
description: "YouTube script-writer. Use when user asks about YouTube scripts, hooks, video structure, retention, SEO, thumbnails, titles. Activates on: 'youtube script', 'write script', 'video hook', 'video structure', 'youtube seo', 'thumbnail', 'youtube скрипт', 'напиши скрипт', 'хук для видео', 'структура видео', 'превью'."
---

# YouTube Script & Content Skill

Universal skill for creating YouTube content: from idea to publication.

## Core Principle

```
Hook = 50% of video success
First 30 seconds determine everything
Every payoff must reward the viewer
```

---

## File Router

When requested, load the corresponding reference file:

| Request contains | File |
|------------------|------|
| hook, opener, opening, first seconds, ВИСП | [youtube-hooks.md](youtube-hooks.md) |
| structure, payoff, logline, video format | [youtube-structure.md](youtube-structure.md) |
| script, scenario, patterns, DNA | [youtube-script-dna.md](youtube-script-dna.md) |
| retention, open loops | [youtube-retention.md](youtube-retention.md) |
| cta, call to action, subscribe, engagement | [youtube-cta.md](youtube-cta.md) |
| seo, tags, description, algorithm | [youtube-seo.md](youtube-seo.md) |
| title, video title, headline | [youtube-titles.md](youtube-titles.md) |
| thumbnail, preview, miniature | [youtube-thumbnails.md](youtube-thumbnails.md) |
| shorts, vertical | [youtube-shorts.md](youtube-shorts.md) |
| research, competitors | [youtube-research.md](youtube-research.md) |
| filming, camera, shooting | [youtube-filming.md](youtube-filming.md) |
| editing, post-production | [youtube-editing.md](youtube-editing.md) |
| publishing, upload | [youtube-publishing.md](youtube-publishing.md) |
| channel setup | [youtube-channel-setup.md](youtube-channel-setup.md) |
| ai prompts, generation | [youtube-ai-prompts.md](youtube-ai-prompts.md) |

---

## Context Loading

При генерации контента загрузи из проекта:

1. `projects/{project}/brand/voice-style.md` — как писать
2. `projects/{project}/learning/patterns.md` — что работает
3. `projects/{project}/learning/examples/youtube/` — референсы

**Используй примеры пользователя как образец стиля.**

---

## Workflow: Script Creation

```
1. Research → youtube-research.md
   - Competitor analysis
   - Topic validation
   - Reference gathering

2. Planning → youtube-structure.md
   - Logline (1-2 sentences)
   - Format (short/medium/long)
   - Payoff list

3. Hook → youtube-hooks.md + youtube-script-dna.md
   - ВИСП check
   - TTS formula
   - Open loop

4. Body → youtube-structure.md + youtube-retention.md
   - Payoffs by structure
   - Open loops between sections
   - Mega payoff at the end

5. CTA → youtube-cta.md
   - Call to action
   - Subscribe/like

6. Metadata → youtube-seo.md + youtube-titles.md
   - Title
   - Description
   - Tags

7. Thumbnail → youtube-thumbnails.md
   - Thumbnail concept
```

---

## Quick Actions

| Command | Action | Files |
|---------|--------|-------|
| "youtube script [topic]" | Full script with hook | hooks + structure + script-dna |
| "youtube hook [topic]" | 5-10 hook variations | hooks + script-dna |
| "youtube structure [topic]" | Video plan with payoffs | structure |
| "youtube seo [topic]" | Title + description + tags | seo + titles |
| "youtube thumbnail [topic]" | Thumbnail concept | thumbnails |
| "youtube shorts [topic]" | Short-form script | shorts |
| "check ВИСП" | Opener audit | hooks |

---

## Key Frameworks

### ВИСП (for opener)
| Component | Question |
|-----------|----------|
| **В** (Value) | What will the viewer get? |
| **И** (Intrigue) | Is there a question in their head? |
| **С** (Urgency) | Why not delay? |
| **П** (Relevance) | Is this about me? |

### TTS (for educational content)
| Element | Description |
|---------|-------------|
| **T**arget | Who is the audience |
| **T**ransformation | What will change |
| **S**takes | What's at stake |

### Payoff Structure
```
Setup → Development → "So what?" → Zinger → Open Loop
```

---

## Technical Rules

```
- 150 words ≈ 1 minute spoken
- Hook: 50-100 words (~30 sec)
- Payoff: 300-500 words
- Short: 2-5 min (quick tips)
- Medium: 6-12 min (tutorials)
- Long: 15+ min (deep dives)
```

---

## Quality Checklist

Before delivering a script:

- [ ] Logline clear in 1-2 sentences?
- [ ] Hook passes ВИСП check?
- [ ] Open loops between sections?
- [ ] Each payoff rewards the viewer?
- [ ] Mega payoff at the end is the strongest?
- [ ] CTA feels natural?
- [ ] Length matches the format?

---

## Notes

- Script = conversation with ONE person
- Not "you all", but "you"
- Every 3-5 minutes — attention reset (self-question)
- Open loop = unresolved tension
- Mega payoff = most important point, place it at the end

---

## Learning Integration

### Где искать паттерны

| Источник | Путь |
|----------|------|
| **Global** | `skills/youtube/` |
| **Project** | `projects/{project}/learning/skill-learning/youtube/patterns.md` |
| **Anti-patterns** | `projects/{project}/learning/skill-learning/youtube/anti-patterns.md` |
| **Examples** | `projects/{project}/learning/skill-learning/youtube/examples/` |

### Команды обучения

| Команда | Куда пишет |
|---------|-----------|
| `это сработало: [что]` | `skill-learning/youtube/patterns.md` |
| `это не сработало: [что]` | `skill-learning/youtube/anti-patterns.md` |
| `запомни пример` | `skill-learning/youtube/examples/` |

---

## Critics System

После генерации скрипта — 3 критика.

### Hook Expert
- ✅ Проходит ВИСП-проверку
- ✅ Интрига в первые 30 сек
- ❌ Нет open loop

### Retention Expert
- ✅ Payoffs каждые 3-5 мин
- ✅ Open loops между секциями
- ❌ Провалы внимания

### Structure Expert
- ✅ Logline ясен
- ✅ Mega payoff в конце
- ❌ Размытая структура

---

*YouTube Skill v1.1 — Learning + Critics*
