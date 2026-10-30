## Case 934 — The long-plan approval in the CLI is put off as a bug with a test

> **context:**
> At the end of Plan Mode the main agent calls `ExitPlanMode`, Claude Code shows the plan file and the person approves it in a dialog; the hook of `rule-spec-capture` then copies the plan into `spec.md` of the session folder. `decision-case-909` put off `rule-spec-capture` with the item of letting a Spec be approved in the Claude Code CLI, since `lesson-plugin-cli-withholds-approval-of-a-long-plan` records that a plan of 15347 bytes was not approved there, while a plan of 58861 bytes was approved in the VS Code extension. The lesson gives the cause as the CLI. Its source is the transcript of the test install, where the text of the refusal stands in line 870 as a user message, not as output of Claude Code. The person thinks the cause is the terminal, since the test install ran in a standalone PowerShell window and not in the terminal of the editor, and chose to keep the approval as it is and to put the item off again as a bug, with a test that finds the cause.
>
> The documentation of Claude Code names no size limit of a plan. `case-guppi` read https://code.claude.com/docs/en/permission-modes, which says that Shift+Tab leaves Plan Mode without approving a plan and that Ctrl+G opens the plan in a text editor, and names no limit. It read https://code.claude.com/docs/en/settings-reference, whose index names three settings of plans, `plansDirectory`, `useAutoModeDuringPlan` and `showClearContextOnPlanAccept`, none of them on the size shown. It read https://code.claude.com/docs/en/env-vars, which names no variable on plan approval. It read the first 100 000 of 1 120 755 characters of the changelog of Claude Code, at https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md, which hold three fixes of the plan approval screen and none on its size; the rest was not read. So whether the fault lies in Claude Code or in the terminal is not known, and the test of this item is what settles it.
>
> The Case writes one `defer` of `rule-spec-capture` with the new item and carries `{supersedes:case 909}`, the form Case 876 used to move a defer. `case-guppi` read `defer`, `clear_deferred_by` and `decision` of `.guppi/guppi/generate.py` whole: `decision` sets `decision-case-909` `superseded` and calls `clear_deferred_by`, which drops only `decision-case-909` from the `deferred_by` of each page in its `defer` list that a line of this Case names, and `defer` adds the new Decision page to the `deferred_by` of `rule-spec-capture` when it is not there; so the page keeps one defer, the new one, whichever runs first. The line of `vault/wiki/backlog.md` shows the `purpose` of the page, by the Criterion of `estimate-backlog-renders`, so the text of the bug stands under `## Deferred` of the Decision page of this Case, which the session that takes up the item reads through `deferred_by`. The governing rule is `rule-backlog`, whose Purpose prevents a deferred item from dropping out of sight; the item stays on the list.
>
> `lesson-plugin-cli-withholds-approval-of-a-long-plan` stands as it is: it records what was seen, and its cause is the guess the test checks. The text of `rule-spec-capture` does not change, so neither of its Estimates is touched. No new Estimate is created, by the person's answer: `estimate-backlog-renders` already checks that `backlog.md` holds one line per live page with a `deferred_by` that is not empty; its Criterion speaks of that mechanism and of no single page, so it stands. The session's ledger holds no `error` lesson, so no line of this Case carries an `addresses` mark.

> **problem:**
> The item of `rule-spec-capture` asks how GUPPI approves a Spec too long for the CLI, but the cause of the refusal is not known, and the person wants the approval kept as it is until a test shows whether Claude Code or the terminal is at fault.

> **recommend:**
> - **How the person approves a long Spec in the CLI**
>   - Recommended: (a) the person approves in the chat, and the hook before `ExitPlanMode` answers it with allow, so no dialog opens.
>   - Answer: none of the options; keep the approval as it is, with the dialog of `ExitPlanMode` and the plan file unchanged; the cause is likely the terminal, since the test ran in a standalone PowerShell window and not in the terminal of the editor; rewrite the item as a bug with a test that finds the cause.
> - **What the test compares**
>   - Recommended: (a) one plan of the size that failed, approved in a standalone PowerShell window and in the terminal of VS Code, the size of each window and whether the dialog opened noted, the result recorded by a lesson line.
>   - Answer: agreed, (a).
> - **How this Case is checked**
>   - Recommended: (a) by `estimate-backlog-renders`, with no new Estimate.
>   - Answer: agreed, (a).

> **given:**
> `rule-spec-capture`: the rule of the approved Spec, put off again with the bug and its test.
> **＋** `decision-case-909`: the Decision page of the earlier item, superseded.
> **＋** `lesson-plugin-cli-withholds-approval-of-a-long-plan`: the record of the refusal in the CLI.
> **＋** `vault/wiki/backlog.md`: the list of put-off items that `guppi backlog` writes.
> **＋** `estimate-backlog-renders`: the check of the lines of `backlog.md`.
> **＋** `rule-backlog`: the rule that no put-off item drops out of sight.

> **when:**
> The librarian runs `uv run --project .guppi guppi generate` and then `uv run --project .guppi guppi backlog` over the Spec that holds this Case.

> **then:**
> `vault/wiki/backlog.md` holds a line for `rule-spec-capture`.
> **＋** The `deferred_by` of `rule-spec-capture` names the Decision page of this Case and not `decision-case-909`.
> **＋** The Decision page of this Case holds under `## Deferred` the bug and the test that compares a standalone PowerShell window with the terminal of VS Code.
> **＋** `decision-case-909` stands `superseded` or `archived`.
> **－** The text of `rule-spec-capture` and the page `lesson-plugin-cli-withholds-approval-of-a-long-plan` do not change.

> **tasks:**
> - [ ] defer `rule-spec-capture`
>   - type: `rule`
>   - purpose: `Bug: approval of a long plan is withheld in the Claude Code CLI, and the cause is not known: the Claude Code CLI or the terminal it runs in, since the refusal was seen in a standalone PowerShell window, with a plan of 15347 bytes, and the approval of a long plan stays as it is until the cause is known. Test: approve by ExitPlanMode one plan of that size in a standalone PowerShell window and in the terminal of VS Code, note the size of each window and whether the approval dialog opened, and record the result by a lesson line, so that the Case that fixes the bug knows where the fault lies (lesson-plugin-cli-withholds-approval-of-a-long-plan; moved here from the defer of case 909)`

> **ratification:**
> ```
> - decision[case 934][defer][rule-spec-capture]{ref:rule-spec-capture}{supersedes:case 909}
> ```
