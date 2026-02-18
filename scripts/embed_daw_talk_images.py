#!/usr/bin/env python3
"""Embed daw-talk images into topic pages, inserting before Source Discussions."""

import json
from pathlib import Path

VAULT = Path("/Users/tylerchase/Documents/Discord Wikipedia")
TOPICS_DIR = VAULT / "Topics" / "Workflow"
ASSETS_DIR = VAULT / "Assets" / "daw-talk"
TOPIC_MAPPING = ASSETS_DIR / "_topic-image-mapping.json"

# Max images per topic page to keep it manageable
MAX_IMAGES_PER_TOPIC = 12


def main():
    with open(TOPIC_MAPPING) as f:
        topic_images = json.load(f)

    for topic_file, images in topic_images.items():
        topic_path = TOPICS_DIR / topic_file
        if not topic_path.exists():
            print(f"SKIP (not found): {topic_file}")
            continue

        # Filter to images that actually exist on disk
        existing_images = []
        for img in images:
            abs_path = VAULT / img['path']
            if abs_path.exists() and abs_path.stat().st_size > 0:
                existing_images.append(img)

        if not existing_images:
            print(f"SKIP (no downloaded images): {topic_file} (0/{len(images)})")
            continue

        # Limit and pick diverse images (spread across dates)
        existing_images.sort(key=lambda x: x['date'])
        if len(existing_images) > MAX_IMAGES_PER_TOPIC:
            # Sample evenly across the timeline
            step = len(existing_images) / MAX_IMAGES_PER_TOPIC
            selected = []
            for i in range(MAX_IMAGES_PER_TOPIC):
                idx = int(i * step)
                selected.append(existing_images[idx])
            existing_images = selected

        # Build image gallery section
        gallery_lines = [
            '',
            '## Community Screenshots',
            '',
        ]
        for img in existing_images:
            caption_parts = [f"**{img['author']}** — {img['date']}"]
            if img['message_content']:
                # Truncate long content
                content = img['message_content'][:150]
                if len(img['message_content']) > 150:
                    content += '...'
                caption_parts.append(content)
            gallery_lines.append(f'![[{img["filename"]}]]')
            gallery_lines.append(f'*{" — ".join(caption_parts)}*')
            gallery_lines.append('')

        # Read existing file
        content = topic_path.read_text()

        # Insert before "## Source Discussions"
        marker = '## Source Discussions'
        if marker in content:
            parts = content.split(marker, 1)
            new_content = parts[0].rstrip() + '\n' + '\n'.join(gallery_lines) + '\n' + marker + parts[1]
        else:
            # Append at end
            new_content = content.rstrip() + '\n' + '\n'.join(gallery_lines) + '\n'

        topic_path.write_text(new_content)
        print(f"EMBEDDED: {topic_file} — {len(existing_images)} images (of {len(images)} matched)")

    print("\nDone!")


if __name__ == '__main__':
    main()
