# Brief — 2026-10-28, librarian of session 1907

## Where things stand

- Session 1907 of the sprint `plugin`. Cases ratified: 892, 893 (893.1, 893.2), 894 (894.1, 894.2, 894.3), 895 (handoff).
- Code: `.guppi/guppi/ratified.py` (`guard` writes a call of `case-guppi` on its case file itself by `builder_write` and `builder_file`, logs `ratified wrote`, exits 2; `held_number` returns its refusal with whether it judged), `.guppi/guppi/ship.py` (`VAULT_IGNORE` taken into the copy), `vault/.gitignore` (new), `.gitignore` (the event-log lines removed). Tests in `test_ratified.py` (9 new tests of the write), `test_ship.py` (one new test), `test_casecheck.py`, `test_caseid.py`. `guppi test` 1790 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- The test of Case 895 ran by `claude -p` 2.1.301 in the session's temporary area, three runs, about 2.4 USD (handoff).
- Readings L13–L19: six `passed`, `estimate-case-build-goes-on-after-a-compaction` `failed`. Lessons L20–L22: one `knowledge`, two `error` (handoff, ledger).
- `guppi materialize` printed `written with 22 entries` for `vault/raw/2026-10-28/1907/materialize.yaml` and `extended with 0 entries` for the yaml of `0118`. The ledger has 22 lines; the yaml holds 21 ledger entries (lines 1–22 but 19, the `failed` reading of the new Estimate, folded into its `create` entry of line 12) and 9 items under `decisions`, so every ledger line is accounted for. Kinds: 10 `update` (4 rules, 6 estimates), 1 `create` (estimate), 1 `defer` (rule, marked `exists`), 6 `estimate`, 3 `lesson`. The librarian added 3 entries (synthesis). All entries are marked `applied`; none `failed`, `incomplete`, `near` or `merged`.
- Pages created (14): decisions 9 (`decision-case-892`, `893`, `893.1`, `893.2`, `894`, `894.1`–`894.3`, `895`); estimates 1 (`estimate-case-build-goes-on-after-a-compaction`, `failed` by its folded reading); lessons 3 (`lesson-case-build-subagent-compaction-fires-below-its-window`, `lesson-hooks-guard-broken-mid-edit-of-its-own-contract`, `lesson-prespec-ask-guppi-opened-a-decision-outside-its-frame`, the last `clustered`); insights 1 (`insight-ask-guppi-reads-a-decision-outside-its-frame`, `open`, severity 2).
- Pages updated (16): rules 4 (`rule-clean-branch` — replace, put off again by 893.1; `rule-spec-reconcile`; `rule-permissions` — replace, `built → draft` by the cascade; `rule-case-build` — replace, Estimate 895 added); estimates 8 (`estimate-clean-branch-code-holds-pointers-only-in-brackets`, `estimate-clean-branch-writes-a-clean-copy`, `estimate-spec-reconcile-refuses-an-edit-of-the-plan`, `estimate-case-build-writes-the-case` — Criterion replaced and read `passed`; `estimate-permissions` — Criterion replaced, `pending`; `estimate-clean-branch-ships-neutral-texts` — put-off taken up by 893.2, `method` set, `failed` kept; `estimate-case-build-reads-no-sibling-file-mid-send`, `estimate-orchestration-rechecks-a-sibling-after-a-joint-send` — `pending → passed`); lessons 1 (`lesson-ask-guppi-read-a-decision-page-without-a-reason`, clustered); decisions 3 (`decision-case-882.3` superseded by 893.1 and `decision-case-891` superseded by 893.2, both archived; `decision-case-882` lost the child 882.3). `guppi generate` printed 29 pages for `1907` and 0 for `0118`, nothing on stderr; the yaml of `0118` gained `superseded_by: ['893.2']` on its two entries of Case 891 and `superseded_by: [decision-case-893.2]` on its record of 891.
- The handoff's instructions, checked: `rule-clean-branch` carries `deferred_by: [decision-case-893.1]` and `guppi backlog` lists it (put off in 9 sessions). `estimate-spec-write-writes-a-defer` keeps `deferred_by: [decision-case-885, decision-case-891]` and `guppi backlog` lists it (put off in 4 sessions). `estimate-clean-branch-ships-neutral-texts` lost `deferred_by` and is gone from `backlog.md`. `guppi render` changed `.claude/agents/case-guppi.md` alone; `.claude/settings.json` stands unchanged.
- This run ticked 18 boxes of `vault/raw/2026-10-28/1907/spec.md`; one task line stays unticked: `read estimate-permissions`. No `guppi sprint-close --apply` line stands in the Spec.
- `guppi cleanup` printed `2 page(s) moved`: `decision-case-882.3` and `decision-case-891`, into `vault/archive/plugin/2026-10-28/1907/decisions/`. `guppi render` printed nothing. `guppi sprint` changed one line of `vault/wiki/sprint.md`: the milestone line of `rule-clean-branch` names `decision-case-893.1` in place of `decision-case-882.3`. `guppi backlog`: 17 items → 17 (`estimate-clean-branch-ships-neutral-texts` gone; `insight-ask-guppi-reads-a-decision-outside-its-frame` added). `guppi glossary` left `vault/wiki/glossary.md` unchanged.
- `guppi archive` printed `raw/2026-10-26/0118 → archive/plugin/2026-10-26/0118/raw`; `raw/2026-10-28/1907` is the session of the run and stays; `raw/2026-10-14/1907` holds no `ledger.md` (only `cases/` and `frontier.md`), so it is no unit.
- Index check: the one `create` entry is an Estimate, so no Grep of the index check ran.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 46 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 9 lines.
  - `lesson-case-build-subagent-compaction-fires-below-its-window` — none: no index line states when Claude Code compacts a subagent or what the compaction hooks carry; the lines of `SubagentStop` speak of its payload and the handback, and `lesson-case-build-agent-context-grows-on-every-resume` of the growth of the context on a resume.
  - `lesson-hooks-guard-broken-mid-edit-of-its-own-contract` — none: `insight-workflow-code-live-before-the-page-it-reads` is about code that runs before the page or file it reads lands; this lesson is about two functions of the guard changed in two steps, with no page in between.
  - `lesson-prespec-ask-guppi-opened-a-decision-outside-its-frame` — joined `lesson-ask-guppi-read-a-decision-page-without-a-reason` in the new Insight `insight-ask-guppi-reads-a-decision-outside-its-frame`: both are `ask-guppi` at `/pre-spec` reading a Decision page for a reason its frame does not name.

