#!/bin/bash
# Audit: Freshness — запускается автоматически при "шарим"

echo "🔍 Audit: Freshness Check"
echo ""

ERRORS=0

# Проверка версий
echo "📦 Версии:"
WORKING_VERSION=$(cat /Users/user/claudecode/VERSION 2>/dev/null || echo "NOT FOUND")
CONSTRUCTOR_VERSION=$(cat /Users/user/claudecode/konstruktor-fabriki/content-factory-template/VERSION 2>/dev/null || echo "NOT FOUND")

if [ "$WORKING_VERSION" != "$CONSTRUCTOR_VERSION" ]; then
    echo "   ⚠️ Несовпадение версий!"
    echo "      Рабочая папка: $WORKING_VERSION"
    echo "      Конструктор: $CONSTRUCTOR_VERSION"
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ Версии синхронизированы: $WORKING_VERSION"
fi

echo ""

# Проверка цен в Max проекте
echo "💰 Проверка цен в projects/max:"
OLD_PRICES=$(grep -rn "790" /Users/user/claudecode/projects/max --include="*.md" 2>/dev/null | wc -l)
if [ $OLD_PRICES -gt 0 ]; then
    echo "   ⚠️ Найдено $OLD_PRICES упоминаний старой цены 790₽"
    grep -rn "790" /Users/user/claudecode/projects/max --include="*.md" 2>/dev/null | head -3
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ Цены актуальны (1490₽)"
fi

echo ""

# Проверка personal data в конструкторе
echo "🔒 Personal data в конструкторе:"
PERSONAL=$(grep -rE "Max Galson|DMG|DSG|Doctor Max|Angelina" /Users/user/claudecode/konstruktor-fabriki/content-factory-template/agents --include="*.md" 2>/dev/null | grep -v "Example\|Note:\|Generic" | wc -l)
if [ $PERSONAL -gt 0 ]; then
    echo "   ⚠️ Найдены личные данные в universal agents!"
    grep -rE "Max Galson|DMG|DSG|Doctor Max|Angelina" /Users/user/claudecode/konstruktor-fabriki/content-factory-template/agents --include="*.md" 2>/dev/null | grep -v "Example\|Note:\|Generic" | head -3
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ Конструктор обезличен"
fi

echo ""
echo "─────────────────────────────────────────"

if [ $ERRORS -gt 0 ]; then
    echo "❌ Найдено $ERRORS проблем — исправь перед синхронизацией!"
    exit 1
else
    echo "✅ Все проверки пройдены — готов к синхронизации"
    exit 0
fi
