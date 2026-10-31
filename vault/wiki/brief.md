# Brief — 2026-10-31, librarian of session 0128

## Where things stand

- Session 0128 of the sprint `plugin`. Cases ratified: 950 (950.1, 950.2), 952, 953, 954 (954.1, 954.2, 954.3), 955. Cases 950, 952, 953 and 954 were built again on the findings of `/pre-spec` and ratified again, 950 and 954 a third time on two findings of `guppi prespec --check`. Case 951 was dropped with no decision line (handoff).
- Code and tests: none changed. `guppi test` 1822 passed, 6 skipped, 1 deselected at the baseline, after the tasks and at Retro; `guppi style` clean (handoff).
- By hand in Work Mode: the test of Case 953, the Claude Code CLI in the empty folder `C:\tmp\plan-approval-test` with the plan text of `resilient-munching-peacock.md`; the approval was withheld in a standalone PowerShell window (120×30) and in the terminal of VS Code (330×16) (handoff).
- Readings: L14 `estimate-skill-sprint-open-asks-the-goal-as-an-open-question` `passed` (folded into the `create` of line 4), L15 `estimate-backlog-renders` `passed`. Lesson: L16 `lesson-plugin-cli-withholds-approval-in-every-window` (handoff, ledger).
- The person put off the sprint item of the clean branch again, the push of `plugin` with a tag `prod-x.y.z` and the read of the CI run, with no reason given (handoff).
- `guppi materialize` printed `written with 16 entries` for `vault/raw/2026-10-31/0128/materialize.yaml` and `extended with 0 entries` for the yaml of `2345`. The ledger has 16 lines (`wc -l`); the yaml holds 15 entries for lines 1–13, 15 and 16, and line 14 is folded into the entry of line 4, so every line is accounted for. Kinds: 9 `update`, 4 `create` (all estimates), 1 `estimate`, 1 `lesson`.
- The librarian added 3 entries by the synthesis (1 `create` of an Insight, 2 `update` of lessons) and 1 mark `near`.
- Marks: 28 `applied` lines (18 under `entries`, 10 under `decisions`); no entry `failed`, `incomplete`, `exists` or `merged`; `unparsed: []`.
- `guppi generate` printed 31 pages written or changed for `0128` and 0 for `2345`; nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `4 page(s) moved`, nothing on stderr. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr.
- Pages created (16), from `git status`: decisions 10 (`decision-case-950`, `950.1`, `950.2`, `952`, `953`, `954`, `954.1`, `954.2`, `954.3`, `955`); estimates 4 (`estimate-skill-sprint-open-asks-the-goal-as-an-open-question` `passed`, `estimate-orchestration-starts-ask-guppi-for-a-hook-test`, `estimate-guppi-keeps-no-defer-of-its-shape`, `estimate-ask-tries-a-decision-call-only-for-a-hook-trial`, the last three `pending`); lessons 1 (`lesson-plugin-cli-withholds-approval-in-every-window`); insights 1 (`insight-plugin-cli-withholds-approval-of-a-long-plan`, `open`, severity 2).
- Pages updated (11), from `git status`: rules 5 (`rule-skill-sprint-open`, `rule-spec-capture`, `rule-orchestration`, `rule-ask`, `rule-search-leaves-out-decisions`); estimates 4 (`estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-shows-the-built-case`, `estimate-search-leaves-out-decisions-refuses-ask-guppi`, `estimate-backlog-renders`); entities 1 (`entity-guppi`); lessons 1 (`lesson-plugin-cli-withholds-approval-of-a-long-plan`, `new → clustered`). With the 4 superseded Decisions, 16 created, 11 updated and 4 superseded make the 31 pages `generate` printed.
- Superseded and moved by `cleanup` to `vault/archive/plugin/2026-10-31/0128/decisions/`: `decision-case-616`, `decision-case-910`, `decision-case-934`, `decision-case-936`.
- Cascade (log): `entity-guppi` `built → draft`.
- Render wrote `.claude/skills/sprint-open/SKILL.md` (Case 952), `vault/wiki/orchestration.md` (Case 954.2), `.claude/agents/ask-guppi.md` and `.claude/rules/search-leaves-out-decisions.md` (Case 954.3). `backlog.md` went from 8 items to 5: `entity-guppi`, `rule-skill-sprint-open`, `rule-spec-capture` and `estimate-search-leaves-out-decisions-refuses-ask-guppi` left it, and `insight-plugin-cli-withholds-approval-of-a-long-plan` entered it as an open Insight.
- This run ticked 18 boxes of `vault/raw/2026-10-31/0128/spec.md` (14 page lines, 4 render lines, and the `read` box of L14 among them); the handoff named 18 boxes waiting. 6 `read` boxes stay unticked.
- The handoff's instructions, checked: the four pages `rule-skill-sprint-open`, `rule-spec-capture`, `estimate-search-leaves-out-decisions-refuses-ask-guppi` and `entity-guppi` carry no `deferred_by` after generate; both `old` texts of Case 954.3 for `rule-ask` stood on the page before generate (lines 37 and 49) and both replaces applied (log); the four renders due were written.
- Index check: the 4 `create` entries are Estimates and have no index. The `lesson` entry was compared, as the handoff asked, by `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (55 lines): it is near `lesson-plugin-cli-withholds-approval-of-a-long-plan` and not the same page, since it records a test that rules out the window and any hook of GUPPI, while the old page records the plan file of whole Cases as the way GUPPI meets the limit.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 55 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 12 lines.
  - `lesson-plugin-cli-withholds-approval-in-every-window` — joined `lesson-plugin-cli-withholds-approval-of-a-long-plan` under the new `insight-plugin-cli-withholds-approval-of-a-long-plan`: both blame the Claude Code CLI, which withholds the approval of a plan above the size it can show; no Insight index line held that pattern.

## Readings due

- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — `pending`; target `rule-search-leaves-out-decisions` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-31/0128/spec.md` (Case 954.1): after the librarian's run that renders `orchestration.md`, `ask-guppi.md` and `search-leaves-out-decisions.md`, `test_grepguard.py`, and the trial in the Work Mode of the session whose brief puts this reading under Work. This run: `guppi render` wrote `vault/wiki/orchestration.md`, `.claude/agents/ask-guppi.md` and `.claude/rules/search-leaves-out-decisions.md` (`git status`); the page carries no `deferred_by`.
- `estimate-orchestration-starts-ask-guppi-for-a-hook-test` — `pending`; target `rule-orchestration` (`draft`); read by its unticked `read` box in the 0128 Spec (Case 954.2): after the librarian's run that renders `orchestration.md`, the Agent calls of the main agent in the same trial. This run: `guppi render` wrote `vault/wiki/orchestration.md`.
- `estimate-ask-tries-a-decision-call-only-for-a-hook-trial` — `pending`; target `rule-ask` (`draft`); read by its unticked `read` box in the 0128 Spec (Case 954.3): after the librarian's run that renders `ask-guppi.md` and `search-leaves-out-decisions.md`, the calls and the answer of `ask-guppi` in the same trial. This run: `guppi render` wrote `.claude/agents/ask-guppi.md` and `.claude/rules/search-leaves-out-decisions.md`.
- `estimate-guppi-keeps-no-defer-of-its-shape` — `pending`; target `entity-guppi` (`draft`); read by its unticked `read` box in the 0128 Spec (Case 955): after the librarian's run that applies the Case, `entity-guppi.md` and `backlog.md` read against the Criterion. This run: generate applied Case 955; `entity-guppi` carries no `deferred_by` line; the `## Deferred` of `backlog.md` holds no line for `entity-guppi`; the diff of `entity-guppi` changes no line of its `## Purpose`.
- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); method: after a librarian's run whose `librarian-guppi.md`, when the run starts, holds the Render of `rule-close` that writes `report.md`, that `report.md` read by `git show` against the Criterion. This run: it started on the frame that writes `report.md` (rendered by the commit `ea453e4b`); its close writes `vault/raw/2026-10-31/0128/report.md` after this brief and commits it.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — `pending`; target `rule-case-build` (`draft`); method: after the `/pre-spec` of the first session whose `case-guppi` runs on the Render of `rule-case-build` that holds the sentence on a new member of a list, the findings of `ask-guppi` at that `/pre-spec` read, the count in the estimate line.
- `estimate-where-to-stop-writes-each-step-whole` — `pending`; target `rule-where-to-stop` (`draft`); method: after the first stop of Work Mode under the new text of `vault/wiki/where-to-stop.md` whose reply asks the person to run commands by hand, that reply read against each line of the Criterion.
- `estimate-case-build-reads-each-list-of-a-new-member` — `pending`; target `rule-case-build` (`draft`); read by its unticked `read` box in the 0128 Spec (Case 950.1): after the `/pre-spec` of the first session on the Render with the sentence on a new member of a list whose plan holds a Case that adds a member to a list.
- `estimate-orchestration-shows-the-built-case` — `pending`; target `rule-orchestration` (`draft`); read by its unticked `read` box in the 0128 Spec (Case 950.2): after the first summary of `case-guppi` in Plan Mode with a line `Other Case` naming a Case of the session, in a session that opens on the Render of `rule-orchestration` that lets the main agent start `ask-guppi` in Work Mode for a hook test.
- `estimate-orchestration-names-related-cases-in-the-dispatch` — `pending`; target `rule-orchestration` (`draft`); method: after the first dispatch of `case-guppi` under the new Render in which a Case of the session sets the form of a text a check reads and the Case of the item may write text of that kind.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch of items taken up together in Plan Mode under the new Render in which a summary carries a line `Other Case` naming a Case of the session.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `pending`, `deferred_by: decision-case-949`; target `rule-plugin-install` (`draft`); method: after the librarian's run of the session that sets this Criterion, with a tag `prod-x.y.z`, installs into three projects with files of their own. This run: `backlog.md` lists the Estimate.
- `estimate-morph-takes-in-the-set-aside-files` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph` and its step in `/hi`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph`, its step in `/hi` and in `/sprint-open`.
- `estimate-ask-query-before-a-create` — `pending`; target `rule-ask` (`draft`); method: after a `case-guppi` builds a Case with a `create` without a `ref` on the rendered `.claude/agents/ask-guppi.md`.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `pending`; target `rule-synthesis` (`draft`); method: after a librarian's run that puts a lesson with `addressed_by` under an `actioned` Insight. This run: the `lesson` entry carries no `addressed_by`; the synthesis put it under a new Insight that stands `open`.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes a reader in code and the text it reads.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); method: after a session whose ledger holds a lesson with the Case that closes its cause, a Case taking up a decision with more than one Case in `deferred_by`, and a lesson line declaring a new tag.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); method: after the first `/work` on the rendered skill in which a Case is ratified in Work Mode.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint, at the reply that acknowledges the opening Case of `/sprint-open`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` whose merge of main leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged into main by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: `test_ship.py`, then after a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: in a session of the sprint before its close, a clean copy installed in an empty project and `/hi` typed.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: the person's answer on `README.md` at the `/hi` after the session that writes it, before the close of the sprint.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`, the live sprint page); method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.

## Flags

- `near`: the `lesson` entry `lesson-plugin-cli-withholds-approval-in-every-window` (line 16) carries `near: lesson-plugin-cli-withholds-approval-of-a-long-plan`. No entry marked `incomplete`, `failed` or `unparsed`.
- No Estimate stands `failed`.
- `guppi check`: 13 lines, exit 1, each a page with `core: true` that stands `draft`: `entity-guppi`, `entity-sprint`, `rule-ask`, `rule-case-build`, `rule-close`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-search-leaves-out-decisions`, `rule-skill-hi`, `rule-synthesis`, `rule-where-to-stop`, `rule-work-mode`. `entity-guppi` entered the list by the cascade of this run (`built → draft`, Case 955 added `estimate-guppi-keeps-no-defer-of-its-shape`). The line `backlog: vault/wiki/backlog.md differs from its sources`, which the handoff counted at the baseline, is gone.
- `backlog.md` holds 5 items, not the 4 the handoff expected: the fifth is the open Insight `insight-plugin-cli-withholds-approval-of-a-long-plan` that this run's synthesis created.
- Stale defer: `rule-work-mode` is put off in 31 sessions (`backlog.md`).
- `estimate-case-build-reads-the-readers-of-a-changed-step`: the Render it waits for reached `.claude/agents/case-guppi.md` by the commit `ea453e4b`, before session 0128, and the handoff reports the `/pre-spec` of 0128 (eleven findings of `ask-guppi`); the ledger of 0128 holds no `estimate` line for it, and `## Debt` of the handoff does not name it.
- `estimate-where-to-stop-writes-each-step-whole`: the new `vault/wiki/where-to-stop.md` was rendered by the commit `ea453e4b`, before session 0128, and the handoff reports a test of Case 953 that the person ran by hand in Work Mode; the ledger of 0128 holds no `estimate` line for it, and `## Debt` of the handoff does not name it.
- `estimate-orchestration-signs-items-taken-together`: the handoff reports a summary of Case 954 with a line `Other Case` naming Case 950 and does not say whether the items were taken up together as a batch; the reading stays in Readings due alone.
- Handoff observation: finding 6 of `/pre-spec` on Case 953 stands open by the person's choice.
- No MOC candidate and no contradiction found.
- No read outside the frame.

