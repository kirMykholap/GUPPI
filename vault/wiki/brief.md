# Brief — 2026-11-02, librarian of session 2035 (2026-11-02)

## Where things stand

- Session 2035 of the sprint `plugin`. Cases ratified: 1007, 1008, 1009 (short-form defers); 1010 with 1010.1, 1010.2, 1010.3 (handoff).
- Code: `.guppi/guppi/casecheck.py` — `changed_targets` takes the task lines by `read_tasks` and of each only its first code span; `names_notes` gives one note with the count for a name held by more than `BROAD_NAME` (20) files. `.guppi/tests/test_casecheck.py` gains four tests. `guppi test` 1908 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L10 `estimate-case-check-notes-the-files-that-name-what-a-case-changes` passed; L11 `estimate-case-check-sends-one-note-for-a-broad-name` passed. Lessons: L12, L13 (error) (handoff).
- `guppi materialize` printed `written with 13 entries` for `vault/raw/2026-11-02/2035/materialize.yaml` and `extended with 0 entries` for the yamls of 0039, 0254, 1337 and 1548. The ledger has 13 lines (`wc -l`). The yaml holds entries for lines 1–10, 12 and 13, and line 11 is folded into the `create` of line 7 (`folded: [11]`), so every line is accounted for. Each decision line of Case 1010 stands once in the ledger (lines 4–9).
- The yaml holds 12 entries under `entries` before the synthesis: 3 `defer` (lines 1–3), 5 `update` (lines 4, 5, 6, 8, 9), 1 `create` (line 7), 1 `estimate` (line 10), 2 `lesson` (lines 12, 13); `decisions` holds 7 items (1007, 1008, 1009, 1010, 1010.1–1010.3).
- The synthesis added 2 entries marked `librarian: synthesis`: 1 `update` in `insights`, 1 `update` in `lessons`. The index check had no entry to compare: the one `create` is an Estimate.
- Marks: every entry and every item of `decisions` carries `applied`; `exists` on the 3 `defer` entries (lines 1–3); no entry `failed`, `incomplete`, `near` or `merged`; `unparsed: []`.
- `guppi generate` printed 18 pages written or changed for `2035`, 0 for `0039`, `0254`, `1337` and `1548`, nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `0 page(s) moved`. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. `guppi archive` printed nothing on stdout or stderr and exited 0: no unit moved and none kept; the five sessions of 2026-11-02 are of the run day, which it does not look at.
- Pages created (10), from the log and `git status`: decisions 7 (`decision-case-1007`, `decision-case-1008`, `decision-case-1009`, `decision-case-1010`, `decision-case-1010.1` to `decision-case-1010.3`); estimates 1 (`estimate-case-check-sends-one-note-for-a-broad-name`, `passed` by L11); lessons 2 (`lesson-orchestration-defer-reply-frontier-heading-in-english`, `clustered`; `lesson-ship-test-comment-writes-a-bare-case-reference`, `new`).
- Pages updated (8), from `git status`: rules 2 (`rule-case-check` by 1010.1 and 1010.2, both `replace` items applied to two passages of its Purpose, and the new Estimate added to `estimates`; `rule-case-build` by 1010.3); estimates 5 (`estimate-retro-loads-on-a-red-command` `deferred_by: [[decision-case-1007]]`; `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` `deferred_by: [[decision-case-1008]]`; `estimate-synthesis-keeps-actioned-by-the-mark` `deferred_by: [[decision-case-1009]]`; `estimate-case-check-notes-the-files-that-name-what-a-case-changes` by 1010.1, Criterion set anew, then `passed` by L10; `estimate-case-build-searches-the-names-of-what-it-changes` by 1010.3, Criterion, `purpose` and `method` set anew, `pending`); insights 1 (`insight-orchestration-acknowledging-reply-keeps-headings-in-english`, by the synthesis).
- Written by the scripts (`git status`): `.claude/agents/case-guppi.md` (`guppi render`, from `rule-case-build` of Case 1010.3; the render box of Case 1010.3 in `spec.md` is ticked); `vault/wiki/backlog.md` (`guppi backlog`: `7 items` → `11 items`, three lines added for `estimate-retro-loads-on-a-red-command`, `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, and one for `insight-orchestration-acknowledging-reply-keeps-headings-in-english`). `guppi sprint` and `guppi glossary` changed no file.
- Synthesis: the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 63 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 17 lines.
  - `lesson-orchestration-defer-reply-frontier-heading-in-english` joined `insight-orchestration-acknowledging-reply-keeps-headings-in-english`: the English heading `## Frontier` copied as a literal into a chat in another language. The pair: the Insight stood `actioned` with `addressed_by: [[decision-case-1002]]`, the lesson entry carries no `addressed_by`, so the `update` set `status: open` and `children` plus the lesson; the Insight now stands `open`, severity 1, its `addressed_by` field unchanged.
  - `lesson-ship-test-comment-writes-a-bare-case-reference`: none — no index line of either Grep names a pointer written without its bracket in a code comment; `lesson-ship-example-file-exempt-whole-left-case-pointers` names a file `ship.py` exempts, not a pointer the agent wrote.

## Readings due

No Estimate stands `failed`. Pending, 26:

- `estimate-case-build-searches-the-names-of-what-it-changes` — `rule-case-build` `draft` — `- [ ] read estimate-case-build-searches-the-names-of-what-it-changes` of `vault/raw/2026-11-02/2035/spec.md`; its `method` waits for the `/pre-spec` of the first session in which the hook sends `case-guppi` a note on a file or a name, on the Render of `rule-case-build` this run rendered into `.claude/agents/case-guppi.md`.
- `estimate-ask-query-before-a-create` — `rule-ask` `draft` — by hand, after the first build of `case-guppi` whose Case proposes a `create` without a `ref`: its agent transcript.
- `estimate-case-build-goes-on-after-a-live-compaction` — `rule-case-build` `draft` — by hand, after the first compaction of a `case-guppi` in a working session: its transcript, note and event log.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` `draft` — by hand, after the first Case that names a test over a live file: its `then` and `tasks`.
- `estimate-case-build-reads-each-list-of-a-new-member` — `rule-case-build` `draft` — by hand, after the first build in a later session whose Case adds a member to a spelled-out list: its transcript and case file.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — `rule-case-build` `draft` — by hand, after the `/pre-spec` of the first session in which a Case adds a file that is no page of `vault/wiki/`: the transcript and case file.
- `estimate-case-build-runs-the-vault-query-first` — `rule-case-build` `draft` — by hand, after the first build whose Case proposes a `create` without a `ref`: its transcript.
- `estimate-hi-writes-frontier` — `rule-skill-hi` `draft` — by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint: the person's answer.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `rule-morph` `draft` — by hand, after the session whose Work Mode builds the setup skill of `rule-morph`: an empty project, `/guppi:install`, `/hi`.
- `estimate-morph-takes-in-the-set-aside-files` — `rule-morph` `draft` — by hand, after the session whose Work Mode builds the setup skill of `rule-morph`: a project with files of its own, `/guppi:install`, `/hi`.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `rule-orchestration` `draft` — by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word: that reply in its transcript; none came in session 2035 (handoff).
- `estimate-orchestration-signs-items-taken-together` — `rule-orchestration` `draft` — by hand, after the first batch of items taken up together whose summary carries a line Other Case: the replies of the main agent.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `rule-plugin-install` `draft` — by hand, after the librarian's run of the session that sets its Criterion, with a tag `prod-x.y.z`: three projects and `/guppi:install`; `deferred_by: [[decision-case-949]]`.
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` — `rule-prespec` `draft` — by hand, after the first `/pre-spec` whose plan holds a Case that adds a file that is no page of `vault/wiki/`: the findings and Grep of `ask-guppi`.
- `estimate-retro-loads-on-a-red-command` — `rule-retro` `draft` — by hand, after the librarian's render of `.claude/skills/retro/SKILL.md` with `--exit-zero`: the first load of `/retro` after it, in its transcript; `deferred_by: [[decision-case-1007]]`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `rule-skill-merge-main` `draft` — by hand, after the first `/merge-main` that leaves a conflicted page: its `merge.md`, Case, decision lines and merge commit.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `rule-skill-pr-review` `draft` — by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `entity-sprint-plugin` `draft` — `pytest .guppi/tests/test_ship.py`; by hand, after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` of `plugin`, before the close of `plugin`; the person's answer at the close when no such run comes.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `entity-sprint-plugin` `draft` — by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `entity-sprint-plugin` `draft` — by hand, in a session of `plugin` before its close: the clean version installed in an empty project.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `entity-sprint-plugin` `draft` — by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`; this run's yaml holds no entry for that lesson.
- `estimate-sprint-plugin-link-graph-is-gone` — `entity-sprint-plugin` `draft` — by hand, after the librarian's run that applies the delete of `entity-link-graph`; this run's yaml holds no entry for that page.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `entity-sprint-plugin` `draft` — by hand, a pull request from a second account read on GitHub, before the close of `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` — `entity-sprint-plugin` `draft` — by hand, the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of `plugin`.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` `draft` — by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`: the yaml and the brief; `deferred_by: [[decision-case-1009]]`. This run: the synthesis put `lesson-orchestration-defer-reply-frontier-heading-in-english`, whose entry carries no `addressed_by`, under `insight-orchestration-acknowledging-reply-keeps-headings-in-english`, which stood `actioned` with `addressed_by: [[decision-case-1002]]`; the `update` carries `set: {children: [<two archived lessons>, the new lesson], status: open}` and no `addressed_by`; the Insight stands `open`, severity 1, `addressed_by` unchanged; the lesson stands `clustered`, not archived; no lesson entry of this run carries `addressed_by`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` `draft` — by hand, after the librarian's render of `.claude/skills/work/SKILL.md` with `--exit-zero`: the first `/work` that loads while `guppi check` exits 1; `deferred_by: [[decision-case-1008]]`.

## Flags

- No entry is marked `incomplete`, `failed`, `near` or `unparsed`. No Estimate stands `failed`.
- `insight-orchestration-acknowledging-reply-keeps-headings-in-english` was set `open` by the synthesis; both earlier children stand archived (by session 1548), so its one live child is `lesson-orchestration-defer-reply-frontier-heading-in-english`; its `addressed_by: [[decision-case-1002]]` stays on the page beside `status: open`.
- The handoff notes that `ask-guppi` reported searches of code beyond the one its frame allows (Notes from memory).
- MOC candidates: none seen. Contradictions: none found.
- Lint: `guppi check` printed nothing and exited 0.

## Next session

Cases:
- C1: the owner pushes `plugin` and a tag `prod-x.y.z`, and the session reads the CI run (handoff, For the next session).
- Whether the threshold of 20 files fits, once a real note under the new code is seen (handoff, For the next session).

Work:
- none

Ask the person:
- none

## Readings at the close

- `uv run --project .guppi guppi test`: 1908 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: printed nothing, exit 0.
- Pages under `vault/wiki/`: decisions 525, entities 5, estimates 352, insights 17, lessons 65, rules 88. Pages under `vault/archive/`: 3232 (`find -name '*.md'`).
