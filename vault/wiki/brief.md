# Brief — 2026-10-04, session 0004: the test page reworded and deleted, a line put off by the conserved Spec, readings

## Where things stand

- Ratified in session 0004: 619 (619.1, 619.2) and 620 (620.1, 620.2); put off: 621, 622, 623.
- Code: `guppi/prespec.py` — `conserved_blocks` and `has_defer_item`; `check_frontier` takes the plan and looks for the `defer` item of `defer case N` in the conserved Spec its title line names, by `conserved_spec_named` of `guppi/box.py`. `tests/test_prespec.py` — three tests. `make test` at the handoff: 1132 passed, 6 skipped; `make style` clean.
- Readings: ledger lines 1–6 and 14–16 passed, line 17 failed (`estimate-ask-finds`). Lessons: lines 22 and 23.
- This run, from `raw/2026-10-04/0004/materialize.yaml` (23 entries and 4 of the synthesis); the yaml of 0115, 0317, 1341 and 1416 were extended with 0 entries and `generate` changed 0 pages for each:
  - created: decisions 9 (`decision-case-619`, `619.1`, `619.2`, `620`, `620.1`, `620.2`, `621`, `622`, `623`); lessons 2 (`lesson-case-build-a-page-judged-true-by-its-mark-not-its-moment`, `lesson-case-build-hits-counted-as-lines`, both clustered).
  - updated: estimates 14 pages (10 readings, 9 passed and 1 failed; the Criteria of `estimate-hi-takes-a-conserved-spec` and `estimate-prespec-checks-the-frontier` replaced whole and set `pending`; the defers of Cases 621, 622 and 623, one of them on a page also read); entities 1 (`entity-reading-probe`, reworded `quillwort` → `bramblewort`, then deleted); rules 3 by Case (`rule-skill-hi`, `rule-orchestration`, `rule-prespec`) and 7 by the cascade — `draft → built`: `rule-prespec-onward`, `rule-retro-onward`, `rule-retro`, `rule-spec-box`, `rule-where-to-stop`, `rule-work-mode`; `built → draft`: `rule-prespec`; insights 2 (`insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan` set `actioned` by Case 620.1; `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` given two children by the synthesis).
  - archived by the cascade of the actioned Insight: `lesson-frontier-has-no-closer-for-a-milestone-item-left-on-the-sprint-page`, `lesson-session-ledger-item-deferred-by-the-conserved-spec-closed-as-work`. `guppi cleanup` moved 3 pages to `vault/archive/migration/2026-10-04/0004/`: those two lessons and `entity-reading-probe`.
  - `guppi archive` moved the session folders `raw/2026-10-03/0115`, `0317`, `1341` and `1416` to `archive/migration/2026-10-03/<HHMM>/raw`; `raw/2026-10-03/` keeps `event_log.md`; the session of this run, `raw/2026-10-04/0004`, stays.
  - rendered: `.claude/skills/hi/SKILL.md` and `vault/wiki/orchestration.md`.
  - Spec boxes ticked: 10 in `raw/2026-10-04/0004/spec.md` (the update and the delete of `entity-reading-probe`, the four updates of 620.1, its two render boxes, the two updates of 620.2).
  - `backlog.md`: 22 → 21 items; the actioned Insight left Deferred; `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` now shows severity 3 (was 1). `sprint.md` and `glossary.md` unchanged.
