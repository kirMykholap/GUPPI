## Case 710 — A file a shell call left in a wrong byte form is repaired or named

> **context:**
> The agent sometimes changes a file of the repository with a Bash or PowerShell command instead of the Edit or Write tool, and on Windows the tool on the way rewrites the bytes of the file. The three lessons of `insight-workflow-file-changed-through-a-shell-command` show it. Windows PowerShell 5.1 read `frontier.md` in the ANSI code page and wrote it back with a byte-order mark and broken characters. Two inline Python scripts in Bash rewrote `guppi/onward.py` by `Path.write_text`, and after the last one the file held 412 CRLF line endings against 0 at HEAD. `guppi/bashguard.py` runs before a Bash call and refuses a heredoc only for a backslash in its body or a redirect into a file on its marker line, so both scripts passed. No hook of `.claude/settings.json` judges or guards a call of the PowerShell tool: the only hook that runs on it is `uv run guppi event tool`, which logs every tool on `PostToolUse`, and its line 242 of `vault/raw/2026-09-18/event_log.md` shows that the agent calls that tool. The person chose a check after the call rather than a wider guard before it, on Bash and on PowerShell; a rule page of its own with its own Estimate; every changed or new file at each call; and a hook that repairs CRLF line endings and a UTF-8 byte-order mark itself and only names a file it cannot repair, in UTF-16 or not valid UTF-8. `.gitattributes` sets `* text=auto eol=lf`, so LF is the form the repository sets for every text file. The hook gives its lines as `hookSpecificOutput.additionalContext`, which `rule-spec-capture` names the one shape in which the stdout of a `PostToolUse` hook reaches the agent (case 255). A file whose characters a tool changed but which stays valid UTF-8 with no mark is not caught, since no byte rule tells it from a sound file; where the hook removes a mark it asks the agent to check the characters, since in the first lesson the mark came with broken characters. A shell call of a subagent is not checked: `rule-governed-files-hook` and `rule-documentation` say that a subagent does not inherit the project's hooks. Case 710.2 sets the Insight `actioned`, its `addressed_by` the decision of Case 710.1, and corrects its Pattern, which names two lessons of three; by `rule-insights-schema` the cascade of `generate` then archives its three lessons. Its `## Proposal` stands: the schema calls it a suggestion, not a decision. `estimate-insights-schema-checked` checks Case 710.2: its Criterion says that an `actioned` Insight requires `addressed_by` and that a page in the shape has no `schema` finding, and its live reading is `make lint` at the librarian's run, which the brief reports. This Case changes no schema, so its Criterion stands; no Estimate reads the words of a Pattern. The person chose the quoted wikilink that the field description of `rule-insights-schema` sets, unless the check of this file refuses a wikilink to a decision of this session. It does: with the quoted wikilink, the `SubagentStop` check printed `casecheck: case 710.2: [[decision-case-710.1]] outside a code span names no page`, since `decision-case-710.1` is written only at the librarian's run. So the field holds the slug without brackets, as the example of `rule-insights-schema` writes it. `slug_of` of `guppi/pages.py`, which `guppi/lint.py` imports, gives the slug inside a `[[slug]]` value and any other value as it stands, so both forms give lint the same slug.
>
> The vault query of `.claude/agents/ask-guppi.md` answers: exists — none; near — `rule-bash-guard`, the guard before a Bash call, which stays as it is, and `rule-python-utf8`, which puts the output of a Python process in UTF-8 and does not judge the files it writes; missing — a check of the bytes of a file after a shell call; rules — `rule-hook-registry` requires the registration in the same Case that creates the rule of the hook, and `rule-harness` counts in its Purpose the rules that run in no pipeline; tags — `hooks`, `harness` and `workflow`, each a row of `tags.md`; a Glob `vault/**/*shell-write*` printed nothing, so `rule-shell-write-check` and `estimate-shell-write-check-repairs-and-reports` are free. `estimate-hook-registry-rendered` says that every hook the harness runs is registered by a line of the Render; that stays true, so its Criterion stands. A Grep of `(?i)hook that refuses a heredoc|run in no pipeline` over `vault/wiki/`, `guppi/`, `tests/`, `.claude/` and `CLAUDE.md` printed `vault/wiki/estimates/estimate-harness-pipeline.md` and `vault/wiki/rules/rule-harness.md`. Case 710.1 changes the Purpose of `rule-harness`. The Criterion of `estimate-harness-pipeline` lists rules the Purpose must name, not all of them, and the Purpose still names each one, so its Criterion stands, as case 640 found. A Grep of `PostToolUse` over `vault/wiki/rules/` and `.claude/` printed `.claude/settings.json`, `.claude/agents/librarian-guppi.md`, `rule-hook-registry.md`, `rule-spec-reconcile.md`, `rule-documentation.md`, `rule-spec-capture.md`, `rule-event-log.md`, `rule-governed-files-hook.md` and `rule-page-read.md`. Only `rule-event-log` sets what happens after a Bash or PowerShell call: its hook writes one log line for every tool, and this Case does not change it. The other passages set the moment after `ExitPlanMode` or `Read`, the librarian's own hook, or a refused call, which has no `PostToolUse`. A Grep of `insight-workflow-file-changed-through-a-shell-command` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `brief.md`, `backlog.md`, `log.md` and the three lessons. The lessons link to the Insight by their `insight` field, which stays true; `backlog.md` lists open Insights and is written again by `guppi backlog` at the librarian's run; `brief.md` and `log.md` are not read. The code of `guppi/shellwrite.py` runs from the working tree at once, but the hook fires only once the render writes `.claude/settings.json`; nothing refuses in between, so no old form is kept. No other Case of this session sets what happens after a shell call or changes a page of this Case.

