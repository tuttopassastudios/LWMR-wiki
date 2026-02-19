---
type: glossary
confidence: medium
aliases:
  - Ground Loop Hum
tags:
  - type/glossary
  - channel/newbie-questions
created: 2026-02-18
modified: 2026-02-18
---

# Ground Loop

## Definition

An unwanted electrical condition that occurs when multiple pieces of equipment are connected to different ground points, creating a loop through which current flows and produces an audible 50/60Hz hum (depending on AC frequency). Ground loops are one of the most common sources of noise in home and project studios.

## Context

Ground loop hum is a frequent troubleshooting topic in #newbie-questions. The classic symptom is a constant low-frequency hum or buzz that persists regardless of gain settings.

### Common Fixes

1. **Plug all audio gear into the same power strip/outlet** — eliminates potential differences between ground points
2. **Use a DI box with ground lift** — breaks the ground loop path (see [[DI Box]])
3. **Check cable connections** — damaged or poorly shielded cables exacerbate the problem
4. **Isolate the source** — disconnect gear one piece at a time to identify which connection creates the loop
5. **Use balanced cables (XLR/TRS)** — balanced connections reject common-mode noise including ground loop artifacts

### What NOT to Do

- **Never use a ground lift adapter ("cheater plug")** on your main power — this removes the safety ground and creates an electrocution hazard
- **Don't assume it's a software issue** — ground loops are always electrical/physical

## Related Terms

- [[XLR]]
- [[DI Box]]
- [[Power Conditioning]]
- [[Cables and Connectivity Guide]]

## See Also

- [[Troubleshooting DAW Issues]]
- [[Beginner FAQ#Troubleshooting]]
