## Case 534 — Python in a session prints UTF-8

> **context:**
> The agent often runs its own Python scripts through the Bash tool. On Windows, Python writes console output in the locale's code page. `guppi/cli.py` measured that code page as cp1252 on 2026-09-09. The Bash tool reads those bytes as UTF-8. So a character outside cp1252 stops the script at the print, which is the case `lesson-bash-tool-heredoc-escapes-interpreted` records. A character inside cp1252, such as the dash, goes through without an error and reaches the agent as U+FFFD. Here that happened at the reading of `estimate-context-size-warns-past-the-limit` (reading L4 of `raw/2026-09-30/0138/ledger.md`). The script ran with no encoding set, printed the dash of `guppi context --prompt` as U+FFFD, and the handoff called it a defect of the hook. The transcript of session 876c4080 holds the correct dash in the hook's stdout and in the text the agent received, and no U+FFFD at all. A second run of the same script with `PYTHONIOENCODING=utf-8` printed the dash. The hook needs no fix. The main agent reads that Estimate again and writes a lesson line; neither is part of this Case. Today `.claude/settings.json` has no `env` block. `rule-settings` is its frame, with three children: `rule-default-mode`, `rule-permissions` and `rule-hook-registry`. None of the three owns an environment. The renderer takes a child's text bare into a `.json` target and finds each child by its marker line in the frame. The vault's answer: no page covers the environment of a session. The near pages are `rule-settings`, the frame that gets the new marker line; `lesson-bash-tool-heredoc-escapes-interpreted`, the manual workaround of setting `PYTHONIOENCODING` in each command; and `lesson-hooks-windows-stdin-encoding`, the hook side, already fixed in code. The tags `harness` and `session` fit. The slugs `rule-python-utf8` and `estimate-python-utf8-output-intact` are free. In the frame, four texts contradict the change. The Purpose and the `purpose` of `rule-settings` both say three rules share the file. The Purpose of `rule-hook-registry` says the file is one text of three rules. The Criterion of `estimate-settings` lists the three children and their key order. This Case changes all four. The sentence of `rule-hook-registry` says "several rules" in place of a number, so a later child leaves it true. That page's `estimate-hook-registry-rendered` speaks of the hooks, so a pair in its Purpose leaves it alone. Sub-case 534.2 replaces the Criterion of `estimate-settings` whole. Two of its lines change on purpose: the line on the order of the children now names the fourth child and the key order, and the line on what `rule-settings` holds now names a variable of the environment too. The lesson stands as it is: it records what was true when it was written. `estimate-default-mode` and `estimate-permissions` speak of the `permissions` keys, which do not change. `rule-harness` stays as it is, since the new rule's parent is `rule-settings`.

> **problem:**
> The Bash tool starts each Python process of a session in the locale's code page. Unless each command sets the encoding, a dash reaches the agent as U+FFFD and other characters stop the script. That already produced one false reading and one false Frontier item. The harness should set UTF-8 once, for every Python process of the session, through a ratified rule.

> **recommend:**
> Create the child rule `rule-python-utf8` under `rule-settings`. Its Render is an `env` block with `"PYTHONUTF8": "1"`, placed after `hooks` so that the key order follows the order of `children`. Replace the Criterion of `estimate-settings` for a fourth child. `PYTHONUTF8=1` turns on the UTF-8 mode of Python: the console, the pipes and the default encoding of a file opened without one. `PYTHONIOENCODING=utf-8` was rejected: it covers only the three standard streams and leaves a file opened without an encoding in cp1252.

### Case 534.1 — the env block sets PYTHONUTF8

> **given:**
> `rule-python-utf8` — the new rule; its Render is the `env` block of the settings file
> **＋** `estimate-python-utf8-output-intact` — the promise of the new rule
> **＋** `rule-settings` — the frame of `.claude/settings.json`; takes the marker line of the new child
> **＋** `rule-hook-registry` — a sibling child; its Purpose names the rules that share the file
> **＋** `.claude/settings.json` — the rendered file; its `env` reaches the processes of the session
> **＋** `rule-render-harness` — the renderer; a `.json` target takes a child's text bare
> **＋** the Bash tool of Claude Code — runs the agent's commands in the environment of the session

> **when:**
> A session starts with `.claude/settings.json` as `uv run guppi render` wrote it from `rule-settings`, and the agent runs a Python script through the Bash tool, with no encoding set in the command, that prints a dash and a character outside cp1252.
> **＋** The hooks of `.claude/settings.json` run in the same session.

> **then:**
> `.claude/settings.json` carries `"PYTHONUTF8": "1"` under `env`, the text of `rule-python-utf8`.
> **＋** The script runs in UTF-8 mode, and the dash reaches the agent in the output of the Bash tool as the dash, not as U+FFFD.
> **＋** The character outside cp1252 prints, and the script does not stop at the print.
> **＋** The output of a hook of `.claude/settings.json` reaches the agent as before, its dashes kept.
> **－** The Render of `rule-python-utf8` holds no key other than `PYTHONUTF8`.

