#!/usr/bin/env python3
"""Extract and categorize messages from #newbie-questions Discord channel.

Special focus on Q&A pair extraction — pairing beginner questions with
verified expert answers to build a FAQ that prevents repeat questions.
"""

import json
import re
from collections import defaultdict
from pathlib import Path

VAULT = Path("/Users/tylerchase/Documents/Discord Wikipedia")
JSON_PATH = Path("/Users/tylerchase/Downloads/Live with Matt Rad - MUSIC - 👼newbie-questions [809922920947646494].json")
OUTPUT_DIR = VAULT / "Extracts" / "newbie-questions"

# Only these users' answers are flagged as authoritative.
# Cross-referenced from Contributors.md and Processing Log across all channels.
VERIFIED_EXPERTS = {
    "oaklandmatt",
    "cian riordan",
    "Nomograph Mastering",
    "hyanrarvey",
    "Ross Fortune",
    "Slow Hand",
    "Jonathan Jetter",
    "NoahNeedleman",
    "chrissorem",
    "spectrummasters",
    "BatMeckley",
    "Adam Thein",
    "David Fuller",
    "Zack Hames",
    "peterlabberton",
    "ALXCPH",
    "Eric Martin",
    "bobby k",
    "Edward Rivera",
    "ehutton21",
    "Will Melones",
    "LAPhill",
    "Rollmottle",
    "Gerhard Westphalen",
    "Bryan DiMaio",
}

