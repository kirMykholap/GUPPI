# Handoff — 2026-09-29, Slice 3g and the form of a round

## Notes from memory

- Every Case of the session was ratified twice: first as built, then again after `/pre-spec`, whose `ask-guppi` found faults in 497, 498–500, 501 and 502. The second ratification's lines are in the same ledger; the ledger hook did not write the lines twice. The Spec holds the rebuilt texts.
- On 501 the person reopened the choice after the first build: the question shape moved from the instructions of `case-guppi` into the `grill-me` template. They twice rejected a "cost" label under an option: an option carries one After item and nothing else.
- On pre-spec finding 7 (translated labels) the person said the language of the labels does not matter at all.
- On pre-spec finding 5 (defer 442 on `rule-ledger-write`, a missing mark) the person chose to leave it deferred; 497 catches only a wrong mark.
- The person wanted a heading and a separate "what the agent noticed" part in the Retro report, and wants the form of Retro discussed again (Case 505). They want to keep `/retro` called at once at the end of Work Mode, with no stop.
- The person complained that the first report after pre-spec was unreadable: its numbers came from the answer of `ask-guppi`, regrouped by Case and out of order. No lesson was written, at the person's word; Cases 503 and 504 carry the fix and the idea.
- The person asked about the look of the Frontier at `/hi`: earlier sessions showed bold `C1` lines, and the checkbox form belongs to the acknowledging reply. They left it for later; no item was made.

## Direct instructions to the librarian

- `entity-sprint-migration` is updated three times (498.6, 499.3, 500.6). Only 500.6 changes the page: its `replace` pair swaps the Slice 3g note. Apply them in ledger order. After `guppi sprint`, Slice 3g should hold one note, on removing the checks of the old shape.
- After this run, `make lint` should count no `unmigrated` page: Cases 498–500 recut the last twelve old-shape Estimates. Say the count in the brief.
- Render order: `.claude/skills/grill-me/SKILL.md` (501.1) before `.claude/skills/wait-what/SKILL.md` (502), which points to it. `.claude/agents/case-guppi.md` (501.2), `.claude/skills/handoff/SKILL.md` (499.2) and `vault/wiki/case-schema.md` (497.4) render too.
- 501.2 carries `{supersedes:case 495}` on `rule-case-build`, and 502 carries `{supersedes:case 496}` on `rule-skill-wait-what`. Both pages should leave `backlog.md`. The defers 503 (`rule-prespec`), 504 (`rule-complaint-becomes-a-lesson`, a new placeholder with no ref) and 505 (`rule-retro`) enter it.
- `estimate-ledger-write-refuses-a-mark-with-no-decision-line` is the only `create` of the session.

## What actually got done

Ratified: 497.1–497.4, 498.1–498.6, 499.1–499.3, 500.1–500.6, 501.1–501.2, 502, 503, 504, 505.

What got done: commits 83ff1ca (code) and 8d5798c (the session folder); `guppi/materialize.py` (`marks_without_decision`, which `lift_line` now calls), `guppi/ledger.py` (`refused_marks` and its stderr line), `guppi/render.py` (the docstring states the finding of probe 139.1), `tests/test_ledger.py` (9 tests, one of them runs the hook and `materialize` on the same lines); the stale `guppi/__pycache__/__init__.cpython-314.pyc` removed; `make test` 900 passed, 2 skipped; `make style` clean. No reading and no lesson was written.

What is not done:
- The readings of Readings due and the unticked `read` lines of the Specs of 2229, 2000, 1318 and 0000 were not taken. They go to a later session; the Estimates this session updates drop out of that list and are read by their new Criterion.
- `make lint` held 145 findings before the work (Baseline of `work.md`); red before the work, not charged to this session.
- The ledger hook refuses a mark with no decision line before it from the working tree now; the rule of 497.4 reaches `case-schema.md` only at this run's render.
- `materialize` judges the mark by the order of the ledger lines, not by the yaml entries: a decision line whose lift failed now counts as a decision line before the lesson.
- The harness filter "settings-json" fired twice on answers of `case-guppi` for 498–500, on a `given` line naming `.claude/settings.json`; the Case texts were unchanged.
- The form of the Retro report: short defer, Case 505.

34 boxes wait for the librarian.
Read in a later session: `estimate-ledger-write-refuses-a-mark-with-no-decision-line`, `estimate-ledger-write-lifts`, `estimate-ledger-write-refuses-a-lesson-without-its-prefix`, `estimate-case-protocol-ledger-line-form`, `estimate-render-harness-reproduces`, `estimate-render-sync-reports`, `estimate-settings`, `estimate-default-mode`, `estimate-governed-files-hook-refuses`, `estimate-end-of-work-order`, `estimate-handoff-dispatches`, `estimate-ask-finds`, `estimate-index-check-merges`, `estimate-cleanup-moves`, `estimate-raw-archive`, `estimate-tests-clock-pinned`, `estimate-skill-grill-me-asks-in-rounds`, `estimate-case-build-writes-a-plain-round`, `estimate-skill-wait-what-re-pitches`.
