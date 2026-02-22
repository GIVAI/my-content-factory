#!/bin/bash
# Parser недоделок — запускается автоматически при "начать сессию"

echo "📋 Недоделки в системе"
echo ""

# TODO markers
echo "🔴 TODO items:"
grep -rn "TODO:" /Users/user/claudecode --include="*.md" 2>/dev/null | grep -v "node_modules\|archive\|.git" | head -5
if [ $? -ne 0 ]; then
    echo "   ✅ Нет TODO markers"
fi

echo ""

# Skeleton agents
echo "🎓 Skeleton agents (требуют наполнения):"
grep -rn "Status: Skeleton" /Users/user/claudecode/agents --include="*.md" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "   ✅ Нет skeleton agents"
fi

echo ""

# Прерванные задачи из session-tracker
echo "⏸️ Прерванные задачи:"
sed -n '/## Прерванные задачи/,/## Ошибки/p' /Users/user/claudecode/session-tracker.md 2>/dev/null | grep -E "^\- " | head -5
if [ $? -ne 0 ]; then
    echo "   ✅ Нет прерванных задач"
fi

echo ""
echo "─────────────────────────────────────────"
echo "💡 Это автоматический парсинг при 'начать сессию'"