> **problem:**
> A shell command can rewrite a file of the repository with CRLF line endings, a byte-order mark or another encoding, and no check sees it: the guard before a Bash call reads only heredocs, and no hook judges a PowerShell call.

> **recommend:**
> - **Where the check catches a file changed through a shell command**
>   - Recommended: (b) check the files after the call: a new hook after each shell call reads the files git sees as changed or new and reports each one with a CRLF line ending, a byte-order mark, or bytes that are not valid UTF-8.
>   - Answer: agreed, (b), after the main agent explained the round again in plain words.
> - **Which shell tools the check covers**
>   - Recommended: (b) Bash and PowerShell.
>   - Answer: agreed, (b).
> - **Which page holds the new check**
>   - Recommended: (a) a new rule page, such as `rule-shell-write-check`, with its own Estimate; `rule-bash-guard` and its Estimate stay as they are, and `rule-hook-registry` gains the hook entries.
>   - Answer: agreed, (a).
> - **Which files the check looks at after each call**
>   - Recommended: (a) every changed or new file, ignored files left out, at every call, so a faulty file is reported again until it is repaired.
>   - Answer: agreed, (a).
> - **What the hook does with a faulty file**
>   - Recommended: (b) repair what is safe and report the rest: the hook turns CRLF into LF and removes a byte-order mark, names the files it repaired, and only reports a file that is not valid UTF-8 or holds UTF-16 text.
>   - Answer: agreed, (b).
> - **What happens to the Insight page**
>   - Recommended: (a) mark it fixed and correct its Pattern: `actioned`, `addressed_by` the decision of this Case, and a Pattern that names the three lessons.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of pre-spec: a hook does run on PowerShell, `uv run guppi event tool`, so `context` and `problem` should say that no hook judges or guards a PowerShell call.
>   - Taken: `context` and `problem` now say that no hook judges a PowerShell call, and that the only hook on it logs the call.
> - **Change**
>   - Asked: a finding of pre-spec, which the person agreed with: write `addressed_by` as the quoted wikilink to `decision-case-710.1`, as the schema sets, and keep the bare slug only if the check of the file refuses that link, quoting its refusal in `context`.
>   - Taken: the check refused the link, so the bare slug stands, and `context` quotes the refusal.

### Case 710.1 — The hook after a shell call repairs or names a file in a wrong byte form

> **given:**
> `rule-shell-write-check`: the new rule of the hook.
> **＋** `estimate-shell-write-check-repairs-and-reports`: the new check of the hook.
> **＋** `guppi/shellwrite.py` and `guppi/cli.py`: the hook and the dispatch of its command.
> **＋** `tests/test_shellwrite.py`: the tests of the hook.
> **＋** `rule-hook-registry` and `.claude/settings.json`: the registration of the hook, rendered into the file.
> **＋** `rule-harness` and `estimate-harness-pipeline`: the parent rule, whose Purpose counts the rules in no pipeline, and the Estimate that lists them. Its Criterion is unchanged.
> **＋** `rule-event-log`: the hook that logs every tool on `PostToolUse`. Unchanged.
> **＋** `.gitattributes`: sets LF for every text file of the repository.

