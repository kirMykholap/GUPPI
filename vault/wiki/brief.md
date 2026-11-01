# Brief — 2026-11-01, librarian of session 0141

## Where things stand

- Session 0141 of the sprint `plugin`. Cases ratified: 977, 978, 979, 980, 981 (981.1, 981.2) (handoff).
- Code: `.guppi/guppi/pages.py` (`page_paths`), `.guppi/guppi/lint.py` (`body_links`, `link_names`, `unknown_links`; `check_refs` judges a body link by the names), `.guppi/guppi/prespec.py` (`known_slugs` removed; `check_bare_links` by `link_names` and `unknown_links`), `.guppi/guppi/ledger.py` (`refused_links`, `link_message`, a docstring paragraph), `.guppi/guppi/casecheck.py` (`DROPPED_LABEL`, `is_dropped`, `summary_after_text`, a docstring paragraph). Tests: `test_ledger.py` (8 `bare_link`), `test_lint.py` (6 `bare_link`, one parametrized test), `test_casecheck.py` (8 `summary_after_text`). `guppi test` 1856 passed, 6 skipped, 1 deselected at the Baseline; 1878 passed, 6 skipped, 1 deselected at Retro; `guppi style` clean (handoff).
- Readings: L1 `estimate-rules-schema-checked` passed (at `/hi`); at Retro `estimate-ledger-write-refuses-a-bare-link-to-no-page`, `estimate-case-check-sends-back-a-summary-after-text`, `estimate-orchestration-shows-the-built-case` and `estimate-ask-searches-at-prespec` passed; `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-case-build-reads-the-link-graph-of-what-it-changes` and `estimate-case-build-reads-the-readers-of-a-changed-step` failed. Lesson: L19 `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone` (error) (handoff).
- `guppi materialize` printed `written with 19 entries` for `vault/raw/2026-11-01/0141/materialize.yaml` and `extended with 0 entries` for `vault/raw/2026-10-31/2307/materialize.yaml`. The ledger has 19 lines (`wc -l`); the yaml holds entries for lines 1–11 and 14–19, and lines 12 and 13 are folded into the `create` entries of lines 3 and 10, so every line is accounted for. Kinds: 6 `estimate`, 3 `create`, 7 `update`, 1 `lesson`, 17 in all; the index check and the synthesis added none.
- Marks: all 17 entries `applied`; no entry `failed`, `exists`, `incomplete`, `near`, `librarian` or `merged`; `unparsed: []`.
- `guppi generate` printed 26 pages written or changed for `0141` and 0 for `2307`; nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `2 page(s) moved`, nothing on stderr. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- Pages created (11), from `git status`: decisions 7 (`decision-case-977`, `decision-case-978`, `decision-case-979`, `decision-case-980`, `decision-case-981`, `decision-case-981.1`, `decision-case-981.2`); estimates 3 (`estimate-ledger-write-refuses-a-bare-link-to-no-page` `passed`, `estimate-case-check-sends-back-a-summary-after-text` `passed`, `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` `pending`); lessons 1 (`lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`, `new`).
- Pages updated (13), from `git status`: estimates 7 (`estimate-rules-schema-checked`, `estimate-ask-searches-at-prespec`, `estimate-orchestration-shows-the-built-case`, each `pending → passed`; `estimate-orchestration-names-related-cases-in-the-dispatch`, `estimate-case-build-reads-the-link-graph-of-what-it-changes`, `estimate-case-build-reads-the-readers-of-a-changed-step`, each `pending → failed`; `estimate-case-build-reads-each-list-of-a-new-member`, `pending`); rules 4 (`rule-ledger-write`, `rule-case-build`, `rule-case-check` by Cases; `rule-rules-schema` `draft → built` by the cascade); lessons 1 (`lesson-ledger-reading-writes-a-bare-wikilink`); entities 1 (`entity-sprint-plugin`, by its `estimates` list).
- Superseded and archived (log): Cases 979, 980 and 981.2 each supersede Cases 971 and 976; generate set `decision-case-971` and `decision-case-976` `archived · superseded`, and cleanup moved both to `vault/archive/plugin/2026-11-01/0141/decisions/`.
- Written by the scripts (`git status`): `.claude/agents/case-guppi.md` (render, one line), `vault/wiki/sprint.md` (one new line, the reading of `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link`), `vault/wiki/backlog.md` (12 → 9 items; `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-names-related-cases-in-the-dispatch` and `estimate-orchestration-shows-the-built-case` left).
- The handoff's instructions, checked against the yaml and by `git diff`: the `update` of `rule-ledger-write` sets `implementation_ref` to 10 paths, `.guppi/guppi/lint.py` and `.guppi/tests/test_lint.py` among them; the diff of `lesson-ledger-reading-writes-a-bare-wikilink` changes the field `root_cause` (line 4) and `## Root cause` (line 18), each to `` `[[slug]]` `` in a code span, and adds one History line; the entries of Cases 979, 980 and 981.2 carry `supersedes: ['971', '976']`, and the log shows the defers of 971 and 976 superseded on the three Estimates.
- This run ticked 15 boxes of `vault/raw/2026-11-01/0141/spec.md` and 1 `read` box of the 2307 Spec (`git diff`); 2 `read` boxes stay unticked in the 0141 Spec (lines 148 and 210) and 2 in the 2307 Spec (lines 118 and 197).
- Index check: one `create` entry other than an Estimate, `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`; the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 60 lines; no index line names the same root cause or a near one.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 60 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 14 lines.
  - `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone` — none: no index line names an Edit that matched only the end of a line and left its box; `lesson-frontier-sprint-line-closed-by-a-case-that-updates-no-sprint-page` and `lesson-frontier-closed-a-backlog-item-deferred-again-as-a-case` name the choice of a closer, not the edit that writes it.

