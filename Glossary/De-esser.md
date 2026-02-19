---
type: glossary
confidence: medium
aliases:
  - De-ess
  - Desser
  - Sibilance Control
tags:
  - type/glossary
created: 2026-02-17
modified: 2026-02-18
---

# De-esser

## Definition

Audio processor that reduces sibilance (harsh "s" and "sh" sounds) in vocal recordings by applying frequency-specific dynamic compression, typically in the 4-10kHz range.

## Context

De-essers are a standard part of vocal processing chains in DAW mixing workflows. They can operate in wideband mode (compressing the entire signal when sibilance is detected) or split-band mode (only compressing the targeted frequency range). Common de-esser plugins include FabFilter Pro-DS, Waves DeEsser, and stock de-essers included in most DAWs.

## Related Terms

- [[Advanced Mixing Techniques]]
- [[Vocal Editing Across DAWs]]

## Mixing Techniques (from #mixing-talk)

In #mixing-talk's vocal mixing discussions (2,741 messages), de-essing is one of the most discussed vocal processing steps:

- **Placement in the chain:** The community consensus is to place the de-esser **after compression**, since compression can exaggerate sibilance. Some engineers use a gentle de-esser both before and after compression
- **Multiple light instances vs one heavy instance:** Using 2-3 de-essers doing light work produces more transparent results than one de-esser working hard
- **Split-band vs wideband:** Split-band mode (only compressing the sibilant frequency range) is generally preferred for transparency
- **Manual de-essing:** The most natural approach — using clip gain to manually reduce individual sibilant peaks — but the most time-consuming
- **BatMeckley's FabFilter approach (pinned):** Using FabFilter Pro-MB's dynamic bands as a precision de-esser for particularly problematic vocal resonances that standard de-essers can't handle

## See Also

- [[Mixing in the DAW]]
- [[Vocal Mixing]]
- [[Compression Techniques]]