> **when:**
> A call of the `Bash` or `PowerShell` tool ends, and `uv run guppi shellwrite` of `guppi/shellwrite.py` on `PostToolUse` reads each file that `git` lists as changed or new and not ignored.

> **then:**
> In each such file the hook turns every CRLF line ending into LF, and removes a UTF-8 byte-order mark at its start.
> **＋** For each file it repaired, one line of `hookSpecificOutput.additionalContext` names the file and what it repaired, and tells the agent to change a file with Edit or Write, never through a shell command; a line on a removed mark also asks the agent to check the characters of the file.
> **＋** A file that opens with a UTF-16 byte-order mark, or that is not valid UTF-8, is not changed: its line names the file and the fault and tells the agent to restore the file with Write.
> **＋** The hook reads every changed or new file at each such call, so a file left faulty is named again at the next call.
> **＋** `.claude/settings.json` registers the hook on `PostToolUse` with the matcher `Bash|PowerShell`, by the Render of `rule-hook-registry`.
> **－** A file outside the repository, a file that `git` ignores, and a file with a NUL byte and no UTF-16 mark are neither read for a fault nor changed.
> **－** A call that leaves no faulty file adds nothing to the context.
> **－** A payload the hook cannot read, or a `git` call that fails, gives exit 0 and one line on stderr; the hook never raises.
> **－** A shell call of a subagent is not checked, since a subagent does not inherit the hooks of `.claude/settings.json`.

> **tasks:**
> - [ ] create `rule-shell-write-check`
>   - ref: `rule-harness`
>   - kind: `Leaf`
>   - purpose: `Prevents a file of the repository from keeping the CRLF line endings, the byte-order mark or the broken encoding that a Bash or PowerShell call left in it`
>   - enforcement: `hook`
>   - implementation_ref: `[guppi/shellwrite.py, tests/test_shellwrite.py, .claude/settings.json]`
>   - tags: `[hooks, harness, workflow]`
>   - sections.Purpose:
>     ```
>     Prevents a file of the repository from keeping the CRLF line endings, the byte-order mark or the broken encoding that a Bash or PowerShell call left in it. On Windows, Windows PowerShell 5.1 reads a UTF-8 file in the ANSI code page and writes it back with a byte-order mark, and Python's `Path.write_text` writes CRLF line endings. The three lessons of `insight-workflow-file-changed-through-a-shell-command` came from such writes, and the guard of `rule-bash-guard`, which reads only heredocs before a Bash call, did not see them. `uv run guppi shellwrite` runs on `PostToolUse` of `Bash` and `PowerShell` and reads each file that `git` lists as changed or new and not ignored. It turns CRLF into LF and removes a UTF-8 byte-order mark, the form `.gitattributes` sets for every text file, and names each file it repaired in `hookSpecificOutput.additionalContext`; a file in UTF-16 or not valid UTF-8 it names without a change, for the agent to restore with Write. A file whose characters changed but which stays valid UTF-8 with no mark is not caught, and a shell call of a subagent is not checked, since a subagent does not inherit the project's hooks (case 710.1).
>     ```
> - [ ] create `estimate-shell-write-check-repairs-and-reports`
>   - ref: `rule-shell-write-check`
>   - kind: `QA`
>   - purpose: `Whether the hook after a Bash or PowerShell call turns CRLF into LF and removes a UTF-8 byte-order mark in each changed or new file of the repository and names each file it repaired, and names without a change a file in UTF-16 or not valid UTF-8`
>   - method: `uv run pytest tests/test_shellwrite.py`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-hook-registry`
>   - old: `{ "matcher": "Read", "hooks": [ { "type": "command", "command": "uv run guppi pageread --after", "timeout": 30 } ] }`
>   - new: `{ "matcher": "Read", "hooks": [ { "type": "command", "command": "uv run guppi pageread --after", "timeout": 30 } ] }, { "matcher": "Bash|PowerShell", "hooks": [ { "type": "command", "command": "uv run guppi shellwrite", "timeout": 30 } ] }`
>   - change: `guppi shellwrite registered on PostToolUse of Bash and PowerShell (case 710.1)`
> - [ ] update `rule-harness`
>   - old: `Ten more belong here and run in no pipeline:`
>   - new: `Eleven more belong here and run in no pipeline:`
>   - old: `the hook that refuses a heredoc with a backslash or a file write, the page`
>   - new: `the hook that refuses a heredoc with a backslash or a file write, the hook that repairs or names a file a shell call left with CRLF line endings, a byte-order mark or bytes that are not UTF-8, the page`
>   - old: `476.1, 640).`
>   - new: `476.1, 640, 710.1).`
>   - change: `an eleventh rule outside the pipeline: the hook that repairs or names a file a shell call left in a wrong byte form (case 710.1)`
> - [ ] `guppi/shellwrite.py`: `run` reads the `PostToolUse` payload of `Bash` or `PowerShell`, lists the changed and new files that are not ignored by `git ls-files -m -o --exclude-standard`, skips a deleted file and a file with a NUL byte and no UTF-16 mark, names a file with a UTF-16 mark or not valid UTF-8 without a change, turns CRLF into LF and removes a UTF-8 mark in the rest, and prints one `hookSpecificOutput.additionalContext` with a line per named file; exit 0 always, one stderr line on an unreadable payload or a failed `git`; the docstring says so and names the rule page.
> - [ ] `guppi/cli.py`: the command `shellwrite` dispatches to `guppi/shellwrite.py`, and the docstring lists it among the hook commands.
> - [ ] `tests/test_shellwrite.py`: in a temporary git repository, a changed file with CRLF and a new file with a UTF-8 mark are repaired and named; a file in UTF-16 and one not valid UTF-8 are named and unchanged; an ignored file, a binary file and a clean file are not touched and give no output; another tool, an unreadable payload and a failed `git` give exit 0.
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-shell-write-check-repairs-and-reports`

