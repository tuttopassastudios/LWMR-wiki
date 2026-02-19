---
type: glossary
confidence: high
aliases:
  - Mixbus
  - 2-Bus
  - Two Bus
  - Stereo Bus
  - Master Bus
  - Master Fader
tags:
  - type/glossary
  - channel/mixing-talk
created: 2026-02-18
modified: 2026-02-18
---

# Mix Bus

## Definition

The final stereo output bus where all mix elements are summed before leaving the DAW or console. Also called the "2-bus," "stereo bus," "master bus," or "master fader." The mix bus is typically the last point where mix processing (compression, EQ, saturation, limiting) is applied before printing or sending to mastering.

## Context

The mix bus is one of the most discussed routing concepts in #mixing-talk (800 categorized messages about bus processing). The community debates what processing belongs on the mix bus, in what order, and how much is appropriate.

Key community positions:
- **Mix into the bus chain** from the start — don't add bus processing after the mix is finished
- **Restraint is essential** — 1-3 dB of compression, subtle EQ, gentle saturation. Nomograph Mastering: "people doing fucked up shit on the mix bus is how I feed my children"
- **Front bus / background bus** architecture (Matt Huber, bobby k) splits the mix into two sub-buses before they hit the final mix bus, allowing differentiated processing

In DAWs, the mix bus is typically the "Master" or "Stereo Out" channel. All submixes ([[Bus]] groups, aux sends) route to the mix bus.

## Related Terms

- [[Bus]]
- [[Mix Bus Processing]]
- [[SSL Bus Compressor]]
- [[Gain Staging]]

## See Also

- [[Mixing in the DAW]]
- [[DAW Routing and Signal Flow]]
