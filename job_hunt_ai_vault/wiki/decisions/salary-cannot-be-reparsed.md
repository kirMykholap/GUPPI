---
title: "Salary cannot be re-parsed, because no raw salary string is stored"
type: decision
status: current
authority: salary-reparse
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [data, collection, db-schema]
---

# Salary cannot be re-parsed

`renormalize` repairs only `city`, `city_any` and `work_format`, from `location_raw`. **There is no
raw salary string in the schema** — `salary_raw` is not stored, unlike `location_raw`.

Consequences:

- a row parsed by an old rule is corrected **only** when the vacancy is met again in a listing;
- a vacancy that has left the site keeps its old parse for ever.

## What this obliged once

After the «currency before the number» fix — dou.ua writes `від $1600`, and the symbol before the
digits broke the word-boundary search, yielding `(1600, 1600)` instead of `(1600, None)` — one
`parse --mode full` was required to replay the amounts. **It was done on 2026-08-05: four
source+tag pairs, 103 cards, 0 new, 103 updated. Do not repeat it.**

No salary actually changed in that run: upsert overwrites `salary_min/max/currency` on every
encounter, so the parse really was replayed by the new code, and the "currency before the number"
pattern simply does not occur in the current live cards.

**A symmetric `salary_raw` is a candidate for plan B.** Until then, any change to salary parsing
carries the same obligation: a full re-parse, and only for what is still listed.

See [[absent-values-never-overwrite]] for the field rule this asymmetry sits beside.
