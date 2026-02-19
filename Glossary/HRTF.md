---
type: glossary
confidence: medium
aliases:
  - Head-Related Transfer Function
tags:
  - type/glossary
  - channel/atmos-talk
created: 2026-02-18
modified: 2026-02-18
---

# HRTF

## Definition

Head-Related Transfer Function — the mathematical description of how sound is filtered by the shape of a listener's head, ears (pinnae), and torso before reaching the eardrums. HRTFs are the foundation of binaural rendering, enabling headphone playback to simulate sounds coming from specific positions in three-dimensional space.

## Context

In Dolby Atmos workflows, HRTF profiles determine how convincing the [[Binaural|binaural]] headphone render sounds. Generic HRTFs work for most listeners but can produce inaccurate localization — particularly for height perception. Dolby has developed a personalized HRTF beta program, and Apple uses ear scanning (via iPhone) to customize Spatial Audio processing for individual listeners. The [[Neumann KU 100]] binaural head physically models a generic HRTF with its head shape, while the 3Dio binaural microphone uses ear-shaped baffles without a full head model. DIY binaural setups (foam mannequin heads with small-diaphragm mics) perform more like a baffle than a true HRTF but still produce a binaural effect.

## Related Terms

- [[Binaural]]
- [[Dolby Atmos]]
- [[Dolby Atmos Renderer]]

## See Also

- [[Dolby Atmos and Immersive Audio]]
- [[Atmos Monitoring and Speaker Setup]]
