#!/usr/bin/env python3
"""Extract and categorize messages from #mixing-talk Discord channel."""

import json
import re
from collections import defaultdict
from pathlib import Path

VAULT = Path("/Users/tylerchase/Documents/Discord Wikipedia")
JSON_PATH = Path("/Users/tylerchase/Downloads/Live with Matt Rad - MUSIC - 👩🍳mixing-talk [875949045078691840].json")
OUTPUT_DIR = VAULT / "Extracts" / "mixing-talk"

CATEGORIES = {
    "compression_techniques": {
        "label": "Compression Techniques",
        "keywords": [
            "compressor", "compress", "ratio", "threshold", "attack time",
            "release time", "knee", "vca compressor", "opto", "optical compressor",
            "fet compressor", "variable mu", "vari-mu", "parallel compress",
            "sidechain compress", "multiband compress", "bus compress",
            "1176", "la-2a", "la2a", "distressor", "ssl comp", "api 2500",
            "shadow hills", "fairchild", "manley vari",
            "pumping", "breathing", "glue", "squash",
        ],
    },
    "eq_techniques": {
        "label": "EQ Techniques",
        "keywords": [
            " eq ", "equaliz", "frequency", "high-pass", "high pass", "hpf",
            "low-pass", "low pass", "lpf", "shelf", "bell curve", "notch",
            "resonance", "mid-side eq", "m/s eq", "pultec", "fabfilter pro-q",
            "pro-q", "maag", "neve eq", "ssl eq", "api eq",
            "parametric", "graphic eq", "dynamic eq", "surgical eq",
            "boost and cut", "subtractive eq", "additive eq",
        ],
    },
    "reverb_delay": {
        "label": "Reverb & Delay",
        "keywords": [
            "reverb", "delay", "echo", " room ", "hall reverb", "plate reverb",
            "spring reverb", "pre-delay", "predelay", "decay time",
            "send and return", "wet/dry", "wet dry", "lexicon",
            "valhalla", "eventide", "altiverb", "fabfilter pro-r",
            "ir reverb", "impulse response", "convolution",
            "slapback", "tape delay", "ping pong", "echoboy",
            "h-delay", "timeless", "soundtoys echoboy",
        ],
    },
    "saturation_distortion": {
        "label": "Saturation & Distortion",
        "keywords": [
            "saturation", "distortion", "harmonic", "tape emulat",
            "clipping", "clipper", "warmth", "decapitator", "saturn",
            "analog emulat", "drive", "tube saturat", "tape machine",
            "studer", "ampex", "j37", "oxide", "soft clip", "hard clip",
            "grit", "heat",
        ],
    },
    "vocal_mixing": {
        "label": "Vocal Mixing",
        "keywords": [
            "vocal", "voice", "singer", "de-ess", "deess", "sibilance",
            "doubles", "ad-lib", "adlib", "vocal bus", "vocal chain",
            "autotune", "auto-tune", "pitch correct", "melodyne",
            "vocal plate", "vocal reverb", "vocal delay", "vocal eq",
            "vocal compress", "breath control", "vocal ride",
            "lead vocal", "background vocal", "backing vocal", "bgv",
        ],
    },
    "drum_mixing": {
        "label": "Drum Mixing",
        "keywords": [
            "drum mix", "kick drum", "snare", "hi-hat", "hihat",
            "overhead", " tom ", "toms ", "cymbal", "drum bus",
            "parallel drum", "sample replace", "sample augment",
            "drum compress", "drum eq", "drum sound", "drum transient",
            "trigger", "slate trigger", "kick and snare",
            "room mic", "drum room", "crush",
        ],
    },
    "bass_mixing": {
        "label": "Bass Mixing",
        "keywords": [
            "bass mix", "sub bass", "low end", "bass guitar",
            " 808", "di bass", "bass di", "bass amp", "bass tone",
            "bass compress", "bass eq",
        ],
    },
    "mix_bus": {
        "label": "Mix Bus / Master Bus",
        "keywords": [
            "mix bus", "mixbus", "master bus", "masterbus",
            "2-bus", "two bus", "stereo bus", "bus chain",
            "bus compressor", "print chain", "master fader",
            "mix bus compress", "bus eq", "bus process",
        ],
    },
    "gain_staging_levels": {
        "label": "Gain Staging & Levels",
        "keywords": [
            "gain stag", "headroom", "clipping level", "peak level",
            " rms", " lufs", "loudness", "metering", " vu ",
            "k-weighting", "true peak", "dbtp", "crest factor",
            "dynamic range", "loudness war",
        ],
    },
    "stereo_width": {
        "label": "Stereo & Width",
        "keywords": [
            "stereo imag", "mono compat", "width", "panning",
            "mid-side", "mid side", "m/s process", "haas effect",
            "imaging", "correlation", "stereo field", "auto-pan",
            "wider", "narrow",
        ],
    },
    "reference_translation": {
        "label": "Reference Mixing & Translation",
        "keywords": [
            "reference track", "reference mix", "translation",
            "car test", "phone test", "compare", " a/b ", "a/b test",
            "pink noise mix", "check on phone", "check in car",
            "earbuds", "laptop speaker", "tonal balance",
        ],
    },
    "automation": {
        "label": "Automation",
        "keywords": [
            "automation", "ride", "volume ride", "fader ride",
            "automate", "clip gain", "fader move",
            "pre-fader", "post-fader", "write mode", "latch mode",
        ],
    },
    "plugin_discussion": {
        "label": "Plugin Discussion",
        "keywords": [
            "plugin", "plug-in", " uad ", "universal audio plugin",
            " waves ", "fabfilter", "soundtoys", "slate digital",
            "izotope", "acustica", "plugin alliance", "brainworx",
            "softube", "arturia", "native instrument", "kilohearts",
            "analog obsession", "tokyo dawn",
        ],
    },
    "monitoring_listening": {
        "label": "Monitoring & Listening",
        "keywords": [
            "monitors", "headphone", " room ", "calibrat",
            "soundid", "sonarworks", "mixcube", "avantone",
            "ns-10", "ns10", "volume level", "listening level",
            "mix volume", "fletcher munson", "equal loudness",
        ],
    },
    "genre_specific": {
        "label": "Genre-Specific Mixing",
        "keywords": [
            "hip-hop mix", "hip hop mix", "rock mix", "pop mix",
            "metal mix", "country mix", "r&b mix", "rnb mix",
            "edm mix", "jazz mix", "indie mix", "punk mix",
            "genre", "style of mix",
        ],
    },
    "low_end_management": {
        "label": "Low End Management",
        "keywords": [
            "low end", "sub", "bass", "rumble", "high-pass", "high pass",
            "hpf", " mud", "muddy", "boxy", "boom", "woof",
            "kick bass", "bass and kick", "frequency pocket",
            "low frequency", "sub energy",
        ],
    },
    "mix_workflow": {
        "label": "Mix Workflow & Philosophy",
        "keywords": [
            "workflow", "philosophy", "template", "starting a mix",
            "start the mix", "approach", "order of operations",
            "mix routine", "mix process", "first thing i do",
            "how do you start", "mix strategy", "top-down",
            "bottom-up", "static mix",
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

    # Bot messages
    if author.get("isBot", False):
        return True

    # Short messages
    if len(content) < 20:
        return True

    # GIF-only (tenor/giphy links with no other content)
    stripped = content.strip()
    if re.match(r'^https?://(tenor\.com|giphy\.com|media\d?\.giphy\.com)/\S+$', stripped):
        return True

    # Emoji-only (only emoji characters and whitespace)
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
    print("=== #mixing-talk Extraction Pipeline ===\n")

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
        print(f"  {cat_info['label']:<35} {count:>6}")
    print(f"  {'Uncategorized':<35} {len(uncategorized):>6}")
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

    # Per-category top quotes (highest-reaction messages for vault content)
    print("\n=== Top Quotes Per Category (for vault enrichment) ===")
    for cat_key, cat_info in CATEGORIES.items():
        msgs = cat_messages[cat_key]
        if not msgs:
            continue
        print(f"\n--- {cat_info['label']} ---")
        for m in msgs[:5]:
            print(f"  [{m['reactions']} react] {m['author']} ({m['date']}): {m['content'][:200]}")

    # Save category summary for easy reference
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
