#!/usr/bin/env python3
"""Extract and categorize messages from #show-your-setup Discord channel."""

import json
import re
from collections import defaultdict
from pathlib import Path

VAULT = Path("/Users/tylerchase/Documents/Discord Wikipedia")
JSON_PATH = Path("/Users/tylerchase/Downloads/Live with Matt Rad - Studio - 📸show-your-setup [808407474944213003].json")
OUTPUT_DIR = VAULT / "Extracts" / "show-your-setup"
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}

CATEGORIES = {
    "monitor_speakers": {
        "label": "Monitor Speakers & Placement",
        "keywords": [
            "ns10", "ns-10", "genelec", "focal", "amphion", "augspurger",
            "barefoot", "atc", "dynaudio", "speaker placement", "monitor placement",
            "subwoofer", "neumann kh", "adam monitor", "adam a7", "adam s",
            "pmc", "kh310", "kh120", "kh150", "kh80",
            "avantone", "mixcube", "auratone", "mix cube",
            "tweeter", "woofer", "speaker stand", "iso pad",
            "near field", "nearfield", "midfield", "far field",
        ],
    },
    "acoustic_treatment": {
        "label": "Acoustic Treatment",
        "keywords": [
            "bass trap", "diffuser", "absorption", "rockwool", "owens corning",
            "gik", "primacoustic", "auralex", "tube trap", "attack wall",
            "reflection point", "first reflection", "room mode", "standing wave",
            "acoustic treatment", "acoustic panel", "foam", "mineral wool",
            "fiberglass", "absorber", "diffusion", "dead room", "live room treatment",
            "cloud panel", "ceiling cloud",
        ],
    },
    "studio_design": {
        "label": "Studio Design & Build",
        "keywords": [
            "studio build", "control room", "live room", "iso booth", "vocal booth",
            "room dimension", "floated floor", "double wall", "construction",
            "renovation", "studio design", "room layout", "floor plan",
            "building a studio", "built my studio", "building my studio",
            "machine room", "wiring", "conduit", "hvac", "ventilation",
            "sound lock", "air gap", "mass loaded vinyl", "mlv",
            "green glue", "resilient channel", "decoupl",
        ],
    },
    "furniture_ergonomics": {
        "label": "Studio Furniture & Ergonomics",
        "keywords": [
            "desk", "standing desk", "ergonomic", "chair", "argosy",
            "sterling modular", "omnirax", "herman miller", "aeron",
            "monitor arm", "screen", "keyboard tray", "sit stand",
            "studio furniture", "custom desk", "built a desk", "diy desk",
            "output platform", "studio desk",
        ],
    },
    "outboard_rack": {
        "label": "Outboard Rack Gear",
        "keywords": [
            "outboard", "rack", "500 series", "lunchbox", "patchbay",
            "summing box", "neve", "api ", "api-", "ssl ", "ssl-",
            "1073", "1176", "la-2a", "la2a", "distressor", "compressor",
            "preamp", "channel strip", "eq rack", "hardware insert",
            "bae", "warm audio", "shadow hills", "manley", "avalon",
            "dangerous", "grace design", "heritage audio",
        ],
    },
    "consoles": {
        "label": "Consoles",
        "keywords": [
            "console", "trident", "neotek", "mci", "soundcraft",
            "mixing desk", "8028", "4000", "9000", "toft", "allen heath",
            "allen & heath", "inline console", "split console",
            "summing mixer", "analog console",
        ],
    },
    "monitor_calibration": {
        "label": "Monitor Calibration & Room Correction",
        "keywords": [
            "sonarworks", "room correction", "calibrat", "rew ",
            "room eq wizard", "umik", "measurement mic",
            "arc system", "reference 4", "soundid", "dirac",
            "spl meter", "pink noise", "waterfall plot",
            "frequency response", "room measurement",
        ],
    },
    "instruments": {
        "label": "Guitars & Instruments",
        "keywords": [
            "guitar", "bass guitar", "fender", "gibson", "telecaster",
            "stratocaster", "les paul", "kemper", "axe fx", "axe-fx",
            "neural dsp", "amp ", "pedalboard", "pedals", "pedal board",
            "piano", "rhodes", "wurlitzer", "synth", "moog", "juno",
            "prophet", "keyboard", "drum kit", "drum set", "cymbals",
            "snare", "kick drum", "hi-hat", "violin", "cello",
            "upright bass", "acoustic guitar", "electric guitar",
        ],
    },
    "lighting_aesthetics": {
        "label": "Studio Lighting & Aesthetics",
        "keywords": [
            "lighting", "led", "rgb", "neon", "vibe", "aesthetic",
            "hue", "nanoleaf", "lamp", "ambient light", "backlight",
            "mood lighting",
        ],
    },
    "monitor_controllers": {
        "label": "Monitor Controllers",
        "keywords": [
            "monitor controller", "dangerous music", "grace design m",
            "crane song", "audient nero", "coleman", "presonus monitor",
            "mackie big knob", "tc electronic level pilot",
        ],
    },
}


def get_author(msg):
    return msg["author"].get("nickname") or msg["author"]["name"]


def get_reactions(msg):
    return sum(r.get("count", 1) for r in msg.get("reactions", []))


def categorize_message(content):
    content_lower = content.lower()
    matched = []
    for cat_key, cat_info in CATEGORIES.items():
        for kw in cat_info["keywords"]:
            if kw in content_lower:
                matched.append(cat_key)
                break
    return matched


