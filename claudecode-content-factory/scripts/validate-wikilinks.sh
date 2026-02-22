#!/bin/bash
# Finds broken wikilinks in the project

echo "Validating wikilinks..."
echo ""

cd /Users/user/claudecode

broken_count=0

grep -r "\[\[.*\]\]" --include="*.md" . | \
  sed 's/.*\[\[\([^]]*\)\]\].*/\1/' | \
  sort -u | \
  while read link; do
    # Extract filename (without alias)
    file="${link%%|*}"

    # Try different extensions and paths
    found=false

    # Try as-is
    if [ -f "$file" ] || [ -f "$file.md" ]; then
      found=true
    fi

    # Try with .md extension if not present
    if [ ! -f "$file" ] && [[ ! "$file" =~ \.md$ ]]; then
      if [ -f "$file.md" ]; then
        found=true
      fi
    fi

    # Try relative paths
    if [ ! -f "$file" ] && [ ! -f "$file.md" ]; then
      # Search for the file
      found_path=$(find . -name "$(basename $file).md" 2>/dev/null | head -1)
      if [ ! -z "$found_path" ]; then
        found=true
      fi
    fi

    if [ "$found" = false ]; then
      echo "⚠️  Broken wikilink: [[$link]]"
      broken_count=$((broken_count + 1))
    fi
  done

if [ $broken_count -eq 0 ]; then
  echo "✅ All wikilinks are valid!"
else
  echo ""
  echo "Found $broken_count broken wikilinks"
fi
