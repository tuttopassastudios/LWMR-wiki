---
type: gear
confidence: high
aliases:
  - AES/EBU
  - AES3
  - AES Digital
tags:
  - type/gear
  - gear/cables
manufacturer:
category: Cable/Connectivity
price_range: $10-$100 per cable
created: 2026-02-17
modified: 2026-02-17
---

# AES-EBU

## Summary

> [!abstract]
> AES/EBU (AES3) is a professional digital audio interconnect standard that carries two channels of digital audio over balanced XLR cables. It is the professional counterpart to consumer S/PDIF and is widely used in high-end studios, particularly for connecting converters to monitors with digital inputs (such as PMC speakers). The community discusses AES/EBU primarily in the context of digital monitor feeds, converter-to-speaker connections, and as part of larger digital routing systems. When feeding digital monitors via AES, the DAC in the interface becomes irrelevant since no DA conversion occurs until the signal reaches the speaker.

## Key Characteristics

- **Balanced digital audio over XLR** -- uses standard 110-ohm XLR cables; more robust than consumer S/PDIF
- **Two channels per connection** -- carries a stereo pair on a single cable
- **Professional standard** -- widely used in mastering studios and high-end facilities
- **Eliminates converter from monitoring chain** -- when feeding AES directly to digital speakers, the interface's DAC is bypassed entirely
- **Can be converted from TOSLINK/S/PDIF** -- format converters exist but add complexity; Hosa sells affordable options for two-channel formats
- **Preferred over TOSLINK for quality** -- generally considered more reliable than optical connections for clock-critical applications
- **Compatible with many high-end monitors** -- PMC, Genelec, and other brands offer AES digital inputs

## Use Cases

- **Digital monitor feed** -- connecting converter AES output directly to PMC or other digital-input speakers
- **Mastering chain connections** -- linking converters, processors, and monitoring in mastering suites
- **Long cable runs** -- balanced nature makes it more resistant to interference than S/PDIF coax over distance
- **Format conversion chains** -- converting between TOSLINK, S/PDIF, and AES as part of complex routing systems

## Settings & Sweet Spots

- When using AES for monitoring, the monitor controller must support digital volume control or you need an external solution
- For the Grace M905, configure the digital out to act as a "digital speaker output" in the menu to feed AES monitors
- Use proper 110-ohm AES/EBU cables rather than standard mic cables for best results, though standard XLR cables will often work for short runs

## Comparable Alternatives

| Connection | Notes |
|-----------|-------|
| [[S-PDIF]] (Coax) | Consumer equivalent; unbalanced; more susceptible to interference |
| [[S-PDIF]] (TOSLINK) | Optical; galvanic isolation but potentially more jitter |
| [[ADAT]] | 8 channels via optical; different use case (expansion, not monitoring) |
| [[Dante]] | Networked audio; higher channel counts but more complex |
| [[MADI]] | High channel count; 64 channels per connection |

## See Also

- [[S-PDIF]]
- [[ADAT]]
- [[Word Clock]]
- [[Lynx Aurora]]
- [[Prism Sound]]

## Source Discussions

> [!quote] Community Insights
> "If Josh ends up on PMCs or any speaker with a digital in going AES/SPDIF... the converter makes absolutely zero difference in that case right? For the audio going to speakers." -- masteredbyjack
>
> "You would need an individually addressable set of outputs so that you could control the level of your speakers. Since you need the ADAT I/O, don't think there's a way with your current setup without giving that up." -- Rollmottle (on the challenge of running both AES monitors and ADAT expansion)
>
> "You can do what you want to do... You have to configure the digital out on the Grace to act as a digital speaker output in the menu." -- Rollmottle (on feeding PMCs via AES through a Grace M905)
