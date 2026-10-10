---
type: decision
case: "126"
status: archived
update: ["[[rule-retro]]"]
supersedes: ["[[decision-case-118]]"]
origin: raw/2026-09-14/1029/ledger.md#case-126
sprint: migration
created: 2026-09-14
tags: [session, workflow, harness, render]
---

## Context

The Render of `rule-retro` (109.1) reads the ledgers of the day with `cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null`. On 2026-09-14 no date-level ledger exists — the first day with the session form of case 103 alone — so `cat` exits 1, the harness reports the substitution failed, and the skill text does not reach the agent; the `retro` event was still recorded. (Case 118 as it stands.)

## Problem

A substitution that names a file which the model of case 103 no longer guarantees fails on every session from now on. The fix is one `|| true` or a glob-only form; it is an `update` of `rule-retro`, which Retro cannot ratify. (Case 118 as it stands.)

## Given

`rule-retro` (`Leaf`, `draft`, `estimate-retro-loads` `failed` on 109.1, `deferred_by: [decision-case-118]`): line 40 of the Render is the substitution above; the text "the ledger lines of today grouped by Case".
**＋** `guppi tail` (`rule-ledger-tail`, `built`, `estimate-ledger-tail` `passed`): prints every record line under `vault/raw/` that no entry of a `materialize.yaml` covers, as `<date>/<HHMM> L<n>: <line>`; exit 0 always; a ledger that cannot be read is a line on stderr and the walk goes on. At Retro, before the librarian, the tail is this session's lines whole.
**＋** The glob form `cat vault/raw/$(date +%F)/*/ledger.md` loses a session across midnight and fails on a day without any ledger; `|| true` hides the failure and does not fix the date.
**－** `rule-ledger-tail` is not changed: the command and its contract stay, a second caller is added.
**－** The Frontier line F5 closes on this Case.

## Criterion

- [[estimate-retro-loads]] § case 126

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-126
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
