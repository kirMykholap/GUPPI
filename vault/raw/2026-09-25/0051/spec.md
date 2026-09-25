<!-- approved 03:21:16 · session df1dd1da -->

# Spec — session 2026-09-25 0051

## Case 414 — Each Case checked right after it is written

> **context:**
> Today the plan is checked once, at `/pre-spec`. The findings pile up until the end of Plan Mode, and a Case written with a fault is found late. Case 407 proposed to check each Case right after it is written and to close the plan to the agent's edits by a guard and a fragment. The pre-spec of session 2214 found contradictions in it, and Case 412 deferred it together with the question of Case 410. This Case takes 412 up and keeps of 407 only the check at once: the `Stop` hook of `rule-spec-write` writes a Case, runs the checks of `prespec --check` on it and gives the findings back to the agent. The guard, the fragment and the comparison without `given` are withdrawn; most findings fell on them. `ratified --edit` on `PostToolUse` still guards the plan.
>
> The other findings are answered so:
> - **The grammar of the ledger lines.** The check of one Case does not read it. A finding on a line that does not parse names no Case, and `/pre-spec` keeps it.
> - **The order of the hooks.** The Claude Code hooks documentation says: "All matching hooks run in parallel". So the hook takes the decision lines from the reply itself and does not wait for `ledger.md`.
> - **Exit 2 after the acknowledging reply.** The agent goes on after its `LEDGER` block. Sub-case 414.2 says that this is a reply of its own.
>
> There is no separate option `prespec --check --case N`: the hook imports the checks, and with the option the Criterion of the Estimates of `prespec --check` that promise to read the Frontier, the ratified copy and the grammar of the window would have to change.
>
> This Case does not decide the question of Case 410, when the prose of a Case is translated. But `{supersedes:case 412}` also lifts the defer of `rule-spec-reconcile`, so the question stays a Frontier item, and a new defer is due at the close of Plan Mode if this session does not decide it.
>
> `frame-guppi` found:
> - the option `--case` contradicted the Estimates of `prespec --check`, so the option is dropped;
> - the sentence on the answer after a refusal was wider than the truth when the ledger hook itself refuses, so it is narrowed to another `Stop` hook;
> - it took the order of the hooks for sequential, which the documentation refutes.
>
> `estimate-spec-write-copies-the-ratified-case` is not touched: its list of refusals is not closed, and the new refusal does not contradict it. Every `create` here is an Estimate with a `ref`, so no vault query is needed.

> **problem:**
> The agent learns of a fault in a written Case only at `/pre-spec`, when the Cases are already many. Each Case should be checked right after it is written, by the same checks as at pre-spec, and the result should not depend on the order of the hooks on one `Stop`.

### Case 414.1 — The Stop hook checks each Case it wrote

> **given:**
> `rule-spec-write` — the `Stop` hook that writes a ratified Case into the plan; its `How it works`.
> **＋** `estimate-spec-write-checks-the-written-case` — the new promise.
> **＋** `rule-prespec` — the checks of `prespec --check`, which the hook runs.
> **＋** `guppi/ratified.py` — `stop`, which writes the Cases of a reply.
> **＋** `guppi/prespec.py` — the checks, run for one Case.
> **＋** `tests/test_ratified.py` — fixes the check after the write.
> **＋** `raw/<hi date>/<hi HHMM>/frontier.md` — the Frontier, which the check after the write skips.

> **when:**
> The `Stop` hook `uv run guppi ratified` has written Case N into the plan file and its ratified copy after a reply whose `LEDGER` block holds the decision lines of Case N.

> **then:**
> The hook runs the checks of `prespec --check`, imported from `guppi/prespec.py`, on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
> **＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
> **＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan and in its ratified copy.
> **＋** A finding of a Case not written in this run is not reported.
> **－** On the re-fire (`stop_hook_active`) nothing is checked: exit 0.
> **－** A Case not written in this run — a last showing that is a `DIFF` block, a defer-only Case — is not checked.
> **－** The Frontier `raw/<hi date>/<hi HHMM>/frontier.md` is not read.
> **－** The plan is not compared with its ratified copy, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
> **－** A ledger line of the window that does not parse is no finding of this check.

