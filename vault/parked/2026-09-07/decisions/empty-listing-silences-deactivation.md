---
title: "An empty work.ua listing silences deactivation for the whole source, and the fix is a fixture"
type: decision
status: current
authority: empty-listing-handling
binding: deferral
basis: external
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [deactivation, data]
---

# An empty work.ua listing silences deactivation for the whole source

**work.ua does not render the `#pjax-jobs-list` container at all when a query finds nothing.**
Checked live during a re-review: `/jobs-zqxwcvbnmlkjhgfd/` returns HTTP 200, 140 KB, and no
container.

So a legitimately empty result does not reach the guard "the counter promises N, there are 0 cards".
It goes to `ParserStructureError` → `run.status="failed"` → and `mark_missing` together with
`rebuild_tag_links` is skipped **for the entire source, for every tag at once**.

**One narrow tag that currently finds nothing halts work.ua deactivation on every pass.**

## The fix, and why it is deferred

A fixture of the «нічого не знайдено» page and explicit recognition of it. That is separate work,
not a line change, which is why it is recorded rather than done.

See [[deactivation-cycle]] — specifically the rule that a failure of any query cancels the marking
for the whole source, which is correct in general and is what bites here.

The source's other quirks are on its page: [[work-ua]].
