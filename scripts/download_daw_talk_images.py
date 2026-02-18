#!/usr/bin/env python3
"""Download, categorize, and catalog images from daw-talk Discord channel."""

import json
import re
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError

VAULT = Path("/Users/tylerchase/Documents/Discord Wikipedia")
JSON_PATH = Path("/Users/tylerchase/Downloads/Live with Matt Rad - Studio - 🖥daw-talk [806967264396967966].json")
ASSETS_DIR = VAULT / "Assets" / "daw-talk"
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}

CATEGORIES = ['daw-screenshots', 'plugin-screenshots', 'session-screenshots', 'gear-photos', 'misc']

PLUGIN_KEYWORDS = [
    'plugin', 'vst', 'au ', 'aax', 'compressor', 'eq ', 'reverb', 'delay',
    'limiter', 'saturator', 'synth', 'instrument', 'fabfilter', 'waves',
    'soundtoys', 'slate', 'izotope', 'ozone', 'neutron', 'pro-q',
    'ssl', 'neve', 'api ', 'uad', 'kontakt', 'omnisphere', 'serum',
    'massive', 'sylenth', 'arturia', 'softube', 'plugin alliance',
    'acustica', 'stock plugin', 'channel strip'
]
SESSION_KEYWORDS = [
    'routing', 'template', 'track layout', 'i/o', 'bus', 'aux',
    'send', 'return', 'signal flow', 'session setup', 'track list',
    'folder track', 'group track', 'submix', 'stem', 'channel',
    'vca', 'master bus', 'print track'
]
GEAR_KEYWORDS = [
    'controller', 'interface', 'hardware', 'midi controller',
    'fader', 'console', 'monitor', 'speaker', 'headphone', 'desk',
    'studio setup', 'rack', 'patchbay', 'apollo', 'focusrite',
    'presonus', 'motu', 'rme', 'avid s1', 'icon platform'
]
MISC_KEYWORDS = [
    'meme', 'lol', 'haha', 'funny', 'joke', 'off topic', 'offtopic',
    'shitpost', '😂', '🤣', 'lmao', 'bruh'
]

TOPIC_KEYWORDS = {
    'DAW Comparison.md': [
        'pro tools', 'ableton', 'logic', 'cubase', 'reaper', 'studio one',
        'fl studio', 'bitwig', 'daw comparison', 'which daw', 'switch daw',
        'better daw', 'daw vs', 'garageband', 'nuendo'
    ],
    'CPU Optimization for Audio.md': [
        'cpu', 'buffer', 'latency', 'performance', 'optimization', 'freeze',
        'bounce in place', 'native', 'dsp', 'processing power', 'overload',
        'asio', 'core audio', 'sample rate', 'thread', 'multicore',
        'activity monitor', 'task manager', 'ram', 'memory'
    ],
    'Session Templates and Organization.md': [
        'template', 'session setup', 'organization', 'folder track',
        'color cod', 'naming convention', 'track layout', 'default session',
        'routing template', 'mix template', 'session organiz'
    ],
    'Keyboard Shortcuts and Macros.md': [
        'shortcut', 'key command', 'macro', 'hotkey',
        'streamdeck', 'touch osc', 'metagrid', 'custom action',
        'key binding', 'quickkey'
    ],
    'Bounce and Export Workflows.md': [
        'bounce', 'export', 'render', 'stem', 'print', 'offline bounce',
        'real-time bounce', 'dither', 'bit depth', 'sample rate convert',
        'mp3', 'wav', 'aiff', 'flac', 'consolidat'
    ],
    'Troubleshooting DAW Issues.md': [
        'crash', 'bug', 'error', 'problem', 'issue', 'fix', 'troubleshoot',
        'not working', 'broke', 'glitch', 'corrupt', "won't open",
        'spinning wheel', 'beach ball'
    ],
    'Computer Hardware for Audio.md': [
        'computer', 'mac', 'pc', 'windows', 'apple silicon', 'm1', 'm2', 'm3', 'm4',
        'intel', 'amd', 'processor', 'ssd', 'hard drive', 'thunderbolt',
        'usb', 'pcie', 'build', 'spec', 'upgrade', 'hackintosh'
    ],
    'Audio File Management.md': [
        'file management', 'audio file', 'file format', 'consolidat',
        'collect all', 'save copy'
    ],
    'Backup and Storage for Audio.md': [
        'backup', 'storage', 'cloud', 'raid', 'nas',
        'time machine', 'dropbox', 'google drive', 'icloud',
        'external drive', 'archive'
    ],
    'DAW Pricing and Licensing.md': [
        'price', 'cost', 'subscription', 'perpetual', 'license',
        'student discount', 'ilok', 'activation', 'rent to own', 'splice rent'
    ],
    'DAW Version History and Updates.md': [
        'update', 'version', 'new feature', 'changelog',
        'beta', 'release', 'live 11', 'live 12', 'pro tools 202',
        'logic 10', 'cubase 1'
    ],
}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:50].rstrip('-')


