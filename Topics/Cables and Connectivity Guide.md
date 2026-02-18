---
type: topic
confidence: high
aliases:
  - Cables
  - Audio Connectivity
  - MADI
  - Dante
  - Patchbays
tags:
  - type/topic
  - domain/hardware
created: 2026-02-17
modified: 2026-02-17
---

# Cables and Connectivity Guide

## Overview
> [!abstract]
> Cables and connectivity are the circulatory system of any studio. This guide covers analog cable types and recommendations, digital audio networking protocols (Dante, MADI, AES/EBU), patchbay wiring, and the community's strong opinions on what works and what causes nightmares in real-world studio environments.

## Community Consensus

- **Cables matter, but not in the audiophile sense** -- Use quality, reliable cables; do not spend hundreds on "boutique" audio cables
- **Mogami and Canare** are the community-standard bulk cable brands
- **Neutrik connectors** are the go-to for XLR and TRS
- **Dante is powerful but problematic** in many real-world deployments
- **MADI is more reliable** than Dante for mission-critical applications
- **Make your own cables** -- It is cheaper, you get exact lengths, and it is an essential studio skill
- **Cable length affects guitar tone** -- This is actual physics, not audiophile nonsense

## Analog Cable Types

### XLR (Balanced)
- Standard for microphone connections and balanced line-level signals
- Always use balanced connections where possible to reject interference
- Quality cables: Mogami or Canare cable with Neutrik connectors

### TRS (Balanced)
- 1/4" tip-ring-sleeve for balanced line-level connections
- Common for patchbays, insert points, and monitor connections
- Same cable quality recommendations as XLR

### TS (Unbalanced)
- 1/4" tip-sleeve for instrument-level connections
- Guitar/bass cables, pedal patch cables
- Keep runs as short as possible to minimize noise pickup

### Cable Length and Guitar Tone
Cable capacitance affects the resonant peak of guitar pickups. This is not subtle:
- Longer cables = more capacitance = rolled-off highs and shifted resonant peak
- This is why some guitarists prefer specific cable lengths for tone
- A buffer pedal at the start of the chain mitigates cable capacitance effects

> [!quote] BatMeckley
> "Pete Thorn did this really interesting video showing how cable length actually changed the resonant peak of a pickup based on impedance. It wasn't simply just 'longer means high end gets weaker because of loss.'"

## Digital Audio Networking

### Dante
Dante (Digital Audio Network Through Ethernet) is widely used but has a complicated reputation:

**Pros:**
- Runs over standard Ethernet infrastructure
- Flexible routing through Dante Controller software
- Widely supported by many manufacturers

**Cons (from community experience):**
- Occasional clocking/jitter errors that are difficult to diagnose
- Audinate software updates have bricked hardware (specifically RME Dante boxes)
- Requires networking knowledge that many audio engineers lack
- Troubleshooting during live events is not feasible

> [!quote] SoundsLikeJoe
> "Moving away from Dante after a couple years of field deployment. Found too many negatives for our situation to continue... Recently Audinate pushing a Dante Controller update that bricked the chip in the RME Dante box."

> [!quote] georget113
> "Dante based studios are a nightmare."

> [!quote] chrissorem
> "I used Dante on the regular, there is somewhat complex system, there is about 18 devices online. It's been nothing but a nightmare for me."

> [!quote] Felix Byrne
> "Let's make an audio tool built by network IT admin, what could go wrong."

### MADI (Multichannel Audio Digital Interface)
The community is shifting toward MADI for critical applications:
- More reliable than Dante for mission-critical work
- Point-to-point connections (no network configuration)
- Up to 64 channels on a single cable (coax or fiber)
- Preferred for backup recording and live broadcast

### AES/EBU
- Professional digital audio standard, 2 channels per connection
- Rock-solid reliability
- Common for connecting standalone converters to interfaces

### USB and Thunderbolt
- Standard for interface-to-computer connections
- Thunderbolt offers lower latency than USB in most implementations
- USB-C/Thunderbolt 3+ has largely unified the connector landscape

## Patchbays

