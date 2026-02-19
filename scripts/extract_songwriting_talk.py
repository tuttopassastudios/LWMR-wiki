#!/usr/bin/env python3
"""Extract and categorize messages from #songwriting-talk Discord channel."""

import json
import re
from collections import defaultdict
from pathlib import Path

VAULT = Path("/Users/tylerchase/Documents/Discord Wikipedia")
JSON_PATH = Path("/Users/tylerchase/Downloads/Live with Matt Rad - MUSIC - ✍songwriting-talk [827573978578026496].json")
OUTPUT_DIR = VAULT / "scripts" / "_songwriting-talk-extract"

CATEGORIES = {
    "lyrics_lyric_writing": {
        "label": "Lyrics & Lyric Writing",
        "keywords": [
            "lyric", "rhyme", "storytell", "metaphor", "vulnerab",
            "honest", "emotion", "word", "phrase", "pen ",
            "write a song", "writing a song", "incriminate",
            "journal", "diary", "poetry", "poet ",
        ],
    },
    "melody_hooks": {
        "label": "Melody & Hooks",
        "keywords": [
            "melody", "melodi", "hook", "topline", "catchy",
            "earworm", "melodic", "hum ", "humm", "sing along",
            "singable", "tune ", "vocal melody",
        ],
    },
    "chord_progressions_harmony": {
        "label": "Chord Progressions & Harmony",
        "keywords": [
            " chord", "progression", "harmony", " key ",
            " scale ", "modulate", "modulation", "minor ",
            "major ", "interval", "voicing", "inversion",
            "substitut", "circle of fifth", "transpose",
        ],
    },
    "song_structure_form": {
        "label": "Song Structure & Form",
        "keywords": [
            "structure", "verse", "chorus", "bridge",
            "pre-chorus", "prechorus", "arrangement", " section",
            "song form", " intro ", " outro", "interlude",
        ],
    },
    "creative_process_workflow": {
        "label": "Creative Process & Workflow",
        "keywords": [
            "process", "routine", "writer's block", "writers block",
            "inspiration", "exercise", "habit", "discipline",
            "morning", "daily", "practice", "brainstorm",
            "creative block", "stuck ", "unfinish",
        ],
    },
    "cowriting_collaboration": {
        "label": "Co-Writing & Collaboration",
        "keywords": [
            "co-writ", "cowrit", "collaborat", "writing session",
            "writing room", "writing camp", "co write", "cowrite",
            "writing partner", "session ", "topliner",
            "writing team", "camp ",
        ],
    },
    "demos_song_production": {
        "label": "Demos & Song Production",
        "keywords": [
            " demo ", "sketch", "produce", " beat ",
            "instrumental", "track ", "production", "producer",
            "arrangement", "produce a song", "work tape",
        ],
    },
    "vocal_performance_delivery": {
        "label": "Vocal Performance & Delivery",
        "keywords": [
            "vocal", "voice", "singer", "phrasing",
            "delivery", " range", "sing ", "singing",
            "performance", "breath", "tone ", "vibrato",
            "falsetto", "head voice", "chest voice",
        ],
    },
    "references_study_learning": {
        "label": "References, Study & Learning",
        "keywords": [
            "reference", " study", " book ", "masterclass",
            "documentary", " learn", "course", "lesson",
            "mentor", "workshop", "tutorial", "analyze",
            "deconstruct", "transcrib",
        ],
    },
    "genre_style": {
        "label": "Genre & Style",
        "keywords": [
            " pop ", " rock ", "country", " r&b",
            "hip hop", "hip-hop", " folk ", " soul ",
            " blues", " indie ", " punk ", "singer-songwriter",
            "singer songwriter", "americana", "gospel",
        ],
    },
    "instrument_composition": {
        "label": "Instrument-Based Composition",
        "keywords": [
            "piano", "guitar", "keyboard", "instrument",
            " play ", "playing", "fingerpick", "strum",
            "acoustic", "ukulele", "loop pedal",
        ],
    },
    "publishing_business": {
        "label": "Publishing & Songwriting Business",
        "keywords": [
            "publish", "royalt", " sync ", "licensing",
            " ascap", " bmi ", " sesac", "split",
            "copyright", " deal ", "contract", "catalog",
            "pitch ", "pitching", "cut ", "placement",
        ],
    },
}


