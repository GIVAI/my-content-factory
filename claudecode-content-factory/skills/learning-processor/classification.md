# Classification Rules

Правила определения тематики материала и маппинг на существующие ресурсы.

## Маппинг тем → Skills

| Ключевые слова в материале | Skill | Target файлы |
|---------------------------|-------|--------------|
| youtube, видео, хуки, retention, сценарий, скрипт, миниатюра, CTR, SEO видео | `youtube` | youtube-hooks.md, youtube-structure.md, youtube-retention.md |
| threads, посты, соцсети, текстовый контент, вовлечение | `threads` | threads-hooks.md, threads-strategy.md, threads-copywriting.md |
| reels, shorts, tiktok, вертикальное видео, короткий контент | `reels` | reels-velizhanin-guide.md |
| карусель, слайды, instagram carousel, визуальный контент | `carousel` | carousel-structure.md, carousel-types.md |
| запуск, launch, PLF, прогрев, последовательность, воронка запуска | `launch` | sequences.md, plc-structure.md, triggers.md |
| смысл, оффер, позиционирование, ценность, триггер, психология продаж | `selling-meanings` | psychology.md, extraction.md, formulas.md |
| промпт, инструкция для AI, system prompt, agent prompt | `prompt-engineer` | techniques.md, templates.md |
| картинка, изображение, AI image, генерация изображений | `nano-banana` | nano-banana-realism.md |

## Маппинг тем → Projects

Проект определяется автоматически:
1. По открытой папке проекта
2. По явным упоминаниям имени эксперта из `brand/profile.md`
3. Если не определяется — спросить пользователя

**Target:** `projects/{project}/learning/`

## Типы извлекаемого контента

| Тип | Признаки в тексте | Куда пишем |
|-----|-------------------|------------|
| **TECHNIQUE** | "как сделать", пошаговый процесс, "метод", "способ" | skill/references/ |
| **FORMULA** | аббревиатура, A→B→C структура, "формула", "фреймворк" | skill/references/ |
| **PATTERN** | "работает потому что", "даёт результат", с метриками | project/learning/patterns.md |
| **WARNING** | "не работает", "ошибка", "избегать", негативный опыт | project/learning/anti-patterns.md |
| **MEANING** | ценностное предложение, боль→решение, эмоция | project/learning/meanings.md |
| **QUOTE** | прямая речь эксперта, ценная формулировка | зависит от контекста |

## Алгоритм определения

```
1. Сканировать первые 1000 слов
2. Найти ключевые слова из таблиц выше
3. Определить primary skill (max matches)
4. Определить project (если есть явные признаки)
5. Если ничего не найдено → спросить пользователя
```

## Примеры классификации

**Пример 1:**
> "Сегодня разберём как делать хуки для YouTube видео. Первые 5 секунд — самые важные..."

- Keywords: youtube, хуки, видео
- **Skill:** youtube
- **Target:** youtube-hooks.md

**Пример 2:**
> "В запуске важна последовательность. PLC — pre-launch content — готовит аудиторию..."

- Keywords: запуск, PLC, последовательность
- **Skill:** launch
- **Target:** plc-structure.md

**Пример 3:**
> "В своих видео [Эксперт] использует особый стиль подачи..."

- Keywords: имя эксперта (из brand/profile.md)
- **Project:** определяется автоматически
- **Target:** projects/{project}/learning/ или projects/{project}/brand/

## Новые темы (не найден skill)

Если тема не маппится ни на один skill:

1. Показать пользователю найденные ключевые слова
2. Предложить варианты:
   - Создать новый skill
   - Добавить как reference к существующему
   - Записать в общий learning
3. Дождаться подтверждения
