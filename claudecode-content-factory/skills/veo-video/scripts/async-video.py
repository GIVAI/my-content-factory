#!/usr/bin/env python3
"""
Veo 3.1 Async Video Generator — LaoZhang.ai /v1/videos API

Рекомендуемый метод для продакшена:
  - НЕ списывает деньги при ошибке
  - Стабильнее (не зависит от long connection)
  - Задачи живут 24 часа

Usage:
  # Text-to-Video
  python3 async-video.py --prompt "A cat playing" --model veo-3.1-fast --output cat.mp4

  # Image-to-Video (single frame — animate)
  python3 async-video.py --prompt "Bring to life" --model veo-3.1-fast-fl \
    --start-frame image.jpg --output animated.mp4

  # First/Last Frame (timelapse transition)
  python3 async-video.py --prompt "Smooth timelapse transition" --model veo-3.1-fast-fl \
    --start-frame start.jpg --end-frame end.jpg --output transition.mp4

  # Batch: multiple transitions for a timelapse project
  python3 async-video.py --batch batch.json --output-dir ./videos/

Environment:
  VEO_API_KEY — API key for Veo 3.1 (see TOOLS.md)
"""

import argparse
import json
import os
import sys
import time
import requests

API_KEY = os.environ.get("VEO_API_KEY")
BASE_URL = "https://api.laozhang.ai/v1"
DEFAULT_MODEL = "veo-3.1-fast-fl"
POLL_INTERVAL = 5  # seconds
TIMEOUT = 600  # 10 minutes


def create_task(prompt: str, model: str, image_paths: list[str] | None = None) -> dict:
    """Step 1: Create a video generation task."""
    url = f"{BASE_URL}/videos"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    if image_paths:
        # Image-to-Video: multipart/form-data
        files = []
        for path in image_paths:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Image not found: {path}")
            files.append(
                ("input_reference", (os.path.basename(path), open(path, "rb"), "image/jpeg"))
            )
        data = {"model": model, "prompt": prompt}
        response = requests.post(url, headers=headers, files=files, data=data)
        # Close file handles
        for _, (_, f, _) in files:
            f.close()
    else:
        # Text-to-Video: JSON
        headers["Content-Type"] = "application/json"
        data = {"model": model, "prompt": prompt}
        response = requests.post(url, headers=headers, json=data)

    response.raise_for_status()
    return response.json()


def poll_status(video_id: str) -> dict:
    """Step 2: Poll task status until completed or failed."""
    url = f"{BASE_URL}/videos/{video_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        if elapsed > TIMEOUT:
            raise TimeoutError(f"Video generation timed out after {TIMEOUT}s")

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        task = response.json()

        status = task["status"]
        elapsed_str = f"{int(elapsed)}s"
        print(f"  [{elapsed_str}] Status: {status}")

        if status == "completed":
            return task
        elif status == "failed":
            error_msg = task.get("error", "Unknown error")
            raise RuntimeError(f"Generation failed: {error_msg}")

        time.sleep(POLL_INTERVAL)


def get_content(video_id: str) -> dict:
    """Step 3: Get video content (URL, duration, resolution)."""
    url = f"{BASE_URL}/videos/{video_id}/content"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def download_video(video_url: str, save_path: str):
    """Step 4: Download the video file."""
    response = requests.get(video_url, stream=True)
    response.raise_for_status()

    os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)

    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    size_mb = os.path.getsize(save_path) / (1024 * 1024)
    print(f"  💾 Saved: {save_path} ({size_mb:.1f} MB)")


