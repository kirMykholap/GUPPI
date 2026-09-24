<!-- approved 23:45:21 · session 106153e6 -->

# Spec — session 2026-09-24 2214

## Case 406 — `rule-case-protocol`: no count of items in the story sections of a Case

> **context:**
> The agent writes counts in the story sections of a Case: how many lines a journal has, how many Estimates are touched. A count goes stale first. An item is added or removed, the count stays in the text and goes into the Spec and onto the Decision page. In session 1916 this was a source of errors. `CLAUDE.md` already says that a count comes from the run that printed it. But a Case is written before the run and edited after it, and nothing checks the count in it. Today the Language paragraph of the Render of `rule-case-protocol` forbids in the story sections a count of sentences, line numbers and quotations. It does not forbid a count of items. The rule goes into `case-schema.md`, not into `CLAUDE.md`: `CLAUDE.md` works without GUPPI too, and only `/hi` loads the Case schema. `estimate-case-protocol-case-form` stands `pending`. Case 396.1 of the conserved Spec of session 1916 already replaces its Criterion whole. This Case takes the `when` and `then` of 396.1 and extends the line on `context`, so the Spec of 1916 is applied first. An `update` with a `ref`, no vault query. `frame-guppi` found no contradiction. The other Estimates of the rule speak of other things, and this Case does not touch them. `estimate-agent-writing-followed` speaks of the width of a claim in any text of the agent, which this Case does not change, so it is not touched either.

> **problem:**
> The rule does not forbid a count of items in `context`, `problem` and `recommend`. A stale count goes into the Spec and onto the Decision page, and neither the ratification nor a script catches it.

> **given:**
> `rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the Sections table and the Language paragraph on the story sections.
> **＋** `estimate-case-protocol-case-form` — the Estimate whose Criterion is replaced.
> **＋** `rule-agent-writing` — the writing rule in `CLAUDE.md`: a count comes from the run that printed it.

> **when:**
> The agent shows a Case in the chat, at its first showing or again.

> **then:**
> The Case opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds its sections in the order of the Sections table, each one blockquote whose first line is `**name:**`.
> **＋** `context` is prose: the mechanism in plain words first, then the state of the pages the Case changes, the vault's answer and why an Estimate of the rule is not touched; a case number stands in `context` or `problem` only when the Case is about that case, and a count of items stands in none of the story sections unless the Case is about that count.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state; `when` and `then` name only what `given` names.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, and `then` holds behaviour only.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; the agent's own text stands after the Case, after one horizontal rule, and the reply ends with a plain question.
> **＋** A Case with sub-cases is shown in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: no line numbers and no quotation unless the Case is about one;
    new: 'no line numbers and no quotation unless the Case is about one; no count of items — lines, pages, Estimates, Cases — unless the Case is about that count: a count goes stale first, and what can be counted a script counts;'
  change: the story sections name no count of items unless the Case is about that count (case 406)
- slug: estimate-case-protocol-case-form
  set:
    status: pending
  change: the Criterion replaced whole — the line on context names no count of items in the story sections; the rest as case 396.1 wrote it (case 406)
```

```tasks
- [ ] update `rule-case-protocol` — the Language paragraph of the Render: no count of items in the story sections
- [ ] update `estimate-case-protocol-case-form` — the Criterion replaced whole by the `when` and `then` of this Case
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-case-form` — by hand, the Cases of this session at its close
```

## Deferred

## Case 408 — Whether frame-guppi pays

> **context:**
> Case 403 deferred the question: whether `frame-guppi` pays, judged by the contradictions it finds against its tokens and time. In session 2214 it was dispatched three times — twice for Case 406, once for Case 407. It found no contradiction for Case 406 and one for Case 407: the circular import between `guppi/prespec.py` and `guppi/ratified.py`, which would have broken the code of Cases 407.2 and 407.4 at the first load. The dispatch for Case 407 cost about 160 thousand tokens and six minutes. The pre-spec of the same session then found in Case 407 contradictions that `frame-guppi` had not reported, with the frame it had read. The person chose to spend the rest of the session on Work Mode.

> **problem:**
> Keep `frame-guppi` or roll it back: decided in a later session, with the data of sessions 1916 and 2214.

```then
defer:
  - slug: rule-frame-check
    type: rule
    purpose: Whether frame-guppi pays — the contradictions it finds against its tokens and time, with the dispatches of sessions 1916 and 2214; rolled back by a Case if it does not
