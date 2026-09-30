<!-- approved 23:40:41 · session 9f03d486 -->

# Spec — session 2042, 2026-09-30

## Case 554 — The Spec hook exits 2 on its own error

> **context:**
> The `Stop` hook `uv run guppi ratified` of `rule-spec-write` copies each ratified Case into the plan file and into `spec.md`. Its whole run sits inside one catch-all handler. When anything inside the run raises, the hook prints `ratified: not done: <error>` to stderr and exits 0. Claude Code does not show the agent the stderr of an exit 0, so the error goes unseen and any Case still waiting in that run is not written. In session 1736 a malformed estimate line in the same reply as the defer of Case 551 made `parse_line` raise. The hook caught the error and exited 0, and Case 551 landed only at its second showing. That is why `estimate-spec-write-writes-a-defer` is `failed`. Case 552.1 fixed `parse_line`, so that line no longer raises, but any other fault in the hook would still be silent. Case 552.4 gave the ledger hook `guppi/ledger.py` exit 2 on its own error once the payload is read, and exit 0 on an error while it reads the payload. This Case gives the `Stop` run of `guppi ratified` the same behaviour. The guard `guppi ratified --guard` of `rule-spec-reconcile` keeps exit 0. The page of that rule says the guard never raises, and that stays true, so the page is not changed. The other `Stop` hooks (`guppi casecheck`, `guppi context`, `guppi onward`) are left to their own Frontier line. How the frame was read:
> - The `How it works` section of `rule-spec-write` states the exit codes of the hook but not the handling of its own error. The new sentence goes at the end of that section, after the sentence on removing a superseded Case. There the refusals that say "the same way" still point to the refusal they meant.
> - The docstring of `guppi/ratified.py` says the hook never raises, and it also describes the guard. It is updated in code.
> - A Grep of `vault/wiki/` for "own error", "swallow" and "never raises" printed hits outside `decisions/` in these places:
>   - `rule-bash-guard` and `estimate-bash-guard` say that `guppi guard` never raises. That is another hook, so they stand.
>   - `rule-spec-reconcile` says that the guard of `guppi ratified` never raises. The guard is unchanged, so it stands.
>   - `lesson-ledger-hook-swallows-a-parse-error` is a recorded fact about the ledger hook, so it stands.
>   - The History of `rule-ledger-write`, `brief.md` and `log.md` are not read.
> - No Criterion of the Estimates of `rule-spec-write` speaks of the hook's own error. They speak of refusals and of the re-fire, and those stay.
> - The `create` carries a `ref`, so no query of the vault was run. A Glob found no page at the slug `estimate-spec-write-exits-2-on-an-error`.
>
> `estimate-spec-write-writes-a-defer` is not touched. Its Criterion is sound, and it failed only because the error was swallowed. It stays `failed` until a later session reads it again by its own method, on the first defer after this change. That reading is not a task of this Case.

> **problem:**
> The `Stop` run of `guppi ratified` swallows its own errors with exit 0. A Case due to be written is then lost, and no sign reaches the agent. This is how the first showing of Case 551 was lost. The question is what the hook does on its own error, whether the guard changes with it, whether the other `Stop` hooks join, and how the promise is recorded.

> **recommend:**
> - **What the Stop run does when it raises**
>   Recommended: (a) exit 2, as the ledger hook does. An error after the payload is read exits 2, the message names the error and says to repeat the ledger lines. An error while reading the payload still exits 0. The re-fire still does nothing.
>   Answer: (a) exit 2, as the ledger hook does.
> - **The edit guard of the same command**
>   Recommended: (a) only the Stop run changes. The guard keeps exit 0 on its own error.
>   Answer: (a) only the Stop run changes.
> - **The other end-of-reply hooks**
>   Recommended: (a) this Case covers `guppi ratified` alone. The other three hooks are decided under their own Frontier item.
>   Answer: (a). Those hooks have their own item in the Frontier and are taken separately.
> - **How the promise is recorded**
>   Recommended: (a) a new Estimate for the error path. The failed Estimate keeps its wording and is read again in a later session.
>   Answer: (a) a new Estimate for the error path; the failed one is read again later.

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case into the Spec
> **＋** `guppi/ratified.py` — `run`, its handler of an error, and the docstring
> **＋** `tests/test_ratified.py` — the tests of the hook
> **＋** `estimate-spec-write-exits-2-on-an-error` — the promise this Case creates
> **＋** `rule-spec-reconcile` — the rule of the guard `uv run guppi ratified --guard` in the same command, which stays as it is

> **when:**
> The `Stop` hook `uv run guppi ratified` fires, and an exception rises in `guppi/ratified.py` after the hook has read the payload: while it reads the transcript, the store, the plan file or `spec.md`, or while it writes, removes or checks a Case.

> **then:**
> The hook exits 2. Its stderr holds `ratified: not done: <error>` and the advice to repeat the ledger lines once the cause is fixed, so the agent sees the error at the end of that reply.
> **＋** A Case of the reply that was not written when the error rose is written at the reply that repeats its ledger lines.
> **＋** A Case written before the error stays written, and the repeat replaces its section.
> **－** An error while the hook reads the payload exits 0 with the error on stderr. The hook cannot tell a re-fire at that point, and exit 2 could loop.
> **－** With `stop_hook_active` (the re-fire after a block), the hook exits 0 and writes nothing, so it cannot loop.
> **－** The guard `uv run guppi ratified --guard` keeps exit 0 with its line on stderr on its own error.
> **－** A refusal of the hook with no error keeps its own reason on stderr and its own exit.

```then
create:
- slug: estimate-spec-write-exits-2-on-an-error
  ref: rule-spec-write
  kind: QA
  purpose: Whether the Spec hook exits 2 with the error on stderr when its Stop run raises after reading the payload, and exits 0 on an error while reading the payload, on the re-fire and in the guard
  method: uv run pytest tests/test_ratified.py — piped payloads, a function of the hook patched to raise
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-spec-write
  replace:
  - old: a Case N none of them holds is no refusal (case 441).
    new: 'a Case N none of them holds is no refusal (case 441). An error of the hook itself after it has read the payload — an exception while it reads the transcript, the store, the plan file or `spec.md`, or writes, removes or checks a Case — exits 2 with `ratified: not done: <error>` and the advice to repeat the ledger lines once the cause is fixed on stderr, so the agent sees it at the end of that reply; a Case not yet written is written at the reply that repeats its lines, and one written before the error stays and is replaced then. An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell a re-fire then; the guard of `rule-spec-reconcile` keeps exit 0 on its own error (case 554).'
  change: the Stop hook exits 2 on its own error after the payload is read, and 0 on an error while it reads the payload (case 554)
```

