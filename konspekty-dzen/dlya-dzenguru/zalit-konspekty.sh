#!/usr/bin/env bash
# Заливка конспектов живых эфиров в LMS «Старт на Дзен» (course_id=2).
# Порядок по DZEN WAY: сначала stage → показ → ожидание подтверждения → прод.
# Контент, не код: деплой не нужен.
set -euo pipefail

FILE="konspekty-efirov.html"
SLUG="konspekty-efirov"
TITLE="Конспекты живых эфиров"
COURSE=2

cd "$(dirname "$0")"
[[ -f scripts/lms-content.py ]] || { echo "Запускать из корня dzen-guru (рядом должна быть scripts/lms-content.py)"; exit 1; }
[[ -f "$FILE" ]] || { echo "Нет файла $FILE — положите его рядом со скриптом"; exit 1; }

echo "── Модули курса $COURSE ──"
python3 scripts/lms-content.py modules --course "$COURSE"
echo
read -rp "В какой модуль класть? Введите id: " MODULE
[[ "$MODULE" =~ ^[0-9]+$ ]] || { echo "id должен быть числом"; exit 1; }

echo
echo "── STAGE ──"
python3 scripts/lms-content.py --stage create-lesson \
    --module "$MODULE" --slug "$SLUG" --title "$TITLE" --file "$FILE"

echo
echo "Урок создан на stage. Откройте и проверьте глазами:"
echo "  • оглавление кликается, переходы работают"
echo "  • таблицы и списки на месте, вёрстка не поехала"
echo "  • тёмная тема выглядит нормально"
echo
read -rp "Всё хорошо? Заливаем на прод? (введите ДА): " OK
[[ "$OK" == "ДА" ]] || { echo "Остановлено. На проде ничего не менялось."; exit 0; }

echo
echo "── ПРОД ──"
python3 scripts/lms-content.py create-lesson \
    --module "$MODULE" --slug "$SLUG" --title "$TITLE" --file "$FILE"

echo
echo "Готово. Урок «$TITLE» в модуле $MODULE."
echo "Проверьте на проде — и можно отправлять анонс."
