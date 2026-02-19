---
type: topic
confidence: high
aliases:
  - Drum Mix
  - Mixing Drums
  - Drum Bus Techniques
tags:
  - domain/mixing
  - type/topic
  - channel/mixing-talk
created: 2026-02-18
modified: 2026-02-18
---

# Drum Mixing

## Summary

> [!abstract]
> Drum mixing is one of the most discussed instrument-specific topics in #mixing-talk with 1,539 categorized messages. The community covers kick/snare/overhead balance, parallel drum compression, drum bus processing, sample augmentation, and genre-specific approaches. Ross Fortune's pinned methodology for rebalancing drums from scratch is a foundational resource. A core insight from cian riordan is that drums (like bass) are "defined by the midrange, not the low end" — low frequencies support, but midrange and high frequencies define.

## Detail

### Drum Balance Philosophy

Ross Fortune's pinned drum rebalancing methodology represents the community's recommended starting point:

> [!quote] Source
> **Author:** Ross Fortune — **Date:** 2023-01-28 — **Channel:** #mixing-talk
> "If I'm totally rebalancing drums, I'll treat them as if I'm tracking them myself and building a basic working drum sound."

The approach: start from scratch with overheads as the foundation, then layer in close mics to supplement what the overheads don't capture well.

### Kick Drum

- High-pass the kick at 30-40Hz to remove sub-rumble below the fundamental
- The "attack" or "click" lives around 3-5kHz — boost here for definition in dense mixes
- The "body" or "thump" lives around 60-100Hz
- Side-chain compress the bass to duck with the kick for low-end clarity
- Sample augmentation (blending a triggered sample with the live kick) is common for consistent level

### Snare

- Snare "crack" lives around 2-4kHz; "body" around 200-300Hz; "ring" around 800Hz-1kHz
- Gate or strip silence on snare close mics to reduce bleed
- Parallel compression on the snare adds sustain and fatness without losing the initial transient
- Top and bottom snare mics may need phase alignment — flip the phase on the bottom mic as a starting point

### Overheads and Cymbals

- Overheads are the stereo picture of the entire kit — they should sound like a "drum kit" before close mics are added
- High-pass overheads at 200-500Hz when relying on close mics for kick and snare body
- cian riordan advocates for getting overheads to sound great first, then using close mics to fill gaps

### Toms

> [!quote] Source
> **Author:** cian riordan — **Date:** 2025-08-13 — **Channel:** #mixing-talk
> "Toms are like the kids in the back of the station wagon, they're going where everyone else is going."

Toms are typically gated or manually edited to remove bleed between hits, then treated with gentle compression and EQ to sit naturally in the kit balance. They rarely need aggressive individual processing.

### Parallel Drum Compression

Parallel compression on the drum bus is one of the most widely recommended techniques:

- [[UREI 1176]] all-buttons mode on a parallel send is the classic approach
- Crush the parallel bus — high ratio, fast attack, fast release — then blend to taste
- The parallel bus adds sustain, body, and excitement without squashing the transients of the main drum bus
- Some members use the [[Empirical Labs Distressor]] at 10:1 or 20:1 for parallel drums

### Drum Bus Processing

The drum bus (all drums summed to one stereo bus) typically receives:

1. **Bus compression** — [[SSL Bus Compressor]] style, 4:1, slow attack to let transients through
2. **EQ** — subtle tonal shaping, often a shelf boost on the top end
3. **Saturation** — gentle tape or tube saturation for cohesion and warmth
4. **Parallel send** — heavily compressed parallel bus blended back in

### Sample Augmentation

The community accepts drum sample augmentation as a standard modern technique:

- Slate Trigger, Superior Drummer, and SSD5 are commonly used triggers
- Samples are blended with live drums — not replacing them entirely
- Triggered samples need to be time-aligned with the live drums
- cian riordan's pinned "tariffs on sessions with drum samples that don't line up with the original" reflects the importance of proper alignment

## Practical Application

- Start with overheads — get them sounding like a balanced kit before reaching for close mics
- Use parallel compression via a dedicated send, not a wet/dry knob
- High-pass the kick to remove sub-rumble, not the fundamental
- Gate or edit toms to remove bleed between hits
- Check drum bus phase — flip polarity on room mics and bottom snare mic and listen for improvement

## Common Mistakes

- Building the drum sound from close mics up instead of overheads down
- Over-gating and creating unnatural, machine-like drum sounds
- Not checking phase relationships between close mics and overheads
- Over-compressing the drum bus and losing punch and transient impact
- Using drum samples that don't time-align with the original performance

### Drum Production Perspective (from #production-talk)

#production-talk adds 593 messages on drum programming and production — complementing the mixing perspective with **creative production techniques**:

> [!quote] Source
> **Author:** Rollmottle — **Date:** 2024-11-26 — **Channel:** #production-talk — 11 reactions
> "Adding stuff is always effective but I like trying to pare back the arrangement to see if I can get away with something. Dropping the kick, the bass or snare for a bar, 1/2 a bar, or one beat can sometimes give you the push and pull you were looking for."

> [!quote] Source
> **Author:** cian riordan — **Date:** 2024-09-09 — **Channel:** #production-talk — 15 reactions
> "Often when I'm recording drums I'll track the drummer at a higher BPM then varispeed everything down to tempo... great way to get deep low end."

Key production-talk drum insights:
- **Percussion is "the sauce"** — esquinalee (12 reactions): live percussion brings life to programmed grooves, but tambourine requires responsibility
- **Click track alternatives** — BatMeckley: "Putting down a drum loop solved a singer's timing issue today"
- **Assembled vs performed** — Dr. Luke and other top producers regularly cut and paste individual hits rather than playing full takes
- **Sample augmentation** — Slow Hand (22 reactions): adding noise tail to a muted kick for decay and presence

## See Also

- [[Drum Recording Techniques]] — tracking drums
- [[Compression Techniques]] — parallel and bus compression
- [[Low End Management]] — kick/bass relationship
- [[Mix Bus Processing]] — downstream bus processing
- [[Beat Making and Drum Programming]] — drum programming from production perspective

## Source Discussions

> [!quote] Discord Source
> **Channel:** #mixing-talk — **Date Range:** 2021-08 to 2026-02
> **Key contributors:** cian riordan, Ross Fortune, hyanrarvey, BatMeckley, JustinLeu, Matt Huber
> **Message volume:** 1,539 categorized messages

> [!quote] Discord Source
> **Channel:** #production-talk — **Date Range:** 2022-01 to 2026-02
> **Key contributors:** spectrummasters (34 msgs), Zack Hames (30 msgs), Ross Fortune (31 msgs), BatMeckley, Rollmottle, cian riordan
> **Message volume:** 593 categorized messages
> See also: [[production-talk Channel Summary]]
