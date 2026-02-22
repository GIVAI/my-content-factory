# Sources — Universal Learning

> Откуда взяты паттерны и метрики эффективности.

---

## Источники данных

| Проект | Тип контента | Паттернов | Score | Дата |
|--------|--------------|-----------|-------|------|
| expert-threads | Threads | 14 | avg 90.6% | 2026-01-24 |
| expert-carousel | Carousel | 5 | approved | 2026-01-23 |
| expert-video | TikTok/Reels | 3 | pending | 2026-01-24 |

---

## Как измеряется Score

### Threads
- **Sales Critic:** Продающая сила (hook, CTA, urgency)
- **Creative Critic:** Креативность (оригинальность, метафоры)
- **Structure Critic:** Структура (flow, readability)
- **Итоговый Score:** Среднее трёх критиков

### Carousel
- **User Approval:** Принято без правок = approved
- **User Rejection:** Требуются правки = rejected
- **Pattern Extraction:** Из approved → approved-patterns

### Video/Reels
- **Views/Retention:** (когда будут данные)
- **Comments/Shares:** (когда будут данные)

---

## Статистика

### По типу паттерна

| Тип | Anti-patterns | Approved | Ratio |
|-----|---------------|----------|-------|
| Стилистика | 7 | 6 | 0.86 |
| Структура | 4 | 5 | 1.25 |
| Темы | 3 | 4 | 1.33 |
| Carousel-specific | 3 | 2 | 0.67 |
| Video-specific | 2 | 0 | 0.00 |

### По частоте нарушений

| Anti-pattern | Частота | Проекты |
|--------------|---------|---------|
| AI → ИИ | 100+ | expert-threads |
| Стрелки → | 50+ | expert-threads |
| Длина > 400 | 10+ | expert-threads |
| Стаккато | 5+ | expert-video, expert-threads |

---

## Promotion Flow

```
Проект Learning (1 hit)
        ↓
    2+ проектов?
        ↓ YES
Learning Agent предлагает
        ↓
   User confirms
        ↓
Universal Learning
```

---

## Changelog

### 2026-01-24
- Initial extraction from expert-threads (10 posts)
- Added expert-carousel carousel patterns
- Added expert-video video anti-patterns
- Created Universal Anti-Patterns (16 items)
- Created Universal Approved Patterns (12 items)

---

*Sources v1.0 — Content Factory*
