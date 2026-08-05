# Instagram Reels Module — {PROJECT}

> **Platform:** Instagram Reels
> **Format:** Vertical videos (15-90 seconds)
> **Module Status:** ⬜ Not configured

---

## Architecture

> **Inherits from:**
> - `skills/reels/` → VISP formula, retention tactics
> - `agents/production/vertical-content.md` → Commands, workflow
> - `../../brand/` → Voice, expertise

---

## Skills — Автоматическая загрузка

### Скиллы (из skills/)

| Скилл | Путь | Когда загружать |
|-------|------|-----------------|
| **reels** | `reels/SKILL.md` + `reels-methodology.md` | ВСЕГДА при создании рилс |
| **nano-banana** | `nano-banana/SKILL.md` + нужный модуль | Генерация обложек, визуалов |
| **selling-meanings** | `selling-meanings/SKILL.md` + нужный модуль | Продающие рилс, CTA, офферы |
| **heygen** | `heygen/SKILL.md` + `heygen-rules.md` + `heygen-motion.md` | AI-аватар для видео (озвучка, движение) |

### Модули nano-banana (по задаче)

| Задача | Модуль |
|--------|--------|
| Обложки/thumbnails | `nano-banana/nano-banana-thumbnails.md` |
| Реалистичные фото | `nano-banana/nano-banana-realism.md` |
| Identity Kit (сохранение лица) | `nano-banana/nano-banana-identity-kit.md` |
| Словарь промптов | `nano-banana/nano-banana-vocabulary.md` |

### Модули selling-meanings (по задаче)

| Задача | Модуль |
|--------|--------|
| Вытащить смыслы из текста | `selling-meanings/extraction.md` |
| Усилить текст продающими элементами | `selling-meanings/amplification.md` |
| Формулы копирайтинга (PAS, AIDA) | `selling-meanings/formulas.md` |
| Психология продаж | `selling-meanings/psychology.md` |

### Порядок загрузки при создании рилс

```
1. ВСЕГДА:  reels/SKILL.md + reels-methodology.md
2. ВСЕГДА:  brand/ (голос, экспертиза)
3. АВАТАР:  heygen/SKILL.md (если AI-аватар)
4. ВИЗУАЛЫ: nano-banana/SKILL.md (обложки, визуалы)
5. ПО ТИПУ: selling-meanings (продающий рилс)
6. ОБУЧЕНИЕ: learning/approved-patterns.md + anti-patterns.md
```

---

## Quick Setup

1. Fill account settings (IG username, posting schedule)
2. Configure `visp-rules.md` with tested patterns
3. Update status to ✅ in main CLAUDE.md
4. Generate: `reels [topic]`

---

## Account Settings

**Instagram Handle:** `@{your_handle}`
**Posting Frequency:** `{Daily / 3x week / Weekly}`
**Optimal Length:** 15-30 seconds (max 90 sec)
**Music:** ☐ Use trending audio / ☐ Original audio

---

## VISP Formula

### В — Внимание / Attention (0-2 sec)
**Goal:** Pattern interrupt

Bold text + movement + surprising visual

### И — Интерес / Interest (2-10 sec)
**Goal:** Hook deeper

"Here's why this matters..."

### С — Страх / Urgency (10-30 sec)
**Goal:** Cost of inaction

"If you don't fix this, {negative outcome}"

### П — Польза / Value (30-60 sec)
**Goal:** The solution

```
Here's what to do:
• {Step 1}
• {Step 2}
• {Result}
```

---

## Commands

| Command | Action |
|---------|--------|
| `reels [topic]` | Generate reels script |
| `reels series [topic]` | Generate 3-part series |
| `reels hook [topic]` | Generate VISP hook |

---

## File Structure

```
modules/instagram-reels/
├── CLAUDE.md           # This file
├── visp-rules.md       # VISP applications
├── reels/              # Generated scripts
│   └── YYYY-MM-DD/
└── analytics/
    └── reels-metrics.md
```

---

## Content Guidelines

**DO:**
- ✅ Visual hook in first frame
- ✅ Fast pacing (no dead time)
- ✅ Text overlays for key points
- ✅ VISP structure throughout
- ✅ Clear CTA at end

**DON'T:**
- ❌ Slow intros
- ❌ Static shots (needs movement)
- ❌ Complex explanations
- ❌ Weak ending

---

## Trending Audio

**How to find:**
- Check Reels trending tab
- Use audio library in IG app
- Monitor competitor usage

**When to use:**
- Trending audio = more reach
- Update visp-rules.md with working audio

---

## Metrics Benchmarks

| Metric | Good | Great | Viral |
|--------|------|-------|-------|
| **Plays** | 2-3x followers | 3-10x | 10x+ |
| **Watch %** | 40-60% | 60-80% | 80%+ |
| **Likes** | 3-5% | 5-10% | 10%+ |
| **Shares** | 1-3% | 3-6% | 6%+ |

---

## Related Files

- [[visp-rules|VISP Rules]] — Formula applications
- [[../../templates/script-template|Script Template]] — Reels section
- [[skills/reels/SKILL|Reels Skill]]

---

**Module Version:** 2.0 | **Status:** ⬜ Not configured
