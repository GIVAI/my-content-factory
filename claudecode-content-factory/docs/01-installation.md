# Установка Content Factory Skeleton

> Гайд для первого запуска скелета контент-фабрики

---

## Требования

1. **Claude Max** ($100/мес) — подписка на Claude с доступом к Claude Code
2. **Терминал** — командная строка (Terminal на Mac, PowerShell на Windows)
3. **Эта папка** — скелет контент-фабрики

---

## Шаг 1: Установка Claude Code

### Mac/Linux

Открой терминал и выполни:

```bash
npm install -g @anthropic-ai/claude-code
```

или через Homebrew:

```bash
brew install claude-code
```

### Windows

```bash
npm install -g @anthropic-ai/claude-code
```

### Проверка установки

```bash
claude --version
```

Если видишь версию — Claude Code установлен.

---

## Шаг 2: Авторизация

При первом запуске Claude Code попросит авторизоваться:

```bash
claude
```

Откроется браузер → войди в аккаунт Claude → разреши доступ.

---

## Шаг 3: Подключение скелета

### Вариант A: Скачал ZIP

1. Распакуй архив
2. Открой терминал в папке скелета:
   ```bash
   cd /путь/к/content-factory-template
   ```
3. Запусти Claude Code:
   ```bash
   claude
   ```

### Вариант B: Создал свою копию конструктора через GitHub

1. Открой https://github.com/maximgalson/content-factory
2. Нажми **"Use this template"** → **"Create a new repository"**
3. Склонируй СВОЮ копию:

```bash
git clone https://github.com/ТВОЙ_ЮЗЕРНЕЙМ/my-content-factory.git
cd my-content-factory
claude
```

---

## Шаг 4: Проверка

После запуска `claude` напиши:

```
интервью мини
```

Если Claude начал задавать вопросы — скелет подключен!

---

## Структура папки

```
content-factory-template/
├── CLAUDE.md              # Главный роутер (Claude читает это)
├── skills/        # 11 навыков
├── agents/                # Агенты
└── projects/_template/    # Шаблон твоего проекта
```

---

## Следующий шаг

Переходи к [02-first-post.md](02-first-post.md) — создаём первый пост за 30 минут.

---

## Проблемы?

- **Claude Code не устанавливается**: Проверь, что установлен Node.js (версия 18+)
- **Не авторизуется**: Убедись, что у тебя активная подписка Claude Max
- **Не видит файлы**: Запусти `claude` из папки со скелетом

Поддержка: [@galsonproAIbot](https://t.me/galsonproAIbot?start=support) | Канал: [@galsonproai](https://t.me/galsonproai)

---

*Фабрика Контента v2.0*  
*Макс Галсон • [galson.pro](https://galson.pro)*
