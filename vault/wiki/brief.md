# Brief — 2026-11-03, librarian of session 2155 (2026-11-02)

## Where things stand

- Session 2155 of the sprint `plugin`. Cases ratified: 1011 with 1011.1, 1011.2, 1011.3 and 1011.4; 1012; 1013; each built again on the findings of `/pre-spec` and ratified again (handoff).
- Code: `.guppi/guppi/casecheck.py` (`names_notes` gives one note per Case that lists each unread file once; `BROAD_NAME` gone), `.guppi/guppi/prespec.py` (`open_box_closers`), `.guppi/guppi/ratified.py` (`text_after`), `.guppi/guppi/frontierguard.py` (new), `.guppi/guppi/cli.py` (`frontierguard`). Tests: `.guppi/tests/test_casecheck.py`, `.guppi/tests/test_frontierguard.py` (new, 13 tests). `guppi test` 1921 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L15 `estimate-sprint-plugin-ci-writes-a-clean-branch` passed (CI run on `prod-0.3.0`); L18, L19, L20, L21 passed. Lessons: L22, L23 (error). C1 of the Frontier closed as work with no Case: the person pushed `plugin` and the tag `prod-0.3.0` by hand (handoff).
- `guppi materialize` printed `written with 23 entries` for `vault/raw/2026-11-02/2155/materialize.yaml` and `extended with 0 entries` for the yamls of 0039, 0254, 1337, 1548 and 2035. The ledger has 23 lines (`wc -l`). The yaml holds entries for lines 1–18 and 20–23; line 19 is folded into the `create` of line 9 (`folded: [19]`), so every line is accounted for; `unparsed: []`.
- The yaml holds 22 entries under `entries` before the synthesis: 13 `update` (lines 1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 14, 16, 17), 2 `create` (lines 8, 9), 1 `delete` (line 3), 4 `estimate` (lines 15, 18, 20, 21), 2 `lesson` (lines 22, 23); `decisions` holds 7 items (1011, 1011.1–1011.4, 1012, 1013).
- Index check: the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` printed 89 lines; no line names the purpose of `rule-frontier-hook`, so it stands as a `create` with no mark. The Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 65 lines: `lesson-ship-docstring-sample-writes-a-real-case-number` got `near: lesson-ship-test-comment-writes-a-bare-case-reference` (same check, another incident); `lesson-caseid-session-option-takes-the-hhmm` got no mark. The `create` of line 9 is an Estimate and has no index check.
- The synthesis added 3 entries marked `librarian: synthesis`: 1 `create` in `insights`, 2 `update` in `lessons`.
- Marks: every entry and every item of `decisions` carries `applied`; one entry carries `near` (line 22); no entry `failed`, `incomplete`, `exists` or `merged`.
- `guppi generate` printed 31 pages written or changed for `2155`, 0 for the other five sessions, nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `4 page(s) moved`. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- `guppi archive` moved 5 units and printed nothing on stderr: `raw/2026-11-02/0039`, `0254`, `1337`, `1548` and `2035` → `archive/plugin/2026-11-02/<HHMM>/raw`. It kept `raw/2026-11-02/2155`, the session of the run.
- Pages created (12), from the log and `git status`: decisions 7 (`decision-case-1011`, `decision-case-1011.1` to `decision-case-1011.4`, `decision-case-1012`, `decision-case-1013`); rules 1 (`rule-frontier-hook`, `core: true`, `draft` → `built` by the cascade, child of `rule-plan-mode`); estimates 1 (`estimate-frontier-hook-refuses-an-open-box-with-a-closer`, `passed` by L19); lessons 2 (`lesson-ship-docstring-sample-writes-a-real-case-number`, `clustered`; `lesson-caseid-session-option-takes-the-hhmm`, `new`); insights 1 (`insight-ship-live-code-writes-a-case-number-outside-a-bracket`, `open`, severity 2, by the synthesis).
- Pages updated (15), from `git status`: rules 6 (`rule-case-check` by 1011.1; `rule-case-build` by 1011.2 and 1011.3, three `replace` items in ledger order; `rule-case-protocol` by 1011.3; `rule-hook-registry` by 1012; `rule-orchestration` by 1013, four `replace` pairs; `rule-plan-mode`, child `rule-frontier-hook` added); estimates 6 (`estimate-case-check-notes-the-files-that-name-what-a-case-changes` by 1011.1, then `passed` by L18; `estimate-case-build-searches-the-names-of-what-it-changes` by 1011.2, `pending`; `estimate-case-build-reads-by-need-and-in-parts` by 1011.3, then `passed` by L20; `estimate-case-build-writes-the-case` by 1011.4, then `passed` by L21; `estimate-orchestration-acknowledging-reply` by 1013, `pending`; `estimate-sprint-plugin-ci-writes-a-clean-branch` `passed` by L15); insights 2 (`insight-orchestration-frontier-closer-leaves-the-box-open` `actioned`, `addressed_by: [[decision-case-1012]]`; `insight-orchestration-acknowledging-reply-keeps-headings-in-english` `actioned`, `addressed_by: [[decision-case-1013]]`); lessons 1 (`lesson-ship-test-comment-writes-a-bare-case-reference`, `clustered` by the synthesis).
- Pages deleted and archived: `estimate-case-check-sends-one-note-for-a-broad-name` deleted by 1011.1. `guppi cleanup` moved it and the three lessons of the two Insights set `actioned` (`lesson-frontier-closer-appended-without-ticking-the-box`, `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`, `lesson-orchestration-defer-reply-frontier-heading-in-english`) to `vault/archive/plugin/2026-11-03/2155/`.
- Written by the scripts (`git status`): `.claude/agents/case-guppi.md` and `vault/wiki/case-schema.md` (render of Cases 1011.2, 1011.3); `.claude/settings.json` (render of Case 1012: `guppi frontierguard` added to `PreToolUse` after `guppi ratified --guard`); `vault/wiki/orchestration.md` (render of Case 1013); `vault/wiki/sprint.md` (`guppi sprint`: the milestone The clean branch and its item stand `[x]`, `passed`); `vault/wiki/backlog.md` (`guppi backlog`: `11 items` → `10 items`, the two Insights set `actioned` gone, `insight-ship-live-code-writes-a-case-number-outside-a-bracket` added). `guppi glossary` changed no file. The render boxes and the page boxes of the Spec stand ticked.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 65 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 17 lines.
  - `lesson-ship-docstring-sample-writes-a-real-case-number` joined `lesson-ship-test-comment-writes-a-bare-case-reference` under the new `insight-ship-live-code-writes-a-case-number-outside-a-bracket`: in both the agent wrote a case number in the live code outside a bracket, and the check of `test_ship.py` failed the full `guppi test` of Work Mode. The lesson entry carries no `addressed_by`, so the Insight is born `open`.
  - `lesson-caseid-session-option-takes-the-hhmm`: none — `insight-caseid-printed-an-id-it-did-not-hold` names a run that printed an id it did not hold, and `lesson-caseid-run-to-check-an-id-held-a-new-one` a run taken for a read of the store; neither names a wrong value given to `--session` from the words "the stamp of the hi: line".

## Readings due

No Estimate stands `failed`. Pending, 26:

- `estimate-case-build-searches-the-names-of-what-it-changes` — `rule-case-build` `draft` — `- [ ] read estimate-case-build-searches-the-names-of-what-it-changes` of `vault/raw/2026-11-02/2155/spec.md`; its `method` waits for the `/pre-spec` of the first session in which the hook sends `case-guppi` the list note, on the Render of `rule-case-build` this run rendered into `.claude/agents/case-guppi.md`.
- `estimate-orchestration-acknowledging-reply` — `rule-orchestration` `draft` — `- [ ] read estimate-orchestration-acknowledging-reply` of `vault/raw/2026-11-02/2155/spec.md`; by hand, after the librarian's render of the sentence of Case 1013: an acknowledging reply and a reply that acknowledges Cases ratified together, in their transcript. This run: `guppi render` wrote `vault/wiki/orchestration.md`, and its diff adds one line that holds "term of the harness".
- `estimate-ask-query-before-a-create` — `rule-ask` `draft` — by hand, after the first build of `case-guppi` whose Case proposes a `create` without a `ref`: its agent transcript.
- `estimate-case-build-goes-on-after-a-live-compaction` — `rule-case-build` `draft` — by hand, after the first compaction of a `case-guppi` in a working session: its transcript, note and event log.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` `draft` — by hand, after the first Case that names a test over a live file: its `then` and `tasks`.
- `estimate-case-build-reads-each-list-of-a-new-member` — `rule-case-build` `draft` — by hand, after the first build in a later session whose Case adds a member to a spelled-out list: its transcript and case file.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — `rule-case-build` `draft` — by hand, after the `/pre-spec` of the first session in which a Case adds a file that is no page of `vault/wiki/`: the transcript and case file of its `case-guppi`.
- `estimate-case-build-runs-the-vault-query-first` — `rule-case-build` `draft` — by hand, after the first build whose Case proposes a `create` without a `ref`: its transcript.
- `estimate-hi-writes-frontier` — `rule-skill-hi` `draft` — by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint: the person's answer.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `rule-morph` `draft` — by hand, after the session whose Work Mode builds the setup skill of `rule-morph`: an empty project, `/guppi:install`, `/hi`.
- `estimate-morph-takes-in-the-set-aside-files` — `rule-morph` `draft` — by hand, after the session whose Work Mode builds the setup skill of `rule-morph`: a project with files of its own, `/guppi:install`, `/hi`.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `rule-orchestration` `draft` — by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word: that reply in its transcript.
- `estimate-orchestration-signs-items-taken-together` — `rule-orchestration` `draft` — by hand, after the first batch of items taken up together whose summary carries a line Other Case: the replies of the main agent.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `rule-plugin-install` `draft` — by hand, after the librarian's run of the session that sets its Criterion, with a tag `prod-x.y.z`: three projects and `/guppi:install`; `deferred_by: [[decision-case-949]]`. This run's yaml holds no entry for it.
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` — `rule-prespec` `draft` — by hand, after the first `/pre-spec` whose plan holds a Case that adds a file that is no page of `vault/wiki/`: the findings and Grep of `ask-guppi`.
- `estimate-retro-loads-on-a-red-command` — `rule-retro` `draft` — by hand, after the librarian's render of `.claude/skills/retro/SKILL.md` with `--exit-zero`: the first load of `/retro` after it, in its transcript; `deferred_by: [[decision-case-1007]]`. This run's render changed no `.claude/skills/retro/SKILL.md`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `rule-skill-merge-main` `draft` — by hand, after the first `/merge-main` that leaves a conflicted page: its `merge.md`, Case, decision lines and merge commit.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `rule-skill-pr-review` `draft` — by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `entity-sprint-plugin` `draft` — by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `entity-sprint-plugin` `draft` — by hand, in a session of `plugin` before its close: the clean version installed in an empty project.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `entity-sprint-plugin` `draft` — by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`. This run's yaml holds no entry for that lesson.
- `estimate-sprint-plugin-link-graph-is-gone` — `entity-sprint-plugin` `draft` — by hand, after the librarian's run that applies the delete of `entity-link-graph`. This run's yaml holds no entry for that page.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `entity-sprint-plugin` `draft` — by hand, a pull request from a second account read on GitHub, before the close of `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` — `entity-sprint-plugin` `draft` — by hand, the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of `plugin`.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` `draft` — by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`: the yaml and the brief; `deferred_by: [[decision-case-1009]]`. This run: no lesson entry carries `addressed_by`; the synthesis put `lesson-ship-docstring-sample-writes-a-real-case-number` and `lesson-ship-test-comment-writes-a-bare-case-reference` under a new Insight, born `open`, and put no lesson under an `actioned` Insight.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` `draft` — by hand, after the librarian's render of `.claude/skills/work/SKILL.md` with `--exit-zero`: the first `/work` that loads while `guppi check` exits 1; `deferred_by: [[decision-case-1008]]`. This run's render changed no `.claude/skills/work/SKILL.md`.

## Flags

- `near`: `lesson-ship-docstring-sample-writes-a-real-case-number` (line 22) is near `lesson-ship-test-comment-writes-a-bare-case-reference`; both now stand `clustered` under `insight-ship-live-code-writes-a-case-number-outside-a-bracket`.
- No entry is marked `incomplete`, `failed` or `unparsed`. No Estimate stands `failed`.
- The handoff notes that `ask-guppi` at `/pre-spec` reported more searches of code than its frame allows, as in session 2035; no finding rested on them (Notes from memory).
- The handoff notes that `claude plugin validate` in the run of `prod.yml` on `prod-0.3.0` printed `ICON_MISSING`; the run passed (Observations).
- The `PostToolUse` hook `shellwrite` reported, on the move of `guppi archive`, that it turned the CRLF line endings of `vault/archive/plugin/2026-11-02/0039/raw/report.md` into LF.
- A read the frame says the job does not need: a Grep of `vault/raw/2026-11-02/2155/spec.md` for `frontierguard`, which printed lines of Case 1012 beyond the unticked and ticked lines, made for Next session — whether a Case of session 2155 adds a file that is no page of `vault/wiki/`, the event of `estimate-case-build-reads-the-readers-of-a-new-files-folder` and `estimate-prespec-finds-a-reader-of-a-new-files-folder`. The handoff did not ask for it.
- MOC candidates: none seen. Stale defers: none seen. Contradictions: none found.
- Lint: `guppi check` printed nothing and exited 0.

## Next session

Cases:
- Whether the plugin gets an icon, since `claude plugin validate` notes `ICON_MISSING` on the clean version (handoff, For the next session).
- Whether `ask-guppi` keeps to its one search of code at `/pre-spec`, or its frame changes: it reported more searches than allowed in two sessions running (handoff, For the next session).
- Defer `estimate-orchestration-acknowledging-reply` into `backlog.md`, since session 2155 did not take its reading (handoff, Debt); the render its `method` waits for ran in this run.

Work:
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — its event is seen: Case 1012 of session 2155 adds `.guppi/guppi/frontierguard.py` and `.guppi/tests/test_frontierguard.py` (handoff, What actually got done).
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` — the same event, the `/pre-spec` of session 2155.

Ask the person:
- none

## Readings at the close

- `uv run --project .guppi guppi test`: 1921 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: printed nothing, exit 0.
- Pages under `vault/wiki/`: decisions 532, entities 5, estimates 352, insights 18, lessons 64, rules 89. Pages under `vault/archive/`: 3288 (`find -name '*.md'`).
