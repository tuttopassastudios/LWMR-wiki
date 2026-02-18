---
type: dashboard
tags:
  - type/dashboard
created: 2026-02-17
modified: 2026-02-17
---

# Audio Production Wiki

> [!tip] Dashboard
> Central hub for navigating the vault. Built from Discord community discussions.

---

## Maps of Content

| Domain | Link |
|--------|------|
| Mixing | [[Mixing]] |
| Mastering | [[Mastering]] |
| Recording | [[Recording]] |
| Acoustics | [[Acoustics]] |
| Signal Flow | [[Signal Flow]] |
| DAWs & Software | [[DAWs and Software]] |
| Plugins | [[Plugins]] |
| Hardware | [[Hardware]] |
| Workflow | [[Workflow]] |

---

## Quick Access

- [[Processing Log]] — Track import progress
- [[Contributors]] — Community contributor rankings
- [[Glossary/]] — Term definitions
- [[daw-talk Channel Summary]] — #daw-talk source data
- [[gear-talk Channel Summary]] — #gear-talk source data

---

## Recently Modified Pages

```dataview
TABLE file.mtime AS "Modified", type, confidence
FROM -"_Meta"
SORT file.mtime DESC
LIMIT 15
```

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
