---
type: glossary
confidence: medium
aliases:
  - Loudness Penalty
tags:
  - type/glossary
  - channel/newbie-questions
created: 2026-02-18
modified: 2026-02-18
---

# Loudness Normalization

## Definition

The process by which streaming platforms automatically adjust playback volume so that all songs play at a similar perceived loudness, regardless of how they were mastered. This is measured in [[LUFS]] (Loudness Units Full Scale).

## Context

"How loud should my master be?" is one of the most common questions in #newbie-questions. The answer involves understanding loudness normalization:

### Platform Targets (approximate)

| Platform | Target | Normalization |
|----------|--------|--------------|
| Spotify | -14 LUFS | Turns down loud masters |
| Apple Music | -16 LUFS | Turns down loud masters |
| YouTube | -14 LUFS | Turns down loud masters |
| SoundCloud | No normalization | Louder = louder |

### Practical Implications

- **Mastering louder than the target** means the platform will turn your track down, and you've sacrificed dynamics for nothing
- **Mastering quieter than the target** on some platforms means your track gets turned up, which can actually sound better due to preserved dynamics
- **True peak ceiling** should be -1 dBTP or lower to avoid distortion from lossy codec conversion (MP3, AAC)

### Where Normalization Doesn't Apply (from #mastering-talk)

Working mastering engineers in #mastering-talk emphasize that normalization is far less universal than commonly assumed:

- **Spotify on smart TV** — no loudness normalization
- **Spotify web browser** — no loudness normalization
- **External/Bluetooth speakers** — normalization behavior varies
- **Sonos and similar systems** — not reliably applied
- **Bandcamp** — no normalization at all
- **Users who disable normalization** — a significant portion of listeners

> [!quote] Nomograph Mastering (2022-11-16) — #mastering-talk — 10 reactions
> "Not everyone has level norm on. Spotify on smart TV does not have level norm. Spotify on web browser does not have loudness norm. Spotify and other DSPs can and will change the targets so you CANNOT depend on them."

The only context where loudness has enforceable consequences is **broadcast advertising** (-24 LUFS in North America, -23 LUFS in Europe).

### Professional Mastering Perspective

The consensus from working mastering engineers is strongly against targeting a LUFS number:

> [!quote] Rollmottle (2023-01-26) — #mastering-talk — 22 reactions, pinned
> "Just master the material for the material."

See [[Loudness Standards and Streaming Delivery]] for comprehensive coverage.

## Related Terms

- [[LUFS]]
- [[Mastering Workflows]]
- [[Intersample Peak]]

## See Also

- [[Loudness Standards and Streaming Delivery]]
- [[Beginner FAQ#Mastering Basics]]
- [[Streaming Economics]]
