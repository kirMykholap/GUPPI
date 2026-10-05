# Brief — 2026-10-05, after the librarian run of session 1343

## Where things stand

- Session 1343 ratified Cases 650 (650.1, 650.2), 651 (651.1–651.3), 652, 654, 655 and 656, each built again on the findings of `/pre-spec`, and the defers 657 and 659; Case 653 was put off whole by 659 (658 superseded by 659).
- Code: `guppi/casecheck.py` (`case_number`, `held_store`, `write_store`), `guppi/ratified.py` (`held_number`, called by `guard`); tests `tests/test_ratified.py` (`-k number_held`, 11), `tests/test_orchestration.py` (new, 4), `tests/test_case_schema.py` fails in place of skipping. Handoff: `make test` 1203 passed, 10 skipped; `make style` clean.
- Readings: L1–L10 at `/hi`, the Work readings L32–L41; lessons L42–L44.
- The yaml: 50 entries (44 from the ledger, 6 of the synthesis); 46 applied; 4 not applied, superseded by case 659 (L21, L22, L23, L29); 0 failed; 0 entries marked `incomplete`; `exists` on the three defers (L28, L29, L31); `unparsed: []`.
- Pages created: estimates 3 (`estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`, `estimate-orchestration-showing-example-passes-the-check`, `estimate-orchestration-defer-example-passes-the-hook`); lessons 3; decisions 17 (13 live, 653, 653.1, 653.2 and 658 archived as superseded).
- Pages updated: rules 4 (`rule-spec-reconcile` by the four pairs of 650.1 only, `rule-orchestration` by 651.1–651.3, `rule-permissions`, `rule-settings`); estimates 26 (20 readings, 5 Criteria replaced by 650.2, 652, 654, 655, 656, and the defers 657 and 659); insights 3 (synthesis, and 651.3 on `insight-workflow-case-schema-silent-on-what-the-scripts-accept`, now `actioned`, `addressed_by: "[[decision-case-651.3]]"`); lessons 3 (synthesis).
- Pages archived by `generate` and `cleanup`: 11 — decisions 649, 653, 653.1, 653.2, 658 (superseded); lessons 6 (the five clustered children of `insight-workflow-case-schema-silent-on-what-the-scripts-accept` still live, and the new `lesson-orchestration-defer-acknowledged-without-its-short-form`), under `vault/archive/migration/2026-10-05/1343/`.
- The handoff checks: the three updates of 653.1 and 653.2 and the defer 658 carry `superseded_by: '659'` and were not applied; `vault/wiki/orchestration.md` holds one block tagged `showing` and one tagged `defer`; `uv run pytest tests/test_orchestration.py`: 4 passed, none skipped; `.claude/settings.json` holds `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`; the pair of 656 on `rule-settings` applied across its line break. `{supersedes:case 649}` of 655 marked the 0311 yaml entry of 649 and its decision record `superseded_by` 655 and archived `decision-case-649`; the Estimate carries no `deferred_by`, so no field on it was cleared.
- The render ticked the two `uv run guppi render` lines of the Spec; `guppi sprint`, `guppi backlog` and `guppi glossary` wrote their files with no stderr.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 81 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
- `lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases` joined `insight-harness-one-rule-implemented-twice-drifts` (it was `actioned` by case 360; reopened, `status: open`).
- `lesson-orchestration-defer-acknowledged-without-its-short-form` joined `insight-workflow-case-schema-silent-on-what-the-scripts-accept` (open on disk at the synthesis, set `actioned` by 651.3 in this run; status left as 651.3 set it; the lesson archived by the cascade).
- `lesson-orchestration-case-heading-named-from-the-frontier-item` joined `insight-case-show-built-case-retyped-by-hand` (it was `actioned` by case 458; reopened, `status: open`).

## Readings due

