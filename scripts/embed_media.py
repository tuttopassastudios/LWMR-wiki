#!/usr/bin/env python3
"""
Embed images and links into existing wiki pages.
Phase 3: Add image galleries to relevant wiki pages
Phase 4: Add External Resources sections with categorized links
"""

import json
import os
import re
from collections import defaultdict

VAULT_PATH = os.path.expanduser("~/Documents/Discord Wikipedia")
ASSETS_BASE = os.path.join(VAULT_PATH, "Assets", "recording-talk")

# Load mappings
with open(os.path.join(ASSETS_BASE, "_image-mapping.json")) as f:
    all_images = json.load(f)

with open(os.path.join(ASSETS_BASE, "_link-mapping.json")) as f:
    all_links = json.load(f)

# === Image classification by wiki page ===
TOPIC_IMAGE_KEYWORDS = {
    "Drum Recording Techniques": {
        "keywords": ["drum", "snare", "kick", "overhead", "cymbal", "hi-hat", "tom", "kit"],
        "exclude": ["bass drum"],  # avoid false positives
    },
    "Guitar Recording": {
        "keywords": ["guitar", "amp", "cab", "cabinet", "electric guitar", "acoustic guitar", "pedal"],
        "exclude": ["bass guitar"],
    },
    "Bass Recording": {
        "keywords": ["bass"],
        "exclude": [],
    },
    "Piano and Keys Recording": {
        "keywords": ["piano", "keys", "keyboard", "rhodes", "wurlitzer", "organ", "upright"],
        "exclude": [],
    },
    "Stereo Miking Techniques": {
        "keywords": ["stereo", "xy", "ortf", "spaced pair", "blumlein", "mid-side"],
        "exclude": [],
    },
    "Room Mics and Ambient Recording": {
        "keywords": ["room mic", "ambient", "room sound", "treatment", "room shot"],
        "exclude": [],
    },
    "Session Mindset and Engineering Philosophy": {
        "keywords": ["session", "console", "studio", "tracking day", "setup sheet"],
        "exclude": [],
    },
}

# Build page -> images mapping
page_images = defaultdict(list)
for img in all_images:
    combined = f"{img['description']} {img['message_content']}".lower()
    scores = {}
    for page, info in TOPIC_IMAGE_KEYWORDS.items():
        score = sum(1 for kw in info["keywords"] if kw in combined)
        if score > 0:
            scores[page] = score

    if scores:
        best = max(scores, key=scores.get)
        page_images[best].append(img)
    elif img['category'] == 'session-setups':
        page_images['Session Mindset and Engineering Philosophy'].append(img)

# Build page -> links mapping
page_links = defaultdict(list)
for link in all_links:
    if link.get('wiki_page'):
        page_name = link['wiki_page'].split('/')[-1].replace('.md', '')
        page_links[page_name].append(link)


def build_gallery_section(images, page_name, max_images=20):
    """Build a Gallery markdown section with image embeds."""
    lines = []
    lines.append("## Gallery")
    lines.append("")
    lines.append(f"*{len(images)} photos shared in #recording-talk. Showing selected highlights.*")
    lines.append("")

    # Sort by relevance score (description length as proxy) then date
    # Prioritize images with descriptive context
    scored = []
    for img in images:
        score = 0
        if img['message_content'].strip():
            score += 2
        if img['description'] != 'uncategorized' and img['description'] != 'session':
            score += 1
        scored.append((score, img))

    scored.sort(key=lambda x: (-x[0], x[1]['date']))
    selected = [img for _, img in scored[:max_images]]

    for img in selected:
        lines.append(f"![[{img['filename']}]]")
        # Add caption
        caption_parts = [f"*{img['author']}"]
        caption_parts.append(f"({img['date']})")
        if img['message_content'].strip():
            ctx = img['message_content'].strip()[:150]
            # Clean up URLs in context
            ctx = re.sub(r'https?://\S+', '', ctx).strip()
            if ctx:
                caption_parts.append(f"— {ctx}")
        lines.append(" ".join(caption_parts) + "*")
        lines.append("")

    if len(images) > max_images:
        lines.append(f"*See [[_image-index|Image Index]] for all {len(images)} photos.*")
        lines.append("")

    return "\n".join(lines)


def build_resources_section(links):
    """Build an External Resources markdown section."""
    lines = []
    lines.append("## External Resources")
    lines.append("")

    # Group by category
    by_cat = defaultdict(list)
    for link in links:
        by_cat[link['category']].append(link)

    # YouTube first
    if 'youtube' in by_cat:
        lines.append("### Videos")
        lines.append("")
        for link in by_cat['youtube']:
            title = link.get('title') or link['url']
            lines.append(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})")
        lines.append("")

    # Dropbox / audio samples
    if 'dropbox' in by_cat:
        lines.append("### Audio Samples & Shootouts")
        lines.append("")
        for link in by_cat['dropbox']:
            title = link.get('title') or link['url']
            lines.append(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})")
        lines.append("")

    # Gear listings
    gear_cats = ['reverb', 'sweetwater', 'gear-marketplace']
    gear_links = []
    for cat in gear_cats:
        gear_links.extend(by_cat.get(cat, []))
    if gear_links:
        lines.append("### Gear Listings")
        lines.append("")
        for link in gear_links:
            title = link.get('title') or link['url']
            lines.append(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})")
        lines.append("")

    # Articles
    if 'articles' in by_cat:
        lines.append("### Articles & References")
        lines.append("")
        for link in by_cat['articles']:
            title = link.get('title') or link['url']
            lines.append(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})")
        lines.append("")

    # Other
    other_cats = ['manufacturer', 'other']
    other_links = []
    for cat in other_cats:
        other_links.extend(by_cat.get(cat, []))
    if other_links:
        lines.append("### Other Links")
        lines.append("")
        for link in other_links:
            title = link.get('title') or link['url']
            lines.append(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})")
        lines.append("")

    lines.append(f"*See [[External Resources from recording-talk|Full External Resources Index]] for all links.*")
    lines.append("")

    return "\n".join(lines)


