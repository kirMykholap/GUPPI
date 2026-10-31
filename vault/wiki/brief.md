# Brief — 2026-10-31, librarian of session 2307

## Where things stand

- Session 2307 of the sprint `plugin`. Cases ratified: 972, 973, 974, 975 and the short-form defer 976. Cases 972–975 were built again on the findings of `/pre-spec` and ratified again (handoff).
- Code: `.guppi/guppi/lint.py` (`names_its_event_inside_a_part`), `.guppi/guppi/prespec.py` (`kept_method`, `wait_form_notes`, `OFF_FORM_WAIT`, the module docstring; `kept_method_waits` reads by `kept_method`). Tests: `test_lint.py` (1 new), `test_prespec.py` (2 new). `guppi test` 1853 passed, 6 skipped, 1 deselected at the baseline; 1856 passed, 6 skipped, 1 deselected at Retro; `guppi style` clean (handoff).
- Readings: L1, L2, L3 passed (at `/hi`), L4 passed (in Plan Mode), L18 `estimate-prespec-hook-reports-a-wait-off-its-form` passed (at Retro). Lessons: L19 and L20 (error) (handoff).
- `guppi materialize` printed `written with 20 entries` for `vault/raw/2026-10-31/2307/materialize.yaml` and `extended with 0 entries` for the yamls of `0128`, `0431` and `1831`. The ledger has 20 lines (`wc -l`); the yaml holds entries for lines 1–17, 19 and 20, and line 18 is folded into the `create` entry of line 5, so every line is accounted for. Kinds: 4 `estimate`, 3 `create`, 6 `update`, 4 `defer`, 2 `lesson`, 19 in all; the index check and the synthesis added none.
- Marks: all 19 entries `applied`; 4 `exists` (the `defer` entries of lines 14–17); no entry `failed`, `incomplete`, `near`, `librarian` or `merged`; `unparsed: []`.
- `guppi generate` printed 30 pages written or changed for `2307` and 0 for `0128`, `0431` and `1831`; nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `1 page(s) moved`, nothing on stderr. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- Pages created (10), from `git status`: decisions 5 (`decision-case-972` to `decision-case-976`); estimates 3 (`estimate-prespec-hook-reports-a-wait-off-its-form` `passed`, `estimate-sprint-plugin-check-finds-no-bare-slug-link` `pending`, `estimate-case-build-reads-the-readers-of-a-new-files-folder` `pending`); lessons 2 (`lesson-ledger-reading-writes-a-bare-wikilink`, `lesson-orchestration-shows-a-round-after-own-text`, both `new`).
- Pages updated (19), from `git status`: estimates 10 (`estimate-close-commits`, `estimate-estimates-schema-checked`, `estimate-materialize-lifts-a-create-value-by-the-schema`, `estimate-link-graph-at-session-start-writes-the-file`, each `pending → passed`; `estimate-link-graph-prints-the-neighbours`; `estimate-rules-schema-checked`, `pending`; the four deferred by Case 976); rules 6 (`rule-case-build`, `rule-rules-schema` by Cases; `rule-prespec-hook` by its `estimates` list; `rule-estimates-schema`, `rule-link-graph-at-session-start`, `rule-materialize` by the cascade); entities 2 (`entity-glossary`; `entity-sprint-plugin` by its `estimates` list); insights 1 (`insight-case-build-changes-a-step-without-reading-its-readers`, `actioned`, severity 0).
- Archived: `lesson-case-build-names-a-file-without-the-readers-of-its-folder`, moved by `cleanup` to `vault/archive/plugin/2026-11-01/2307/lessons/` after its Insight went `actioned` (log: `archived · insight actioned`).
- Cascade (log): `rule-estimates-schema`, `rule-link-graph-at-session-start` and `rule-materialize` `draft → built`; `rule-rules-schema` `built → draft`.
- Written by the scripts (`git status`): `.claude/agents/case-guppi.md` and `vault/wiki/rules/schema.yaml` (render), `vault/wiki/glossary.md` (glossary), `vault/wiki/sprint.md` (one new line, the reading of `estimate-sprint-plugin-check-finds-no-bare-slug-link`), `vault/wiki/backlog.md` (12 items; `estimate-handoff-dispatches` entered; `insight-case-build-changes-a-step-without-reading-its-readers` left).
- The handoff's instructions, checked by `git diff` and Grep: Case 973 changed the `## Result` of `estimate-link-graph-prints-the-neighbours` and added one History line, no field and no `## Criterion`; its `[[slug]]` stands in a code span. Case 974: the Insight is `actioned` with `addressed_by: "[[decision-case-974]]"`, and its lesson moved to the archive. Case 975: the two new texts of `rule-rules-schema` stand once each in the page and once each in `vault/wiki/rules/schema.yaml`; the new text of `entity-glossary` stands once in the page and once in `vault/wiki/glossary.md`; the old opening text stands 0 times in the page and the file. Case 976: `deferred_by` reads `["[[decision-case-971]]", "[[decision-case-976]]"]` on the three Estimates of Case 971 and `["[[decision-case-976]]"]` on `estimate-handoff-dispatches`.
- This run ticked 13 boxes of `vault/raw/2026-10-31/2307/spec.md`, 3 `read` boxes of the 1831 Spec and 1 `read` box of the 0431 Spec (`git diff`); 3 `read` boxes stay unticked in the 2307 Spec, 5 in the 1831 Spec and 4 in the 0431 Spec.
- `guppi archive` printed `raw/2026-10-31/0128 → archive/plugin/2026-10-31/0128/raw`, `raw/2026-10-31/0431 → archive/plugin/2026-10-31/0431/raw` and `raw/2026-10-31/1831 → archive/plugin/2026-10-31/1831/raw`, nothing on stderr; session 2307 stays in `vault/raw/2026-10-31/`. The 1831 Spec is now `vault/archive/plugin/2026-10-31/1831/raw/spec.md` and the 0431 Spec `vault/archive/plugin/2026-10-31/0431/raw/spec.md`; the line numbers below are theirs.
- Index check: no `create` entry other than an Estimate, so no Grep of a category ran.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 59 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14 lines.
  - `lesson-ledger-reading-writes-a-bare-wikilink` — none: no index line names a reading text copied into a page with no check of its link form; `lesson-librarian-writes-a-total-no-count-printed` and `insight-orchestration-writes-from-its-own-reading` name a written fact with no source, not a bare link.
  - `lesson-orchestration-shows-a-round-after-own-text` — none: no index line names a round shown after a text of the agent; `insight-orchestration-writes-from-its-own-reading` names a fact written from impression, not the opening of a shown round.

