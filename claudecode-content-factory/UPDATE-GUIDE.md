# Гайд по обновлениям

Как получать обновления skills и agents без потери твоих данных.

---

## Золотое правило

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ✅ ОБНОВЛЯТЬ:              ❌ НЕ ТРОГАТЬ:                     │
│   ├── skills/*       └── projects/{твой-проект}/*      │
│   ├── agents/*                   ├── brand/                    │
│   ├── docs/*                     ├── strategy/                 │
│   ├── projects/_template/*       ├── content/                  │
│   ├── README.md                  ├── learning/                 │
│   ├── CLAUDE.md                  ├── references/               │
│   ├── UPDATE-GUIDE.md            ├── sessions/                 │
│   ├── CHANGELOG.md               └── CLAUDE.md                 │
│   └── structure-readme.md                                      │
│                                                                 │
│   _template = шаблон             {твой-проект} = ТВОИ ДАННЫЕ   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Простое правило:** `projects/_template/` можно обновлять (это шаблон). `projects/{любое-другое-имя}/` — твои данные, никогда не трогай при обновлении.

---

## Что обновляется

| Компонент | Частота | Пример |
|-----------|---------|--------|
| **Skills** | Еженедельно | Новые техники, хуки, формулы |
| **Agents** | Ежемесячно | Новые агенты, улучшения пайплайна |
| **Architecture** | Редко | Фундаментальные изменения |

---

## Два способа обновления

### Способ обновления: ZIP

**Обновление (пошагово):**

1. **Скачай** свежую версию: https://github.com/maximgalson/content-factory → Code → Download ZIP
2. **Распакуй** в отдельную папку (например, `content-factory-new`)
3. **Скопируй** только системные файлы:

```
ИЗ content-factory-new/     →     В content-factory/
├── skills/*              ├── skills/       ✅ ЗАМЕНИТЬ
├── agents/*                      ├── agents/               ✅ ЗАМЕНИТЬ
├── docs/*                        ├── docs/                 ✅ ЗАМЕНИТЬ
├── projects/_template/*          ├── projects/_template/   ✅ ЗАМЕНИТЬ
├── README.md                     ├── README.md             ✅ ЗАМЕНИТЬ
├── CLAUDE.md                     ├── CLAUDE.md             ✅ ЗАМЕНИТЬ
├── UPDATE-GUIDE.md               ├── UPDATE-GUIDE.md       ✅ ЗАМЕНИТЬ
└── CHANGELOG.md                  └── CHANGELOG.md          ✅ ЗАМЕНИТЬ

                                  └── projects/my-project/  ❌ НЕ ТРОГАТЬ!
```

4. **Удали** папку `content-factory-new`

**Команды для копирования (Mac/Linux):**
```bash
# Замена системных файлов
cp -r content-factory-new/skills/* content-factory/skills/
cp -r content-factory-new/agents/* content-factory/agents/
cp -r content-factory-new/docs/* content-factory/docs/
cp -r content-factory-new/projects/_template/* content-factory/projects/_template/
cp content-factory-new/README.md content-factory/
cp content-factory-new/CLAUDE.md content-factory/
cp content-factory-new/UPDATE-GUIDE.md content-factory/
cp content-factory-new/CHANGELOG.md content-factory/
```

---

## Версионирование

Текущая версия конструктора: см. файл `VERSION`

Каждый skill имеет версию в frontmatter:

```yaml
---
name: youtube
version: 1.0.0
updated: 2026-01-17
---
```

Полная история изменений: [CHANGELOG.md](CHANGELOG.md)

---

## Если изменил skill под себя

1. **Сохрани** свою версию:
   ```bash
   cp -r skills/youtube skills/youtube-backup
   ```

2. **Обнови** из источника

3. **Перенеси** свои изменения вручную

---

## Анонсы обновлений

Новые версии анонсируются в:
закрытом канале Фабрика Контента ()
- Telegram-канал [@galsonproai](https://t.me/galsonproai)
- Coworking эфиры (разбор новых features)

---

## Поддержка

Сайт: [galson.pro](https://galson.pro) | Поддержка: [@galsonproAIbot](https://t.me/galsonproAIbot?start=support) | Канал: [@galsonproai](https://t.me/galsonproai)

---

*Фабрика Контента v2.0*  
*Макс Галсон • [galson.pro](https://galson.pro)*
