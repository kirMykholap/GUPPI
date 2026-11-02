# Brief — 2026-11-02, librarian of session 1548 (2026-11-02)

## Where things stand

- Session 1548 of the sprint `plugin`. Cases ratified: 1005 with 1005.1, 1005.2, 1005.3; 1006 (handoff).
- Code: `.guppi/guppi/casecheck.py` gains the note of names (`looked_files`, `carried_names`, `changed_targets`, `named_files`, `name_pattern`, `names_notes`, joined to `check_answer` by `looked`); `.guppi/tests/test_casecheck.py` gains eight tests and its fixture plan moves under a home folder. `guppi test` 1904 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L7 and L9 `estimate-orchestration-acknowledging-reply` passed; L10 `estimate-case-check-notes-the-files-that-name-what-a-case-changes` passed. Lessons: L11 (knowledge), L12 (error) (handoff).
- `guppi materialize` printed `written with 12 entries` for `vault/raw/2026-11-02/1548/materialize.yaml` and `extended with 0 entries` for the yamls of 0039, 0254 and 1337. The ledger has 12 lines (`wc -l`); the yaml holds entries for lines 1–9, 11 and 12, and line 10 is folded into the `create` of line 2 (`folded: [10]`), so every line is accounted for. The yaml holds 11 entries under `entries` before the synthesis: 6 `update` (lines 1, 3, 4, 5, 6, 8), 1 `create` (line 2), 2 `estimate` (lines 7, 9), 2 `lesson` (lines 11, 12); `decisions` holds 5 items (1005, 1005.1–1005.3, 1006).
- The synthesis added 3 entries marked `librarian: synthesis`: 1 `create` in `insights`, 2 `update` in `lessons`. The index check added `near` to the entry of line 12.
- Marks: every entry and every item of `decisions` carries `applied`; no entry `failed`, `exists`, `incomplete` or `merged`; one `near`; `unparsed: []`.
- `guppi generate` printed 18 pages written or changed for `1548`, 0 for `0039`, `0254` and `1337`, nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `2 page(s) moved`. `guppi render`, `sprint`, `backlog`, `glossary` and `archive` printed nothing on stderr.
- Pages created (9), from the log and `git status`: decisions 5 (`decision-case-1005`, `decision-case-1005.1` to `decision-case-1005.3`, `decision-case-1006`); estimates 1 (`estimate-case-check-notes-the-files-that-name-what-a-case-changes`, `passed` by L10); lessons 2 (`lesson-case-check-names-note-lists-hundreds-of-files`, `new`; `lesson-frontier-closer-appended-without-ticking-the-box`, `clustered`); insights 1 (`insight-orchestration-frontier-closer-leaves-the-box-open`, from the synthesis, `open`, severity 2).
- Pages updated (7), from `git status`: rules 2 (`rule-case-check` by 1005.1; `rule-case-build` by 1005.2 and 1005.3); estimates 3 (`estimate-case-build-searches-the-names-of-what-it-changes` by 1005.2, Criterion, `purpose` and `method` set anew, `failed → pending`; `estimate-case-build-reads-each-list-of-a-new-member` by 1005.3, Criterion set anew, `failed → pending`; `estimate-orchestration-acknowledging-reply` `failed → passed` by L7, then `passed → passed` by L9, whose result is the one on the page); insights 1 (`insight-orchestration-acknowledging-reply-keeps-headings-in-english` `actioned` by 1006, `addressed_by: [[decision-case-1002]]`, severity 0, kept live); lessons 1 (`lesson-orchestration-closes-a-frontier-line-by-its-closer-alone` `new → clustered`).
- Archived by `generate` and `guppi cleanup` (2): `lesson-acknowledging-reply-labels-left-in-english` and `lesson-orchestration-acknowledging-reply-leaves-the-frontier-heading-untranslated`, to `vault/archive/plugin/2026-11-02/1548/lessons/`, log line `archived · insight actioned`.
- Written by the scripts (`git status`): `.claude/agents/case-guppi.md` (`guppi render`); `vault/wiki/backlog.md` (`guppi backlog`: the line of `insight-orchestration-acknowledging-reply-keeps-headings-in-english` gone, a line of `insight-orchestration-frontier-closer-leaves-the-box-open` added). `guppi sprint` and `guppi glossary` changed no file.
- This run ticked 9 boxes of `vault/raw/2026-11-02/1548/spec.md` (`git diff`). Unticked boxes of the Specs under `vault/raw/` now, each a `read` box: lines 122 and 163 of the 1548 Spec; lines 270 and 317 of the 1337 Spec; line 253 of the 0039 Spec.
- The handoff's instructions, checked after the run:
  - `guppi check` after this run: exit 0, no line. It names neither `rule-case-build` nor `rule-orchestration` as `a page with core: true that is draft`. Both pages still carry `status: draft` and `core: true`.
  - L9 is the result on `estimate-orchestration-acknowledging-reply`: `generate` applied L7 and then L9, and the `## Result` holds the text of L9 (`git diff`).
  - Case 1006: the Insight stands `actioned` with `addressed_by: [[decision-case-1002]]`; the cascade archived its two lessons and kept the Insight.
