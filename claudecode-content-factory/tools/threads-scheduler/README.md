# Threads Scheduler

Автопостинг в Threads через MoreLogin CDP. Берёт посты из Notion, планирует их по расписанию через UI Threads.

## Как работает

1. Читает посты со статусом "Approved" из Notion-базы
2. Открывает браузер MoreLogin через Chrome DevTools Protocol (CDP)
3. Для каждого поста: открывает compose → вводит текст → выбирает время → планирует
4. Обновляет статус в Notion на "Published"

## Требования

- **Node.js** 18+
- **MoreLogin** с запущенным профилем (CDP порт открыт)
- **Notion API ключ** с доступом к базе постов
- **npm-пакет `ws`** (WebSocket)

## Установка

```bash
cd tools/threads-scheduler
npm install ws
cp config.example.json config.json
# Заполни config.json своими данными
```

## Настройка config.json

| Секция | Поле | Описание |
|--------|------|----------|
| `notion.token` | Notion API ключ | `ntn_...` |
| `notion.databaseId` | ID базы с постами | Из URL Notion |
| `notion.statusProperty` | Название свойства статуса | По умолчанию `Status` |
| `notion.approvedValue` | Значение для готовых постов | По умолчанию `Approved` |
| `notion.publishedValue` | Значение после публикации | По умолчанию `Published` |
| `notion.titleProperties` | Массив имён свойств заголовка | `["Post", "Name"]` |
| `morelogin.cdpPort` | CDP порт профиля MoreLogin | По умолчанию `51830` |
| `schedule.times` | Массив времён постинга | `["08:23", "13:07", "20:11"]` |
| `schedule.timezone` | Таймзона | `Europe/Moscow` |
| `schedule.days` | На сколько дней вперёд планировать | `1` |
| `schedule.maxPosts` | Макс. постов за запуск | `10` |
| `delays.*` | Задержки (мс) между действиями | Подстройка под скорость |
| `logging.directory` | Папка логов | `./logs` |
| `logging.accountName` | Имя аккаунта для логов | Любое |

### Формат постов в Notion

- Посты хранятся как **code-блоки** внутри страницы
- Каждый code-блок = один пост в треде (первый — основной, остальные — реплаи)
- Опционально: свойство `Image URL` (url) для картинки

## Запуск

```bash
# Обычный запуск
node threads-scheduler.js

# С кастомным конфигом
node threads-scheduler.js --config /path/to/config.json

# Тестовый прогон (без реальной публикации)
node threads-scheduler.js --dry-run
```

## Вывод

Скрипт выводит JSON-результат в формате:

```
__RESULT__{"account":"my-account","success":5,"failed":0,"scheduled":[...],"errors":[]}
```

Логи пишутся в `./logs/threads-{account}-{date}.log`.

## Мультиаккаунт

Для каждого аккаунта создай отдельный `config.json` с нужным CDP-портом:

```bash
node threads-scheduler.js --config config-account1.json
node threads-scheduler.js --config config-account2.json
```