- Index check: the yaml holds no `create` entry; the two `lesson` entries are compared in the synthesis below; neither is the same event as a live lesson, so no merge and no `near`.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 75 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
  - `lesson-case-build-a-page-judged-true-by-its-mark-not-its-moment` joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`: the context judged `rule-orchestration` true on a Grep of the word `defer case`, a check narrower than the claim.
  - `lesson-case-build-hits-counted-as-lines` joined `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`, beside its child `lesson-case-build-a-count-in-context-not-from-a-run` (as the handoff names): a count taken from the agent's own reading of an output, not from a command that counts the thing claimed.
  - The Insight stays `open`; neither lesson entry carries `addressed_by`.

## Readings due

- `estimate-ask-finds` — failed · `rule-ask` `draft` · method: by hand in a later session, three dispatches of ask-guppi read against the event log. Result (0004 L17): two of the four /pre-spec dispatches since case 582 (0317, 1416) do not open with the five lines the Criterion requires. Put off by Case 623.
- `estimate-handoff-holds-each-fact-once` — failed · `rule-handoff` `draft` · method: one reading by hand at a /handoff, against the close of its Retro. Result (1341 L2): the handoff of 0317 names Case 613.3 in four sections. Put off by Case 621.
- `estimate-orchestration-shows-the-built-case` — failed · `rule-orchestration` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:122`; method: by hand, the Cases of a session at its close against its Agent, SendUserFile, Skill and SendMessage calls. Result (0115 L18): the showing of Case 610 put a sentence of its own between the heading of the Case and its list. Put off by Case 622.
- `estimate-case-check-requires-each-question-of-the-rounds` — pending · `rule-case-check` `draft` · method: pytest `-k rounds`, then by hand a Case the hook sends back for a missing title
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — pending · `rule-case-check` `draft` · box `archive/migration/2026-10-03/0115/raw/spec.md:398`; method: pytest `-k clash`, then by hand an answer the hook sends back for this reason
- `estimate-case-check-sends-back-a-faulty-case` — pending · `rule-case-check` `draft` · box `archive/migration/2026-10-03/0115/raw/spec.md:99`; method: pytest `-k subagent`, then by hand an answer the hook sends back
- `estimate-case-check-sends-back-a-faulty-round` — pending · `rule-case-check` `draft` · box `archive/migration/2026-10-03/0115/raw/spec.md:141`; method: pytest `-k round_form`, then by hand a round the hook sends back live
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — pending · `rule-case-check` `draft` · box `archive/migration/2026-10-03/0115/raw/spec.md:353`; method: pytest `-k shape`, then by hand an answer the hook sends back for this reason
- `estimate-generate-rewords` — pending · `rule-page-generation` `draft` · method: pytest on a temp vault; the live reading a librarian's run that applies a reword · this run: `guppi generate` printed `generate: reword ` + "`quillwort` → `bramblewort`" + `: entities/entity-reading-probe (1)` and `2026-10-04/0004: 39 page(s) written or changed`; yaml lines 7 (the update with the reword) and 8 (the delete) both carry `applied`, in that order; the History of `vault/archive/migration/2026-10-04/0004/entities/entity-reading-probe.md` holds `reworded: ` + "`quillwort` → `bramblewort`" + ` · [[decision-case-619.1]]` before `deleted · [[decision-case-619.2]]`; `log.md` gained the line `entities/entity-reading-probe reworded: ` + "`quillwort` → `bramblewort`" + ` · [[decision-case-619.1]] · generate`; after the run a count of `quillwort` over `vault/wiki/` found it in `brief.md` (1) and `log.md` (2) only; the Estimate status changes this run wrote to `log.md` each cite an `estimate` ledger line (L1–6, L14–17)
- `estimate-hi-takes-a-conserved-spec` — pending · `rule-skill-hi` `draft` · box `raw/2026-10-04/0004/spec.md:176`; method: `uv run guppi render --check`; by hand, a session whose person takes a conserved Spec at the Frontier
- `estimate-lint-runs-every-step` — pending · `rule-lint` `draft` · method: the make lint of the Baseline of a later /work whose backlog step is red
- `estimate-orchestration-signs-a-batch-together` — pending · `rule-orchestration` `draft` · method: by hand at a Plan Mode in which the person's word asks that a ratified Case change
- `estimate-prespec-checks-the-frontier` — pending · `rule-prespec` `draft` · box `raw/2026-10-04/0004/spec.md:221`; method: `uv run pytest tests/test_prespec.py`
- `estimate-ratification-ledger-line-form` — pending · `rule-ratification` `draft` · method: by hand, a session where a lesson and the Case that closes its cause stand together, and a Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-session-start-context` — pending · `rule-session-start` `draft` · method: `make test-session-start`; by hand, a session opened without /hi whose reply carries a LEDGER block
- `estimate-spec-write-reaches-the-approved-spec` — pending · `rule-spec-write` `draft` · method: pytest `-k approved_spec`; by hand, a Case ratified in Work Mode
- `estimate-sprint-close-archives-done-insights-and-lone-lessons` — pending · `rule-sprint-close` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:300`; method: by hand after the first close of a sprint
- `estimate-sprint-close-archives-the-decisions` — pending · `rule-sprint-close` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:263`; method: by hand after the first close of a sprint
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` — pending · `rule-sprint-close` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:336`; method: by hand after the first close of a sprint
- `estimate-sprint-close-settles-unread-estimates` — pending · `rule-sprint-close` `draft` · box `archive/migration/2026-10-03/0317/raw/spec.md:375`; method: by hand, the record of the first close of a sprint
- `estimate-sprint-migration-leftovers-gone` — pending · `entity-sprint-migration` `draft` · method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — pending · `entity-sprint-migration` `draft` · method: `make lint`, exit 0 — or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — pending · `entity-sprint-migration` `draft` · method: `make test` on the last commit of migration, then git log of main after the merge

## Flags

- No entry of the 0004 yaml marked `incomplete`, `failed`, `near` or `unparsed` (`unparsed: []`); `guppi generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary` and `archive` printed nothing on stderr.
- The yaml of 0115 (now `archive/migration/2026-10-03/0115/raw/materialize.yaml`), lines 3–6 (Case 608), carry `superseded_by: 610.1` and neither `applied` nor `failed`; line 3 carries `incomplete: [criterion]`. They stand as earlier runs left them.
- Failed Estimates: `estimate-ask-finds`, `estimate-handoff-holds-each-fact-once`, `estimate-orchestration-shows-the-built-case`.
- The defers of Cases 621, 622 and 623 wrote a History line `deferred` on the three failed Estimates and no `deferred_by` field; `backlog.md` lists none of them (as the handoff says).
- The handoff notes that the readings of lines 6, 14, 15 and 16 were closed `passed` on the person's word, with the moment no one brings on by hand written as not exercised; the `method` of each still names that moment.
- Stale defers, from `make lint`: `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239.
- `make lint`, exit 2, 29 lines: 5 `deferred`; 20 `unread: pending`; 3 `unread: failed`; the make error line. No finding on `entity-reading-probe`.
- A read my frame says the run does not need: a Grep of the text of the archived page `vault/archive/migration/2026-10-04/0004/entities/entity-reading-probe.md` (its `status`, `reworded` and `deleted` lines), for the Readings due line of `estimate-generate-rewords`, whose Criterion names the History line `reworded`.
- No MOC candidate and no contradiction found.

