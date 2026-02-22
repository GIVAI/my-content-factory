#!/bin/bash
# Обновление конструктора — копирует ТОЛЬКО скиллы, не трогает твои данные
# Использование: ./update.sh путь-к-новой-версии

set -e

NEW_VERSION="${1:?Укажи путь к скачанной новой версии: ./update.sh ~/Downloads/content-factory-main}"

echo "🏭 Обновление конструктора"
echo ""

# Определяем что обновляем — Claude Code или OpenClaw
if [ -f "CLAUDE.md" ]; then
  SKILLS_SRC="$NEW_VERSION/claudecode-content-factory/skills"
  TYPE="Claude Code"
elif [ -d "$HOME/.openclaw/workspace/skills" ]; then
  SKILLS_SRC="$NEW_VERSION/openclaw-content-factory/skills"
  TYPE="OpenClaw"
else
  echo "❌ Не могу определить тип установки. Запусти из папки конструктора."
  exit 1
fi

if [ ! -d "$SKILLS_SRC" ]; then
  echo "❌ Не найдена папка скиллов в $SKILLS_SRC"
  echo "   Проверь что скачал правильную версию."
  exit 1
fi

echo "📦 Тип: $TYPE"
echo "📁 Новые скиллы: $SKILLS_SRC"
echo ""

# Бэкап
BACKUP_DIR="backup-$(date +%Y%m%d-%H%M%S)"
echo "💾 Создаю бэкап скиллов → $BACKUP_DIR/"

if [ "$TYPE" = "Claude Code" ]; then
  mkdir -p "$BACKUP_DIR"
  cp -r skills/ "$BACKUP_DIR/skills-old" 2>/dev/null || true
  
  echo "📥 Копирую новые скиллы..."
  cp -r "$SKILLS_SRC"/* skills/
  
  echo ""
  echo "✅ Скиллы обновлены!"
  echo ""
  echo "⚠️  НЕ тронуто (твои данные):"
  echo "   • brand/     — твой голос и аудитория"
  echo "   • learning/  — что сработало / не сработало"  
  echo "   • memory/    — дневные логи"
  echo "   • MEMORY.md  — долгосрочная память"
  echo "   • projects/  — твои проекты"
else
  mkdir -p "$BACKUP_DIR"
  cp -r ~/.openclaw/workspace/skills/ "$BACKUP_DIR/skills-old" 2>/dev/null || true
  
  echo "📥 Копирую новые скиллы..."
  cp -r "$SKILLS_SRC"/* ~/.openclaw/workspace/skills/
  
  echo "🔄 Перезапуск OpenClaw..."
  openclaw gateway restart 2>/dev/null || echo "⚠️  Перезапусти вручную: openclaw gateway restart"
  
  echo ""
  echo "✅ Скиллы обновлены!"
  echo ""
  echo "⚠️  НЕ тронуто (твои данные):"
  echo "   • brand/     — твой голос и аудитория"
  echo "   • learning/  — что сработало / не сработало"
  echo "   • memory/    — дневные логи"
  echo "   • MEMORY.md  — долгосрочная память"
fi

echo ""
echo "💾 Бэкап старых скиллов: $BACKUP_DIR/"
echo ""
echo "🎉 Готово! Конструктор обновлён."
