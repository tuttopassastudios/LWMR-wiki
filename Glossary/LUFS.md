---
type: glossary
confidence: medium
aliases:
  - Loudness Units
  - LKFS
tags:
  - type/glossary
  - channel/atmos-talk
created: 2026-02-17
modified: 2026-02-18
---

# LUFS

## Definition

Loudness Units relative to Full Scale — a standardized measurement of perceived audio loudness used for streaming platform targets (typically -14 LUFS for Spotify/Apple Music) and immersive audio delivery specifications.

## Context

LUFS has become the primary loudness metric in modern mastering workflows, replacing peak-based measurements for delivery compliance. Streaming platforms normalize playback volume based on integrated LUFS values, meaning tracks mastered significantly louder than the target are turned down rather than gaining a competitive advantage. Most mastering limiters and metering plugins display LUFS readings (short-term, momentary, and integrated).

For [[Dolby Atmos]] delivery, the loudness specification is stricter than stereo: **-18 LUFS-I** (integrated) with a true peak ceiling of **-1 dBTP**. This is the standard target for major label Atmos masters, and UMG QC will flag non-compliant deliverables.

## Related Terms

- [[Mastering Workflows]]
- [[Gain Staging]]
- [[Dolby Atmos]]

## Mixing Context (from #mixing-talk)

In #mixing-talk, LUFS is discussed within the broader loudness and gain staging conversation (706 categorized messages). Key community perspectives:

- **Streaming normalization debate:** Ongoing tension between targeting -14 LUFS (Spotify's normalization point) and mastering louder for competitive playback on platforms that don't normalize. The community generally advises mixing with awareness of LUFS targets but not obsessing over hitting an exact number
- **Reference track matching:** When A/B comparing against a reference, loudness-matching via LUFS is critical — the louder track almost always sounds "better" due to psychoacoustics, not actual quality differences
- **Mixing metering:** Multiple members use LUFS meters during mixing (not just mastering) to ensure mixes are in a reasonable loudness range before sending to mastering

## Mastering Context (from #mastering-talk)

In #mastering-talk (419 loudness/LUFS messages, 22,909 total), working mastering engineers provide a sharply different perspective on LUFS than typical online discourse:

- **"Just master the material for the material"** — Rollmottle's pinned summary: targeting a specific LUFS number is misguided because not all platforms normalize, not all users enable normalization, and many genres benefit from being pushed into a limiter
- **The -14 LUFS target is largely internet chatter** — Nomograph Mastering (pinned): "The dedication with which a Mastering Engineer advocates -14 is inversely proportional to the amount of records they've done that you've heard of"
- **Perceived loudness is built in the arrangement and mix** — Nomograph Mastering: "Perceived loudness is almost all determined by the arrangement. Mixing can enhance it some. Mastering can enhance it less"
- **Normalization doesn't apply everywhere** — Spotify on smart TV, Spotify web browser, Sonos, and many external speakers don't normalize; Bandcamp doesn't normalize at all
- **Genre-appropriate references matter more than numbers** — Nomograph Mastering: "If you want a -7 LUFS master then you need to build a -7 LUFS mix"

See [[Loudness Standards and Streaming Delivery]] for comprehensive platform-specific normalization data.

## See Also

- [[Mastering Workflows]]
- [[Loudness Standards and Streaming Delivery]]
- [[Dolby Atmos and Immersive Audio]]
- [[Reference Mixing and Translation]]
- [[Mix Bus Processing]]
- [[Loudness Normalization]]

## Beginner Context (from #newbie-questions)

"How loud should my master be?" is one of the most common beginner questions. The expert guidance from #newbie-questions:

> [!quote] Discord Source — LAPhill (2023-07-26) — 18 reactions (pinned in #newbie-questions)
> "This is such an important lesson to anyone following along who's either a mixer or especially a mastering engineer. You can send someone spiraling with doubt based off of one comment."

See [[Beginner FAQ#Mastering Basics]] and [[Loudness Normalization]].
