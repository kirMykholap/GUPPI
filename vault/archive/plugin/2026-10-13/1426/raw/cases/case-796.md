## Case 796 — A script fed inline to an interpreter is refused before a shell call

> **context:**
> In Work Mode of session 2349 the agent changed `guppi/materialize.py` with a Python script typed inline in a Bash call. The event log of 2026-10-13 holds the command at 03:26:00: `python - <<'EOF' from pathlib import Path p = Path("guppi/materialize.py") ...`. The check before a Bash call, `uv run guppi bashguard` of `rule-bash-guard`, refuses a heredoc for two reasons only: a backslash in its body, or a marker line that writes a file. A heredoc fed into Python with neither reason passes. The hook after the call, `rule-shell-write-check`, then turned the CRLF line endings that the script wrote back into LF. This is the third such case. The archived `insight-workflow-file-changed-through-a-shell-command` records two Python heredocs that rewrote `guppi/onward.py`, in sessions 0211 and 0425, and one PowerShell call that rewrote a session file. Case 710.1 answered with the repair after the call, and the agent's choice came back. So the cause of `lesson-work-mode-edited-a-source-file-through-the-shell` is that nothing refuses an inline script before it runs. The one place that sends the agent to Edit is the refusal message of the Bash check.
>
> The person chose a refusal before the call, in both shells. Case 796.1 adds a third reason to the Bash check: a heredoc whose marker line runs an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`). Case 796.2 creates `rule-powershell-guard`, a new check before a PowerShell call that refuses a here-string piped into one of those interpreters. A script run by path and a script passed by `-c` or `-e` still pass in both shells. In PowerShell, a quoted string, a variable or the output of a command piped into an interpreter also still passes. These are left not done by the person's answers.
>
> The pages. `rule-bash-guard` is a `Leaf` that still holds `## How it works`. `rules/schema.yaml` says that such a section leaves at the page's next touch (cases 193, 200.2). No form of an `update` removes a section: Case 793 of session 2349 put that form off. By the person's answer, a one-off task in Work Mode removes the section by hand, as case 589.2 did for `rule-case-check`. The section's facts already stand in the docstring of `guppi/bashguard.py`. The section's sentence that a heredoc with no backslash whose output goes to a pipe or the screen passes becomes false with Case 796.1, and the section leaves with it. The Purpose of `rule-harness` names its members, among them the hook that refuses a heredoc with a backslash or a file write, and it counts them as eleven. Case 796.1 adds the third reason there. Case 796.2 adds the new check and makes the count twelve. The Criterion of `estimate-harness-pipeline` names a subset of those members, the Bash check among them by its two old reasons. The new Purpose still names that check, with one reason more, so the Criterion stands. The Criterion of `estimate-bash-guard` states what the check refuses and lets through, so Case 796.1 replaces it whole. Its `purpose` states the old promise and is set anew. Its `method` names only the tests and a live refusal, so it stands. Case 796.2 creates `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`. Case 796.2 changes the Render of `rule-hook-registry`. The Criterion of `estimate-hook-registry-rendered` promises that the `"hooks"` key of `.claude/settings.json` equals that Render byte for byte, and that every hook the harness runs is registered by one of its lines. The new hook gets its line in the Render in the same `update`, so the promise holds as written and the Criterion stands. An `update` of a Render touches no Estimate of the live reading (case 378.5), and the librarian's `render --check` reads it again. The registration on `PowerShell` is read by the `method` of the new Estimate after the librarian's run renders the file, since the target of that Estimate has no Render of its own. The `then` lines of the two sub-cases match each other on purpose, since each one sets the same kind of refusal for one of the two shells. They name different hooks, messages and log lines, so nothing is signed twice. The two lines of the old Criterion of `estimate-bash-guard` that name only two reasons are not carried word for word: Case 796.1 replaces them with lines that name three.
>
> What the frame showed. A Grep `bashguard|bash-guard|PowerShell` over `vault/wiki/` (with `log.md` and `brief.md` left out) printed `estimates/estimate-bash-guard.md`, `rules/rule-bash-guard.md`, `lessons/lesson-work-mode-edited-a-source-file-through-the-shell.md`, `estimates/estimate-harness-make-runs-in-both-shells.md`, `rules/rule-hook-registry.md`, `rules/rule-harness.md`, `rules/rule-shell-write-check.md` and `estimates/estimate-shell-write-check-repairs-and-reports.md`. The same Grep over `.claude/` printed `.claude/settings.json`. The Purpose of `rule-shell-write-check` says that the Bash guard reads only heredocs before a Bash call, and the docstring of `guppi/shellwrite.py` says the same. Both stay true. The Criterion of `estimate-shell-write-check-repairs-and-reports` speaks of the hook after a call, which no part of this Case changes. `estimate-harness-make-runs-in-both-shells` runs `make` from PowerShell and pipes no here-string. A Grep `heredoc|here-string|interpreter` over `vault/wiki/` printed `brief.md` and `log.md`, which are not read, and `lessons/lesson-work-mode-edited-a-source-file-through-the-shell.md`, `rules/rule-documentation.md`, `rules/rule-shell-write-check.md`, `rules/rule-harness.md`, `rules/rule-hook-registry.md`, `rules/rule-bash-guard.md`, `lessons/lesson-bash-tool-heredoc-escapes-interpreted.md`, `estimates/estimate-harness-pipeline.md`, `estimates/estimate-documentation-completes.md` and `estimates/estimate-bash-guard.md`. `rule-documentation` and `estimate-documentation-completes` forbid the librarian to put a file under `vault/` by a heredoc, which stays true. `lesson-bash-tool-heredoc-escapes-interpreted` sends a multi-line edit script to the scratchpad, run by path, which both checks let through. A Grep `<<|@'|@"|\| *python` over `.claude/` printed nothing, so no harness text tells an agent to run a command that the new checks refuse. On `PreToolUse`, `.claude/settings.json` registers `guppi prespec` on `ExitPlanMode`, `guppi gate` on `Skill`, `guppi guard` and `guppi ratified --guard` on `Edit|Write|MultiEdit`, `guppi bashguard` on `Bash`, `guppi pageread` on `Read` and `guppi grepguard` on `Grep`. None of them runs on `PowerShell`.
>
> One judgment. A Grep `python3?\b.*-|interpreter|INTERPRET|\bnode\b|PowerShell` over `guppi/` printed `guppi/bashguard.py`, `guppi/shellwrite.py` and `guppi/event.py`. They hold only a docstring on how the shell layer treats escapes, the tool names of the repair hook, and a note on a byte-order mark. No function of either side judges an interpreter today. Case 796.1 adds that one function to `guppi/bashguard.py`, and `guppi/powershellguard.py` imports it, so no second copy is written. A Grep `settings\.json|rule-bash-guard|rule-hook-registry|rule-harness|estimate-bash-guard` over `tests/` printed `tests/test_bashguard.py`, `tests/test_guard.py`, `tests/test_ratified.py`, `tests/test_render.py`, `tests/test_glossary.py` and `tests/test_pages.py`. Each one writes its files under a temporary folder or names the slug in a docstring, so no test reads the live pages or the live `.claude/settings.json` that this Case changes. In `tests/test_bashguard.py`, the commands `CLEAN_PIPE` and `NULL_ONLY` feed `python` and are expected to pass, so Case 796.1 changes them. A Glob `vault/**/*powershell*` printed only `vault/archive/migration/2026-10-07/0636/lessons/lesson-session-frontier-rewritten-through-powershell.md`, so both new slugs are free. The lesson is of session 2349, so no decision line carries `{addresses:...}` (case 284.2).

