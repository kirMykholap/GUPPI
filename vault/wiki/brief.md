# Brief — 2026-10-31, librarian of session 1831

## Where things stand

- Session 1831 of the sprint `plugin`. Cases ratified: 966, 967 (967.1, 967.2, 967.3), 968, 969 (969.1, 969.2, 969.3), 970 (970.1, 970.2, 970.3) and the short-form defer 971. Cases 967, 968 and 969 were built again on the findings of `/pre-spec` and ratified again (handoff).
- Code: `.guppi/guppi/links.py` (new: `guppi links <slug or path>` and `guppi links --write`), `cli.py`, `pages.py`, `.guppi/.gitignore` (`links.md`), `materialize.py` (`schema_values`, `is_allowed`, `typed_value`), `ratified.py`, `prespec.py` (`core_as_left`), `lint.py`, `ship.py` (`.guppi/links.md` in `LEFT_OUT`). Tests: `test_links.py` (new, 13), `test_materialize.py` (6 new), `test_lint.py` (2 new), `test_schemas.py` (2 new). `guppi test` 1830 passed, 6 skipped, 1 deselected at the baseline; 1851 passed, 8 skipped, 1 deselected at Retro; `guppi style` clean (handoff).
- By hand in Work Mode: the box of Case 956.3 in `vault/raw/2026-10-31/0431/spec.md` ticked (handoff).
- Readings: L1 passed (at /hi), L30 and L31 passed (at Retro). Lesson: L32 (error) (handoff).
- `guppi materialize` printed `written with 32 entries` for `vault/raw/2026-10-31/1831/materialize.yaml` and `extended with 0 entries` for the yamls of `0128` and `0431`. The ledger has 32 lines (`wc -l`); the yaml holds entries for lines 1–29, 31 and 32, and line 30 is folded into the `create` entry of line 6, so every line is accounted for. Kinds: 15 `update`, 7 `create`, 2 `delete`, 4 `defer`, 2 `estimate`, 1 `lesson`; the synthesis added 2 `update` entries, 33 in all.
- Marks: every entry `applied`; 4 `exists` (the `defer` entries of lines 26–29); 2 `librarian: synthesis`; no entry `failed`, `incomplete`, `near` or `merged`; `unparsed: []`.
- `guppi generate` printed 45 pages written or changed for `1831` and 0 for `0128` and `0431`; nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `3 page(s) moved`, nothing on stderr. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- Pages created (23), from `git status`: decisions 15 (`decision-case-966`, `967`, `967.1`, `967.2`, `967.3`, `968`, `969`, `969.1`, `969.2`, `969.3`, `970`, `970.1`, `970.2`, `970.3`, `971`); entities 1 (`entity-link-graph`, `built`, `core: true`); rules 1 (`rule-link-graph-at-session-start`, `draft`, `core: true`); estimates 5 (`estimate-link-graph-prints-the-neighbours` `passed`, `estimate-case-build-reads-the-link-graph-of-what-it-changes`, `estimate-link-graph-at-session-start-writes-the-file`, `estimate-materialize-lifts-a-create-value-by-the-schema`, `estimate-case-build-runs-the-vault-query-first`, the four `pending`); lessons 1 (`lesson-case-build-names-a-file-without-the-readers-of-its-folder`, `clustered`).
- Pages updated (19), from `git status`: rules 8 (`rule-ask`, `rule-backlog`, `rule-case-build`, `rule-case-protocol`, `rule-estimates-schema`, `rule-harness`, `rule-hook-registry`, `rule-materialize`; `rule-backlog` and `rule-materialize` by the cascade and the `estimates` list); estimates 9 (`estimate-ask-query-before-a-create`, `estimate-ask-searches-at-prespec`, `estimate-case-build-reads-the-readers-of-a-changed-step`, `estimate-estimates-schema-checked`, `estimate-lint-checks-the-statuses` `passed`, and the four deferred by Case 971); entities 1 (`entity-guppi`); insights 1 (`insight-case-build-changes-a-step-without-reading-its-readers`).
- Deleted by Case 969.3 and moved by `cleanup` to `vault/archive/plugin/2026-10-31/1831/estimates/`: `estimate-backlog-keeps-the-work-taken-out-of-a-built-page` (read `passed` by line 1 before the delete) and `estimate-guppi-keeps-no-defer-of-its-shape`. `decision-case-963`, superseded by 969.1, moved to `vault/archive/plugin/2026-10-31/1831/decisions/`.
- Cascade (log): `entity-link-graph` `draft → built`, `rule-backlog` `draft → built`; `rule-estimates-schema` `built → draft`, `rule-materialize` `built → draft`.
- The handoff's instructions, checked: `entity-link-graph` (line 14) and `rule-link-graph-at-session-start` (line 15) hold `core: true` as a boolean, and the yaml loads both as `True`; the three `replace` pairs of `rule-case-build` (Cases 966, 967.2, 970.1) and the two of `rule-case-protocol` (Cases 968, 969.1) applied with no error, and each new text stands once in its page; the reading of line 1 applied before the delete of line 19; `rule-estimates-schema` left `backlog.md` and the four Estimates of Case 971 entered it (8 items to 12, the reopened Insight the twelfth); the render wrote `.claude/settings.json` (line 23 holds `guppi links --write` beside `guppi render --sync`), `.claude/agents/case-guppi.md`, `.claude/agents/ask-guppi.md`, `vault/wiki/case-schema.md` and `vault/wiki/estimates/schema.yaml` (`once` at lines 20, 25 and 57) (`git status`).
- This run ticked 34 boxes of `vault/raw/2026-10-31/1831/spec.md` and one `read` box of `vault/raw/2026-10-31/0431/spec.md` (`estimate-backlog-keeps-the-work-taken-out-of-a-built-page`) (`git diff`); 8 `read` boxes stay unticked in the 1831 Spec and 5 in the 0431 Spec.
- Index check: `entity-link-graph` compared by `^(purpose|deferred_by):` over `vault/wiki/entities/` (5 lines): no page holds the same purpose and none is near; `entity-guppi` is its parent. `rule-link-graph-at-session-start` compared by `^(purpose|deferred_by):` over `vault/wiki/rules/` (89 lines): none the same, none near; the closest, `rule-session-start` and `rule-hook-registry`, guard the state at session start and the registration of hooks.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 58 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14 lines.
  - `lesson-case-build-names-a-file-without-the-readers-of-its-folder` — joined `insight-case-build-changes-a-step-without-reading-its-readers` (now 3 children). The Insight stood `actioned` by `decision-case-924`; the lesson carries no `addressed_by`, so the Insight is `open` again with `addressed_by` kept; it stands in `backlog.md` with severity 1.

