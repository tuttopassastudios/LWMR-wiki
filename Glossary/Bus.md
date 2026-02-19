---
type: glossary
confidence: medium
aliases:
  - Buss
  - Audio Bus
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-18
---

# Bus

## Definition

A virtual audio pathway that combines multiple signals for group processing. Used for submixing (drum bus, vocal bus, instrument bus) and parallel processing. The term originates from analog console architecture where physical bus bars carried combined signals.

## Context

Bus routing is a core mixing technique. Common uses include grouping all drum tracks to a drum bus for cohesive compression and EQ, routing vocals to a vocal bus for group processing, and creating parallel processing chains. The routing capabilities and ease of bus creation vary by DAW — [[Cubase]] and [[Pro Tools]] are frequently cited for flexible bus routing, while [[Ableton Live]]'s Group Tracks serve a similar function with a different workflow.

## Related Terms

- [[Aux Track]]
- [[VCA]]
- [[Summing]]
- [[Sidechain]]

## Bus Architecture (from #mixing-talk)

In #mixing-talk (800 mix bus messages), bus architecture is a central mixing topic:

- **Front bus / background bus:** Matt Huber and bobby k champion splitting the mix into two sub-buses — a "front bus" (vocal, lead instruments) and "background bus" (pads, ambience, supporting elements) — each with differentiated processing before hitting the [[Mix Bus]]
- **Drum bus:** Universally used — all drum elements routed to a drum bus for cohesive compression and EQ. [[SSL Bus Compressor]] at 4:1 with slow attack is the community standard
- **Vocal bus:** All vocal elements (lead, doubles, BGVs, ad-libs) routed to a vocal bus for group compression and shared reverb sends
- **Parallel bus:** A dedicated bus for parallel compression — heavily compressed signal blended back with the unprocessed audio
- See also [[Mix Bus]] for the dedicated glossary entry on the stereo output bus

## See Also

- [[Mixing in the DAW]]
- [[DAW Comparison]]
- [[Mix Bus]]
- [[Mix Bus Processing]]
- [[VCA]]
