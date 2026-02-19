---
type: topic
confidence: high
aliases:
  - Compression Types
  - Compressor Topology
  - Parallel Compression Techniques
tags:
  - domain/mixing
  - type/topic
  - channel/mixing-talk
created: 2026-02-18
modified: 2026-02-18
---

# Compression Techniques

## Summary

> [!abstract]
> Compression is the most discussed technical topic in #mixing-talk (2,443 categorized messages). The community's approach centers on understanding the four main compressor topologies — VCA, FET, opto, and variable-mu — and learning when each is appropriate. Nomograph Mastering's pinned compressor guide (62 reactions) is the channel's definitive resource, recommending engineers pick one model from each category and master it before branching out. Parallel compression, bus compression, and sidechain techniques are extensively discussed practical applications.

## Detail

### The Four Compressor Topologies

The community consistently returns to the four main compressor types as the foundation of compression knowledge:

**VCA (Voltage Controlled Amplifier):** Fast, precise, and clean. The [[SSL Bus Compressor]] is the defining example. VCA compressors excel at "glue" — making individual elements feel like a cohesive mix. Used extensively on mix buses, drum buses, and stem groups.

**FET (Field Effect Transistor):** Aggressive, fast, characterful. The [[UREI 1176]] is the quintessential FET compressor with the fastest attack time (~20 microseconds). Known for adding energy and excitement, particularly in "all buttons in" mode for parallel compression on drums.

**Opto (Optical):** Smooth, program-dependent, musical. The [[Teletronix LA-2A]] is the classic example with its T4B opto cell creating naturally musical compression. The community favors opto compression on vocals, bass, and acoustic instruments where a gentle, transparent touch is needed.

**Variable-mu (Tube):** Warm, gentle, harmonically rich. The Fairchild 670 and Manley Vari-Mu are the reference points. Used for subtle bus compression where harmonic enrichment is as important as dynamic control.

> [!quote] Source
> **Author:** Nomograph Mastering — **Date:** 2024-12-23 — **Channel:** #mixing-talk
> "Ok, so that's a quick summary of the four main types of comp. My suggestion is to pick one model from each category. One and only one. Forget the rest for a while. Start trying it in various places to develop a feel for what each type does."

### Parallel Compression

[[Parallel Compression]] (aka New York compression) is one of the most frequently discussed techniques. The approach involves blending a heavily compressed signal with the unprocessed original to add density and sustain without sacrificing transients. Common applications:

- **Drums:** An [[UREI 1176]] in all-buttons mode on a parallel send is the community's go-to for adding power to drum buses
- **Vocals:** Gentle parallel compression to add body and consistency while preserving natural dynamics
- **Mix bus:** Subtle parallel compression for overall mix density

The community prefers dedicated parallel sends over plugin wet/dry knobs for more precise control over the blend.

### Bus Compression

Bus compression is applied to grouped signals (drum bus, vocal bus, instrument bus, mix bus) to create cohesion. Key community insights:

- **Slow attack, fast release** on the mix bus lets transients through while adding glue
- **2-4 dB of gain reduction** is the sweet spot for most bus compression — more than that and you're likely over-compressing
- The [[SSL Bus Compressor]] at 4:1, slow attack, auto release is the starting point most members reference
- Multiple members use **front bus / background bus** architecture with different compression approaches on each

### Sidechain Compression

[[Sidechain]] compression uses one signal to trigger compression on another. The most common application is kick drum triggering bass compression to create space in the low end. The community also discusses:

- Sidechain HPF on compressors to prevent bass frequencies from triggering unwanted gain reduction
- Multiband sidechain (using [[Soothe2]]) for frequency-specific ducking
- Vocal sidechain on instrument buses to create automatic space for vocals

### Settings by Source

Community-shared starting points:

| Source | Compressor Type | Ratio | Attack | Release | Notes |
|--------|----------------|-------|--------|---------|-------|
| Lead vocal | LA-2A / opto | 3:1-4:1 | Medium | Auto | 3-5 dB GR |
| Drum bus | SSL / VCA | 4:1 | Slow (30ms) | Fast | Let transients through |
| Parallel drums | 1176 / FET | 20:1 | Fast | Fast | All-buttons or high ratio |
| Bass | LA-2A / opto | 4:1 | Medium | Auto | Smooth, consistent |
| Mix bus | SSL / VCA | 2:1-4:1 | Slow | Auto | 1-3 dB GR max |
| Acoustic guitar | Distressor | 2:1 | Medium | Medium | Gentle, transparent |

## Practical Application

- Learn one compressor per topology before expanding your collection
- Set up a dedicated parallel compression bus rather than using wet/dry knobs
- Use the HPF on your compressor's sidechain to prevent low-frequency content from dominating the gain reduction
- Start with less compression than you think you need — 2-3 dB of gain reduction on most sources
- Listen for "pumping" and "breathing" as signs of over-compression or wrong attack/release settings

## Common Mistakes

- Using the same compressor type on every source without considering what each topology does best
- Over-compressing the mix bus and destroying dynamic range
- Not using the sidechain HPF, causing bass-heavy sources to pump
- Stacking multiple compressors without understanding what each one is contributing
- Chasing gain reduction numbers instead of listening to the musical effect

## See Also

- [[Parallel Compression]] — dedicated glossary entry
- [[SSL Bus Compressor]] — VCA bus compression standard
- [[UREI 1176]] — FET compression reference
- [[Teletronix LA-2A]] — optical compression reference
- [[Empirical Labs Distressor]] — versatile multi-mode compressor
- [[Mix Bus Processing]] — bus chain context
- [[Gain Staging]] — levels before and after compression

## Source Discussions

> [!quote] Discord Source
> **Channel:** #mixing-talk — **Date Range:** 2021-08 to 2026-02
> **Key contributors:** Nomograph Mastering, cian riordan, chrissorem, BatMeckley, Ross Fortune, Slow Hand, ALXCPH
> **Message volume:** 2,443 categorized messages
