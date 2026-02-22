# Настройка Конструктора Фабрики Контента

> **Пошаговая инструкция:** Установка → Проверка → Первый контент

---

## Шаг 1: Установка (уже сделано)

Если ты скачал эту папку, значит конструктор уже установлен:

✅ **Skills установлены** в `skills/`
- threads, youtube, reels, carousel, selling-meanings, storytelling, etc.

✅ **Agents установлены** в `agents/`
- Production, Analytics, Strategy, Personal

✅ **Routing настроен** в `CLAUDE.md`
- Автоматическая подгрузка skills при генерации

---

## Шаг 2: Проверка установки

Запусти тестовую команду:

```
threads 3
```

**Что должно произойти:**
1. Claude автоматически загружает `skills/threads/threads-copywriting.md`, `threads-hooks.md`
2. Генерирует 3 поста для Threads
3. Посты содержат хуки из skill (формулы, структура)

**Если не работает:**
- Проверь что папка `skills/threads/` существует
- Проверь что файлы `threads-copywriting.md`, `threads-hooks.md` в ней есть
- См. раздел "Troubleshooting" ниже

---

## Шаг 3: Создание своего проекта

### 3.1. Скопируй шаблон

```bash
cp -r projects/_template projects/myproject
```

Замени `myproject` на название своего проекта (латиницей, без пробелов).

### 3.2. Заполни brand/voice-style.md

Открой `projects/myproject/brand/voice-style.md` и заполни:

**Обязательные поля:**
- **ToV (Tone of Voice):** 4 трейта с процентами (40% + 30% + 20% + 10%)
  - Пример: "40% Практичный + 30% Лаконичный + 20% Дружелюбный + 10% Техничный"
- **Запрещённые паттерны:** Минимум 5 anti-patterns
  - Пример: "НЕ используем 'AI', только 'ИИ' или названия инструментов"
  - Пример: "НЕ стрелки → в тексте"

**Опционально:**
- Аудитория (кто читает, чего ищут)
- Начала постов (разрешённые/запрещённые зацепки)
- Концовки (варианты)

### 3.3. Добавь routing в главный CLAUDE.md

Открой главный `CLAUDE.md` (роутер в корне проекта) и добавь свой проект:

```markdown
| Trigger | Config |
|---------|--------|
| "myproject threads" | `projects/myproject/threads/CLAUDE.md` |
```

### 3.4. Тестирование

Запусти команду для своего проекта:

```
myproject threads 5
```

**Ожидаемый результат:**
- Загружаются skills (threads-copywriting, threads-hooks)
- Загружается `projects/myproject/brand/voice-style.md`
- Генерируется 5 постов с твоим голосом

---

## Шаг 4: Настройка Notion (опционально)

Если хочешь автопубликацию в Notion:

### 4.1. Создай базу в Notion

1. Открой Notion
2. Создай новую Database (Table)
3. Назови: "Threads {твой аккаунт}"

### 4.2. Добавь Properties

Скопируй структуру:

| Property | Type | Options |
|----------|------|---------|
| **Post** | title | — |
| **Topic** | text | — |
| **Format** | select | Facts, Story, Question, Tips, Hack |
| **Status** | select | Pending, Approved, Rejected, Published |
| **Score** | number | — |
| **Batch ID** | text | — |

### 4.3. Получи Database ID и Data Source ID

1. Открой базу в браузере
2. URL: `https://notion.so/{DATABASE_ID}?v={VIEW_ID}`
3. Скопируй DATABASE_ID
4. Запусти в Claude Code:
   ```
   notion-fetch {DATABASE_URL}
   ```
5. Найди в ответе: `collection://{DATA_SOURCE_ID}`

### 4.4. Обнови project CLAUDE.md

В `projects/myproject/threads/CLAUDE.md` добавь:

```markdown
## Notion Integration

| Параметр | Значение |
|----------|----------|
| Database ID | `{твой DATABASE_ID}` |
| Data Source ID | `{твой DATA_SOURCE_ID}` |
```

### 4.5. Тестирование с Notion

```
myproject threads 3
```

Проверь что 3 pages созданы в Notion базе.

---

## Шаг 5: Использование Skills

### Threads посты

```
threads 5
```
→ Загружает: threads skill + твой голос

### YouTube скрипт

```
youtube script про фабрику контента
```
→ Загружает: youtube skill + storytelling (если история)

### Продающий пост

```
threads продающий пост про мой продукт
```
→ Загружает: threads + selling-meanings (авто-детект)

### Карусель

```
carousel про автоматизацию контента
```
→ Загружает: carousel + nano-banana (для промптов изображений)

---

## Проверка связей (Debugging)

### Test 1: Skills загружаются?

Запусти:
```
threads 3
```

