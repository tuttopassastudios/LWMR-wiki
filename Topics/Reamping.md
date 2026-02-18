---
type: topic
confidence: high
aliases:
  - Re-amping
  - Reamp
  - DI Recording
tags:
  - type/topic
  - domain/recording
created: 2026-02-17
modified: 2026-02-17
---

# Reamping

## Overview
> [!abstract]
> Reamping is the process of sending a previously recorded clean/DI signal back out through amplifiers, pedals, or other outboard gear to capture new tonal variations without requiring the musician to re-perform. This guide covers DI box selection, signal splitting workflows, reamp boxes, and the philosophical debates around when reamping is and is not appropriate.

## Community Consensus

- **Always capture a clean DI** when recording electric guitar or bass -- even if you love the amp tone, having the DI gives you editing reference and creative options later
- **Signal splitting quality matters** if you plan to do serious reamping; a simple Y-cable technically works but dedicated splitters preserve impedance and tone
- **Fuzz pedals and passive pickups** have a unique impedance interaction -- germanium fuzzes especially need to "see" the pickup directly, which complicates DI placement in the chain
- **Test tones are essential** before reamping to calibrate latency and phase alignment between the original and reamped signals
- **The performance is linked to the sound** -- a guitarist plays differently through a cranked Marshall than a clean DI, so reamping is best for tonal variations rather than completely replacing a committed sound

## Key Approaches

### The Standard Reamp Workflow
1. Record clean DI signal (instrument → DI box → interface) simultaneously with the amp/wet signal
2. Edit and comp the DI track as needed in the DAW
3. Send DI out from DAW through a reamp box (converts line level back to instrument level)
4. Run through amp/pedal chain and mic the result
5. Record the reamped signal back into the DAW
6. Align timing using the test tone offset

### Signal Splitting Options
| Approach | Pros | Cons |
|----------|------|------|
| Dedicated DI/Splitter ([[Radial JDI]], [[Radial J48]]) | Clean split, proper impedance | Cost |
| [[Little Labs PCP Instrument Distro]] | Studio-grade, solves impedance issues every session | ~$500+ |
| [[Little Labs RedEye]] | Reamp + DI in one box | Higher cost |
| Tuner pedal bypass out (Boss TU-2/TU-3) | Budget-friendly, already on pedalboard | Lower signal quality |
| Y-cable | Cheapest option | Impedance issues, signal degradation |

### DI Box Recommendations
- **[[Radial J48]]** -- Community favorite for active DI when using pedals; pedals respond properly to its output impedance
- **[[Radial JDI]]** -- Excellent passive option for clean DI duties
- **[[Rupert Neve Designs RNDI]]** -- Praised for its large, open sound; several members preferred it over the J48
- **[[Countryman Type 85]]** -- Reliable workhorse, longtime studio standard
- **[[Teegarden DI]]** -- Less "vibey" but equally large sounding

## Common Debates

### "Safety DI" vs Committed Performance
> [!quote] Ross Fortune
> "The reason I say fuck getting a safety btw: the guitarist will play into the sound - the performance will be inextricably linked with whatever they've played into."

The community is split on whether capturing a clean DI is essential insurance or an unnecessary crutch. The pragmatic middle ground: capture the DI for editing reference (you can see transients clearly on a clean signal), but do not plan to use it as a replacement for the amp tone.

### Passive vs Active DI for Splitting
- **Passive DI before pedals** with passive pickups = "gonna be kinda a bummer" (BatMeckley)
- **Active DI (J48)** recommended when pedals are in the chain, as some pedals (especially bass effects) do not respond the same way through a passive DI
- The [[Little Labs PCP]] is the "solve every problem in every session" tool for those who can afford it

### Fuzz Pedal Impedance
Germanium fuzzes interact directly with pickup impedance. Placing any buffer or DI between the guitar and a fuzz changes the sound fundamentally. As BatMeckley noted, this is why Matt Bellamy has fuzz factories built directly into his guitars. This is physics, not opinion -- but whether you care about the difference is subjective.

## Recommended Gear

| Category | Budget | Mid-Range | High-End |
|----------|--------|-----------|----------|
| Active DI | [[Radial J48]] (~$200) | [[Rupert Neve Designs RNDI]] (~$270) | [[Little Labs PCP]] (~$500) |
| Passive DI | [[Radial JDI]] (~$200) | -- | -- |
| Reamp Box | [[Radial ProRMP]] | [[Little Labs RedEye]] | [[Radial JD7]] (multi-amp splitting) |
| Splitter | Boss TU-2/TU-3 bypass | [[Radial JD7]] | [[Little Labs PCP Instrument Distro]] |

## Tips from the Community

- **Always run a test tone** through your entire reamp chain before committing. This lets you measure exact latency and check for phase flips. Some pedals invert phase, which will cause issues if you blend reamped and DI signals
- **Line up returns sample-accurate** -- even working at the same sample rate, always verify latency through the chain
- When reamping through pedals with a dry signal bleed (like the Boss DM-2), run a test tone first so you can time-align the blended return and avoid phasing
- The quality of the DI matters more if you plan to reamp through high-gain amps; for editing reference only, almost anything works
- Consider reamping vocals and synths through guitar pedals for creative effects -- not just guitars
- If budget is extremely tight, a tuner pedal with a bypass output can serve as a basic signal splitter

## Common Mistakes

- **Reamping as a replacement for commitment** -- Recording a lifeless DI with plans to "fix it in reamp" usually results in a lifeless performance through a good amp
- **Ignoring impedance matching** -- Running a line-level DAW output directly into a guitar amp without a reamp box results in level and impedance mismatches that sound harsh and wrong
- **Forgetting to check phase** -- Blending a DI and reamped signal without checking for phase cancellation
- **Placing DI before fuzz pedals** with passive pickups, then wondering why the fuzz sounds different
- **Not accounting for latency drift** -- Especially when reamping through analog gear, DA/AD conversion adds latency that must be compensated

## See Also
- [[Cables and Connectivity Guide]]
- [[Outboard vs In-The-Box]]
- [[Recording and Tracking Workflows]]
- [[DIY and Clone Gear]]

## Recording-Talk Perspectives

### Creative Reamping
A Deleted User shared their approach: "Reamp through the pedals and the Spamp recorded back in with the Peluso 47" -- using reamping for creative vocal reverb effects, not just guitar tones.

### Guitar Recording Context
The #recording-talk channel reinforces that the DI is essential even when the amp tone is perfect -- it serves as an editing reference where transients are clearly visible. See [[Guitar Recording]] and [[Bass Recording]] for instrument-specific DI workflows.

## Source Discussions
> [!quote] Discord Source
> Channel: #gear-talk
> Matches: 173
> Key contributors: hyanrarvey, Zack Hames, Bryan DiMaio, BatMeckley, Eric Martin, cian riordan, Ross Fortune, NoahNeedleman, David Fuller

> [!quote] Discord Source
> Channel: #recording-talk
> Key contributors: cian riordan, BatMeckley, Zack Hames