> **problem:**
> An agent can rewrite a source file with a script typed inline and fed to an interpreter in a Bash or PowerShell call, and no check refuses it before it runs. The repair after the call fixes the line endings but not the choice, and the same choice has rewritten a source file in three sessions.

> **recommend:**
> - **Where the fix lives**
>   - Recommended: (a) the check before a Bash call also refuses a heredoc fed into an interpreter.
>   - Answer: (a).
> - **PowerShell calls**
>   - Recommended: (a) Bash only, with the PowerShell gap named as not done.
>   - Answer: (b) Bash and PowerShell.
> - **Where the PowerShell check lives**
>   - Recommended: (a) a new rule beside the Bash one, both checks importing one list of interpreters.
>   - Answer: agreed, (a).
> - **What the PowerShell check refuses**
>   - Recommended: (a) a here-string piped into an interpreter.
>   - Answer: agreed, (a).
> - **A script passed by a flag**
>   - Recommended: (a) leave it out, named as not done.
>   - Answer: agreed, (a).
> - **The section on how the Bash check works**
>   - Recommended: (a) remove the section by hand, once.
>   - Answer: agreed, (a).

### Case 796.1 — The Bash check refuses a heredoc fed into an interpreter

> **given:**
> `guppi/bashguard.py`: the check before a Bash call, and the one judgment of an interpreter.
> **＋** `tests/test_bashguard.py`: the tests of the check.
> **＋** `rule-bash-guard`: the rule of the check; its Purpose changes and its `## How it works` leaves.
> **＋** `estimate-bash-guard`: its Criterion is replaced whole.
> **＋** `rule-harness`: its Purpose names the check by what it refuses.
> **＋** `/dev/null`: the one redirect target that is no file write.
> **＋** `raw/<date>/event_log.md`: the log a refusal is written to.

