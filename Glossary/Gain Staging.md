---
type: glossary
confidence: low
aliases:
  - Gain Structure
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-17
---

# Gain Staging

## Definition

The practice of managing signal levels at each point in the audio chain to maintain optimal headroom and signal-to-noise ratio. Essential for both analog and digital workflows, though the consequences of poor gain staging differ between the two domains.

## Context

In analog systems, improper gain staging can introduce noise (too low) or distortion (too high). In digital systems with 32-bit float internal processing, clipping individual channels is technically non-destructive, but maintaining sensible levels improves metering accuracy and plugin behavior — many plugin emulations of analog hardware respond differently depending on input level. A common guideline is to aim for peaks around -18dBFS to -12dBFS on individual tracks.

## Related Terms

- [[Bit Depth]]
- [[Summing]]
- [[VCA]]

## Recording Context

In #recording-talk, gain staging is discussed primarily in the context of tracking through outboard gear. cian riordan notes that "24 bits is an insane amount of headroom" -- the community generally advises leaving 6-12 dB below digital 0 when tracking. The more nuanced discussion involves deliberately driving preamp and compressor inputs for tonal character (e.g., using [[UREI 1176]]s as line distortion by "blowing up the input and trimming the output").

## See Also

- [[Mixing in the DAW]]
- [[DAW Comparison]]
- [[Recording and Tracking Workflows]]
