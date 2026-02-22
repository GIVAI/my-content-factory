#!/bin/bash
# Quick Audit — ежедневная проверка при "закрыть сессию"
# Быстрая версия: только критичные проблемы (5-10 сек)

echo "⚡ Quick Audit (ежедневная проверка)"
echo ""

ERRORS=0

# 1. Проверка версий (быстро)
echo "📦 Версии:"
WORKING_VERSION=$(cat /Users/user/claudecode/VERSION 2>/dev/null || echo "NOT FOUND")
CONSTRUCTOR_VERSION=$(cat /Users/user/claudecode/konstruktor-fabriki/content-factory-template/VERSION 2>/dev/null || echo "NOT FOUND")

if [ "$WORKING_VERSION" != "$CONSTRUCTOR_VERSION" ]; then
    echo "   ⚠️ Версии не синхронизированы"
    echo "      Рабочая: $WORKING_VERSION | Конструктор: $CONSTRUCTOR_VERSION"
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ Синхронизированы: $WORKING_VERSION"
fi

echo ""

# 2. Новые skeleton agents (быстро)
echo "🎓 Skeleton agents:"
SKELETONS=$(grep -rn "Status: Skeleton" /Users/user/claudecode/agents --include="*.md" 2>/dev/null | wc -l)
if [ $SKELETONS -gt 0 ]; then
    echo "   ⚠️ Найдено $SKELETONS skeleton agents"
    grep -rn "Status: Skeleton" /Users/user/claudecode/agents --include="*.md" 2>/dev/null | head -3
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ Нет skeleton agents"
fi

echo ""

# 3. Критичные TODO в session-tracker (быстро)
echo "📋 Прерванные задачи:"
INTERRUPTED=$(sed -n '/## Прерванные задачи/,/## Ошибки/p' /Users/user/claudecode/session-tracker.md 2>/dev/null | grep -E "^\- " | wc -l)
if [ $INTERRUPTED -gt 0 ]; then
    echo "   ⚠️ $INTERRUPTED прерванных задач"
    sed -n '/## Прерванные задачи/,/## Ошибки/p' /Users/user/claudecode/session-tracker.md 2>/dev/null | grep -E "^\- " | head -2
else
    echo "   ✅ Нет прерванных задач"
fi

echo ""
echo "─────────────────────────────────────────"

if [ $ERRORS -gt 0 ]; then
    echo "⚠️ $ERRORS проблем — исправь завтра утром"
    echo "💡 Это не блокирует работу, просто напоминание"
    exit 0  # Не блокируем "закрыть сессию"
else
    echo "✅ Всё в порядке — хорошей ночи!"
    exit 0
fi
