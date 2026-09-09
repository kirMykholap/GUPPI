---
title: "The address bar is updated by an HX-Push-Url header, never by hx-push-url"
type: decision
status: current
authority: address-bar-updates
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [htmx, filters]
---

# The address bar is updated by a header, not by the attribute

## The defect

`hx-push-url="true"` puts the **actual request URL** into the address bar. After the first filter
change the address became `/vacancies/rows?…`, and reopening it returned a bare set of `<tr>` with
no page around it — a saved link did not open.

**This was a defect of the spec and the plan, not of the implementation.** Both prescribed the
attribute on a wrong reading of its semantics, and the implementation followed them correctly.

## What was decided

The fragment route sends a header instead, and **which header depends on whether the user
navigated**:

| Situation | Header | Why |
|---|---|---|
| the user changed a filter | `HX-Push-Url` | they navigated; a history entry is correct |
| the refresh at the end of a collection (`after_collection=true`) | `HX-Replace-Url` | **nobody navigated** |

The second row closes a defect measured live during slice 3: the end of a collection wrote a
browser-history entry with no user action, `history.length` 44 → 45. The fix is not a tighter
string comparison. **The address still has to follow the screen** — the chips have just been reset
([[table-refreshes-itself]]), so leaving the old address means the next reload restores the stale
set, which is the same defect from the other side — but nobody navigated, and `replaceState` is
exactly that pair. Measured after the fix, in Edge against the production database on 2026-08-06:
`history.length` **50 → 50**, with the address rewritten to the reset chip set.

The two headers are mutually exclusive in htmx — `HX-Push-Url` is read first and short-circuits — so
this is a branch rather than a combination.

**The header is sent only at `offset=0`.** A «показать ещё» request (`offset>0`) carries none, which
is why paging further into a list does not rewrite the address and a saved link never contains an
`offset`. Verified both ways after the final review's fixes.

**The defect it closed was self-limiting, which is why it read as Minor before it was fixed.** Slice
2b's guard skips the push when the pushed address already equals the current one; slice 3 changed
what the default address *is* — the chips are now checked by default and the `tags_set` marker rides
with them, so an untouched page serialises to `?tags_set=true&tag=…&tag=…`, which on a freshly opened
bare `/vacancies` is not the current address. So the first collection to end on a fresh page cost one
history entry and every later one was silent. The visible consequence was the one
`_current_page_url`'s docstring names: one press of «назад» went to bare `/vacancies`, restored from
the back-forward cache, **showing the table as it was before the collection**.

The now-dead `hx-push-url` attributes were **removed rather than left in place**, because a future
branch returning 200 without a header would have resurrected the original defect silently.

A later guard redirects a fragment URL opened as a page, because the header cannot undo addresses
already sitting in bookmarks and restored tabs.

## What it obliges

Section 7 of the 2a design was reconciled with the code, including this prescription, **so that a
later reading of the design cannot re-prescribe it**. That reconciliation is the durable half of
the fix: the code was fixed in an afternoon, the document that caused it would have kept causing it.

See [[profile-resolution]] for what `_page_url` does and does not put in the address.
