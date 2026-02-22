# HeyGen Motion Prompts

Промпты для оживления фото (Photo Avatar → Custom prompt).

---

## Рекомендуемый движок

**Kling** — лучший выбор для говорящей головы.

---

## Проблема склейки

HeyGen генерирует максимум **10 секунд**. Для 60 сек нужно склеивать 6 фрагментов.

**Решение:** Промпт возвращает в нейтральную позу в начале и конце.

---

## Промпты

### 1. Говорящая голова (эксперт)

```
Expert delivers calm, authoritative speech to camera. Minimal head movement - only subtle micro-expressions. Eyes maintain steady contact with slight natural blinks every 3-4 seconds.

Movement pattern: Start and end in neutral position. Small eyebrow raises on key points. Gentle jaw movement simulating speech rhythm with natural pauses. Shoulders completely still.

Critical: No nodding, no head tilts, no swaying. Face returns to exact neutral expression at frame end for seamless loop continuity.
```

### 2. С предметом в руках

```
Expert speaks calmly to camera. Hands remain completely frozen on object - absolutely no hand or arm movement.

Face only: gentle blinking every 3-4 seconds, subtle lip movement for speech, minimal eyebrow micro-expressions.

Head position stable - no nodding, no tilting, no turning. Shoulders and torso locked still.

Start and end in identical neutral expression for seamless loop transition.
```

### 3. Усиление (если дёргается)

Добавить в начало:
```
CRITICAL: Zero movement below neck. Only facial animation allowed.
```

---

## Склейка

| Длина | Crossfade |
|-------|-----------|
| 30 сек | 0.3 сек |
| 60 сек | 0.3-0.5 сек |

---

*HeyGen Motion v1.0*
