---
title: "The collection frame is checked against every city in the raw string, not just the first"
type: concept
status: current
authority: city-frame-matching
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [data, collection]
---

# The frame is checked against all the cities, the column shows one

dou.ua lists cities separated by commas — «Київ, Варшава (Польща)» — and the source never says
which one is primary.

- **`dto.city` is the first part.** It is a field for display, because the column is one column.
- **`_violates_city` looks at every part**, through `normalize.location.city_candidates`.

Otherwise a profile framed on «Варшава» would silently lose a vacancy that does not contradict the
frame but confirms it in a non-first part.

**The string-splitting rule lives in exactly one place, the normalisation layer.** A copy in
`ingest` would drift from it silently.

Two accepted cosmetic consequences: a multi-part location is displayed by its first city, and
`parse_location("за кордоном")` with no remote marker yields `city="за кордоном"` — which is
accidentally right for the frame, since it matches no city in the reference list, and shows up in
the table as if it were a city name.

The cost of getting this wrong was measured once: see
[[a-deferred-check-must-be-run-when-its-condition-arrives]].
