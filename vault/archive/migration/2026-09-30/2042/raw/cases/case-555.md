## Case 555 — The other end-of-reply hooks on their own error

> **context:**
> Three `Stop` hooks run after each reply of the main agent, beside the ledger hook and the Spec hook. `guppi casecheck` compares a shown Case with the answer of `case-guppi` that passed the checks. `guppi context` shows the person the size of the context window. `guppi onward` sends the agent from the end of Retro to `/handoff`. Each of the three wraps its whole run in one catch-all handler. When anything inside raises, the hook prints its error to stderr and exits 0. Claude Code does not show the agent the stderr of an exit 0, so nobody sees the error. For example, when the comparison of `guppi casecheck` raises, a Case that differs from the checked answer reaches the person unchecked, and nothing shows it. Case 552.4 gave the ledger hook exit 2 on its own error after the payload is read. Case 554 gave the `Stop` run of `guppi ratified` the same. This Case covers the other three hooks, one sub-case each, because each is its own rule and can fail and be fixed apart. `guppi casecheck` and `guppi onward` take exit 2. `guppi context` only informs, so it shows its error to the person in place of the size line and never blocks. Two more sub-cases add the exception of the hook's own error to an existing promise that the change would make false. Case 555.4 does this for `guppi onward`, whose error now blocks a reply before Retro too. Case 555.5 does it for `guppi context`, whose error now prints a line that does not open with the count. In 555.4, the line of every other case and the line without a `hi` each gain the words "with no error of its own". In 555.5, the line of the size line gains the words "with no error of its own". The check of the answer notes such lines as not carried, and the change is on purpose. The other lines of both Criteria are carried as they stand. What this Case does not do: the `--subagent` run of `guppi casecheck` and the `--prompt` run of `guppi context` keep exit 0. The reason that the later `Stop` check gives, when an error of the `--subagent` run left no Case file, is not reworded. The main agent offered that rewording, and the person agreed to the recommendation without it. How the frame was read. `read_payload` of `guppi/event.py` catches its own errors and returns an empty payload. `read_records` of `guppi/ledger.py` returns nothing for a transcript it cannot read. So an error of `guppi context` rises only while it counts the tokens, and its page keeps its sentence that an unreadable transcript prints nothing. The three rule pages say nothing about a hook's own error. Each sub-case adds that sentence at one anchor, and a Grep of `vault/wiki/` found each anchor once. For `rule-context-size`, the anchor is the end of its paragraph, after the page introduces `--prompt`. `rule-case-check` says the hooks never raise, and that stays true. A Grep of `vault/wiki/` for `rule-context-size|rule-retro-onward|guppi context|guppi onward`, with the hits under `decisions/` left aside, printed `brief.md`, `log.md`, `where-to-stop.md`, `rule-case-check`, `rule-context-size`, `rule-end-of-work`, `rule-harness`, `rule-hook-registry`, `rule-python-utf8`, `rule-retro`, `rule-where-to-stop`, `estimate-context-size-warns-past-the-limit`, `estimate-context-size-shown-after-each-reply`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-python-utf8-output-intact`, `estimate-page-read-cuts-the-history` and `lesson-bash-tool-python-cp1252-dash-shown-as-u-fffd`. The hits in `brief.md` and `log.md` were not read. Of the rest, only `estimate-retro-onward-sends-the-agent-to-the-handoff` and `estimate-context-size-shown-after-each-reply` state what a hook prints or how it exits in a way that its own error would make false, and Cases 555.4 and 555.5 replace their Criteria. `estimate-context-size-warns-past-the-limit` speaks of the text past the limit, which an error does not reach, so it stands. `rule-where-to-stop` and `where-to-stop.md` say that the hook lets a reply that opens with `STOP:` end. That stays true. The hook checks the first word before it reads any file, and even after an error the repeat run ends the reply. A Grep of `vault/wiki/` for `rule-case-check` or `casecheck` near "exit 0", "own error", "swallow" or "never raise" printed `brief.md`, two Decision pages, `rule-spec-reconcile` (about the guard) and a reading line of `estimate-case-check-notes-a-criterion-line-not-carried`. None of them speaks of the `Stop` run's own error, so all of them stand. No test in `tests/test_casecheck.py`, `tests/test_context.py` or `tests/test_onward.py` covers the error path. The Criteria of the Estimates of `rule-case-check` speak of findings, the comparison and the re-fire, not of an error of the hook. The `purpose` of the two reworded Estimates speaks of what the hook does with no error, and is left as it is. The check of the answer noted `then` lines of the sub-cases that share most of their words. They share a shape because the three hooks take one pattern, but each line is a promise of a different hook, and each line names its hook. Every `create` carries a `ref`, so no query of the vault was run. A Glob found no page at the three new slugs.

> **problem:**
> `guppi casecheck`, `guppi context` and `guppi onward` swallow their own errors with exit 0. A Case can then be shown unchecked, the size line can go missing, or the run can stop before `/handoff`, and the agent never sees why. The question is what each hook does on its own error, and how the promise is recorded.

> **recommend:**
> - **How the change is recorded**
>   Recommended: (a) one sub-case per hook that changes, each with a new Estimate for its error path; no existing Estimate changes.
>   Answer: (a), yes. A later question and a later change each made one exception: the existing promises of `guppi onward` and of `guppi context` are reworded, in Cases 555.4 and 555.5.

### Case 555.1 — The Case check blocks on its own error

> **recommend:**
> - **The Case check at the end of a reply**
>   Recommended: (a) block on its own error, as the ledger hook does.
>   Answer: (a), agreed.
> - **The Case check when `case-guppi` answers**
>   Recommended: (a) keep it quiet on its own error, since a send-back would loop and the later refusal keeps a faulty Case from the person.
>   Answer: (a). The person asked why, the main agent explained it, and the person agreed with the recommendation.

> **given:**
> `rule-case-check` — the rule of the check of a Case, on `SubagentStop` and on `Stop`
> **＋** `guppi/casecheck.py` — `run`, its handlers of an error, and the docstring
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `estimate-case-check-exits-2-on-an-error` — the promise this sub-case creates
> **＋** `rule-ledger-write` — the ledger hook, whose handling of its own error this follows

> **when:**
> The `Stop` hook `uv run guppi casecheck` fires, and an exception rises in `guppi/casecheck.py` after the hook has read the payload: while it reads the transcript, the event log or the store, or while it compares a shown Case or reads a sending.

> **then:**
> `guppi casecheck` exits 2. Its stderr holds `casecheck: not checked: <error>` and the advice to show the Case again once the cause is fixed, so the agent sees the error at the end of that reply.
> **＋** While the cause stands, `guppi casecheck` blocks with the same error at every `Stop`.
> **－** An empty or unreadable payload of `guppi casecheck` exits 0 with its line on stderr.
> **－** On the re-fire after a block (`stop_hook_active`), `guppi casecheck` exits 0 and compares nothing, so it cannot loop.
> **－** The run `uv run guppi casecheck --subagent` on `SubagentStop` keeps exit 0 with its error on stderr, since a send-back to `case-guppi` is not ended by `stop_hook_active` and would loop.
> **－** A refusal of `guppi casecheck` with no error keeps its own reason on stderr and its exit 2.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old:
>     ````
>     on the re-fire (`stop_hook_active`) it exits 0.
>     ````
>   - new:
>     ````
>     on the re-fire (`stop_hook_active`) it exits 0. An error of the `Stop` run itself after it has read the payload — an exception while it reads the transcript, the event log or the store, or compares a shown Case or reads a sending — exits 2 with `casecheck: not checked: <error>` and the advice to show the Case again once the cause is fixed on stderr, so the agent sees it at the end of that reply. An empty or unreadable payload exits 0 with its line on stderr. The run of `--subagent` keeps exit 0 with its error on stderr, since a send-back to `case-guppi` is not ended by `stop_hook_active` and would loop; a Case its error left with no file is refused later by the `Stop` check (case 555.1).
>     ````
>   - change: `the Stop run exits 2 on its own error after the payload is read; the --subagent run keeps exit 0 (case 555.1)`
> - [ ] create `estimate-case-check-exits-2-on-an-error`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the Stop run of the Case check exits 2 with the error on stderr when it raises after reading the payload, and exits 0 on the re-fire, on an empty payload and in the --subagent run`
>   - method: `uv run pytest tests/test_casecheck.py — piped payloads, a function of the hook patched to raise`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: `run` reads the payload and returns 0 on an empty one as now; the `--subagent` run keeps a handler that prints `casecheck: not checked: <error>` and returns 0; the `Stop` run has its own handler that prints `casecheck: not checked: <error>` with the advice to show the Case again once the cause is fixed and returns 2; the module docstring says so
> - [ ] `tests/test_casecheck.py`: a patched `against_store` that raises gives exit 2 and the stderr line on `Stop`; the same payload with `stop_hook_active` gives exit 0; an empty payload gives exit 0 and its line; a patched `check_answer` that raises gives exit 0 and the stderr line in `--subagent`
> - [ ] read `estimate-case-check-exits-2-on-an-error` — in a later session