CATEGORIES = {
    "getting_started": {
        "label": "Getting Started",
        "keywords": [
            "where to start", "where do i start", "how to start",
            "how do i start", "first step", "getting started",
            "beginner", "newbie", "just starting", "brand new",
            "how to learn", "learning to mix", "learning to record",
            "how do i learn", "teach myself", "self-taught",
            "where to begin", "where should i begin", "starting out",
            "new to music", "new to audio", "new to recording",
            "new to mixing", "never mixed", "never recorded",
        ],
    },
    "monitoring_headphones": {
        "label": "Monitoring & Headphones",
        "keywords": [
            "monitor speaker", "studio monitor", "headphone",
            "nearfield", "mixing on headphone", "mix on headphone",
            "which monitors", "which headphone", "dt770", "dt990",
            "hd600", "hd650", "ath-m50", "akg k", "beyerdynamic",
            "sennheiser", "sony mdr", "audio-technica",
            "untreated room", "no treatment",
            "open back", "closed back", "reference headphone",
        ],
    },
    "microphone_selection": {
        "label": "Microphone Selection",
        "keywords": [
            "first mic", "budget mic", "cheap mic", "starter mic",
            "which mic", "what mic", "best mic", "mic for vocal",
            "condenser vs dynamic", "dynamic mic", "condenser mic",
            "sm58", "sm57", "sm7b", "at2020", "at2035",
            "rode nt1", "rode nt", "akg p", "mxl",
            "usb mic", "xlr mic", "mic technique", "mic placement",
            "pop filter", "shock mount", "mic stand",
        ],
    },
    "recording_basics": {
        "label": "Recording Basics",
        "keywords": [
            "recording level", "how to record", "record vocal",
            "recording vocal", "gain staging", "input level",
            "clipping", "peaking", "too hot", "too quiet",
            "room noise", "background noise", "noise floor",
            "reflection filter", "closet", "blanket",
            "record guitar", "recording guitar",
            "direct input", " di ", "line in",
        ],
    },
    "mixing_basics": {
        "label": "Mixing Basics",
        "keywords": [
            "how to mix", "mixing basics", "basic mix",
            " eq ", "equalize", "equalizer", "equalisation",
            "compressor", "compress", "compression",
            "panning", " pan ", "stereo image",
            "volume balance", "level balance", "static mix",
            "first mix", "start mixing",
            "what is eq", "what is compress",
            "high pass", "low pass", "high-pass", "low-pass",
        ],
    },
    "vocal_production": {
        "label": "Vocal Production",
        "keywords": [
            "vocal chain", "vocal processing", "vocal recording",
            "vocal plugin", "vocal preset", "vocal effect",
            "de-ess", "deess", "autotune", "auto-tune",
            "pitch correct", "vocal reverb", "vocal delay",
            "vocal eq", "vocal compress", "vocal mix",
            "double vocal", "doubles", "ad-lib", "adlib",
            "vocal bus", "vocal send", "vocal warm",
        ],
    },
    "gear_recommendations": {
        "label": "Gear Recommendations",
        "keywords": [
            "what gear", "which gear", "recommend", "suggestion",
            "budget gear", "affordable", "cheap",
            "first interface", "audio interface", "what interface",
            "which interface", "focusrite", "scarlett", "audient",
            "presonus", "motu", "universal audio", "apollo",
            "what to buy", "buy first", "first purchase",
            "upgrade", "worth it", "good enough",
        ],
    },
    "plugin_recommendations": {
        "label": "Plugin Recommendations",
        "keywords": [
            "free plugin", "best plugin", "which plugin",
            "stock plugin", "built-in plugin", "default plugin",
            "essential plugin", "must-have plugin",
            "plugin recommend", "plugin suggest",
            "paid plugin", "cheap plugin",
            "waves", "fabfilter", "izotope", "slate",
            "analog obsession", "tokyo dawn",
            "plugin alliance", "native instrument",
        ],
    },
    "daw_workflow": {
        "label": "DAW Workflow",
        "keywords": [
            "which daw", "what daw", "best daw", "daw for",
            "pro tools", "logic pro", "ableton", "fl studio",
            "reaper", "cubase", "studio one", "garageband",
            "daw template", "daw shortcut", "daw workflow",
            "switch daw", "learn daw", "free daw",
            "daw comparison", "daw recommend",
        ],
    },
    "mastering_basics": {
        "label": "Mastering Basics",
        "keywords": [
            "mastering", "master my", "how to master",
            "loudness", " lufs", "streaming level",
            "limiter", "limiting", "ceiling",
            "diy master", "master yourself", "self master",
            "spotify", "apple music", "soundcloud",
            "how loud", "too quiet on spotify",
            "distrokid", "tunecore", "cd baby", "landr",
        ],
    },
    "music_theory_arrangement": {
        "label": "Music Theory & Arrangement",
        "keywords": [
            "music theory", "chord", "scale", "key of",
            "arrangement", "song structure", "verse chorus",
            "songwriting", "melody", "harmony",
            "how to arrange", "instrumentat",
            "composition", "write a song", "writing music",
            "bridge", "intro", "outro", "hook",
            "tempo", "time signature", " bpm",
        ],
    },
    "career_learning": {
        "label": "Career & Learning",
        "keywords": [
            "career", "profession", "full-time", "full time",
            "make money", "get client", "find client",
            "practice", "how long does it take",
            "audio school", "recording school", "degree",
            "education", "course", "tutorial", "youtube",
            "mixing course", "online course",
            "intern", "assistant", "studio assistant",
            "portfolio", "demo reel",
            "work for free", "free mix", "exposure",
        ],
    },
    "file_management": {
        "label": "File Management",
        "keywords": [
            "stem", "bounce", "export",
            "file format", " wav ", " mp3 ", " aiff ",
            " flac ", "bit depth", "sample rate",
            "44.1", "48k", "96k", "24 bit", "16 bit",
            "file size", "storage", "backup",
            "send files", "deliver", "delivery",
            "google drive", "dropbox", "wetransfer",
        ],
    },
    "acoustic_treatment": {
        "label": "Acoustic Treatment",
        "keywords": [
            "acoustic treat", "room treat", "sound treat",
            "foam", "acoustic foam", "acoustic panel",
            "bass trap", "diffuser", "absorption",
            "reflection", "standing wave", "room mode",
            "rockwool", "owens corning", "diy panel",
            "closet booth", "vocal booth", "iso booth",
            "untreated", "no treatment",
            "mattress", "egg crate", "moving blanket",
        ],
    },
    "troubleshooting": {
        "label": "Troubleshooting",
        "keywords": [
            "latency", "delay when record", "lag",
            "noise", "hum", "buzz", "hiss",
            "click", "pop", "crackle", "glitch",
            "not working", "won't work", "doesn't work",
            "no sound", "can't hear", "no output",
            "driver", "asio", "core audio",
            "ground loop", "interference", "static",
            "buffer size", "dropout", "overload",
            "crash", "freeze", "hang",
        ],
    },
}