def get_author(msg):
    return msg["author"].get("nickname") or msg["author"]["name"]


def get_reactions(msg):
    return sum(r.get("count", 1) for r in msg.get("reactions", []))


def is_noise(msg):
    """Filter noise: bot messages, short messages, GIF-only, emoji-only."""
    content = msg.get("content", "")
    author = msg.get("author", {})

    if author.get("isBot", False):
        return True

    if len(content) < 20:
        return True

    stripped = content.strip()
    if re.match(r'^https?://(tenor\.com|giphy\.com|media\d?\.giphy\.com)/\S+$', stripped):
        return True

    emoji_pattern = re.compile(
        r'^[\s\U0001F600-\U0001F64F\U0001F300-\U0001F5FF'
        r'\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF'
        r'\U00002702-\U000027B0\U000024C2-\U0001F251'
        r'\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F'
        r'\U0001FA70-\U0001FAFF\U00002600-\U000026FF'
        r'\U0000FE00-\U0000FE0F\U0000200D]+$'
    )
    if emoji_pattern.match(stripped):
        return True

    return False


def categorize_message(content):
    content_lower = content.lower()
    matched = []
    for cat_key, cat_info in CATEGORIES.items():
        for kw in cat_info["keywords"]:
            if kw in content_lower:
                matched.append(cat_key)
                break
    return matched


