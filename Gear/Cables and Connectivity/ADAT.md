---
type: gear
confidence: high
aliases:
  - ADAT Lightpipe
  - ADAT Optical
  - Toslink ADAT
tags:
  - type/gear
  - gear/cables
manufacturer:
category: Cable/Connectivity
price_range: $5-$30 per cable
created: 2026-02-17
modified: 2026-02-17
---

# ADAT

## Summary

> [!abstract]
> ADAT (Alesis Digital Audio Tape) Lightpipe is an optical digital audio protocol that carries 8 channels of audio at 44.1/48 kHz over a single TOSLINK fiber optic cable. It is the most common method for expanding the channel count of audio interfaces, connecting external preamps, and linking converters in studio systems. The community frequently discusses ADAT in the context of expanding I/O on Apollo, RME, Focusrite, and other interfaces. A key limitation is that many interfaces force a choice between ADAT and S/PDIF on shared optical ports, and channel count halves at higher sample rates (4 channels at 88.2/96 kHz via S/MUX).

## Key Characteristics

- **8 channels at 44.1/48 kHz per TOSLINK cable** -- the standard for multi-channel optical digital audio
- **4 channels at 88.2/96 kHz (S/MUX)** -- channel count halves at double sample rates
- **Shared optical ports with S/PDIF** -- many interfaces cannot run ADAT and optical S/PDIF simultaneously; you must choose one or the other
- **Standard TOSLINK connectors** -- uses the same physical connector as optical S/PDIF
- **Primary method for I/O expansion** -- connecting external preamps (Audient ASP880, PreSonus Digimax, etc.) to interfaces
- **Galvanic isolation** -- optical connection eliminates ground loops between connected devices
- **Clocking considerations** -- slave devices must sync to the master clock via the ADAT stream or word clock

## Use Cases

- **Expanding interface channel count** -- adding 8 preamp channels via external units like the Audient ASP880 or PreSonus Digimax
- **Connecting hardware inserts** -- using ADAT to route through external converters for outboard gear integration (e.g., RME Fireface for hardware inserts)
- **Format conversion** -- RME and MOTU LP32 can split ADAT into optical S/PDIF outputs or perform other format conversions
- **Multi-room routing** -- using ADAT between rooms or between separate converter units

## Settings & Sweet Spots

- When using ADAT for hardware inserts, you lose the ability to use the same optical port for S/PDIF monitoring output -- plan your routing accordingly
- If your interface has two TOSLINK ports, check whether both can run ADAT simultaneously or if one must be dedicated to S/PDIF
- For data transfer between devices where conversion does not occur, optical connections (ADAT) provide galvanic isolation and are preferred by some engineers

## Comparable Alternatives

| Connection | Channels | Notes |
|-----------|----------|-------|
| [[AES-EBU]] | 2 | Professional two-channel digital; balanced XLR |
| [[S-PDIF]] | 2 | Consumer two-channel; coax or optical |
| [[MADI]] | 64 | High channel count for large installations |
| [[Dante]] | Variable | Networked audio over ethernet |
| DB25 Analog | 8 | Analog equivalent channel count per cable |

## Common Mistakes

- **Assuming ADAT and S/PDIF can run simultaneously on shared optical ports** -- most interfaces with TOSLINK share the port between ADAT and S/PDIF modes
- **Forgetting channel count halves at higher sample rates** -- at 88.2/96 kHz you get 4 channels per ADAT connection, not 8
- **Not setting the correct clock source** -- ADAT expansion devices must be slaved to the master interface's clock to avoid sync issues
- **Using ADAT for monitoring when you need the port for expansion** -- plan which function gets priority on shared optical I/O

## See Also

- [[AES-EBU]]
- [[S-PDIF]]
- [[Word Clock]]
- [[Audient]]
- [[RME]]

## Source Discussions

> [!quote] Community Insights
> "I currently use the Toslink for 8 I/O on an RME Fireface via ADAT. This is where my HW inserts live and I don't want to lose them." -- Ross Fortune
>
> "As far as I understand, I have to choose ADAT or SPDIF on the 8p -- it can't run both simultaneously (which is a god damn shame as it has 2x Toslink In and 2x Toslink Out ports)." -- Ross Fortune
>
> "Hosa sells any format converter you need for the 2 channel formats but if you need to split out ADAT or convert to S/PDIF it's going to cost you a lot more." -- Gerhard Westphalen
>
> "AFAIK it's limited to the main outs and S/PDIF can be set to mirror that. But not ADAT." -- Gerhard Westphalen (on Apollo ADAT volume control limitations)
