# Handoff — 2026-10-05, the case-file guard, the examples of orchestration.md, the readings of 0311

## Notes from memory

- The person asked why `case-guppi` searches now asked for permission; the prompts came from the builders of 654 and 655 reading transcripts under `~/.claude/projects`. The person first proposed to drop `permissionMode: acceptEdits` and to check; after the round that showed the write of the case file would then prompt or be refused, the person chose the allow rule of Case 656. Whether `acceptEdits` itself plays a part in prompts outside the project was not established.
- The person asked that the example heading of 651 be in English, since the example is documentation.
- Case 653 was ratified with its code behind `stop:`; at `/pre-spec` the ask-guppi run found its page texts would land at the librarian even if the code waited, and the person put the whole Case off (Case 659; Case 658 carried only the parent's mark and was replaced).
- 650: the `agent_id` in the `PreToolUse` input rests on the line of the 0311 handoff that the builder quoted; the ask-guppi run closed its finding on the hand reading the new Estimate's method adds, not on that quote.
- 656: the ask-guppi finding on the `rule-settings` pair (its anchor crosses a line break) was left by the person; `guppi/generate.py` joins the tokens of `old` by `\s+`.

## Direct instructions to the librarian

- Check first that `materialize` marks the lines of 653.1 and 653.2 superseded by 659 and that none of their three updates applies (`estimate-case-check-sends-back-a-faulty-case`, `rule-spec-reconcile` by 653.1, `estimate-case-check-sends-back-a-ratified-case-in-another-shape`); 658 is superseded by 659 in its own session.
- `rule-spec-reconcile` takes the pairs of 650.1 only; 653.1 also had a pair on it, which must not apply.
- 651.1 holds fourteen `replace` pairs on `rule-orchestration`, 651.2 and 651.3 one each whose `new` holds a block fenced by four backticks inside a five-backtick `then`; after the render, `vault/wiki/orchestration.md` should hold one block tagged `showing` and one tagged `defer`, and `uv run pytest tests/test_orchestration.py` should run them (4 tests, none skipped).
- 651.3 sets `addressed_by: decision-case-651.3` on the Insight; other Insights hold the form `"[[decision-case-N]]"`.
- 656: the pair on the Purpose of `rule-settings` spans lines 21–22; the render of `.claude/settings.json` should add `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)` to the allow list.
- 655 carries `{supersedes:case 649}`; the ask-guppi run noted that Estimates carry no `deferred_by`, so check what that mark clears.
- The new Estimate of 650.1 joins the `estimates` of `rule-spec-reconcile`; the two of 651 join those of `rule-orchestration`.

## What actually got done

- Cases ratified: 650 (650.1, 650.2), 651 (651.1–651.3), 652, 654, 655, 656, each built again on the findings of `/pre-spec` and ratified again; the defers 657 and 659.
- Code: `guppi/casecheck.py` — `case_number`, `held_store`, `write_store`, the docstring of the held number; `guppi/ratified.py` — `held_number`, called by `guard`, and the docstrings. Tests: `tests/test_ratified.py` (`-k number_held`, 11 tests), `tests/test_orchestration.py` new (4 tests, skipped until the render), `tests/test_case_schema.py` fails in place of skipping.
- `make test`: 1203 passed, 10 skipped (baseline 1192 passed, 6 skipped). `make style` clean.
- Readings: L1–L10 at `/hi`; the Work readings L32–L41. Lessons: L42–L44.

## Debt

No box of code, test or command is unticked.
The page, render and `read` lines of the Spec wait for the librarian.
- `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` — created by 650.1; pytest at the `/hi` of a later session, and by hand the store entry the first Write of a live `case-guppi` leaves, with its `agent_id`.
- `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — updated by 650.2; a later session.
- `estimate-orchestration-showing-example-passes-the-check`, `estimate-orchestration-defer-example-passes-the-hook` — created by 651.2, 651.3; after the render, passed and not skipped.
- `estimate-case-protocol-example-passes-the-check` — updated by 652; the `/hi` of a later session.
- `estimate-synthesis-clusters` — updated by 654; the librarian run of a later session with at least two lessons.
- `estimate-ask-searches-at-prespec` — updated by 655; the `/hi` of a later session, first over the three ask-guppi runs of the `/pre-spec` of 0311.
- `estimate-spec-write-answers-a-refusal` — its moment came in this session: Case 659 refused at the reply that acknowledged it and written at the reply that answered the refusal; read at the `/hi` of the next session.
- `estimate-spec-write-reaches-the-approved-spec` — a Case ratified in Work Mode; none in this session.
- `estimate-case-build-writes-the-case` — still lacks a `create` without a `ref` and a change of one sub-case asked by the person.
- `estimate-case-check-shows-only-the-checked-case` — the first reply the `Stop` check refuses; none in this session.
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page` — the first answer of `case-guppi` on an item from the backlog; none.
- `estimate-ask-query-before-a-create` — a `create` without a `ref`; none.
- `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-build-checks-the-finished-case` — put off by 659 and 657.
- The Estimates of the sprint close (`estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-brief-written`, `estimate-backlog-renders`, the three `estimate-sprint-close-*`, the three `estimate-sprint-migration-*`) — the session that closes the sprint, or the one after it.

## Observations

- The Spec hook removes a parent with its sub-cases on `{supersedes:case N}`, while `prespec.superseded_in_window` and `materialize.mark_superseded` mark only the number named: two readings of one mark.
- The guard of 650.1 runs from code now; the page that describes it comes with this librarian run.
- `make lint` was not run here; its baseline (exit 2, 5 `deferred`, 43 `unread`) holds no line this work changed.
- At this `/pre-spec` ask-guppi runs again broke `.claude/rules/search-leaves-out-decisions.md` (the exclusion put first, a Grep at the root without it) and the 651 run searched the archive by a wildcard; each named it, and no finding rested on it.
- Three Work readings failed: `estimate-orchestration-shows-the-built-case` (the heading of 653), `estimate-case-protocol-case-form` (`given` lines with two things or a state, a count in `then` of 652; the reading of 2026-10-03 accepted paired lines), `estimate-prespec-confirms-the-findings-once` (four sentences under a finding in three confirmations).

## For the next session

- One judgment of a `{supersedes:case N}` on a Case with sub-cases, for the Spec hook, `prespec` and `materialize`.
- Remove the skips of `tests/test_orchestration.py` once its two Estimates pass.
- `estimate-case-protocol-case-form` failed: whether `case-guppi` changes or the Criterion accepts a pair such as a module and its test on one line.
- `estimate-prespec-confirms-the-findings-once` failed: the confirmation of ask-guppi exceeds three sentences.
- `estimate-orchestration-shows-the-built-case` failed: the heading of a top-level Case whose summary carries no line for it.
- `estimate-search-leaves-out-decisions-in-every-agent` failed (L10).
- C1 and C2 of the sprint were left for a later session.

## Ask the person

- `estimate-permissions` — needs the person — in the session after the render of `.claude/settings.json`, did a Read, Grep or Glob of `case-guppi` under `~/.claude/projects/c--PROJECTS-GUPPI/` still ask for permission?
