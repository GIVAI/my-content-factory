# UFC — Unified Field Context

**Цель:** Автоматически подтягивать релевантный контекст при генерации контента.

## Проблема

Агент забывает стиль, правила, learning при длинных сессиях или после /new.

## Решение

UFC собирает goal-specific контекст из:
- `brand/voice-style.md` проекта
- `learning/*.md` (последние файлы)
- Специфичные файлы под задачу

## Как использовать

### В CLAUDE.md или AGENTS.md

Добавь правило:
```
Перед генерацией контента:
1. Определить тип задачи (threads/reels/telegram/youtube)
2. Загрузить brand/voice-style.md
3. Загрузить learning/approved-patterns.md
4. Загрузить learning/anti-patterns.md
5. Только после этого генерировать
```

### Триггеры загрузки

| Задача | Что грузить |
|--------|-------------|
| threads | voice-style + threads-patterns + anti-patterns |
| reels | voice-style + reels-patterns + anti-patterns |
| youtube | voice-style + youtube-patterns + anti-patterns |
| telegram | voice-style + telegram-patterns + anti-patterns |
| любой пост | voice-style + approved-patterns + anti-patterns |

### Автоматическая версия (advanced)

Для продвинутых пользователей — Python скрипт:

```python
# context-builder.py
# Определяет проект и тип задачи из текста запроса
# Собирает релевантный контекст
# Выдаёт markdown для вставки в промпт
```

## Структура проекта для UFC

```
projects/{project}/
├── brand/
│   ├── voice-style.md     ← ОБЯЗАТЕЛЬНО
│   ├── audience.md
│   └── beliefs.md
├── learning/
│   ├── approved-patterns.md  ← ОБЯЗАТЕЛЬНО
│   ├── anti-patterns.md      ← ОБЯЗАТЕЛЬНО
│   └── skill-learning/
│       ├── threads/
│       ├── reels/
│       └── youtube/
```

## Принцип

> "Каждый раз когда агент генерирует контент, он должен сначала вспомнить:
> 1. Как звучит этот эксперт (voice-style)
> 2. Что работало раньше (approved-patterns)
> 3. Что делать НЕЛЬЗЯ (anti-patterns)"

## Преимущества

- Консистентный голос даже после /new
- Агент не забывает правила после 50 сообщений
- Меньше правок от клиента
- Накопленное обучение реально используется

---

*UFC v1.0 — Content Factory*