> **ratification:**
> ```
> - decision[case 710.1][create][rule-shell-write-check]{ref:rule-harness}{tags:hooks,harness,workflow}
> - decision[case 710.1][create][estimate-shell-write-check-repairs-and-reports]{ref:rule-shell-write-check}{tags:hooks,harness,workflow}
> - decision[case 710.1][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 710.1][update][rule-harness]{ref:rule-harness}
> ```

### Case 710.2 — The Insight is marked fixed and its Pattern names three lessons

> **given:**
> `insight-workflow-file-changed-through-a-shell-command`: the Insight that becomes `actioned`.
> **＋** `rule-insights-schema`: the schema that requires `addressed_by` on an `actioned` Insight.
> **＋** `guppi/generate.py`: writes the fields and the Pattern from the `update`.
> **＋** `guppi/lint.py`: `make lint`, which checks the page against the schema.

> **when:**
> The librarian's run applies the yaml of this session by `guppi/generate.py`, and `make lint` of `guppi/lint.py` reads `insight-workflow-file-changed-through-a-shell-command` by the schema of `rule-insights-schema`.

> **then:**
> `insight-workflow-file-changed-through-a-shell-command` holds `status: actioned` and `addressed_by: decision-case-710.1`.
> **＋** Its `## Pattern` says three lessons share one cause and names the third: an inline Python script in Work Mode that rewrote a file of the repository with CRLF line endings.
> **＋** `make lint` prints no `schema` finding on `insight-workflow-file-changed-through-a-shell-command`.
> **－** Its `## Proposal` does not change.

> **tasks:**
> - [ ] update `insight-workflow-file-changed-through-a-shell-command`
>   - set: `{status: actioned, addressed_by: decision-case-710.1}`
>   - old: `Two lessons, one cause.`
>   - new: `Three lessons, one cause.`
>   - old: `so the bashguard guard let it through.`
>   - new: `so the bashguard guard let it through. In Work Mode of session 0425 a python heredoc in Bash rewrote guppi/onward.py with Path.write_text again, and the file held 412 CRLF line endings against 0 at HEAD.`
>   - change: `actioned by decision-case-710.1, the hook that repairs or names a file a shell call left in a wrong byte form; the Pattern names the third lesson (case 710.2)`

> **ratification:**
> ```
> - decision[case 710.2][update][insight-workflow-file-changed-through-a-shell-command]{ref:insight-workflow-file-changed-through-a-shell-command}
> ```
