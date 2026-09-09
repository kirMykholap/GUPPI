---
title: "A status value is either an address or a stage, and the gate treats them oppositely"
type: concept
status: current
authority: status-value-gate-treatment
basis: code
sprint: S3
created: 2026-08-28
sources: ["archive/2026-08-28/the-sprint-list-stops-lying-and-archiving-gets-a-predicate/handoffs/2026-08-28-the-sprint-list-stops-lying-and-archiving-gets-a-predicate.md", "scripts/vault-check.sh", "job_hunt_ai_vault/wiki/decisions/_schema.yaml"]
tags: [vault, record-schema, harness]
---

# The distinction

**An address says where the page belongs.** `deprecated` and `archived` both mean the page is not in
`wiki/` any more, so finding one here is evidence of an unfinished move and the gate says so.

**A stage says how far along the page is.** `implemented` and `processed` mark a page that stays
here while something else is tested; the gate judges neither, because the mark is not a claim about
placement at all ([[processed-means-the-decisions-content-moved-on-and-the-mark-opens-a-state]],
[[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]]).

# Both marks were minted on 2026-08-28 and only one of them obliges a page to leave

**`archived` is written by the sweep as it moves a page**, so finding it under `wiki/` means the
move did not complete. The gate's `retired` verdict now fires on it as well as on `deprecated`, and
carries the value it found in its detail field, so one message names whichever mark it met and sends
the reader to the right repair.

**`processed` produces no verdict at all**, in `wiki/decisions/`, where alone it is legal.

# Why a gate that reddened every new value alike would have been wrong twice over

**It would have passed both red cases** — the two values are not the same kind of thing — **and it
would have locked the librarian out of the folder it is meant to drain.** A red gate is read by
`lock-the-librarian.ps1` as a refusal to dispatch, so the only writer allowed to clear it cannot run
([[the-librarian-lock-hook]], [[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**That is why the third selftest case asserts silence.** Proving that a verdict fires is half of it;
proving that the other value produces nothing is the half that keeps the corpus workable.

# How the pair was proved, 2026-08-28

**Three directions, against a sandbox copy of the live corpus under `VAULT=`**: `archived` in
`wiki/lessons/` is red with the unfinished-move message; `processed` in `wiki/entities/` is red
through the `badvalue` verdict; `processed` in `wiki/decisions/` gives no verdict.

**Neither narrowed suite run is a reading of the suite** — `--only processed` caught 3 and missed 0,
`--only archived` caught 4 and missed 0, and the whole suite was not run
([[a-narrow-suite-run-that-matches-no-case-still-prints-a-catch]]).