## Readings due

- `estimate-case-build-reads-each-list-of-a-new-member` — `failed`; target `rule-case-build` (`draft`); deferred by Cases 971 and 976; method: at Retro, `.claude/agents/case-guppi.md` and the transcripts of the build of Case 956.1 and the `/pre-spec` of session 0431. Result: the `case-guppi` of Case 956.1 ran no search for a hook already in the list and missed the docstring list of `.guppi/guppi/cli.py`.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `failed`; target `rule-orchestration` (`draft`); deferred by Cases 971 and 976; method: at Retro, the dispatch of Case 961 in the transcript of session 0431. Result: the dispatch named Case 960 by id and path, but its sentence named only its new Estimate and not the pages it changes.
- `estimate-orchestration-shows-the-built-case` — `failed`; target `rule-orchestration` (`draft`); deferred by Cases 971 and 976; method: at Retro, `vault/wiki/orchestration.md` and the showing of Cases 960 and 956 in the transcript of session 0431. Result: the answer of the `case-guppi` of 956 put `**Built:**` on its fourth line and the main agent showed it as a built Case.
- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); read: line 651 of the 1831 Spec; method: after the first build of `case-guppi` whose Case proposes a `create` without a `ref` on the new Render of `rule-ask`.
- `estimate-ask-searches-at-prespec` — `pending`; target `rule-ask` (`draft`); read: line 686 of the 1831 Spec; method: after the first `/pre-spec` whose `ask-guppi` runs on the new Render of `rule-ask`.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes a reader and the text it reads.
- `estimate-case-build-reads-the-link-graph-of-what-it-changes` — `pending`; target `rule-case-build` (`draft`); read: line 220 of the 1831 Spec; method: after the `/pre-spec` of the first session on the Render that holds the sentence on `.guppi/links.md` and whose start wrote that file.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — `pending`; target `rule-case-build` (`draft`); read: line 57 of the 1831 Spec; method: after the `/pre-spec` of the first session on the Render that follows a step to the one who carries it out.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — `pending`; target `rule-case-build` (`draft`); read: line 197 of `vault/raw/2026-10-31/2307/spec.md`; method: after the `/pre-spec` of the first session on the new Render of `rule-case-build` in which a Case adds a file that is no page.
- `estimate-case-build-runs-the-vault-query-first` — `pending`; target `rule-case-build` (`draft`); read: line 606 of the 1831 Spec; method: after the first build on the new Render whose Case proposes a `create` without a `ref`.
- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); deferred by Case 971; read: line 88 of the 0431 Spec; method: after the librarian's run of a session that starts with the hook of `rule-librarian-report-copy`: `report.md` of the session folder beside the librarian's last output. This run: no `report.md` stands in `vault/raw/2026-10-31/2307/` while this brief is written.
- `estimate-handoff-dispatches` — `pending`; target `rule-handoff` (`draft`); deferred by Case 976; read: line 136 of the 0431 Spec; method: after a `/handoff` whose skill commits `report.md`: the event log, `handoff.md`, `git log` and the transcript of that session.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph`.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch of items taken up together under the new Render in which a summary carries a line `Other Case`.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`; target `rule-plugin-install` (`draft`); deferred by Case 949; method: by hand, three projects with `/guppi:install` from a local clean version. This run: no step of it printed a fact its method names.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); read: line 629 of the 0431 Spec; method: after a lesson line that declares a new tag by a `newtag` block.
- `estimate-rules-schema-checked` — `pending`; target `rule-rules-schema` (`draft`); read: line 262 of the 2307 Spec; method: `pytest .guppi/tests/test_schemas.py -k rules`; by hand, after a librarian's run: the live `vault/wiki/rules/schema.yaml` against the Criterion and `guppi check`. This run: the render wrote `vault/wiki/rules/schema.yaml`; the new opening text and the new Enforcement sentence stand once each in it, the old opening text 0 times; `guppi check` printed 15 lines, none a `schema` finding, one `rules/rule-rules-schema: status: a page with core: true that is draft`; `guppi test` printed 1856 passed, 6 skipped, 1 deselected.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-spec-box-runs-a-conserved-spec` — `pending`; target `rule-spec-box` (`draft`); read: line 184 of the 0431 Spec; method: `guppi render --check`; by hand, after a session that runs a conserved Spec by `/box`.
- `estimate-sprint-plugin-check-finds-no-bare-slug-link` — `pending`; target `entity-sprint-plugin` (`draft`); read: line 118 of the 2307 Spec; method: by hand, after the librarian's run that applies the `update` of `estimate-link-graph-prints-the-neighbours`: `guppi check` and `git log -p -1` on that page. This run: `guppi check` printed 15 lines, no `ref` line for `estimate-link-graph-prints-the-neighbours`; `git diff` of that page shows the `## Result` line and one History line changed; the commit is made at the close, after this brief.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); method: `pytest .guppi/tests/test_ship.py`; by hand, after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z`, before the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: in a session of the sprint `plugin` before its close, the clean version installed in an empty project.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); method: a pull request from a second account read on GitHub, before the close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer on `README.md` at the `/hi` after the session that writes it, before the close.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); method: after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: neither lesson entry carries `addressed_by`, and neither joined an Insight.