```tasks
- [ ] update `rule-spec-write`
- [ ] create `estimate-spec-write-exits-2-on-an-error`
- [x] `guppi/ratified.py`: `run` reads the payload in its own handler that prints the error and returns 0; the handler of the guard prints the error and returns 0; the handler of the `Stop` run prints `ratified: not done: <error>` with the advice to repeat the ledger lines and returns 2; the docstring says so
- [x] `tests/test_ratified.py`: a patched `write_case` that raises gives exit 2 and the stderr line; the same payload with `stop_hook_active` gives exit 0 and writes nothing; a payload that cannot be read gives exit 0 and the stderr line; a patched `guard_refusal` that raises gives exit 0 in `--guard`
- [ ] read `estimate-spec-write-exits-2-on-an-error` — in a later session
```

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

```then
create:
- slug: estimate-case-check-exits-2-on-an-error
  ref: rule-case-check
  kind: QA
  purpose: Whether the Stop run of the Case check exits 2 with the error on stderr when it raises after reading the payload, and exits 0 on the re-fire, on an empty payload and in the --subagent run
  method: uv run pytest tests/test_casecheck.py — piped payloads, a function of the hook patched to raise
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: on the re-fire (`stop_hook_active`) it exits 0.
    new: 'on the re-fire (`stop_hook_active`) it exits 0. An error of the `Stop` run itself after it has read the payload — an exception while it reads the transcript, the event log or the store, or compares a shown Case or reads a sending — exits 2 with `casecheck: not checked: <error>` and the advice to show the Case again once the cause is fixed on stderr, so the agent sees it at the end of that reply. An empty or unreadable payload exits 0 with its line on stderr. The run of `--subagent` keeps exit 0 with its error on stderr, since a send-back to `case-guppi` is not ended by `stop_hook_active` and would loop; a Case its error left with no file is refused later by the `Stop` check (case 555.1).'
  change: the Stop run exits 2 on its own error after the payload is read; the --subagent run keeps exit 0 (case 555.1)
```

```tasks
- [ ] update `rule-case-check`
- [ ] create `estimate-case-check-exits-2-on-an-error`
- [x] `guppi/casecheck.py`: `run` reads the payload and returns 0 on an empty one as now; the `--subagent` run keeps a handler that prints `casecheck: not checked: <error>` and returns 0; the `Stop` run has its own handler that prints `casecheck: not checked: <error>` with the advice to show the Case again once the cause is fixed and returns 2; the module docstring says so
- [x] `tests/test_casecheck.py`: a patched `against_store` that raises gives exit 2 and the stderr line on `Stop`; the same payload with `stop_hook_active` gives exit 0; an empty payload gives exit 0 and its line; a patched `check_answer` that raises gives exit 0 and the stderr line in `--subagent`
- [ ] read `estimate-case-check-exits-2-on-an-error` — in a later session
```

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

```then
create:
- slug: estimate-context-size-shows-its-error
  ref: rule-context-size
  kind: QA
  purpose: Whether the Stop run of guppi context prints its own error as the systemMessage in place of the size line and exits 0, and the --prompt run keeps its error on stderr with exit 0
  method: uv run pytest tests/test_context.py — piped payloads, a function of the hook patched to raise
  tags:
  - hooks
  - harness
  - session
update:
- slug: rule-context-size
  replace:
  - old: below the limit it prints nothing.
    new: 'below the limit it prints nothing. An error of the hook itself on `Stop` — an exception while it counts the tokens of the records it read — prints a `systemMessage` of one line, `context: not counted: <error>`, in place of the size line, so the person sees it, and exits 0; the run of `--prompt` puts its error on stderr and exits 0, since a block there would block the person''s message (case 555.2).'
  change: the Stop run shows its own error to the person as the systemMessage and still exits 0 (case 555.2)
```

```tasks
- [ ] update `rule-context-size`
- [ ] create `estimate-context-size-shows-its-error`
- [x] `guppi/context.py`: on an exception in the `Stop` run, `run` prints `{"systemMessage": "context: not counted: <error>"}` to stdout and returns 0; in the `--prompt` run it prints `context: not counted: <error>` to stderr and returns 0 as now; the module docstring says so
- [x] `tests/test_context.py`: a patched `sizes` that raises gives, on `Stop`, exit 0 and one JSON line whose `systemMessage` opens with `context: not counted:`; the same with `--prompt` gives exit 0, nothing on stdout and the line on stderr
- [ ] read `estimate-context-size-shows-its-error` — in a later session
```

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

```then
create:
- slug: estimate-retro-onward-exits-2-on-an-error
  ref: rule-retro-onward
  kind: QA
  purpose: Whether guppi onward exits 2 with the error and the advice to call /handoff on stderr when it raises after reading the payload, and exits 0 on the re-fire and on an empty payload
  method: uv run pytest tests/test_onward.py — piped payloads, a function of the hook patched to raise
  tags:
  - session
  - workflow
  - hooks
  - harness
update:
- slug: rule-retro-onward
  replace:
  - old: so it fires at most once a turn and cannot loop.
    new: 'so it fires at most once a turn and cannot loop. An error of the hook itself after it has read the payload — an exception while it reads the reply, the session folder or the event log — exits 2 with `onward: not checked: <error>` on stderr and the advice to commit the session folder and call `/handoff` if Retro has ended and `handoff.md` does not stand, so the agent sees it, before Retro too; on the re-fire it exits 0, so this too fires at most once a turn (case 555.3).'
  change: the hook exits 2 on its own error after the payload is read, with the advice to call /handoff (case 555.3)
```

```tasks
- [ ] update `rule-retro-onward`
- [ ] create `estimate-retro-onward-exits-2-on-an-error`
- [x] `guppi/onward.py`: `run` reads the payload and returns 0 on an empty one or on `stop_hook_active` before its handler; the handler prints `onward: not checked: <error>` with the advice to commit the session folder and call `/handoff` if Retro has ended and `handoff.md` does not stand, and returns 2; the module docstring says so
- [x] `tests/test_onward.py`: a patched `retro_marked` that raises gives exit 2 and the stderr line with the advice; the same payload with `stop_hook_active` gives exit 0 and nothing on stderr; an empty payload gives exit 0
- [ ] read `estimate-retro-onward-exits-2-on-an-error` — in a later session
```

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

```then
update:
- slug: estimate-retro-onward-sends-the-agent-to-the-handoff
  set:
    status: pending
  change: the Criterion replaced whole — the exits 0 of the judgment hold with no error of the hook's own (case 555.4)
```

```tasks
- [ ] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
- [ ] read `estimate-retro-onward-sends-the-agent-to-the-handoff` — in a later session
```

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

```then
update:
- slug: estimate-context-size-shown-after-each-reply
  set:
    status: pending
  change: the Criterion replaced whole — the size line holds with no error of the hook's own (case 555.5)
```

```tasks
- [ ] update `estimate-context-size-shown-after-each-reply`
- [ ] read `estimate-context-size-shown-after-each-reply` — in a later session
```

## Case 556 — The method of the Estimate schema promise runs the test of `method`

