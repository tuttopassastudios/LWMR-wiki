#!/usr/bin/env python3
"""
Extract and download recording-relevant images from #recording-talk Discord export.
Classifies images into categories based on message context, downloads them with
descriptive filenames, and generates an image index for the wiki.
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from collections import defaultdict
from pathlib import Path

# === Configuration ===
JSON_PATH = os.path.expanduser(
    "~/Downloads/Live with Matt Rad - Studio - 🎤recording-talk [916021850683879434].json"
)
VAULT_PATH = os.path.expanduser("~/Documents/Discord Wikipedia")
ASSETS_BASE = os.path.join(VAULT_PATH, "Assets", "recording-talk")

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.heic'}

# Keywords for classification
CATEGORY_KEYWORDS = {
    "session-setups": [
        "session", "setup", "tracking", "recording day", "studio", "live room",
        "control room", "recording some", "today's session", "tracking day",
        "console", "desk", "patch bay", "patchbay", "signal flow",
        "recording bloody", "string day", "orchestra", "ensemble",
        "band", "artist", "singer", "vocalist", "player", "musician",
        "my setup", "the setup", "setup sheet", "input list",
    ],
    "mic-placement": [
        "mic placement", "mic position", "overhead", "close mic", "room mic",
        "spaced pair", "xy", "ortf", "blumlein", "mid-side", "m/s",
        "kick mic", "snare mic", "hi-hat mic", "tom mic",
        "guitar mic", "amp mic", "cab mic", "vocal mic",
        "how i mic", "where i put", "placement", "distance",
        "inches", "feet", "angle", "aimed", "pointing",
        "two angles", "mic'd", "miked", "miking", "micing",
    ],
    "gear-photos": [
        "bought", "new gear", "just got", "arrived", "unboxed",
        "my mic", "my preamp", "my compressor", "my eq",
        "sm57", "sm7b", "u87", "u47", "c414", "re20", "421",
        "1073", "1176", "la-2a", "la2a", "distressor", "api",
        "neve", "ssl", "ua", "universal audio", "warm audio",
        "ribbon", "condenser", "dynamic", "preamp", "compressor",
        "mic locker", "gear", "interface", "converter",
        "elam", "royer", "coles", "akg", "neumann", "shure",
        "sennheiser", "beyerdynamic", "audio-technica",
        "tube", "transformer", "capsule",
        "reverb.com", "sweetwater", "shootout", "comparison",
    ],
    "diagrams": [
        "diagram", "drawing", "sketch", "illustration", "chart",
        "frequency", "response", "polar pattern", "phase",
        "scientific drawing", "crayons",
    ],
}

# Keywords that suggest recording-relevance even without category match
RECORDING_RELEVANT = [
    "record", "mic", "drum", "guitar", "bass", "vocal", "piano", "keys",
    "amp", "cab", "di", "preamp", "overhead", "snare", "kick", "tom",
    "acoustic", "electric", "string", "brass", "wind", "percussion",
    "mono", "stereo", "room", "ambient", "bleed", "isolation",
    "gain", "level", "pad", "phantom", "48v",
    "sound", "tone", "bright", "dark", "warm", "crispy",
    "mix", "track", "take", "punch", "overdub",
    "studio", "booth", "live room", "dead room", "treated",
]

# Keywords suggesting NOT recording-relevant
SKIP_KEYWORDS = [
    "meme", "lol", "haha", "lmao", "bruh",
    "selfie", "my face", "my cat", "my dog", "my kid",
    "food", "dinner", "lunch", "beer", "coffee",
    "vacation", "holiday", "christmas tree",
    "screenshot", "twitter", "tweet", "instagram",
]

# Contextual reply lookup - we'll also check the parent message for context
def get_reply_context(msg, messages_by_id):
    """Get context from the message this is replying to."""
    ref = msg.get("reference")
    if ref and ref.get("messageId"):
        parent = messages_by_id.get(ref["messageId"])
        if parent:
            return parent.get("content", "")
    return ""


def classify_image(msg_content, reply_content, filename):
    """Classify an image based on message context. Returns (category, description, relevance_score)."""
    combined = f"{msg_content} {reply_content} {filename}".lower()

    # Check skip keywords first
    skip_score = sum(1 for kw in SKIP_KEYWORDS if kw in combined)
    if skip_score >= 2 and not any(kw in combined for kw in RECORDING_RELEVANT[:10]):
        return None, None, 0

    # Score each category
    category_scores = {}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in combined)
        if score > 0:
            category_scores[cat] = score

    # General recording relevance
    relevance = sum(1 for kw in RECORDING_RELEVANT if kw in combined)

    if category_scores:
        best_cat = max(category_scores, key=category_scores.get)
        return best_cat, generate_description(combined, best_cat), relevance + category_scores[best_cat]
    elif relevance >= 2:
        # Relevant but no clear category - default to session-setups
        return "session-setups", generate_description(combined, "session-setups"), relevance
    elif not msg_content.strip():
        # No context at all - still download if in a recording channel (lower priority)
        return "session-setups", "uncategorized", 1
    else:
        return None, None, 0


def generate_description(text, category):
    """Generate a brief description for the filename based on context."""
    text_lower = text.lower()

    # Try to identify what instrument/source
    instruments = {
        "drum": "drum", "snare": "snare", "kick": "kick", "tom": "tom",
        "overhead": "overhead", "cymbal": "cymbal", "hi-hat": "hihat",
        "guitar": "guitar", "bass": "bass", "vocal": "vocal",
        "piano": "piano", "keys": "keys", "organ": "organ",
        "string": "strings", "brass": "brass", "horn": "horn",
        "acoustic": "acoustic", "electric": "electric",
        "amp": "amp", "cabinet": "cab", "di": "di",
    }

    found_instruments = []
    for kw, label in instruments.items():
        if kw in text_lower:
            found_instruments.append(label)

    # Try to identify what type of shot
    shot_types = {
        "setup": "setup", "placement": "placement", "position": "position",
        "session": "session", "tracking": "tracking",
        "shootout": "shootout", "comparison": "comparison",
        "studio": "studio", "room": "room", "console": "console",
        "bought": "new-gear", "arrived": "new-gear", "unboxed": "new-gear",
        "mic locker": "mic-locker", "gear": "gear",
        "diagram": "diagram", "drawing": "drawing",
    }

    found_types = []
    for kw, label in shot_types.items():
        if kw in text_lower:
            found_types.append(label)

    parts = []
    if found_instruments:
        parts.extend(found_instruments[:2])
    if found_types:
        parts.extend(found_types[:1])

    if parts:
        return "-".join(dict.fromkeys(parts))  # deduplicate preserving order

    if category == "session-setups":
        return "session"
    elif category == "gear-photos":
        return "gear"
    elif category == "mic-placement":
        return "mic-placement"
    elif category == "diagrams":
        return "diagram"
    return "photo"


def sanitize_filename(name):
    """Make a string safe for filenames."""
    name = re.sub(r'[^\w\-]', '-', name.lower())
    name = re.sub(r'-+', '-', name).strip('-')
    return name[:50]


def download_image(url, dest_path, retries=3):
    """Download an image from Discord CDN."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            })
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                with open(dest_path, 'wb') as f:
                    f.write(data)
                return True
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"  FAILED: {e}")
                return False
    return False


