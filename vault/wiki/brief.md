# Brief — 2026-10-03, session 1416: the conserved Spec of session 1341 run by /box

## Where things stand

- The conserved Spec of session 1341 ran by `/box` on `spec/2026-10-03-1341`: Case 614 (`create entity-reading-probe`) and the defers of Cases 615–618. No Case was ratified in session 1416.
- No code file or test changed; `vault/raw/2026-10-03/1341/carry.md` deleted. `make test` at the handoff: 1129 passed, 6 skipped; `make style` clean.
- Readings: ledger of 1341 lines 1–4 (3 passed, 1 failed); ledger of 1416 lines 1–7 passed, line 8 failed, line 9 passed. Lesson: 1416 line 10.
- This run, from `raw/2026-10-03/1341/materialize.yaml` (9 entries) and `raw/2026-10-03/1416/materialize.yaml` (10 entries and 3 of the synthesis); the yaml of 0115 and 0317 were extended with 0 entries:
  - created: decisions 5 (`decision-case-614` to `decision-case-618`); entities 1 (`entity-reading-probe`, marked `near: entity-glossary`); lessons 1 (`lesson-session-ledger-item-deferred-by-the-conserved-spec-closed-as-work`); insights 1 (`insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan`, synthesis).
  - updated: estimates 14 pages (13 readings, 11 passed and 2 failed; the defers of Cases 617 and 618, one of them on a page also read); entities 2 (the defers of Cases 615 and 616 on `entity-sprint-migration` and `entity-guppi`); lessons 1 (`lesson-frontier-has-no-closer-for-a-milestone-item-left-on-the-sprint-page` clustered); rules 6 by the cascade, `draft → built`: `rule-ledger-write`, `rule-carry-over`, `rule-compact-recall`, `rule-event-log`, `rule-plan-mode`, `rule-spec-capture`.
  - Spec boxes ticked: `create entity-reading-probe` of 1341; `read estimate-orchestration-defers-in-one-reply` of 0115; three `read` boxes of 0317 (`estimate-case-check-refuses-text-outside-the-list`, `estimate-lint-reports-a-method-tied-to-a-one-off-moment`, `estimate-hi-takes-its-readings`).
  - `backlog.md` no longer lists a conserved Spec; it lists `entity-guppi`, `entity-sprint-migration` and the new Insight under Deferred.
- Index check: the Grep `^(purpose|deferred_by):` over `vault/wiki/entities/` printed 4 lines; the `create` of `entity-reading-probe` kept and marked `near: entity-glossary` — its purpose repeats the meaning of the purpose of `entity-glossary` and says it is a test page, not the source of `glossary.md`.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 74 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 30 lines.
  - `lesson-session-ledger-item-deferred-by-the-conserved-spec-closed-as-work` joined `lesson-frontier-has-no-closer-for-a-milestone-item-left-on-the-sprint-page` in the new `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan`: both lessons name a Frontier line whose end stands outside the session's own plan and fits no closer, closed `work`. Both lessons now `clustered`.

## Readings due