```then
create:
- slug: estimate-spec-write-checks-the-written-case
  kind: QA
  purpose: Each Case the Stop hook writes into the plan is checked at once, and a finding comes back to the agent
  method: uv run pytest tests/test_ratified.py -k checks_the_written; by hand, the first ratification of a session after the change
  tags:
  - hooks
  - harness
  - workflow
  ref: rule-spec-write
update:
- slug: rule-spec-write
  replace:
  - old: A last showing that is a `DIFF` block writes nothing.
    new: A last showing that is a `DIFF` block writes nothing. After the write it runs the checks of `prespec --check`, imported from `guppi/prespec.py`, on each Case it wrote, with the decision lines of the reply added to those of the session's ledger — the ledger hook runs in parallel on the same `Stop` — and without the Frontier, the ratified copy, the translation and the grammar of the ledger, which stay with `/pre-spec`; on a finding it exits 2 with the findings on stderr, each naming its Case, and the written Case stays (case 414.1).
  change: the Stop hook checks each Case it wrote (case 414.1)
```

```tasks
- [ ] update `rule-spec-write` — one sentence in `How it works`: the check after the write
- [ ] create `estimate-spec-write-checks-the-written-case` — the new promise of the check after the write
- [x] `guppi/prespec.py` — the checks of `check` for a set of Cases and extra records, the Frontier, the ratified copy and the grammar left out; `check` calls the same function for the whole run
- [x] `guppi/ratified.py` — `stop`: the checks on each Case written, the reply's decision records added to the window's, `guppi/prespec.py` imported inside the function; the module docstring
- [x] `tests/test_ratified.py` — `-k checks_the_written`: a written Case with a finding exits 2 and stays written, a clean one exits 0, a finding of another Case not reported, a line of the reply not yet in the ledger counted, the re-fire checks nothing
- [ ] read `estimate-spec-write-checks-the-written-case` — `uv run pytest tests/test_ratified.py -k checks_the_written`, then by hand at the first ratification after the change
```

### Case 414.2 — The answer to a Stop hook's refusal is a reply of its own

> **given:**
> `rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the paragraph on ledger lines.
> **＋** `estimate-case-protocol-acknowledging-reply` — the Estimate whose Criterion is replaced.
> **＋** `rule-ledger-write` — the ledger hook on `Stop`, which writes the `LEDGER` block of the reply.

> **when:**
> The person ratifies a Case, or ratifies again a Case shown again after its ratification, and the agent writes the reply that acknowledges it.

> **then:**
> The reply has four parts, in this order: the `LEDGER` block first; the heading `## Case N — ratified` and a paragraph `Changes:` — what changes, in one or two sentences; a paragraph `Notes:` — facts that did not enter the Case, omitted when there are none; the heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last.
> **＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` naming the ids, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply — exit 2 — the agent's answer to the refusal is a reply of its own and may call tools; the `LEDGER` block stands written.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: and the last reply of a session has none.
    new: 'and the last reply of a session has none. When a `Stop` hook other than the ledger hook refuses a reply that carries a `LEDGER` block — exit 2 — the ledger hook has written the block at that same `Stop`: the agent''s answer to the refusal is a reply of its own and may call tools (case 414.2).'
  change: the answer to a Stop hook's refusal after a LEDGER block is a reply of its own (case 414.2)
- slug: estimate-case-protocol-acknowledging-reply
  set:
    status: pending
  change: the Criterion replaced whole — the answer to a Stop hook's refusal is a reply of its own (case 414.2)
```

