## Case 542 — A short defer is written with no Retro moment

> **context:**
> When the person defers a decision, the `Stop` hook of `rule-spec-write` writes it in the short form under `## Deferred`. It uses the plan file while `spec.md` in the session's folder does not stand, and `spec.md` once it stands. Case 531.14 gave a short defer one moment, the close of Plan Mode: Retro puts nothing off, and what it would put off is a line of `handoff.md`. `rule-case-protocol`, `rule-retro`, the `retro` skill and the glossary row Retro already say this. Five texts still name Retro as the moment of a defer. The Purpose of `rule-spec-capture` says the hook writes a defer-only Case "at Retro", and so does the docstring of `guppi/spec.py`, which it mirrors (case 200.4). The "How it works" section of `rule-spec-write` and the docstring of `guppi/ratified.py` say it too. So does the Criterion of `estimate-spec-write-writes-a-defer`. The code comments in `guppi/ratified.py` and `guppi/materialize.py` and a test name in `tests/test_ratified.py` say the same. Case 531.14 named `rule-spec-write` in its `given` but gave it no `update`. The hook's behaviour stays: it still writes a defer into `spec.md` once that file stands. After case 531.14 no step of the protocol reaches that path, but that does not make any sentence false once "at Retro" is gone. The Criterion of `estimate-spec-write-writes-a-defer` is replaced whole, since it names Retro. Two of its lines change on purpose. The first line no longer names Retro or Plan Mode as the moment: it names only whether `spec.md` stands. The exception on the ratified copy `<plan>.ratified.md` goes, because the hook has written no such copy since case 445.2. Its other half stays: the check after the write does not run on a defer. The other lines are carried word for word. The other Estimates of `rule-spec-write` and of `rule-spec-capture` do not name Retro and are not touched. The History lines that name Retro stay: they record what was decided then. The open defer on `rule-spec-write` by case 475 is a different bug, about a Case built again as a parent. It stays in the backlog, and this Case does not supersede it. This Case creates no page, so the vault query was not run.

> **problem:**
> Two pages, an Estimate and the code still say the hook writes a short defer at Retro, and Retro puts nothing off since case 531.14. Each such sentence is false and must be corrected without changing what the hook does.

> **recommend:**
> Change the words only. Drop "at Retro" from both pages, both docstrings, both code comments and the test name, and replace the Criterion of the Estimate whole without the Retro clause and without the dead clause on the ratified copy. The rejected options were to write a defer into both files, like any other Case, or to refuse a defer once `spec.md` stands. The first changes the code for a path that nothing reaches. The second loses the Case of a ledger line that the ledger hook writes at the same `Stop`.

> **given:**
> `rule-spec-write` — the `Stop` hook that writes a short defer, its "How it works"
> **＋** `estimate-spec-write-writes-a-defer` — the promise that the hook writes a short defer, its Criterion replaced whole
> **＋** `rule-spec-capture` — the writers of `spec.md`, its Purpose
> **＋** `guppi/ratified.py` — the hook, its docstring and the comment on the target of a defer
> **＋** `guppi/spec.py` — the docstring that names the writers of `spec.md`
> **＋** `guppi/materialize.py` — the comment on the short form in the check for an incomplete Case
> **＋** `tests/test_ratified.py` — the test of a defer written into `spec.md`
> **＋** `rule-case-protocol` — a short defer has one moment, the close of Plan Mode

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

> **then:**
> The hook writes that Case under `## Deferred` of the plan file while `spec.md` in the session's folder does not stand, and of that `spec.md` once it stands: the heading, `context`, `problem` and the `then` block as the reply shows them.
> **＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
> **＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **＋** A key of a `defer` item that `item_keys` of `guppi/materialize.py` does not give a `defer` of its category: exit 2 with `` `<key>`: not a key of defer <slug> `` on stderr, and nothing of the Case is written.
> **＋** A `then` block that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — as the function of `guppi/materialize.py` judges it: exit 2 with the line of the comment and the advice to quote the value on stderr, and nothing of the Case is written.
> **－** A `#` inside a quoted value or inside a `|` or `>` block is text, not a comment, and is no refusal.
> **－** A `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).
> **－** The check after the write does not run on the Case.

> **tasks:**
> - [ ] update `rule-spec-capture` — the writers of `spec.md`: a defer-only Case with no Retro moment
>   - old: `` removes a superseded Case, and writes a defer-only Case at Retro under `## Deferred` (cases 421.1, 441) ``
>   - new: `` removes a superseded Case, and writes a defer-only Case under `## Deferred` (cases 421.1, 441, 542) ``
>   - change: `the Stop hook of rule-spec-write writes a defer-only Case under ## Deferred with no Retro moment; Retro puts nothing off (case 542)`
> - [ ] update `rule-spec-write` — a short defer goes into spec.md once it stands, with no Retro moment
>   - old: `` under `## Deferred` of the plan file, or of `spec.md` in the session's folder once that file stands, at Retro; the check after the write does not run on it (case 421.1) ``
>   - new: `` under `## Deferred` of the plan file, or of `spec.md` in the session's folder once that file stands; the check after the write does not run on it (cases 421.1, 542) ``
>   - change: `a short defer goes under ## Deferred of spec.md once it stands, with no Retro moment (case 542)`
> - [ ] update `estimate-spec-write-writes-a-defer` — the Criterion replaced whole: no Retro moment, no ratified copy
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a defer goes into spec.md once it stands, with no Retro moment; the clause on the ratified copy dropped (case 542)`
> - [ ] `guppi/spec.py` — the docstring: the `Stop` hook of `rule-spec-write` writes a defer-only Case under `## Deferred`, "at Retro" dropped
> - [ ] `guppi/ratified.py` — the docstring of the defer: "(Retro)" dropped; the comment on the target of a defer: it goes to `spec.md` once that file stands, with no Retro
> - [ ] `guppi/materialize.py` — the comment on the check for an incomplete Case names the short form of a defer, not of Retro
> - [ ] `tests/test_ratified.py` — `test_write_a_defer_at_retro_goes_into_the_spec_of_the_folder` renamed to `test_write_a_defer_once_the_spec_stands_goes_into_it`, its body unchanged
> - [ ] `uv run pytest tests/test_ratified.py -k defer` green
> - [ ] read `estimate-spec-write-writes-a-defer` — `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change, in a later session

> **ratification:**
> ```
> - decision[case 542][update][rule-spec-capture]{ref:rule-spec-capture}
> - decision[case 542][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 542][update][estimate-spec-write-writes-a-defer]{ref:rule-spec-write}
> ```
