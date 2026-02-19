---
type: topic
confidence: high
aliases:
  - Low End Control
  - Bass Management
  - Sub Management
tags:
  - domain/mixing
  - type/topic
  - channel/mixing-talk
created: 2026-02-18
modified: 2026-02-18
---

# Low End Management

## Summary

> [!abstract]
> Low end management is one of the most frequently discussed mixing challenges in #mixing-talk with 2,203 categorized messages. The community's core insight is counterintuitive: bass instruments are "defined by the midrange and high end" and merely "supported by the low end" (cian riordan). Key techniques include high-pass filtering strategy, kick/bass frequency pocketing, mono bass below ~200Hz, mid-side EQ for bass clarity, and subtractive approaches to carving space. Nomograph Mastering's FFT analysis posts provide the channel's most technical low-end resources.

## Detail

### The Fundamental Insight

> [!quote] Source
> **Author:** cian riordan — **Date:** 2025-07-25 — **Channel:** #mixing-talk
> "Something to chew on: bass instruments, kick drums, et all — they're not defined by the low end, they're defined by the midrange and high end. They're just supported by the low end."

This perspective reframes low end management: rather than obsessing over sub frequencies, the community emphasizes that perceived bass quality comes from upper harmonics and midrange presence, while the sub frequencies simply provide weight and "feel."

### High-Pass Filter Strategy

High-pass filtering (HPF) is the most basic and most discussed low-end tool:

- **Not everything needs a high-pass filter** — the community pushes back against "HPF everything" advice from YouTube
- **Gentle slopes (6-12 dB/oct)** are preferred over steep slopes to avoid unnatural thinning
- **Cut below where the instrument actually has useful content** — a vocal HPF at 80Hz is common, but pushing it to 200Hz will thin the voice
- **The kick drum HPF** should remove rumble below the fundamental (~30-40Hz) without cutting the punch
- **Bass guitar HPF** is controversial — some members HPF at 30-40Hz, others leave it wide open

> [!quote] Source
> **Author:** cian riordan — **Date:** 2024-05-28 — **Channel:** #mixing-talk
> "If the synth is extremely subby, consider pushing in some midrange via EQ or saturation to help define it in the mix."

### Kick/Bass Relationship

The kick and bass competing for low-end space is the defining mixing challenge:

- **Frequency pocketing:** Identify the kick's fundamental (50-80Hz) and boost the bass slightly above or below, or vice versa
- **Sidechain compression:** The kick triggers gentle compression on the bass, creating momentary space for each kick hit
- **Choose a leader:** Decide whether the kick or bass "owns" the sub frequencies for a given song, and shape the other around it
- **Saturation on bass:** Adding harmonic content to the bass via saturation makes it audible on small speakers where sub frequencies are inaudible

### Mono Bass

The community consensus is that low frequencies (below ~150-200Hz) should be mono:

- Low frequencies in stereo cause phase cancellation issues on varied playback systems
- Mid-side EQ with a high-pass on the side channel is a clean way to mono the bass
- Colin Althaus provided a detailed technical explanation of how HPF on only the Side channel affects phase relationships below the cutoff frequency

### FFT and Spectral Analysis

Nomograph Mastering's pinned posts on FFT analysis provide technical depth on low-end frequency behavior:

> [!quote] Source
> **Author:** Nomograph Mastering — **Date:** 2024-02-21 — **Channel:** #mixing-talk
> "Anyone who has experience with something like Plugin Alliance Paul Frindle's DSM will know that it's excellent at high mid and high frequency manipulation but at 16 bands has almost no low end resolution."

This insight — that FFT-based processors have inherently lower resolution at low frequencies due to how logarithmic frequency scales map onto linear FFT bins — is critical for understanding why some "smart" EQ tools struggle with bass.

### Mud, Boxiness, and Problem Frequencies

Common problem areas in the low-mid range:

- **200-300Hz:** "Mud" — excess here makes mixes sound thick and unfocused
- **300-500Hz:** "Boxiness" — room resonances and cabinet coloration often pile up here
- **Subtractive approach:** Cutting problem frequencies is more effective than boosting desired frequencies for low-end clarity
- Matt Huber's approach: go track by track, listening for and EQing out frequencies that mask other elements

## Practical Application

- Define bass instruments with midrange and harmonic content, not just sub frequencies
- Use gentle HPF slopes (6-12 dB/oct) and cut below where useful content actually exists
- Decide whether kick or bass "owns" the sub frequencies for each song
- Keep bass mono below 150-200Hz using mid-side EQ
- Address 200-500Hz mud and boxiness with surgical subtractive EQ

## Common Mistakes

- Aggressively high-passing everything and creating a thin, weightless mix
- Boosting sub frequencies on bass instead of adding midrange definition
- Leaving bass in stereo below 200Hz, causing phase cancellation on mono/near-mono systems
- Not addressing the kick/bass relationship specifically — hoping "it'll work out" in mastering
- Relying on subwoofers for low-end decisions without checking on headphones and small speakers

### Bass Production Perspective (from #production-talk)

#production-talk adds 268 messages on bass production — focusing on the **creative/production side** of low-end management:

> [!quote] Source
> **Author:** cian riordan — **Date:** 2024-09-09 — **Channel:** #production-talk — 15 reactions
> "Often when I'm recording drums I'll track the drummer at a higher BPM then varispeed everything down to tempo... great way to get deep low end."

> [!quote] Source
> **Author:** peterlabberton — **Date:** 2022-09-11 — **Channel:** #production-talk — 13 reactions
> "If you have your monitoring sorted out, these sub decisions become way more intuitive and effortless. If you're just guessing on headphones, you're going to second-guess everything."

> [!quote] Source
> **Author:** Slow Hand — **Date:** 2022-07-18 — **Channel:** #production-talk — 10 reactions
> "Obviously starting with the right bass is going to get you 70% of the way there, but you know what really surprised the hell out of me? The *strings*. If you're not getting anywhere close to the low end you want, look at what's happening above the bass."

Key production-talk bass insights:
- **Varispeed technique** — recording at higher tempo and slowing down creates deep, natural-sounding low end
- **Monitoring is foundational** — sub decisions are nearly impossible to make accurately without proper monitoring
- **808 development** — Skyler Young is building a custom 808/synth bass plugin because existing tools (808 Cooker, SubLab) have room for improvement
- **Bass lives in the arrangement** — the strings, guitars, and other mid-range instruments define how the bass is perceived

## See Also

- [[Drum Mixing]] — kick drum processing
- [[Gain Staging]] — levels and headroom in the low end
- [[Reference Mixing and Translation]] — checking low end on multiple systems
- [[Mix Bus Processing]] — bus chain impact on low end
- [[Beat Making and Drum Programming]] — 808 and bass programming

## Source Discussions

> [!quote] Discord Source
> **Channel:** #mixing-talk — **Date Range:** 2021-08 to 2026-02
> **Key contributors:** cian riordan, Nomograph Mastering, spectrummasters, Colin Althaus, Edward Rivera, peterlabberton
> **Message volume:** 2,203 categorized messages

> [!quote] Discord Source
> **Channel:** #production-talk — **Date Range:** 2022-01 to 2026-02
> **Key contributors:** cian riordan, peterlabberton, Slow Hand, Skyler Young, Eric Martin
> **Message volume:** 268 bass production categorized messages
> See also: [[production-talk Channel Summary]]
