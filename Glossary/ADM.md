---
type: glossary
confidence: medium
aliases:
  - Audio Definition Model
tags:
  - type/glossary
  - channel/atmos-talk
created: 2026-02-18
modified: 2026-02-18
---

# ADM

## Definition

Audio Definition Model — the standardized metadata format (ITU-R BS.2076) used for Dolby Atmos project interchange. ADM BWF (Broadcast Wave Format) files contain both the audio content and the spatial positioning metadata needed to reconstruct an Atmos mix.

## Context

ADM is the standard delivery format for Dolby Atmos productions. The Dolby Album Assembler outputs ADM BWF files for distribution. A key limitation confirmed by the community: [[Cubase]] cannot import ADM files — this capability is exclusive to Nuendo, making it a hard requirement for post-production workflows involving Atmos project exchange. [[Pro Tools]] and [[Logic Pro]] handle Atmos projects through their own internal formats and renderer integration rather than ADM import/export.

## Related Terms

- [[Dolby Atmos]]
- [[Dolby Atmos Renderer]]
- [[Spatial Audio and Dolby Atmos]]

## See Also

- [[Dolby Atmos and Immersive Audio]]