> **ratification:**
> ```
> - decision[case 555.1][update][rule-case-check]{ref:rule-case-check}
> - decision[case 555.1][create][estimate-case-check-exits-2-on-an-error]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 555.2 — The context-size hook shows its own error

> **recommend:**
> - **The context-size hook**
>   Recommended: (a) show the error to the person in place of the size line, and never block.
>   Answer: (a), agreed.

> **given:**
> `rule-context-size` — the rule of the hooks that show the size of the context window
> **＋** `guppi/context.py` — `run`, its handler of an error, and the docstring
> **＋** `tests/test_context.py` — the tests of the hook
> **＋** `estimate-context-size-shows-its-error` — the promise this sub-case creates

> **when:**
> The `Stop` hook `uv run guppi context` fires, and an exception rises in `guppi/context.py` while it counts the tokens of the records it read from the transcript.

> **then:**
> `guppi context` prints JSON with a `systemMessage` of one line, `context: not counted: <error>`, in place of the size line, so the person sees the error after that reply.
> **－** `guppi context` exits 0 on its own error too, so it never blocks the reply.
> **－** On the re-fire after a block (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, `guppi context` prints nothing, as before.
> **－** The run `uv run guppi context --prompt` on `UserPromptSubmit` keeps its error on stderr and exit 0, since a block there would block the person's message.

> **tasks:**
> - [ ] update `rule-context-size`
>   - old:
>     ````
>     below the limit it prints nothing.
>     ````
>   - new:
>     ````
>     below the limit it prints nothing. An error of the hook itself on `Stop` — an exception while it counts the tokens of the records it read — prints a `systemMessage` of one line, `context: not counted: <error>`, in place of the size line, so the person sees it, and exits 0; the run of `--prompt` puts its error on stderr and exits 0, since a block there would block the person's message (case 555.2).
>     ````
>   - change: `the Stop run shows its own error to the person as the systemMessage and still exits 0 (case 555.2)`
> - [ ] create `estimate-context-size-shows-its-error`
>   - ref: `rule-context-size`
>   - kind: `QA`
>   - purpose: `Whether the Stop run of guppi context prints its own error as the systemMessage in place of the size line and exits 0, and the --prompt run keeps its error on stderr with exit 0`
>   - method: `uv run pytest tests/test_context.py — piped payloads, a function of the hook patched to raise`
>   - tags: `[hooks, harness, session]`
> - [ ] `guppi/context.py`: on an exception in the `Stop` run, `run` prints `{"systemMessage": "context: not counted: <error>"}` to stdout and returns 0; in the `--prompt` run it prints `context: not counted: <error>` to stderr and returns 0 as now; the module docstring says so
> - [ ] `tests/test_context.py`: a patched `sizes` that raises gives, on `Stop`, exit 0 and one JSON line whose `systemMessage` opens with `context: not counted:`; the same with `--prompt` gives exit 0, nothing on stdout and the line on stderr
> - [ ] read `estimate-context-size-shows-its-error` — in a later session

> **ratification:**
> ```
> - decision[case 555.2][update][rule-context-size]{ref:rule-context-size}
> - decision[case 555.2][create][estimate-context-size-shows-its-error]{ref:rule-context-size}{tags:hooks,harness,session}
> ```

### Case 555.3 — The Retro hook blocks on its own error

> **recommend:**
> - **The hook that sends the agent on from Retro**
>   Recommended: (a) block on its own error, with the advice to call `/handoff` if Retro has ended and `handoff.md` does not stand.
>   Answer: (a), agreed.

> **given:**
> `rule-retro-onward` — the rule of the `Stop` hook that sends the agent from the end of Retro to `/handoff`
> **＋** `guppi/onward.py` — `run`, its handler of an error, and the docstring
> **＋** `tests/test_onward.py` — the tests of the hook
> **＋** `estimate-retro-onward-exits-2-on-an-error` — the promise this sub-case creates
> **＋** `rule-where-to-stop` — the page that says the hook lets a reply that opens with `STOP:` end

> **when:**
> The `Stop` hook `uv run guppi onward` fires, and an exception rises in `guppi/onward.py` after the hook has read the payload: while it reads the reply, the session folder or the event log.

> **then:**
> `guppi onward` exits 2. Its stderr holds `onward: not checked: <error>` and the advice: if Retro has ended and `handoff.md` does not stand, commit the session folder and call `/handoff`.
> **＋** While the cause stands, `guppi onward` blocks with the same error at every `Stop` of the session, before Retro too.
> **－** An empty payload of `guppi onward` exits 0 with nothing on stderr.
> **－** On the re-fire after a block (`stop_hook_active`), `guppi onward` exits 0 and prints nothing, so it fires at most once a turn.
> **－** With no error, `guppi onward` exits 2 or 0 by its own judgment, as before.

> **tasks:**
> - [ ] update `rule-retro-onward`
>   - old:
>     ````
>     so it fires at most once a turn and cannot loop.
>     ````
>   - new:
>     ````
>     so it fires at most once a turn and cannot loop. An error of the hook itself after it has read the payload — an exception while it reads the reply, the session folder or the event log — exits 2 with `onward: not checked: <error>` on stderr and the advice to commit the session folder and call `/handoff` if Retro has ended and `handoff.md` does not stand, so the agent sees it, before Retro too; on the re-fire it exits 0, so this too fires at most once a turn (case 555.3).
>     ````
>   - change: `the hook exits 2 on its own error after the payload is read, with the advice to call /handoff (case 555.3)`
> - [ ] create `estimate-retro-onward-exits-2-on-an-error`
>   - ref: `rule-retro-onward`
>   - kind: `QA`
>   - purpose: `Whether guppi onward exits 2 with the error and the advice to call /handoff on stderr when it raises after reading the payload, and exits 0 on the re-fire and on an empty payload`
>   - method: `uv run pytest tests/test_onward.py — piped payloads, a function of the hook patched to raise`
>   - tags: `[session, workflow, hooks, harness]`
> - [ ] `guppi/onward.py`: `run` reads the payload and returns 0 on an empty one or on `stop_hook_active` before its handler; the handler prints `onward: not checked: <error>` with the advice to commit the session folder and call `/handoff` if Retro has ended and `handoff.md` does not stand, and returns 2; the module docstring says so
> - [ ] `tests/test_onward.py`: a patched `retro_marked` that raises gives exit 2 and the stderr line with the advice; the same payload with `stop_hook_active` gives exit 0 and nothing on stderr; an empty payload gives exit 0
> - [ ] read `estimate-retro-onward-exits-2-on-an-error` — in a later session

> **ratification:**
> ```
> - decision[case 555.3][update][rule-retro-onward]{ref:rule-retro-onward}
> - decision[case 555.3][create][estimate-retro-onward-exits-2-on-an-error]{ref:rule-retro-onward}{tags:session,workflow,hooks,harness}
> ```

### Case 555.4 — The Retro hook's promise excepts its own error

> **recommend:**
> - **The existing promise of the Retro hook**
>   Recommended: (a) reword that promise in a sub-case of its own, with the hook's own error as an exception; the new Estimate for the error path stays.
>   Answer: (a), agreed.

> **given:**
> `estimate-retro-onward-sends-the-agent-to-the-handoff` — the promise of the judgment of `guppi onward`, whose Criterion this sub-case replaces whole
> **＋** `rule-retro-onward` — the rule of the hook
> **＋** `.claude/settings.json` — the registration of the hook on `Stop`
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the report of the session, whose absence the hook judges
> **＋** `/handoff` — the skill the reason of the hook names
> **＋** `vault/wiki/where-to-stop.md` — the conditions of a deliberate stop that the reason of the hook names

> **when:**
> The `Stop` hook `uv run guppi onward` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, `stop_hook_active` is false, and the reply that ended does not open with `STOP:`.
> **＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
> **＋** In every other case with no error of its own it exits 0 and prints nothing: before the mark `retro`, once `handoff.md` stands, on a reply that follows a refusal of a `Stop` hook, and on a reply that opens with `STOP:`.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck` and `uv run guppi context`.
> **－** It counts nothing, reads no test result and calls no model: its judgment is the mark, the file, the flag and the first word of the reply.
> **－** Without a `hi` of the session in the event log, and with no error of its own, it exits 0.
> **－** It writes no file and no mark.