def get_author(msg):
    return msg["author"].get("nickname") or msg["author"]["name"]


def get_reactions(msg):
    return sum(r.get("count", 1) for r in msg.get("reactions", []))


def is_expert(author_name):
    return author_name in VERIFIED_EXPERTS


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


def is_question(content):
    """Check if a message is likely a question."""
    if "?" in content:
        return True
    lower = content.lower()
    question_starters = [
        "how do", "how can", "how should", "how would",
        "what is", "what are", "what does", "what do",
        "which", "where do", "where can", "where should",
        "why do", "why does", "why is", "why are",
        "can i", "can you", "should i", "do i need",
        "is it", "is there", "does anyone", "has anyone",
        "any recommendation", "any suggestion", "any advice",
        "anyone know", "anyone have", "does it matter",
    ]
    return any(lower.startswith(q) or f" {q}" in lower[:80] for q in question_starters)


def categorize_message(content):
    content_lower = content.lower()
    matched = []
    for cat_key, cat_info in CATEGORIES.items():
        for kw in cat_info["keywords"]:
            if kw in content_lower:
                matched.append(cat_key)
                break
    return matched


def build_qa_pairs(messages):
    """Pair questions with nearby expert responses (within 10 messages)."""
    qa_pairs = []
    for i, msg in enumerate(messages):
        content = msg.get("content", "")
        if is_noise(msg):
            continue
        if not is_question(content):
            continue

        author = get_author(msg)
        question_entry = {
            "question_id": msg["id"],
            "question_author": author,
            "question_date": msg["timestamp"][:10],
            "question": content,
            "question_reactions": get_reactions(msg),
            "categories": categorize_message(content),
            "expert_answers": [],
            "community_answers": [],
        }

        # Look at next 10 messages for responses
        for j in range(i + 1, min(i + 11, len(messages))):
            resp = messages[j]
            if is_noise(resp):
                continue
            resp_author = get_author(resp)
            resp_content = resp.get("content", "")

            # Skip if it's another question (conversation moved on)
            if is_question(resp_content) and resp_author != author:
                break

            # Skip self-replies that are also questions
            if resp_author == author and is_question(resp_content):
                continue

            answer_entry = {
                "answer_id": resp["id"],
                "author": resp_author,
                "date": resp["timestamp"][:10],
                "content": resp_content,
                "reactions": get_reactions(resp),
                "is_expert": is_expert(resp_author),
            }

            if is_expert(resp_author):
                question_entry["expert_answers"].append(answer_entry)
            else:
                question_entry["community_answers"].append(answer_entry)

        # Only keep pairs that have at least one expert answer OR high-reaction community answer
        has_expert = len(question_entry["expert_answers"]) > 0
        has_endorsed = any(a["reactions"] >= 15 for a in question_entry["community_answers"])
        if has_expert or has_endorsed:
            qa_pairs.append(question_entry)

    return qa_pairs