```

## Case 409 — The limit of 400 000 tokens and the text of its hook

> **context:**
> Case 404 deferred the limit of 400 000 tokens in `guppi/context.py`. The brief of session 1916 adds a second point on the same page: past the limit the `UserPromptSubmit` hook orders the session closed with `/retro` and `/handoff`, and the person reads the mark as "take no more work", not as a reason to leave Plan Mode for Retro. Both wait for a session that reaches the limit.

> **problem:**
> Which limit is right, and what the hook says past it: decided once a session reaches it.

```then
defer:
  - slug: rule-context-size
    type: rule
    purpose: The limit of 400 000 tokens in guppi/context.py, and the text of the UserPromptSubmit hook past it — take no more work, not close the session; judged once a session reaches it
```

## Case 412 — Only hooks write the Spec: deferred with the findings of pre-spec

> **context:**
> Case 407 was ratified in this session and leaves the Spec by this Case. Its mechanism: `prespec --check --case N` checks one Case without the Frontier and the translation; the `Stop` hook of `rule-spec-write` runs it on each Case it writes and gives the findings back by exit 2; a `PreToolUse` guard of `rule-spec-reconcile` refuses every edit of the plan by the agent but its creation and the part below `## Deferred`; the agent writes the name, `context`, `problem`, `given` and the task lines that are no items through a `Write` of `<plan>.fragment.md`, which the guard refuses, merges into the plan and checks; the comparison with the ratified copy drops `given` and the task lines that are no items. The full text of Case 407 stands in the ratified copy of this plan. The pre-spec of this session found in it what the next session answers first: a `given` written unshown still reaches the Decision page, against the purposes of `rule-spec-write` and `rule-spec-reconcile`; the `ratification` row of the Case schema keeps clauses on an edit of the plan and a `DIFF` of it, and a new task line on a file changes the scope; `is_plan` takes the fragment and the plan of a subagent for plan files; the finding of a ledger line that does not parse names no Case; `estimate-case-protocol-checks-its-frame` reads a changed `given` before a showing again, which would no longer happen; an exit 2 after the acknowledging reply makes the agent go on after its `LEDGER` block; no page says whether `guppi ledger` writes its lines before `guppi ratified` checks them at the same `Stop`; in Plan Mode the client may ask the person before a `Write` outside the plan file, by `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt`. The question of Case 410 — when the prose of a Case is translated — waits for the same mechanism and is taken in here.

> **problem:**
> How the Spec is written by hooks alone, with each Case checked at once: decided in a later session, with the findings above answered.

```then
defer:
  - slug: rule-prespec
    type: rule
    purpose: The check of one Case, prespec --check --case N, run by the hooks after each ratified Case (case 407.1, 407.5)
  - slug: rule-spec-write
    type: rule
    purpose: The Stop hook checks each Case it writes and gives the findings back (case 407.2)
  - slug: rule-spec-reconcile
    type: rule
    purpose: The agent writes into the plan only through a fragment the guard merges and checks; when the prose of a Case is translated (cases 407.3, 407.4, 410)
```

## Case 413 — One behaviour signed from two sides

> **context:**
> The pre-spec of session 1916 found a promise signed twice: `estimate-case-protocol-case-form` (Case 396.1) and `estimate-prespec-checks-the-frame` both say that `when` and `then` name only what `given` names — the first as the form of a Case, the second as the finding of `prespec --check`. Case 406 carried the line of 396.1 on unchanged. Case 411 deferred the question on `rule-case-protocol`, which Case 406 changes in the same Spec; this Case defers it on `rule-prespec`, the page of the other Estimate, and supersedes 411.

> **problem:**
> Which of the two Estimates keeps the line: decided in a later session.

```then
defer:
  - slug: rule-prespec
    type: rule
    purpose: The line on the frame — when and then name only what given names — signed by estimate-case-protocol-case-form and estimate-prespec-checks-the-frame; one of them keeps it
```
