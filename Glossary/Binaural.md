---
type: glossary
confidence: medium
aliases:
  - Binaural Audio
  - Binaural Rendering
tags:
  - type/glossary
  - channel/atmos-talk
created: 2026-02-17
modified: 2026-02-18
---

# Binaural

## Definition

Audio technique that uses two channels to create a 3D stereo sound experience, simulating how human ears perceive spatial audio. In recording, this involves capturing with two microphones placed at ear positions (often on a dummy head). In rendering, algorithms apply [[HRTF]] (Head-Related Transfer Function) processing to simulate 3D positioning over headphones.

## Context

In Dolby Atmos workflows, binaural rendering is the primary monitoring and playback method for headphone listeners — which represents the vast majority of Atmos consumption. Two competing binaural renderers exist:

- **Dolby Binaural** — respects the near/mid/far object distance settings chosen during mixing in the [[Dolby Atmos Renderer]]
- **Apple Spatial Audio** — ignores Dolby's binaural metadata entirely, applying its own undocumented spatialization with head tracking on AirPods and compatible headphones

This difference is the single biggest practical challenge in Atmos mixing. Matt Huber's testing showed up to 4.5 dB level differences between the two renderers when using objects, but near-identical translation when using bed tracks. Most professional Atmos mixers check both renders and make compromise decisions.

Apple offers personalized HRTF via iPhone ear scanning to improve spatial accuracy. Dolby has developed a personalized HRTF beta program. For binaural recording, the [[Neumann KU 100]] binaural head (~$7,000) is the reference standard, while the 3Dio Free Space (~$500) and DPA binaural kits offer more affordable options.

## Related Terms

- [[HRTF]]
- [[Dolby Atmos]]
- [[Dolby Atmos Renderer]]

## See Also

- [[Dolby Atmos and Immersive Audio]]
- [[Spatial Audio and Dolby Atmos]]
