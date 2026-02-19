---
type: topic
confidence: high
aliases:
  - Virtual Instruments
  - VST Instruments
  - MIDI Programming
tags:
  - domain/production
  - type/topic
  - channel/production-talk
created: 2026-02-18
modified: 2026-02-18
---

# MIDI and Virtual Instruments

## Summary

> [!abstract]
> MIDI and virtual instruments are discussed in #production-talk with 331 categorized messages, plus significant overlap with sampling (603 msgs) and keys/piano (249 msgs). The channel covers MIDI programming technique, virtual instrument realism, the live-vs-virtual debate, orchestral MIDI programming, and specific instrument recommendations. LAPhill provides the channel's most authoritative voice on orchestral MIDI programming, while cian riordan offers the perspective of blending virtual instruments with live recordings.

## Detail

### Realistic Orchestral Programming

LAPhill is the channel's orchestral MIDI programming authority:

> [!quote] Source
> **Author:** LAPhill — **Date:** 2023-11-16 — **Channel:** #production-talk — 9 reactions
> "By far, the most important element in realistic orchestral sound is in the programming. You need a controller where you can automate cc1 and cc11 (modulation and expression). Instruments, especially strings, that just sit on one dynamic sound like a flat line sound like a machine."

Key principles for orchestral realism:
- **Expression (CC11) and modulation (CC1)** are the foundation — without dynamic automation, MIDI strings/brass/woodwinds sound static and artificial
- **Velocity alone is not enough** — real instruments have timbral changes across dynamics that velocity-only programming misses
- **Articulation switching** — using keyswitches or expression maps to move between legato, staccato, tremolo, pizzicato, etc.
- **Blending live and virtual** — even one real instrument on top of a virtual bed dramatically improves realism

### Live vs Virtual Debate

> [!quote] Source
> **Author:** cian riordan — **Date:** 2023-11-17 — **Channel:** #production-talk — 8 reactions
> "I always find in record production, where strings are usually less featured than film/tv compositions, even blending in a single real string recording with a VST bed makes a huge difference in making it feel alive."

> [!quote] Source
> **Author:** Joel "Roomie" Berghult — **Date:** 2024-09-06 — **Channel:** #production-talk — 13 reactions
> "I spent so many hours over the last few years trying to make Guitar VST:s work for realism (for time/travel purposes), and it's always a pain. Tracked a real guitar for 20 minutes and it blew away hours of programming."

Community consensus: virtual instruments are powerful tools but tracking even a brief real performance usually elevates the result.

### Piano and Keys

The channel was literally founded on this topic — oaklandmatt's first post (12 reactions) asked "what y'all using for piano":

- **[[Keyscape]]** by Spectrasonics — widely recommended for realistic acoustic and electric pianos
- **Alicia's Keys** by Native Instruments — popular but oaklandmatt expressed being "sick of" its character
- **Addictive Keys** — lightweight alternative favored for pop production
- **Noire** by Native Instruments — recommended for atmospheric/textural piano

### Recommended Virtual Instruments

From community discussion:
- **Synths:** Arturia V Collection (cian riordan, 11 reactions: "invested over a decade ago and have yet to need another software synth"), [[Serum]], [[Vital]], Omnisphere
- **Drums:** [[Superior Drummer]], [[EZDrummer]], Battery, Addictive Drums
- **Orchestra:** Spitfire, 8Dio, EastWest, Kontakt libraries
- **Keys:** [[Keyscape]], Alicia's Keys, Addictive Keys

### Transient Shaping for Virtual Instruments

> [!quote] Source
> **Author:** youngteam — **Date:** 2024-08-23 — **Channel:** #production-talk — 8 reactions
> "Just want to share some sauce that khs transient shaper has changed my life lately. I've been on the hunt for a good ZERO LATENCY transient designer and this thing just fucks. Attack, decay, a mid env."

## Practical Application

- Automate CC1 (modulation) and CC11 (expression) on orchestral instruments — static MIDI lines sound artificial
- Blend even a single real instrument recording with virtual beds for dramatic realism improvement
- Choose virtual instruments based on the mix context — a solo virtual piano needs more realism than one buried in a dense arrangement
- Use transient shapers to add life and definition to virtual instrument recordings
- Build templates with articulation switching pre-configured to speed up orchestral programming

## Common Mistakes

- Relying solely on velocity for dynamics without expression/modulation automation
- Spending hours trying to make a virtual instrument sound "real" when 20 minutes of tracking would be better
- Using too many different virtual instruments when one well-programmed library would be more cohesive
- Ignoring MIDI latency compensation when layering virtual instruments with live recordings
- Not using keyswitches/expression maps for articulation switching in orchestral programming

## See Also

- [[Sound Design in DAWs]] — synthesis techniques and workflow
- [[Sampling and Sample Libraries]] — sample-based instruments and libraries
- [[Songwriting and Arrangement]] — arrangement context for instrument choices
- [[Plugin Ecosystem Overview]] — virtual instrument formats and compatibility
- [[Melodyne]] — pitch correction for virtual and recorded instruments

## Source Discussions

> [!quote] Discord Source
> **Channel:** #production-talk — **Date Range:** 2022-01 to 2026-02
> **Key contributors:** LAPhill, cian riordan, Joel "Roomie" Berghult, oaklandmatt, youngteam, Slow Hand
> **Message volume:** 331 MIDI/virtual instruments + 249 keys/piano categorized messages
