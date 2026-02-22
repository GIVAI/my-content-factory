#!/usr/bin/env python3
"""
Create a SwipeFile page in Notion with all properties.
Usage: python3 create_page.py <title> <source_url> <source_type> <tags_csv> <use_for_csv> <attention> <how_to_use>
Prints page_id on success.
"""
import sys, json, os, subprocess

DB_ID = "SWIPEFILE_DB_ID"

def create_page(title, source_url, source_type, tags, use_for, attention, how_to_use):
    token = os.environ.get("NOTION_API_KEY", "")
    if not token:
        print("ERROR: NOTION_API_KEY not set"); sys.exit(1)

    props = {
        "Name": {"title": [{"text": {"content": title}}]},
        "Source": {"url": source_url} if source_url else {"url": None},
        "Source Type": {"select": {"name": source_type}} if source_type else {"select": None},
        "Tags": {"multi_select": [{"name": t.strip()} for t in tags.split(",") if t.strip()]},
        "Use For": {"multi_select": [{"name": u.strip()} for u in use_for.split(",") if u.strip()]},
        "rFqk": {"select": {"name": attention}} if attention else {"select": None},
        "How to use": {"rich_text": [{"text": {"content": how_to_use}}]} if how_to_use else {"rich_text": []}
    }

    data = json.dumps({"parent": {"database_id": DB_ID}, "properties": props})
    result = subprocess.run([
        "curl", "-s", "-X", "POST", "https://api.notion.com/v1/pages",
        "-H", f"Authorization: Bearer {token}",
        "-H", "Notion-Version: 2022-06-28",
        "-H", "Content-Type: application/json",
        "-d", data
    ], capture_output=True, text=True)

    resp = json.loads(result.stdout)
    if "id" in resp: print(resp["id"])
    else: print(f"ERROR: {resp.get('message', 'unknown')}"); sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 8:
        print("Usage: python3 create_page.py <title> <source_url> <source_type> <tags_csv> <use_for_csv> <attention> <how_to_use>")
        sys.exit(1)
    create_page(*sys.argv[1:8])
