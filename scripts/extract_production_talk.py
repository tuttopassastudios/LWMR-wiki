#!/usr/bin/env python3
"""Extract and categorize messages from #production-talk Discord channel."""

import json
import re
from collections import defaultdict
from pathlib import Path

VAULT = Path("/Users/tylerchase/Documents/Discord Wikipedia")
JSON_PATH = Path("/Users/tylerchase/Downloads/Live with Matt Rad - MUSIC - 🎹production-talk [937549855524544532].json")
OUTPUT_DIR = VAULT / "scripts" / "_production-talk-extract"

CATEGORIES = {
    "songwriting_arrangement": {
        "label": "Songwriting & Arrangement",
        "keywords": [
            "songwrit", "song structure", "verse", "chorus", "bridge",
            "hook", "melody", "lyric", "chord progression", "song form",
            "pre-chorus", "prechorus", "outro", "intro ",
            "arrangement", "arrange ",
        ],
    },
    "sound_design_synthesis": {
        "label": "Sound Design & Synthesis",
        "keywords": [
            "sound design", "synth", "synthesizer", "oscillator", "wavetable",
            "subtractive", "fm synthesis", "granular", "serum", "vital ",
            "omnisphere", "preset", "patch ", "modular", "eurorack",
            "filter ", "envelope", " lfo", "modulation",
        ],
    },
    "sampling_libraries": {
        "label": "Sampling & Sample Libraries",
        "keywords": [
            "sample library", "kontakt", " 8dio", "spitfire", "eastwest",
            "splice", " loop ", "one-shot", "one shot", "sample pack",
            "drum kit", "sampler", "sample ", "chopping",
        ],
    },
    "midi_virtual_instruments": {
        "label": "MIDI & Virtual Instruments",
        "keywords": [
            " midi", "virtual instrument", " vst", " vsti",
            "keyscape", "piano vst", "alicia keys", "addictive keys",
            "superior drummer", "ezdrummer", "ez drummer",
            "battery ", "instrument rack", "articulation",
            "expression map", "velocity ",
        ],
    },
    "beat_making_drums": {
        "label": "Beat Making & Drum Programming",
        "keywords": [
            " beat ", "beat making", "beatmaking", "drum programming",
            "drum machine", " 808", "hi-hat", "hi hat",
            " kick ", " snare ", " trap ", "boom bap",
            " pattern", "quantize", "quantization",
            " swing", " groove", " mpc", "maschine",
            "drum rack", "drum pattern",
        ],
    },
    "bass_production": {
        "label": "Bass Production",
        "keywords": [
            " bass ", "sub bass", "sub-bass", "808 bass",
            "bass synth", "bass guitar", "bass tone",
            "low end", " sub ", "bass line", "bassline",
        ],
    },
    "vocal_production": {
        "label": "Vocal Production",
        "keywords": [
            "vocal", "autotune", "auto-tune", "auto tune",
            "pitch correct", "melodyne", "formant",
            "vocal chop", "vocal stack", "harmony",
            "double ", "ad-lib", "adlib", "vocal chain",
            "tuning", "vocal production",
        ],
    },
    "guitar_production": {
        "label": "Guitar Production",
        "keywords": [
            "guitar", "amp sim", "amp model", "neural dsp",
            " helix", " kemper", "guitar tone", "pedal",
            "reamping", "reamp", "di guitar",
            "electric guitar", "acoustic guitar",
        ],
    },
    "keys_piano": {
        "label": "Keys & Piano",
        "keywords": [
            "piano", " keys ", "keyboard", "rhodes",
            "wurlitzer", " organ", "keyscape",
            " nord ", "electric piano", "clavinet",
        ],
    },
    "genre_production": {
        "label": "Genre-Specific Production",
        "keywords": [
            "hip hop", "hip-hop", " r&b", " pop ",
            " rock ", "country", " edm ", "electronic",
            " trap ", "lo-fi", "lofi", " indie ",
            " metal", " jazz ", " soul ", " funk ",
            "genre ",
        ],
    },
    "production_workflow": {
        "label": "Production Workflow",
        "keywords": [
            "workflow", "template", "session", "organize",
            "arrange window", "project", " demo ",
            "rough mix", "production process", "creative process",
            "production workflow",
        ],
    },
    "music_theory": {
        "label": "Music Theory & Harmony",
        "keywords": [
            "music theory", " chord", " scale ", " key ",
            "harmony", "interval", "modal", " minor ",
            " major ", "transpose", "circle of fifths",
            "relative minor", "key change", "modulate",
        ],
    },
    "arrangement_orchestration": {
        "label": "Arrangement & Orchestration",
        "keywords": [
            "orchestrat", " string ", " brass ", " horn ",
            "woodwind", " section", " layer", " texture",
            " pad ", " score ", "compose", "composer",
            "arrangement", "arranging",
        ],
    },
    "creative_techniques": {
        "label": "Creative & Experimental Techniques",
        "keywords": [
            "creative", "experiment", " effect", "reverse ",
            "glitch", "stutter", " chop ", "pitch shift",
            "time stretch", "resample", "mangl", "distort",
            "bitcrush", "lo-fi effect",
        ],
    },
    "reference_inspiration": {
        "label": "References & Inspiration",
        "keywords": [
            "reference", "inspiration", "influence", " album ",
            " artist", " song ", " listen", " study ",
            "analyze", "deconstruct", "transcrib",
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
    print("=== #production-talk Extraction Pipeline ===\n")

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
