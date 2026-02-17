---
type: topic
confidence: medium
aliases:
  - ITB Mixing
  - In The Box Mixing
  - DAW Mixing
tags:
  - domain/mixing
  - type/topic
created: 2026-02-17
modified: 2026-02-17
---

# Mixing in the DAW

## Summary
> [!abstract]
> Mixing entirely within a DAW ("in the box" or ITB) is the dominant approach in modern production. Community discussions focus on DAW-specific mixing workflows, bus processing philosophy, gain staging, and the creative use of routing features like Audio Effect Racks (Ableton), Aux tracks (Pro Tools), and flexible bus creation (Cubase).

## Detail

### Mix Bus Philosophy
bobby k shared a detailed approach to creative bus processing that represents a sophisticated ITB mixing methodology:

- **Front bus vs. background bus** — separate processing chains for foreground and background elements
- **Background bus** receives shelf cuts, mild bus compression, multiband sidechain (Soothe2), and width reduction
- **Stereo width management** — background at ~75% of front bus width, positioned between LC and CR
- Background elements are "smeared" with filtering, saturation, and transient reduction to create depth

> [!quote] Source
> **Author:** bobby k — **Date:** 2021-06-28 — **Channel:** #daw-talk
> "My background bus gets generous shelf cuts from UAD's Pultec, mild bus compression, and most importantly a multiband sidechain from the front bus through Soothe2. Its stereo width is about 75% of the front bus."

### DAW-Specific Mixing Strengths
Each DAW offers different mixing advantages:

| DAW | Mixing Strength |
|-----|----------------|
| [[Pro Tools]] | AudioSuite, playlists, VCA faders, industry-standard console workflow |
| [[Ableton Live]] | Audio Effect Racks for parallel processing, creative routing |
| [[Cubase]] | Flexible bus creation, Control Room, Direct Offline Processing |
| [[Reaper]] | Fully customizable routing, JS plugins, SWS extensions |
| [[Logic Pro]] | Strong stock plugins, Flex Pitch, integrated workflow |

### Parallel Processing
Parallel processing is a key technique discussed extensively:
- In [[Ableton Live]], Audio Effect Racks allow splitting a signal into multiple parallel chains on a single track (Slow Hand)
- In [[Pro Tools]], aux sends to parallel processing buses are the standard approach
- The ability to A/B entire processing chains is a significant workflow advantage of racks (Slow Hand)

## Practical Application
- Choose your mixing DAW based on workflow speed, not perceived sound quality (all DAWs sum identically — see [[DAW Summing and Sound Differences]])
- Set up templates with routing, color coding, and default processing pre-configured
- Use bus compression and processing to create depth and separation
- Use parallel processing for adding energy without losing dynamics

## Common Mistakes
- Over-processing individual channels instead of using bus-level treatment
- Ignoring [[Gain Staging]] — proper levels throughout the chain are essential
- Not using templates — rebuilding routing from scratch wastes time
- Choosing a DAW for mixing based on summing myths rather than workflow fit

## See Also
- [[DAW Summing and Sound Differences]] — all DAWs sum the same
- [[DAW Routing and Signal Flow]] — routing techniques across DAWs
- [[Session Templates and Organization]] — template setup
- [[Gain Staging]] — level management
- [[Bus]] — grouping and bus processing
- [[Sidechain]] — inter-track processing

## Source Discussions

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** bobby k, Slow Hand, Adam Thein, oaklandmatt, austenballard
> **Message volume:** 1,996 categorized messages (581 from identified experts)
