## Case 625 — The method of four Estimates no longer names a moment no one brings on

> **context:**
> An Estimate's `method` says how its reading is taken and at which moment. At `/hi` the agent takes a pending reading only when every moment its `method` names has come; a reading whose moment has come in no session waits, and its line stays open (`rule-skill-hi`). The `method` of four Estimates names a moment that a normal run never brings, and that no one stages. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` names a `/work` the person types. `estimate-prespec-onward-sends-the-agent-on` and `estimate-retro-onward-sends-the-agent-to-the-handoff` name a Plan Mode or an end of Retro at which the ledger hook refuses a line. `estimate-retro-runs-on-to-the-handoff` names a Retro at which that hook refuses a line. Session 0004 closed all four `passed` on the person's word (its ledger lines 6, 14, 15 and 16), with that moment written as not exercised. The handoff of 0004 notes that no Case changed the `method`. So the next time a Case sets one of them `pending`, its reading waits for good, or needs the person's word again.
>
> The person chose to drop the moment from the `method` of the four and to keep the change to these four pages: no rule page changes. The Criterion, `purpose` and status of each stay. The behaviour at the dropped moment is still set by `rule-work-mode`, `rule-prespec-onward`, `rule-retro-onward` and `rule-retro`, and it is still promised. `estimate-retro-runs-on-to-the-handoff` already treats a `/retro` the person types this way: its `When` names it, and its `method` does not. In the two hook Estimates, `tests/test_onward.py` keeps covering a refusal of the ledger hook, through the tests that a ledger refusal of the same reply or of a later reply sends the hook on again, in Plan Mode too. Nothing reads a `/work` the person types, or the agent's answer to a refusal at Retro. The person treats a fault there as a lesson when it comes. A change to a part alone sets no status (case 378.4), so the four stay `passed` and no new reading is due. The one Case for four Estimates stands against the rule of one promise per Case because it changes only `method` and no promise, and the person chose one Case.
>
> What done means: no new Estimate. `estimate-lint-reports-a-method-tied-to-a-one-off-moment` checks the form of the four new `method` texts, in pre-spec and in the `make lint` of the librarian's run. `estimate-hi-takes-its-readings` already promises the behaviour this change unblocks: `/hi` takes a reading once every moment its `method` names has come. Its Criterion stands because it reads the moment from the `method` and does not list moments.
>
> Frame checks:
> - A Grep of `^method:.*(ledger hook refuses|refusal of the ledger hook|person types)` over `vault/wiki/estimates/` printed only the four pages. No other `method` names these moments.
> - A Grep of the four slugs over the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed `log.md`, `rule-prespec-onward.md`, `rule-retro-onward.md`, `rule-retro.md`, `rule-work-mode.md`, `estimate-case-build-answers-what-done-means.md`, `estimate-generate-renames.md` and `estimate-retro-onward-exits-2-on-an-error.md`. It printed no code file. The hits in the rule pages are their `estimates` fields and History lines. The hits in `estimate-case-build-answers-what-done-means` and `estimate-generate-renames` are in past Results. `estimate-retro-onward-exits-2-on-an-error` uses the Criterion of `estimate-retro-onward-sends-the-agent-to-the-handoff` for the stretch, and that Criterion stays. No hit is made false.
> - A Grep of `not exercised` printed 26 files over `vault/wiki/` and none over `.claude/`. The phrase appears only in Results and `brief.md`, and no rule sets it, so this Case sets nothing about it.
> - The change sets no new moment. It changes what the reading step of `rule-skill-hi` finds in four `method` fields, and the text of that step stays true. The `method` description in `rule-estimates-schema` stays true: each new `method` names the kind of its moment, holds `by hand` or `pytest`, and has no word "first".
> - Case 624 changes `rule-handoff` and `estimate-handoff-holds-each-fact-once` and sets the writing of `handoff.md`. This Case changes neither page and sets no part of that moment. After it, a handoff that lists these four in `## Debt` no longer lists these moments.
>
> The Case creates no page, so the vault query was not run.

> **problem:**
> Four Estimates name in their `method` a moment that a normal run never brings: a `/work` the person types, or a refusal of the ledger hook. Each passed only on the person's word, and when a later Case sets one `pending`, its reading waits for that moment for good. The question is whether the `method` keeps the moment or drops it.