> **context:**
> `estimate-estimates-schema-checked` promises that lint checks every Estimate page against its schema. One line of its Criterion promises that a page without a `method` field gets the finding `schema: missing field method`. The page's `method` field is the command that checks the promise: `pytest tests/test_schemas.py -k estimates`. pytest matches `-k` against the test names. The shared tests that run once per category are labelled with the category name, so `estimates` selects them. The test of a page without `method` is `test_an_estimate_without_method_is_one_finding`. Its name holds `estimate` but not `estimates`, so the filter skips it. The reading of 2026-09-29, "4 passed, 1 skipped", fits the five shared tests alone. So the page stands `passed` on a run that never checked the line about `method`. The handoff of session 1736 recorded this gap, and case 548 noted it and left it for a later session. Case 548 fixed the same gap on `estimate-decisions-schema-checked` with the singular filter `-k decision`. This Case follows that fix. The new method runs `-k estimate`. By a read of `tests/test_schemas.py`, that filter selects the five shared tests for Estimate pages and the test of a page without `method`, and no other test. The method text also names a page without `method` among its steps. The new method keeps two of the forms that the Render of `rule-estimates-schema` asks of a `method`: the word `pytest`, and a path under `tests/` that exists. The page goes back to `pending`. Its Criterion is written back word for word, since only a replaced Criterion sets `pending`. `rule-ledger-write` refuses a reading of a promise that a decision line of the same session updates, so the reading with the new command waits for a later session. Until then, the cascade of `generate` sets `rule-estimates-schema` from `built` to `draft`, since its one Estimate no longer stands `passed`. A Grep of the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` for `estimate-estimates-schema-checked` found `brief.md`, `log.md` and the `estimates` field of `rule-estimates-schema`. `brief.md` and `log.md` were not read for this, and the field only links the promise. So no other live text repeats the method. A Grep of `vault/wiki/estimates/` for methods that run `tests/test_schemas.py` found the six schema Estimates. The four for entities, lessons, insights and rules run `-k` with their category name. The file holds no test for those four categories beyond the shared ones, so their filters miss nothing. The docstring of `tests/test_schemas.py` names `estimate-<category>-schema-checked` in general terms, and it stays true. No reader of a text changes, so no old form needs to be kept. This Case creates no page, so no vault query ran.

> **problem:**
> The method of `estimate-estimates-schema-checked` selects the tests by a name that the test of a page without `method` does not contain. So the reading behind the page's `passed` never ran the test of one of its promises. The question is how the method selects that test, and whether the page waits for a new reading.

> **recommend:**
> - **How should the method select the test for a missing `method`?**
>   - Recommended: (a) the singular filter `-k estimate`, as the method of `estimate-decisions-schema-checked` uses, with the method text naming a page without `method`; no code change.
>   - Answer: (a). The person asked for a plain explanation first, and then agreed with the recommendation.
> - **Should the page go back to waiting for a new reading?**
>   - Recommended: (a) set the page `pending`, write its Criterion back word for word, and read it with the new command in a later session.
>   - Answer: (a). The person agreed with the recommendation after the explanation.

> **given:**
> `estimate-estimates-schema-checked` — the promise of the Estimate schema, whose method and status this Case sets
> **＋** `tests/test_schemas.py` — the tests of the page schemas on the live files, which the method selects by name
> **＋** `pytest tests/test_schemas.py -k estimate` — the command of the new method
> **＋** `make lint` — the live reading the method names
> **＋** `wiki/estimates/` — the folder of the Estimate pages that `make lint` reads
> **＋** `rule-estimates-schema` — the rule the promise belongs to, whose Render sets the forms of a `method`
> **＋** `rule-ledger-write` — the rule that holds a reading of a promise the session changes for a later session

> **when:**
> The reading of `estimate-estimates-schema-checked` follows its method.

> **then:**
> The method of `estimate-estimates-schema-checked` runs `pytest tests/test_schemas.py -k estimate`, which selects the tests for each category on an Estimate page and the test of an Estimate page without `method`.
> **＋** The method names a page in the shape, a page without `method`, then one defect at a time, and expects no schema finding on `wiki/estimates/` in `make lint`.
> **＋** `estimate-estimates-schema-checked` stands `pending` until a reading with the new method, and `rule-estimates-schema` stands `draft` until that reading passes.
> **－** The text of the Criterion of `estimate-estimates-schema-checked` does not change.
> **－** `tests/test_schemas.py` does not change.
> **－** The reading of `estimate-estimates-schema-checked` is not taken in this session, as `rule-ledger-write` requires.

```then
update:
- slug: estimate-estimates-schema-checked
  set:
    status: pending
    method: pytest tests/test_schemas.py -k estimate on the live vault/wiki/estimates/schema.yaml — a page in the shape, a page without method, then one defect at a time; the live reading make lint, no schema finding on wiki/estimates/
  sections:
    Criterion: |-
      When:
      `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

      Then:
      The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
      **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
      **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
      **＋** `fields` and `sections` describe each name of these lists; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
      **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.
  change: the method runs -k estimate and names a page without method, so the test of method runs; the reading is due again, the Criterion stands (case 556)
