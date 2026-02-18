---
type: software
confidence: medium
aliases:
  - Sonarworks
  - SoundID Reference
  - Sonarworks Reference
tags:
  - type/software
  - software/plugins
manufacturer: Sonarworks
category: Plugin
price_range: $100–$300
created: 2026-02-17
modified: 2026-02-17
---

# Sonarworks SoundID

## Summary

> [!abstract]
> Sonarworks SoundID Reference is a room/speaker correction system that measures your monitoring environment and applies corrective EQ to flatten the frequency response. With 25 mentions across 16 threads, it is discussed in the context of improving monitoring accuracy. Key considerations include its interaction with monitor controllers (mono buttons, volume control) and whether it should be used as a DAW plugin or system-wide application.

## Key Characteristics

- Measures room and speaker response, then applies corrective EQ curves
- Available as DAW plugin or system-wide application
- Applies different correction curves to left and right speakers independently
- Headphone calibration profiles included
- Interacts complexly with hardware monitor controllers (mono buttons, etc.)

## Use Cases

- Flattening monitoring frequency response in untreated or partially treated rooms
- Headphone calibration for consistent mixing on headphones
- Reference monitoring for critical listening
- Improving translation of mixes across playback systems

## Settings & Sweet Spots

- Use the system-wide version to avoid mono button conflicts with DAW plugin version
- When using as DAW plugin, place as last plugin on master chain
- Mono fold-down from hardware monitor controller will not work correctly with DAW plugin version due to independent L/R correction curves

## Comparable Alternatives

| Product | Notes |
|---------|-------|
| IK Multimedia ARC | Similar room correction system |
| Dirac Live | Room correction for monitoring |
| Hardware monitor controller EQ | Manual approach without measurement |
| Proper acoustic treatment | "Almost always monitoring and room treatment" should come first |

## Common Mistakes

- Using the DAW plugin version and expecting hardware mono buttons to work correctly — "the mono-button would have to come in front of the Sonarworks plugin"
- Relying on Sonarworks instead of investing in proper acoustic treatment
- Not understanding that L/R have different correction curves, which affects mono compatibility checking

## See Also

- [[FabFilter]]
- [[iZotope]]

## Source Discussions

> [!quote] Community Insights
> "My right and left speaker have different correction curves applied so the mono-button would have to come in front of the Sonarworks plugin right?" — rse
>
> "9 times out of 10 I tell them that what they have is usually more than adequate. This 'x' and 'y' is almost always monitoring and room treatment." — cian riordan (on prioritizing monitoring over gear)

> [!quote] francoslate — Bass trapping vs Sonarworks (#monitoring-talk, July 2021)
> "I recently got my large garage treated by a popular company here — all main reflection points have been treated and it sounds nicely dead at the listening position. However on Fuzz Measure it seems a lot of my low frequencies are ringing for 1 second or even a little more. Im understanding this to mean that I would need more bass trapping, but some other producer friends have done similar treatments just getting the reflection points covered, then using Sonarworks, and seem to get mixes translating very well."

> [!quote] Discord Source
> Channel: #🔈monitoring-talk
> Messages: 22
> Date range: April 2021 – March 2022
> Key contributors: David Fuller, francoslate, cian riordan
> Notable: Community debate on room correction software vs physical treatment — consensus favors treatment first, Sonarworks as supplement
> See also: [[monitoring-talk Channel Summary]]
