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

## See Also

- [[Mastering Workflows]]
- [[Dolby Atmos and Immersive Audio]]
- [[Reference Mixing and Translation]]
- [[Mix Bus Processing]]
