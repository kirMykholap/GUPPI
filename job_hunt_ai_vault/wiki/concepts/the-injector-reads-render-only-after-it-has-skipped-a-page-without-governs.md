---
title: "The injector reads `render:` only after it has skipped every page carrying no `governs:`"
type: concept
status: current
authority: injector-render-blindspot
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "scripts/vault-inject.sh", "job_hunt_ai_vault/wiki/concepts/_schema.yaml"]
tags: [harness, record-schema, vault]
---

# The order of the injector's own passes

**`scripts/vault-inject.sh` skips every page carrying no `governs:` before it ever looks at
`render:`.** The field is read inside the branch that has already decided the page renders
somewhere.

**So a nonsense `render:` on a page with neither `governs:` nor a region is seen by nothing.** The
injector never reaches it, and the gate only reaches it if the folder's schema names the field's
legal values.

# What that forced

**The `values:` list had to be copied into `wiki/concepts/_schema.yaml` rather than left to the
injector's own guard.** Without the copy, `render: banana` passes rule 2 on a `concepts/` page while
failing on a `rules/` one — the same value, two verdicts, decided by which folder the page happens
to sit in ([[a-fields-legal-values-live-beside-its-legal-keys]],
[[a-value-outside-the-schemas-list-is-red]]).

**And nothing obliged the copy.** [[the-legal-value-list-lives-in-each-folders-schema]] obliges the
reverse direction only — a change to an existing set is made in every folder's file — and says
nothing about a field newly **admitted** to a second folder. The copy is recorded as an inference
with the ruling that needed it ([[an-absent-render-is-red-on-a-page-that-renders]]).

# The general shape

**A guard that runs after a filter cannot see what the filter dropped.** The injector's filter is
*does this page render at all*, which is exactly the population whose `render:` value is
uninteresting — until somebody writes a page that will render later and stamps it early. **The
verdict that catches that case belongs to the schema, which has no filter.**
