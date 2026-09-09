---
title: "DIVERGENCE: an implemented proposal stays in `wiki/proposals/` because nothing exists to move it"
type: decision
status: archived
authority: implemented-placement-divergence
binding: divergence
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/pages/a-style-rule-for-the-prose-a-session-writes.md"]
tags: [record-schema, vault, process]
---

# What was broken

**`wiki/proposals/a-style-rule-for-the-prose-a-session-writes.md` carries `status: implemented` and
sits in `wiki/proposals/`.** Both
[[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]] and
`wiki/proposals/_schema.yaml` say such a page moves to `archive/`.

# The ruling, 2026-08-24

> **owner:** «поле пишем, размещение не трогаем, расхождение записываем отдельно.»

**The `decided_by:` field was written and the placement was not touched.**

**Rejected: moving the page during the back-fill.** A move rewrites citations and is a second change
riding on a job that was about one field; and the party that should do it is a script rather than a
hand ([[the-archive-mover-is-a-sweep-inside-the-archive-script-at-the-lint-stage]]).

# Why it is recorded as a divergence rather than as a pending task

**The rule is unconditional and the page is in breach of it today.** Naming it a task would say the
store is consistent and the work is queued; it is not consistent, and a reader who trusts the rule
will be wrong about this page.

**And the gate judges `implemented` not at all**, deliberately — the mark opens a state rather than
naming a place ([[a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place]]). So nothing
mechanical will ever report this, which is the reason it needed a page.

# Corrected 2026-08-25 — the breach is on two pages, not one

**Read off the `status:` lines in `wiki/`**: two pages carry `status: implemented` and both sit in
`wiki/proposals/` — `a-style-rule-for-the-prose-a-session-writes`, which this page names, and
`a-verdict-pairing-the-idea-status-with-a-named-decision`, whose breach was recorded nowhere. It took
the mark in the same session.

**A hand-written divergence records what somebody noticed**, which is the argument for the sweep rather
than a fault of this page ([[the-archive-sweep-reports-a-refusal-and-the-gate-stays-silent-about-placement]]).

**Both pass the archive precondition** — cited by six and four live pages — so the sweep's first run
would move both and refuse nothing.
