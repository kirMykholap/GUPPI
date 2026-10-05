# Brief — 2026-10-05, after the librarian run of session 1616

## Where things stand

- Session 1616 ratified Cases 660 (660.1–660.4), 661 (661.1, 661.2), 662 (662.1–662.3), 664 (664.1–664.3) and 668, and the defers 665, 666 and 667; Case 663 was superseded by 668 (`{supersedes:case 663}`).
- Code: `guppi/materialize.py` (`in_family`, `mark_superseded`, `refold`), `guppi/prespec.py` (`retired_by`), `guppi/ratified.py` and `guppi/casecheck.py` import `in_family`; `guppi/generate.py` (`supersede_children`); `guppi/casecheck.py` (`summary_findings`, `top_heading`, `summary_names`); `guppi/grepguard.py` new, `guppi/cli.py`. Tests: `tests/test_grepguard.py` new (15), `tests/test_casecheck.py` (`-k summary_names_the_case`, 10), `tests/test_orchestration.py` (one new test), `tests/test_prespec.py`, `tests/test_materialize.py`, `tests/test_generate.py`. Handoff: `make test` 1244 passed, 6 skipped; `make style` clean.
- Readings: L1–L6 at `/hi`, the Work reading L40; lessons L41–L43.
- The yaml: 48 entries (43 from the ledger, 5 of the synthesis); 44 applied; 4 not applied, superseded by case 668 (L25, L26, L27, L36); 0 failed; `incomplete: [criterion]` on L25 and L36, both superseded; `exists` on the three defers (L33–L35); `unparsed: []`.
- Pages created: decisions 21 (20 live; `decision-case-663` superseded by 668 and archived); estimates 4 (`estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`, `estimate-case-check-sends-back-a-summary-without-the-case-name`, `estimate-search-leaves-out-decisions-by-the-grep-hook`, `estimate-synthesis-reads-the-status-its-yaml-sets`); lessons 3; insights 1 (`insight-ledger-ratified-line-never-withdrawn`, synthesis, `severity: 2`).
- Pages updated: estimates 16 (7 readings, 9 Criteria replaced by 660.1–660.3, 661.1, 661.2, 662.1, 662.2, 664.2, 664.3, and the defers 665–667); rules 11 (10 by decisions: `rule-page-generation`, `rule-decisions-schema`, `rule-retro`, `rule-handoff`, `rule-case-build`, `rule-orchestration`, `rule-case-check`, `rule-search-leaves-out-decisions`, `rule-hook-registry`, `rule-synthesis`; `rule-materialize` by the cascade alone; `rule-materialize`, `rule-page-generation` and `rule-retro` set `built → draft` by the cascade); entities 1 (`entity-glossary`, three updates 660.2, 660.3, 668, on three rows); insights 1 (synthesis; `severity` 1 → 2 by `generate`); lessons 1 existing (synthesis), and two of the new lessons clustered in the same run.
- Pages archived by `generate` and `cleanup`: 1 — `decision-case-663` (superseded), under `vault/archive/migration/2026-10-05/1616/decisions/`.
- `guppi materialize` wrote `superseded_by: decision-case-658` beside `decision-case-659` into the `decisions` records 653.1 and 653.2 of `raw/2026-10-05/1343/materialize.yaml` (the family reading of 660.2); it added 0 entries to the yamls of 0109, 0311 and 1343.
- The handoff checks: L25–L27 and L36 carry `superseded_by: '668'` and were not applied; `estimate-synthesis-reads-the-status-the-run-sets` has no page; the three updates of `entity-glossary` replace text on three different rows (the rows `supersedes`, Decision (status), Insight (status)); after the render `.claude/settings.json` registers `uv run guppi grepguard` on `PreToolUse` of `Grep`, `.claude/agents/case-guppi.md` asks for the `**Case:**` line, and `uv run pytest tests/test_orchestration.py` gave 6 passed, none skipped.
- The render wrote `.claude/agents/case-guppi.md`, `.claude/agents/librarian-guppi.md`, `.claude/rules/search-leaves-out-decisions.md`, `.claude/settings.json`, `.claude/skills/handoff/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/orchestration.md` and `vault/wiki/decisions/schema.yaml`. The scripts ticked 37 boxes of the 1616 Spec, 2 `read` lines of the 0311 Spec and 6 of the 1343 Spec; 13 `read` lines of the 1616 Spec stay open. `guppi sprint` left `sprint.md` unchanged; `guppi backlog` and `guppi glossary` rewrote their files; no stderr from any script.
- `guppi archive` printed nothing on stdout or stderr and moved no unit: the four units with a ledger (0109, 0311, 1343, 1616) are dated 2026-10-05, the day of the run, which it does not look at; the earlier dates of `vault/raw/` hold only `event_log.md`.

Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 78 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 31 lines.
- `lesson-case-build-renamed-a-slug-of-a-ratified-case-under-its-old-number` joined `lesson-ledger-a-dropped-item-needs-a-superseding-sub-case` under the new `insight-ledger-ratified-line-never-withdrawn` (`open`; no `addressed_by` on the lesson entry).
- `lesson-orchestration-heading-of-a-showing-composed-by-the-main-agent` joined `insight-case-show-built-case-retyped-by-hand` (`open` on disk, no decision entry of this yaml sets it `actioned`; the update carries `children` only; the lesson entry's `addressed_by: decision-case-662.2` is not written to the Insight).
- `lesson-ask-search-exclusion-of-decisions-left-to-each-agent` — none: no index line holds a rule of the Grep exclusion applied by hand per call or the order of a glob; the Insights on rules no script reads speak of the chat form of a Case and of the reply language. It stays `new`.

## Readings due

Failed:
- `estimate-case-build-checks-the-finished-case` — failed — `rule-case-build` stands `draft` — result: the four ask-guppi runs at the `/pre-spec` of 0109 found pages, rules and a lesson the Cases 638–641 missed; put off by case 667 — read: by hand at `/pre-spec` of a later session after the render (method).
- `estimate-case-protocol-case-form` — failed — `rule-case-protocol` stands `draft` — result: L38 of 1343, `given` with two things on a line (650.1, 650.2, 653.1, 654) and with state (656, 653.1); put off by case 665 — read: by hand, the Cases of a session at its close (method).
- `estimate-prespec-confirms-the-findings-once` — failed — `rule-prespec` stands `draft` — result: L41 of 1343, four sentences under one finding in the confirmation runs; put off by case 666 — read: by hand at the `/pre-spec` of a later session whose findings send a Case back (method).

Pending:
- `estimate-prespec-catches-a-superseded-case` — pending — `rule-prespec` stands `draft` — read: `- [ ] read` line of the 1616 Spec; pytest `tests/test_prespec.py`, live at the first `/pre-spec` of a later session whose window holds a supersedes (method).
- `estimate-materialize-marks-superseded` — pending — `rule-materialize` stands `draft` — read: `- [ ] read` line of the 1616 Spec; pytest `tests/test_materialize.py` plus one live reading of a librarian's run (method). This run: `guppi materialize` exit 0; L25, L26, L27 and L36 (case 663) carry `superseded_by: '668'`, L37–L39 carry `supersedes: ['663']`; the `decisions` record 663 carries `superseded_by: [decision-case-668]`; the records 653.1 and 653.2 of the 1343 yaml got `decision-case-658` beside `decision-case-659`; the lesson and estimate entries carry no mark.
- `estimate-generate-writes-the-decision-page` — pending — `rule-page-generation` stands `draft` — read: `- [ ] read` line of the 1616 Spec; pytest `tests/test_generate.py`, the live reading in the librarian's run (method). This run: `guppi generate` exit 0, 59 pages written or changed in 1616; 21 Decision pages created (parents 660, 661, 662, 664 and their sub-cases, 663, 665–668); `decision-case-663` set superseded by `decision-case-668`, archived by the cascade and moved by `cleanup`; 663 has no `children`; no other Decision page changed.
- `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` — pending — `rule-retro` stands `draft` — read: `- [ ] read` line of the 1616 Spec; by hand at a `/retro` whose ledger holds a supersedes on a Case with sub-cases (method).
- `estimate-orchestration-showing-example-passes-the-check` — pending — `rule-orchestration` stands `draft` — read: `- [ ] read` line of the 1616 Spec, at the `/hi` of a later session.
- `estimate-orchestration-defer-example-passes-the-hook` — pending — `rule-orchestration` stands `draft` — read: `- [ ] read` line of the 1616 Spec, at the `/hi` of a later session.
- `estimate-case-build-writes-the-case` — pending — `rule-case-build` stands `draft` — read: `- [ ] read` line of the 1616 Spec, by hand in a later session after the render; also open in the 0311 Spec.
- `estimate-orchestration-shows-the-built-case` — pending — `rule-orchestration` stands `draft` — read: `- [ ] read` line of the 1616 Spec, by hand at the close of a later session after the render.
- `estimate-case-check-sends-back-a-summary-without-the-case-name` — pending — `rule-case-check` stands `draft` — read: `- [ ] read` line of the 1616 Spec, at the `/hi` of a later session.
- `estimate-search-leaves-out-decisions-by-the-grep-hook` — pending — `rule-search-leaves-out-decisions` stands `draft` — read: `- [ ] read` line of the 1616 Spec; `uv run pytest tests/test_grepguard.py`, then a Grep over `vault/wiki/` in the main agent and in a subagent at the `/hi` of a later session (method).
- `estimate-search-leaves-out-decisions-in-every-agent` — pending — `rule-search-leaves-out-decisions` stands `draft` — read: `- [ ] read` line of the 1616 Spec; by hand at the `/hi` of a later session (method).
- `estimate-ask-searches-at-prespec` — pending — `rule-ask` stands `draft` — read: `- [ ] read` line of the 1616 Spec; by hand at the `/hi` of a later session (method). Its L4 reading failed before 664.3 replaced its Criterion.
- `estimate-synthesis-reads-the-status-its-yaml-sets` — pending — `rule-synthesis` stands `draft` — read: `- [ ] read` line of the 1616 Spec; by hand after a librarian run in which a lesson joins an Insight that a decision entry of the same yaml sets `actioned` (method). This run: no decision entry of the 1616 yaml sets an Insight `actioned`; L42 joined `insight-case-show-built-case-retyped-by-hand`, `open` on disk, by an update with `children` only; the Insight stands `open` and the lesson `clustered` after `generate`.
- `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` — pending — `rule-spec-reconcile` stands `draft` — read: `- [ ] read` line of the 1343 Spec; `uv run pytest tests/test_ratified.py -k number_held`, and by hand the store entry the first Write of a live `case-guppi` leaves (method).
- `estimate-spec-write-reaches-the-approved-spec` — pending — `rule-spec-write` stands `draft` — read: `- [ ] read` line of the 0311 Spec; pytest `-k approved_spec`, by hand a Case ratified in Work Mode (method).
- `estimate-case-check-sends-back-a-faulty-case` — pending — `rule-case-check` stands `draft` — read: `- [ ] read` line of the 0311 Spec; pytest `-k subagent`, by hand a file sent back, fixed by Edit and passed, and a live round after a built Case (method).
- `estimate-case-check-shows-only-the-checked-case` — pending — `rule-case-check` stands `draft` — read: `- [ ] read` line of the 0311 Spec; pytest `-k stop`, by hand the first reply the hook refuses (method).
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page` — pending — `rule-case-check` stands `draft` — read: `- [ ] read` line of the 0311 Spec; pytest `-k backlog`, by hand the first answer on an item taken from the backlog (method).
- `estimate-permissions` — pending — `rule-permissions` stands `draft` — read: `- [ ] read` lines of the 0311 and 1343 Specs; the person's word on the client's prompt (method).
- `estimate-ask-query-before-a-create` — pending — `rule-ask` stands `draft` — read: by hand at the `/hi` of a later session, a `case-guppi` that built a `create` without a `ref` (method).
- `estimate-hi-writes-frontier` — pending — `rule-skill-hi` stands `draft` — read: by hand at the `/hi` of the session after the close of a sprint (method).
- `estimate-hi-takes-a-conserved-spec` — pending — `rule-skill-hi` stands `draft` — read: `uv run guppi render --check`; by hand, a session that takes a conserved Spec, and the `/hi` after the close of a sprint (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — pending — `rule-work-mode` stands `draft` — read: `uv run guppi render --check`; by hand, a `/work` at the fork, one that `/box` calls and the `/work` of a session that closes a sprint (method).
- `estimate-brief-written` — pending — `rule-brief` stands `draft` — read: by hand at the `/hi` after the librarian's run of the session that closes a sprint (method). This run closed no sprint: no line of the 1616 Spec holds `guppi sprint-close`.
- `estimate-backlog-renders` — pending — `rule-backlog` stands `draft` — read: `uv run pytest tests/test_backlog.py`, plus `vault/wiki/backlog.md` after the librarian's run of the session that closes a sprint (method). This run: `guppi backlog` exit 0, no stderr, `backlog.md` rewritten; no sprint closed.
- `estimate-sprint-close-runs-in-the-librarian-run` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_sprint_close.py -k tick`; by hand after the librarian's run of the session that closes a sprint (method). This run: no `guppi sprint-close` line in the 1616 Spec, none run.
- `estimate-sprint-close-next-session-opens-the-sprint` — pending — `rule-sprint-close` stands `draft` — read: pytest `tests/test_ledger.py -k sprint` and `tests/test_materialize.py -k sprint`; by hand at the librarian's run of the session after the close of a sprint (method). This run: the yaml's `sprint` is `migration`; `guppi sprint` exit 0, no stderr.
- `estimate-sprint-close-takes-the-readings-in-groups` — pending — `rule-sprint-close` stands `draft` — read: by hand after the Work Mode of the session that closes a sprint (method).
- `estimate-sprint-migration-leftovers-gone` — pending — `entity-sprint-migration` stands `draft` — read: by hand in the Work Mode of the session that closes the sprint, before the librarian's run (method).
- `estimate-sprint-migration-lint-clean` — pending — `entity-sprint-migration` stands `draft` — read: `make lint` in the Work Mode of the session that closes the sprint, before the librarian's run (method).
- `estimate-sprint-migration-merges` — pending — `entity-sprint-migration` stands `draft` — read: `make test` on the last commit of migration, in the Work Mode of the session that closes it (method).

## Flags

- `incomplete: [criterion]` on L25 (`estimate-synthesis-reads-the-status-the-run-sets`) and L36 (`estimate-synthesis-reads-the-status-its-yaml-sets`, case 663); both carry `superseded_by: '668'` and were not applied; L37 of case 668 created the page whole.
- No entry marked `failed` or `near`; `unparsed: []`.
- Failed Estimates: `estimate-case-build-checks-the-finished-case`, `estimate-case-protocol-case-form`, `estimate-prespec-confirms-the-findings-once` (put off by 667, 665, 666).
- Stale defers, from the lint: `rule-subagent-guppi` deferred 31 times since case 29; `rule-complaint-becomes-a-lesson` (since case 504), `rule-ledger-line-withdrawn-on-re-ratification` (since case 594), `rule-morph` (since case 239), `rule-prespec-judges-the-spec-whole` (since case 643), 1 time each.
- MOC candidates: none found. Contradictions: none found.
- The lint: 39 lines — 5 `deferred`, 34 `unread` (31 pending, 3 failed); no other finding; `make lint` exits red.
- Handoff, Notes from memory: the person did not see the defers 665, 666 and 667 before they were written; the person's "Идём работать" was taken as the close of Plan Mode.
- Handoff, Observations: `supersede_children` of `generate` finds a child page only when it stands; an order where the superseding record comes before the parent's page is not covered by a test.
- Handoff, Observations: `estimate-ask-searches-at-prespec` failed at L4, and 664.3 then replaced its Criterion and set it `pending`; the failure stands in the ledger before the update.

## Next session

Cases:
- `estimate-ask-searches-at-prespec` failed (L4): in two of three ask-guppi runs a Read came between the rules Grep and the Greps of the other categories — whether the frame of `ask-guppi` or the Criterion changes (handoff, For the next session).
- A renamed or dropped target of a ratified Case needs a new number, and no check says so before the Spec hook; `rule-ledger-line-withdrawn-on-re-ratification` stands in the backlog, and `insight-ledger-ratified-line-never-withdrawn` is open on the same cause (handoff, For the next session).
- C1 and C2 of the sprint were left for a later session (handoff, For the next session).
- `estimate-case-build-checks-the-finished-case` failed, put off by 667 (and earlier by 647, 657).
- `estimate-case-protocol-case-form` failed, put off by 665.
- `estimate-prespec-confirms-the-findings-once` failed, put off by 666.

Work:
- `estimate-prespec-catches-a-superseded-case`
- `estimate-materialize-marks-superseded`
- `estimate-generate-writes-the-decision-page`
- `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`
- `estimate-orchestration-showing-example-passes-the-check`
- `estimate-orchestration-defer-example-passes-the-hook`
- `estimate-case-build-writes-the-case`
- `estimate-orchestration-shows-the-built-case`
- `estimate-case-check-sends-back-a-summary-without-the-case-name`
- `estimate-search-leaves-out-decisions-by-the-grep-hook`
- `estimate-search-leaves-out-decisions-in-every-agent`
- `estimate-ask-searches-at-prespec`
- `estimate-synthesis-reads-the-status-its-yaml-sets`
- `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
- `estimate-ask-query-before-a-create`
- `estimate-hi-writes-frontier`
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
- Ledger lines this run did not apply: L25, L26, L27 and L36 of the 1616 ledger (case 663), superseded by case 668; the ledger holds 43 lines and the yaml an entry for each.

Ask the person:
- `estimate-permissions` — needs the person — in a session after the render of `.claude/settings.json`, did a Read, Grep or Glob of `case-guppi` under `~/.claude/projects/c--PROJECTS-GUPPI/` ask for permission? (No `case-guppi` of session 1616 made such a call.)

## Readings at the close

- `make test`: 1244 passed, 6 skipped.
- `make lint`: 39 lines — 5 `deferred`, 34 `unread`; red.
- Pages: decisions 1146, estimates 221, rules 79, lessons 81, insights 31, entities 4; `vault/archive/` 850 pages.
