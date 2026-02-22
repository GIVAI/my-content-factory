# Technical — Skills Routing & Architecture

> Этот файл для Claude. Человеку читать не нужно.

---

## Skills — Автоматическая загрузка

Все скиллы лежат в `skills/`. Загружай нужные автоматически по триггеру.

| Скилл | Путь | Триггер | Что делает |
|-------|------|---------|------------|
| **threads** | `threads/SKILL.md` + `threads-copywriting.md` + `threads-hooks.md` | "threads", "пост", "тред" | Методика Threads: VISP, хуки, вовлечение |
| **telegram** | `telegram/SKILL.md` + `telegram-copywriting.md` + `telegram-hooks.md` | "telegram", "телеграм", "тг пост" | Методика Telegram: хуки, копирайтинг |
| **youtube** | `youtube/SKILL.md` + нужные модули | "youtube", "сценарий", "script" | YouTube методика: VHF, TOP-5, удержание |
| **carousel** | `carousel/SKILL.md` + `carousel-structure.md` + `carousel-types.md` | "carousel", "карусель" | Структура каруселей, дизайн, CTA |
| **reels** | `reels/SKILL.md` + `reels-methodology.md` | "reels", "shorts", "рилс" | VISP формула, вертикальное видео |
| **selling-meanings** | `selling-meanings/SKILL.md` + нужный модуль | "продающий", "оффер", "CTA", "смыслы" | Продающие смыслы, формулы, психология |
| **storytelling** | `storytelling/SKILL.md` + `slippery-slide.md` | "история", "story", "кейс" | Сторителлинг, скользкая горка, триггеры |
| **nano-banana** | `nano-banana/SKILL.md` + нужный модуль | "картинка", "обложка", "промпт" | Генерация изображений, identity kit |
| **heygen** | `heygen/SKILL.md` + `heygen-rules.md` + `heygen-motion.md` | "heygen", "аватар", "видео аватар" | AI-аватары, правила озвучки |
| **launch** | `launch/SKILL.md` | "запуск", "прогрев", "launch" | Запуски, воронки, прогревы |
| **prompt-engineer** | `prompt-engineer/SKILL.md` | "промпт", "prompt" | Промпт-инженерия |
| **learning-processor** | `learning-processor/SKILL.md` | "обучение", "разобрать материал" | Извлечение знаний из материалов |
| **laozhang-onboarding** | `laozhang-onboarding/SKILL.md` | "laozhang", "генерация картинок", "nano banana api" | Настройка LaoZhang API |
| **copywriting** | `copywriting/SKILL.md` | "копирайтинг", "текст" | Халилов + Шугерман |
| **editing** | `editing/SKILL.md` | "редактура", "отредактируй" | Правила Ильяхова |
| **headlines** | `headlines/SKILL.md` | "заголовок", "headline" | Формулы заголовков |
| **veo-video** | `veo-video/SKILL.md` | "veo", "видео генерация" | Генерация видео через Veo 3.1 |
| **timelapse-creator** | `timelapse-creator/SKILL.md` | "таймлапс", "timelapse" | Создание таймлапсов |
| **seo-blog-writer** | `seo-blog-writer/SKILL.md` | "статья", "блог", "seo" | SEO статьи |

---

## Auto-Loading Rules

### selling-meanings (загружается автоматически для продающего контента)
**Триггеры:** "продающий", "selling", "оффер", "offer", "CTA", "закреп", "pinned", "конверсия", "продажи"

### storytelling (загружается автоматически для историй)
**Триггеры:** "история", "story", "кейс", "case", "сторителлинг", "storytelling"

---

## Модули selling-meanings (загружать по задаче)

| Задача | Модуль |
|--------|--------|
| Вытащить смыслы из текста | `selling-meanings/extraction.md` |
| Усилить текст продающими элементами | `selling-meanings/amplification.md` |
| Формулы копирайтинга (PAS, AIDA, etc) | `selling-meanings/formulas.md` |
| Офферы по Хормози | `selling-meanings/hormozi-offers.md` |
| Психология продаж | `selling-meanings/psychology.md` |
| Готовые шаблоны | `selling-meanings/templates.md` |

## Модули storytelling (загружать по задаче)

| Задача | Модуль |
|--------|--------|
| Скользкая горка (затягивающий текст) | `storytelling/slippery-slide.md` |
| Психологические триггеры | `storytelling/psychological-triggers.md` |
| Продающая статья | `storytelling/selling-article.md` |

---

## Общие паттерны (shared-learnings)

| Файл | Назначение |
|------|------------|
| `shared-learnings/UNIVERSAL-APPROVED-PATTERNS.md` | Что работает (все форматы) |
| `shared-learnings/UNIVERSAL-ANTI-PATTERNS.md` | Что НЕ работает |
| `shared-learnings/TONE-FORMULAS.md` | Формулы тона |
| `shared-learnings/SOURCES.md` | Источники знаний |

---

## Порядок загрузки

```
1. РОУТИНГ  → CLAUDE.md определяет формат
2. СКИЛЛ    → skills/{формат}/SKILL.md + модули
3. БРЕНД    → brand/ (голос, аудитория, экспертиза)
4. МОДУЛЬ   → modules/{формат}/CLAUDE.md (настройки проекта)
5. ОБУЧЕНИЕ → learning/ (паттерны, анти-паттерны)
```

---

## Agents

| Агент | Роль | Путь |
|-------|------|------|
| AI Operator | Управление, решения | `agents/ai-operator.md` |
| Threads Writer | Посты для Threads | `agents/production/threads.md` |
| YouTube Producer | Сценарии для YouTube | `agents/production/youtube.md` |
| Vertical Content | Reels/Shorts | `agents/production/vertical-content.md` |
| Content Pipeline | Универсальный | `agents/production/content-pipeline.md` |
| Analyst | Метрики и инсайты | `agents/analytics/analyst.md` |
| Learning Agent | Обучение и паттерны | `agents/analytics/learning-agent.md` |
| Sales Critic | Продающая сила | `agents/analytics/critics/sales-critic.md` |
| Creative Critic | Креатив | `agents/analytics/critics/creative-critic.md` |
| Structure Critic | Структура | `agents/analytics/critics/structure-critic.md` |
| Selling Meanings | Продающие смыслы | `agents/strategy/selling-meanings.md` |
| Project Architect | Создание проектов | `agents/strategy/project-architect.md` |
| Offer Core | Ядро оффера | `agents/products/offer-core.md` |
| Customer Research | Кастдев | `agents/audience/customer-research.md` |

---

## Принципы

1. **Lazy loading** — загружаются только нужные модули (~70% экономия токенов)
2. **No duplication** — проекты наследуют от skills, не копируют
3. **Learning loop** — система учится из правок пользователя
4. **Progressive disclosure** — функции раскрываются по мере готовности пользователя

---

*Technical Reference — Content Factory v1.15*
