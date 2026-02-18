---
type: gear
confidence: low
aliases:
  - Word Clock
  - Master Clock
  - WC
  - BNC Clock
tags:
  - type/gear
  - gear/cables
manufacturer:
category: Cable/Connectivity
price_range: $50-$3,000+ (dedicated clock units)
created: 2026-02-17
modified: 2026-02-17
---

# Word Clock

## Summary

> [!abstract]
> Word clock is a synchronization signal used to keep multiple digital audio devices running at the same sample rate and phase. It is transmitted via BNC cables and is essential when connecting multiple converters, interfaces, or digital processors in a studio. The community has a nuanced view: while proper clocking is important for multi-device systems, the prevailing advice is that internal clocks are almost always better than external master clocks, external clock purchases are rarely justified, and the money is better spent on a better converter. The quality of a device's PLL (Phase-Locked Loop) circuit -- which receives external clock signals -- matters as much as the clock source itself.

## Key Characteristics

- **BNC connector standard** -- word clock uses 75-ohm BNC cables
- **Internal clock is almost always better** -- community consensus strongly favors using a converter's internal clock rather than an external master clock
- **PLL quality matters enormously** -- even a high-quality external clock signal is only useful if the receiving device's PLL circuit is good enough to use it properly
- **Clock at the most important AD** -- in multi-device setups, the primary AD converter should typically be the clock master
- **External clocks rarely improve sound** -- Dan Lavry (Lavry Engineering) was notably anti-external clocking; the community agrees
- **Clocking is "really really complex"** -- there is no simple TLDR; testing is essential
- **Sample drift can occur** -- when using ADAT-connected expansion units, slight sample offset can vary between power cycles

## Use Cases

- **Synchronizing multiple converters** -- essential when using separate AD and DA converters or expansion units
- **Pro Tools HD systems** -- HD rigs with multiple Digilink devices need proper clock distribution
- **ADAT expansion** -- expansion preamps connected via ADAT must slave to the master interface's clock
- **S/PDIF digital connections** -- the receiving device can extract clock from the S/PDIF stream as an alternative to dedicated word clock

## Settings & Sweet Spots

- Default to using the internal clock of your best/most important converter
- Only use external word clock when you must synchronize multiple devices and cannot use embedded clock (via AES, S/PDIF, or ADAT)
- When sending word clock, use the output of the device that is locked to its input signal
- Keep BNC cables short and use proper 75-ohm termination

## Common Mistakes

- **Buying an external master clock expecting better sound** -- this is almost never the right investment; a better converter will yield more improvement
- **Clocking from a worse device** -- always clock from your best converter, not from a cheaper unit
- **Not testing and measuring** -- clocking behavior varies by device; do your own tests and report back
- **Assuming the "consensus" is correct** -- the community urges independent testing over accepting received wisdom about clocking

## See Also

- [[AES-EBU]]
- [[S-PDIF]]
- [[ADAT]]
- [[Lavry]]
- [[Lynx Aurora]]
- [[Crane Song]]

## Source Discussions

> [!quote] Community Insights
> "Unless you have to it's pretty much always better to run on the internal clock." -- David Fuller
>
> "Clocking is really really complex, and there is no TLDR here. Whether or not it's worse (it will never be better) depends on the PLL circuit." -- Nomograph Mastering
>
> "Generally you want to clock at the most important AD. But ask yourself why you think it's the most important." -- Nomograph Mastering
>
> "A high integrity clock signal is only useful if it's received properly." -- Nomograph Mastering
>
> "What are you trying to achieve by clocking the Lavry? If 'better' is the answer... would be more worthy investment to buy a new converter design vs a clock to improve the DA10." -- SoundsLikeJoe
>
> "I assume I will need a word clock cable as well to keep things in sync?" -- joshbonanno (common question about Grace M905 to PMC digital monitor setup)
