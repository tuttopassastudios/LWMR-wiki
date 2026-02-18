#!/usr/bin/env python3
"""
Extract and categorize web links from #recording-talk Discord export.
Filters out irrelevant links (GIFs, streaming, social) and categorizes
the rest for integration into the wiki.
"""

import json
import os
import re
import time
from collections import defaultdict
from urllib.parse import urlparse

# === Configuration ===
JSON_PATH = os.path.expanduser(
    "~/Downloads/Live with Matt Rad - Studio - 🎤recording-talk [916021850683879434].json"
)
VAULT_PATH = os.path.expanduser("~/Documents/Discord Wikipedia")

# Domains to SKIP
SKIP_DOMAINS = {
    "tenor.com", "media.tenor.com",  # GIFs
    "giphy.com", "media.giphy.com",  # GIFs
    "open.spotify.com", "spotify.com",  # Streaming
    "music.apple.com", "itunes.apple.com",  # Streaming
    "tidal.com",  # Streaming
    "soundcloud.com",  # Streaming (most are personal tracks)
    "instagram.com", "www.instagram.com",  # Social
    "tiktok.com", "www.tiktok.com", "vm.tiktok.com",  # Social
    "twitter.com", "x.com",  # Social
    "facebook.com", "www.facebook.com", "m.facebook.com",  # Social
    "discord.com", "discord.gg", "discordapp.com",  # Discord internal
    "cdn.discordapp.com",  # Discord CDN (images handled separately)
    "images-ext-1.discordapp.net", "images-ext-2.discordapp.net",  # Discord proxied
    "media.discordapp.net",  # Discord media
    "cdn.jsdelivr.net",  # Emoji CDN
}

# Domain categorization
DOMAIN_CATEGORIES = {
    "youtube": ["youtube.com", "youtu.be", "m.youtube.com"],
    "dropbox": ["dropbox.com", "dl.dropboxusercontent.com"],
    "reverb": ["reverb.com"],
    "sweetwater": ["sweetwater.com"],
    "articles": [
        "soundonsound.com", "tapeop.com", "gearspace.com",
        "gearslutz.com",  # old name for gearspace
        "wikipedia.org", "en.wikipedia.org",
        "prosoundweb.com", "recordingmag.com",
        "mixonline.com", "eqmag.com",
        "behind-the-mixer.com",
    ],
    "gear-marketplace": [
        "bhphotovideo.com", "amazon.com", "ebay.com",
        "guitarcenter.com", "musiciansfriend.com",
        "zzounds.com", "adorama.com",
        "vintageking.com", "atlasproaudio.com",
    ],
    "manufacturer": [
        "neumann.com", "shure.com", "sennheiser.com",
        "audio-technica.com", "akg.com", "beyerdynamic.com",
        "royer.com", "warm-audio.com", "universalaudio.com",
        "slate digital.com", "waves.com",
        "api.com", "apiaudio.com",
        "rupert neve designs", "rupertneve.com",
        "bae-audio.com", "chandlerltd.com",
        "focusrite.com", "audient.com", "presonus.com",
        "avid.com",
    ],
}

# Wiki page mapping for link distribution
TOPIC_KEYWORDS = {
    "Topics/Recording/Drum Recording Techniques.md": [
        "drum", "snare", "kick", "overhead", "cymbal", "hi-hat", "tom",
        "room mic", "drum overhead", "drum recording", "kit",
    ],
    "Topics/Recording/Guitar Recording.md": [
        "guitar", "amp", "cabinet", "cab", "sm57", "ribbon", "electric guitar",
        "acoustic guitar", "guitar recording", "guitar tone", "pedal",
    ],
    "Topics/Recording/Vocal Recording.md": [
        "vocal", "voice", "singer", "singing", "vocal chain", "pop filter",
        "de-ess", "vocal recording", "mic technique vocal",
    ],
    "Topics/Recording/Bass Recording.md": [
        "bass", "bass guitar", "bass di", "bass amp", "bass recording",
        "bass tone",
    ],
    "Topics/Recording/Piano and Keys Recording.md": [
        "piano", "keys", "keyboard", "rhodes", "wurlitzer", "organ",
        "piano recording", "upright", "grand piano",
    ],
    "Topics/Recording/Stereo Miking Techniques.md": [
        "stereo", "xy", "ortf", "spaced pair", "blumlein", "mid-side",
        "stereo miking", "stereo technique", "stereo array",
    ],
    "Topics/Recording/Room Mics and Ambient Recording.md": [
        "room mic", "ambient", "room sound", "reverb", "room treatment",
        "acoustic treatment", "diffusion", "absorption",
    ],
    "Topics/Recording/Session Mindset and Engineering Philosophy.md": [
        "session", "engineer", "philosophy", "workflow", "client",
        "artist", "mindset", "professionalism", "career",
    ],
}