```tasks
- [ ] update `rule-case-protocol` — the paragraph on ledger lines in the Render: the answer to a refusal
- [ ] update `estimate-case-protocol-acknowledging-reply` — the Criterion replaced whole by the `when` and `then` of this Case
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-acknowledging-reply` — by hand, the first acknowledging reply a `Stop` hook refuses
```

## Case 415 — The pre-spec check holds the line on the frame

> **context:**
> One promise is signed twice. `estimate-case-protocol-case-form` promises in its line on `given`: "`when` and `then` name only what `given` names". It is read by hand at the close of a session. `estimate-prespec-checks-the-frame` promises the same as a finding of `prespec --check`, and a test reads it. `case-form` stands `pending`, `checks-the-frame` `passed`. The pre-spec of session 1916 found the double, and Case 413 deferred the choice. The rule itself in the Render of `rule-case-protocol` (the Sections table) does not change, so the behaviour of the rule and of the hooks stays as it is and `frame-guppi` is not dispatched. Only the Criterion of one Estimate changes. No vault query: it is an `update` with a `ref`.

> **problem:**
> Which of the two Estimates keeps the line on the frame, so that one promise is signed once?

> **given:**
> `estimate-case-protocol-case-form` — the Estimate whose Criterion is replaced.
> **＋** `estimate-prespec-checks-the-frame` — the Estimate that keeps the line on the frame.
> **＋** `rule-case-protocol` — the rule whose Case form the first Estimate reads.

> **when:**
> The agent shows a Case in the chat, at its first showing or again.

> **then:**
> The Case opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds its sections in the order of the Sections table, each one blockquote whose first line is `**name:**`.
> **＋** `context` is prose: the mechanism in plain words first, then the state of the pages the Case changes, the vault's answer and why an Estimate of the rule is not touched; a case number stands in `context` or `problem` only when the Case is about that case, and a count of items stands in none of the story sections unless the Case is about that count.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, and `then` holds behaviour only.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; the agent's own text stands after the Case, after one horizontal rule, and the reply ends with a plain question.
> **＋** A Case with sub-cases is shown in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole.

```then
update:
- slug: estimate-case-protocol-case-form
  set:
    status: pending
  change: the Criterion replaced whole — the line on the frame of when and then left to estimate-prespec-checks-the-frame (case 415)
```

```tasks
- [ ] update `estimate-case-protocol-case-form` — the Criterion replaced whole by the `when` and `then` of this Case
- [ ] read `estimate-case-protocol-case-form` — by hand, the Cases of this session at its close
```

## Case 417 — A parent whose sub-cases are all superseded is no finding of the ratified copy

> **context:**
> `prespec --check` compares the plan with its ratified copy. A section of the copy with no Case in the plan is a finding. There is one exception: a Case a `{supersedes:case N}` of the session's window names. It breaks on a parent. A parent has no ledger lines of its own; its sub-cases carry them. When every sub-case is superseded, the parent leaves the plan with them, but its heading stays in the copy, and no `supersedes` line names it. In session 2214 this happened to Case 407: 412 superseded 407.1–407.5, and pre-spec still printed `case 407: in the ratified copy, not in the plan`. This is `lesson-prespec-parent-of-superseded-sub-cases`. The change touches one sentence of the Render of `rule-prespec` and the Criterion of `estimate-prespec-checks-the-ratified-copy`, and no other Estimate. `frame-guppi` found no contradiction. The lesson gets no mark: it was written in another session. No vault query: both items are an `update` with a `ref`.

> **problem:**
> A parent whose sub-cases are all superseded gives a false finding at every `/pre-spec` of its session, and the agent has to explain it by hand.

> **given:**
> `rule-prespec` — its Render `.claude/skills/pre-spec/SKILL.md`: the sentence on the ratified copy.
> **＋** `estimate-prespec-checks-the-ratified-copy` — the Estimate whose Criterion is replaced.
> **＋** `guppi/prespec.py` — `check_ratified`, the sections of the copy with no Case in the plan.
> **＋** `tests/test_prespec.py` — fixes the comparison with the ratified copy.

> **when:**
> `guppi prespec --check <plan>` runs at `/pre-spec`, after the agent translated the names, `context` and `problem` of the plan, and reads the plan and its ratified copy `<plan>.ratified.md`.

> **then:**
> A Case of the plan whose ids, `given`, `when`, `then`, `then` block or `tasks` differ from its section in the ratified copy: one finding naming the Case and the parts.
> **＋** A Case of the plan with no section in the copy, and a section of the copy with no Case in the plan: one finding each.
> **＋** A name, `context` or `problem` that still holds a Cyrillic letter: one finding.
> **－** The section of a Case a `{supersedes:case N}` of the session's window names is no finding: that Case left the plan (case 299.1).
> **－** The section of a parent with sub-cases in the copy, every one of them named by such a line, is no finding: the parent left the plan with them.
> **－** A Case under `## Deferred` is not compared.

```then
update:
- slug: rule-prespec
  replace:
  - old: a Case a `{supersedes:case N}` of the window names excepted
    new: a Case a `{supersedes:case N}` of the window names excepted, and a parent with sub-cases in the copy, every one of them named by such a line (case 417)
  change: a parent whose every sub-case is superseded is no finding of the ratified copy (case 417)
- slug: estimate-prespec-checks-the-ratified-copy
  set:
    status: pending
  change: the Criterion replaced whole — a parent whose every sub-case is superseded is no finding (case 417)
```