```

```tasks
- [ ] update `estimate-estimates-schema-checked`
- [x] `uv run pytest tests/test_schemas.py -k estimate --collect-only -q`: the tests for each category on `estimates` and `test_an_estimate_without_method_is_one_finding` are listed, and no other test
- [ ] read `estimate-estimates-schema-checked` — in a later session: `uv run pytest tests/test_schemas.py -k estimate`, then `make lint`
```

## Case 557 — `case-guppi` checks moments and searches, records each question as it was answered, and lists what a round decides

> **context:**
> `case-guppi` builds every Case from the instruction in `.claude/agents/case-guppi.md`, which is rendered from `rule-case-build`. Three readings of that instruction failed in session 1736, and the handoff carried each one on as a fix to decide. First, `estimate-case-build-checks-the-finished-case`: at `/pre-spec`, `ask-guppi` found three faults the builder's own check had missed. Case 547 widened the Frontier rule to cover the first reply of `/hi`, whose form `rule-skill-hi` sets. The builder's Grep for `Frontier` over `.claude/` printed `.claude/skills/hi/SKILL.md`, but only its passage on a later reply was judged, and the summary line of `rule-skill-hi` says nothing about the Frontier. Case 548 said a Grep found only the page and `brief.md`, while it printed `brief.md`, `log.md` and `rule-decisions-schema`. Case 552 listed the hits of `parse_line` without three of them. Second, `estimate-case-build-records-the-rounds-in-recommend`: the item of Case 549 on how the texts state the condition kept its first recommendation after the next question settled it the other way, which goes against the rule that asks for the latest one. Third, `estimate-case-build-writes-a-plain-round`: the sentence on what a first round decides ran parallel clauses inside one sentence on Cases 548 and 550, and the Context of Case 547 named five examples in one sentence. `.claude/skills/grill-me/SKILL.md` sets such a series one item per line. Case 551 put `rule-case-build` off over that third fault, so the page carries `deferred_by` and stands in `backlog.md`. The Frontier of this session names the three faults as its items C4, C6 and C9, and the person took all three into this Case. Its sub-case 557.3 decides the fault of Case 551 and carries `{supersedes:case 551}`, so the defer is retired and the page leaves the backlog. The Frontier lines come from the brief, not the backlog, so the check of `rule-case-check` on backlog lines does not apply. The rule stands `draft`.
> The Case was ratified, then built again after each of two reports of `ask-guppi` at `/pre-spec`. The first report raised four points. The new text of 557.1 had dropped the clause that a claim of `context` names the search it rests on, while its `then` kept it. The text now keeps it. The new text of 557.3 wrote a list shape of its own, against the line of `estimate-case-build-writes-a-plain-round` that asks the instruction to point each list to `.claude/skills/grill-me/SKILL.md` and word no shape of its own. The person chose to have the text name the two places and point to the template for the shape. `estimate-case-check-requires-each-question-of-the-rounds` asks that every question title of the rounds have an item in `recommend`, but 557.2 gave an item only to an answered question. The person chose that a question never answered still gets one item that says so, so that promise stands and is named in 557.2. The count of **＋** lines in the new Criterion of 557.1 was corrected. The second report found two more points. The `then` of 557.3 set every series of examples as a list, which is wider than `estimate-skill-grill-me-asks-in-rounds`, where a short series of words inside a sentence stays in it. That Estimate now stands in the `given` of 557.3, and the `then` says a series falls under the template's list rule like any other series. The text also said "when it has two or more parts", while the same paragraph already uses "part" for the parts of the Context. It now says "when it names two or more decisions". The second point was the list of hits of one Grep below, which had left out `entity-glossary`.
> This Case holds only `update` items, so no vault query ran. It adds no hook and changes no code. The hook of `rule-case-check` reads only the bold title of each `recommend` item, by `recommend_titles` in `guppi/casecheck.py`, which reads the top level of the list. So the sub-items that 557.2 sets need no old form in any reader. `tests/test_casecheck.py`, `tests/test_ratified.py` and `tests/test_generate.py` already write `Recommended:` and `Answer:` as sub-items. All five Estimates of `rule-case-build` were read. Two have their Criterion replaced whole. The new Criterion of 557.1 carries each old line word for word and adds two, so it holds seven **＋** lines. The new Criterion of 557.2 rewrites its first line and drops the line on the latest recommendation, as the person's choice sets, and carries its other lines word for word. `estimate-case-build-writes-a-plain-round` asks for a list one item per line in the Context, and for an instruction that points to the template, which the new text of 557.3 does. So it stands, stays `failed` until a reading after the render, and leaves what counts as a list to `estimate-skill-grill-me-asks-in-rounds`, which also stands. `estimate-case-build-writes-the-case` says the Context is one prose paragraph. That stays true, because a list inside it has been allowed since case 512. `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` speaks of readers in code and is not touched.
> Searches, outside `vault/raw/` and `vault/archive/`. A Grep for `Recommended:|both the latest|the latest recommendation|latest answer` printed 20 files: `case-schema.md`, `decisions/schema.yaml`, `.claude/agents/case-guppi.md`, `log.md`, nine Decision pages from `decision-case-547` to `decision-case-552.4`, `estimate-case-build-records-the-rounds-in-recommend`, `rule-case-build`, `rule-case-protocol`, `rule-decisions-schema` and the three tests above. The pages and renders among them enter 557.2, and `log.md` and the Decision pages were not read. A Grep for `[Rr]ecommend` over `vault/wiki/estimates/` printed 16 pages. Beyond the two Estimates of this Case and `estimate-case-check-requires-each-question-of-the-rounds`, each speaks of where `recommend` stands or how it is copied, not of what its items say. `estimate-case-protocol-case-form` points to the Sections table of `case-schema.md` and stays true. A Grep for `[Rr]ecommend|latest` over `glossary.md`, `vault/wiki/entities/`, `.claude/skills/`, `.claude/agents/` and `guppi/*.py` printed 12 files: `glossary.md`, `entity-glossary`, `.claude/skills/grill-me/SKILL.md`, `.claude/skills/wait-what/SKILL.md`, `.claude/agents/case-guppi.md`, `guppi/ratified.py`, `guppi/materialize.py`, `guppi/generate.py`, `guppi/casecheck.py`, `guppi/context.py`, `guppi/cleanup.py` and `guppi/archive.py`. The glossary rows name the section. The two skills speak of the recommended answer of a question. `ratified.py`, `materialize.py` and `generate.py` carry the section as text, and `casecheck.py` reads its titles. `context.py`, `cleanup.py`, `archive.py` and a docstring of `materialize.py` use "recommended" or "latest" in other senses. `case-guppi.md` is the render this Case changes. None of them is made false. A Grep for `judge them by meaning|names the search it rests on|search it rests on|by meaning` printed 27 files. Besides `rule-case-build`, its render and its Estimate, the live hits in `rule-ask`, `.claude/agents/ask-guppi.md`, `glossary.md`, `entity-glossary`, `rule-synthesis`, `.claude/agents/librarian-guppi.md`, `estimate-synthesis-clusters` and `estimate-ask-finds` speak of how `ask-guppi` and the synthesis compare pages. `brief.md`, `log.md` and 14 Decision pages were not read. A Grep for `rule-case-build` outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed 19 files. None of their lines states the check, the form of `recommend` or the Context of a round, except the pages this Case changes. `insight-case-form-chat-form-read-by-no-script`, near item C6, is about the main agent's own text before a round, which is item C5, and stays `open`.

> **problem:**
> The instruction of `case-guppi` does not tell it to look for other rules that act at the moment a change sets, and it does not tell it to report what a search printed, so faults reached `/pre-spec`. It asks a `recommend` item to give the latest recommendation even when a later question with its own title replaced it, which rewrites the record of the choice. It lets the Context of a first round run what the round decides and a series of examples inside one sentence, against the list rule of `grill-me`, and that fault holds the rule in the backlog.

> **recommend:**
> - **How does this Case stand next to the put-off rule and the two other items on it?**
>   - Recommended: (a) this Case alone, for the check only, with the put-off decision left for the Case on the plain-round item.
>   - Answer: (b) one Case for all three items on the rule, in sub-cases; the plain-round sub-case retires the put-off decision.
> - **Change**
>   - Asked: at the second pre-spec, the fix of the two points the report of `ask-guppi` found.
>   - Taken: `estimate-skill-grill-me-asks-in-rounds` stands in the `given` of 557.3, whose `then` puts a series of examples under the template's list rule like any other series; the text says "when it names two or more decisions"; the list of live hits of the Grep for `by meaning` in `context` names `entity-glossary`.

### Case 557.1 — `case-guppi` searches for rules at the same moment and reports what a search printed

> **recommend:**
> - **How should the check before a Case is shown be fixed?**
>   - Recommended: (a) sharpen the instruction on both points: search for rules that act at the moment the change sets, and report what a search printed; the Estimate's Criterion replaced to match.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render paragraph on the check of the finished Case changes
> **＋** `.claude/agents/case-guppi.md` — the render of `rule-case-build`, read by `case-guppi` at each dispatch
> **＋** `.claude/agents/ask-guppi.md` — the recipe whose index lines the check reads by meaning
> **＋** `vault/wiki/rules/` — the rule pages the check searches for the moment a change sets
> **＋** `.claude/` — the harness files the check searches for the same moment
> **＋** `estimate-case-build-checks-the-finished-case` — the promise of the check, its Criterion replaced whole

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one.
> **＋** Where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit.
> **＋** For a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands, and a claim of `context` about every text names the search it rests on.
> **＋** A claim of `context` about a search names its pattern and the paths it ran over, lists each file the search printed, a file it does not read included, or gives the count it printed, and claims nothing the search did not print.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: rule-case-build
  replace:
  - old: For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. Each hit the change makes false enters the Case, or `context` says why it stands, and a claim of `context` about every text names the search it rests on.
    new: For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. When the change sets what happens at a moment — a reply, a hook event, a command — Grep `vault/wiki/rules/` and `.claude/` for the words that name that moment, read each passage of each hit that sets a form or a behaviour at that moment, and bound the Case so that it does not cover that moment, or name the other rule in `given` (case 557.1). Each hit the change makes false enters the Case, or `context` says why it stands, and a claim of `context` about every text names the search it rests on. A claim of `context` about a search names its pattern and the paths it ran over, and lists each file the search printed, a file it does not read included, or gives the count the search printed; it claims nothing the search did not print (case 557.1).
  change: case-guppi searches the rules and .claude/ for the moment a change sets, and a claim of context about a search lists what the search printed (case 557.1)
- slug: estimate-case-build-checks-the-finished-case
  set:
    status: pending
    purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, what each search printed, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec
    method: 'by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a claim of context that its search did not print, two sub-cases whose texts on one page contradict; the count of each in the reading line'
  change: the Criterion replaced whole — the search for rules at the same moment, and a claim about a search that lists what it printed (case 557.1)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-checks-the-finished-case`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-checks-the-finished-case` — in a later session, at `/pre-spec` after the render
```

### Case 557.2 — `recommend` records each question as it was answered

> **recommend:**
> - **How should an item of `recommend` read when a later question replaced its recommendation?**
>   - Recommended: (b) each item keeps what was asked and answered at the time, with the title in bold and the sub-items `Recommended:` and `Answer:` as they stood when it was answered; a later question that replaced it is its own item; a question asked again is one item; a question the person left unanswered is asked again, and one never answered gets a short item that says so; `rule-case-protocol` and its render change too.
>   - Answer: the person proposed to record every answered question with its recommendation and answer as sub-items, asked how costly it is for `case-guppi` to place each item under its sub-case, and asked for an example first; after the example and the explanation, (b); a later question added the short item for a question never answered.
> - **What happens to a question that never got an answer, now that `recommend` holds only answered questions?**
>   - Recommended: (a) an unanswered question still gets a short item: its `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did; the check and its promise do not change.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render paragraph on how it writes `recommend` changes
> **＋** `.claude/agents/case-guppi.md` — the render of `rule-case-build`
> **＋** `rule-case-protocol` — its Render sets the form of `recommend` in the Sections table and the Language paragraph
> **＋** `vault/wiki/case-schema.md` — the render of `rule-case-protocol`, loaded by `/hi`
> **＋** `rule-decisions-schema` — its Render describes the `## Recommend` of a Decision page
> **＋** `vault/wiki/decisions/schema.yaml` — the render of `rule-decisions-schema`, read by `guppi lint`
> **＋** `estimate-case-build-records-the-rounds-in-recommend` — the promise of the record, its Criterion replaced whole
> **＋** `estimate-case-check-requires-each-question-of-the-rounds` — the promise of the hook of `rule-case-check` that each question title of the rounds has an item in `recommend`

> **when:**
> `case-guppi` answers with a Case, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, with a sub-item `Recommended:` with what the agent recommended and a sub-item `Answer:` with the person's answer in English, both as they stood when the person answered that question.
> **＋** A later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer.
> **＋** A question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it.
> **＋** A question the person left unanswered is asked again in the next round under the same title; a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did.
> **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
> **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
> **＋** An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, and the other items stand in the parent's `recommend`.
> **＋** A Case with sub-cases carries `problem` on the parent only.
> **－** No item quotes the person's words word for word.
> **－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.

```then
update:
- slug: rule-case-build
  replace:
  - old: 'Write `recommend` as the schema sets it: one item per question of your rounds on the Case, its first line the title of the question in bold as the round wrote it, then a line `Recommended:` with what you recommended and a line `Answer:` with the person''s answer in English, both the latest where a later question changed them;'
    new: 'Write `recommend` as the schema sets it: one item per question of your rounds on the Case, its first line the title of the question in bold as the round wrote it, then a sub-item `Recommended:` with what you recommended and a sub-item `Answer:` with the person''s answer in English, both as they stood when the person answered that question; a later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer; a question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it; a question the person left unanswered you ask again in your next round under the same title, and a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did (case 557.2);'
  change: recommend holds one item per question, its recommendation and answer as they stood when the person answered it, as sub-items; a question never answered says so (case 557.2)
- slug: rule-case-protocol
  replace:
  - old: one item per question of the rounds of `case-guppi` — the question, what it recommended, the person's answer in English, both the latest — one per change
    new: one item per question of the rounds of `case-guppi` — the question, what it recommended, the person's answer in English, both as they stood when the person answered it, or a note that it was not answered (case 557.2) — one per change
  - old: '`recommend` is a list, one item per question of the rounds: its first line the title of the question in bold as the round wrote it, then a line `Recommended:` and a line `Answer:`, the person''s answer in English, both the latest where a later question changed them;'
    new: '`recommend` is a list, one item per question of the rounds: its first line the title of the question in bold as the round wrote it, then a sub-item `Recommended:` and a sub-item `Answer:`, the person''s answer in English, both as they stood when the person answered that question; a later question that replaced an earlier one is an item of its own, a question asked in more than one round is one item, of the last round in which the person answered it, and a question never answered says so in its `Answer:` sub-item (case 557.2);'
  change: recommend holds one item per question, its recommendation and answer as they stood when the person answered it, as sub-items; a question never answered says so (case 557.2)
- slug: rule-decisions-schema
  replace:
  - old: one item per question of the rounds of `case-guppi` — the question, the latest recommendation, the person's latest answer — one per change
    new: one item per question of the rounds of `case-guppi` — the question, its recommendation and the person's answer as they stood when the person answered it, or a note that it was not answered (case 557.2) — one per change
  change: '## Recommend holds each question with its recommendation and answer as they stood when the person answered it (case 557.2)'
- slug: estimate-case-build-records-the-rounds-in-recommend
  set:
    status: pending
    purpose: Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the recommendation and the answer in English as they stood when the person answered it, or a note that it was not answered — a sub-case with its own items and no problem
  change: the Criterion replaced whole — one item per question, its recommendation and answer as they stood when the person answered it, a question never answered noted (case 557.2)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `rule-case-protocol`
- [ ] update `rule-decisions-schema`
- [ ] update `estimate-case-build-records-the-rounds-in-recommend`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [ ] read `estimate-case-build-records-the-rounds-in-recommend` — in a later session after the render, the Case files against the rounds in the chat
```

### Case 557.3 — The Context of a first round treats what the round decides and a series of examples as lists

> **recommend:**
> - **How should the Context of a first round stop running a list inside one sentence?**
>   - Recommended: (a) name the two places, what the round decides when it has two or more parts and a series of examples, as lists; the shape is left to the `grill-me` template; the Criterion of `estimate-case-build-writes-a-plain-round` stands; this Case retires the put-off decision.
>   - Answer: agreed, (a); a later question set the wording to point to the template.
> - **How does the instruction name the two places in the Context without writing a list shape of its own?**
>   - Recommended: (a) name the two places and point to the template for the shape; the promise of a plain round stands and is read again after the render.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render paragraph on the Context of a first round changes
> **＋** `.claude/agents/case-guppi.md` — the render of `rule-case-build`
> **＋** `.claude/skills/grill-me/SKILL.md` — the template that sets what a list is and its shape
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads what counts as a list, which stands
> **＋** `estimate-case-build-writes-a-plain-round` — the promise of a plain round, whose Criterion stands
> **＋** `decision-case-551` — the defer of `rule-case-build` that this sub-case retires

> **when:**
> `case-guppi` answers with a first round of questions on an item, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> What the round decides, when it names two or more decisions, falls in the `**Context:**` under the list rule of `.claude/skills/grill-me/SKILL.md` like any other series.
> **＋** A series of examples in the `**Context:**` falls under the list rule of `.claude/skills/grill-me/SKILL.md` like any other series.
> **＋** `.claude/agents/case-guppi.md` names these two places and points to `.claude/skills/grill-me/SKILL.md` for the shape, with no shape of its own.
> **＋** The prose of the `**Context:**` goes on after a list.
> **－** What counts as a list stays as `estimate-skill-grill-me-asks-in-rounds` reads it.
> **－** The Criterion of `estimate-case-build-writes-a-plain-round` does not change.

```then
update:
- slug: rule-case-build
  replace:
  - old: A list or a quotation in the context stands as the grill-me template sets it, and the prose goes on after it.
    new: A list or a quotation in the context stands as the grill-me template sets it, and the prose goes on after it; what the round decides, when it names two or more decisions, and a series of examples fall under the list rule of that template like any other series (case 557.3).
  change: what a first round decides and a series of examples in its Context fall under the list rule of grill-me; the defer of case 551 retired (case 557.3)
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-a-plain-round` — in a later session after the render, one first round and one later round of `case-guppi`
```

## Case 558 — The librarian reads what its job needs and flags a read its frame does not name

> **context:**
> The librarian runs after the handoff and turns the session's ratified decisions into vault pages through the scripts, then writes the brief. Its frame is the Render of `rule-documentation`, rendered into `.claude/agents/librarian-guppi.md`. The frame names three inputs and a list of allowed reads, and bans the rest: the ledger beyond one read, the plan, `wiki/decisions/`, any search of `vault/archive/`, a Spec beyond its unticked lines, and `log.md` outside its diff. `estimate-documentation-completes` fails the whole promise on any read outside the list, even when the pages, the steps and the commit are right. Its History holds fifteen readings: nine failed and six passed. The last five in a row failed on a read outside the list. After each failure a Case widened or reworded the list (cases 349, 357, 474.1, 530.1), and the next run found another read. The reading of session 1736 on the run of 070d8e6 failed on four reads, all made for the brief. The first was a `git status` over `vault/wiki/decisions/`. The second was a `grep` of `git status` output for `vault/archive`. The third was the target, status and method of 52 Estimate pages, for Readings due. The fourth was a `grep` over every Decision page, for the page count at the close. The rounds found that each read on record served the librarian's job, mostly the brief, which asks for facts no input carries. Two of the reads came from gaps in the frame (the yaml marks undescribed, cases 44 and 58; no form of a synthesis entry, case 474.1). None was a read for its own sake. The person decided the following. The librarian decides what it needs to read. Its instructions name the reads the job is known to need and forbid no read. When it makes a read the frame does not name, it writes one line under Flags of the brief: what it read and which part of its job needed it. That line is its feedback on the frame. A read with its flag fails nothing. A read without one fails the reading. A read the handoff asks for is judged like the librarian's own reads, and only a repair of a yaml entry stays refused. The synthesis section loses its bans on reads in the same way. A `git status`, a listing or a file count may cover `vault/wiki/decisions/` and `vault/archive/`, since each prints only paths and numbers. The Glob by slug still finds an archived page that a script names in an error. What the job does not need is a search of the text of the archived pages. If the flags show too much token cost, the person takes the question up again. In the frame: `rule-synthesis` bans another session's yaml and the archive, and the Criterion of `estimate-synthesis-clusters` bans the archive, so 558.2 changes both. `estimate-brief-written` says Flags are "as before", and the person chose that it gains the new line, so 558.3 replaces its Criterion. The Purpose and `purpose` of `rule-materialize` say the script "Prevents the librarian from reading the ledger and the Spec", which the change makes false. `rule-rules-schema` requires a `purpose` that says what the rule prevents. So 558.1 rewords both texts: the script prevents the need for the ledger beyond its one read and for the Spec beyond its unticked lines, which matches the one read of the ledger that the new frame names. `estimate-synthesis-keeps-actioned-by-the-mark` speaks of `addressed_by`, and `estimate-brief-carries-the-run-facts` speaks of Readings due, so both stand. `rule-index-check` holds no ban on reads and stands. The report of `rule-close` already lists "the flags you raised", so it carries the new flags and stands. The sentence of `rule-brief` that reads a fact from a page and names the page in the report stands, because the frame names that read. The row of the glossary for the librarian names its inputs, which do not change. `lesson-handoff-instructs-a-repair-the-librarian-rule-forbids` is about a repair, which stays refused. The claims about the texts rest on three searches. First, a Grep of `librarian` near `read`, `open` or `search` over `vault/wiki/` printed so much that the harness saved it to a file. Its hits under `rules/`, `entities/` and the root pages were read. They state the librarian's reads only in `rule-documentation`, `rule-materialize`, `glossary.md` and `entity-glossary`, and the other hits there speak of readings of Estimates after the librarian's run. Its hits under `lessons/` and `insights/` were not all read. The one read is `insight-librarian-frame-omits-required-reads`, which is `actioned` and tells a history. Second, a Grep of `read no|never read|not read` over `vault/wiki/estimates/` printed one Estimate about the librarian's reads, `estimate-documentation-completes`. Third, a Grep of `read no|reads no|never read|not read` over the Estimates of `rule-documentation`, `rule-synthesis` and `rule-brief` printed it and `estimate-synthesis-clusters`. 558.1 and 558.2 replace both Criteria. The check of the answer noted six lines of the three old Criteria that the new ones do not carry. Five of them are the bans and the list of reads that the person removed. Four of those five stand in `estimate-documentation-completes`. The fifth is the archive line of `estimate-synthesis-clusters`, which 558.2 replaces. The sixth line is the line of `estimate-brief-written` that keeps Flags "as before", and 558.3 changes it. The check also noted that 558.1 and 558.3 share words on the flag. They check it from two angles: 558.1 checks that each read in the event log has its flag, and 558.3 checks the form of the line in Flags. The parent's `recommend` keeps an item for each of the two questions of the first round that the person did not answer. As the rebuilt Case 557.2 sets, each of these items says that its question was not answered and names the later question that replaced it. No hook and no code reads the frame: the librarian renders its own agent file, and the client loads it at the next session start. The first run under the new frame is therefore the librarian's run after the next session. The Case creates no page, so no vault query ran.

> **problem:**
> The librarian's frame bans reads by a closed list, and its Estimate fails on any read outside it. The list keeps missing reads that the job needs, mostly for the brief, so the Estimate has failed five times in a row, each time on a read its work needed, and each fix only widened the list until the next run. The question was whether the promise gets softer, what the bans protect, and how a read that the frame did not foresee becomes feedback instead of a failure.

> **recommend:**
> - **How strict the promise on reads stays**
>   Recommended: (a) check only the bans; the list of reads stays in the frame as a guide.
>   Answer: not answered; the person asked first why the librarian's reads are banned, and the later question on what a read outside the list does to `estimate-documentation-completes` replaced it.
> - **Which of the four reads of the last run become allowed**
>   Recommended: (a) all four; the ban covers the content of a page, not its name.
>   Answer: not answered; the later question on what the ban on Decision pages and the archive covers replaced it.
> - **Where the brief gets the facts that sent the librarian outside its list**
>   Recommended: (a) a script prints the facts the brief needs.
>   Answer: (b) the frame allows the reads the job needs: the librarian decides itself what it needs; if it is seen to spend too many tokens, the question is taken up again.
> - **What a read outside the list does to `estimate-documentation-completes`**
>   Recommended: (a) a read outside the list is a finding, not a failure; the Estimate fails only on a ban.
>   Answer: (a), agreed; the next round widened it, so that no read fails once the librarian records it.
> - **What the ban on Decision pages and the archive covers**
>   Recommended: (a) the ban covers the text of a page, not its name.
>   Answer: (a), with a correction: the Estimate does not fail when pages are read, since such a read is a finding that the librarian must record; the librarian's instructions speak of no hard ban, and ask it to say so when it needs a read of its own; this is the librarian's feedback on its frame.
> - **How a read beyond the frame's list reaches the next session**
>   Recommended: (a) the librarian writes each such read into Next session, `Cases`, of its brief.
>   Answer: not a Case; it is closer to a flag or a lesson.
> - **Where the librarian records a read outside its inputs**
>   Recommended: (a) a line under Flags of the brief.
>   Answer: (a), agreed.
> - **Change**
>   Asked: fix the findings of the second pre-spec run: the Purpose of `rule-materialize` says the ledger is not needed at all while the frame needs one read of it; the frame says the job does not need a search of the archive while it names the Glob by slug and a listing of the archive; the context misstates the state of Case 557.2 and the count of the lines not carried.
>   Taken: the `purpose` and the Purpose of `rule-materialize` say the ledger beyond its one read and the Spec beyond its unticked lines; the frame says the job does not need a search of the text of the pages under `vault/archive/`; the context names the rebuilt 557.2 and counts five removed bans among the six lines not carried.

### Case 558.1 — The frame names the reads the job needs and forbids none

> **recommend:**
> - **A read that the handoff asks for**
>   Recommended: (a) only the repair stays refused; a read the handoff asks for is a read like any other.
>   Answer: (a), agreed, after the main agent explained the refusals of the frame.

> **given:**
> `rule-documentation` — the frame of the librarian: its inputs, the reads its job is known to need, and its one refusal
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from the frame
> **＋** `estimate-documentation-completes` — the promise of the phase, its Criterion replaced whole
> **＋** `rule-materialize` — its Purpose says what the yaml prevents the librarian from needing
> **＋** `vault/wiki/brief.md` — the brief, whose Flags carry each read the frame does not name
> **＋** `handoff.md`, `vault/wiki/tags.md` — two of the librarian's inputs
> **＋** `rule-index-check`, `rule-synthesis` — the judgments whose Greps give the index lines
> **＋** `Makefile` — `make test-documentation` and `make lint`

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

> **then:**
> `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
> **＋** Every read in its event log beyond its inputs and beyond the reads its frame names has its line under Flags of the new `vault/wiki/brief.md`.
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
> **＋** It wrote `vault/wiki/brief.md` with the `Write` tool. The new brief holds no fact taken from the old brief, and the librarian put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc.
> **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
> **－** A read that has its line under Flags fails nothing, whatever it read: a Decision page, a Spec, the ledger or the archive.
> **－** A hook's refusal of one of its calls is not worked around by another route: the librarian names the refusal in the report and goes on as the refusal says.
> **－** The librarian refuses an instruction of the handoff to repair a yaml entry. It names what was asked and why in the report, and the refusal does not stop the run.

```then
update:
- slug: rule-documentation
  replace:
  - old: 'Open a page under `vault/wiki/` for four reasons only:'
    new: 'The reads below are the ones your job is known to need; make them without a flag. When you need a read they do not name, make it, and write one line under Flags of the brief: what you read and which part of your job needed it, and the handoff when it asked for the read. That line is your feedback on this frame, not a fault: no read is forbidden to you (case 558.1). Open a page under `vault/wiki/` for these four reasons:'
  - old: Never read `ledger.md`, `plan.md` or `wiki/decisions/`, never search `vault/archive/`, nor read `spec.md` beyond its unticked `- [ ]` lines
    new: Your job does not need `plan.md`, the text of a page under `wiki/decisions/` or a search of the text of the pages under `vault/archive/`, nor `ledger.md` beyond the one read below, nor `spec.md` beyond its unticked `- [ ]` lines
  - old: 'One read of `ledger.md` is allowed and no other:'
    new: 'One read of `ledger.md` is needed:'
  - old: only by the Glob `vault/archive/**/<slug>.md`, open it, and name the page in the report; no other Glob, Grep, `grep`, `find` or `ls` runs over the archive (case 474.1).
    new: by the Glob `vault/archive/**/<slug>.md`, open it, and name the page in the report (case 474.1).
  - old: run `git status` and `git diff` on the files the scripts of this run wrote, never over `vault/wiki/decisions/` or `vault/archive/`.
    new: run `git status` and `git diff` on the files the scripts of this run wrote; a `git status`, a listing or a file count may cover `vault/wiki/decisions/` and `vault/archive/`, since it prints paths and numbers and no text of a page (case 558.1).
  - old: Read `vault/wiki/log.md` only through `git diff -- vault/wiki/log.md`, which before the commit shows only the lines this run added; never `Read`, `tail`, `head` or `grep` it.
    new: Read `vault/wiki/log.md` through `git diff -- vault/wiki/log.md`, which before the commit shows only the lines this run added.
  - old: |-
      An instruction of the handoff that this frame forbids — a repair of an
      entry, a read of `ledger.md` beyond the one allowed above, a Spec beyond its unticked lines, a decision page, a search of the archive or an archived page that no script named in an error — you do not
      carry out: name it in the report, what was asked and why it was refused, and go on
      (case 90.3).
    new: 'An instruction of the handoff to repair an entry you do not carry out: name it in the report, what was asked and why it was refused, and go on (case 90.3). A read the handoff asks for you judge as you judge your own reads, and flag it, the handoff named, when this frame does not name it (case 558.1).'
  - old: It starts empty, reads three inputs, and opens a page only for a reason its frame names.
    new: It starts empty, reads three inputs and the reads its frame names, and flags in the brief any other read it makes, so the frame learns what the job needs (case 558.1).
  change: the frame names the reads the job needs and forbids none; a read it does not name is made and flagged in the brief; only a repair asked by the handoff is refused (case 558.1)
- slug: rule-materialize
  set:
    purpose: Prevents the librarian from needing the ledger beyond its one read or the Spec beyond its unticked lines, or from routing a decision by guesswork
  replace:
  - old: Prevents the librarian from reading the ledger and the Spec beyond its unticked lines (case 271), or from routing
    new: Prevents the librarian from needing the ledger beyond its one read or the Spec beyond its unticked lines (case 271), or from routing
  change: the purpose prevents the need for the reads, not the reads, since the librarian's frame forbids no read (case 558.1)
- slug: estimate-documentation-completes
  set:
    status: pending
  change: the Criterion replaced whole — a read the frame does not name is flagged under Flags of the brief and fails nothing; only a repair asked by the handoff is refused (case 558.1)
```

