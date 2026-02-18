#!/usr/bin/env python3
"""
Convert Obsidian ![[filename]] image embeds to markdown ![alt](discord-cdn-url) format.
This allows images to render on GitHub Pages without committing binary files.
"""

import json
import os
import re
from collections import defaultdict

VAULT_PATH = os.path.expanduser("~/Documents/Discord Wikipedia")
JSON_PATH = os.path.expanduser(
    "~/Downloads/Live with Matt Rad - Studio - 🎤recording-talk [916021850683879434].json"
)
MAPPING_PATH = os.path.join(VAULT_PATH, "Assets", "recording-talk", "_image-mapping.json")

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.heic'}

# Load Discord JSON for URL lookup
print("Loading Discord JSON...")
with open(JSON_PATH) as f:
    discord_data = json.load(f)

# Build message_id -> ordered list of image attachment URLs
msg_image_urls = {}
for msg in discord_data['messages']:
    img_atts = []
    for att in msg.get('attachments', []):
        fn = att['fileName'].lower()
        ext = os.path.splitext(fn)[1]
        if ext in IMAGE_EXTENSIONS:
            # Strip query params for cleaner URLs (base Discord CDN URLs work without tokens)
            base_url = att['url'].split('?')[0]
            img_atts.append(base_url)
    if img_atts:
        msg_image_urls[msg['id']] = img_atts

# Load our image mapping
with open(MAPPING_PATH) as f:
    mapping = json.load(f)

# Build filename -> CDN URL lookup
# The download script processed attachments in order per message,
# so we track per-message indices
msg_att_index = defaultdict(int)
filename_to_url = {}

for img in mapping:
    mid = img['message_id']
    urls = msg_image_urls.get(mid, [])
    idx = msg_att_index[mid]

    if idx < len(urls):
        filename_to_url[img['filename']] = urls[idx]
    else:
        # Fallback - try first URL
        if urls:
            filename_to_url[img['filename']] = urls[0]
        else:
            print(f"  WARNING: No URL found for {img['filename']} (msg {mid})")

    msg_att_index[mid] = idx + 1

print(f"Built URL lookup for {len(filename_to_url)} of {len(mapping)} images")

# Now find and replace all ![[filename]] in wiki pages
def convert_embeds_in_file(filepath):
    """Replace ![[image.ext]] with ![alt](cdn-url) in a file."""
    with open(filepath, 'r') as f:
        content = f.read()

    original = content

    # Pattern: ![[filename.ext]] possibly followed by caption on next line
    def replace_embed(match):
        filename = match.group(1)
        url = filename_to_url.get(filename)
        if url:
            # Use filename as alt text (cleaned up)
            alt = filename.rsplit('.', 1)[0].replace('-', ' ').replace('_', ' ')
            return f"![{alt}]({url})"
        return match.group(0)  # Leave unchanged if no URL

    content = re.sub(r'!\[\[([^\]]+\.(?:jpg|jpeg|png|webp|heic))\]\]', replace_embed, content)

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False


# Process all markdown files in the vault
print("\nConverting image embeds in wiki pages...")
converted_files = []

for root, dirs, files in os.walk(VAULT_PATH):
    # Skip hidden dirs and node_modules
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fn in files:
        if fn.endswith('.md'):
            filepath = os.path.join(root, fn)
            if convert_embeds_in_file(filepath):
                rel = os.path.relpath(filepath, VAULT_PATH)
                converted_files.append(rel)
                print(f"  ✓ {rel}")

print(f"\nConverted {len(converted_files)} files")

# Also update the _image-index.md to use CDN links
index_path = os.path.join(VAULT_PATH, "Assets", "recording-talk", "_image-index.md")
if os.path.exists(index_path):
    with open(index_path, 'r') as f:
        content = f.read()

    # Replace ![[filename]] embeds
    def replace_index_embed(match):
        filename = match.group(1)
        url = filename_to_url.get(filename)
        if url:
            alt = filename.rsplit('.', 1)[0].replace('-', ' ').replace('_', ' ')
            return f"![{alt}]({url})"
        return match.group(0)

    content = re.sub(r'!\[\[([^\]]+\.(?:jpg|jpeg|png|webp|heic))\]\]', replace_index_embed, content)

    # Also replace the embed reference format in the index
    # `![[filename.jpg]]` -> `![alt](url)`
    def replace_backtick_embed(match):
        filename = match.group(1)
        url = filename_to_url.get(filename)
        if url:
            return f"`![{filename}]({url})`"
        return match.group(0)

    content = re.sub(r'`!\[\[([^\]]+\.(?:jpg|jpeg|png|webp|heic))\]\]`', replace_backtick_embed, content)

    with open(index_path, 'w') as f:
        f.write(content)
    print(f"  ✓ Updated _image-index.md")

# Update the mapping JSON to include CDN URLs
for img in mapping:
    img['cdn_url'] = filename_to_url.get(img['filename'], '')

with open(MAPPING_PATH, 'w') as f:
    json.dump(mapping, f, indent=2)
print(f"  ✓ Updated _image-mapping.json with CDN URLs")

print("\nDone!")