> **recommend:**
> - **Drop or keep the moment that never comes**
>   - Recommended: (a) drop the moment from the `method` of all four; the tests of `tests/test_onward.py` keep covering the refusal path of the two hooks, and a fault at a typed `/work` or in the answer to a refusal shows as a lesson when it comes.
>   - Answer: agreed with the recommendation, (a).
> - **Only these four pages, or a general rule**
>   - Recommended: (a) only the four pages; no sentence is added to `rule-estimates-schema`.
>   - Answer: agreed with the recommendation, (a).
> - **What the pages promise about the moment that was dropped**
>   - Recommended: (a) keep the promises and change only `method`; the four stay `passed`, as `estimate-retro-runs-on-to-the-handoff` already treats a typed `/retro`.
>   - Answer: agreed with the recommendation, (a).
> - **How we know this change is done**
>   - Recommended: (a) no new check; the Case names `estimate-lint-reports-a-method-tied-to-a-one-off-moment` for the form and `estimate-hi-takes-its-readings` for the next reading.
>   - Answer: agreed with the recommendation, (a).
> - **One Case or one sub-case per page**
>   - Recommended: (a) one Case with four page updates, ratified together.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — the reading of `/work`; its `method` changes
> **＋** `estimate-prespec-onward-sends-the-agent-on` — the reading of the hook that sends Plan Mode on; its `method` changes
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — the reading of the hook that sends Retro on; its `method` changes
> **＋** `estimate-retro-runs-on-to-the-handoff` — the reading of Retro; its `method` changes
> **＋** `tests/test_onward.py` — the tests of a refusal of the ledger hook that the two hook Estimates name
> **＋** `rule-skill-hi` — the reading step at `/hi`, which reads the moments of a `method`; unchanged
> **＋** `rule-estimates-schema` — the form of a `method`; unchanged

> **when:**
> At `/hi`, the agent reads the `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-retro-onward-sends-the-agent-to-the-handoff` or `estimate-retro-runs-on-to-the-handoff` to judge, by the reading step of `rule-skill-hi`, whether each moment of its reading has come.

> **then:**
> The `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` names only a `/work` the agent calls, and no `/work` the person types.
> **＋** The `method` of `estimate-prespec-onward-sends-the-agent-on` names `tests/test_onward.py` for a refusal of the ledger hook, and a reading by hand at a Plan Mode that closes its last Case, with no refusal of the ledger hook as its moment.
> **＋** The `method` of `estimate-retro-onward-sends-the-agent-to-the-handoff` names `tests/test_onward.py` for a refusal of the ledger hook, and a reading by hand at an end of Retro, with no refusal of the ledger hook as its moment.
> **＋** The `method` of `estimate-retro-runs-on-to-the-handoff` names a run from `/work` to the librarian, and no Retro at which the ledger hook refuses a line.
> **＋** So, by `rule-skill-hi`, the next reading of each of them is taken once the moments its `method` names have come, with no word from the person.
> **－** The Criterion, `purpose` and status of each stay: a `/work` the person types, a refusal of the ledger hook and the agent's answer to it stay promised.
> **－** `rule-estimates-schema` and `rule-skill-hi` stay as they are.

> **tasks:**
> - [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
>   - set: `{method: "uv run guppi render --check; by hand, a /work the agent calls at the fork and a /work that /box calls: the branch, work.md, the ticks of the Spec, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent's own run of its command, recorded in the estimate line"}`
>   - change: `method names no /work the person types, a moment no one brings on (case 625)`
> - [ ] update `estimate-prespec-onward-sends-the-agent-on`
>   - set: `{method: "uv run pytest tests/test_onward.py tests/test_ledger.py, which cover a refusal of the ledger hook; by hand at a Plan Mode that closes its last Case: the transcript, the event log and frontier.md, recorded in the estimate line"}`
>   - change: `method names no Plan Mode at which the ledger hook refuses a line, a moment no one brings on; the tests cover the refusal (case 625)`
> - [ ] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
>   - set: `{method: "uv run pytest tests/test_onward.py tests/test_ledger.py, which cover a refusal of the ledger hook; by hand at an end of Retro: the transcript, the event log and handoff.md, recorded in the estimate line"}`
>   - change: `method names no end of Retro at which the ledger hook refuses a line, a moment no one brings on; the tests cover the refusal (case 625)`
> - [ ] update `estimate-retro-runs-on-to-the-handoff`
>   - set: `{method: "by hand at a run from /work to the librarian: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line"}`
>   - change: `method names no Retro at which the ledger hook refuses a line, a moment no one brings on (case 625)`

> **ratification:**
> ```
> - decision[case 625][update][estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]{ref:rule-work-mode}
> - decision[case 625][update][estimate-prespec-onward-sends-the-agent-on]{ref:rule-prespec-onward}
> - decision[case 625][update][estimate-retro-onward-sends-the-agent-to-the-handoff]{ref:rule-retro-onward}
> - decision[case 625][update][estimate-retro-runs-on-to-the-handoff]{ref:rule-retro}
> ```
