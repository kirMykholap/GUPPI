## Case 467 — A backlog item leaves when the Case that decides it names its page

> **context:**
> `vault/wiki/backlog.md` has no state of its own. `guppi backlog` rewrites it whole from the pages that carry `deferred_by`, the open Insights, the `## Backlog` section of the sprint page, and the folders that hold `carry.md`. An item leaves when its source changes. For a deferred page, a Case carries `{supersedes:case M}`, and `generate.clear_deferred_by` then removes Decision M from `deferred_by`. The file changes only in the librarian's run and in `carry`, never while a session runs. The person saw a count that did not move because they read the file before the librarian's run over session 1819. That run took it from 19 to 16 items: cases 459, 462 and 463 removed `rule-claude-md`, `rule-one-judgment-one-implementation` and `rule-page-generation`. The cleared Insights of session 1255 are `actioned`, and neither is in the file.
> The mechanism has two gaps. First, no script checks that a Case which takes an item from the backlog supersedes its defers. Case 429 asks for this, but `prespec` checks only the closer word of a `backlog` line. Second, `clear_deferred_by` clears every target in the superseded Decision's `defer` list. Case 220 and case 243 each defer both `rule-git-context` and `rule-github-issues`, so deciding one page would remove the other from the backlog undecided. Clearing page by page brings up a third point. Cases 459 and 462 decided their items with no decision line on the deferred page. From now on, a Case that decides a backlog item names the page on a decision line. When nothing on the page changes, an `update` with only `change` is enough; it applies and writes a History line, as case 439 showed.
> The vault's answer: both new Estimates carry a `ref`, so no vault query is needed. A Glob of `vault/**/` finds no page for either slug.
> What the frame changes: the sentence of `rule-case-check` "the Frontier left to `/pre-spec`", the case-429 paragraph of `rule-case-protocol`, the finding list in the Render of `rule-prespec`, the sentence of the `rule-backlog` Purpose on how an item leaves, the docstrings of `guppi/casecheck.py` and `guppi/generate.py`, and the `supersedes` line of the Criterion of `estimate-generate-writes-the-decision-page`. The hook of 467.2 is the only hook on `SubagentStop`. 467.1 and 467.2 apply one rule to the page of a `backlog` line: some Case among Case N and its sub-cases both names the page on a decision line other than a `defer` and carries each `{supersedes:case M}`. 467.1 applies it at pre-spec to the Case the closed line names. 467.2 applies it before showing, to each top-level Case of the answer that names the page.
> Estimates not touched, and why:
> - `estimate-prespec-checks-the-frontier` speaks of boxes and closers.
> - `estimate-case-check-sends-back-a-faulty-case` promises that `judge` runs and that a finding goes back, not which checks it holds.
> - The Criterion of `estimate-case-protocol-ledger-line-form` promises the `{supersedes}` blocks of a deferred decision taken up, which stays true. The added requirement, the page named on a decision line, is held by the new `estimate-prespec-requires-a-backlog-item-decided-on-its-page`.
> - `estimate-backlog-renders` and `estimate-backlog-checks-the-file` promise the render from `deferred_by` and its check, which stay true. The update of the `rule-backlog` Purpose touches neither.
> - `estimate-generate-cascades` archives a superseded Decision and leaves `deferred_by` alone.
> - Line 32 of `estimate-git-context-current` records the past supersede of case 106 by case 115.
>
> Not done:
> - no checkboxes in `backlog.md`, and `guppi/backlog.py` is unchanged;
> - `insight-hi-skill-substitution-checked-by-a-model-call` stays until a Case rewrites its Pattern and Proposal with `{supersedes:case 448}`;
> - a `defer` of an Estimate or a lesson still writes no `deferred_by` (no case exists);
> - a Decision superseded for one of its pages is archived by the cascade in the same run, while a page of its `defer` list that the Case did not name still links to it in `deferred_by`; lint accepts the link, and a later supersede still reaches the Decision, since `generate.find` reads the archive.

> **problem:**
> A Case can decide a backlog item without retiring its defers, and nothing catches it. A Case that retires a defer shared by two pages clears both, although it decided one. The item should leave the backlog exactly when a Case decides it, page by page, and a Case that fails to make it leave should be sent back before it is ratified.

> **recommend:**
> Three sub-cases. 467.1 is a check in `guppi/prespec.py` on each Frontier line of the source `backlog` closed `[x] · case N`: Case N, or its sub-case, names the page on a decision line and supersedes each Decision of its `deferred_by`. 467.2 runs the same function from `casecheck --subagent` on each open `backlog` line, so case-guppi fixes the Case before the person sees it. 467.3 has `generate` clear a defer only from the pages the superseding Case names. Rejected: checkboxes in `backlog.md` only copy what `deferred_by` already says, and a hard refusal of every Case that touches a deferred page would block a Case like 460.5, which changed `rule-ledger-write` for another reason.

### Case 467.1 — pre-spec requires a backlog item decided on its page

