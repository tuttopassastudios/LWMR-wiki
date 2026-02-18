---
type: gear
confidence: high
aliases:
  - SPDIF
  - S/PDIF
  - Sony/Philips Digital Interface
  - Coax Digital
  - Optical Digital
tags:
  - type/gear
  - gear/cables
manufacturer:
category: Cable/Connectivity
price_range: $5-$50 per cable
created: 2026-02-17
modified: 2026-02-17
---

# S-PDIF

## Summary

> [!abstract]
> S/PDIF (Sony/Philips Digital Interface Format) is a consumer-grade digital audio interconnect that carries two channels of audio over either coaxial (RCA) or optical (TOSLINK) cables. It is widely used in studio setups for connecting DACs, feeding digital monitors, and linking interfaces to external converters. The community frequently discusses S/PDIF in the context of digital monitoring chains, format conversion between devices, and the trade-offs between coaxial and optical variants. Coax S/PDIF is generally preferred for sound quality, while optical provides galvanic isolation. S/PDIF shares TOSLINK ports with ADAT on many interfaces, creating routing conflicts.

## Key Characteristics

- **Two channels of digital audio** -- stereo only, unlike ADAT's 8 channels
- **Two physical formats** -- coaxial (75-ohm RCA) and optical (TOSLINK)
- **Coax generally preferred** -- better clock integrity than optical; use short, quality 75-ohm cables
- **TOSLINK provides galvanic isolation** -- eliminates potential ground loop issues between devices
- **Shares TOSLINK ports with ADAT** -- most interfaces force a choice between ADAT mode and S/PDIF mode on optical ports
- **Can carry clock signal** -- the receiving device can extract clock from the S/PDIF stream; no separate word clock needed for two-device setups
- **Format converters available** -- Hosa and others make affordable TOSLINK-to-coax and S/PDIF-to-AES converters
- **Apollo can mirror main outs to S/PDIF** -- useful for feeding digital monitors while retaining ADAT for other purposes

## Use Cases

- **Feeding external DACs** -- connecting an interface to a dedicated DAC for monitoring
- **Digital monitor feed** -- sending stereo digital audio to powered monitors with digital inputs
- **Clocking from S/PDIF** -- using the embedded clock from a high-quality converter to slave other devices; "clocking from SPDIF is just fine"
- **Format conversion** -- converting between optical and coax, or between S/PDIF and AES/EBU
- **Reference playback** -- Topping and similar USB DACs connected via S/PDIF for Spotify referencing

## Settings & Sweet Spots

- For S/PDIF clocking, use a short, quality cable specifically rated for S/PDIF (75-ohm)
- Coax S/PDIF is preferred over TOSLINK for clock-critical connections
- On Apollo interfaces, S/PDIF can be set to mirror the main outputs, allowing digital monitor feed while ADAT handles other I/O

## Comparable Alternatives

| Connection | Notes |
|-----------|-------|
| [[AES-EBU]] | Professional balanced equivalent; XLR; more robust for long runs |
| [[ADAT]] | 8 channels but shares TOSLINK port |
| USB Audio | Direct computer-to-DAC; can introduce noise from computer |
| [[Dante]] | Networked alternative for larger systems |

## Common Mistakes

- **Using a standard RCA cable instead of 75-ohm coax** -- regular audio RCA cables may cause reflections and clock errors; use proper digital coax
- **Assuming TOSLINK and coax sound identical** -- coax generally provides better clock performance
- **Not checking ADAT/S/PDIF port conflicts** -- verify your interface can run S/PDIF and ADAT simultaneously before planning your routing
- **Long TOSLINK runs** -- optical cables degrade over longer distances; keep runs short

## See Also

- [[AES-EBU]]
- [[ADAT]]
- [[Word Clock]]
- [[Lavry]]
- [[Focusrite Clarett]]

## Source Discussions

> [!quote] Community Insights
> "Clocking from SPDIF is just fine, use a short good quality cable made for SPDIF." -- Nomograph Mastering
>
> "AFAIK it's limited to the main outs and SPDIF can be set to mirror that. But not ADAT." -- Gerhard Westphalen (on Apollo S/PDIF mirroring)
>
> "AES and coax SPDIF can cause problems from the electrical connection between gear so that's also something to keep in mind... for gear that's only doing data transfer and no conversion I'd opt for one of the optical connections." -- Gerhard Westphalen
>
> "Hosa sells any format converter you need for the 2 channel formats but if you need to split out ADAT or convert to SPDIF it's going to cost you a lot more." -- Gerhard Westphalen