### Why Use a Patchbay
- Centralizes all studio connections in one accessible location
- Allows re-routing without crawling behind racks
- Normalled connections maintain default routing while allowing overrides
- Extends the life of gear jacks by reducing plug/unplug cycles

### Patchbay Types
| Type | Behavior | Best For |
|------|----------|----------|
| Full Normal | Top and bottom connected by default; inserting a cable breaks the connection | Signal chains that should always be connected (preamp → interface) |
| Half Normal | Top and bottom connected by default; inserting into top splits signal, inserting into bottom breaks connection | Flexible routing with monitoring capability |
| Open (Thru) | No default connection | Aux sends, effects returns, ad-hoc routing |

### Wiring Recommendations
- Label everything obsessively -- "Future you will thank present you"
- Use consistent cable colors for different signal types
- Keep analog and digital runs separated where possible
- TT (tiny telephone) patchbays are the professional standard but 1/4" TRS bays are more practical for smaller studios

## Recommended Cable Brands

| Category | Budget | Professional |
|----------|--------|-------------|
| Bulk cable | Canare Star Quad | Mogami Neglex |
| XLR connectors | Amphenol | Neutrik |
| TRS connectors | Generic | Neutrik |
| Guitar cables | Pre-made Mogami | Custom Mogami/Canare |
| Patch cables | Hosa (functional) | Mogami, custom-built |

## Studio Wiring Best Practices

### Power and Signal Separation
- Keep audio cables away from power cables -- cross at 90 degrees if they must intersect
- Use balanced connections for any run over 10 feet
- Star grounding where possible to avoid ground loops

### Cable Management
- Velcro ties, not zip ties (zip ties crush cables over time)
- Leave service loops for future re-routing
- Label both ends of every cable
- Document your wiring with photos and diagrams

### Grounding and Noise
- Ground loops are the #1 cause of studio hum/buzz
- Balanced connections reject common-mode noise
- Ground lift switches on DI boxes exist for a reason -- use them when needed
- See [[Power Conditioning]] for more on clean power

## Common Debates

### Cable Quality -- Does It Matter?
- **For analog audio**: Quality construction (good solder joints, proper shielding, strain relief) matters enormously for reliability. Exotic conductor materials do not matter audibly
- **For guitar cables**: Cable capacitance genuinely affects tone. This is measurable and audible
- **For digital audio**: A cable either works or it does not. There is no "better sounding" HDMI or AES cable

### Dante vs MADI vs AVB
- **Dante**: Most flexible, worst reliability track record in the community
- **MADI**: Most reliable, less flexible routing
- **AVB**: Gaining traction but less widely supported
- For fixed installations with IT support: Dante can work well
- For live/location work: MADI is strongly preferred

## Tips from the Community

- Make your own cables. Bulk Mogami + Neutrik connectors + basic soldering skills = huge savings and exact lengths
- Test every cable before installing it in your permanent rig
- Keep spare cables of every type you use in the studio
- When debugging noise issues, swap cables first before assuming gear is broken
- For Dante: keep your audio network on a completely separate switch from your internet/IT network
- Invest in a cable tester -- saves hours of troubleshooting

## Common Mistakes

- **Using unbalanced cables for long runs** -- Guaranteed noise pickup
- **Zip-tying cable bundles too tightly** -- Damages cable over time
- **Running audio and power cables in parallel** -- Creates interference
- **Trusting Dante for mission-critical live applications** without redundancy
- **Not labeling cables** -- Creates chaos during troubleshooting
- **Ignoring cable capacitance** in guitar signal chains
- **Using cheap patch cables in the patchbay** -- The patchbay is only as good as its weakest cable

## See Also
- [[Power Conditioning]]
- [[Reamping]]
- [[AD-DA Conversion]]
- [[DIY and Clone Gear]]
- [[Gear Maintenance and Repair]]

## Source Discussions
> [!quote] Discord Source
> Channel: #gear-talk
> Matches: 700
> Key contributors: Rollmottle, Bryan DiMaio, BatMeckley, David Fuller, cian riordan, Eric Martin, Nomograph Mastering, hyanrarvey, SoundsLikeJoe, Will Melones, Gerhard Westphalen, jantrit, Adam Thein, LAPhill, Ross Fortune