> **given:**
> `rule-prespec` — the pre-spec check; its Render is the skill
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from `rule-prespec`, which lists the findings
> **＋** `guppi/prespec.py` — `judge` and `check_frontier`, where the new function lives
> **＋** `tests/test_prespec.py` — the tests of the check
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session, whose lines name the source and the closer
> **＋** `rule-case-protocol` — its case-429 paragraph says how a deferred decision is taken up; its Render is `vault/wiki/case-schema.md`
> **＋** `estimate-prespec-requires-a-backlog-item-decided-on-its-page` — the new promise

> **when:**
> `uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, the decision lines of the session's window, and the pages of the vault.

> **then:**
> For each line of the Frontier closed `[x] … · backlog · case N`, each page that its title names in a code span and that carries `deferred_by` is checked against Case N and its sub-cases.
> **＋** A finding when no decision line of Case N or of its sub-cases, other than a `defer`, names that page.
> **＋** A finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and `{supersedes:case M}`.
> **－** A line of another source, an open line, a line closed `work` or put off, and a page without `deferred_by`, such as an open Insight or a note of the sprint page's `## Backlog`, give no finding of this check.

> **tasks:**
> - [ ] `guppi/prespec.py` — one function that judges the page of a `backlog` Frontier line against the decision lines of a Case and its sub-cases and the page's `deferred_by`: some Case among them names the page on a line other than a `defer` and carries each `{supersedes:case M}`; `check_frontier` calls it on each line closed `[x] … · backlog · case N`
> - [ ] `tests/test_prespec.py` — a line closed `· backlog · case N` whose page is named by no line of Case N; one whose page is named but whose Decision M is not superseded; one where a sub-case names the page and carries every `{supersedes}` while another sub-case is an `update` of the page with only `change`; a page without `deferred_by`; a line of another source
> - [ ] update `rule-prespec`
>   - old: `changes the sprint page (case 314.2), for every ratified Case`
>   - new: `` changes the sprint page (case 314.2), for every line closed `· case N` whose source segment is `backlog` and whose title names in a code span a page with `deferred_by`, when no decision line of Case N or of a sub-case, other than a `defer`, names that page, or when no Case among them both names the page and carries `{supersedes:case M}` for a Decision M of its `deferred_by` — `generate` clears a defer only from the pages the superseding Case names (case 467.1), for every ratified Case ``
>   - change: `the finding on a backlog item decided without its page named and its defers superseded (case 467.1)`
> - [ ] update `rule-case-protocol`
>   - old: `so that every defer of the page is retired (case 429).`
>   - new: `` so that every defer of the page is retired (case 429); the Case, or the sub-case, that carries the blocks also names the page on a decision line other than a `defer` — an `update` with only `change` when nothing on the page changes — since `generate` clears a defer only from the pages the superseding Case names. `/pre-spec` reports a Case that closes a Frontier line of the source `backlog` when no Case among it and its sub-cases both names the page and carries each block; the check of the answer of `case-guppi` sends back a Case that names the page of an open `backlog` line when no Case among it and its sub-cases in the answer both names the page and carries each block (case 467). ``
>   - change: `a Case that takes up a deferred decision names its page on a decision line; what pre-spec and the check of case-guppi's answer each report (case 467)`
> - [ ] create `estimate-prespec-requires-a-backlog-item-decided-on-its-page`
>   - type: `estimate`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `A Case that decides an item taken from the backlog names its page and supersedes every Decision of its deferred_by, or pre-spec reports it`
>   - method: `uv run pytest tests/test_prespec.py -k backlog`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-prespec-requires-a-backlog-item-decided-on-its-page`

> **ratification:**
> ```
> - decision[case 467.1][update][rule-prespec]{ref:rule-prespec}
> - decision[case 467.1][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 467.1][create][estimate-prespec-requires-a-backlog-item-decided-on-its-page]{ref:rule-prespec}{tags:session,workflow,harness}
> ```

### Case 467.2 — the check of case-guppi's answer requires the same, on an open backlog line

> **given:**
> `rule-case-check` — the `SubagentStop` check of the answer of `case-guppi`; its text leaves the Frontier to pre-spec
> **＋** `guppi/casecheck.py` — `check_answer` and `subagent`, which will call the function of 467.1
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `guppi/prespec.py` — the one function that judges the page of a `backlog` Frontier line
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session, read for its open lines
> **＋** `rule-one-judgment-one-implementation` — one judgment in one module, imported by both callers
> **＋** `estimate-case-check-requires-a-backlog-item-decided-on-its-page` — the new promise

> **when:**
> `SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, and the pages of the vault.

> **then:**
> For each open line of the Frontier whose source is `backlog`, each page that its title names in a code span and that carries `deferred_by` is checked against each top-level Case N of the answer that, itself or through a sub-case, names that page on a decision line other than a `defer`.
> **＋** Case N gets a finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases in the answer both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and the missing mark. The hook exits 2, and `case-guppi` answers again.
> **＋** The judgment is the function of `guppi/prespec.py` that the pre-spec check runs, imported, not copied.
> **－** A Case of the answer that names no such page, an answer while no open line of the source `backlog` stands, and a page without `deferred_by` get no finding of this check.