```tasks
- [ ] update `rule-documentation`
- [ ] update `rule-materialize`
- [ ] update `estimate-documentation-completes`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-documentation-completes` — by hand, the first librarian run whose agent file holds this Render: its event log against the Flags of its brief
```

### Case 558.2 — The synthesis drops its bans on reads

> **recommend:**
> - **Whether the synthesis section drops its bans too**
>   Recommended: (a) yes: the synthesis says "name it" instead of "never", like the frame.
>   Answer: (a), agreed.

> **given:**
> `rule-synthesis` — the synthesis section of the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from it
> **＋** `estimate-synthesis-clusters` — the promise of the synthesis, its Criterion replaced whole
> **＋** `vault/wiki/lessons/`, `vault/wiki/insights/` — the pages the Greps of the synthesis index
> **＋** `vault/archive/` — the archive, which the synthesis does not need
> **＋** `estimate-documentation-completes` — the promise that each read the frame does not name is flagged

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The report names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, and the comparisons made against their lines, by meaning.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
> **＋** A lesson without a pair stays `new`.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line, and the flag of such a read is the promise of `estimate-documentation-completes`.

```then
update:
- slug: rule-synthesis
  replace:
  - old: 'The archive is not read: a lesson is archived only when its'
    new: 'The archive is not needed: a lesson is archived only when its'
  - old: 'Read no `materialize.yaml` other than the ones `guppi materialize` names, and look for no earlier entry: the entries of the synthesis have these forms (case 474.1).'
    new: The entries of the synthesis have these forms, so no earlier entry and no `materialize.yaml` other than the ones `guppi materialize` names is needed (case 474.1); when you still need one, read it and flag the read as the frame says (case 558.2).
  - old: Do not read the archive and do not write pages yourself.
    new: 'The archive is not needed: an actioned Insight stays live with its pattern in its index line; when you still need an archived page, read it and flag the read as the frame says (case 558.2). Do not write pages yourself.'
  change: the synthesis forbids no read; another session's yaml or an archived page it still needs is read and flagged (case 558.2)