def main():
    print("=== #newbie-questions Extraction Pipeline ===\n")

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
    authors = defaultdict(lambda: {"count": 0, "substantive": 0, "chars": 0, "reactions": 0, "topics": defaultdict(int), "is_expert": False})
    for m in messages:
        a = get_author(m)
        authors[a]["count"] += 1
        authors[a]["reactions"] += get_reactions(m)
        authors[a]["is_expert"] = is_expert(a)
        if not is_noise(m):
            authors[a]["substantive"] += 1
            authors[a]["chars"] += len(m.get("content", ""))
            cats = categorize_message(m.get("content", ""))
            for cat in cats:
                authors[a]["topics"][cat] += 1
    print(f"Unique authors: {len(authors)}")

    # Expert vs non-expert breakdown
    expert_msgs = sum(1 for m in substantive if is_expert(get_author(m)))
    print(f"Expert substantive messages: {expert_msgs}")
    print(f"Non-expert substantive messages: {len(substantive) - expert_msgs}")

    # Top authors by substantive messages
    top_authors = sorted(authors.items(), key=lambda x: x[1]["substantive"], reverse=True)[:30]
    print(f"\nTop 30 authors by substantive messages:")
    print(f"{'Author':<28} {'Expert':>6} {'Total':>6} {'Subst':>6} {'Subst%':>6} {'Avg Len':>8} {'React':>6} {'Top Topics'}")
    for name, stats in top_authors:
        avg_len = stats["chars"] // max(stats["substantive"], 1)
        subst_pct = (stats["substantive"] / max(stats["count"], 1)) * 100
        top_topics = sorted(stats["topics"].items(), key=lambda x: -x[1])[:3]
        topic_str = ", ".join(f"{t[0]}({t[1]})" for t in top_topics)
        expert_flag = "YES" if stats["is_expert"] else ""
        print(f"{name[:27]:<28} {expert_flag:>6} {stats['count']:>6} {stats['substantive']:>6} {subst_pct:>5.0f}% {avg_len:>8} {stats['reactions']:>6} {topic_str}")

    # Categorize
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cat_messages = defaultdict(list)
    uncategorized = []
    total_categorized_msgs = set()

    for m in substantive:
        content = m.get("content", "")
        author = get_author(m)
        cats = categorize_message(content)
        entry = {
            "id": m["id"],
            "author": author,
            "date": m["timestamp"][:10],
            "content": content,
            "reactions": get_reactions(m),
            "attachments": len(m.get("attachments", [])),
            "is_pinned": m.get("isPinned", False),
            "is_expert": is_expert(author),
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
        expert_count = sum(1 for m in cat_messages[cat_key] if m["is_expert"])
        total_cat_entries += count
        print(f"  {cat_info['label']:<35} {count:>6}  (expert: {expert_count})")
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

    # === Q&A Pair Extraction (PRIMARY DELIVERABLE) ===
    print(f"\n=== Q&A Pair Extraction ===")
    qa_pairs = build_qa_pairs(messages)
    print(f"Total Q&A pairs with expert/endorsed answers: {len(qa_pairs)}")

    # Sort by number of expert answers, then by question reactions
    qa_pairs.sort(key=lambda x: (len(x["expert_answers"]), x["question_reactions"]), reverse=True)

    with open(OUTPUT_DIR / "qa_pairs.json", "w") as f:
        json.dump(qa_pairs, f, indent=2)

    # Category breakdown of Q&A pairs
    qa_by_cat = defaultdict(int)
    for qa in qa_pairs:
        for cat in qa["categories"]:
            qa_by_cat[cat] += 1
        if not qa["categories"]:
            qa_by_cat["uncategorized"] += 1
    print(f"\nQ&A pairs by category:")
    for cat_key, cat_info in CATEGORIES.items():
        print(f"  {cat_info['label']:<35} {qa_by_cat[cat_key]:>6}")

    # Preview top Q&A pairs
    print(f"\nTop 15 Q&A pairs (by expert answer count):")
    for qa in qa_pairs[:15]:
        print(f"  Q: {qa['question_author']} ({qa['question_date']}): {qa['question'][:120]}")
        for ans in qa["expert_answers"][:2]:
            print(f"    A [{ans['reactions']} react] {ans['author']}: {ans['content'][:120]}")
        print()

    # === Expert Advice Extraction ===
    expert_messages = []
    for m in substantive:
        author = get_author(m)
        if is_expert(author):
            content = m.get("content", "")
            expert_messages.append({
                "id": m["id"],
                "author": author,
                "date": m["timestamp"][:10],
                "content": content,
                "reactions": get_reactions(m),
                "categories": categorize_message(content),
                "is_pinned": m.get("isPinned", False),
            })
    expert_messages.sort(key=lambda x: x["reactions"], reverse=True)
    with open(OUTPUT_DIR / "expert_advice.json", "w") as f:
        json.dump(expert_messages, f, indent=2)
    print(f"\nExpert advice messages saved: {len(expert_messages)}")

    # Pinned messages
    pinned = [m for m in messages if m.get("isPinned")]
    print(f"\nPinned messages: {len(pinned)}")
    for p in pinned:
        print(f"  [{get_reactions(p)} react] {get_author(p)} ({p['timestamp'][:10]}): {p.get('content','')[:150]}")

    # High-reaction messages
    reacted = [(m, get_reactions(m)) for m in substantive]
    reacted.sort(key=lambda x: x[1], reverse=True)
    print(f"\nTop 30 most-reacted substantive messages:")
    for m, r in reacted[:30]:
        author = get_author(m)
        expert_flag = " [EXPERT]" if is_expert(author) else ""
        print(f"  [{r:>3} reactions] {author:<25}{expert_flag} ({m['timestamp'][:10]}): {m.get('content','')[:120]}")

    top_reacted = []
    for m, r in reacted[:100]:
        author = get_author(m)
        top_reacted.append({
            "id": m["id"],
            "author": author,
            "date": m["timestamp"][:10],
            "content": m.get("content", ""),
            "reactions": r,
            "categories": categorize_message(m.get("content", "")),
            "is_expert": is_expert(author),
        })
    with open(OUTPUT_DIR / "top_reacted.json", "w") as f:
        json.dump(top_reacted, f, indent=2)

    # Save author stats
    author_list = []
    for name, stats in sorted(authors.items(), key=lambda x: x[1]["substantive"], reverse=True)[:50]:
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
            "is_expert": stats["is_expert"],
            "top_topics": {t[0]: t[1] for t in top_topics},
        })
    with open(OUTPUT_DIR / "author_stats.json", "w") as f:
        json.dump(author_list, f, indent=2)

    # Per-category top quotes (for vault enrichment)
    print("\n=== Top Expert Quotes Per Category (for vault enrichment) ===")
    for cat_key, cat_info in CATEGORIES.items():
        msgs = cat_messages[cat_key]
        expert_msgs = [m for m in msgs if m["is_expert"]]
        if not expert_msgs:
            print(f"\n--- {cat_info['label']} --- (no expert messages)")
            continue
        expert_msgs.sort(key=lambda x: x["reactions"], reverse=True)
        print(f"\n--- {cat_info['label']} ---")
        for m in expert_msgs[:5]:
            print(f"  [{m['reactions']} react] {m['author']} ({m['date']}): {m['content'][:200]}")

    # Save summary
    summary = {
        "total_messages": len(messages),
        "date_range": f"{min(dates)} to {max(dates)}",
        "substantive_messages": len(substantive),
        "noise_filtered": len(messages) - len(substantive),
        "unique_authors": len(authors),
        "unique_messages_categorized": len(total_categorized_msgs),
        "uncategorized": len(uncategorized),
        "expert_substantive_messages": expert_msgs,
        "qa_pairs_count": len(qa_pairs),
        "expert_advice_count": len(expert_messages),
        "activity_by_year": dict(sorted(year_counts.items())),
        "categories": {
            cat_key: {
                "label": cat_info["label"],
                "count": len(cat_messages[cat_key]),
                "expert_count": sum(1 for m in cat_messages[cat_key] if m["is_expert"]),
            }
            for cat_key, cat_info in CATEGORIES.items()
        },
        "pinned_count": len(pinned),
        "qa_pairs_by_category": dict(qa_by_cat),
    }
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print("\n=== Extraction complete ===")
    print(f"Output saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
