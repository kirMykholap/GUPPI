# Brief — 2026-10-07, after the librarian run of session 2114

## Where things stand

- Session 2114 ratified Cases 722 (722.1, 722.2, 722.3), 723 (723.1, 723.2, 723.3), 725 (725.1, 725.2) and 726 (726.1, 726.2). No Case of the session is superseded by another. No Case 724 exists: `raw/2026-10-07/2114/cases/case-724.md` is 0 bytes (handoff, What actually got done; Direct instructions).
- Code: `guppi/casecheck.py` (`other_blocks` leaves out a stored part its top-level file no longer holds, by `left_by_its_file`, and a Case a `{supersedes}` mark of the answer's own `ratification` names); `guppi/ratified.py` (`remove_superseded` also removes a parent whose every sub-case with a decision line is retired, by `prespec.retired_whole`; new `ancestors`); `guppi/prespec.py` (new `defer_notes`, called by `plan_findings`). Tests: `tests/test_casecheck.py`, `tests/test_ratified.py`, `tests/test_prespec.py`. Handoff: `make test` 1428 passed, 6 skipped; `make style` clean.
- Readings of the session: L19–L26 — seven `passed`, `estimate-orchestration-defers-in-one-reply` `failed` (L22). Lessons: L27–L30.
- The ledger: 30 lines. The yaml: 34 entries (2 `create`, 21 `update`, 1 `defer`, 6 `estimate`, 4 `lesson`), 6 of them `update`s added by the synthesis; 2 lines folded into creates (L24 into `estimate-case-check-leaves-out-a-case-the-file-supersedes`, L25 into `estimate-prespec-notes-a-page-another-case-defers`); every ledger line is accounted for. 34 entries and 14 decision records carry `applied`; 0 `failed`, 1 `exists` (the defer of `rule-case-protocol`, L6), 0 `incomplete`, 0 `near`, 0 `merged`; `unparsed: []`.
- Pages created: decisions 14 (722, 722.1, 722.2, 722.3, 723, 723.1, 723.2, 723.3, 725, 725.1, 725.2, 726, 726.1, 726.2); estimates 2 (`estimate-case-check-leaves-out-a-case-the-file-supersedes`, `estimate-prespec-notes-a-page-another-case-defers`, each `passed` by its folded line); lessons 4 (`lesson-case-build-emptied-the-file-of-a-ratified-case`, `lesson-case-check-refuses-a-rebuild-under-a-new-number`, `lesson-orchestration-showed-a-case-while-a-round-stood-open`, `lesson-orchestration-recommended-a-rebuild-that-signed-a-promise-twice`).
- Pages updated: rules 7 (`rule-case-check` by 722.1 and 725.2, `decision-case-720` cleared from its `deferred_by`; `rule-spec-write` by 722.2; `rule-case-protocol` by 722.3, `decision-case-721` cleared and `decision-case-722.3` added to `deferred_by`; `rule-orchestration` by 723.1, `decision-case-721` cleared, `built` → `draft` by the cascade; `rule-skill-hi` by 723.3; `rule-case-build` by 725.1; `rule-prespec` by 726.2); estimates 7 (`estimate-case-check-sends-back-a-clash-with-another-case`, `estimate-spec-write-removes-a-superseded-case`, `estimate-orchestration-takes-back-a-ratified-case`, `estimate-case-build-writes-the-case`, `estimate-prespec-reconciles` — Criterion replaced, then `passed`; `estimate-orchestration-defers-in-one-reply` — Criterion replaced, then `failed`; `estimate-hi-writes-frontier` — Criterion and `method` replaced, `pending`); insights 3 and lessons 3 by the synthesis. Decisions 713, 720, 721 set `superseded` (713 by 723.1, 720 by 722.1, 721 by 722.3 and 723.1).
- The handoff's Direct instructions, as the run left them: `rule-case-protocol` ends with `deferred_by: ["[[decision-case-722.3]]"]`; `rule-orchestration` carries no `deferred_by`; `rule-case-check` carries no `deferred_by` and both replace pairs (722.1, 725.2) are in its Purpose; `estimate-hi-writes-frontier` has the 723.3 `method` and stands `pending`; the render wrote the five files the handoff names.
- The render wrote `vault/wiki/case-schema.md`, `vault/wiki/orchestration.md`, `.claude/skills/hi/SKILL.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md`. The scripts ticked 31 boxes of the 2114 Spec (26 by `generate`, 5 by `render`); one box stays open: `- [ ] read \`estimate-hi-writes-frontier\``. No unticked line of the 2114 Spec holds `guppi sprint-close`; none ran. `guppi materialize` named the 0211, 0425, 0636 and 1804 yamls ("extended with 0 entries"); the run added `superseded_by` marks to 5 entries and 3 decision records of the 1804 yaml; `generate` wrote 0 pages from those four.
- `cleanup: 3 page(s) moved`: `decision-case-713`, `decision-case-720`, `decision-case-721` to `vault/archive/migration/2026-10-07/2114/decisions/`.
- `guppi sprint` left `sprint.md` unchanged; `guppi backlog` rewrote `backlog.md` (12 items before, 12 after: `rule-case-check` and `rule-orchestration` left, `insight-orchestration-items-taken-together-unruled` and `insight-workflow-case-written-without-reading-the-pages-it-changes` came in; `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line` severity 2 → 3); `guppi glossary` left `glossary.md` unchanged. The run added 66 lines to `log.md`. `generate`, `cleanup`, `render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- `guppi archive` exit 0, no stdout, no stderr; it moved no unit. `raw/2026-10-07/0211`, `0425`, `0636`, `1804` and `2114` stay: all are dated the day of the run, and 2114 is the session of the run.
- Index check: the two `create` entries are Estimates; no Grep ran for them.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 76 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 36 lines.
- `lesson-case-build-emptied-the-file-of-a-ratified-case`: none; no index line names a Render of `rule-case-build` that tells case-guppi to empty a file against `rule-orchestration` (`lesson-case-build-splits-a-ratified-leaf-case` and `insight-ledger-ratified-line-never-withdrawn` name a missing step and a ledger line, not that instruction). Stays `new`.
- `lesson-case-check-refuses-a-rebuild-under-a-new-number` joined `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line` (`open`, stays `open`).
- `lesson-orchestration-showed-a-case-while-a-round-stood-open` joined `insight-orchestration-items-taken-together-unruled`. The Insight was `actioned` by `decision-case-699.5`; the update set it `open`, and `addressed_by` stands.
- `lesson-orchestration-recommended-a-rebuild-that-signed-a-promise-twice` joined `insight-workflow-case-written-without-reading-the-pages-it-changes`. The Insight was `actioned` by `decision-case-391.2`; the update set it `open`, and `addressed_by` stands.

## Readings due

Failed:
- `estimate-orchestration-defers-in-one-reply` — failed — `rule-orchestration` stands `draft` — read: by hand, a decision the person asks to put off, its line of `frontier.md` closed `[-] … · defer case N`, in a reply that leaves no line under the Cases heading open; a sprint item put off or a backlog item kept is not this reading (method). Result (L22): not read; in session 2114 only the sprint items C1 and C2 were put off, closed `· sprint · defer`, which the method excludes.

Pending:
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: the unticked `- [ ] read \`estimate-hi-writes-frontier\`` of the 2114 Spec; the method: the person's answer at the `/hi` of the session after the close of a sprint, written into the estimate line; unit: the frontier findings of `guppi prespec --check` in `tests/test_prespec.py`.
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run: no sprint closed; this brief is written by the librarian at the end of its run.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr; `backlog.md` holds `12 items`; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no line of the 2114 Spec holds `guppi sprint-close`, none ran; `vault/archive/` received 3 pages from `cleanup` under `migration/2026-10-07/2114/decisions/`; `guppi archive`: no stdout.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: no step read the tree for it.
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method). This run: `make lint` 14 finding lines — 1 `deferred`, 12 `unread`, 1 `method`; exit 2.
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method). This run: `make test` 1428 passed, 6 skipped, on the working tree of this run.