- slug: estimate-synthesis-clusters
  set:
    status: pending
  change: the Criterion replaced whole — a read of another session's yaml or of the archive fails nothing here; its flag is the promise of estimate-documentation-completes (case 558.2)
```

```tasks
- [ ] update `rule-synthesis`
- [ ] update `estimate-synthesis-clusters`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-synthesis-clusters` — by hand, the yaml and the report of the first librarian run after the render whose yaml holds at least two lesson entries
```

### Case 558.3 — Flags of the brief carry the librarian's own reads

> **given:**
> `rule-brief` — the brief section of the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from it
> **＋** `estimate-brief-written` — the promise of the form of the brief, its Criterion replaced whole
> **＋** `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/sprint.md` — the brief, the list of deferred items and the sprint
> **＋** `handoff.md`, `frontier.md` — the sources of Next session, of the librarian and of `carry`
> **＋** `rule-carry-over` — the second writer of the brief, the skill `carry`
> **＋** `rule-documentation` — the frame whose named reads decide which read is flagged

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
> **＋** Where things stand, Readings due and Readings at the close are as before.
> **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and add one kind: a read of the librarian that its frame does not name, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
> **＋** An item stands in one list only. A list with no item is the line "none".
> **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
> **－** The brief states no decision: the sort by kind is not a judgment of the work.

