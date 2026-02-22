# Психотерапевт Анна

> Пример готового проекта для Content Factory

---

## Профиль

**Кто:** Анна Иванова, врач-психотерапевт
**Ниша:** Тревожные расстройства, панические атаки
**Продукт:** Онлайн-консультации

---

## Быстрые команды

| Команда | Что делает |
|---------|------------|
| `/threads 5` | 5 постов для Threads |
| `/youtube script [тема]` | Сценарий для YouTube |
| `/critics` | Оценка от 3 критиков |

---

## Обязательно загружать

```
brand/profile.md      — кто я
brand/voice-style.md  — как пишу
brand/audience.md     — кто читает
```

---

## Skills — Автоматическая загрузка

### Триггеры и скиллы

| Команда / Триггер | Скиллы из `skills/` | Когда |
|-------|------|-------|
| `threads`, `пост` | `threads/SKILL.md` + `threads-copywriting.md` + `threads-hooks.md` | Каждый пост |
| `youtube script`, `сценарий` | `youtube/SKILL.md` + `youtube-structure.md` + `youtube-hooks.md` | Каждый сценарий |
| `carousel`, `карусель` | `carousel/SKILL.md` + `carousel-structure.md` + `carousel-types.md` | Каждая карусель |
| `reels`, `рилс` | `reels/SKILL.md` + `reels-methodology.md` | Каждый рилс |
| `telegram`, `тг пост` | `telegram/SKILL.md` + `telegram-copywriting.md` + `telegram-hooks.md` | Каждый пост ТГ |
| Продающий контент | `selling-meanings/SKILL.md` + нужный модуль | CTA, офферы, воронки |
| Истории, кейсы | `storytelling/SKILL.md` + `slippery-slide.md` | Сторителлинг |
| Картинки, обложки | `nano-banana/SKILL.md` + нужный модуль | Визуалы |
| AI-аватар видео | `heygen/SKILL.md` + `heygen-rules.md` | HeyGen видео |

### Порядок загрузки

```
1. СКИЛЛ     → skills/{формат}/SKILL.md
2. БРЕНД     → brand/ (профиль, голос, аудитория)
3. ДОП.СКИЛЛ → selling-meanings / storytelling (по типу)
4. ОБУЧЕНИЕ  → learning/approved-patterns.md (что работает)
```

### Пример для психотерапевта Анны

```
Анна: "threads 5 постов про панические атаки"

Claude загружает:
1. threads/SKILL.md + threads-copywriting.md + threads-hooks.md
2. brand/profile.md (Анна, психотерапевт)
3. brand/voice-style.md (эмпатичный, профессиональный)
4. storytelling/SKILL.md (истории пациентов — анонимно)
5. learning/approved-patterns.md
→ Генерирует 5 постов в голосе Анны
```

---

*Example Project — Content Factory v2.0*