def extract_urls_from_content(content):
    """Extract URLs from message content text."""
    url_pattern = r'https?://[^\s<>\)\]\"\'`]+'
    urls = re.findall(url_pattern, content)
    # Clean trailing punctuation
    cleaned = []
    for url in urls:
        url = url.rstrip('.,;:!?)>')
        if url:
            cleaned.append(url)
    return cleaned


def extract_urls_from_embeds(embeds):
    """Extract URLs from message embeds."""
    urls = []
    for embed in embeds:
        if embed.get('url'):
            urls.append({
                'url': embed['url'],
                'title': embed.get('title', ''),
                'description': embed.get('description', ''),
            })
    return urls


def get_domain(url):
    """Extract domain from URL."""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain
    except Exception:
        return ""


def should_skip(url):
    """Check if URL should be skipped."""
    domain = get_domain(url)
    return domain in SKIP_DOMAINS


def categorize_url(url):
    """Categorize a URL by its domain."""
    domain = get_domain(url)
    for category, domains in DOMAIN_CATEGORIES.items():
        for d in domains:
            if d in domain:
                return category
    return "other"


def map_to_wiki_page(content, url, embed_title=""):
    """Determine which wiki page a link is most relevant to."""
    combined = f"{content} {embed_title}".lower()

    scores = {}
    for page, keywords in TOPIC_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in combined)
        if score > 0:
            scores[page] = score

    if scores:
        return max(scores, key=scores.get)
    return None