```then
update:
- slug: rule-brief
  replace:
  - old: failed Estimates; MOC candidates; stale defers; contradictions; the lint output.
    new: 'failed Estimates; MOC candidates; stale defers; contradictions; the lint output; each read you made beyond the reads your frame names, one line each: what you read and which part of your job needed it, and the handoff when it asked for the read (case 558.3).'
  change: Flags carry each read of the librarian beyond the reads its frame names (case 558.3)
- slug: estimate-brief-written
  set:
    status: pending
  change: the Criterion replaced whole — Flags hold a line for each read of the librarian beyond the reads its frame names (case 558.3)
```

```tasks
- [ ] update `rule-brief`
- [ ] update `estimate-brief-written`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-brief-written` — by hand, the brief of the first librarian run whose agent file holds this Render
```

## Deferred

## Case 560 — The defer of the own-text fault targets its Estimate

> **context:**
> Case 559 deferred `rule-case-protocol` over the fault that `estimate-case-protocol-shows-the-built-case` found in session 1736: the main agent wrote a line of its own before the first question of a round of `case-guppi`. Case 557.2 of the same session updates `rule-case-protocol`, and a Case that changes a page another Case of the plan defers is a pre-spec finding. The person agreed to defer the Estimate itself instead.

> **problem:**
> The defer of the own-text fault must not target a page that Case 557.2 changes in the same Spec.

```then
defer:
  - slug: estimate-case-protocol-shows-the-built-case
    type: estimate
    purpose: The main agent shows a round of case-guppi with no text of its own before the first question, its own text only after the last question and one horizontal rule; this Estimate failed on that in session 1736
```
