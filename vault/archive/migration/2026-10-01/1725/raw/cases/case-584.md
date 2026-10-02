## Case 584 — A refused reply does not start a new turn: fix the casecheck comment and add a test

> **context:**
> The `Stop` hook `uv run guppi casecheck` refuses a shown Case when the reply's turn has no `SendUserFile` call on the Case file. Its function `turn_of_reply` decides where the turn starts. The turn starts after the last `user` record that is not marked `isMeta` and that holds more than tool results. The module docstring of `guppi/casecheck.py` explains this, and then says that a refusal of a `Stop` hook adds no `user` record. That claim is false. Line 676 of the session 1441 transcript is a `user` record marked `isMeta`, and its content opens with `Stop hook feedback:`. A Grep for `Stop hook feedback` in that transcript printed 23 occurrences. Session 1237 is the other source the brief and the handoff of session 1441 name, and I did not open its transcript. The `own_refusals` docstring in `guppi/ledger.py` already describes this record shape and names both sessions as its source. The behaviour is still right: `turn_of_reply` skips every `isMeta` record, so a refusal does not start a new turn. A file sent before the refusal therefore still counts for the reply that follows. No test checks this. A Grep for `isMeta|turn_of_reply|refusal` in `tests/test_casecheck.py` printed nothing. A Grep for the false claim, with the pattern ``(adds|add) no `?user`? record|no user record`` over the repository outside `vault/raw/`, printed 2 files: `vault/wiki/brief.md` and `guppi/casecheck.py`. The brief hit is the flag of this item and is not read. The page `rule-case-check` does not make the claim: its How it works says the turn is the records after the person's last prompt, by `turn_of_reply`, which stays true. So the page gets only a History line. The Case creates no page, so no vault query was run. A Grep for `turn of the reply|last prompt|isMeta` over `vault/wiki/estimates/estimate-case-check-*` printed 2 files: `estimate-case-check-shows-only-the-checked-case.md` and `estimate-case-check-refuses-text-before-a-round.md`. Neither Criterion speaks of a refusal record. `estimate-case-check-shows-only-the-checked-case` is the Estimate that checks this change. Its Criterion requires a `SendUserFile` call on the case file in the turn of the reply. The new test keeps that sending inside the turn when a refusal stands after it, and the test's name holds `stop`, so the Estimate's method `uv run pytest tests/test_casecheck.py -k stop` runs it. Its Criterion stands, because the behaviour it promises does not change. The Case adds and changes no hook, and no other Case of this session touches `guppi/casecheck.py` or `rule-case-check`.

> **problem:**
> The module docstring of `guppi/casecheck.py` says a refusal of a `Stop` hook adds no `user` record, and the transcripts show one, marked `isMeta`. A later fix of `turn_of_reply` that trusts the docstring could treat the refusal as the start of a turn. The hook would then refuse a Case whose file was already sent, and no test would catch it. The question was how far the fix goes.

> **recommend:**
> - **How far should the fix go?**
>   - Recommended: (b) fix the docstring and add a test, with a name that holds `stop`, in which a file is sent, a refusal record follows and the Case is shown again; the Criterion of `estimate-case-check-shows-only-the-checked-case` stands.
>   - Answer: agreed, (b).

> **given:**
> `guppi/casecheck.py` — the `Stop` hook and its module docstring
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `rule-case-check` — the rule the hook implements, given a History line

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case, and the turn of the reply holds a `SendUserFile` call on its case file followed by a refusal of a `Stop` hook.
> **＋** A reader reads the module docstring of `guppi/casecheck.py`.

> **then:**
> `uv run guppi casecheck` counts the `SendUserFile` call before the refusal as a sending in the turn of the reply.
> **＋** The module docstring of `guppi/casecheck.py` says that a refusal of a `Stop` hook is a `user` record marked `isMeta`, its text opening with `Stop hook feedback:`, and that the turn of the reply skips it as it skips any `isMeta` record, as measured on the transcripts of sessions 1237 and 1441.
> **－** The refusal record does not start a new turn of the reply.

> **tasks:**
> - [ ] update `rule-case-check`
>   - change: `the module docstring of guppi/casecheck.py says a Stop refusal is a user record marked isMeta, which the turn of the reply skips; a test checks a sending before a refusal (case 584)`
> - [ ] `guppi/casecheck.py`: replace the claim in the module docstring that a `Stop` hook's refusal adds no `user` record with the measured record shape, the transcripts of sessions 1237 and 1441 as its source
> - [ ] `tests/test_casecheck.py`: a test, with a name that holds `stop`, of a turn with a `SendUserFile` call on the case file, then a `user` record marked `isMeta` whose content opens with `Stop hook feedback:`, then a reply that shows the Case; the hook exits 0
> - [ ] `uv run pytest tests/test_casecheck.py -k stop`

> **ratification:**
> ```
> - decision[case 584][update][rule-case-check]{ref:rule-case-check}
> ```