def main():
    print("Loading JSON data...")
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    messages = data['messages']
    print(f"Total messages: {len(messages)}")

    # Extract all links
    print("\nExtracting links...")
    all_links = []
    seen_urls = set()

    for msg in messages:
        content = msg.get('content', '') or ''
        author = msg['author'].get('nickname') or msg['author']['name']
        date = msg['timestamp'][:10]
        msg_id = msg['id']

        # From content text
        for url in extract_urls_from_content(content):
            if url not in seen_urls and not should_skip(url):
                seen_urls.add(url)
                all_links.append({
                    'url': url,
                    'title': '',
                    'embed_description': '',
                    'author': author,
                    'date': date,
                    'message_content': content[:300],
                    'message_id': msg_id,
                    'source': 'content',
                    'category': categorize_url(url),
                    'wiki_page': map_to_wiki_page(content, url),
                })

        # From embeds
        for embed_info in extract_urls_from_embeds(msg.get('embeds', [])):
            url = embed_info['url']
            if url not in seen_urls and not should_skip(url):
                seen_urls.add(url)
                all_links.append({
                    'url': url,
                    'title': embed_info['title'],
                    'embed_description': embed_info['description'],
                    'author': author,
                    'date': date,
                    'message_content': content[:300],
                    'message_id': msg_id,
                    'source': 'embed',
                    'category': categorize_url(url),
                    'wiki_page': map_to_wiki_page(content, url, embed_info['title']),
                })

    # Also count skipped for stats
    skipped_counts = defaultdict(int)
    for msg in messages:
        content = msg.get('content', '') or ''
        for url in extract_urls_from_content(content):
            if should_skip(url):
                skipped_counts[get_domain(url)] += 1
        for embed in msg.get('embeds', []):
            if embed.get('url') and should_skip(embed['url']):
                skipped_counts[get_domain(embed['url'])] += 1

    print(f"\nExtracted {len(all_links)} relevant links")
    print(f"Skipped domains:")
    for domain, count in sorted(skipped_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            print(f"  {domain}: {count}")

    # Category breakdown
    cat_counts = defaultdict(int)
    for link in all_links:
        cat_counts[link['category']] += 1
    print(f"\nBy category:")
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")

    # Sort by category then date
    all_links.sort(key=lambda x: (x['category'], x['date']))

    # Write master External Resources page
    resources_path = os.path.join(VAULT_PATH, "Sources", "External Resources from recording-talk.md")
    print(f"\nWriting External Resources page...")

    with open(resources_path, 'w') as f:
        f.write("---\n")
        f.write("type: index\n")
        f.write(f"created: {time.strftime('%Y-%m-%d')}\n")
        f.write(f"total_links: {len(all_links)}\n")
        f.write("tags: [type/index, source/recording-talk]\n")
        f.write("---\n\n")
        f.write("# External Resources from recording-talk\n\n")
        f.write("Links shared in the #recording-talk channel, organized by category.\n\n")
        f.write(f"**Total links:** {len(all_links)}\n\n")

        # YouTube section
        yt_links = [l for l in all_links if l['category'] == 'youtube']
        if yt_links:
            f.write(f"## YouTube Videos & Tutorials ({len(yt_links)})\n\n")
            for link in yt_links:
                title = link['title'] or link['url']
                f.write(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})")
                if link['message_content'] and link['title']:
                    # Add brief context if message had text beyond just the URL
                    ctx = link['message_content'].replace(link['url'], '').strip()
                    if ctx and len(ctx) > 10:
                        ctx = ctx[:120].rstrip()
                        if len(link['message_content']) > 130:
                            ctx += "..."
                        f.write(f"\n  - *{ctx}*")
                f.write("\n")
            f.write("\n")

        # Dropbox section
        db_links = [l for l in all_links if l['category'] == 'dropbox']
        if db_links:
            f.write(f"## Audio Samples & Shootouts ({len(db_links)})\n\n")
            for link in db_links:
                title = link['title'] or link['url']
                f.write(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})")
                if link['message_content']:
                    ctx = link['message_content'].replace(link['url'], '').strip()[:120]
                    if ctx and len(ctx) > 10:
                        f.write(f"\n  - *{ctx}*")
                f.write("\n")
            f.write("\n")

        # Gear listings (Reverb + Sweetwater + marketplace)
        gear_links = [l for l in all_links if l['category'] in ('reverb', 'sweetwater', 'gear-marketplace')]
        if gear_links:
            f.write(f"## Gear Listings & Reviews ({len(gear_links)})\n\n")
            for link in gear_links:
                title = link['title'] or link['url']
                source = link['category'].title()
                f.write(f"- [{title}]({link['url']}) — {source} — shared by {link['author']} ({link['date']})\n")
            f.write("\n")

        # Articles
        art_links = [l for l in all_links if l['category'] == 'articles']
        if art_links:
            f.write(f"## Articles & References ({len(art_links)})\n\n")
            for link in art_links:
                title = link['title'] or link['url']
                f.write(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})\n")
            f.write("\n")

        # Manufacturer pages
        mfr_links = [l for l in all_links if l['category'] == 'manufacturer']
        if mfr_links:
            f.write(f"## Manufacturer Pages ({len(mfr_links)})\n\n")
            for link in mfr_links:
                title = link['title'] or link['url']
                f.write(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})\n")
            f.write("\n")

        # Other
        other_links = [l for l in all_links if l['category'] == 'other']
        if other_links:
            f.write(f"## Other Resources ({len(other_links)})\n\n")
            for link in other_links:
                title = link['title'] or link['url']
                f.write(f"- [{title}]({link['url']}) — shared by {link['author']} ({link['date']})\n")
            f.write("\n")

    print(f"External Resources page written to {resources_path}")

    # Write JSON mapping for distribution script
    mapping_path = os.path.join(VAULT_PATH, "Assets", "recording-talk", "_link-mapping.json")
    with open(mapping_path, 'w') as f:
        json.dump(all_links, f, indent=2)
    print(f"Link mapping JSON written to {mapping_path}")

    # Print wiki page distribution
    page_counts = defaultdict(int)
    for link in all_links:
        if link['wiki_page']:
            page_counts[link['wiki_page']] += 1
    print(f"\nLinks mapped to wiki pages:")
    for page, count in sorted(page_counts.items(), key=lambda x: -x[1]):
        print(f"  {page}: {count}")
    unmapped = sum(1 for l in all_links if not l['wiki_page'])
    print(f"  (unmapped): {unmapped}")

    return len(all_links)


if __name__ == "__main__":
    main()
