---
type: topic
confidence: medium
aliases:
  - Speaker Design
  - Crossover Theory
  - Crossover Design
  - Driver Design
  - Cabinet Design
tags:
  - type/topic
  - domain/hardware
  - channel/nerd-talk
created: 2026-02-18
modified: 2026-02-18
---

# Speaker Design and Crossover Theory

## Overview
> [!abstract]
> Speaker design was the single largest topic cluster in #nerd-talk with 145 messages — yet no existing vault page covered the theory behind why monitors sound the way they do. While the vault has gear pages for specific monitors, this page covers the engineering principles: crossover types, driver design, cabinet acoustics, and why understanding speaker design helps engineers make better mixing decisions. The top contributors — Nomograph Mastering (34 msgs), David Fuller (20), and Gerhard Westphalen (19) — brought mastering, electronics, and DSP perspectives respectively.

## Community Consensus

- **Crossover design is the most important factor in a monitor's sound character** — More important than driver quality alone
- **Active crossovers (bi/tri-amped) are superior to passive crossovers** for studio monitoring — This is why most pro monitors are active
- **Cabinet design fundamentally shapes low-frequency response** — Sealed, ported, and bass reflex all have different tradeoffs
- **Understanding speaker design helps you interpret what you hear** — If you know your monitors have a 2.5kHz crossover, you know to be careful about decisions in that region
- **No monitor is perfect** — Every design is a set of engineering compromises; knowing the tradeoffs helps you compensate

## Crossover Types

### What Is a Crossover?
A crossover is a filter network that divides the full-range audio signal into frequency bands, sending each band to the appropriate driver (tweeter, midrange, woofer). The crossover point, slope, and topology all affect the monitor's sound.

### Passive Crossovers
Passive crossovers use inductors, capacitors, and resistors to divide the signal after amplification:

| Characteristic | Detail |
|---------------|--------|
| **Signal path** | After the amplifier, before the drivers |
| **Components** | Inductors, capacitors, resistors |
| **Advantages** | Simple design, single amplifier needed, no power required for the crossover |
| **Disadvantages** | Power loss in components, limited slope options, component drift over time, less precise |
| **Common in** | Hi-fi speakers, guitar cabinets, budget monitors |

**Filter slopes in passive designs:**
- **6 dB/octave (1st order)** — Gentle slope, wide overlap between drivers, good phase coherence but poor driver isolation
- **12 dB/octave (2nd order)** — Most common passive slope, reasonable isolation
- **18 dB/octave (3rd order)** — Steeper, better isolation, more complex component network
- **24 dB/octave (4th order)** — Linkwitz-Riley alignment, excellent isolation, complex and expensive in passive form

### Active Crossovers
Active crossovers divide the signal before amplification, with each driver getting its own dedicated amplifier:

| Characteristic | Detail |
|---------------|--------|
| **Signal path** | Before the amplifiers, each driver has its own amp |
| **Implementation** | Analog op-amp filters or DSP (digital signal processing) |
| **Advantages** | Precise filter control, steeper slopes possible, no power loss, DSP correction, each amp optimized for its driver |
| **Disadvantages** | Multiple amplifiers needed, more complex design, higher cost |
| **Common in** | Professional studio monitors, PA systems |

### DSP Crossovers
Modern monitors increasingly use DSP-based crossovers, which offer:
- **FIR (Finite Impulse Response) filters** — Linear phase, no phase shift at crossover point, but add latency
- **IIR (Infinite Impulse Response) filters** — Minimal latency, but introduce phase shift (similar to analog filters)
- **Room correction** — Some monitors (Genelec SAM, KII Three) include onboard room correction DSP
- **Driver compensation** — DSP can correct for individual driver non-linearities

### Crossover Points and Why They Matter for Mixing
Common crossover frequencies in studio monitors:

| Configuration | Typical Crossover(s) | Notes |
|--------------|----------------------|-------|
| **2-way (tweeter + woofer)** | 1.5–3 kHz | Most nearfield monitors. Crossover region sits in the critical vocal/presence range |
| **3-way (tweeter + mid + woofer)** | ~300-500 Hz and ~2-4 kHz | Midfield/main monitors. Keeps crossover out of the most critical vocal range |
| **Coaxial** | Varies | Driver alignment eliminates time offset between drivers at the crossover point |