> **when:**
> The agent calls `Bash`, and `uv run guppi bashguard` on `PreToolUse` reads `tool_input.command` of the payload and finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line.

> **then:**
> A heredoc whose body holds a backslash, whose marker line writes a file (`>` or `>>` not to `/dev/null`, `tee`), or whose marker line runs an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`) as one of its commands exits 2 with the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path> | it feeds <interpreter>>. Write a whole file with the Write tool and change a file with Edit, never through Bash; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
> **＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard refused: <reason>` goes to `raw/<date>/event_log.md`.
> **＋** A `<<<` here-string, a heredoc with no backslash, no file write and no interpreter on its marker line, a command without a heredoc, another tool — exit 0.
> **＋** A payload the hook cannot read — exit 0 with one line on stderr.
> **－** An interpreter that runs a script by path, or takes it by `-c` or `-e`, is no reason to refuse.
> **－** The hook never raises.

> **tasks:**
> - [ ] `guppi/bashguard.py`: one function judges whether a marker line runs an interpreter of the list, as its first command or after a `|`, `&&`, `||` or `;`, and names it; `refusal` gives `it feeds <interpreter>` after the backslash and the file write; the docstring gains the new reason and keeps every fact of the `## How it works` that leaves the page.
> - [ ] `tests/test_bashguard.py`: `python - <<'EOF'`, `uv run python - <<EOF` and `cat <<EOF | node` are refused with `it feeds <interpreter>` and logged; `python -c "print(1)"` and `python script.py` pass; `CLEAN_PIPE` and `NULL_ONLY` feed `cat` in place of `python` and still pass.
> - [ ] `vault/wiki/rules/rule-bash-guard.md`: a one-off in Work Mode, before the librarian's run: the section `## How it works`, heading and text, removed by hand.
> - [ ] update `rule-bash-guard`
>   - set:
>     ```
>     purpose: Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool
>     ```
>   - sections.Purpose:
>     ```
>     Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool. On this Windows machine the tool's shell layer interprets backslash escapes inside a heredoc body before the interpreter reads it, whatever the quoting of the marker; three sessions (H, L, M) broke edit scripts that way with the lesson live, and a heredoc that writes a file fails on quotes in its body. A heredoc with neither, fed to Python, rewrote a source file in three more sessions, and `Path.write_text` left CRLF line endings in it (`insight-workflow-file-changed-through-a-shell-command`, `lesson-work-mode-edited-a-source-file-through-the-shell`): a source file changes by Edit, and a script goes into the scratchpad and runs by path. A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. A script run by path or passed by `-c` or `-e` passes. The mechanism stands in the docstring of `guppi/bashguard.py`, and a PowerShell call is the rule `rule-powershell-guard` (cases 127, 796.1).
>     ```
>   - change: `a heredoc whose marker line runs an interpreter is refused; How it works removed by hand, a one-off, its facts in the docstring of guppi/bashguard.py (case 796.1)`
> - [ ] update `estimate-bash-guard`
>   - set:
>     ```
>     status: pending
>     purpose: A heredoc with a backslash, a file write or an interpreter it feeds is refused before it runs, with a message that sends the agent to Write and Edit and says the refusal is no finding
>     ```
>   - change: `the Criterion replaced whole — a heredoc fed into an interpreter is refused (case 796.1)`
> - [ ] update `rule-harness`
>   - old: `the hook that refuses a heredoc with a backslash or a file write,`
>   - new: `the hook that refuses a heredoc with a backslash, a file write or an interpreter it feeds,`
>   - change: `the Bash guard named with its third reason (case 796.1)`
> - [ ] read `estimate-bash-guard`