> **tasks:**
> - [ ] create `rule-python-utf8`
>   - type: `rule`
>   - kind: `Leaf`
>   - purpose: `Prevents a Python script that a session runs on Windows from printing through the code page of the locale, where a dash reaches the agent as U+FFFD and a character outside the code page stops the script`
>   - enforcement: `render`
>   - governs: `.claude/settings.json`
>   - render_mode: `partial`
>   - ref: `rule-settings`
>   - tags: `[harness, session]`
>   - sections.Purpose:
>     ```
>     Prevents a Python script that a session runs on Windows from printing through the code page of the locale (measured cp1252, `guppi/cli.py`). The Bash tool reads the output as UTF-8: a character outside the code page stops the script at the print, and a character inside it, such as the dash, reaches the agent as U+FFFD without an error. A reading of 2026-09-30 took that mark for a defect of `guppi context --prompt`, while the transcript held the dash (case 534). `PYTHONUTF8=1` in the `env` of `.claude/settings.json` puts every Python process of the session in UTF-8 mode: the console, the pipes and the default encoding of a file opened without one. The `guppi` commands set UTF-8 on their own stdout and stderr in `guppi/cli.py` and do not depend on it.
>     ```
>   - sections.Render:
>     ```
>     <!-- rule-python-utf8 -->
>       "env": {
>         "PYTHONUTF8": "1"
>       }
>     <!-- /rule-python-utf8 -->
>     ```
> - [ ] create `estimate-python-utf8-output-intact`
>   - type: `estimate`
>   - ref: `rule-python-utf8`
>   - kind: `QA`
>   - purpose: `A Python script the agent runs through the Bash tool with no encoding set prints a dash and a character outside cp1252 intact, and the hooks keep their output`
>   - method: `uv run guppi render --check and json.load of .claude/settings.json; then by hand at a later session start: a Python script run through the Bash tool with no encoding in the command prints a dash and a character outside cp1252, and the tool output shows both; the Stop line of guppi context shows its dash`
>   - tags: `[harness, session]`
> - [ ] update `rule-settings`
>   - set: `{purpose: Keeps the rules that share .claude/settings.json from becoming two copies of one file}`
>   - sections.Purpose:
>     ```
>     Keeps the rules that share `.claude/settings.json` from becoming two copies
>     of one file. The permission mode a session opens in, what may be written without a
>     question, which hook fires on which event, and the environment every process of the
>     session runs with are different rules with different criteria, and one file carries
>     them all. This page is the file: its body is the whole of `settings.json`, and each
>     `<!-- child -->` line names the page that owns that text.
>
>     `parent: rule-harness`: the file belongs to no phase of the session.
>     ```
>   - sections.Render:
>     ```
>     <!-- rule-settings -->
>     {
>       "permissions": {
>     <!-- rule-default-mode -->
>     <!-- rule-permissions -->
>       },
>       "hooks": {
>     <!-- rule-hook-registry -->
>       },
>     <!-- rule-python-utf8 -->
>     }
>     <!-- /rule-settings -->
>     ```
>   - change: `a fourth child, rule-python-utf8, owns the env block after hooks`
> - [ ] update `rule-hook-registry`
>   - old: `the file is one text of three rules`
>   - new: `the file is one text of several rules`
>   - change: `the Purpose no longer counts the rules that share .claude/settings.json; rule-python-utf8 joined them`
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-python-utf8-output-intact` at a later session start

> **ratification:**
> ```
> - decision[case 534.1][create][rule-python-utf8]{ref:rule-settings}{tags:harness,session}
> - decision[case 534.1][create][estimate-python-utf8-output-intact]{ref:rule-python-utf8}{tags:harness,session}
> - decision[case 534.1][update][rule-settings]{ref:rule-settings}
> - decision[case 534.1][update][rule-hook-registry]{ref:rule-hook-registry}
> ```

### Case 534.2 — the settings file is rendered from four children

> **given:**
> `estimate-settings` — the promise that the settings file is rendered whole and loads
> **＋** `rule-settings` — the frame of `.claude/settings.json`
> **＋** `rule-default-mode` — the child that owns `defaultMode`
> **＋** `rule-permissions` — the child that owns `allow`
> **＋** `rule-hook-registry` — the child that owns the hooks
> **＋** `rule-python-utf8` — the child that owns `env`
> **＋** `.claude/settings.json` — the rendered file
> **＋** `vault/raw/<date>/event_log.md` — the day's event log that a session start writes to

> **when:**
> `uv run guppi render` writes `.claude/settings.json` from `rule-settings` and its children, and the next session starts from that file.

> **then:**
> The file is the Render of `rule-settings`, and the text of each child replaces its `<!-- child -->` line in the order of `children`: `rule-default-mode`, `rule-permissions`, `rule-hook-registry`, `rule-python-utf8`. That order gives the order of the top-level keys of the file: `permissions`, `hooks`, `env`.
> **＋** The file parses as JSON, and `uv run guppi render --check` exits 0.
> **＋** The next session start writes its `session-start` line into `vault/raw/<date>/event_log.md`, from the hooks of the rendered file.
> **－** `rule-settings` holds no rule of its own about what a hook, a permission or a variable of the environment may be.

> **tasks:**
> - [ ] update `estimate-settings`
>   - set: `{status: pending, purpose: "The settings file is rendered whole from rule-settings and its children, parses as JSON and loads at session start"}`
>   - change: `the Criterion replaced whole — a fourth child, rule-python-utf8, and the env key after hooks`
> - [ ] read `estimate-settings` at a later session start

> **ratification:**
> ```
> - decision[case 534.2][update][estimate-settings]{ref:estimate-settings}
> ```
