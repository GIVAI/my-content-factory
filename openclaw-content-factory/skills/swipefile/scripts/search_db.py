#!/usr/bin/env python3
"""
Search SwipeFile DB by name/author for cross-references.
Usage: python3 search_db.py <query>
Returns: page_id, name, url for each match.
"""
import sys, json, os, subprocess

DB_ID = "SWIPEFILE_DB_ID"

def search(query):
    token = os.environ.get("NOTION_API_KEY", "")
    data = json.dumps({"filter": {"property": "Name", "title": {"contains": query}}, "page_size": 10})
    result = subprocess.run([
        "curl", "-s", "-X", "POST",
        f"https://api.notion.com/v1/databases/{DB_ID}/query",
        "-H", f"Authorization: Bearer {token}",
        "-H", "Notion-Version: 2022-06-28",
        "-H", "Content-Type: application/json",
        "-d", data
    ], capture_output=True, text=True)

    resp = json.loads(result.stdout)
    for r in resp.get("results", []):
        t = r["properties"].get("Name", {}).get("title", [])
        name = t[0]["plain_text"] if t else "?"
        url = r.get("url", "")
        print(f"{r['id']}\t{name}\t{url}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 search_db.py <query>"); sys.exit(1)
    search(sys.argv[1])