- Index check: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 62 lines.
  - `lesson-case-check-names-note-lists-hundreds-of-files` — no index line names the same cause; kept as a `create`.
  - `lesson-frontier-closer-appended-without-ticking-the-box` — near `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`: the same cause in another session (0141, L19), not the same page; kept as a `create` with `near`.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 62 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 16 lines.
  - `lesson-frontier-closer-appended-without-ticking-the-box` — joined `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone` under the new `insight-orchestration-frontier-closer-leaves-the-box-open`: in both the Edit that closes a Frontier line matched only the tail of the line, so the box stayed open. No Insight had this pattern; `insight-frontier-line-closed-by-the-case-built-on-its-item` is about why a line is closed, not how the box is written. Neither lesson entry carries `addressed_by`, so the Insight was born `open`.
  - `lesson-case-check-names-note-lists-hundreds-of-files` — none: its cause is the breadth of the names note of the hook of `rule-case-check`; no lesson or Insight line names how many notes or hits a check sends.
- Archive: `guppi archive` printed nothing, exit 0, and moved no unit. No `pending` Estimate's `method` names the archive step.

## Readings due

- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); method: by hand, after the first build of `case-guppi` whose Case proposes a `create` without a `ref` on the Render of `rule-ask` that runs every category.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: by hand, after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: by hand, after the first Case built under the Render that names a test over a live file and changes a reader and the text it reads.
- `estimate-case-build-reads-each-list-of-a-new-member` — `pending`; target `rule-case-build` (`draft`); read: line 163 of `vault/raw/2026-11-02/1548/spec.md`; method: by hand, after the first build of `case-guppi` in a later session whose Case adds a member to a list that texts spell out one by one.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — `pending`; target `rule-case-build` (`draft`); read: line 240 of `vault/archive/plugin/2026-11-01/2227/raw/spec.md`; method: by hand, after the `/pre-spec` of the first session whose `case-guppi` names in `context` each search for the folders of a new file, and in which a Case adds a file that is no page.
- `estimate-case-build-runs-the-vault-query-first` — `pending`; target `rule-case-build` (`draft`); method: by hand, after the first build on the Render that sets when the vault query runs, whose Case proposes a `create` without a `ref`.
- `estimate-case-build-searches-the-names-of-what-it-changes` — `pending`; target `rule-case-build` (`draft`); read: line 122 of `vault/raw/2026-11-02/1548/spec.md`; method: by hand, after the `/pre-spec` of the first session in which the hook of `rule-case-check` sends `case-guppi` a note on a file that names what its Case changes.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint, the person's answer.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: by hand, after the session whose Work Mode builds the setup skill of `rule-morph`.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); method: by hand, after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `pending`; target `rule-orchestration` (`draft`); read: line 94 of `vault/archive/plugin/2026-11-01/2227/raw/spec.md`; method: by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word, that reply in the transcript of its session.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: by hand, after the first batch of items taken up together under the Render in which a summary carries a line `Other Case`.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`; target `rule-plugin-install` (`draft`); deferred by Case 949; method: by hand, after the librarian's run of the session that sets this Criterion, three projects with `/guppi:install` from a local clean version. This run: no step of it printed a fact its method names.
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` — `pending`; target `rule-prespec` (`draft`); read: line 296 of `vault/archive/plugin/2026-11-01/2227/raw/spec.md`; method: by hand, after the first `/pre-spec` on the Render that holds the question on the readers of the folders of a new file, whose plan holds a Case that adds a file that is no page.
- `estimate-retro-loads-on-a-red-command` — `pending`; target `rule-retro` (`draft`); read: line 317 of `vault/raw/2026-11-02/1337/spec.md`; method: by hand, after the librarian's render that writes `.claude/skills/retro/SKILL.md` with `--exit-zero` on its lines Tests and Style, the text of that file and the first load of `/retro` after that render. This run: `guppi render` did not write `.claude/skills/retro/SKILL.md`; its lines 7 and 9 hold `guppi test --exit-zero` and `guppi style --exit-zero`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: by hand, after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); read: line 488 of `vault/archive/plugin/2026-11-01/2227/raw/spec.md`; method: `pytest .guppi/tests/test_ship.py`; by hand, after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` of a commit of `plugin`, before the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: by hand, in a session of `plugin` before its close, the clean version installed as a plugin in an empty project.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`, the output of `guppi check` and `git log -p -1` of that page. This run: the yaml holds no entry of `lesson-ledger-reading-writes-a-bare-wikilink`; `guppi check` printed no line, exit 0.
- `estimate-sprint-plugin-link-graph-is-gone` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); read: line 253 of `vault/raw/2026-11-02/0039/spec.md`; method: by hand, after the librarian's run that applies the delete of `entity-link-graph` and renders `.claude/settings.json`. This run: the yaml holds no delete of `entity-link-graph`; `guppi render` did not write `.claude/settings.json`; `guppi test` 1904 passed, 6 skipped, 1 deselected.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: by hand, a pull request from a second account read on GitHub, before the close of `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: by hand, the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of the sprint.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); method: by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`: the yaml and the brief. This run: neither lesson entry carries `addressed_by`; the synthesis put `lesson-frontier-closer-appended-without-ticking-the-box` under a new Insight born `open`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); read: line 270 of `vault/raw/2026-11-02/1337/spec.md`; method: by hand, after the librarian's render that writes `.claude/skills/work/SKILL.md` with `--exit-zero` on its lines Tests and Lint, `guppi render --check`, the text of that file and the first `/work` that loads after that render while `guppi check` exits 1. This run: `guppi render` did not write `.claude/skills/work/SKILL.md`; its lines 11 and 13 hold `guppi test --exit-zero` and `guppi check --exit-zero`; `guppi check` exits 0.

## Flags

- `near`: `lesson-frontier-closer-appended-without-ticking-the-box` near `lesson-orchestration-closes-a-frontier-line-by-its-closer-alone`; both clustered under `insight-orchestration-frontier-closer-leaves-the-box-open` by the synthesis.
- No entry `incomplete`, `failed` or `unparsed`. No `failed` Estimate. No MOC candidate named by a step of this run. No stale defer: the two live `deferred_by` (`rule-ratification` → `decision-case-907`, `estimate-plugin-install-sets-aside-the-files-of-the-project` → `decision-case-949`) name pages under `vault/wiki/decisions/`.
- `rule-case-build` and `rule-orchestration` carry `core: true` and `status: draft`; `guppi check` names neither after this run.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: the handoff says Cases 1005 and 1006 were ratified again after `/pre-spec`, and the context of Case 1006 names a reply that acknowledges them; whether that reply waits for the person's word is in the transcript of session 1548, which this run did not read. Its reading is listed under Work.
- Lint (`guppi check`): exit 0, no line.
- Reads the frame says the librarian's job does not need: none.

## Next session

Cases:
- C1: `guppi check` after this run exits 0 and names no core page in draft; the owner pushes `plugin` and a tag `prod-x.y.z`, and the session reads the CI run (handoff, For the next session).
- The breadth of the note of names (L11, `lesson-case-check-names-note-lists-hundreds-of-files`): whether the hook narrows what it notes, such as the paths of a task line that only imports a module, or names that hundreds of texts hold — a decision once the first real note is seen (handoff, For the next session).
- `estimate-synthesis-keeps-actioned-by-the-mark`: proposed to defer into `backlog.md`, since its event may not come for long (handoff, For the next session).
- W1 and W2 need a Work Mode run from the Claude Code CLI (handoff, For the next session).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: proposed to defer into `backlog.md`, since its session did not take its reading — it waits for the first `/work` that loads in the Claude Code CLI while `guppi check` exits 1 (handoff, Debt).
- `estimate-retro-loads-on-a-red-command`: proposed to defer into `backlog.md`, since its session did not take its reading — it waits for the first load of `/retro` in the Claude Code CLI (handoff, Debt).

Work:
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — an acknowledging reply after `/pre-spec` stands in session 1548 (handoff; Flags); read line 94 of `vault/archive/plugin/2026-11-01/2227/raw/spec.md`.

Ask the person:
- none

## Readings at the close

- `uv run --project .guppi guppi test`: 1904 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 0, no line.
- Pages under `vault/wiki/` (`*.md`): entities 5, rules 88, estimates 351, lessons 63, insights 17, decisions 518.
