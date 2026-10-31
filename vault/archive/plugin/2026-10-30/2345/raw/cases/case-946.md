## Case 946 — The moved facts stand as the code bears them out

> **context:**
> Case 942.1 removed `## How it works` from each Leaf of `vault/wiki/rules/` and moved its facts into the docstrings of the code. The agent of session 2005 found two facts that do not match today's code, and it moved neither. At /hi of this session, the reading of `estimate-rules-schema-leaf-carries-no-how-it-works` was `failed` on those two facts. The first fact is the last sentence of the old section of `rule-governed-files-hook`, which said that subagents get no project hook. The archived Spec of session 2026-09-12/0454 holds that sentence. The sentence is false. The Claude Code hooks page (https://code.claude.com/docs/en/hooks) says that hooks from settings files also run inside subagents and that the hook input then carries `agent_id` and `agent_type`. In this build, the `PostToolUse` hook `pageread` added its context to the reads of `case-guppi`, which is a subagent. The docstring of `.guppi/guppi/ratified.py` also records the `agent_type` that Claude Code gives a hook fired inside a subagent (measured 2026-10-05). I read `run`, `governed`, `relative` and `key` of `.guppi/guppi/guard.py`: no condition reads the agent, so the hook refuses an edit of a subagent the same way.
>
> The second fact is the condition under which the Spec hook removes a parent. The old section of `rule-spec-write`, as the archived Spec of session 2026-10-07/2114 holds it (case 722.2), removes the parent when it holds no decision line of its own that no mark retires. The docstring says the parent holds no decision line of its own. I read `remove_superseded`, `ancestors` and `remove_case` of `.guppi/guppi/ratified.py`, `retired_whole`, `retired_by` and `superseded_in_window` of `.guppi/guppi/prespec.py`, and `in_family` of `.guppi/guppi/materialize.py`. The parent step tests `parent not in own`, so the docstring states that step as written. But a mark retires the parent's own line only when it names the parent or a Case above it, by `in_family`. Such a mark puts that Case among the removed Cases, and `remove_case` removes it with all its sub-cases. So the two texts give the same result. The old wording therefore stays true in `vault/wiki/case-schema.md`, in its source `rule-case-protocol` and in the Criterion of `estimate-spec-write-removes-a-superseded-case`, and these stand. The test `test_superseded_a_parent_with_a_line_of_its_own_stays` of `.guppi/tests/test_ratified.py` covers the parent step, and the code does not change.
>
> The rule that governs is `rule-rules-schema`: a Leaf keeps its mechanism in the docstring of its code. `CLAUDE.md` asks for a real source for each claim, so a false fact is corrected, never moved. The Criterion of `estimate-rules-schema-leaf-carries-no-how-it-works` asks that each fact stand in the docstring, which a corrected fact cannot meet, so Case 946.1 replaces that Criterion and sets its `purpose` and `method` anew. Two lines of the old Criterion do not carry over on purpose: its `When`, which waited for the librarian's run that has already applied Case 942.1, and the fact line that asked for each fact as it stood. Case 946.2 likewise drops the line of the Criterion of `estimate-shell-write-check-repairs-and-reports` that a shell call of a subagent is not checked. A Grep for `does not inherit|inherit no project hook` printed `vault/wiki/brief.md`, `vault/wiki/rules/rule-documentation.md`, `vault/wiki/rules/rule-shell-write-check.md` and `vault/wiki/estimates/estimate-shell-write-check-repairs-and-reports.md` over `vault/wiki/`, nothing over `.claude/`, and `.guppi/guppi/shellwrite.py` over `.guppi/guppi/`. The brief is not read. Case 946.2 fixes the other four. I read `run`, `lines_for`, `judge` and `changed_files` of `.guppi/guppi/shellwrite.py`, and no condition reads the agent. The Render of `rule-documentation` keeps the librarian's own `PostToolUse` hook, and only the reason given in its `## How it works` goes. This Case does not judge whether that hook is still needed. The Criterion of `estimate-governed-files-hook-refuses` says nothing about subagents, so it stands. A Grep of `.guppi/tests/` for `How it works`, the slugs of the Estimates and `librarian-guppi.md` found no test that reads a live file this Case changes. The session's ledger holds no `error` lesson.