## Flags

- No entry marked `incomplete`, `failed`, `near` or `unparsed`. `exists`: the defer of `rule-case-protocol` (L6, case 722.3); the page was on disk and took the defer.
- Failed Estimate: `estimate-orchestration-defers-in-one-reply` (L22); by the cascade its target `rule-orchestration` went `built` → `draft`.
- Synthesis: `insight-orchestration-items-taken-together-unruled` went from `actioned` (by `decision-case-699.5`) to `open` with its new child `lesson-orchestration-showed-a-case-while-a-round-stood-open`.
- Synthesis: `insight-workflow-case-written-without-reading-the-pages-it-changes` went from `actioned` (by `decision-case-391.2`) to `open` with its new child `lesson-orchestration-recommended-a-rebuild-that-signed-a-promise-twice`.
- Lint, new this run: `estimates/estimate-hi-writes-frontier: method: a MOC's Estimate names no \`make <target>\``, after the `method` that case 723.3 set.
- Handoff, Direct instructions: `raw/2026-10-07/2114/cases/case-724.md` stands empty; no Case 724 exists.
- Handoff, Notes from memory: Case 722, Q3 — the person chose a second sub-case for the pre-spec half against the recommendation; the fix moved to the Spec hook (722.2).
- Handoff, Notes from memory: Case 722, Q6 — 722 kept as first ratified, its defer of `rule-case-protocol` included; Case 723 changed its Q3 answer; the sentence of F5 of Case 713 stays wrong and put off.
- Handoff, Notes from memory: the person's answers twice named a Case by the wrong number; the agent asked once and the person confirmed.
- Handoff, Notes from memory: Case 722 was ratified three times with the same ledger lines; its `recommend` holds `**Change**` items for each.
- Handoff, Notes from memory: the `case-guppi` of Case 726, asked whether "The body of a deferred decision is not read" stays in the new Criterion of `estimate-prespec-reconciles`, answered without saying; the Spec holds it as the last `－` line of 726.2.
- Handoff, Observations: `make lint` was red before the work, exit 2, 13 finding lines, among them `backlog: vault/wiki/backlog.md differs from its sources`, which the brief of session 1804 did not list; after this run's `guppi backlog` that line is not in the lint output.
- Handoff, Observations: the Case-file check that ran in session 2114 was the old one; Case 725.2 changes it in code this session.
- Handoff, Observations: the sprint items of the close of `migration` were put off again; the close was not prepared.
- Handoff, Observations: `ask-guppi` at pre-spec narrowed its lessons Grep against its frame, as it reported; no finding rested on it.
- Handoff, Observations: each turn in Plan Mode carried a system reminder to end with a picker or `ExitPlanMode`; the agent called `ExitPlanMode` only after `/pre-spec`.
- Contradiction, handoff For the next session: the sentence of `rule-case-protocol` that a Frontier line is closed again by the superseding Case does not hold for a sprint or backlog item whose Case is taken back (F5 of Case 713), put off again by 722.3.
- Stale defers, from the lint: `rule-morph` deferred 1 time since case 239.
- MOC candidates: the lint names none.
- The lint: 14 finding lines — 1 `deferred` (`rules/rule-morph`), 12 `unread` (11 `pending`, 1 `failed`: the 12 Estimates of Readings due), 1 `method` (`estimate-hi-writes-frontier`); `make lint` exit 2.
- Read beyond the frame: the `librarian: synthesis` entries of the 1804 `materialize.yaml`, for the synthesis — the form of `children` in an `update` of an Insight; the handoff did not ask for it.

