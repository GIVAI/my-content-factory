#!/usr/bin/env python3
"""
Append blocks to a Notion page in batches.
Usage: python3 notion_batch_append.py <page_id> <blocks_json_file>
"""
import sys, json, os, subprocess

def append_blocks(page_id, blocks, batch_size=25):
    token = os.environ.get("NOTION_API_KEY", "")
    if not token:
        print("ERROR: NOTION_API_KEY not set"); sys.exit(1)

    total = len(blocks)
    batch_num = 0
    for i in range(0, total, batch_size):
        batch = blocks[i:i+batch_size]
        batch_num += 1
        data = json.dumps({"children": batch})
        result = subprocess.run([
            "curl", "-s", "-X", "PATCH",
            f"https://api.notion.com/v1/blocks/{page_id}/children",
            "-H", f"Authorization: Bearer {token}",
            "-H", "Notion-Version: 2022-06-28",
            "-H", "Content-Type: application/json",
            "-d", data
        ], capture_output=True, text=True)

        resp = json.loads(result.stdout)
        if "results" in resp:
            print(f"Batch {batch_num}: OK ({len(batch)} blocks)")
        else:
            print(f"Batch {batch_num}: ERROR - {resp.get('message', 'unknown')[:200]}")
            sys.exit(1)

    print(f"Done: {total} blocks in {batch_num} batches")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 notion_batch_append.py <page_id> <blocks.json>"); sys.exit(1)
    page_id = sys.argv[1]
    with open(sys.argv[2]) as f:
        blocks = json.load(f)
    append_blocks(page_id, blocks)