> **tasks:**
> - [ ] `guppi/casecheck.py` — `subagent` passes the session's `frontier.md` and the records of the `ratification` fences to the function of `guppi/prespec.py` for each open `backlog` line and each top-level Case of the answer that names its page; the docstring sentence "The Frontier and the grammar of the window stay with `/pre-spec` (case 445.2)" names this one exception
> - [ ] `tests/test_casecheck.py` — an answer whose Case names the page of an open `backlog` line without its `{supersedes}`, sent back; the same with every `{supersedes}`, passed; a sub-case that names the page and carries every `{supersedes}` beside a sub-case that is an `update` of the page with only `change`, passed; a Case naming the page only in a `defer` line; no open `backlog` line
> - [ ] update `rule-case-check`
>   - old: `` does not judge by their keys (case 436.4), the Frontier left to `/pre-spec`. ``
>   - new: `` does not judge by their keys (case 436.4), the Frontier left to `/pre-spec` but for one check: for each open line of the session's `frontier.md` whose source is `backlog` and each page of its title that carries `deferred_by`, a Case of the answer that, itself or through a sub-case, names the page on a decision line other than a `defer` gets a finding for each Decision of that list when no Case among it and its sub-cases both names the page and carries its `{supersedes}`, by the function of `guppi/prespec.py` that `/pre-spec` runs (case 467.2). ``
>   - change: `the answer of case-guppi is checked against the open backlog lines of the Frontier (case 467.2)`
> - [ ] create `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
>   - type: `estimate`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `A Case of case-guppi that names the page of an open backlog line, where no Case among it and its sub-cases both names the page and supersedes every Decision of its deferred_by, goes back to case-guppi`
>   - method: `uv run pytest tests/test_casecheck.py -k backlog, then by hand the first answer of case-guppi on an item taken from the backlog`
>   - tags: `[hooks, harness, workflow]`
> - [ ] read `estimate-case-check-requires-a-backlog-item-decided-on-its-page`

> **ratification:**
> ```
> - decision[case 467.2][update][rule-case-check]{ref:rule-case-check}
> - decision[case 467.2][create][estimate-case-check-requires-a-backlog-item-decided-on-its-page]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 467.3 — generate clears a defer only from the pages the superseding Case names

> **given:**
> `guppi/generate.py` — `decision` and `clear_deferred_by`, and the docstring that describes a `supersedes`
> **＋** `tests/test_generate.py` — the tests of the Decision page and of a `supersedes`
> **＋** `rule-page-generation` — the rule of `generate`, whose mechanism lives in the docstring
> **＋** `estimate-generate-writes-the-decision-page` — its Criterion states the clearing of every target of the `defer` list
> **＋** `rule-backlog` — its Purpose says how an item leaves the backlog
> **＋** `vault/wiki/backlog.md` — the file `guppi backlog` writes from `deferred_by`

> **when:**
> `uv run guppi generate` writes the Decision page of a Case whose decision lines carry `{supersedes:case M}`.

> **then:**
> Decision M is set `superseded`, and the Case is appended to its `superseded_by`.
> **＋** Each page of the `defer` list of Decision M that a decision line of the Case names drops Decision M from its `deferred_by`. An empty `deferred_by` is dropped.
> **＋** A later Case that supersedes Decision M again clears the pages it names in the same way.
> **－** A page of the `defer` list that no decision line of the Case names keeps Decision M in its `deferred_by`, and stays in `vault/wiki/backlog.md`.

> **tasks:**
> - [ ] `guppi/generate.py` — `clear_deferred_by` takes the slugs that the superseding record's `targets` name and clears only those pages; the docstring sentence "removes its slug from the `deferred_by` of every target of its `defer` list" says the same
> - [ ] `tests/test_generate.py` — a Decision that defers two pages, superseded by a Case naming one of them: one page cleared, one kept; a second Case superseding the same Decision, then archived, and naming the other page: that page cleared too
> - [ ] update `estimate-generate-writes-the-decision-page`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a supersedes clears deferred_by only on the pages the superseding Case names (case 467.3)`
>   - sections.Criterion:
>     ```
>     When:
>     `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.
>
>     Then:
>     One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Context` and `## Problem` from `case_text`, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
>     **＋** The page is written before the first entry of its lines, so their History lines name it.
>     **＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
>     **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`.
>     **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
>     **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
>     **－** The page holds no `## When` and no `## Criterion`: the promise lives on the Estimate.
>     ```
> - [ ] update `rule-backlog`
>   - old: `a Case that decides it supersedes its defer`
>   - new: `a Case that decides it names its page on a decision line and supersedes its defer (case 467.3)`
>   - change: `an item leaves when the Case that decides it names its page and supersedes its defer (case 467.3)`
> - [ ] read `estimate-generate-writes-the-decision-page`

> **ratification:**
> ```
> - decision[case 467.3][update][estimate-generate-writes-the-decision-page]{ref:estimate-generate-writes-the-decision-page}
> - decision[case 467.3][update][rule-backlog]{ref:rule-backlog}
> ```