> [!note]
> The crossover region is where two drivers are both contributing to the sound. Phase alignment, driver positioning, and crossover slope all affect how smoothly this transition works. A poorly designed crossover creates a dip or bump in the frequency response at the crossover point — which can fool you into over- or under-emphasizing those frequencies in your mix.

## Driver Design

### Tweeters
Tweeters reproduce the high frequencies, typically above 1.5–4 kHz:

- **Soft dome** — Silk or fabric dome, smooth rolloff, slightly warmer top end. Common in Yamaha NS-10 (and similar), many European monitors
- **Metal dome** — Aluminum, titanium, or beryllium, extended high-frequency response, can have a "breakup" resonance peak at the top of its range
- **Ribbon** — Thin metal ribbon in a magnetic field, very fast transient response, wide horizontal dispersion but narrow vertical. Used in some high-end monitors (HEDD, Adam)
- **AMT (Air Motion Transformer)** — Folded ribbon design, used in Adam monitors. Very fast, detailed, distinctive sound

### Midrange Drivers
Found in 3-way monitors, handling the critical ~300 Hz–4 kHz range:
- Often cone-type drivers similar to small woofers
- Material choices (paper, kevlar, polypropylene) affect coloration
- This range covers the human voice's fundamental and harmonics — midrange quality is critical for vocal mixing

### Woofers
Woofers handle low frequencies, typically below 1.5–3 kHz in 2-way monitors or below ~500 Hz in 3-way designs:

- **Cone material** — Paper (warm, natural), polypropylene (clean, neutral), kevlar (stiff, controlled), aluminum (rigid, fast)
- **Driver size** — Larger drivers move more air but have slower transient response. Common sizes: 5" (nearfield), 6.5-8" (nearfield/midfield), 10-12" (midfield/main)
- **Excursion** — How far the cone can move. Long-excursion drivers produce more bass from smaller cabinets but may have more distortion at extremes

## Cabinet Design

### Sealed (Acoustic Suspension)
- **How it works:** Completely sealed enclosure, the trapped air acts as a spring on the driver cone
- **Bass response:** Gradual rolloff (12 dB/octave below resonance), extends lower than you might expect
- **Transient response:** Tight, controlled bass — the sealed air provides damping
- **Tradeoffs:** Less efficient (needs more amplifier power), less deep bass extension than ported designs of the same size
- **Used in:** Many studio monitors where bass accuracy is prioritized over bass extension (e.g., Amphion, some ATC models)

### Ported (Bass Reflex)
- **How it works:** A tuned port (tube) in the cabinet reinforces bass at the port's resonant frequency
- **Bass response:** Extended low end with a steep rolloff below the port tuning frequency (24 dB/octave)
- **Transient response:** Less tight than sealed — the port resonance "rings" slightly
- **Tradeoffs:** More efficient and deeper bass, but port turbulence can add noise, and the steep rolloff below tuning can cause problems with room modes
- **Used in:** Many studio monitors where bass extension is valued (e.g., Genelec, KRK, JBL)

> [!note]
> The "sealed vs ported" debate parallels the "tight bass vs deep bass" debate. Mastering engineers often prefer sealed designs for their controlled transient response. Mixing engineers may prefer ported designs for the extended low-frequency monitoring range. Neither is objectively better — it depends on your room, your work, and your preferences.

### Transmission Line
- Less common in studio monitors but found in some high-end designs (PMC)
- Uses a long, folded pathway behind the driver to absorb and reinforce low frequencies
- Combines some advantages of sealed (controlled transients) and ported (extended bass)
- Typically larger and more expensive

### Cabinet Construction
- **Material:** MDF (most common), plywood, aluminum, or composite
- **Bracing:** Internal bracing reduces cabinet resonance — you want the drivers making sound, not the cabinet
- **Rounded edges:** Reduce diffraction effects that cause frequency response irregularities
- **Isolation:** Decoupling pads (IsoAcoustics, Primacoustic Recoil Stabilizers) prevent the cabinet from coupling with the surface it sits on

