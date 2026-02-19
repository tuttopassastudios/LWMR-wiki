---
type: glossary
confidence: medium
aliases:
  - Dolby Atmos
  - Atmos
tags:
  - type/glossary
  - channel/atmos-talk
created: 2026-02-17
modified: 2026-02-18
---

# Dolby Atmos

## Definition

Object-based immersive audio format by Dolby that combines a channel-based bed (typically 7.1.4 — seven ear-level speakers, one subwoofer, four height speakers) with up to 118 individually positioned audio objects rendered in three-dimensional space.

## Context

Dolby Atmos has become increasingly relevant in music production as streaming platforms (Apple Music, Tidal, Amazon Music) support spatial audio playback. The [[Dolby Atmos Renderer]] processes beds and objects into the appropriate output for the listener's system — a full speaker array, soundbar, or headphones via [[Binaural|binaural]] rendering. [[Pro Tools]] is the primary professional DAW for Atmos mixing, while [[Logic Pro]] offers the most accessible entry point with built-in spatial audio tools. Delivery uses the [[ADM]] BWF format assembled via the Dolby Album Assembler, targeting -18 [[LUFS]]-I and -1 dBTP.

A critical practical reality: Apple's Spatial Audio ignores Dolby's binaural metadata (near/mid/far object distance settings) and applies its own undocumented spatialization, meaning Atmos mixes can sound significantly different between the two renderers. Bed tracks translate more consistently across renderers than objects (up to 4.5 dB level difference with objects). The [[LFE]] channel should be avoided or used sparingly in music — calibration varies wildly across playback systems.

## Related Terms

- [[Dolby Atmos Renderer]]
- [[ADM]]
- [[Binaural]]
- [[HRTF]]
- [[LFE]]
- [[LUFS]]

## See Also

- [[Dolby Atmos and Immersive Audio]]
- [[Spatial Audio and Dolby Atmos]]
- [[Atmos Monitoring and Speaker Setup]]