> **ratification:**
> ```
> - decision[case 796.1][update][rule-bash-guard]{ref:rule-bash-guard}
> - decision[case 796.1][update][estimate-bash-guard]{ref:rule-bash-guard}
> - decision[case 796.1][update][rule-harness]{ref:rule-harness}
> ```

### Case 796.2 — A PowerShell check refuses a here-string piped into an interpreter

> **given:**
> `rule-powershell-guard`: the new rule of the check before a PowerShell call.
> **＋** `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`: the new check of the rule.
> **＋** `guppi/powershellguard.py`: the new check.
> **＋** `guppi/bashguard.py`: the one judgment of an interpreter, which the new check imports.
> **＋** `guppi/cli.py`: the command `powershellguard`.
> **＋** `tests/test_powershellguard.py`: the tests of the new check.
> **＋** `rule-hook-registry`: the hook entry on `PreToolUse` of `PowerShell`, rendered into `.claude/settings.json`.
> **＋** `rule-harness`: its Purpose names the new rule.
> **＋** `raw/<date>/event_log.md`: the log a refusal is written to.

> **when:**
> The agent calls `PowerShell`, and `uv run guppi powershellguard` of `guppi/powershellguard.py` on `PreToolUse` reads `tool_input.command` of the payload and finds every here-string: the text from a line that ends with `@'` or `@"` to a line that opens with `'@` or `"@`.

> **then:**
> A here-string whose closing line pipes it into an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`) exits 2 with the reason on stderr: `powershellguard: here-string refused — it is piped into <interpreter>. Write a whole file with the Write tool and change a file with Edit, never through PowerShell; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
> **＋** Before the refusal one line `- HH:MM:SS <stamp> powershellguard refused: <reason>` goes to `raw/<date>/event_log.md`.
> **＋** `guppi/powershellguard.py` judges the interpreter by the function of `guppi/bashguard.py` that the Bash check calls, and keeps no list of its own.
> **＋** `.claude/settings.json` registers the hook on `PreToolUse` with the matcher `PowerShell`, by the Render of `rule-hook-registry`.
> **＋** A here-string not piped into an interpreter, a command without a here-string, another tool — exit 0; a payload the hook cannot read — exit 0 with one line on stderr.
> **－** A quoted string, a variable or the output of a command piped into an interpreter, a script run by path, and a script passed by `-c` or `-e` are no reason to refuse.
> **－** The hook never raises.