def categorize_image(message_content, filename):
    content_lower = (message_content + ' ' + filename).lower()
    if any(kw in content_lower for kw in MISC_KEYWORDS):
        return 'misc'
    if any(kw in content_lower for kw in GEAR_KEYWORDS):
        return 'gear-photos'
    if any(kw in content_lower for kw in PLUGIN_KEYWORDS):
        return 'plugin-screenshots'
    if any(kw in content_lower for kw in SESSION_KEYWORDS):
        return 'session-screenshots'
    return 'daw-screenshots'


def generate_description(message_content, original_filename):
    name = Path(original_filename).stem
    name_clean = re.sub(r'(image\d*|unknown|screen.?shot|img|photo|pic)', '', name, flags=re.I)
    name_clean = re.sub(r'[\d_\-\.]+', ' ', name_clean).strip()
    if name_clean and len(name_clean) > 3:
        return slugify(name_clean)
    if message_content:
        words = message_content.split()[:6]
        slug = slugify(' '.join(words))
        if slug and len(slug) > 3:
            return slug
    return 'uncategorized'


def match_topics(message_content):
    if not message_content:
        return []
    content_lower = message_content.lower()
    return [t for t, kws in TOPIC_KEYWORDS.items() if any(kw in content_lower for kw in kws)]


