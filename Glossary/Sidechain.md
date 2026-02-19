---
type: glossary
confidence: medium
aliases:
  - Sidechain Compression
  - Sidechaining
  - Key Input
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-18
---

# Sidechain

## Definition

A technique in which one audio signal (the "key" or "trigger") controls a processor applied to a different audio signal. The most common application is sidechain compression, where a kick drum signal triggers a compressor on a bass or pad track, causing it to duck in volume with each kick hit, creating a rhythmic pumping effect.

## Context

Sidechain compression is ubiquitous in electronic music production and increasingly common across all genres for managing frequency conflicts between kick and bass. Beyond compression, sidechaining can be applied to gates, EQs, and other dynamics processors. The ease of sidechain routing varies by DAW — [[Ableton Live]] makes it straightforward through its routing dropdowns, while [[Pro Tools]] uses key input assignments on dynamics plugins.

## Related Terms

- [[Bus]]
- [[Aux Track]]
- [[Gain Staging]]

## Mixing Techniques (from #mixing-talk)

In #mixing-talk, sidechain techniques are extensively discussed within the compression (2,443 messages) and low end management (2,203 messages) categories:

- **Kick/bass sidechain:** The most common application — kick drum triggers gentle compression on the bass to create momentary space in the low end
- **Compressor sidechain HPF:** Using the sidechain high-pass filter on bus compressors prevents bass-heavy content from triggering unwanted gain reduction — critical for mix bus and drum bus compression
- **Multiband sidechain (Soothe2):** bobby k's front/background bus architecture uses Soothe2's multiband sidechain to duck the background bus in frequency ranges occupied by the front bus
- **Vocal sidechain:** Some members sidechain instrument buses from the vocal to create automatic space for the lead vocal

## See Also

- [[Mixing in the DAW]]
- [[DAW Comparison]]
- [[Compression Techniques]]
- [[Low End Management]]
