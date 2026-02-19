---
type: dashboard
tags:
  - type/dashboard
created: 2026-02-18
modified: 2026-02-18
---

# Editorial Dashboard

> [!tip] Internal Dashboard
> Editorial metrics and review tools. This page is excluded from the published site.

---

## Low-Confidence Pages (Needs Review)

```dataview
TABLE type, tags
FROM -"_Meta"
WHERE confidence = "low"
SORT file.name ASC
```

## Medium-Confidence Pages

```dataview
TABLE type, tags
FROM -"_Meta"
WHERE confidence = "medium"
SORT file.name ASC
```

## Orphan Pages (No Backlinks)

```dataview
LIST
FROM -"_Meta" AND -"MOC"
WHERE length(file.inlinks) = 0
SORT file.name ASC
```

## Processing Summary

```dataview
TABLE WITHOUT ID
  file.link AS "Log Entry",
  length(file.lists) AS "Items Logged"
FROM "_Meta"
WHERE file.name = "Processing Log"
```

---

## Vault Stats

```dataview
TABLE WITHOUT ID
  length(filter(file.lists, (x) => true)) AS "Total Entries"
FROM ""
WHERE false
```

**Total pages by type:**

```dataview
TABLE WITHOUT ID
  type AS "Type",
  length(rows) AS "Count"
FROM -"_Meta/Templates"
WHERE type
GROUP BY type
SORT type ASC
```

---

## Quick Editorial Links

- [[Processing Log]] — Track import progress
- [[Contributors]] — Community contributor rankings
- [[daw-talk Channel Summary]] — #daw-talk source data
- [[gear-talk Channel Summary]] — #gear-talk source data
- [[nerd-talk Channel Summary]] — #nerd-talk source data
- [[recording-talk Channel Summary]] — #recording-talk source data
- [[ableton-live Channel Summary]] — #ableton-live source data
- [[cubase Channel Summary]] — #cubase source data
- [[logic-pro Channel Summary]] — #logic-pro source data
- [[monitoring-talk Channel Summary]] — #monitoring-talk source data
- [[pro-tools Channel Summary]] — #pro-tools source data
