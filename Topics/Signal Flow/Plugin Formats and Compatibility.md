---
type: topic
confidence: medium
aliases:
  - Plugin Formats
  - VST vs AU vs AAX
  - Plugin Compatibility
tags:
  - domain/signal-flow
  - type/topic
created: 2026-02-17
modified: 2026-02-17
---

# Plugin Formats and Compatibility

## Summary

> [!abstract]
> Audio plugins come in several formats — AAX (Pro Tools), VST/VST3 (cross-platform), and AU (macOS). Format choice is dictated by DAW: Pro Tools requires AAX, Logic uses AU, and Ableton/Cubase/Reaper support VST and/or AU. The Apple Silicon transition created significant compatibility challenges, with Rosetta bridging the gap during the transition period.

## Detail

### Format Overview

| Format | Developer | DAW Support | Notes |
|--------|-----------|------------|-------|
| **[[AAX]]** | Avid | [[Pro Tools]] only | Required for Pro Tools; limits plugin availability |
| **[[VST]]/VST3** | Steinberg | [[Cubase]], [[Reaper]], [[Ableton Live]] | Most widely supported cross-platform format |
| **[[AU]]** (Audio Units) | Apple | [[Logic Pro]], [[Ableton Live]], [[Reaper]] | macOS only |

### Apple Silicon Compatibility

The M1 transition created a multi-year compatibility challenge:

- [[Logic Pro]] went M1-native first — Rosetta-only plugins couldn't load in native mode (Slow Hand, 2021)
- [[Ableton Live]] and most others ran under Rosetta initially, allowing older plugins to work
- Plugin developers needed to release separate M1-native builds
- Many developers have since updated, but some legacy plugins remain Rosetta-only

> [!quote] Source
> **Author:** Slow Hand — **Date:** 2021-11-10 — **Channel:** #daw-talk
> "I'm all-in on Mac M1 at this point. Here are the big software companies I'm using: Ableton (Rosetta), NI Komplete, Goodhertz, FabFilter, Valhalla, iZotope, Waves, SoundToys, LiquidSonics."

> [!quote] Source
> **Author:** Slow Hand — **Date:** 2021-09-23 — **Channel:** #daw-talk
> "Logic does not run with Rosetta at all. So plugins that are only Rosetta compatible won't work in a DAW that's M1 compatible until they're updated."

### AAX Limitations

Pro Tools' AAX-only requirement can limit plugin choices and create stability issues:

> [!quote] Source
> **Author:** mixedbywong_my — **Date:** 2022-06-24 — **Channel:** #daw-talk
> "Lately I've been reading about a lot of PT users having major issues with stability especially with newer plugins. Could be an AAX thing as Nuendo/Cubase and Logic use VST/VST3/AU."

### Licensing and Authorization

Plugin licensing varies by manufacturer — iLok, native licensing, subscription models. The iLok system remains controversial:

> [!quote] Source
> **Author:** Ross Fortune — **Date:** 2023-01-22 — **Channel:** #daw-talk
> (Shared a story about iLok physical dongles being vulnerable to theft at studio facilities)

> [!quote] Source
> **Author:** Will Melones — **Date:** 2025-12-29 — **Channel:** #daw-talk
> "Why does every company have a download manager and installer app? I generally groan at them all — Acustica, IK, Steinberg. I don't need to see products I don't own."

## Practical Application

- Check plugin format support before purchasing — verify your DAW supports the format
- When running Apple Silicon, verify M1-native support for critical plugins before upgrading
- Pro Tools users: ensure plugins are AAX-compatible before purchase
- Consider DAW format support when choosing a new DAW

## Common Mistakes

- Buying plugins in the wrong format for your DAW
- Upgrading macOS/hardware without checking plugin compatibility first
- Assuming Rosetta performance equals native performance
- Not maintaining plugin backups (licenses, installers)

## See Also

- [[AAX]] — Avid's plugin format
- [[VST]] — Steinberg's cross-platform format
- [[AU]] — Apple's Audio Units format
- [[Pro Tools]] — AAX-only DAW
- [[Plugin Ecosystem Overview]] — major plugin developers

## Source Discussions

> [!quote] Discord Source
> **Channel:** #daw-talk — **Date Range:** 2021-02 to 2026-02
> **Key contributors:** Slow Hand, mixedbywong_my, Ross Fortune, Will Melones, ALXCPH
> **Message volume:** 2,355 categorized messages (720 from identified experts)