def generate_single(prompt: str, model: str, output: str,
                     start_frame: str | None = None, end_frame: str | None = None):
    """Complete workflow for a single video."""
    # Build image paths list
    image_paths = None
    if start_frame:
        image_paths = [start_frame]
        if end_frame:
            image_paths.append(end_frame)

    # Step 1
    print(f"\n📤 Creating task...")
    print(f"   Model: {model}")
    print(f"   Prompt: {prompt[:80]}...")
    if image_paths:
        print(f"   Frames: {', '.join(image_paths)}")

    task = create_task(prompt, model, image_paths)
    video_id = task["id"]
    print(f"   Task ID: {video_id}")

    # Step 2
    print(f"\n⏳ Polling status...")
    poll_status(video_id)
    print(f"   ✅ Generation complete!")

    # Step 3
    print(f"\n📥 Getting video content...")
    content = get_content(video_id)
    video_url = content["url"]
    duration = content.get("duration", "?")
    resolution = content.get("resolution", "?")
    print(f"   Duration: {duration}s, Resolution: {resolution}")

    # Step 4
    print(f"\n💾 Downloading...")
    download_video(video_url, output)

    print(f"\n✅ Done: {output}")
    return output


def generate_batch(batch_file: str, output_dir: str, model: str):
    """Batch generation from JSON file.
    
    JSON format:
    [
      {
        "prompt": "Smooth timelapse transition...",
        "start_frame": "frames/frame-1.jpg",
        "end_frame": "frames/frame-2.jpg",
        "output": "segment-1-2.mp4"
      },
      ...
    ]
    """
    with open(batch_file) as f:
        tasks = json.load(f)

    os.makedirs(output_dir, exist_ok=True)
    
    results = []
    total = len(tasks)
    
    for i, task_spec in enumerate(tasks, 1):
        print(f"\n{'='*60}")
        print(f"  📹 Video {i}/{total}: {task_spec.get('output', f'video-{i}.mp4')}")
        print(f"{'='*60}")

        output_path = os.path.join(output_dir, task_spec.get("output", f"video-{i}.mp4"))
        
        try:
            result = generate_single(
                prompt=task_spec["prompt"],
                model=task_spec.get("model", model),
                output=output_path,
                start_frame=task_spec.get("start_frame"),
                end_frame=task_spec.get("end_frame"),
            )
            results.append({"output": result, "status": "ok"})
        except Exception as e:
            print(f"  ❌ Error: {e}")
            results.append({"output": output_path, "status": "error", "error": str(e)})

    # Summary
    print(f"\n{'='*60}")
    print(f"  📊 Batch Summary")
    print(f"{'='*60}")
    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"  ✅ Success: {ok}/{total}")
    if ok < total:
        print(f"  ❌ Failed: {total - ok}/{total}")
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Veo 3.1 Async Video Generator")
    parser.add_argument("--prompt", help="Video generation prompt")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Model name (default: {DEFAULT_MODEL})")
    parser.add_argument("--start-frame", help="Start frame image path (for image-to-video)")
    parser.add_argument("--end-frame", help="End frame image path (for first/last frame mode)")
    parser.add_argument("--output", "-o", default="video.mp4", help="Output file path")
    parser.add_argument("--batch", help="Batch JSON file path")
    parser.add_argument("--output-dir", default="./videos", help="Output directory for batch mode")
    parser.add_argument("--api-key", help="API key (overrides VEO_API_KEY env)")
    parser.add_argument("--poll-interval", type=int, default=POLL_INTERVAL, help="Poll interval in seconds")
    parser.add_argument("--timeout", type=int, default=TIMEOUT, help="Timeout in seconds")
    args = parser.parse_args()

    global API_KEY, POLL_INTERVAL, TIMEOUT
    
    if args.api_key:
        API_KEY = args.api_key
    if not API_KEY:
        print("❌ Set VEO_API_KEY environment variable or pass --api-key", file=sys.stderr)
        sys.exit(1)

    POLL_INTERVAL = args.poll_interval
    TIMEOUT = args.timeout

    if args.batch:
        generate_batch(args.batch, args.output_dir, args.model)
    elif args.prompt:
        generate_single(args.prompt, args.model, args.output, args.start_frame, args.end_frame)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