def main():
    print("Loading JSON data...")
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    messages = data['messages']
    print(f"Total messages: {len(messages)}")

    # Build message lookup for reply context
    messages_by_id = {msg['id']: msg for msg in messages}

    # Extract and classify all images
    print("\nClassifying images...")
    to_download = []
    skipped = []

    for msg in messages:
        for att in msg.get('attachments', []):
            fn = att['fileName'].lower()
            ext = os.path.splitext(fn)[1]
            if ext not in IMAGE_EXTENSIONS:
                continue

            content = msg.get('content', '') or ''
            reply_ctx = get_reply_context(msg, messages_by_id)

            category, desc, score = classify_image(content, reply_ctx, fn)

            if category is None:
                skipped.append({
                    'fileName': att['fileName'],
                    'author': msg['author'].get('nickname') or msg['author']['name'],
                    'content': content[:100],
                    'score': score,
                })
                continue

            author_name = sanitize_filename(
                msg['author'].get('nickname') or msg['author']['name']
            )
            date = msg['timestamp'][:10]

            to_download.append({
                'url': att['url'],
                'original_filename': att['fileName'],
                'category': category,
                'description': desc,
                'author': author_name,
                'author_display': msg['author'].get('nickname') or msg['author']['name'],
                'date': date,
                'message_content': content,
                'message_id': msg['id'],
                'size': att.get('fileSizeBytes', 0),
                'score': score,
                'ext': ext,
            })

    print(f"\nClassification results:")
    print(f"  To download: {to_download.__len__()}")
    print(f"  Skipped: {len(skipped)}")

    # Count by category
    cat_counts = defaultdict(int)
    for img in to_download:
        cat_counts[img['category']] += 1
    for cat, count in sorted(cat_counts.items()):
        print(f"    {cat}: {count}")

    # Sort by date for consistent numbering
    to_download.sort(key=lambda x: (x['date'], x['message_id']))

    # Track filenames to avoid duplicates
    used_filenames = set()

    # Download images
    print(f"\nDownloading {len(to_download)} images...")
    downloaded = []
    failed = []

    for i, img in enumerate(to_download):
        # Generate filename
        base_name = f"{img['author']}_{img['date']}_{img['description']}"
        filename = sanitize_filename(base_name) + img['ext']

        # Handle duplicates
        if filename in used_filenames:
            counter = 2
            while f"{sanitize_filename(base_name)}-{counter}{img['ext']}" in used_filenames:
                counter += 1
            filename = f"{sanitize_filename(base_name)}-{counter}{img['ext']}"
        used_filenames.add(filename)

        dest_dir = os.path.join(ASSETS_BASE, img['category'])
        dest_path = os.path.join(dest_dir, filename)

        progress = f"[{i+1}/{len(to_download)}]"
        print(f"  {progress} {filename}", end="", flush=True)

        if download_image(img['url'], dest_path):
            img['saved_filename'] = filename
            img['saved_path'] = os.path.join("Assets", "recording-talk", img['category'], filename)
            downloaded.append(img)
            print(" ✓")
        else:
            failed.append(img)
            print(" ✗")

        # Rate limiting - be nice to Discord CDN
        if i % 10 == 0 and i > 0:
            time.sleep(0.5)

    print(f"\nDownload complete: {len(downloaded)} succeeded, {len(failed)} failed")

    # Generate image index
    print("\nGenerating image index...")
    index_path = os.path.join(ASSETS_BASE, "_image-index.md")

    with open(index_path, 'w') as f:
        f.write("---\n")
        f.write("type: index\n")
        f.write(f"created: {time.strftime('%Y-%m-%d')}\n")
        f.write(f"total_images: {len(downloaded)}\n")
        f.write("---\n\n")
        f.write("# Image Index — recording-talk\n\n")
        f.write(f"**Total downloaded:** {len(downloaded)} images\n")
        f.write(f"**Failed:** {len(failed)} images\n")
        f.write(f"**Skipped (off-topic):** {len(skipped)} images\n\n")

        # By category
        for cat in ["session-setups", "mic-placement", "gear-photos", "diagrams"]:
            cat_imgs = [img for img in downloaded if img['category'] == cat]
            if not cat_imgs:
                continue

            f.write(f"## {cat.replace('-', ' ').title()} ({len(cat_imgs)} images)\n\n")

            for img in cat_imgs:
                f.write(f"### `{img['saved_filename']}`\n")
                f.write(f"- **Author:** {img['author_display']}\n")
                f.write(f"- **Date:** {img['date']}\n")
                if img['message_content']:
                    # Truncate long content
                    content = img['message_content'][:200]
                    if len(img['message_content']) > 200:
                        content += "..."
                    f.write(f"- **Context:** {content}\n")
                f.write(f"- **Embed:** `![[{img['saved_filename']}]]`\n")
                f.write(f"- **Message ID:** {img['message_id']}\n")
                f.write("\n")

    print(f"Image index written to {index_path}")

    # Also write a JSON mapping for use by other scripts
    mapping_path = os.path.join(ASSETS_BASE, "_image-mapping.json")
    mapping_data = []
    for img in downloaded:
        mapping_data.append({
            'filename': img['saved_filename'],
            'path': img['saved_path'],
            'category': img['category'],
            'author': img['author_display'],
            'date': img['date'],
            'description': img['description'],
            'message_content': img['message_content'][:300],
            'message_id': img['message_id'],
        })

    with open(mapping_path, 'w') as f:
        json.dump(mapping_data, f, indent=2)

    print(f"Image mapping JSON written to {mapping_path}")

    # Summary of skipped images (for review)
    skip_log_path = os.path.join(ASSETS_BASE, "_skipped-images.json")
    with open(skip_log_path, 'w') as f:
        json.dump(skipped, f, indent=2)
    print(f"Skipped images log written to {skip_log_path}")

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Downloaded: {len(downloaded)}")
    for cat in ["session-setups", "mic-placement", "gear-photos", "diagrams"]:
        count = sum(1 for img in downloaded if img['category'] == cat)
        print(f"  {cat}: {count}")
    print(f"Failed: {len(failed)}")
    print(f"Skipped: {len(skipped)}")

    return len(downloaded), len(failed), len(skipped)


if __name__ == "__main__":
    main()