```tasks
- [ ] update `rule-prespec` — the sentence on the ratified copy in the Render: the parent of superseded sub-cases excepted
- [ ] update `estimate-prespec-checks-the-ratified-copy` — the Criterion replaced whole by the `when` and `then` of this Case
- [x] `guppi/prespec.py` — `check_ratified`: a section of the copy with no Case in the plan excepted when it is a parent with sub-cases in the copy, each named by a supersedes of the window
- [x] `tests/test_prespec.py` — `-k ratified`: a parent whose sub-cases are all superseded no finding; a parent with one sub-case not superseded still a finding
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-checks-the-ratified-copy` — `uv run pytest tests/test_prespec.py -k ratified`
```

## Deferred

## Case 416 — The Case built by case-guppi, shown and written by hooks

> **context:**
> Today the main agent reads the pages of a Case, then `frame-guppi` reads the same frame again, and the main agent writes the Case into the chat; the agent also edits the plan to translate it. In this session the person proposed a new scheme: the main agent reads only the Frontier item and its source and decides — answer itself, discuss a fork, or dispatch; a Case is always built by one subagent, `case-guppi` (the renamed `frame-guppi`, on Opus with effort medium), which asks the vault, reads the frame and writes the Case; a `SubagentStop` hook checks it by the checks of `prespec --check` and sends it back on a finding; a hook shows the checked Case to the person by `systemMessage`; a question or a change goes to the same `case-guppi` by `SendMessage`; `ratified` writes the Case the person saw; a guard refuses every edit of the plan by the agent while a line under `## Cases` of the Frontier is open, the defers written by the hook too, and the translation comes after; `ask-guppi` answers at pre-spec only; the orchestration of the main agent becomes a rule of its own, loaded by `/hi`, and `case-schema.md` goes to `case-guppi`. Measured in this session from the transcript: the answer of a subagent in the main transcript is wrapped and indented by the harness, its raw text stands in `subagents/agent-<id>.jsonl`; the reply to `SendMessage` comes as a `task-notification`; a `SendMessage` after a pause re-cached the agent's whole context. Not yet measured: how a long `systemMessage` renders, the live payload of `SubagentStop`, and whether a `systemMessage` stands in the transcript — the live probe of this session's Work Mode, reported in the handoff. The question of Case 408 — whether `frame-guppi` pays — is taken into this one.

> **problem:**
> How a Case is built, checked, shown and written under the new scheme: decided in the next session, with the results of the live probe.

```then
defer:
  - slug: rule-frame-check
    type: rule
    purpose: frame-guppi becomes case-guppi, which builds the Case from the Frontier item and the person's choices — the vault query, the frame, the form — on Opus with effort medium, and is asked again by SendMessage; whether it pays, measured by its dispatches (the question of case 408)
  - slug: rule-case-protocol
    type: rule
    purpose: case-schema.md read by case-guppi only; the orchestration of the main agent — the triage of a Frontier item, the dispatch, the acknowledging reply, LEDGER, defers and the one rule — a rule of its own loaded by /hi
  - slug: rule-spec-write
    type: rule
    purpose: The Case checked on SubagentStop and shown by a hook from the answer of case-guppi; ratified writes the Case the person saw, and writes the defers too
  - slug: rule-spec-reconcile
    type: rule
    purpose: The plan written by hooks alone — a guard refuses the agent's edits while a line under Cases of the Frontier is open; when and how the prose of a Case is translated (the question of case 410)
  - slug: rule-ask
    type: rule
    purpose: ask-guppi answers at pre-spec only; the vault query before a create moves to case-guppi
```

## Case 418 — The limit of 400 000 tokens, again

> **context:**
> Cases 404 and 409 deferred the limit of 400 000 tokens in `guppi/context.py` and the text of the `UserPromptSubmit` hook past it: take no more work, not close the session. The session that would judge them has not come yet; this session did not take the item up.

> **problem:**
> Which limit is right, and what the hook says past it: decided once a session reaches it.

```then
defer:
  - slug: rule-context-size
    type: rule
    purpose: The limit of 400 000 tokens in guppi/context.py, and the text of the UserPromptSubmit hook past it — take no more work, not close the session; judged once a session reaches it
```
