# The Complete Guide to Building Skills for Claude (Anthropic, Jan 2026)

Source: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

## Структура скилла

```
skill-name/           ← kebab-case обязательно
├── SKILL.md          ← обязательно (точное имя, case-sensitive)
├── scripts/          ← опционально (Python, Bash)
├── references/       ← документация, загружается по запросу
└── assets/           ← шаблоны, иконки, используемые в output
```

## Критические правила

- SKILL.md — точное имя (не SKILL.MD, не skill.md)
- Папка в kebab-case: `notion-project-setup` ✅, `Notion Project Setup` ❌
- НЕ включать README.md внутри скилла
- YAML frontmatter обязательно с `---` разделителями
- `name`: kebab-case, без пробелов и заглавных
- `description`: ЧТО делает + КОГДА использовать (триггеры!)
- Без XML тегов `< >` в frontmatter (безопасность)
- SKILL.md до 5000 слов, детали → в references/

## 3 уровня загрузки (Progressive Disclosure)

1. **YAML frontmatter** → всегда в системном промпте (решает когда загружать)
2. **SKILL.md body** → загружается когда скилл активирован
3. **references/** → подгружается по необходимости (экономия токенов)

## YAML Frontmatter

### Обязательные поля
```yaml
---
name: skill-name-in-kebab-case
description: What it does and when to use it. Include specific trigger phrases.
---
```

### Опциональные поля
```yaml
license: MIT
allowed-tools: "Bash(python:*) Bash(npm:*) WebFetch"
metadata:
  author: Company Name
  version: 1.0.0
  mcp-server: server-name
  category: productivity
  tags: [project-management, automation]
```

### Description — самая важная часть
Структура: `[Что делает] + [Когда использовать] + [Ключевые возможности]`

**Хорошо:**
```
description: Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", "component documentation", or "design-to-code handoff".
```

**Плохо:**
```
description: Helps with projects.
```

## 3 категории скиллов

### Category 1: Document & Asset Creation
- Создание контента, документов, дизайнов
- Встроенные стайлгайды и шаблоны
- Чеклисты качества
- Не требует внешних инструментов

### Category 2: Workflow Automation
- Многошаговые процессы
- Шаблоны для типовых структур
- Ревью и улучшение на каждом шаге
- Итеративные циклы

### Category 3: MCP Enhancement
- Надстройка над MCP серверами
- Координация нескольких MCP-вызовов
- Экспертные знания домена
- Обработка ошибок MCP

## 5 паттернов построения

### Pattern 1: Sequential Workflow
Многошаговые процессы в определённом порядке.
- Явный порядок шагов
- Зависимости между шагами
- Валидация на каждом этапе
- Инструкции отката при ошибках

### Pattern 2: Multi-MCP Coordination
Несколько сервисов в одном workflow.
- Чёткое разделение фаз
- Передача данных между MCP
- Валидация перед переходом к следующей фазе

### Pattern 3: Iterative Refinement
Качество улучшается с итерациями.
- Явные критерии качества
- Цикл улучшений
- Скрипты валидации
- Знать когда остановиться

### Pattern 4: Context-Aware Tool Selection
Разные инструменты в зависимости от контекста.
- Чёткие критерии выбора
- Fallback опции
- Прозрачность решений

### Pattern 5: Domain-Specific Intelligence
Специализированные знания поверх инструментов.
- Экспертиза домена встроена в логику
- Compliance перед действием
- Полная документация
- Чёткое управление

## Тестирование

### 3 типа тестов
1. **Triggering** — скилл загружается когда нужно (и НЕ загружается когда не нужно)
2. **Functional** — правильные output'ы, API работает, edge cases
3. **Performance** — сравнение с/без скилла (токены, сообщения, ошибки)

### Метрики успеха
- Скилл триггерится на 90% релевантных запросов
- Завершает workflow за X вызовов инструментов
- 0 ошибок API за workflow
- Пользователь не перенаправляет и не уточняет

## Troubleshooting

### Скилл не триггерится
- Description слишком общий → добавить конкретные фразы
- Нет триггерных слов → добавить "Use when..."
- Отладка: спросить "When would you use skill X?" — Claude процитирует description

### Скилл триггерится слишком часто
- Добавить negative triggers: "Do NOT use for..."
- Быть конкретнее в description
- Уточнить scope

### Инструкции не выполняются
- Инструкции слишком длинные → сократить, bullet points
- Критичное закопано → вынести наверх, ## CRITICAL
- Неоднозначный язык → конкретные проверки вместо "validate properly"
- Для критичных валидаций → скрипт вместо текстовых инструкций

### Большой контекст
- SKILL.md под 5000 слов
- Детали в references/
- Не более 20-50 скиллов одновременно

## Чеклист валидации скилла

### До начала
- [ ] 2-3 конкретных use case
- [ ] Инструменты определены (built-in или MCP)
- [ ] Структура папок спланирована

### Во время разработки
- [ ] Папка в kebab-case
- [ ] SKILL.md существует (точное написание)
- [ ] YAML frontmatter с `---`
- [ ] name: kebab-case
- [ ] description: ЧТО + КОГДА
- [ ] Без `< >` тегов
- [ ] Инструкции ясные и actionable
- [ ] Обработка ошибок
- [ ] Примеры есть
- [ ] References подключены

### После загрузки
- [ ] Тест: триггерится на очевидных задачах
- [ ] Тест: триггерится на перефразированных запросах
- [ ] Тест: НЕ триггерится на нерелевантном
- [ ] Функциональные тесты пройдены
- [ ] Мониторинг under/over-triggering