## Readings due

- `estimate-case-build-reads-each-list-of-a-new-member` — `failed`; target `rule-case-build` (`draft`); deferred by Case 971; method: at Retro, `.claude/agents/case-guppi.md` and the transcripts of the build of Case 956.1 and of the `/pre-spec` of session 0431. Result: the `case-guppi` of Case 956.1 ran no search for a hook already in the list and missed the docstring list of `.guppi/guppi/cli.py`.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `failed`; target `rule-orchestration` (`draft`); deferred by Case 971; method: at Retro, the dispatch of Case 961 in the transcript of session 0431. Result: the dispatch named Case 960 by id and path, but its sentence named only its new Estimate and not the pages it changes.
- `estimate-orchestration-shows-the-built-case` — `failed`; target `rule-orchestration` (`draft`); deferred by Case 971; method: at Retro, `vault/wiki/orchestration.md` and the showing of Cases 960 and 956 in the transcript of session 0431. Result: the answer of the `case-guppi` of 956 put `**Built:**` on its fourth line and the main agent showed it as a built Case.
- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); read: `- [ ] read` line 651 of `vault/raw/2026-10-31/1831/spec.md`; method: after the first build of `case-guppi` whose Case proposes a `create` without a `ref` on the new Render of `rule-ask`.
- `estimate-ask-searches-at-prespec` — `pending`; target `rule-ask` (`draft`); read: line 686 of the 1831 Spec; method: after the first `/pre-spec` whose `ask-guppi` runs on the new Render of `rule-ask`.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes a reader and the text it reads.
- `estimate-case-build-reads-the-link-graph-of-what-it-changes` — `pending`; target `rule-case-build` (`draft`); read: line 220 of the 1831 Spec; method: after the `/pre-spec` of the first session on the Render that holds the sentence on `.guppi/links.md` and whose start wrote that file.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — `pending`; target `rule-case-build` (`draft`); read: line 57 of the 1831 Spec; method: after the `/pre-spec` of the first session on the Render that follows a step to the one who carries it out.
- `estimate-case-build-runs-the-vault-query-first` — `pending`; target `rule-case-build` (`draft`); read: line 606 of the 1831 Spec; method: after the first build on the new Render whose Case proposes a `create` without a `ref`.
- `estimate-close-commits` — `pending`; target `rule-close` (`draft`); method: `pytest .guppi/tests/test_render.py -k paths`; by hand, after a librarian's run whose frame holds the Render of `rule-close`: `git log` and `git status`. This run: the commit is made at the close, after this brief; `guppi render --paths` printed 32 paths.
- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); deferred by Case 971; method: after the librarian's run of a session that starts with the hook of `rule-librarian-report-copy`: `report.md` of the session folder beside the librarian's last output. This run: no `report.md` stands in `vault/raw/2026-10-31/1831/` while this brief is written.
- `estimate-estimates-schema-checked` — `pending`; target `rule-estimates-schema` (`draft`); read: line 465 of the 1831 Spec; method: after the librarian's run that renders `vault/wiki/estimates/schema.yaml` with `once`: `pytest .guppi/tests/test_schemas.py -k estimate` and `guppi check`. This run: the render wrote the file with `once` at lines 20, 25 and 57; `guppi check` printed 18 lines, none a `schema` finding; `guppi test` printed 1853 passed, 6 skipped, 1 deselected.
- `estimate-handoff-dispatches` — `pending`; target `rule-handoff` (`draft`); read: `- [ ] read` line 136 of `vault/raw/2026-10-31/0431/spec.md`; method: after a `/handoff` whose skill commits `report.md`: the event log, `handoff.md`, `git log` and the transcript of that session.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint.
- `estimate-link-graph-at-session-start-writes-the-file` — `pending`; target `rule-link-graph-at-session-start` (`draft`); read: line 297 of the 1831 Spec; method: `pytest .guppi/tests/test_links.py`; and by hand, after the first session start whose `.claude/settings.json` holds the hook.
- `estimate-materialize-lifts-a-create-value-by-the-schema` — `pending`; target `rule-materialize` (`draft`); read: line 375 of the 1831 Spec; method: `pytest .guppi/tests/test_materialize.py`; by hand, after the first librarian's run that creates a page whose `create` writes `core` as `true`: the `core` field of that page and `guppi lint`. This run: `entity-link-graph` line 14 and `rule-link-graph-at-session-start` line 15 read `core: true`, both loaded as the boolean `True` from the yaml; `guppi check` printed 18 lines, none a `schema` finding, one `rules/rule-link-graph-at-session-start: status: a page with core: true that is draft`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph`.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch of items taken up together under the new Render in which a summary carries a line `Other Case`.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`; target `rule-plugin-install` (`draft`); deferred; method: by hand, three projects with `/guppi:install` from a local clean version.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); read: line 629 of the 0431 Spec; method: after a lesson line that declares a new tag by a `newtag` block.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-spec-box-runs-a-conserved-spec` — `pending`; target `rule-spec-box` (`draft`); read: line 184 of the 0431 Spec; method: `guppi render --check`; by hand, after a session that runs a conserved Spec by `/box`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); method: `pytest .guppi/tests/test_ship.py`; by hand, after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z`, before the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: in a session of the sprint `plugin` before its close, the clean version installed in an empty project.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); method: a pull request from a second account read on GitHub, before the close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer on `README.md` at the `/hi` after the session that writes it, before the close.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); method: after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: the lesson of line 32 carries no `addressed_by`; it joined `insight-case-build-changes-a-step-without-reading-its-readers`, which stood `actioned` and is `open` now.