> **tasks:**
> - [ ] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the exits 0 of the judgment hold with no error of the hook's own (case 555.4)`
> - [ ] read `estimate-retro-onward-sends-the-agent-to-the-handoff` — in a later session

> **ratification:**
> ```
> - decision[case 555.4][update][estimate-retro-onward-sends-the-agent-to-the-handoff]{ref:rule-retro-onward}
> ```

### Case 555.5 — The size-line promise excepts the hook's own error

> **recommend:**
> - **Change**
>   Asked: the check before the Spec found that the promise of the size line, `estimate-context-size-shown-after-each-reply`, becomes false when the hook prints its own error in place of the size line. The person chose to treat it the way the promise of the Retro hook is treated.
>   Taken: a sub-case of its own replaces that Criterion whole. Its line on the size line holds with no error of the hook's own, and every other line stands as it was.

> **given:**
> `estimate-context-size-shown-after-each-reply` — the promise of the size line of `guppi context`, whose Criterion this sub-case replaces whole
> **＋** `rule-context-size` — the rule of the hook

> **when:**
> The `Stop` hook `uv run guppi context` runs after a reply of the main agent and reads the transcript at `transcript_path`.

> **then:**
> With no error of its own, the hook prints JSON with a `systemMessage` of one line that opens with `context: <N> tokens (<+D> since the last reply)`.
> **＋** N is the sum of the input, cache read, cache creation and output tokens of the last main-agent API call the transcript holds; D is N less the same sum at the last main-agent call before the person's last prompt.
> **＋** The records of a subagent (`isSidechain`) are not counted.
> **＋** On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, the hook prints nothing.
> **－** The hook never blocks: it exits 0 in every case.

> **tasks:**
> - [ ] update `estimate-context-size-shown-after-each-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the size line holds with no error of the hook's own (case 555.5)`
> - [ ] read `estimate-context-size-shown-after-each-reply` — in a later session

> **ratification:**
> ```
> - decision[case 555.5][update][estimate-context-size-shown-after-each-reply]{ref:rule-context-size}
> ```
