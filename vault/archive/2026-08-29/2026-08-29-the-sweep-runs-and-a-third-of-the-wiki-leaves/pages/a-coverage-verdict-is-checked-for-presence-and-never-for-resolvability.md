---
title: "A coverage verdict is checked for presence and never for resolvability"
type: lesson
status: archived
authority: coverage-verdict-resolvability
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["scripts/vault-coverage.sh", "job_hunt_ai_vault/archive", "archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [vault, harness, testing]
---

# The finding

**`bash scripts/vault-coverage.sh` asks whether a unit has a verdict. It never asks whether the
verdict names anything.** A line reading `page:some-slug — plus a sentence explaining what went onto
it` counts exactly as a bare slug does, and resolves against the tree not at all.

**The librarian found 21 such verdicts in one sidecar during an ingest of 2026-08-26.** Measured
across every sidecar in this vault the same week: **802 of 2149 `page:` verdicts carry a space**,
which is to say they carry prose after the slug.

```
find . -name '*.coverage.tsv' -print0 | xargs -0 \
  awk -F'\t' '$2 ~ /^page:/ {tot++; if ($2 ~ / /) bad++} END {print bad, "of", tot}'
```

# Why it passed for two weeks

**The sidecar's two readers want different things and only one of them exists.** Coverage counts
verdicts, so it is satisfied. **The other reader — a human sampling for fidelity, or a script that
would resolve `page:` against the tree — is the one the prose was written for**, and it was written
helpfully: the trailing sentence says what landed on the page, which is genuinely useful to a person.

**So the defect is invisible in the direction that looks like care.** The verdicts with prose are the
ones somebody thought about.

# What follows

**The verdict is a bare slug, and several are comma-separated with nothing else.** Anything a reader
would want to say about the mapping belongs in `log.md`, where the ingest already writes its account.

**Nothing rewrites the sidecars already written.** `raw/` is immutable and the sidecars are keyed to
its lines; a sweep would be a second rewrite over an immutable record's index, and the population is
history rather than an obligation ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**The mechanical repair is a resolvability verdict inside `vault-coverage.sh`** — every `page:` slug
names a file under `wiki/` or `archive/` — and it is not designed here. It would have to start as an
advisory, because 802 lines would be red on the day it landed.
