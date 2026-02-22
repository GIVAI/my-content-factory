#!/bin/bash
# Adds Related section to agent files without it

echo "Adding Related sections to agent files..."

find /Users/user/claudecode/agents/ -name "*.md" -not -name "_*" -not -name "README.md" | while read file; do
  if ! grep -q "## Related" "$file"; then
    echo "Adding Related to: $file"
    echo "" >> "$file"
    echo "## Related" >> "$file"
    echo "- [[_index|Agents Index]] — Full agent list" >> "$file"
    echo "- [[../CLAUDE|Main Router]]" >> "$file"
  else
    echo "Skipping (already has Related): $file"
  fi
done

echo "Done!"
