---
type: glossary
confidence: low
aliases:
  - Elastic Time
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-17
---

# Elastic Audio

## Definition

[[Pro Tools]]' built-in time-stretching and pitch-shifting engine that allows non-destructive manipulation of audio timing without cutting and moving regions.

## Context

Elastic Audio is used for timing correction, tempo conforming, and quantizing audio to the grid in [[Pro Tools]]. It offers multiple algorithm modes (polyphonic, rhythmic, monophonic, X-Form) suited to different material types. Elastic Audio can be applied in real-time or rendered for higher-quality offline processing via X-Form.

## Relationship to Beat Detective

[[Elastic Audio]] and [[Beat Detective]] serve overlapping purposes in [[Pro Tools]] — both can quantize audio to the grid — but use fundamentally different approaches. Beat Detective cuts audio at transients and moves the resulting clips to the grid, while Elastic Audio time-stretches audio non-destructively. In #pro-tools, Zack Hames documented room mic glitches during Beat Detective quantization, where room mic transients don't align cleanly with close mic edits. Elastic Audio can sometimes produce smoother results on room mics since it stretches rather than cuts, but may introduce time-stretch artifacts on percussive material. Many drum editors use Beat Detective for close mics and Elastic Audio (or manual editing) for room mics.

## Related Terms

- [[Pro Tools]]
- [[Beat Detective]]
- [[Editing Techniques Across DAWs]]
- [[Warp Mode]]

## See Also

- [[Time Stretch]]
- [[Drum Recording Techniques]]