def main():
    print("=== DAW-Talk Image Pipeline ===\n")

    with open(JSON_PATH) as f:
        data = json.load(f)
    messages = data['messages']
    print(f"Total messages: {len(messages)}")

    # Extract image attachments
    images = []
    for msg in messages:
        for i, att in enumerate(msg.get('attachments', [])):
            fname = att.get('fileName', '')
            if not any(fname.lower().endswith(ext) for ext in IMAGE_EXTS):
                continue
            author_name = msg['author'].get('nickname') or msg['author']['name']
            images.append({
                'original_filename': fname,
                'url': att['url'],
                'author': author_name,
                'date': msg['timestamp'][:10],
                'message_content': msg.get('content', ''),
                'message_id': msg['id'],
            })
    print(f"Image attachments: {len(images)}")

    # Create category directories
    for cat in CATEGORIES:
        (ASSETS_DIR / cat).mkdir(parents=True, exist_ok=True)

    # Build mapping
    filename_counts = defaultdict(int)
    mapping = []
    topic_images = defaultdict(list)

    for img in images:
        author_slug = slugify(img['author'])
        date = img['date']
        desc = generate_description(img['message_content'], img['original_filename'])
        ext = Path(img['original_filename']).suffix.lower()
        category = categorize_image(img['message_content'], img['original_filename'])

        base = f"{author_slug}_{date}_{desc}"
        key = base + ext
        filename_counts[key] += 1
        count = filename_counts[key]
        filename = f"{base}-{count}{ext}" if count > 1 else f"{base}{ext}"

        rel_path = f"Assets/daw-talk/{category}/{filename}"
        abs_path = VAULT / rel_path

        entry = {
            'filename': filename,
            'path': rel_path,
            'category': category,
            'author': img['author'],
            'date': date,
            'description': desc,
            'message_content': img['message_content'][:500],
            'message_id': img['message_id'],
            'cdn_url': img['url'],
            '_abs_path': str(abs_path),
        }
        mapping.append(entry)
        for topic in match_topics(img['message_content']):
            topic_images[topic].append(entry)

    cat_counts = defaultdict(int)
    for e in mapping:
        cat_counts[e['category']] += 1
    print("\nCategory breakdown:")
    for cat, count in sorted(cat_counts.items()):
        print(f"  {cat}: {count}")

    # Download using curl (Python urlretrieve fails on Discord CDN tokens)
    print(f"\nDownloading {len(mapping)} images...")
    downloaded = 0
    failed = 0
    skipped = 0
    failed_entries = []

    for entry in mapping:
        abs_path = Path(entry['_abs_path'])
        if abs_path.exists() and abs_path.stat().st_size > 0:
            skipped += 1
            continue
        result = subprocess.run(
            ['curl', '-sS', '-f', '-L', '-o', str(abs_path), entry['cdn_url']],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            downloaded += 1
            if downloaded % 50 == 0:
                print(f"  ...{downloaded} downloaded")
        else:
            failed += 1
            failed_entries.append({'filename': entry['filename'], 'error': result.stderr.strip(), 'cdn_url': entry['cdn_url']})
            if failed <= 5:
                print(f"  FAILED: {entry['filename']}: {result.stderr.strip()}")
            # Clean up empty file
            if abs_path.exists():
                abs_path.unlink()

    print(f"Downloaded: {downloaded}, Skipped (existing): {skipped}, Failed: {failed}")

    # Save skipped/failed
    if failed_entries:
        with open(ASSETS_DIR / '_failed-downloads.json', 'w') as f:
            json.dump(failed_entries, f, indent=2)

    # Strip internal path before saving
    clean_mapping = []
    for e in mapping:
        ec = {k: v for k, v in e.items() if not k.startswith('_')}
        clean_mapping.append(ec)

    # Save _image-mapping.json
    with open(ASSETS_DIR / '_image-mapping.json', 'w') as f:
        json.dump(clean_mapping, f, indent=2)
    print(f"\nSaved: Assets/daw-talk/_image-mapping.json")

    # Resize with sips
    print("\nResizing images (sips -Z 1200)...")
    for cat in CATEGORIES:
        cat_dir = ASSETS_DIR / cat
        imgs = [p for p in cat_dir.iterdir() if p.suffix.lower() in IMAGE_EXTS]
        if not imgs:
            continue
        for batch_start in range(0, len(imgs), 50):
            batch = imgs[batch_start:batch_start + 50]
            paths_str = ' '.join(f'"{p}"' for p in batch)
            subprocess.run(f'sips -Z 1200 {paths_str}', shell=True, capture_output=True)
        print(f"  Resized {len(imgs)} in {cat}/")

    # Generate _image-index.md
    index_lines = [
        '---', 'type: index',
        f'created: {datetime.now().strftime("%Y-%m-%d")}',
        f'total_images: {len(clean_mapping)}',
        '---', '',
        '# Image Index — daw-talk', '',
        f'**Total downloaded:** {downloaded + skipped} images',
        f'**Failed:** {failed} images', '',
    ]
    for cat_name in CATEGORIES:
        cat_entries = [e for e in clean_mapping if e['category'] == cat_name]
        display_name = cat_name.replace('-', ' ').title()
        index_lines.append(f'## {display_name} ({len(cat_entries)} images)')
        index_lines.append('')
        for entry in cat_entries:
            index_lines.append(f'### `{entry["filename"]}`')
            index_lines.append(f'- **Author:** {entry["author"]}')
            index_lines.append(f'- **Date:** {entry["date"]}')
            if entry['message_content']:
                index_lines.append(f'- **Context:** {entry["message_content"][:200]}')
            index_lines.append(f'- **Embed:** `![[{entry["filename"]}]]`')
            index_lines.append(f'- **Message ID:** {entry["message_id"]}')
            index_lines.append('')
    with open(ASSETS_DIR / '_image-index.md', 'w') as f:
        f.write('\n'.join(index_lines))
    print(f"Saved: Assets/daw-talk/_image-index.md")

    # Save topic mapping
    topic_clean = {}
    for t, imgs in topic_images.items():
        topic_clean[t] = [{k: v for k, v in e.items() if not k.startswith('_')} for e in imgs]
    with open(ASSETS_DIR / '_topic-image-mapping.json', 'w') as f:
        json.dump(topic_clean, f, indent=2)
    print(f"Saved: Assets/daw-talk/_topic-image-mapping.json")

    print("\nTopic page matches:")
    for topic, imgs in sorted(topic_images.items()):
        print(f"  {topic}: {len(imgs)} images")

    print("\n=== Pipeline complete ===")


if __name__ == '__main__':
    main()