## Readings due

- `estimate-case-build-reads-the-link-graph-of-what-it-changes` — `failed`; target `rule-case-build` (`draft`); method: after the `/pre-spec` of the first session on the Render that holds the sentence on `.guppi/links.md`, the transcripts of each `case-guppi` of that session. Result: 2 of 4 Cases of session 2307 found the block of each existing page and file they change; no `context` said that a page it creates has no block.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — `failed`; target `rule-case-build` (`draft`); method: after the `/pre-spec` of the first session on the Render that follows a step to the one who carries it out, the findings of its `ask-guppi`. Result: 1 of 7 findings at the pre-spec of session 2307, Case 972 missed the kept-method path of the wait check.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `failed`; target `rule-orchestration` (`draft`); method: at Retro, the dispatches of session 0141 in its transcript. Result: the dispatch of 980 named Case 977 with its pages and no path, the dispatch of 981 with its pages, no sentence and no path; 2 of 4 related-Case mentions after the batch fall short.
- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); method: after the first build of `case-guppi` whose Case proposes a `create` without a `ref` on the Render of `rule-ask` that runs every category.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes a reader and the text it reads.
- `estimate-case-build-reads-each-list-of-a-new-member` — `pending`; target `rule-case-build` (`draft`); read: line 210 of `vault/raw/2026-11-01/0141/spec.md`; method: after the first build of `case-guppi` in a later session whose Case adds a member to a list that texts spell out one by one.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — `pending`; target `rule-case-build` (`draft`); read: line 197 of the 2307 Spec; method: after the `/pre-spec` of the first session on the new Render of `rule-case-build` in which a Case adds a file that is no page.
- `estimate-case-build-runs-the-vault-query-first` — `pending`; target `rule-case-build` (`draft`); method: after the first build on the new Render whose Case proposes a `create` without a `ref`.
- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); deferred by Case 971; method: after the librarian's run of a session that starts with the hook of `rule-librarian-report-copy`: `report.md` of the session folder beside the librarian's last output. This run: no `report.md` stands in `vault/raw/2026-11-01/0141/` while this brief is written.
- `estimate-handoff-dispatches` — `pending`; target `rule-handoff` (`draft`); deferred by Case 976; method: after a `/handoff` whose skill commits `report.md`: the event log, `handoff.md`, `git log` and the transcript of that session.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph`.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch of items taken up together under the new Render in which a summary carries a line `Other Case`.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`; target `rule-plugin-install` (`draft`); deferred by Case 949; method: by hand, after the librarian's run of the session that sets this Criterion, three projects with `/guppi:install` from a local clean version. This run: no step of it printed a fact its method names.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); method: after a lesson line that declares a new tag by a `newtag` block.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-spec-box-runs-a-conserved-spec` — `pending`; target `rule-spec-box` (`draft`); method: `guppi render --check`; by hand, after a session that runs a conserved Spec by `/box`.
- `estimate-sprint-plugin-check-finds-no-bare-slug-link` — `pending`; target `entity-sprint-plugin`; read: line 118 of the 2307 Spec; method: by hand, after the librarian's run that applies the `update` of `estimate-link-graph-prints-the-neighbours`: `guppi check` and `git log -p -1` on that page. This run: `guppi check` printed 13 lines, no `ref` line for `estimate-link-graph-prints-the-neighbours`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin`; method: `pytest .guppi/tests/test_ship.py`; by hand, after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z`, before the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin`; method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin`; method: in a session of the sprint `plugin` before its close, the clean version installed in an empty project.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `pending`; target `entity-sprint-plugin`; read: line 148 of `vault/raw/2026-11-01/0141/spec.md`; method: by hand, after the librarian's run that applies the `update` of `lesson-ledger-reading-writes-a-bare-wikilink`: `guppi check` and `git log -p -1` on that page. This run: `guppi check` printed 13 lines, no `ref` line for `lesson-ledger-reading-writes-a-bare-wikilink`; `git diff` of that page changes line 4 (`root_cause`) and line 18 (`## Root cause`), each `[[slug]]` now in a code span, and adds one History line; the commit is made at the close, after this brief.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin`; method: a pull request from a second account read on GitHub, before the close.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin`; method: the person's answer on `README.md` at the `/hi` after the session that writes it, before the close.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); method: after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: the one lesson entry carries no `addressed_by` and joined no Insight.

