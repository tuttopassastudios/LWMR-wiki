---
type: glossary
confidence: low
aliases:
  - Beat Detective
tags:
  - type/glossary
created: 2026-02-18
modified: 2026-02-18
---

# Beat Detective

## Definition

[[Pro Tools]]' built-in drum and rhythm quantization tool that uses transient detection to align audio regions to the session's tempo grid. Beat Detective analyzes audio waveforms, identifies transient peaks, separates regions at those transients, and conforms them to the grid — the standard workflow for tightening drum performances in professional studios.

## Context

Beat Detective remains essential for drum editing in Pro Tools despite the availability of [[Elastic Audio]] for non-destructive quantization. The typical workflow involves detecting transients across drum tracks, separating clips at those points, conforming to the grid, and filling gaps with crossfades. Zack Hames documented detailed drum editing workflows in #pro-tools, including challenges with room mic glitches during quantization — room mics can produce artifacts when their transients don't align cleanly with close mics. sethmanchester shared a creative trick: record drums at a slower BPM, use Beat Detective to quantize, then speed the session back up to the target tempo. Adam Thein discussed stray-track fixes for situations where Beat Detective misidentifies transients.

## Related Terms

- [[Pro Tools]]
- [[Elastic Audio]]
- [[Editing Techniques Across DAWs]]

## See Also

- [[Drum Recording Techniques]] — recording workflows that feed into Beat Detective editing
- [[Comping]] — complementary take selection workflow
