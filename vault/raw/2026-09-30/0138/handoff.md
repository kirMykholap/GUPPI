# Handoff — 2026-09-30, the conserved Spec of session 2024 built

## Notes from memory

- The person found at `/hi` that the `/carry` of session 2024 had dropped the whole Work list. The open W lines were restored by hand into the Frontier of this session from the Frontier of 2024 and the brief of 1c196e8; the fix of `rule-carry-over` was put off. The person wants the loss kept in view.
- The person chose to take only the conserved Spec and to put every other item off; the Slice 5 items stay on the sprint page.
- The person asked about the eight values cut at ` #` in the archived Specs of 2026-09-12 to 2026-09-21 and decided that archived Specs are archive and are not touched. Do not raise them again as a Frontier item. Their cut History lines stand on `rule-case-protocol`, `rule-retro`, `rule-page-generation` and `estimate-generate-writes`, and in `log.md`.
- C8 (`estimate-glossary-terms-defined` failed) and C9 (`estimate-documentation-completes` failed) were closed `· work`: their decisions are Cases 527 and 530 of the Spec of 2024.

## Direct instructions to the librarian

- Two units to apply: `raw/2026-09-29/2024/` — its `carry.md` is deleted in commit 734d216, so `materialize` walks it now: Cases 526–532, the readings L1, L5, L24 and the defer of Case 532 — and `raw/2026-09-30/0138/`, this session: the defer of Case 533, one lesson of each kind and four readings.
- The Work Mode boxes of the Spec of 2024 were ticked in `raw/2026-09-29/2024/spec.md`; this session's own `spec.md` holds only the deferred Case 533 and has no `tasks`.
- The Spec of 2024 renders many harness files: `case-schema.md`, the skills `hi`, `work`, `retro`, `handoff`, `pre-spec`, `.claude/agents/librarian-guppi.md`, `.claude/settings.json` (the new `Stop` hook `guppi onward`), `vault/wiki/where-to-stop.md`, the glossary and the sprint. `guppi/onward.py` stands in code; the hook fires from the first session after the render.
- `entity-glossary` is updated by Cases 527.1, 528.2, 531.1 and 531.11 in ledger order; 531.1 anchors on the text around the words 527.1 rewrites.
- `rule-carry-over` gets `deferred_by` from Case 533, while Case 531.10 names it only in `given`; no Case of that Spec changes it.

## What actually got done

Ratified: 533; 526, 527.1, 527.2, 528.1, 528.2, 528.3, 528.5, 529, 530.1, 530.2, 531.1–531.15, 532.

What got done: commit 734d216; `guppi/materialize.py`, `guppi/ratified.py`, `guppi/bashguard.py`, `guppi/onward.py` (new), `guppi/cli.py`, `guppi/prespec.py`, `guppi/gate.py`; `tests/test_ratified.py`, `tests/test_bashguard.py`, `tests/test_onward.py` (new), `tests/test_prespec.py`, `tests/test_gate.py`; `raw/2026-09-29/2024/carry.md` deleted; the remote `origin` removed by the person; make test 934 passed, 2 skipped; make style clean; lesson L1, readings L3–L6.

What is not done:
- `make lint` red before the work — `backlog: vault/wiki/backlog.md differs from its sources` and 82 lines of `guppi lint` in the Baseline of `work.md`: red before the work, the librarian's run is its reading.
- The auto mode classifier refused `git remote remove origin` twice, the person's word in the chat included: lesson L7.
- `guppi context --prompt` on `UserPromptSubmit` delivers U+FFFD in place of the dash after "400 000", while its `Stop` line keeps the dash: a deferred bug, not investigated.
- `/work` names only the session's own `spec.md`; the conserved Spec of 2024 was run from its own folder, its boxes ticked there, `carry.md` deleted in Work Mode: the rule has no words for taking up a conserved Spec.
- Case 531.10 keeps the short brief of `/carry` without Next session, so after the render the rule text still holds the defect of lesson L1 and defer 533.

78 boxes wait for the librarian.
Read in a later session: `estimate-glossary-terms-defined`, `estimate-git-context-current`, `estimate-hi-no-read-calls`, `estimate-sprint-migration-leftovers-gone`, `estimate-documentation-completes`, `estimate-bash-guard`, `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-loads`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-handoff-holds-each-fact-once`, `estimate-handoff-dispatches`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-work-mode-takes-the-work-readings`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-brief-written`, `estimate-hi-writes-frontier`, `estimate-prespec-checks-the-frontier`, `estimate-hi-takes-its-readings`, `estimate-case-protocol-defers-in-one-reply`, `estimate-retro-commit-gates`.