> **problem:**
> Two facts of the removed `## How it works` sections stand in no docstring. One fact is false, and its false reason also stands in four other live texts. The Estimate on the moved facts asks for each fact as it stood, so it cannot pass.

> **recommend:**
> - **What the docstring of guard.py says about subagents**
>   - Recommended: (a) the docstring states the true fact: Claude Code runs the hook on a call of a subagent too, and the hook refuses it the same way.
>   - Answer: agreed, (a).
> - **Whether the Case also fixes the same false reason elsewhere**
>   - Recommended: (a) a second sub-case fixes the docstring of `shellwrite.py`, the Purpose of `rule-shell-write-check`, the Criterion of its Estimate and the `## How it works` of `rule-documentation`.
>   - Answer: agreed, (a).
> - **What the docstring of ratified.py says about removing a parent**
>   - Recommended: (a) the docstring adds one clause that joins the two wordings; the code does not change.
>   - Answer: agreed, (a).
> - **How the Estimate on the moved facts is checked**
>   - Recommended: (a) replace the Criterion of `estimate-rules-schema-leaf-carries-no-how-it-works` whole, and set its purpose and method anew.
>   - Answer: agreed, (a).

### Case 946.1 — Each moved fact stands in the docstring as the code bears it out

> **given:**
> `estimate-rules-schema-leaf-carries-no-how-it-works`: its Criterion is replaced whole, and its purpose and method are set anew.
> **＋** `.guppi/guppi/guard.py`: the hook of `rule-governed-files-hook`, whose docstring gains the fact on subagents.
> **＋** `.guppi/guppi/ratified.py`: the Spec hook of `rule-spec-write`, whose docstring gains the clause on a retired parent.
> **＋** `rule-rules-schema`: the rule that a Leaf keeps its mechanism in the docstring of its code.
> **＋** `rule-internal-context`: its `## Purpose` holds the facts of its old section.
> **＋** `vault/wiki/rules/`: the Rule pages that the reading covers.

> **when:**
> After Work Mode writes the docstrings of `.guppi/guppi/guard.py` and `.guppi/guppi/ratified.py`, an agent reads each Leaf page of `vault/wiki/rules/` and the docstring of the code that its `implementation_ref` names.

> **then:**
> No Leaf page of `vault/wiki/rules/` carries a section `## How it works`.
> **＋** Each fact that such a section held stands, as the code bears it out, in the docstring of the code that the page's `implementation_ref` names, and for `rule-internal-context` in its `## Purpose`; a fact that the code does not bear out stands there corrected.
> **＋** The docstring of `.guppi/guppi/guard.py` says that Claude Code runs the hook on a call of a subagent too, and that the hook refuses such a call the same way.
> **＋** The docstring of `.guppi/guppi/ratified.py` says that a parent whose own decision line a mark retires is named by that mark or lies under a Case it names, and leaves by that mark with its sub-cases.
> **－** A remark on what stood before some Case does not move into the docstrings or the Purpose.
> **－** A MOC page of `vault/wiki/rules/` keeps its `## How it works`.

> **tasks:**
> - [ ] `.guppi/guppi/guard.py`: the module docstring says that Claude Code runs the hook on a call of a subagent too, and that the hook reads no agent, so it refuses an edit of a governed file by a subagent the same way.
> - [ ] `.guppi/guppi/ratified.py`: in the paragraph of the module docstring on the removal, after "a parent with a line of its own stays", one clause says that a parent whose own line a mark retires is named by that mark or lies under a Case it names, and leaves by that mark with its sub-cases; `remove_superseded` does not change.
> - [ ] update `estimate-rules-schema-leaf-carries-no-how-it-works`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether no Leaf page of vault/wiki/rules/ carries How it works, each fact it held standing as the code bears it out in the docstring of its code or, for rule-internal-context, in its Purpose, a fact the code does not bear out standing corrected"
>     method: "by hand at Retro of the session that changes it: a Grep for ^## How it works over vault/wiki/rules/ and the kind of each page it prints, no Leaf among them; the docstrings of .guppi/guppi/guard.py and .guppi/guppi/ratified.py read against the How it works sections that git show 9d19aafe prints as removed, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — a fact the code does not bear out stands corrected in the docstring`
> - [ ] read `estimate-rules-schema-leaf-carries-no-how-it-works`

