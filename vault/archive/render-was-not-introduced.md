---
title: "`render:` was not introduced, because only the region mode has a writer"
type: decision
status: deprecated
authority: delivery-mode-field
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-inject.sh", "job_hunt_ai_vault/CLAUDE.md"]
tags: [harness, vault]
superseded_by: [[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]
---

# Decided 2026-08-17: no `render:` field on a rule page

The design named **four delivery modes** — `region`, `whole`, `zone`, `none` — and proposed a
`render:` field to select between them
([[the-harness-is-built-by-a-script-and-guarded-by-a-gate]]). **Only `region` is built**, so the
field would have exactly one legal value, no writer, and no reader that could ever branch on it.

**Rejected: adding the field now, against the modes that are coming.** A field nothing writes and
nothing reads is a per-page invention: every author guesses at its values, and the guesses become
the schema ([[a-field-with-no-register-produces-unique-values-by-default]],
[[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]]).

## The consequence, and it is a live defect

**[[marked-regions-and-the-prose-outside-them]] states two of its four verdicts through a field
that does not exist.** Two of those verdicts read *"a `render: region` rule with…"*. Anyone reading
that proposal as a specification builds something uncheckable — the predicate it names cannot be
evaluated against any page in this store.

**The page needs rewriting**, and it carries a correction section as of 2026-08-17 rather than a
deletion. This is the second time a design has been found asserting a field it invented in prose;
the first was found by a `/pre-task` on the same day
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

## When it comes back

The day a second delivery mode is built. At that point the field has a writer, a reader and at
least two values, which is the admission test this store already uses for a field
([[the-frontmatter-core-is-fixed-and-updated-joins-it]]).

# Retired 2026-08-20: the re-entry condition on this page was met

**This page named its own condition** — *"the day a second delivery mode is built"* — and the `whole`
mode is that day ([[the-whole-mode-owns-a-file-end-to-end]]). `render:` is reinstated and required
in `wiki/rules/_schema.yaml` on the owner's ruling of 2026-08-19
([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]).

**Read this page for why a field with one legal value was refused**, which is unchanged as an
argument and is the reason the successor could state an admission test rather than argue one. **The
consequence section is spent**: [[marked-regions-and-the-prose-outside-them]] stated verdicts through
a field that did not exist, and the field exists now.
