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

> **tasks:**
> - [ ] update `rule-spec-write`
>   - old:
>     ````
>     a Case N none of them holds is no refusal (case 441).
>     ````
>   - new:
>     ````
>     a Case N none of them holds is no refusal (case 441). An error of the hook itself after it has read the payload — an exception while it reads the transcript, the store, the plan file or `spec.md`, or writes, removes or checks a Case — exits 2 with `ratified: not done: <error>` and the advice to repeat the ledger lines once the cause is fixed on stderr, so the agent sees it at the end of that reply; a Case not yet written is written at the reply that repeats its lines, and one written before the error stays and is replaced then. An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell a re-fire then; the guard of `rule-spec-reconcile` keeps exit 0 on its own error (case 554).
>     ````
>   - change: `the Stop hook exits 2 on its own error after the payload is read, and 0 on an error while it reads the payload (case 554)`
> - [ ] create `estimate-spec-write-exits-2-on-an-error`
>   - ref: `rule-spec-write`
>   - kind: `QA`
>   - purpose: `Whether the Spec hook exits 2 with the error on stderr when its Stop run raises after reading the payload, and exits 0 on an error while reading the payload, on the re-fire and in the guard`
>   - method: `uv run pytest tests/test_ratified.py — piped payloads, a function of the hook patched to raise`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/ratified.py`: `run` reads the payload in its own handler that prints the error and returns 0; the handler of the guard prints the error and returns 0; the handler of the `Stop` run prints `ratified: not done: <error>` with the advice to repeat the ledger lines and returns 2; the docstring says so
> - [ ] `tests/test_ratified.py`: a patched `write_case` that raises gives exit 2 and the stderr line; the same payload with `stop_hook_active` gives exit 0 and writes nothing; a payload that cannot be read gives exit 0 and the stderr line; a patched `guard_refusal` that raises gives exit 0 in `--guard`
> - [ ] read `estimate-spec-write-exits-2-on-an-error` — in a later session

> **ratification:**
> ```
> - decision[case 554][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 554][create][estimate-spec-write-exits-2-on-an-error]{ref:rule-spec-write}{tags:hooks,harness,workflow}
> ```
