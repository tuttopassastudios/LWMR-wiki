# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Extract and categorize messages from #general-talk Discord channel.

The broadest channel on the server (52,236 messages) covering mixing philosophy,
career advice, mental health, learning resources, community culture, and more.

Features beyond standard extraction:
- 30 keyword categories in 3 tiers (existing domains, new domains, enrichment)
- Q&A pair extraction (borrowed from newbie-questions pattern)
- Resource extraction (URLs, images/attachments)
- Expert advice extraction with VERIFIED_EXPERTS list
"""

import json
import re
from collections import defaultdict
from pathlib import Path

VAULT = Path("/Users/tylerchase/Documents/Discord Wikipedia")
JSON_PATH = Path("/Users/tylerchase/Downloads/Live with Matt Rad - Community - 💬general-talk [800115582531928067].json")
OUTPUT_DIR = VAULT / "Extracts" / "general-talk"

# Combined from all previous scripts — cross-referenced from Contributors.md and Processing Log
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
    "masteredbyjack",
    "Berlin",
    "Edsel Holden",
    "hebakadry",
    "austenballard",
    "Josh",
    "Rob Domos",
}

# === TIER 1: Existing vault domains (15 categories) ===
# === TIER 2: New domains (10 categories) ===
# === TIER 3: Enrichment catch-alls (5 categories) ===

CATEGORIES = {
    # --- TIER 1: Existing vault domains ---
    "mixing_general": {
        "label": "Mixing (General)",
        "tier": 1,
        "keywords": [
            "mixing", "mix bus", "mixbus", "mix session", "mix revision",
            "mix note", "mix feedback", "submix", "stem mix",
            "mix reference", "mix translate", "static mix", "rough mix",
            "bus compress", "parallel compress", "vocal mix",
            "drum mix", "bass mix", "low end mix",
        ],
    },
    "mastering_general": {
        "label": "Mastering (General)",
        "tier": 1,
        "keywords": [
            "mastering", "master bus", "masterbus", "mastered",
            "limiter", "limiting", "ceiling", " lufs",
            "loudness", "true peak", "dither",
            "master chain", "mastering chain", "master session",
            "vinyl master", "streaming master",
        ],
    },
    "recording_general": {
        "label": "Recording (General)",
        "tier": 1,
        "keywords": [
            "recording", "tracking", "overdub", "punch in",
            "mic placement", "mic technique", "room mic",
            "preamp", "pre-amp", "gain staging",
            "record vocal", "recording vocal", "tracking session",
            "take", "comping", "comp take",
        ],
    },
    "production_general": {
        "label": "Production (General)",
        "tier": 1,
        "keywords": [
            "producing", "producer", "production", "arrangement",
            "beat making", "beatmaking", "drum programming",
            "sound design", "synth", "synthesizer",
            "sample pack", "sample library", "loop",
            "midi", "virtual instrument", "vst instrument",
        ],
    },
    "songwriting": {
        "label": "Songwriting",
        "tier": 1,
        "keywords": [
            "songwriting", "songwriter", "song writing",
            "lyric", "melody", "hook", "chorus",
            "verse", "bridge", "song structure",
            "co-writing", "co-write", "topliner", "topline",
            "write a song", "writing music", "writing session",
        ],
    },
    "daw_software": {
        "label": "DAW & Software",
        "tier": 1,
        "keywords": [
            " daw ", "pro tools", "logic pro", "ableton",
            "fl studio", "reaper", "cubase", "studio one",
            "garageband", "luna", "bitwig",
            "plugin", "plug-in", " vst ", " aax ", " au ",
            "software update", "software version",
        ],
    },
    "gear_hardware": {
        "label": "Gear & Hardware",
        "tier": 1,
        "keywords": [
            "interface", "audio interface", "converter",
            "preamp", "pre-amp", "outboard",
            "console", "mixing desk", "summing",
            "compressor hardware", "hardware eq",
            "mic pre", "500 series", "500-series",
            "patchbay", "patch bay",
            "apollo", "scarlett", "focusrite", "audient",
            "ssl", "neve", "api ", "rupert neve",
        ],
    },
    "acoustics_studio": {
        "label": "Acoustics & Studio",
        "tier": 1,
        "keywords": [
            "acoustic treat", "room treat", "bass trap",
            "diffuser", "absorption", "reflection",
            "standing wave", "room mode", "flutter echo",
            "studio build", "studio design", "control room",
            "isolation", "soundproof", "floating floor",
            "rockwool", "owens corning", "acoustic panel",
        ],
    },
    "atmos_immersive": {
        "label": "Atmos & Immersive",
        "tier": 1,
        "keywords": [
            "dolby atmos", "atmos", "immersive",
            "spatial audio", "binaural", "ambisonics",
            "7.1.4", "5.1.4", "object-based", "bed track",
            "apple spatial", "renderer",
        ],
    },
    "monitoring_listening": {
        "label": "Monitoring & Listening",
        "tier": 1,
        "keywords": [
            "monitor speaker", "studio monitor", "headphone",
            "nearfield", "midfield", "subwoofer",
            "ns-10", "ns10", "avantone", "mixcube",
            "sonarworks", "soundid", "reference headphone",
            "auratone", "yamaha hs", "adam audio", "genelec",
            "focal", "kali audio", "ik multimedia",
            "listening level", "mix volume", "calibrat",
        ],
    },
    "signal_flow": {
        "label": "Signal Flow",
        "tier": 1,
        "keywords": [
            "signal flow", "signal chain", "routing",
            " bus ", " aux ", "send and return",
            "insert", "parallel", "serial",
            "sidechain", "pre-fader", "post-fader",
            "gain structure", "i/o",
        ],
    },
    "troubleshooting": {
        "label": "Troubleshooting",
        "tier": 1,
        "keywords": [
            "latency", "buffer size", "dropout",
            "crash", "freeze", "glitch",
            "noise floor", "hum", "buzz", "hiss",
            "ground loop", "interference",
            "not working", "won't work", "doesn't work",
            "no sound", "can't hear",
            "driver", "asio", "core audio",
            "troubleshoot", "debug", "fix this",
        ],
    },
    "plugin_discussion": {
        "label": "Plugin Discussion",
        "tier": 1,
        "keywords": [
            "plugin", "plug-in", " uad ", "universal audio plugin",
            " waves ", "fabfilter", "soundtoys", "slate digital",
            "izotope", "acustica", "plugin alliance", "brainworx",
            "softube", "arturia", "native instrument", "kilohearts",
            "analog obsession", "tokyo dawn", "valhalla",
            "eventide", "lexicon", "sonnox",
        ],
    },
    "music_theory": {
        "label": "Music Theory",
        "tier": 1,
        "keywords": [
            "music theory", "chord progression", "scale",
            "key of", "major key", "minor key",
            "interval", "harmony", "counterpoint",
            "time signature", " bpm ", "tempo",
            "relative minor", "mode", "dorian",
            "circle of fifth", "tritone",
        ],
    },
    "file_delivery": {
        "label": "File & Delivery",
        "tier": 1,
        "keywords": [
            "stem", "bounce", "export", "print",
            "file format", " wav ", " mp3 ", " aiff ",
            " flac ", "bit depth", "sample rate",
            "44.1", "48k", "96k", "24 bit", "16 bit",
            "delivery", "deliverable", "file naming",
            "google drive", "dropbox", "wetransfer",
        ],
    },

    # --- TIER 2: New domains ---
    "career_advice": {
        "label": "Career Advice",
        "tier": 2,
        "keywords": [
            "career", "profession", "full-time", "full time",
            "make a living", "make money", "income",
            "get client", "find client", "build clientele",
            "portfolio", "demo reel", "resume",
            "intern", "internship", "assistant",
            "audio school", "recording school", "degree",
            "job", "hire", "hiring", "freelance",
            "side hustle", "day job", "quit my job",
            "going full time", "sustainable",
        ],
    },
    "mental_health": {
        "label": "Mental Health",
        "tier": 2,
        "keywords": [
            "mental health", "burnout", "burn out",
            "anxiety", "depression", "stress",
            "imposter syndrome", "impostor syndrome",
            "self-doubt", "self doubt", "confidence",
            "comparison", "comparing myself",
            "motivation", "demotivat", "frustrated",
            "overwhelm", "discouraged", "giving up",
            "therapy", "therapist", "self-care", "self care",
            "break from music", "taking a break",
            "perfectionism", "perfectionist",
        ],
    },
    "learning_education": {
        "label": "Learning & Education",
        "tier": 2,
        "keywords": [
            "how to learn", "learning to", "learn mixing",
            "learn production", "learning curve",
            "course", "tutorial", "youtube channel",
            "book recommend", "reading list",
            "practice routine", "ear training",
            "online course", "masterclass", "workshop",
            "pensado", "produce like a pro", "recording revolution",
            "mix with the masters", "nail the mix",
            "puremix", "groove3", "linkedin learning",
            "skillshare", "udemy", "coursera",
            "how long does it take", "how many years",
        ],
    },
    "community_events": {
        "label": "Community Events",
        "tier": 2,
        "keywords": [
            "meetup", "meet up", "hangout", "hang out",
            "live stream", "livestream", "matt rad live",
            "community", "discord event", "server event",
            "challenge", "contest", "competition",
            "song-a-week", "mix contest", "mix competition",
            "feedback session", "critique session",
            "collab", "collaboration thread",
            "anniversary", "milestone", "celebration",
        ],
    },
    "artist_development": {
        "label": "Artist Development",
        "tier": 2,
        "keywords": [
            "artist develop", "develop as an artist",
            "find your sound", "finding my sound",
            "artistic identity", "artistic voice",
            "creative identity", "unique sound",
            "standing out", "differentiate",
            "brand", "branding", "image",
            "social media", "instagram", "tiktok",
            "release strategy", "single vs album",
            "fan base", "fanbase", "audience",
            "marketing your music", "promote",
        ],
    },
    "remote_collaboration": {
        "label": "Remote Collaboration",
        "tier": 2,
        "keywords": [
            "remote session", "remote recording",
            "remote mix", "remote master",
            "online collaborat", "remote collaborat",
            "source connect", "audiomovers", "listento",
            "zoom session", "facetime session",
            "cloud collab", "splice", "bandlab",
            "file sharing", "revision workflow",
            "working remote", "remote client",
        ],
    },
    "studio_building": {
        "label": "Studio Building",
        "tier": 2,
        "keywords": [
            "building a studio", "build my studio",
            "studio setup", "home studio", "project studio",
            "bedroom studio", "garage studio",
            "studio upgrade", "upgrading my studio",
            "cable management", "wiring",
            "studio furniture", "desk", "studio desk",
            "rack mount", "rack gear",
            "power condition", "ups battery",
            "studio photo", "studio tour",
        ],
    },
    "industry_insights": {
        "label": "Industry Insights",
        "tier": 2,
        "keywords": [
            "music industry", "industry trend",
            "streaming platform", "spotify", "apple music",
            "record label", "major label", "indie label",
            "a&r", "distribution", "distributor",
            "distrokid", "tunecore", "cd baby",
            "sync licensing", "sync deal",
            "ai music", "ai generated", "ai mixing",
            "industry change", "future of music",
            "grammy", "award",
        ],
    },
    "networking_relationships": {
        "label": "Networking & Relationships",
        "tier": 2,
        "keywords": [
            "networking", "relationship",
            "word of mouth", "referral",
            "mentor", "mentorship",
            "open mic", "local scene",
            "connect with artist", "meeting artist",
            "studio etiquette", "professionalism",
            "reputation", "credibility",
            "community building", "giving back",
        ],
    },
    "off_topic_fun": {
        "label": "Off-Topic & Fun",
        "tier": 2,
        "keywords": [
            "off topic", "random", "funny",
            "meme", "joke", "lol",
            "weekend", "holiday", "vacation",
            "movie", "tv show", "netflix",
            "food", "coffee", "beer", "drink",
            "game", "gaming", "video game",
            "sports", "football", "basketball",
            "weather", "pets", "dog", "cat",
        ],
    },

    # --- TIER 3: Enrichment catch-alls ---
    "specific_gear_mentions": {
        "label": "Specific Gear Mentions",
        "tier": 3,
        "keywords": [
            "1176", "la-2a", "la2a", "distressor",
            "ssl g", "ssl e", "api 2500",
            "shadow hills", "fairchild", "manley",
            "pultec", "maag", "chandler",
            "burl", "dangerous", "bettermaker",
            "neumann", "u87", "u67", "u47",
            "sm7b", "sm58", "sm57",
            "royer", "coles", "ribbon mic",
        ],
    },
    "streaming_platforms": {
        "label": "Streaming & Platforms",
        "tier": 3,
        "keywords": [
            "spotify", "apple music", "tidal",
            "amazon music", "youtube music",
            "soundcloud", "bandcamp", "audiomack",
            "streaming number", "stream count",
            "playlist", "algorithmic",
            "release friday", "release day",
        ],
    },
    "creative_philosophy": {
        "label": "Creative Philosophy",
        "tier": 3,
        "keywords": [
            "philosophy", "art vs commerce",
            "creative process", "creative block",
            "inspiration", "taste", "ear develop",
            "less is more", "serve the song",
            "trust your ear", "use your ear",
            "feel vs technical", "vibe", "emotion",
            "intent", "intentional", "musical decision",
            "subjectiv", "objectiv",
        ],
    },
    "matt_rad_references": {
        "label": "Matt Rad References",
        "tier": 3,
        "keywords": [
            "matt rad", "oaklandmatt", "matt's",
            "live with matt", "matt said",
            "matt stream", "matt video",
            "matt instagram", "matt youtube",
        ],
    },
    "health_hearing": {
        "label": "Health & Hearing",
        "tier": 3,
        "keywords": [
            "hearing", "hearing loss", "hearing damage",
            "tinnitus", "ear fatigue", "ear ringing",
            "earplug", "ear protection", "hearing protection",
            "volume limit", "safe listening",
            "posture", "ergonomic", "back pain",
            "carpal tunnel", "wrist pain", "rsi",
            "eye strain", "screen time",
            "exercise", "stretch",
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


def extract_resources(messages):
    """Extract URLs, images, and attachments with context."""
    url_pattern = re.compile(r'https?://\S+')
    resources = []

    for m in messages:
        if is_noise(m):
            continue

        content = m.get("content", "")
        author = get_author(m)
        date = m["timestamp"][:10]
        reactions = get_reactions(m)

        # Extract URLs from message content
        urls = url_pattern.findall(content)
        for url in urls:
            # Clean trailing punctuation
            url = url.rstrip('.,;:!?)>"\'')

            resource_type = "link"
            if "youtube.com" in url or "youtu.be" in url:
                resource_type = "youtube"
            elif "open.spotify.com" in url:
                resource_type = "spotify"
            elif "soundcloud.com" in url:
                resource_type = "soundcloud"
            elif any(ext in url.lower() for ext in [".png", ".jpg", ".jpeg", ".gif", ".webp"]):
                resource_type = "image"
            elif any(ext in url.lower() for ext in [".pdf", ".doc", ".docx"]):
                resource_type = "document"
            elif "twitter.com" in url or "x.com" in url:
                resource_type = "social"
            elif "instagram.com" in url:
                resource_type = "social"
            elif "reddit.com" in url:
                resource_type = "social"
            elif "tiktok.com" in url:
                resource_type = "social"

            resources.append({
                "url": url,
                "type": resource_type,
                "author": author,
                "date": date,
                "context": content[:300],
                "reactions": reactions,
                "is_expert": is_expert(author),
                "message_id": m["id"],
            })

        # Extract attachments
        for att in m.get("attachments", []):
            att_url = att.get("url", "")
            att_name = att.get("fileName", "")
            att_type = "attachment"
            if any(ext in att_name.lower() for ext in [".png", ".jpg", ".jpeg", ".gif", ".webp"]):
                att_type = "image"
            elif any(ext in att_name.lower() for ext in [".wav", ".mp3", ".flac", ".aif"]):
                att_type = "audio"
            elif any(ext in att_name.lower() for ext in [".pdf", ".doc", ".docx"]):
                att_type = "document"

            resources.append({
                "url": att_url,
                "type": att_type,
                "fileName": att_name,
                "author": author,
                "date": date,
                "context": content[:300],
                "reactions": reactions,
                "is_expert": is_expert(author),
                "message_id": m["id"],
            })

    return resources


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
    print("=== #general-talk Extraction Pipeline ===\n")

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
    top_authors = sorted(authors.items(), key=lambda x: x[1]["substantive"], reverse=True)[:40]
    print(f"\nTop 40 authors by substantive messages:")
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
    for tier_num in [1, 2, 3]:
        tier_label = {1: "TIER 1 — Existing vault domains", 2: "TIER 2 — New domains", 3: "TIER 3 — Enrichment catch-alls"}[tier_num]
        print(f"\n  --- {tier_label} ---")
        for cat_key, cat_info in CATEGORIES.items():
            if cat_info["tier"] != tier_num:
                continue
            count = len(cat_messages[cat_key])
            expert_count = sum(1 for m in cat_messages[cat_key] if m["is_expert"])
            total_cat_entries += count
            print(f"  {cat_info['label']:<40} {count:>6}  (expert: {expert_count})")
    print(f"\n  {'Uncategorized':<40} {len(uncategorized):>6}")
    print(f"  Unique messages categorized: {len(total_categorized_msgs)}")
    print(f"  Categorization rate: {len(total_categorized_msgs) / len(substantive) * 100:.1f}%")
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

    # === Q&A Pair Extraction ===
    print(f"\n=== Q&A Pair Extraction ===")
    qa_pairs = build_qa_pairs(messages)
    print(f"Total Q&A pairs with expert/endorsed answers: {len(qa_pairs)}")

    qa_pairs.sort(key=lambda x: (len(x["expert_answers"]), x["question_reactions"]), reverse=True)

    with open(OUTPUT_DIR / "qa_pairs.json", "w") as f:
        json.dump(qa_pairs, f, indent=2)

    # Q&A category breakdown
    qa_by_cat = defaultdict(int)
    for qa in qa_pairs:
        for cat in qa["categories"]:
            qa_by_cat[cat] += 1
        if not qa["categories"]:
            qa_by_cat["uncategorized"] += 1
    print(f"\nQ&A pairs by category (top 15):")
    for cat_key, count in sorted(qa_by_cat.items(), key=lambda x: -x[1])[:15]:
        label = CATEGORIES[cat_key]["label"] if cat_key in CATEGORIES else cat_key
        print(f"  {label:<40} {count:>6}")

    # Preview top Q&A pairs
    print(f"\nTop 10 Q&A pairs (by expert answer count):")
    for qa in qa_pairs[:10]:
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

    # === Resource Extraction ===
    print(f"\n=== Resource Extraction ===")
    resources = extract_resources(messages)
    print(f"Total resources extracted: {len(resources)}")

    # Resource type breakdown
    type_counts = defaultdict(int)
    for r in resources:
        type_counts[r["type"]] += 1
    print(f"Resource type breakdown:")
    for rtype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {rtype:<20} {count:>6}")

    # Sort by reactions and save
    resources.sort(key=lambda x: x["reactions"], reverse=True)
    with open(OUTPUT_DIR / "resources.json", "w") as f:
        json.dump(resources, f, indent=2)

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

    # Per-category top expert quotes (for vault enrichment)
    print("\n=== Top Expert Quotes Per Category (for vault enrichment) ===")
    for cat_key, cat_info in CATEGORIES.items():
        msgs = cat_messages[cat_key]
        expert_msgs_cat = [m for m in msgs if m["is_expert"]]
        if not expert_msgs_cat:
            continue
        expert_msgs_cat.sort(key=lambda x: x["reactions"], reverse=True)
        print(f"\n--- {cat_info['label']} (Tier {cat_info['tier']}) ---")
        for m in expert_msgs_cat[:3]:
            print(f"  [{m['reactions']} react] {m['author']} ({m['date']}): {m['content'][:200]}")

    # Save summary
    summary = {
        "total_messages": len(messages),
        "date_range": f"{min(dates)} to {max(dates)}",
        "substantive_messages": len(substantive),
        "noise_filtered": len(messages) - len(substantive),
        "unique_authors": len(authors),
        "unique_messages_categorized": len(total_categorized_msgs),
        "categorization_rate": round(len(total_categorized_msgs) / len(substantive) * 100, 1),
        "uncategorized": len(uncategorized),
        "expert_substantive_messages": expert_msgs,
        "qa_pairs_count": len(qa_pairs),
        "expert_advice_count": len(expert_messages),
        "resources_count": len(resources),
        "resource_types": dict(type_counts),
        "activity_by_year": dict(sorted(year_counts.items())),
        "categories": {
            cat_key: {
                "label": cat_info["label"],
                "tier": cat_info["tier"],
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