## Next session

Cases:
- F5 of Case 713: the sentence of `rule-case-protocol` that a Frontier line is closed again by the superseding Case does not hold for a sprint or backlog item whose Case is taken back; put off again by Case 722.3 (handoff, For the next session).
- `estimate-orchestration-defers-in-one-reply` is `failed`, not read: a Case decides whether its method waits for a defer of a source other than the sprint or the backlog or reads the Render (handoff, For the next session; L22).
- Lessons L29 and L30 have no fix: how the main agent holds a Case that comes back while another Case's round is open, outside a batch; and a recommendation to widen a Criterion checked against "nothing is signed twice" before it is given (handoff, For the next session; now under `insight-orchestration-items-taken-together-unruled` and `insight-workflow-case-written-without-reading-the-pages-it-changes`, both `open`).
- The close of the sprint `migration`: a session of its own (handoff, For the next session).
- The `method` of `estimate-hi-writes-frontier` set by case 723.3 draws the lint finding "a MOC's Estimate names no `make <target>`" (lint of this run).

Work:
- `estimate-hi-takes-a-conserved-spec`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-brief-written`
- `estimate-backlog-renders`
- `estimate-sprint-close-runs-in-the-librarian-run`
- `estimate-sprint-close-next-session-opens-the-sprint`
- `estimate-sprint-close-takes-the-readings-in-groups`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`

Ask the person:
- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back?

## Readings at the close

- `make test`: 1428 passed, 6 skipped.
- `make lint`: 14 finding lines — 1 `deferred`, 12 `unread`, 1 `method`; exit 2.
- Pages under `vault/wiki/`: rules 77, estimates 246, insights 36, lessons 80, decisions 1279, entities 4.
