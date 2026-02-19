---
type: glossary
confidence: medium
aliases:
  - Selection-Based Processing
  - SBP
tags:
  - type/glossary
  - daw/logic
created: 2026-02-18
modified: 2026-02-18
---

# Selection-Based Processing

## Definition

A [[Logic Pro]] feature that allows applying AudioUnit effects to a selected audio region destructively — similar to [[Pro Tools]]' AudioSuite. Select an audio region, choose an AU plugin, preview and apply. The processed audio replaces the original selection in the arrange window.

## Context

While Selection-Based Processing fills a gap in Logic's offline processing capabilities, the community reports significant reliability issues:
- **Audio dropouts** — unpredictable dropouts occurring after SBP use (spectrummasters, #logic-pro)
- **Destructive file corruption** — SBP can corrupt the underlying audio file in ways that are difficult to undo (itaylerner, #logic-pro)
- **Recommended workaround** — use Bounce in Place instead of SBP for more predictable results

> [!warning]
> Community consensus from #logic-pro is to avoid Selection-Based Processing for critical work. Bounce in Place is the safer alternative.

## Related Terms

- [[Logic Pro]]
- [[Offline Bounce]]

## See Also

- [[Logic Pro]] — parent DAW
- [[Troubleshooting DAW Issues]] — SBP-related issues documented
- [[Bounce and Export Workflows]] — Bounce in Place as alternative
