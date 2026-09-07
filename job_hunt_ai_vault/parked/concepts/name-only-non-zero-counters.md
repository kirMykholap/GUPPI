---
title: "A summary names only non-zero counters, because a clause that always says the same thing stops being read"
type: concept
status: current
authority: summary-line-content
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [collection, web]
---

# Name only the non-zero counters

`has_problems` is true when any of four counters is non-zero, and the summary line used to name
two of them unconditionally.

**Every quick run marks its id set incomplete** — that is what "does not touch the disappeared"
means ([[collection-modes-and-why-source-filters-do-not-decide]]) — so «Проверить новое» *always* ended with
«с ошибкой 0, усечено 0». Two zeros and no reason, on every single run.

**That is exactly the drift `ingest/summary.py` was extracted to prevent, reintroduced one layer up
in the template.** Extracting a component does not stop a duplicate growing above it.

Now only non-zero counters are named.

The general form of this rule already exists in the project's logging convention: the normal
outcome is `logger.info` with numbers, and `warning` is for what should not have happened — in
particular when a condition filtered out the **whole** set it was applied to. A warning that fires
always stops being read, and so does a clause.