## Readings due

- `estimate-case-build-goes-on-after-a-compaction` (failed) — `rule-case-build` (draft) — result (2026-10-28, Work Mode): the helper compacted at preTokens 72126, 74307 and 75012 with `autoCompactWindow: 100000`, so the first Then line (a `compact_boundary` after it passes 100000 tokens) is not shown; the other lines hold. Read by its `method`: by hand, in the Work Mode of the session that creates it, the test by `claude -p`.
- `estimate-clean-branch-ships-neutral-texts` (failed) — `rule-clean-branch` (draft) — result (2026-10-17, /hi of 1805): `guppi ship --allow-draft` exit 0; it fails on sentences true only in the repository of GUPPI. Read by its `method`: by hand, after the librarian's run of session 1907, with a tag `prod-x.y.z` in the history of HEAD: `guppi ship --allow-draft` into an empty folder, each sentence read whole. This run: no step ran `guppi ship`; `git tag --merged HEAD` prints `prod-0.2.0`, `prod-1`, `prod-2`; the commit of this run comes after this brief.
- `estimate-permissions` (pending) — `rule-permissions` (draft) — read by the unticked `read estimate-permissions` of the Spec of 1907; its `method`: the rendered allow list and `test_render.py`, then by hand after the first Case file `case-guppi` writes in Plan Mode of a later session, the person's word.
- `estimate-close-commits` (pending, `deferred_by` case 885) — `rule-close` (draft) — by its `method`: `test_render.py -k paths`, then by hand after the librarian's run of the next session whose `.claude/agents/librarian-guppi.md` holds the new Render of `rule-close`: `git log`, `git status` and the report. This run: `guppi render` changed `.claude/agents/case-guppi.md` alone; the close commit of this run comes after this brief.
- `estimate-clean-branch-writes-the-session-files` (pending, `deferred_by` case 885) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py -k skeleton`, then by hand after the librarian's run of the session that set the `method`, with a tag `prod-x.y.z`: an install in an empty folder with no git. This run: no install.
- `estimate-git-context-offers-git-init` (pending, `deferred_by` case 862) — `rule-git-context` (draft) — by its `method`: by hand after the librarian's run, an install into an empty folder with no git, `/hi` three times. This run: no install.
- `estimate-plugin-install-offers-to-install-uv` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by its `method`: after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install from a terminal with no `uv`. This run: no install.
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (pending, `deferred_by` case 862) — `rule-plugin-install` (draft) — by its `method`: after the librarian's run of the session that set the Criterion, with a tag `prod-x.y.z`: an install offline with an empty cache of `uv`. This run: no install.
- `estimate-guppi-package-is-ready-after-the-install` (pending, `deferred_by` case 862) — `rule-guppi-package` (draft) — by its `method`: after a tag `prod-x.y.z`, an install in an empty project with `uv`, `/hi`, and the person's answer.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` (pending) — `rule-case-build` (draft) — by its `method`: after the first Case built under the Render of `rule-case-build` that names a test over a live file; not seen in the handoff or the ledger of 1907.
- `estimate-orchestration-shows-the-built-case` (pending) — `rule-orchestration` (draft) — by its `method`: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` under the new Render; not seen in the handoff or the ledger of 1907 (the handoff names a `Sibling` line).
- `estimate-orchestration-signs-items-taken-together` (pending) — `rule-orchestration` (draft) — by its `method`: after the first batch taken up together in Plan Mode in which a summary carries a line `Other Case`; not seen in the handoff or the ledger of 1907.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — by its `method`: after the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by its `method`: after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen in the ledger of 1907.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` that leaves a conflicted page; not seen.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`; not seen.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered skill in which a Case is ratified in Work Mode; not seen in the handoff or the ledger of 1907.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — by its `method`: a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` of a commit of `plugin`, before the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — by its `method`: in a session of `plugin` before its close, an install of the clean version into an empty project.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — by its `method`: a pull request from a second account, before the close of `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer on `README.md` at the `/hi` after the session that writes it.

## Flags

- No entry is marked `incomplete`, `failed`, `near` or `unparsed`.
- Failed Estimates: `estimate-case-build-goes-on-after-a-compaction`, `estimate-clean-branch-ships-neutral-texts`.
- `estimate-clean-branch-ships-neutral-texts` stands `failed`: Case 893.2 set its `method` and took its put-off up, and set no `status`.
- `estimate-spec-write-writes-a-defer` keeps `decision-case-891` in its `deferred_by`; `decision-case-891` is now `superseded` and under `vault/archive/plugin/2026-10-28/1907/decisions/` (handoff: as the context of Case 893.2 says).
- MOC candidates: none seen.
- Stale defers (`backlog.md`): `rule-work-mode` put off in 31 sessions, `rule-clean-branch` in 9, `rule-orchestration` in 8, `estimate-spec-write-writes-a-defer` in 4.
- Contradictions: none seen.
- Lint (`guppi check`, exit 1, 14 lines): 11 lines `status: a page with core: true that is draft` (`entity-sprint`, `rule-case-build`, `rule-close`, `rule-git-context`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-permissions`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode`); `estimate-case-build-goes-on-after-a-compaction: unread: failed`; `estimate-clean-branch-ships-neutral-texts: unread: failed`; `estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`.
- Read the frame says the job does not need: `git diff` of `vault/raw/2026-10-26/0118/materialize.yaml`, the earlier yaml, for the facts of Where things stand on what this run left on disk (`git status` named it modified).
- Read the frame says the job does not need: `git diff` of `vault/wiki/decisions/decision-case-882.md` (its `children` line and one History line), for the count of pages updated per category in Where things stand.

## Next session

### Cases

- The procedure for a full `case-guppi`, put off on `rule-orchestration` by Case 884, can be built from lesson L20 (`lesson-case-build-subagent-compaction-fires-below-its-window`); `estimate-case-build-goes-on-after-a-compaction` stands `failed` on its first Then line until a Case replaces that line with what the test showed (handoff, For the next session).
- Whether a `Read` before the next `Edit` is enough after the guard wrote a case file is seen at the first build of a Case in Plan Mode; a refusal of Claude Code ("modified since read") there would need a Case on `rule-case-build` (handoff, For the next session).
- `estimate-clean-branch-ships-neutral-texts` stands `failed`; its `method` waits for the librarian's run of session 1907 with a tag `prod-x.y.z` in the history of HEAD, and `prod-0.2.0` stands there.

### Work

- none

### Ask the person

- `estimate-permissions` — needs the person — In the next Plan Mode, after the librarian's render, does Claude Code ask you anything when `case-guppi` writes or edits its Case file, and does it ask at a Grep of a subagent on the folder of the saved transcripts and on a file under it?
- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?

## Readings at the close

- `uv run --project .guppi guppi test`: 1790 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: 14 lines (exit 1), as in Flags.
- Pages under `vault/wiki/`: decisions 307, entities 5, estimates 312, insights 10, lessons 49, rules 86; files under `vault/archive/`: 2902 `.md`, after `guppi archive`.
