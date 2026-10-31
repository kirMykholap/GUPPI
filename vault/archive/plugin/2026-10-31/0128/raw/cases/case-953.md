## Case 953 — The test of the approval of a long plan runs in this session

> **context:**
> At the end of Plan Mode the agent calls `ExitPlanMode`, Claude Code shows the plan file, and the person approves it in a dialog. In install A of session 0327 the Claude Code CLI refused the plan file `resilient-munching-peacock.md`, of 15347 bytes, as too large to show in full, while a longer plan was approved in the VS Code extension; `lesson-plugin-cli-withholds-approval-of-a-long-plan` records it. Case 934 kept the approval as it is and put the item off as a bug with a test that finds the cause: the Claude Code CLI or the standalone PowerShell window it ran in. The `deferred_by` of `rule-spec-capture` names only `decision-case-934`, whose `## Deferred` holds that test. This Case runs the test in the Work Mode of this session and retires the defer; the text of `rule-spec-capture` does not change, so its update carries only `change` and the mark `{supersedes:case 934}`, as `case-schema.md` sets it for a deferred decision taken up. The test runs in an empty folder with no GUPPI, since `.claude/settings.json` of this repository and of `C:\tmp\guppi-0327-a` both register `guppi prespec` on `PreToolUse` of `ExitPlanMode`, a hook that runs before the dialog opens; a Glob found the plan file that failed still at `C:\Users\kir\.claude\plans\resilient-munching-peacock.md`, so the test shows the same text. The Case is checked by `estimate-backlog-renders`, whose Criterion stands: it checks that `vault/wiki/backlog.md` lists a page under `## Deferred` only while its `deferred_by` is not empty, and the defer retired here takes the item off that list at the librarian's run; its `method` runs `.guppi/tests/test_backlog.py` over a made-up vault, whose `test_a_page_without_deferred_by_and_an_insight_not_open_are_no_items` asserts that a page with no `deferred_by` is no item, so a task runs that test in this session, and the live `vault/wiki/backlog.md` is left to the librarian's run (finding 8 of `/pre-spec`). The `root_cause` of `lesson-plugin-cli-withholds-approval-of-a-long-plan` already blames the Claude Code CLI, so the new lesson line records the result as a new fact under a slug that names what the test found, and the index check of `rule-index-check`, which compares the `root_cause` of each new lesson with the lessons that stand, judges at the librarian's run whether it repeats that page (finding 6 of `/pre-spec`). Neither `estimate-spec-capture-appends` nor `estimate-spec-capture-offers-the-fork` speaks of the approval dialog, so both stand. A Grep of the session's ledger for `lesson\[error\]` and for `\{addresses:` printed nothing, so this Case closes no lesson of the session.

> **problem:**
> The approval of a long plan is withheld in the Claude Code CLI, and nobody knows whether Claude Code or the terminal is at fault, so no Case can fix it yet.

> **recommend:**
> - **What to do with the deferred item**
>   - Recommended: (a) run the test in this session's Work Mode, by hand, its result recorded by a lesson line.
>   - Answer: agreed, (a).
> - **Where the test runs, and with which plan**
>   - Recommended: (b) in an empty folder with no GUPPI, with the text of the plan that failed.
>   - Answer: agreed, (b).
> - **How this Case is checked**
>   - Recommended: (a) by `estimate-backlog-renders`, with no new Estimate.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: finding 6 of `/pre-spec`: name the lesson of the first failure in `given`, and record the result as a new fact under a slug that names what the test found, the librarian's index check judging a duplicate.
>   - Taken: `given` names the lesson and `rule-index-check`; the `then` line and the lesson task say so.
> - **Change**
>   - Asked: finding 8 of `/pre-spec`: the `then` states what `.guppi/tests/test_backlog.py` checks, and a task runs that test.
>   - Taken: the `then` line names the test over a made-up vault, and a task runs it against `estimate-backlog-renders`.

> **given:**
> `rule-spec-capture`: the page whose defer this Case retires.
> **＋** `C:\Users\kir\.claude\plans\resilient-munching-peacock.md`: the plan text that the Claude Code CLI refused.
> **＋** `estimate-backlog-renders`: the check that the item leaves the backlog.
> **＋** `vault/wiki/backlog.md`: the list of deferred items, written by `guppi backlog`.
> **＋** `.guppi/tests/test_backlog.py`: the test that `estimate-backlog-renders` runs.
> **＋** `lesson-plugin-cli-withholds-approval-of-a-long-plan`: the lesson of the first failure, whose `root_cause` blames the Claude Code CLI.
> **＋** `rule-index-check`: the librarian's check that a new page is no second page of a fact.

> **when:**
> The person starts the Claude Code CLI in a new empty folder with no GUPPI, once in a standalone PowerShell window and once in the terminal of VS Code, and in each the agent writes the text of `C:\Users\kir\.claude\plans\resilient-munching-peacock.md` into its plan and calls `ExitPlanMode`.

> **then:**
> For each window the person reports whether the approval dialog opened, and the size of the window in columns and rows.
> **＋** One lesson line in the ledger of this session records both results as a new fact, under a slug that names what the test found, beside `lesson-plugin-cli-withholds-approval-of-a-long-plan`; the index check of `rule-index-check` at the librarian's run judges whether it repeats that page.
> **＋** The defer of `rule-spec-capture` is retired; over a made-up vault, `.guppi/tests/test_backlog.py` shows that `vault/wiki/backlog.md` lists a page under `## Deferred` only while its `deferred_by` is not empty.
> **－** The approval of a plan in GUPPI and the text of `rule-spec-capture` do not change.
> **－** No hook of GUPPI runs in the empty folder.

> **tasks:**
> - [ ] update `rule-spec-capture`
>   - change: `the deferred test of the approval of a long plan taken up and run by hand`
> - [ ] stop: by hand, the person runs the test of `when` in a standalone PowerShell window and in the terminal of VS Code, and reports for each whether the approval dialog opened and the size of the window.
> - [ ] The main agent writes one `knowledge` lesson line with both results and its `source`, under a slug that names what the test found, so that the Case that fixes the bug knows where the fault lies.
> - [ ] `uv run --project .guppi pytest .guppi/tests/test_backlog.py`: read against `estimate-backlog-renders`.

> **ratification:**
> ```
> - decision[case 953][update][rule-spec-capture]{ref:rule-spec-capture}{supersedes:case 934}
> ```