- `estimate-hi-takes-a-conserved-spec` — failed · `rule-skill-hi` `draft` · method: `uv run guppi render --check`; by hand, a session whose person takes a conserved Spec at the Frontier. Result (1416 L8): C4, the failed reading of `estimate-handoff-holds-each-fact-once` deferred by Case 618 of the conserved Spec, was refused as `· ledger · defer case 618` by `uv run guppi prespec --check` and closed `[x] … · ledger · work`, a closer the Criterion does not list.
- `estimate-handoff-holds-each-fact-once` — failed · `rule-handoff` `draft` · method: one reading by hand at a /handoff, against the close of its Retro. Result (1341 L2): the handoff of 0317 names Case 613.3 in four sections, and Cases 611 and 612.1, the two lessons and `estimate-hi-takes-its-readings` in two. Put off by Case 618.
- `estimate-orchestration-shows-the-built-case` — failed · `rule-orchestration` `draft` · box `raw/2026-10-03/0317/spec.md:122`; method: by hand, the Cases of a session at its close against its Agent, SendUserFile, Skill and SendMessage calls. Result (0115 L18): the showing of Case 610 put a sentence of its own between the heading of the Case and its list. Put off by Case 617.
- `estimate-ask-finds` — pending · `rule-ask` `draft` · method: three dispatches of ask-guppi in a later session, read against the event log
- `estimate-case-check-requires-each-question-of-the-rounds` — pending · `rule-case-check` `draft` · method: pytest `-k rounds`, then by hand a Case the hook sends back for a missing title
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — pending · `rule-case-check` `draft` · box `raw/2026-10-03/0115/spec.md:398`; method: pytest `-k clash`, then by hand an answer the hook sends back for this reason
- `estimate-case-check-sends-back-a-faulty-case` — pending · `rule-case-check` `draft` · box `raw/2026-10-03/0115/spec.md:99`; method: pytest `-k subagent`, then by hand an answer the hook sends back
- `estimate-case-check-sends-back-a-faulty-round` — pending · `rule-case-check` `draft` · box `raw/2026-10-03/0115/spec.md:141`; method: pytest `-k round_form`, then by hand a round the hook sends back live
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — pending · `rule-case-check` `draft` · box `raw/2026-10-03/0115/spec.md:353`; method: pytest `-k shape`, then by hand an answer the hook sends back for this reason
- `estimate-generate-rewords` — pending · `rule-page-generation` `draft` · method: pytest on a temp vault; the live reading a librarian's run that applies a reword · this run: neither yaml of 1341 nor of 1416 carries a `reword` item; `guppi generate` printed 0, 0, 14 and 17 pages written or changed for 0115, 0317, 1341 and 1416; the lines this run added to `log.md` hold no `reworded` line
- `estimate-handoff-dispatches` — pending · `rule-handoff` `draft` · method: by hand at the /handoff of a later session and of a session that /box runs: the event log, handoff.md, the dispatch line and git log
- `estimate-lint-runs-every-step` — pending · `rule-lint` `draft` · method: the make lint of the Baseline of a later /work whose backlog step is red
- `estimate-orchestration-signs-a-batch-together` — pending · `rule-orchestration` `draft` · method: by hand at a Plan Mode in which the person's word asks that a ratified Case change
- `estimate-prespec-onward-sends-the-agent-on` — pending · `rule-prespec-onward` `draft` · method: pytest; by hand at a Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification
- `estimate-ratification-ledger-line-form` — pending · `rule-ratification` `draft` · method: by hand, a session where a lesson and the Case that closes its cause stand together, and a Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-retro-loads` — pending · `rule-retro` `draft` · method: by hand at a /retro, and at a /retro of a session that /box runs
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — pending · `rule-retro-onward` `draft` · method: pytest; by hand at an end of Retro at which the ledger hook refuses a line
- `estimate-retro-runs-on-to-the-handoff` — pending · `rule-retro` `draft` · method: by hand at a run from /work to the librarian, and at a Retro where the ledger hook refuses a line
- `estimate-session-start-context` — pending · `rule-session-start` `draft` · method: `make test-session-start`; by hand, a session opened without /hi whose reply carries a LEDGER block
- `estimate-spec-box-runs-a-conserved-spec` — pending · `rule-spec-box` `draft` · method: `uv run guppi render --check`; by hand, a session that runs a conserved Spec by /box: git log, the branches, the folders, the dispatch line and the librarian's commit · this run: on branch `migration`; at its start the tree held one untracked file, `vault/raw/2026-10-03/1416/handoff.md`; the librarian's commit follows this brief
- `estimate-spec-write-reaches-the-approved-spec` — pending · `rule-spec-write` `draft` · method: pytest `-k approved_spec`; by hand, a Case ratified in Work Mode
- `estimate-sprint-close-archives-done-insights-and-lone-lessons` — pending · `rule-sprint-close` `draft` · box `raw/2026-10-03/0317/spec.md:300`; method: by hand after the first close of a sprint
- `estimate-sprint-close-archives-the-decisions` — pending · `rule-sprint-close` `draft` · box `raw/2026-10-03/0317/spec.md:263`; method: by hand after the first close of a sprint
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` — pending · `rule-sprint-close` `draft` · box `raw/2026-10-03/0317/spec.md:336`; method: by hand after the first close of a sprint
- `estimate-sprint-close-settles-unread-estimates` — pending · `rule-sprint-close` `draft` · box `raw/2026-10-03/0317/spec.md:375`; method: by hand, the record of the first close of a sprint
- `estimate-sprint-migration-leftovers-gone` — pending · `entity-sprint-migration` `draft` · method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — pending · `entity-sprint-migration` `draft` · method: `make lint`, exit 0 — or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — pending · `entity-sprint-migration` `draft` · method: `make test` on the last commit of migration, then git log of main after the merge
- `estimate-where-to-stop-stops-only-on-its-conditions` — pending · `rule-where-to-stop` `draft` · method: by hand at a run from /work to the librarian, and at a run of /box
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending · `rule-work-mode` `draft` · method: `uv run guppi render --check`; by hand, a /work the agent calls at the fork, a /work the person types and a /work that /box calls
- `estimate-work-mode-takes-the-work-readings` — pending · `rule-work-mode` `draft` · method: by hand at a /work and at a /work that /box calls