- `estimate-search-leaves-out-decisions-in-every-agent` — failed — `rule-search-leaves-out-decisions` stands `draft` — L10: 9 Greps over `vault/`, `vault/wiki/` or the root without `!**/decisions/**` in the transcripts of 0311; two Reads of a Decision page for no reason of their frame — read: by hand at the `/hi` of a later session (method).
- `estimate-orchestration-shows-the-built-case` — failed — `rule-orchestration` stands `draft` — L36: the heading of Case 653 rendered Frontier item C3, its summary holding items for 653.1 and 653.2 only — read: by hand, the Cases of a session at its close (method).
- `estimate-case-protocol-case-form` — failed — `rule-case-protocol` stands `draft` — L38: `given` with two things on a line (650.1, 650.2, 653.1, 654) and with state (656, 653.1); a count in `then` of 652 — read: by hand, the Cases of a session at its close (method).
- `estimate-prespec-confirms-the-findings-once` — failed — `rule-prespec` stands `draft` — L41: the runs on 650 (3.1), 652 (1.1) and 654 (1.1) wrote four sentences under one finding — read: at the `/pre-spec` of a later session whose findings send a Case back (method).
- `estimate-case-build-checks-the-finished-case` — failed — `rule-case-build` stands `draft` — L22 of session 0109: the ask-guppi runs at `/pre-spec` of 0109 found pages and rules the Cases missed; put off by case 657 — read: at `/pre-spec` of a later session after the render (method).
- `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` — pending — `rule-spec-reconcile` stands `draft` — read: `- [ ] read` line of spec.md 1343; `uv run pytest tests/test_ratified.py -k number_held`, and by hand the store entry the first Write of a live `case-guppi` leaves.
- `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — pending — `rule-spec-reconcile` stands `draft` — read: `- [ ] read` line of spec.md 1343.
- `estimate-orchestration-showing-example-passes-the-check` — pending — `rule-orchestration` stands `draft` — read: `- [ ] read` line of spec.md 1343.
- `estimate-orchestration-defer-example-passes-the-hook` — pending — `rule-orchestration` stands `draft` — read: `- [ ] read` line of spec.md 1343.
- `estimate-case-protocol-example-passes-the-check` — pending — `rule-case-protocol` stands `draft` — read: `- [ ] read` line of spec.md 1343, at the `/hi` of a later session.
- `estimate-ask-searches-at-prespec` — pending — `rule-ask` stands `draft` — read: `- [ ] read` line of spec.md 1343.
- `estimate-permissions` — pending — `rule-permissions` stands `draft` — read: `- [ ] read` line of spec.md 1343; the live probe is the person's word.
- `estimate-synthesis-clusters` — pending — `rule-synthesis` stands `draft` — read: `- [ ] read` line of spec.md 1343 — this run: the brief names `^(root_cause|deferred_by):` over `vault/wiki/lessons/` with 81 lines and `^(pattern|deferred_by):` over `vault/wiki/insights/` with 31 lines; three lesson entries, each with one line in the brief, each joined to a live Insight; no new Insight created; 6 entries added, each with `librarian: synthesis` (3 Insight updates with `children`, 2 of them `status: open`; 3 lesson updates with `status: clustered`); the report names the three Insight pages opened to judge a shared cause, with the outcome; no read of another session's yaml or of a page under `vault/archive/` was made for the synthesis.
- `estimate-ask-query-before-a-create` — pending — `rule-ask` stands `draft` — read: by hand at the `/hi` of a later session, a `case-guppi` that built a `create` without a `ref` (method).
- `estimate-case-build-writes-the-case` — pending — `rule-case-build` stands `draft` — read: by hand, live dispatches in a session after the render (method).
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page` — pending — `rule-case-check` stands `draft` — read: pytest `-k backlog`, then the first answer of `case-guppi` on a backlog item (method).
- `estimate-case-check-sends-back-a-faulty-case` — pending — `rule-case-check` stands `draft` — read: pytest `-k subagent`, then by hand a file the hook sends back (method); put off by case 659.
- `estimate-case-check-shows-only-the-checked-case` — pending — `rule-case-check` stands `draft` — read: pytest `-k stop`, then the first reply the hook refuses (method).
- `estimate-spec-write-answers-a-refusal` — pending — `rule-spec-write` stands `draft` — read: pytest `-k answers_a_refusal`; by hand at the `/hi` of a later session (method).
- `estimate-spec-write-reaches-the-approved-spec` — pending — `rule-spec-write` stands `draft` — read: pytest `-k approved_spec`; by hand, a Case ratified in Work Mode (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `guppi render --check`; by hand, a session that takes a conserved Spec and the `/hi` after the close of a sprint (method).
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `guppi render --check`; by hand, a `/work` at the fork, one from `/box` and the `/work` of the session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method).
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `pytest tests/test_backlog.py`, and `backlog.md` after the librarian's run of the session that closes a sprint (method).
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: at the librarian's run of the session after the close of a sprint (method).
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: after the librarian's run of the session that closes a sprint (method).
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: the tree, in the Work Mode of the session that closes the sprint (method).
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint (method).
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of `migration`, in the Work Mode of the session that closes it (method).

## Flags