## Flags

- Entries marked `incomplete`, `failed`, `near` or `unparsed`: none.
- Failed Estimates: 3 — `estimate-case-build-reads-the-link-graph-of-what-it-changes`, `estimate-case-build-reads-the-readers-of-a-changed-step`, `estimate-orchestration-names-related-cases-in-the-dispatch`.
- `guppi check` printed 13 lines, exit 1 (15 before the work, per the handoff): 10 `status: a page with core: true that is draft` (`rule-ask`, `rule-case-build`, `rule-close`, `rule-handoff`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-spec-box`, `rule-synthesis`); 3 `unread: failed` (the three above). No `ref` line and no `backlog.md differs from its sources` line.
- Stale defer: `estimate-close-reports-the-run` keeps `deferred_by: ["[[decision-case-971]]"]` and `estimate-handoff-dispatches` keeps `deferred_by: ["[[decision-case-976]]"]`, and both stand in `backlog.md`; this run, generate set `decision-case-971` and `decision-case-976` `archived · superseded` and cleanup moved them to `vault/archive/plugin/2026-11-01/0141/decisions/` (log). The supersedes of Cases 979, 980 and 981.2 retired those defers on three other Estimates only.
- Defers in `backlog.md` put off in 2 or more sessions: `rule-spec-box` (8), `rule-ratification` (2).
- MOC candidates: none seen. Contradictions: the stale defer above.
- Reads outside what the frame says the job needs: none.

## Next session

### Cases

- `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed: `case-guppi` greps the block of some of the pages and files it changes but not each one, and no `context` says that a page it creates has no block; what changes in `rule-case-build`, or whether the Criterion is too strict for a created page (handoff, For the next session).
- `estimate-case-build-reads-the-readers-of-a-changed-step` failed: Case 972 of session 2307 missed the kept-method path of the wait check, which does the same step (handoff, For the next session).
- `estimate-orchestration-names-related-cases-in-the-dispatch` failed again: whether the rule needs a guard, or whether a Case that only changes how pre-spec reads a link counts as related (handoff, For the next session).
- C1, the clean branch: push `plugin` and a tag `prod-x.y.z`, and read the CI run (handoff, For the next session).
- Whether `backlog --check` should leave out the Frontier of the live session, so the Baseline does not show `backlog.md differs from its sources` after a put-off (handoff, For the next session).
- `estimate-close-reports-the-run` and `estimate-handoff-dispatches` stay deferred by `decision-case-971` and `decision-case-976`, which this run archived as superseded (Flags, log).

### Work

none

### Ask the person

none

## Readings at the close

- `uv run --project .guppi guppi test`: 1878 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: 13 lines, exit 1 (above).
- Live pages: decisions 469, entities 6, estimates 345, insights 13, lessons 61, rules 88.
