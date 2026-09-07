---
title: "Parsers yield raw strings, normalisation yields canonical values, and the boundary is held by an AST test"
type: concept
status: current
authority: normalisation-boundary
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [data, architecture]
---

# The normalisation layer

Three stages, and each may only do its own job:

```
parser  →  RawVacancy      the source's strings, extracted and nothing more
normalize →  VacancyDTO     canonical values
ingest    →  the database
```

**The dictionary of values is now one for all sources, and it cannot drift**, because the boundary
is held by an AST test: `parsers/` and `normalize/` do not import `jobhunt.db`, `jobhunt.ingest`,
`jobhunt.web` or `sqlalchemy`. See [[architectural-boundaries]].

That single dictionary is why the city-splitting rule exists in exactly one place — a copy in
`ingest` would drift silently. See [[collection-frame-city-check]].

The layering is also what makes some fixes impossible without widening a contract: a per-request
progress heartbeat needs a signal in `BaseParser`, because parsers may not know about the database
and `touch()` does not commit. That is why [[stale-after-thirty-minutes]] is a window rather than
a heartbeat.

The column that will one day need this layer's output as a vector is not yet possible — [[pgvector-extension-not-enabled]].
