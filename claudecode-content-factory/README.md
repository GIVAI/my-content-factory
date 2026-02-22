# Content Factory

AI-система для создания контента с Claude Code. Пишет посты, сценарии и карусели в твоём голосе.

---

## Быстрый старт (5 минут)

### 1. Установи Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Создай свою копию конструктора

1. Открой конструктор: https://github.com/maximgalson/content-factory
2. Нажми зелёную кнопку **"Use this template"** → **"Create a new repository"**
3. Назови как хочешь (например `my-content-factory`), нажми **Create**
4. Склонируй СВОЮ копию:

```bash
git clone https://github.com/ТВОЙ_ЮЗЕРНЕЙМ/my-content-factory.git
cd my-content-factory
```

### 3. Запусти Claude

```bash
claude
```

### 4. Напиши `начать` или `/setup`

Claude проведёт интервью за 10 минут и сгенерирует первые посты.

---

## Что получаешь

### 15 Skills (методы создания контента)

| Skill | Для чего |
|-------|----------|
| **threads** | Посты для Threads/X |
| **youtube** | Сценарии для YouTube |
| **reels** | Рилсы и шорты |
| **carousel** | Карусели для Instagram |
| **selling-meanings** | Продающие смыслы |
| **storytelling** | Истории и кейсы |
| **launch** | Запуски продуктов (PLF) |
| **nano-banana** | AI-генерация картинок |
| **offer-core** | Формулировка ядра оффера |
| **customer-research** | Исследование аудитории |
| **prompt-engineer** | Создание промптов |

**Advanced Skills:** [agent-architect и skill-creator](docs/advanced-skills-showcase.md) — создание своих агентов и skills

### Голос под тебя

Claude учится твоему стилю:
- Как ты говоришь (на ты/Вы, формально/неформально)
- Какие темы поднимаешь
- Какие слова используешь и не используешь

### Система обучения

```
это сработало     → сохраняет успешный паттерн
это не сработало  → запоминает что не работает
```

Чем больше используешь — тем точнее контент.

---

## Команды

### Контент

```
/threads 5              → 5 постов для Threads
/youtube script [тема]  → Сценарий для YouTube
/carousel [тема]        → Карусель для Instagram
/reels [тема]           → Рилс-идея
```

### Настройка

| Слово | Слэш | Что делает |
|-------|------|------------|
| `начать` | `/setup` | Первая настройка (10 мин) |
| `интервью` | `/interview` | Полное интервью (30 мин) |
| `интервью мини` | `/interview mini` | Быстрое интервью (10 мин) |

### Анализ

```
/critics         → Оценка от 3 критиков
/insights        → Что сработало, что нет
```

---

## Структура проекта

```
content-factory/
├── CLAUDE.md                    # Главный файл (инструкции для Claude)
│
├── skills/              # 13 skills (методы)
│   ├── threads/
│   ├── youtube/
│   ├── carousel/
│   └── ...
│
├── agents/                      # Агенты (специалисты)
│   ├── production/             # Создание контента
│   ├── analytics/              # Анализ и критика
│   └── strategy/               # Стратегия
│
├── projects/
│   ├── _template/              # Шаблон для твоего проекта
│   │   ├── brand/              # Твой голос
│   │   ├── learning/           # Что работает/не работает
│   │   └── onboarding/         # Интервью
│   │
│   └── example-psychologist/   # Пример готового проекта
│
└── docs/                        # Документация
    ├── 00-complete-setup-guide.md
    ├── 01-installation.md
    ├── 02-first-post.md
    └── 03-integrations.md
```

---

## Требования

- **Claude Max** — подписка $100/месяц
- **Claude Code** — установка через npm
- **Node.js 18+** — для Claude Code

---

## Документация

### Для людей (простым языком)

| Документ | Описание |
|----------|----------|
| [Что такое скиллы?](docs/skills-guide.md) | 12 методик создания контента |
| [Что такое агенты?](docs/agents-guide.md) | Твоя команда специалистов |

### Техническое

| Документ | Описание |
|----------|----------|
| [Полный гайд](docs/00-complete-setup-guide.md) | Всё от А до Я |
| [Установка](docs/01-installation.md) | Claude Code + настройка |
| [Первый пост](docs/02-first-post.md) | От нуля до поста за 30 мин |
| [Интеграции](docs/03-integrations.md) | Notion, n8n, автоматизация |

---

## FAQ

**Q: Нужен ли Claude Max?**
A: Да, Claude Code требует подписку Claude Max ($100/месяц).

**Q: Посты не похожи на меня?**
A: Скажи `интервью` заново или добавь примеры в `learning/approved-patterns.md`

**Q: Как добавить свой формат?**
A: Все форматы уже включены. Для нового — используй `/skill-creator`

**Q: Работает на русском?**
A: Да, система полностью работает на русском языке.

---

## Полезные материалы

Дополнительные скиллы и инструменты — [RESOURCES.md](RESOURCES.md)

| Материал | Что даёт |
|----------|----------|
| [Nano Banana Промпты](RESOURCES.md#-nano-banana-pro--библиотека-промптов-для-генерации-картинок) | 6000+ промптов для генерации картинок |

---

## Поддержка

- Поддержка: [@galsonproAIbot](https://t.me/galsonproAIbot?start=support)
- Канал: [@galsonproai](https://t.me/galsonproai)
- Issues: [GitHub Issues](https://github.com/maximgalson/content-factory/issues)

---

## Лицензия

Проприетарная лицензия. Конструктор предоставляется для личного использования. Распространение, копирование и публикация запрещены без разрешения автора.

---

*Фабрика Контента v2.0*  
*Макс Галсон • [galson.pro](https://galson.pro)*