## Why Speaker Design Matters for Mixing

### Knowing Your Monitors' Compromises
Every monitor has design compromises. Understanding them helps you compensate:

| Monitor Characteristic | Mixing Implication |
|-----------------------|-------------------|
| 2-way with 2.5 kHz crossover | Be careful with vocal presence decisions around 2-3 kHz |
| Ported design tuned to 45 Hz | Bass below 45 Hz rolls off very steeply — check on headphones or a sub |
| Small 5" woofer | Limited bass output — reference on larger speakers for low-end decisions |
| Ribbon/AMT tweeter | Very detailed top end — your mixes may sound slightly duller on other systems |
| Near-wall placement boosts bass | Not your monitors' fault — it is physics (see [[Acoustic Treatment Guide]]) |

### The Crossover Region and Mixing Decisions
The frequency range around your monitors' crossover point is where the speaker is least accurate. In a 2-way monitor with a 2 kHz crossover:
- Two drivers are contributing to the sound
- Phase alignment between drivers affects the response
- Your listening height relative to the tweeter/woofer axis matters most here

This is why ear-height alignment with the tweeter is standard practice — it puts you on-axis where the crossover behavior is most controlled.

## Subwoofers and Bass Management

### When to Add a Sub
- Your monitors roll off above 50-60 Hz and you need to monitor lower
- You work in genres with significant sub-bass content (hip-hop, EDM, film)
- Your room is large enough and treated enough to support accurate sub-bass monitoring

### Subwoofer Integration
- **Crossover point:** Typically 80 Hz, matching the main monitors' rolloff
- **Phase alignment:** The sub must be time-aligned with the mains — adjust delay/phase until the crossover region is smooth
- **Placement:** Corner placement maximizes output but excites every room mode. Front wall placement between mains is often the best compromise
- **Calibration:** Use measurement software (REW) to verify the sub integrates smoothly with the mains

## See Also
- [[Monitor Controllers Guide]] — The signal chain feeding your speakers
- [[Acoustic Treatment Guide]] — Room treatment affects what you hear from any speaker
- [[Impedance and Audio Electronics]] — Amplifier-speaker impedance interaction
- [[nerd-talk Channel Summary]] — Source channel for this topic

## Source Discussions
> [!quote] Discord Source
> Channel: #🧠nerd-talk
> Messages: ~145 (the single largest topic cluster in nerd-talk)
> Key contributors: Nomograph Mastering (34), David Fuller (20), Gerhard Westphalen (19), Bryan DiMaio, tim adamson 🇦🇺, spectrummasters
> Date range: January 2024 – February 2026
> Notable: Extensive discussion of crossover theory, driver materials, and cabinet design — the theoretical foundation for the gear-specific monitor pages in the vault

> [!quote] Rollmottle — Speaker burn-in philosophy (#monitoring-talk, March 2022, 14 reactions)
> "I feel like recommending a burn in at this point is a company's way of saying 'don't call us until you've gotten used to them...then you can you tell if something's actually wrong with them or you just weren't used to them yet.'"

> [!quote] David Fuller — PMC transmission line critique (#monitoring-talk, April 2021)
> "An acoustic transmission line like the ones that PMC uses really only work in big boxes — like no smaller than a floorstanding tower speaker. Trying to cram one in a standmount size box is going to, just by the way that these things work, have far too high of a tuning, often overlapping where the woofer itself peaks. You end up with a weirdly lumpy and uneven bass response. There is zero benefit of using a transmission line over a port in small boxes."

> [!quote] Discord Source
> Channel: #🔈monitoring-talk
> Messages: Extensive real-world crossover/driver discussion across PMC (transmission line), ATC (sealed), ported designs
> Date range: April 2021 – March 2022
> Key contributors: David Fuller, Rollmottle, sethearnest, cian riordan, peterlabberton
> Notable: Practical listening-based observations that complement nerd-talk's theoretical foundations
> See also: [[monitoring-talk Channel Summary]]