## Next session

Cases:
- Whether the `method` of the Estimates read on the person's word drops the moment no one brings on by hand — a `/work` the person types, a refusal of the ledger hook — or keeps it as a part not exercised (handoff, For the next session).
- `rule-sprint-close` and where the close of a sprint runs, Slice 5, put off again (handoff, For the next session).
- `estimate-ask-finds` failed (0004 L17), put off by Case 623.
- `estimate-handoff-holds-each-fact-once` failed (1341 L2), put off by Case 621.
- `estimate-orchestration-shows-the-built-case` failed (0115 L18), put off by Case 622.

Work:
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-sends-back-a-faulty-round`
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- `estimate-generate-rewords`
- `estimate-hi-takes-a-conserved-spec`
- `estimate-lint-runs-every-step`
- `estimate-orchestration-signs-a-batch-together`
- `estimate-prespec-checks-the-frontier`
- `estimate-ratification-ledger-line-form`
- `estimate-session-start-context`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-close-archives-done-insights-and-lone-lessons`
- `estimate-sprint-close-archives-the-decisions`
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
- `estimate-sprint-close-settles-unread-estimates`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- the unticked boxes of the Specs: 4 `read` of `archive/migration/2026-10-03/0115/raw/spec.md`, 5 `read` of `archive/migration/2026-10-03/0317/raw/spec.md`, 2 `read` of `raw/2026-10-04/0004/spec.md`; each names a reading above or under Cases

Ask the person:
- none

## Readings at the close

- `make test`: 1132 passed, 6 skipped.
- `make lint`: exit 2, 29 lines (5 deferred, 20 unread: pending, 3 unread: failed, the make error line).
- Pages: rules 78, entities 4, estimates 201, lessons 75, insights 30, decisions 1027; archive 786 `.md` files, 864 files in all.
- Ledger lines: 0004 23 of 23 have an entry in the yaml.