def extract_images(messages):
    """Extract image attachment metadata (no downloading)."""
    images = []
    for msg in messages:
        for att in msg.get("attachments", []):
            fname = att.get("fileName", "")
            if not any(fname.lower().endswith(ext) for ext in IMAGE_EXTS):
                continue
            images.append({
                "filename": fname,
                "url": att["url"],
                "author": get_author(msg),
                "date": msg["timestamp"][:10],
                "message_content": msg.get("content", "")[:300],
                "message_id": msg["id"],
                "reactions": get_reactions(msg),
            })
    return images


def main():
    print("=== #show-your-setup Extraction Pipeline ===\n")

    with open(JSON_PATH) as f:
        data = json.load(f)
    messages = data["messages"]
    print(f"Total messages: {len(messages)}")

    # Filter substantive
    substantive = [m for m in messages if len(m.get("content", "")) >= 40]
    print(f"Substantive (40+ chars): {len(substantive)}")

    # Unique authors
    authors = defaultdict(lambda: {"count": 0, "substantive": 0, "chars": 0, "reactions": 0})
    for m in messages:
        a = get_author(m)
        authors[a]["count"] += 1
        authors[a]["reactions"] += get_reactions(m)
        if len(m.get("content", "")) >= 40:
            authors[a]["substantive"] += 1
            authors[a]["chars"] += len(m.get("content", ""))
    print(f"Unique authors: {len(authors)}")

    # Top authors by substantive messages
    top_authors = sorted(authors.items(), key=lambda x: x[1]["substantive"], reverse=True)[:25]
    print("\nTop 25 authors by substantive messages:")
    print(f"{'Author':<25} {'Total':>6} {'Subst':>6} {'Avg Len':>8} {'React':>6}")
    for name, stats in top_authors:
        avg_len = stats["chars"] // max(stats["substantive"], 1)
        print(f"{name[:24]:<25} {stats['count']:>6} {stats['substantive']:>6} {avg_len:>8} {stats['reactions']:>6}")

    # Categorize
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cat_messages = defaultdict(list)
    uncategorized = []

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
            for cat in cats:
                cat_messages[cat].append(entry)
        else:
            uncategorized.append(entry)

    print(f"\nCategory breakdown:")
    total_categorized = 0
    for cat_key, cat_info in CATEGORIES.items():
        count = len(cat_messages[cat_key])
        total_categorized += count
        print(f"  {cat_info['label']}: {count}")
    print(f"  Uncategorized: {len(uncategorized)}")
    print(f"  Total categorized messages: {total_categorized} (some in multiple categories)")

    # Save categorized bundles
    for cat_key in CATEGORIES:
        msgs = cat_messages[cat_key]
        # Sort by reactions descending
        msgs.sort(key=lambda x: x["reactions"], reverse=True)
        outpath = OUTPUT_DIR / f"{cat_key}.json"
        with open(outpath, "w") as f:
            json.dump(msgs, f, indent=2)
        print(f"  Saved: {outpath.name} ({len(msgs)} messages)")

    # Save uncategorized
    with open(OUTPUT_DIR / "uncategorized.json", "w") as f:
        json.dump(uncategorized, f, indent=2)

    # Extract images (metadata only)
    images = extract_images(messages)
    print(f"\nImage attachments: {len(images)}")
    with open(OUTPUT_DIR / "images.json", "w") as f:
        json.dump(images, f, indent=2)

    # Image categorization
    img_cats = defaultdict(list)
    for img in images:
        cats = categorize_message(img["message_content"])
        if not cats:
            img_cats["general_setup"].append(img)
        else:
            for c in cats:
                img_cats[c].append(img)

    print("\nImage category breakdown:")
    for cat, imgs in sorted(img_cats.items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(imgs)}")

    with open(OUTPUT_DIR / "images_categorized.json", "w") as f:
        json.dump({k: v for k, v in img_cats.items()}, f, indent=2)

    # Save author stats
    author_list = []
    for name, stats in top_authors:
        avg_len = stats["chars"] // max(stats["substantive"], 1)
        author_list.append({
            "name": name,
            "total": stats["count"],
            "substantive": stats["substantive"],
            "avg_length": avg_len,
            "reactions": stats["reactions"],
        })
    with open(OUTPUT_DIR / "author_stats.json", "w") as f:
        json.dump(author_list, f, indent=2)

    # Extract pinned messages
    pinned = [m for m in messages if m.get("isPinned")]
    print(f"\nPinned messages: {len(pinned)}")
    for p in pinned:
        print(f"  {get_author(p)} ({p['timestamp'][:10]}): {p.get('content','')[:100]}")

    # High-reaction messages
    reacted = [(m, get_reactions(m)) for m in substantive]
    reacted.sort(key=lambda x: x[1], reverse=True)
    print("\nTop 20 most-reacted substantive messages:")
    for m, r in reacted[:20]:
        print(f"  [{r} reactions] {get_author(m)} ({m['timestamp'][:10]}): {m.get('content','')[:100]}")

    top_reacted = []
    for m, r in reacted[:50]:
        top_reacted.append({
            "id": m["id"],
            "author": get_author(m),
            "date": m["timestamp"][:10],
            "content": m.get("content", ""),
            "reactions": r,
        })
    with open(OUTPUT_DIR / "top_reacted.json", "w") as f:
        json.dump(top_reacted, f, indent=2)

    print("\n=== Extraction complete ===")


if __name__ == "__main__":
    main()
