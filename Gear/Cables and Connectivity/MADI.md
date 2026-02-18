---
type: gear
confidence: medium
aliases:
  - MADI Protocol
  - Multichannel Audio Digital Interface
  - AES10
tags:
  - type/gear
  - gear/cables
manufacturer:
category: Cable/Connectivity
price_range: $100-$500 per interface card
created: 2026-02-17
modified: 2026-02-17
---

# MADI

## Summary

> [!abstract]
> MADI (Multichannel Audio Digital Interface, also AES10) is a professional digital audio protocol that carries up to 64 channels of audio over a single cable -- either coaxial (BNC) or optical fiber. MADI is increasingly discussed in the community as a preferred alternative to Dante for high-channel-count applications, particularly in live recording and broadcast environments where reliability is paramount. After experiencing Dante's reliability issues, multiple professionals are migrating to MADI for backup recording and multi-channel routing. MADI is also used to connect older Antelope Orion converters to modern computers via PCIe cards or RME MADIface.

## Key Characteristics

- **64 channels per single cable** -- massive channel density over coaxial (BNC) or optical fiber
- **Highly reliable** -- point-to-point connection without the networking complexity of Dante
- **No network configuration required** -- simpler than Dante; does not require IT administration skills
- **RME MADIface** -- popular computer interface for MADI connectivity
- **Preferred for live recording** -- reliability makes it suitable for concerts and broadcast where downtime is unacceptable
- **Used with Antelope Orion converters** -- MADI output from older Antelope units can connect to modern computers via MADIface or PCIe chassis
- **Optical MADI for galvanic isolation** -- optical fiber version eliminates electrical connection between gear, avoiding potential noise issues
- **USB can degrade MADI performance** -- USB connections tend to be worse than optical for data transfer; many DACs perform objectively worse when fed from USB

## Use Cases

- **Backup recording for live events** -- replacing Dante for reliable multi-channel capture
- **High channel count studio routing** -- connecting 64 channels between rooms or between converters and computers
- **Legacy converter connectivity** -- keeping older Antelope or other MADI-equipped converters connected to modern systems
- **Broadcast environments** -- where reliability and channel count matter more than flexibility

## Comparable Alternatives

| Protocol | Channels | Notes |
|----------|----------|-------|
| [[Dante]] | Variable | More flexible routing but reliability issues; requires network expertise |
| [[ADAT]] | 8 (per cable) | Lower channel count; simpler; widely supported |
| [[AES-EBU]] | 2 | Professional standard; only two channels |
| AVB (MOTU) | Variable | Ethernet-based; MOTU-centric ecosystem |
| Thunderbolt | Variable | Direct computer connection; interface-dependent |

## Common Mistakes

- **Assuming MADI is obsolete** -- it remains actively used in professional environments and is gaining adoption as Dante refugees seek alternatives
- **Not considering PCIe chassis for MADI cards** -- modern Macs can use external PCIe chassis to add MADI card connectivity
- **Choosing Dante over MADI for live work** -- MADI's simplicity and reliability make it the better choice for time-critical environments

## See Also

- [[Dante]]
- [[AES-EBU]]
- [[ADAT]]
- [[RME]]
- [[Antelope Audio]]

## Source Discussions

> [!quote] Community Insights
> "I'm going to move over to a different format like MADI for backups. I think a pure MADI format might be a better direction." -- SoundsLikeJoe (after moving away from Dante)
>
> "For gear that's only doing data transfer and no conversion I'd opt for one of the optical connections (SPDIF, ADAT, MADI). So that my computer and all of its potential noise over USB is completely separate from my audio gear." -- Gerhard Westphalen
>
> "USB tends to be the worse of all digital connections. Many DACs perform objectively worse when fed from USB." -- Gerhard Westphalen
>
> "I think if you want to use that device with a new computer the best bet might be to configure the MADI routing on the current rig and get a MADIface." -- Bryan DiMaio