## Next session

### Cases

- The bug of the approval of a long plan: the test shows the Claude Code CLI withholds it in any window, while the VS Code extension approves it; a Case decides the fix, such as a shorter plan file, an approval in the chat, or the extension as the way to approve a Spec (handoff `## For the next session`; `insight-plugin-cli-withholds-approval-of-a-long-plan`).
- The sprint item of the clean branch stays open: the push of `plugin` with a tag `prod-x.y.z` and the read of the CI run (handoff `## For the next session`).

### Work

- `estimate-search-leaves-out-decisions-refuses-ask-guppi`
- `estimate-orchestration-starts-ask-guppi-for-a-hook-test`
- `estimate-ask-tries-a-decision-call-only-for-a-hook-trial`
- `estimate-guppi-keeps-no-defer-of-its-shape`
- `estimate-close-reports-the-run`
- `estimate-case-build-reads-the-readers-of-a-changed-step`
- `estimate-where-to-stop-writes-each-step-whole`

### Ask the person

- none

## Readings at the close

- `uv run --project .guppi guppi test`: 1822 passed, 6 skipped, 1 deselected, exit 0.
- `uv run --project .guppi guppi check`: 13 lines, exit 1 (above).
- Pages under `vault/wiki/`: decisions 424, entities 5, estimates 332, insights 13, lessons 56, rules 86. Pages under `vault/archive/`: 3078 after `guppi archive` (3063 before it); `guppi archive` moved `raw/2026-10-30/2345` to `archive/plugin/2026-10-30/2345/raw`, and the folder of 0128 stays.