**Проверь в ответе Claude:**
- Упоминает ли "скользкая горка" (из threads-copywriting.md)?
- Использует ли формулы хуков (из threads-hooks.md)?

Если НЕТ → skills не загрузились.

**Решение:**
1. Проверь путь: `skills/threads/` (относительно корня проекта)
2. Проверь файлы в папке: `threads-copywriting.md`, `threads-hooks.md`
3. Проверь `routing-engine.md` (там должен быть threads в таблице)

### Test 2: Продающий контент авто-детектится?

Запусти:
```
threads продающий пост про мой продукт
```

**Проверь:**
- Использует ли психологические триггеры (из selling-meanings/psychology.md)?
- Применяет ли формулы (из selling-meanings/formulas.md)?

Если НЕТ → selling-meanings не подгрузился.

**Решение:**
1. Проверь путь: `skills/selling-meanings/` (относительно корня проекта)
2. Проверь файлы: `psychology.md`, `formulas.md`, `extraction.md`
3. Проверь в `routing-engine.md` auto-loading rules

### Test 3: Голос проекта применяется?

Запусти:
```
myproject threads 5
```

**Проверь:**
- Соответствует ли стиль твоему ToV из `brand/voice-style.md`?
- Избегает ли anti-patterns, которые ты указал?

Если НЕТ → voice-style.md не загрузился.

**Решение:**
1. Проверь путь: `projects/myproject/brand/voice-style.md`
2. Проверь routing в главном `CLAUDE.md` (добавлен ли твой проект?)

---

## Troubleshooting

### Проблема: Skills не загружаются

**Симптомы:**
- Контент без методологий
- Нет упоминаний "скользкая горка", хуков, триггеров
- Посты выглядят общими

**Решение:**
1. Убедись что `skills/` папка существует
2. Проверь что в ней есть подпапки: `threads/`, `youtube/`, `selling-meanings/`, etc.
3. Проверь `routing-engine.md` — там должны быть пути к skills
4. Перезапусти Claude Code

### Проблема: Голос проекта не применяется

**Симптомы:**
- Стиль не соответствует твоему ToV
- Anti-patterns проскальзывают

**Решение:**
1. Проверь `projects/{project}/brand/voice-style.md` заполнен?
2. Проверь routing в главном `CLAUDE.md` — добавлен ли твой проект?
3. Убедись что команда правильная: `{project} threads 5`

### Проблема: Selling-meanings не подключается

**Симптомы:**
- Продающий контент без триггеров
- Нет психологических формул

**Решение:**
1. Проверь ключевые слова: "продающий", "CTA", "оффер", "закреп"
2. Проверь `skills/selling-meanings/` существует?
3. Проверь `routing-engine.md` → Conditional Loading Rules

### Проблема: Notion не работает

**Симптомы:**
- Контент генерируется, но не попадает в Notion

**Решение:**
1. Проверь Database ID и Data Source ID правильные?
2. Проверь Notion Integration подключена к базе?
3. Попробуй ручной тест:
   ```
   notion-create-pages (с правильными параметрами)
   ```

---

## Дальнейшие шаги

### После первых постов

1. **Анализируй результаты:**
   - Что сработало? → Запиши в `learning/approved-patterns.md`
   - Что не сработало? → Запиши в `learning/anti-patterns.md`

2. **Обновляй голос:**
   - По мере работы дополняй `brand/voice-style.md`
   - Добавляй новые anti-patterns

3. **Расширяй форматы:**
   - Попробуй `youtube script`
   - Попробуй `carousel`
   - Попробуй `reels`

### Автоматизация

Когда workflow стабилизируется:

1. Настрой n8n для автопубликации
2. Добавь Telegram bot для ревью
3. Подключи analytics для learning loop

---

## Полезные команды

| Команда | Что делает |
|---------|------------|
| `threads 5` | 5 отдельных постов |
| `thread 5` | 1 ветка из 5 постов |
| `youtube script [тема]` | Сценарий для YouTube |
| `carousel [тема]` | Карусель для Instagram |
| `это сработало` | Записать паттерн (fast-track) |
| `это не сработало` | Записать антипаттерн (fast-track) |

---

## Поддержка

**Документация:**
- [routing-engine.md](routing-engine.md) — Полная логика routing
- [SKILLS-ROUTING.md](SKILLS-ROUTING.md) — Таблица skills
- [ALL-SKILLS.md](ALL-SKILLS.md) — Описание каждого skill

**Вопросы:**
- Поддержка: [@galsonproAIbot](https://t.me/galsonproAIbot?start=support)
- Канал: [@galsonproai](https://t.me/galsonproai)
- Сайт: [galson.pro](https://galson.pro)

---

*Фабрика Контента v2.0*  
*Макс Галсон • [galson.pro](https://galson.pro)*
