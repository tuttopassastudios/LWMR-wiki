---
type: topic
confidence: medium
aliases:
  - Mix Techniques
  - Mixing Tips
  - Advanced Mixing
tags:
  - domain/mixing
  - type/topic
created: 2026-02-17
modified: 2026-02-17
---

# Advanced Mixing Techniques

## Summary
> [!abstract]
> Advanced mixing techniques discussed in the community go beyond basic level balancing into parallel compression, bus processing strategies, dynamic EQ, saturation, and stereo imaging. A recurring theme is the use of dual-bus mixing architectures and smart EQ tools like [[Soothe2]] and [[Gullfoss]] to solve frequency masking problems that traditional processing cannot address efficiently.

## Detail

### Parallel Compression
Parallel compression (also called New York compression) is widely used on drums, vocals, and mix buses. Members blend a heavily compressed signal with the dry original to add density without sacrificing transients. Common approaches include using an [[1176]]-style compressor with fast attack/release on the parallel bus, or using a DAW's built-in wet/dry mix knob on compressor plugins.

### Bus Compression Approaches
Bus compression strategies vary by genre and preference. The community frequently discusses [[SSL]]-style bus compression for glue, [[1176]] all-buttons mode for aggressive parallel treatment, and [[LA-2A]] optical compression for smoother vocal buses. A standout technique involves splitting the mix into a "front bus" and "background bus" for differentiated processing.

> [!quote] Source
> **Author:** bobby k — **Date:** 2021-06-28 — **Channel:** #daw-talk
> "I got the idea to do a main mixbuss and a background mixbuss and it's been a game changer for me..."

> [!quote] Source
> **Author:** bobby k — **Date:** 2021-06-28 — **Channel:** #daw-talk
> "then my 'background buss' gets generous shelf cuts from UAD's pultec, it gets mild buss compression... and most importantly, it gets a multiband side chain from the front buss through Soothe2..."

### Dynamic EQ and Multiband
Dynamic EQ and multiband compression serve similar purposes but with different workflows. Community members generally prefer dynamic EQ ([[FabFilter Pro-Q 3]], [[TDR Nova]]) for surgical frequency problems and multiband compression for broader tonal shaping. [[Soothe2]] and [[Gullfoss]] represent a newer category of "smart" EQ tools that automatically identify and attenuate resonances, with members reporting significant workflow speedups.

### Saturation and Harmonic Enhancement
Saturation is used across the mix for warmth, density, and controlled clipping. Members discuss tape saturation on the mix bus, tube saturation on vocals, and hard clipping on drums as a gain staging tool. Popular tools include [[Decapitator]], [[Saturn 2]], and [[Studer A800]] emulations. Clipping before compression is a technique several members use to tame transients without pumping artifacts.

### Stereo Imaging and Width Management
Mid-side processing and stereo width management are discussed for creating depth and separation. Members recommend keeping low frequencies mono (below ~200Hz), using mid-side EQ to brighten the sides independently, and using [[Haas effect]] delays carefully to avoid phase issues in mono. Width plugins and auto-pan effects are used sparingly to avoid translation problems across playback systems.

## Practical Application
- Set up a front bus and background bus architecture for clearer mix hierarchy
- Use [[Soothe2]] on vocals and cymbals to tame resonances before traditional EQ
- Apply parallel compression on a separate bus rather than using plugin wet/dry for more control
- Check all stereo width processing in mono to ensure translation
- Use clipping before compression on drums to control transients transparently

## Common Mistakes
- Over-compressing the mix bus and destroying dynamic range
- Using multiband compression when a simple dynamic EQ would be more precise
- Adding stereo width effects without checking mono compatibility
- Stacking too many saturation plugins and creating harshness in the upper mids
- Relying on smart EQ tools as a substitute for intentional mix decisions

## See Also
- [[Mixing in the DAW]] — foundational mixing concepts and workflows
- [[DAW Routing and Signal Flow]] — setting up bus architectures
- [[Gain Staging]] — proper levels before and after processing
- [[De-esser]] — specialized dynamic processing for sibilance

## Source Discussions

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** Will Melones, Iwan Morgan, ehutton21, Slow Hand, cian riordan
> **Message volume:** 220 categorized messages