def insert_sections_into_page(filepath, gallery_md, resources_md):
    """Insert Gallery and External Resources sections into a wiki page."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Strategy: Insert Gallery before "## See Also" and External Resources after "## See Also" section
    # If no "## See Also", insert before "## Source Discussions"

    new_sections = ""
    if gallery_md:
        new_sections += gallery_md + "\n"
    if resources_md:
        new_sections += resources_md + "\n"

    if not new_sections:
        return False

    # Try to insert before ## See Also
    if "## See Also" in content:
        content = content.replace("## See Also", new_sections + "## See Also")
    elif "## Source Discussions" in content:
        content = content.replace("## Source Discussions", new_sections + "## Source Discussions")
    else:
        # Append at end
        content = content.rstrip() + "\n\n" + new_sections

    with open(filepath, 'w') as f:
        f.write(content)

    return True


# === Process each wiki page ===
RECORDING_PAGES = {
    "Drum Recording Techniques": "Topics/Recording/Drum Recording Techniques.md",
    "Guitar Recording": "Topics/Recording/Guitar Recording.md",
    "Bass Recording": "Topics/Recording/Bass Recording.md",
    "Piano and Keys Recording": "Topics/Recording/Piano and Keys Recording.md",
    "Stereo Miking Techniques": "Topics/Recording/Stereo Miking Techniques.md",
    "Room Mics and Ambient Recording": "Topics/Recording/Room Mics and Ambient Recording.md",
    "Session Mindset and Engineering Philosophy": "Topics/Recording/Session Mindset and Engineering Philosophy.md",
}

# Also check for Vocal Recording page
vocal_paths = [
    "Topics/Recording/Vocal Recording.md",
    "Topics/Mixing/Vocal Chain and Processing.md",
]
for vp in vocal_paths:
    full = os.path.join(VAULT_PATH, vp)
    if os.path.exists(full):
        RECORDING_PAGES["Vocal Recording"] = vp
        break

# Map images for Vocal Recording too
TOPIC_IMAGE_KEYWORDS["Vocal Recording"] = {
    "keywords": ["vocal", "voice", "singer", "singing"],
    "exclude": [],
}

# Reclassify vocal images
for img in all_images:
    combined = f"{img['description']} {img['message_content']}".lower()
    if any(kw in combined for kw in ["vocal", "voice", "singer"]):
        if img not in page_images.get("Vocal Recording", []):
            page_images["Vocal Recording"].append(img)

print("=" * 60)
print("EMBEDDING IMAGES AND LINKS INTO WIKI PAGES")
print("=" * 60)

for page_name, rel_path in RECORDING_PAGES.items():
    filepath = os.path.join(VAULT_PATH, rel_path)
    if not os.path.exists(filepath):
        print(f"\n  SKIP {page_name} — file not found")
        continue

    images = page_images.get(page_name, [])
    links = page_links.get(page_name, [])

    print(f"\n{page_name}:")
    print(f"  Images: {len(images)}")
    print(f"  Links: {len(links)}")

    gallery_md = build_gallery_section(images, page_name) if images else ""
    resources_md = build_resources_section(links) if links else ""

    if gallery_md or resources_md:
        success = insert_sections_into_page(filepath, gallery_md, resources_md)
        if success:
            print(f"  ✓ Updated {rel_path}")
        else:
            print(f"  ✗ Failed to update {rel_path}")
    else:
        print(f"  — Nothing to add")

# === Also handle Headphone Mixes and Recording Workflows pages ===
extra_pages = {
    "Headphone Mixes and Cue Systems": "Topics/Recording/Headphone Mixes and Cue Systems.md",
    "Recording and Tracking Workflows": "Topics/Recording/Recording and Tracking Workflows.md",
}

for page_name, rel_path in extra_pages.items():
    filepath = os.path.join(VAULT_PATH, rel_path)
    if not os.path.exists(filepath):
        continue

    links = page_links.get(page_name, [])
    if links:
        resources_md = build_resources_section(links)
        insert_sections_into_page(filepath, "", resources_md)
        print(f"\n{page_name}: {len(links)} links ✓")

print("\n" + "=" * 60)
print("DONE")
print("=" * 60)
print(f"\nTotal images distributed: {sum(len(v) for v in page_images.values())}")
print(f"Total links distributed: {sum(len(v) for v in page_links.values())}")