> **ratification:**
> ```
> - decision[case 946.1][update][estimate-rules-schema-leaf-carries-no-how-it-works]{ref:rule-rules-schema}
> ```

### Case 946.2 — A shell call of a subagent is checked like any other

> **given:**
> `.guppi/guppi/shellwrite.py`: the hook of `rule-shell-write-check`, whose docstring drops the false reason.
> **＋** `rule-shell-write-check`: its Purpose says what the hook does not check.
> **＋** `estimate-shell-write-check-repairs-and-reports`: its Criterion is replaced whole without the line on subagents.
> **＋** `rule-documentation`: its `## How it works` gives the reason for the librarian's own hook.
> **＋** `.claude/settings.json`: the file that registers the hook.
> **＋** `rule-hook-registry`: the rule whose Render writes the registration.

> **when:**
> A call of the `Bash` or `PowerShell` tool ends, and `uv run --project .guppi guppi shellwrite` of `.guppi/guppi/shellwrite.py` on `PostToolUse` reads each file that `git` lists as changed or new and not ignored.

> **then:**
> In each such file the hook turns every CRLF line ending into LF, and removes a UTF-8 byte-order mark at its start.
> **＋** For each file it repaired, one line of `hookSpecificOutput.additionalContext` names the file and what it repaired, and tells the agent to change a file with Edit or Write, never through a shell command; a line on a removed mark also asks the agent to check the characters of the file.
> **＋** A file that opens with a UTF-16 byte-order mark, or that is not valid UTF-8, is not changed: its line names the file and the fault and tells the agent to restore the file with Write.
> **＋** The hook reads every changed or new file at each such call, so a file left faulty is named again at the next call.
> **＋** `.claude/settings.json` registers the hook on `PostToolUse` with the matcher `Bash|PowerShell`, by the Render of `rule-hook-registry`.
> **－** A file outside the repository, a file that `git` ignores, and a file with a NUL byte and no UTF-16 mark are neither read for a fault nor changed.
> **－** A call that leaves no faulty file adds nothing to the context.
> **－** A payload the hook cannot read, or a `git` call that fails, gives exit 0 and one line on stderr; the hook never raises.

> **tasks:**
> - [ ] `.guppi/guppi/shellwrite.py`: the module docstring drops the sentence that a shell call of a subagent is not checked, and says that Claude Code runs the hooks of `.claude/settings.json` inside a subagent too, so a shell call of a subagent is checked the same way.
> - [ ] update `rule-shell-write-check`
>   - old: `A file whose characters changed but which stays valid UTF-8 with no mark is not caught, and a shell call of a subagent is not checked, since a subagent does not inherit the project's hooks (case 710.1).`
>   - new: `` A file whose characters changed but which stays valid UTF-8 with no mark is not caught (case 710.1). A shell call of a subagent is checked the same way, since Claude Code runs the hooks of `.claude/settings.json` inside a subagent too. ``
>   - change: `a shell call of a subagent is checked, since Claude Code runs the project's hooks inside a subagent`
> - [ ] update `rule-documentation`
>   - old: `writes its commands to the event log, since a subagent does not inherit the project's hooks;`
>   - new: `writes its commands to the event log;`
>   - change: `How it works drops the false reason that a subagent does not get the project's hooks`
> - [ ] update `estimate-shell-write-check-repairs-and-reports`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the line that a shell call of a subagent is not checked removed`
> - [ ] read `estimate-shell-write-check-repairs-and-reports`

> **ratification:**
> ```
> - decision[case 946.2][update][rule-shell-write-check]{ref:rule-shell-write-check}
> - decision[case 946.2][update][rule-documentation]{ref:rule-documentation}
> - decision[case 946.2][update][estimate-shell-write-check-repairs-and-reports]{ref:rule-shell-write-check}
> ```