- `decision-case-653`: its record in the yaml is marked `incomplete: [context, problem]`; the page is superseded by 658 and 659 and archived.
- Failed Estimates: `estimate-search-leaves-out-decisions-in-every-agent`, `estimate-orchestration-shows-the-built-case`, `estimate-case-protocol-case-form`, `estimate-prespec-confirms-the-findings-once`, `estimate-case-build-checks-the-finished-case`.
- Not applied: L21, L22, L23 (the three updates of 653.1 and 653.2) and L29 (defer 658), each `superseded_by: '659'`.
- Synthesis: `insight-workflow-case-schema-silent-on-what-the-scripts-accept` was `open` on disk at the synthesis and is set `actioned` by 651.3 of this run; `lesson-orchestration-defer-acknowledged-without-its-short-form` joined it with no status change, and the cascade archived the lesson in the same run. The rule of synthesis does not say whether an Insight that a Case of the same run sets `actioned` counts as `actioned` for a lesson that joins it.
- Synthesis: two Insights closed by cases 360 and 458 are reopened by this run (`insight-harness-one-rule-implemented-twice-drifts`, `insight-case-show-built-case-retyped-by-hand`); both stand `open` with their old `addressed_by`.
- Contradiction (handoff Observations): the Spec hook removes a parent with its sub-cases on `{supersedes:case N}`, while `prespec.superseded_in_window` and `materialize.mark_superseded` mark only the number named.
- Handoff Observations: at the `/pre-spec` of 1343 ask-guppi runs broke `.claude/rules/search-leaves-out-decisions.md` and the 651 run searched the archive by a wildcard; no finding rested on it.
- Stale defers, from lint: `rule-subagent-guppi` deferred 31 times since case 29; `backlog.md`: `rule-work-mode` put off in 30 sessions, `rule-spec-box` in 6.
- The unticked `> - [ ]` lines 1319–1367 of spec.md 0311 stand inside a quote, the example of case 646; they are not tasks.
- MOC candidates: none found by this run.
- `make lint`: exit 2 — 36 lines: 5 `deferred` (`rule-complaint-becomes-a-lesson`, `rule-ledger-line-withdrawn-on-re-ratification`, `rule-morph`, `rule-prespec-judges-the-spec-whole`, `rule-subagent-guppi`), 31 `unread` (the 31 Estimates of Readings due); the handoff baseline was 5 `deferred`, 43 `unread`.
- Read outside the job: the 0311 `materialize.yaml`, the lines of its entry and record of case 649 (grep, and `git diff` of the file), for the handoff check of what `{supersedes:case 649}` of 655 clears; the handoff asked for the check.

## Next session

Cases
- One judgment of a `{supersedes:case N}` on a Case with sub-cases, for the Spec hook, `prespec` and `materialize` (handoff, For the next session).
- Remove the skips of `tests/test_orchestration.py` once its two Estimates pass (handoff, For the next session).
- `estimate-case-protocol-case-form` failed: whether `case-guppi` changes or the Criterion accepts a pair such as a module and its test on one line (handoff).
- `estimate-prespec-confirms-the-findings-once` failed: the confirmation of ask-guppi exceeds three sentences (handoff).
- `estimate-orchestration-shows-the-built-case` failed: the heading of a top-level Case whose summary carries no line for it (handoff).
- `estimate-search-leaves-out-decisions-in-every-agent` failed (L10) (handoff).
- `estimate-case-build-checks-the-finished-case` failed, put off by case 657.
- C1 and C2 of the sprint were left for a later session (handoff).
- Whether a lesson that joins an Insight set `actioned` by a Case of the same run reopens it (`lesson-orchestration-defer-acknowledged-without-its-short-form`, this librarian run).

Work
- read `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`
- read `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
- read `estimate-orchestration-showing-example-passes-the-check`
- read `estimate-orchestration-defer-example-passes-the-hook`
- read `estimate-case-protocol-example-passes-the-check`
- read `estimate-ask-searches-at-prespec`
- read `estimate-synthesis-clusters`
- read `estimate-ask-query-before-a-create`
- read `estimate-case-build-writes-the-case`
- read `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
- read `estimate-case-check-sends-back-a-faulty-case`
- read `estimate-case-check-shows-only-the-checked-case`
- read `estimate-spec-write-answers-a-refusal`
- read `estimate-spec-write-reaches-the-approved-spec`
- read `estimate-hi-takes-a-conserved-spec`
- read `estimate-hi-writes-frontier`
- read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- read `estimate-brief-written`
- read `estimate-backlog-renders`
- read `estimate-sprint-close-next-session-opens-the-sprint`
- read `estimate-sprint-close-runs-in-the-librarian-run`
- read `estimate-sprint-close-takes-the-readings-in-groups`
- read `estimate-sprint-migration-leftovers-gone`
- read `estimate-sprint-migration-lint-clean`
- read `estimate-sprint-migration-merges`
- ledger L21, L22, L23 and L29 of 1343 not applied: superseded by case 659.

Ask the person
- `estimate-permissions` — needs the person — in the session after the render of `.claude/settings.json`, did a Read, Grep or Glob of `case-guppi` under `~/.claude/projects/c--PROJECTS-GUPPI/` still ask for permission?

## Readings at the close

- `make test`: 1207 passed, 6 skipped.
- `make lint`: exit 2, 5 `deferred`, 31 `unread`.
- Live pages: rules 79, estimates 217, lessons 78, insights 30, decisions 1126, entities 4; `vault/archive/`: 849 `.md` files.