## Flags

- `near`: the `create` of `entity-reading-probe` (1341 L5) marked `near: entity-glossary`, as Case 614 expects; not merged.
- No entry marked `incomplete`, `failed` or `unparsed`; `guppi generate`, `cleanup`, `render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- Failed Estimates: `estimate-hi-takes-a-conserved-spec`, `estimate-handoff-holds-each-fact-once`, `estimate-orchestration-shows-the-built-case`.
- The defers of Cases 617 and 618 wrote a History line `deferred` on `estimate-orchestration-shows-the-built-case` and `estimate-handoff-holds-each-fact-once` and no `deferred_by` field; `guppi/generate.py` marks `deferred_by` on a Rule, an Entity or an Insight only (case 124.2), and `backlog.md` lists neither Estimate.
- Stale defers, from `make lint`: `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239.
- `make lint`, exit 2, 39 lines: `entities/entity-reading-probe: schema: missing field parent (given {'kind': 'Leaf'})` and `entities/entity-reading-probe: orphan: no other live page names it in its frontmatter` (as Case 614 expects); 5 `deferred`; 28 `unread: pending`; 3 `unread: failed`; the make error line.
- The handoff names `estimate-index-check-merges` among the readings of the next `/hi`, from the report of this run; its page stands `passed`, so it is not under Readings due.
- No MOC candidate and no contradiction found.

## Next session

Cases:
- Which closer a Frontier line of the ledger Tail takes when the conserved Spec the person takes already defers its target: `rule-skill-hi` lists none, and `guppi prespec` judges `defer case N` only against the Cases of the session's own plan (handoff, For the next session).
- A Case replaces `quillwort` by `bramblewort` by `reword` and then deletes `entity-reading-probe`, before any close of the sprint (handoff, For the next session).
- `estimate-hi-takes-a-conserved-spec` failed (1416 L8).
- `estimate-handoff-holds-each-fact-once` failed (1341 L2), put off by Case 618.
- `estimate-orchestration-shows-the-built-case` failed (0115 L18), put off by Case 617.

Work:
- `estimate-ask-finds`
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-sends-back-a-faulty-round`
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- `estimate-generate-rewords`
- `estimate-handoff-dispatches`
- `estimate-lint-runs-every-step`
- `estimate-orchestration-signs-a-batch-together`
- `estimate-prespec-onward-sends-the-agent-on`
- `estimate-ratification-ledger-line-form`
- `estimate-retro-loads`
- `estimate-retro-onward-sends-the-agent-to-the-handoff`
- `estimate-retro-runs-on-to-the-handoff`
- `estimate-session-start-context`
- `estimate-spec-box-runs-a-conserved-spec`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-close-archives-done-insights-and-lone-lessons`
- `estimate-sprint-close-archives-the-decisions`
- `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
- `estimate-sprint-close-settles-unread-estimates`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-where-to-stop-stops-only-on-its-conditions`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-work-mode-takes-the-work-readings`
- the unticked boxes of the Specs: 4 `read` of `raw/2026-10-03/0115/spec.md`, 5 `read` of `raw/2026-10-03/0317/spec.md`; each names a reading above or under Cases

Ask the person:
- none

## Readings at the close

- `make test`: 1129 passed, 6 skipped.
- `make lint`: exit 2, 39 lines (2 on `entity-reading-probe`, 5 deferred, 28 unread: pending, 3 unread: failed, the make error line).
- Pages: rules 78, entities 5, estimates 201, lessons 75, insights 30, decisions 1018; archive 757 files.
- Ledger lines: 1341 9 of 9 and 1416 10 of 10 have an entry in the yaml.