> **tasks:**
> - [ ] create `rule-powershell-guard`
>   - type: `rule`
>   - kind: `Leaf`
>   - purpose: `Prevents a here-string from feeding a script to an interpreter through the PowerShell tool`
>   - enforcement: `hook`
>   - implementation_ref: `[guppi/powershellguard.py, tests/test_powershellguard.py, .claude/settings.json]`
>   - tags: `[hooks, harness]`
>   - sections.Purpose:
>     ```
>     Prevents a here-string from feeding a script to an interpreter through the PowerShell tool. A script fed inline to Python rewrote a source file in three sessions, and `Path.write_text` left CRLF line endings in it (`insight-workflow-file-changed-through-a-shell-command`, `lesson-work-mode-edited-a-source-file-through-the-shell`). `rule-bash-guard` refuses such a heredoc before a Bash call; a here-string piped into an interpreter is the same script in PowerShell, and no check saw it before the call. A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. The interpreters are judged by the one function of `guppi/bashguard.py`, so both checks answer alike. A quoted string, a variable or the output of a command piped into an interpreter, a script run by path, and a script passed by `-c` or `-e` pass. The mechanism stands in the docstring of `guppi/powershellguard.py` (case 796.2).
>     ```
> - [ ] create `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`
>   - ref: `rule-powershell-guard`
>   - kind: `QA`
>   - purpose: `A here-string piped into an interpreter is refused before a PowerShell call runs, with a message that sends the agent to Write and Edit and says the refusal is no finding`
>   - method: `uv run pytest tests/test_powershellguard.py; after the librarian's run of this session renders rule-hook-registry: the PowerShell entry of .claude/settings.json read against the Criterion`
>   - tags: `[hooks, harness]`
> - [ ] `guppi/powershellguard.py`: the `PreToolUse` hook on `PowerShell`: it finds every here-string, refuses one whose closing line pipes it into an interpreter by the function of `guppi/bashguard.py`, logs the refusal by `guppi.event` before it says it, and never raises; its docstring holds the mechanism.
> - [ ] `guppi/cli.py`: the command `powershellguard`, and its name in the list of hook commands of the docstring.
> - [ ] `tests/test_powershellguard.py`: `@'` and `@"` here-strings piped into `python -`, `uv run python -` and `node` are refused with the reason and logged; a here-string piped into `Out-File` or to the screen, a quoted string piped into `python`, `python script.py`, a `Bash` payload and an unreadable payload pass; `cli.main(["powershellguard"])` dispatches to the hook.
> - [ ] update `rule-hook-registry`
>   - old: `"command": "uv run guppi bashguard", "timeout": 30 } ] },`
>   - new:
>     ```
>     "command": "uv run guppi bashguard", "timeout": 30 } ] },
>     { "matcher": "PowerShell",
>       "hooks": [ { "type": "command", "command": "uv run guppi powershellguard", "timeout": 30 } ] },
>     ```
>   - change: `guppi powershellguard registered on PreToolUse of PowerShell (case 796.2)`
> - [ ] update `rule-harness`
>   - old: `Eleven more belong here`
>   - new: `Twelve more belong here`
>   - old: `the hook that repairs or names a file a shell call left`
>   - new: `the hook that refuses a PowerShell here-string piped into an interpreter, the hook that repairs or names a file a shell call left`
>   - old: `640, 710.1).`
>   - new: `640, 710.1, 796).`
>   - change: `the PowerShell guard named among the rules in no pipeline (case 796.2)`
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`

> **ratification:**
> ```
> - decision[case 796.2][create][rule-powershell-guard]{ref:rule-harness}{tags:hooks,harness}
> - decision[case 796.2][create][estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter]{ref:rule-powershell-guard}{tags:hooks,harness}
> - decision[case 796.2][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 796.2][update][rule-harness]{ref:rule-harness}
> ```