## Flags

- Entries marked `incomplete`, `failed`, `near` or `unparsed`: none.
- Failed Estimates: 3 — `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-orchestration-shows-the-built-case`, all three deferred by Cases 971 and 976.
- `guppi check` printed 15 lines, exit 1 (19 before the work, per the handoff): 11 `status: a page with core: true that is draft` (`rule-ask`, `rule-case-build`, `rule-close`, `rule-handoff`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-rules-schema`, `rule-skill-hi`, `rule-spec-box`, `rule-synthesis`); 3 `unread: failed` (the three above); 1 `ref`: `lessons/lesson-ledger-reading-writes-a-bare-wikilink: ref: body names slug, which no live or archived page carries`. The `backlog.md differs from its sources` line of the handoff's baseline is not in this output.
- `lesson-ledger-reading-writes-a-bare-wikilink`, created this run: its `## Root cause` (line 18) holds the bare `[[slug]]` copied from ledger line 19, the form the lesson records, and lint reads it as a link.
- Defers in `backlog.md` put off in 2 or more sessions: `rule-spec-box` (8), `estimate-orchestration-shows-the-built-case` (4), `rule-ratification` (2), `estimate-case-build-reads-each-list-of-a-new-member` (2), `estimate-orchestration-names-related-cases-in-the-dispatch` (2).
- MOC candidates: none seen. Contradictions: none seen.
- Reads outside what the frame says the job needs: none.

## Next session

### Cases

- C1, the clean branch: push `plugin` and a tag `prod-x.y.z` on its last commit, and read the CI run by `estimate-sprint-plugin-ci-writes-a-clean-branch` (handoff, For the next session).
- Whether the ledger hook refuses a reading line whose text holds a bare `[[…]]` that names no page (`lesson-ledger-reading-writes-a-bare-wikilink`) (handoff, For the next session).
- Why `guppi check` reported `backlog.md differs from its sources` at the start of session 2307 (handoff, For the next session).
- `estimate-case-build-reads-each-list-of-a-new-member` — `failed`, deferred by Cases 971 and 976, stands in `backlog.md`.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `failed`, deferred by Cases 971 and 976, stands in `backlog.md`.
- `estimate-orchestration-shows-the-built-case` — `failed`, deferred by Cases 971 and 976, stands in `backlog.md`.
- Defect: the `## Root cause` of `lesson-ledger-reading-writes-a-bare-wikilink` holds a bare `[[slug]]` (`guppi check`, `ref` finding).

### Work

- `estimate-rules-schema-checked` — read; its `read` box, line 262 of `vault/raw/2026-10-31/2307/spec.md`.
- `estimate-ask-searches-at-prespec` — read on the `/pre-spec` of session 2307; its `read` box, line 686 of `vault/archive/plugin/2026-10-31/1831/raw/spec.md`.
- `estimate-case-build-reads-the-link-graph-of-what-it-changes` — read on the `/pre-spec` of session 2307; its `read` box, line 220 of `vault/archive/plugin/2026-10-31/1831/raw/spec.md`.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — read on the `/pre-spec` of session 2307; its `read` box, line 57 of `vault/archive/plugin/2026-10-31/1831/raw/spec.md`.

### Ask the person

none

## Readings at the close

- `uv run --project .guppi guppi test`: 1856 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: 15 lines, exit 1 (above).
- Live pages: decisions 464, entities 6, estimates 342, insights 13, lessons 60, rules 88.