## Flags

- Entries marked `incomplete`, `failed`, `near` or `unparsed`: none.
- Failed Estimates: 3 — `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-orchestration-shows-the-built-case`, all three deferred by Case 971.
- `guppi check` printed 18 lines (16 before the work, per the handoff): 13 `status: a page with core: true that is draft` (`rule-ask`, `rule-case-build`, `rule-close`, `rule-estimates-schema`, `rule-handoff`, `rule-link-graph-at-session-start`, `rule-materialize`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-spec-box`, `rule-synthesis`); 3 `unread: failed` (the three above); 1 `unread: pending` (`estimate-link-graph-at-session-start-writes-the-file`); 1 `ref` (`estimates/estimate-link-graph-prints-the-neighbours: ref: body names slug, which no live or archived page carries`).
- `estimate-link-graph-prints-the-neighbours`, created this run: lint reads the word `slug` of its Criterion (the code spans `[[slug]]` and `## <slug or path>`) as a slug of a page.
- `estimate-link-graph-at-session-start-writes-the-file`, created this run: the by-hand part of its `method` opens with `and by hand, after`, not `by hand, after`, so lint reads it as a reading that does not wait, `unread: pending`.
- Defers in `backlog.md` put off in 2 or more sessions: `rule-ratification` (2), `estimate-orchestration-shows-the-built-case` (3).
- MOC candidates: none seen. Contradictions: none seen.
- Reads outside what the frame says the job needs: none.

## Next session

### Cases

- C1, the clean branch: push `plugin` and a tag `prod-x.y.z` on its last commit, and read the CI run by its Estimate (handoff, For the next session).
- Whether the Enforcement sentence of the rules schema should name a hook that writes a file, such as `rule-librarian-report-copy` and `rule-link-graph-at-session-start`, which refuse nothing (Case 967.3) (handoff, For the next session).
- Whether `case-guppi` reads, for a new generated file, the readers of its folder, such as the tree walk of `guppi ship` (L32); its lesson reopened `insight-case-build-changes-a-step-without-reading-its-readers` (handoff, For the next session).
- `estimate-handoff-dispatches`, read against its Criterion from the transcript of session 0431 (handoff, For the next session).
- `estimate-case-build-reads-each-list-of-a-new-member` — `failed`, deferred by Case 971, stands in `backlog.md`.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `failed`, deferred by Case 971, stands in `backlog.md`.
- `estimate-orchestration-shows-the-built-case` — `failed`, deferred by Case 971, stands in `backlog.md`.
- Defect: lint reads the word `slug` in the code span `[[slug]]` of the Criterion of `estimate-link-graph-prints-the-neighbours` as a link to a page (`guppi check`, `ref` finding).
- Defect: the `method` of `estimate-link-graph-at-session-start-writes-the-file` writes `and by hand, after`, which the wait predicate of lint does not read as a wait (`guppi check`, `unread: pending`).
- `estimate-link-graph-at-session-start-writes-the-file` — defer into `backlog.md`, since its session did not take its reading (the first session start whose `.claude/settings.json` holds the hook) (handoff, Debt).

### Work

- `estimate-close-commits` — read; its `read` box, line 219 of `vault/raw/2026-10-31/0431/spec.md`.
- `estimate-estimates-schema-checked` — read; its `read` box, line 465 of `vault/raw/2026-10-31/1831/spec.md`.
- `estimate-materialize-lifts-a-create-value-by-the-schema` — read; its `read` box, line 375 of `vault/raw/2026-10-31/1831/spec.md`.

### Ask the person

none

## Readings at the close

- `uv run --project .guppi guppi test`: 1853 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: 18 lines, exit 1 (above).
- Live pages: decisions 459, entities 6, estimates 339, insights 13, lessons 59, rules 88.
