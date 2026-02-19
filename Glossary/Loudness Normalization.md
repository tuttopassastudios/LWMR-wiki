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

> [!quote] Discord Source — Nomograph Mastering (2022-10-22) — 59 reactions (pinned in #newbie-questions)
> "If I was asked 'What sample rate should people make records at in 2022?' And was forced to choose then the answer would be 48k."

The community's ongoing debate is whether to master to -14 LUFS for Spotify or master louder for competitive playback on non-normalizing platforms.

## Related Terms

- [[LUFS]]
- [[Mastering Workflows]]

## See Also

- [[Beginner FAQ#Mastering Basics]]
- [[Streaming Economics]]
