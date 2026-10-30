## Case 902 — The stale defer of the defer check leaves the backlog

> **context:**
> When the person puts a check off, the page of the check gets `deferred_by`, which names the Decision page of that defer, and `guppi backlog` lists every live page with `deferred_by`. A later Case clears a defer only when it supersedes the old Decision and also names the page on a decision line of its own, as `rule-case-protocol` sets it (case 467.3). A page the later Case does not name keeps the defer and stays on the list. The cascade of `guppi generate` archives a superseded Decision page (case 104.1), and `guppi cleanup` moves it under `vault/archive/`. Case 900.2 superseded `decision-case-885` and named only `estimate-clean-branch-writes-the-session-files`, so `estimate-close-commits` and `estimate-spec-write-writes-a-defer` kept the defer while the Decision page went to `vault/archive/plugin/2026-10-29/0327/decisions/`. The brief calls this a defect, but the code did what its rules set: `clear_deferred_by` and `decision` of `.guppi/guppi/generate.py` clear only the targets the superseding Case names, `archived_by_cascade` archives each superseded Decision, and `find` reaches a page under `vault/archive/`, so a later Case can still take the defer up; for an earlier page that stands `archived`, `decision` keeps it `archived` and clears the targets the new Case names (case 683). A Grep of `deferred_by: \[.*decision-case-(885|891)` over `vault/wiki/` printed `estimate-close-commits.md` and `estimate-spec-write-writes-a-defer.md`. `estimate-spec-write-writes-a-defer` also names `decision-case-891`, which the brief does not mention; a Glob found that page under `vault/archive/plugin/2026-10-28/1907/decisions/`, superseded by Case 893.2. Both of its defers waited for the by-hand reading of a short-form defer that the person asks for. That reading was taken at the Retro of session 0118, and the page has stood `passed` since 2026-10-26, so both defers are stale. This Case takes up both defers on that page with an `update` that carries `change` alone. `materialize.py` writes such an item as a History line only: it lifts no Criterion and sets no status (case 588.2). This Case leaves the defer of `estimate-close-commits` to Case 903.1, which replaces the Criterion, `purpose` and `method` of that page and no part this Case changes. Its ratified line in the session's ledger names that page and carries `{supersedes:case 885}`, so the same run of `generate` clears that defer too. `decision-case-885` then takes both Cases into its `superseded_by`. No new Estimate is created. `estimate-generate-writes-the-decision-page`, `passed` on 2026-10-26, already checks this behaviour: its Criterion says that a `supersedes` of an earlier page that stands `archived` keeps that page archived and removes its slug from the `deferred_by` of each target that the superseding Case names. Its Criterion stands, since this Case changes no code.

> **problem:**
> `estimate-spec-write-writes-a-defer` passed its reading, but it stays on the backlog list. The two Decisions that put it off are archived and were never taken up for it.

> **recommend:**
> - **What this item fixes**
>   - Recommended: (a) no code change: take up the open defers, since `generate` already clears a defer from an archived Decision for the pages that the superseding Case names.
>   - Answer: agreed, (a).
> - **Which of the two checks this Case takes up**
>   - Recommended: (a) `estimate-spec-write-writes-a-defer` only, with a History line and both defers superseded; the defer of `estimate-close-commits` is retired by the Case that rewords its `method`.
>   - Answer: agreed, (a).

> **given:**
> `estimate-spec-write-writes-a-defer`: the check whose defers this Case takes up.
> **＋** `decision-case-885`: an archived Decision that put the check off.
> **＋** `decision-case-891`: an archived Decision that put the check off.
> **＋** `.guppi/guppi/generate.py`: clears a defer for the pages the superseding Case names.
> **＋** `vault/wiki/backlog.md`: the list of put-off items that `guppi backlog` writes.
> **＋** `rule-case-protocol`: sets how a Case takes up a defer.

> **when:**
> `uv run --project .guppi guppi generate` reads the decision line of this Case. The line names `estimate-spec-write-writes-a-defer` and supersedes `decision-case-885` and `decision-case-891`.
> **＋** `uv run --project .guppi guppi backlog` writes `vault/wiki/backlog.md` after it.

> **then:**
> `estimate-spec-write-writes-a-defer` carries no `deferred_by`. Its status, `method` and Criterion stay as they are.
> **＋** `decision-case-885` and `decision-case-891` stay `archived` in the folders where they stand, and each takes this Case into its `superseded_by`.
> **＋** `vault/wiki/backlog.md` no longer lists `estimate-spec-write-writes-a-defer`.

> **tasks:**
> - [ ] update `estimate-spec-write-writes-a-defer`
>   - change: `the defers of decision-case-885 and decision-case-891 taken up: the by-hand reading they waited for passed on 2026-10-26`

> **ratification:**
> ```
> - decision[case 902][update][estimate-spec-write-writes-a-defer]{ref:estimate-spec-write-writes-a-defer}{supersedes:case 885}{supersedes:case 891}
> ```