def main():
    print("=== #songwriting-talk Extraction Pipeline ===\n")

    with open(JSON_PATH) as f:
        data = json.load(f)
    messages = data["messages"]
    print(f"Total messages: {len(messages)}")

    # Date range
    dates = [m["timestamp"][:10] for m in messages]
    print(f"Date range: {min(dates)} to {max(dates)}")

    # Filter noise
    substantive = [m for m in messages if not is_noise(m)]
    print(f"Substantive (non-noise): {len(substantive)}")
    print(f"Noise filtered: {len(messages) - len(substantive)}")

    # Activity by year
    year_counts = defaultdict(int)
    for m in messages:
        year_counts[m["timestamp"][:4]] += 1
    print(f"\nActivity by year: {dict(sorted(year_counts.items()))}")

    # Unique authors
    authors = defaultdict(lambda: {"count": 0, "substantive": 0, "chars": 0, "reactions": 0, "topics": defaultdict(int)})
    for m in messages:
        a = get_author(m)
        authors[a]["count"] += 1
        authors[a]["reactions"] += get_reactions(m)
        if not is_noise(m):
            authors[a]["substantive"] += 1
            authors[a]["chars"] += len(m.get("content", ""))
            cats = categorize_message(m.get("content", ""))
            for cat in cats:
                authors[a]["topics"][cat] += 1
    print(f"Unique authors: {len(authors)}")

    # Top authors by substantive messages
    top_authors = sorted(authors.items(), key=lambda x: x[1]["substantive"], reverse=True)[:30]
    print(f"\nTop 30 authors by substantive messages:")
    print(f"{'Author':<28} {'Total':>6} {'Subst':>6} {'Subst%':>6} {'Avg Len':>8} {'React':>6} {'Top Topics'}")
    for name, stats in top_authors:
        avg_len = stats["chars"] // max(stats["substantive"], 1)
        subst_pct = (stats["substantive"] / max(stats["count"], 1)) * 100
        top_topics = sorted(stats["topics"].items(), key=lambda x: -x[1])[:3]
        topic_str = ", ".join(f"{t[0]}({t[1]})" for t in top_topics)
        print(f"{name[:27]:<28} {stats['count']:>6} {stats['substantive']:>6} {subst_pct:>5.0f}% {avg_len:>8} {stats['reactions']:>6} {topic_str}")

    # Categorize
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cat_messages = defaultdict(list)
    uncategorized = []
    total_categorized_msgs = set()

    for m in substantive:
        content = m.get("content", "")
        cats = categorize_message(content)
        entry = {
            "id": m["id"],
            "author": get_author(m),
            "date": m["timestamp"][:10],
            "content": content,
            "reactions": get_reactions(m),
            "attachments": len(m.get("attachments", [])),
            "is_pinned": m.get("isPinned", False),
        }
        if cats:
            total_categorized_msgs.add(m["id"])
            for cat in cats:
                cat_messages[cat].append(entry)
        else:
            uncategorized.append(entry)

    print(f"\nCategory breakdown:")
    total_cat_entries = 0
    for cat_key, cat_info in CATEGORIES.items():
        count = len(cat_messages[cat_key])
        total_cat_entries += count
        print(f"  {cat_info['label']:<40} {count:>6}")
    print(f"  {'Uncategorized':<40} {len(uncategorized):>6}")
    print(f"  Unique messages categorized: {len(total_categorized_msgs)}")
    print(f"  Total category entries: {total_cat_entries} (includes multi-category)")

    # Save categorized bundles
    for cat_key in CATEGORIES:
        msgs = cat_messages[cat_key]
        msgs.sort(key=lambda x: x["reactions"], reverse=True)
        outpath = OUTPUT_DIR / f"{cat_key}.json"
        with open(outpath, "w") as f:
            json.dump(msgs, f, indent=2)

    # Save uncategorized
    with open(OUTPUT_DIR / "uncategorized.json", "w") as f:
        json.dump(uncategorized, f, indent=2)

    # Pinned messages
    pinned = [m for m in messages if m.get("isPinned")]
    print(f"\nPinned messages: {len(pinned)}")
    for p in pinned:
        print(f"  {get_author(p)} ({p['timestamp'][:10]}): {p.get('content','')[:150]}")

    # High-reaction messages
    reacted = [(m, get_reactions(m)) for m in substantive]
    reacted.sort(key=lambda x: x[1], reverse=True)
    print(f"\nTop 30 most-reacted substantive messages:")
    for m, r in reacted[:30]:
        print(f"  [{r:>3} reactions] {get_author(m):<25} ({m['timestamp'][:10]}): {m.get('content','')[:120]}")

    top_reacted = []
    for m, r in reacted[:100]:
        top_reacted.append({
            "id": m["id"],
            "author": get_author(m),
            "date": m["timestamp"][:10],
            "content": m.get("content", ""),
            "reactions": r,
            "categories": categorize_message(m.get("content", "")),
        })
    with open(OUTPUT_DIR / "top_reacted.json", "w") as f:
        json.dump(top_reacted, f, indent=2)

    # Save author stats
    author_list = []
    for name, stats in top_authors:
        avg_len = stats["chars"] // max(stats["substantive"], 1)
        subst_pct = (stats["substantive"] / max(stats["count"], 1)) * 100
        top_topics = sorted(stats["topics"].items(), key=lambda x: -x[1])[:5]
        author_list.append({
            "name": name,
            "total": stats["count"],
            "substantive": stats["substantive"],
            "substantive_pct": round(subst_pct, 1),
            "avg_length": avg_len,
            "reactions": stats["reactions"],
            "top_topics": {t[0]: t[1] for t in top_topics},
        })
    with open(OUTPUT_DIR / "author_stats.json", "w") as f:
        json.dump(author_list, f, indent=2)

    # Per-category top quotes
    print("\n=== Top Quotes Per Category (for vault enrichment) ===")
    for cat_key, cat_info in CATEGORIES.items():
        msgs = cat_messages[cat_key]
        if not msgs:
            continue
        print(f"\n--- {cat_info['label']} ---")
        for m in msgs[:5]:
            print(f"  [{m['reactions']} react] {m['author']} ({m['date']}): {m['content'][:200]}")

    # Save category summary
    summary = {
        "total_messages": len(messages),
        "date_range": f"{min(dates)} to {max(dates)}",
        "substantive_messages": len(substantive),
        "noise_filtered": len(messages) - len(substantive),
        "unique_authors": len(authors),
        "unique_messages_categorized": len(total_categorized_msgs),
        "uncategorized": len(uncategorized),
        "activity_by_year": dict(sorted(year_counts.items())),
        "categories": {
            cat_key: {
                "label": cat_info["label"],
                "count": len(cat_messages[cat_key]),
            }
            for cat_key, cat_info in CATEGORIES.items()
        },
        "pinned_count": len(pinned),
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print("\n=== Extraction complete ===")
    print(f"Output saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
