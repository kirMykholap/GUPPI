---
type: rule
kind: Leaf
purpose: Prevents a set of ratified decisions from reaching the Spec with a contradiction between them or with the vault
status: draft
enforcement: render
governs: .claude/skills/pre-spec/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-prespec-reconciles]]", "[[estimate-prespec-checks-the-plan]]", "[[estimate-prespec-catches-bare-wikilinks]]", "[[estimate-prespec-catches-a-command-line-off-form]]", "[[estimate-prespec-catches-a-superseded-case]]", "[[estimate-prespec-binds-a-sprint-line]]", "[[estimate-prespec-catches-an-unwrapped-render]]", "[[estimate-prespec-catches-a-method-without-a-form]]", "[[estimate-prespec-simulates-the-pairs]]", "[[estimate-prespec-refuses-a-pair-inside-a-criterion]]", "[[estimate-prespec-checks-the-frame]]", "[[estimate-prespec-notes-a-long-chain]]", "[[estimate-prespec-checks-the-ratified-copy]]"]
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Purpose

Prevents a set of ratified decisions from reaching the Spec with a contradiction between
them or with the vault. The question to `ask-guppi` before a `create` without a `ref` asks "does this exist"; this
one asks, once, "does this set hold together". Its run is recorded by `guppi gate` on the `Skill` call, one `prespec` line with the session's stamp, which is what the pre-spec hook looks for (case 136.1).

## Render

<!-- rule-prespec -->
---
name: pre-spec
description: Check this Plan Mode's ratified decisions against each other and the vault before the Spec is approved.
---


Run `uv run guppi prespec --check <the plan file of this Plan Mode> --session <id>`, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder (cases 213.3, 256). Read the first line of the output before the exit code: 'no hi recorded for session …; nothing checked' means the wrong value, and the check did not run. It prints one line
for every decision line of this session that has no item under its own Case in the plan,
for every item that has no line, for every line of `raw/<hi date>/<hi HHMM>/frontier.md` (the session's folder, case 73) still open under `## Cases` — a line of `## Work` may stand open until its work is done (case 356.1) —, closed by a Case the plan does not hold, or closed `[x]` whose closer — the last segment after ` · ` — is `sprint`; `[-] … · sprint` is clean, a sprint item left for a later session, no Case and no `defer` needed (case 310.6), and a line whose source segment is `sprint` closed `· defer case N` is a finding — a sprint item is not deferred (case 356.2), and for every line closed `· case N` whose source segment — the one before the closer — is `sprint` and no `update` of the sprint page stands under Case N — a decided item of the sprint changes the sprint page (case 314.2), for every ratified Case with a line of a kind other than `defer` and no `tasks` block (a defer-only Case has no work, case 74), for every Estimate a `then` block creates or sets `pending` with no task line of its own — a line `- [ ] read `<slug>`` whose first backticked slug is that Estimate, as `generate` matches it when it ticks; a slug named on another Estimate's read line, or on a line that is not a read line, has no task line of its own (case 327), for every `update` item carrying `file` — the file route is gone (case 320), for every `replace` pair whose `old` stands inside the `## Criterion` of an Estimate page — a Criterion changes only whole (case 378.4), for every item of a `then` block carrying `sections: Render` whose target is a page with `enforcement: render` and whose text does not open with `<!-- slug -->` and close with `<!-- /slug -->` (case 325.1), for every Case whose `then` block holds two or more Estimate items — a `create`, or an `update` with `set: {status: pending}` — without a written `sections: Criterion` (one promise per Case: split it, by [[rule-atomicity]]), for every `update` of an Estimate whose page does not exist, and for every `create` of an Estimate whose `ref` names no live rule or entity (case 203.1), and for every `create` of an Estimate, or `update` carrying `set: {method: …}`, whose `method` names none of the four forms lint classifies — a `make <target>`, the word `pytest`, a path under `tests/`, or the words `by hand` — by lint's own predicate, the existence of the file and of the target left to lint (case 331), and for every `[[slug]]` outside a code span in the plan — in the blockquotes and in the strings of the `then` blocks — that names neither a live or archived page, nor a slug a `create` of the same plan carries, nor a hub file of `wiki/` (case 264.2), for every `{supersedes:case N}` line of the session's window whose `## Case N` or `### Case N` heading still stands in the plan — the superseded Case leaves the Spec, the superseding one is written whole, and a decision line of Case N then needs no item (case 299.2), and for every `tasks` line that opens with the bare word `render` or `sprint`, or with the command outside a code span — the tickers of `render` and `sprint` match the command in the first code span, and a line of another form stays debt (case 279.2), for every slug or path in a code span of a Case's `when` or `then` that its `given` — its own or its parent's — does not name, a path being a span that holds a `/` and one more character, and for every slug of its `then` block the `given` does not name (case 378.7); an Estimate has its own line and its own item (case 189). It then applies the `replace` and `reword` pairs of every Case of the plan to copies of the pages in memory, in entry order, whitespace collapsed as `generate` collapses it, writing nothing, and prints one line for every anchor that misses or hits more than once, with its Case, the page's slug and the opening of its `old` — the anchor judged against the page as the Spec leaves it, not as it stands today (case 351). It also runs every record line of the session's window — `raw/<hi date>/<hi HHMM>/ledger.md` whole, plus the date-level ledgers from the `hi` date to today from the `hi` time on, while any exist (case 103.4) — through `materialize.parse_line` and prints one line for each that does not parse, with its file and line number (case 75.2). It also prints one line for every Case of the plan whose ids, `given`, `when`, `then`, `then` block or `tasks` differ from its section in the ratified copy `<plan>.ratified.md` beside the plan file, for every Case of the plan with no section there and every section there with no Case in the plan — a Case a `{supersedes:case N}` of the window names excepted, and the Cases under `## Deferred` not compared — and for every name, `context` or `problem` still holding a Cyrillic letter: translate them before you run it (case 387.4). It also prints a line opening with `note:` for every Case whose `given` or `then` holds more than seven **＋** lines — a sign the Case is not atomic; a `note:` line is not a finding, sets no exit code and is answered in one line in the chat (case 378.8). Fix the plan, the frontier or the line for each finding, then run it again until it prints no finding.

Dispatch the `ask-guppi` agent once with the absolute path of the plan file and the instruction to read for every Case there outside the `## Deferred` heading its `context`, its `when` and `then` sections and its `then` block — `replace` old and new, `set`, `sections` — and, for an `update` of a rule or an entity, the page's `estimates`, before judging a page, so that a finding can name a wrong wording or a wrong place, and of a Case under `## Deferred` only the slugs of its `defer` items; the agent writes no list of the decisions — the plan is the list (case 388). Three questions: which of these contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes — one that does is a finding (case 203.2); which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out (case 388). Answer the findings with one report before any Case is shown again: each finding numbered, with the fix you propose or why it is already known, and the decisions you need from the person; then show the changed Cases again in one reply (case 388). A wrong fact of a `context` is fixed in the plan as a change of prose. The body of a Case under `## Deferred` is not read: the session that takes the defer up judges it with its own pre-spec. A Case of this plan that changes a page another Case of this plan defers is still a finding (case 186.2). Raise each
finding as a Case, or say in one line why it is already known. Then exit Plan Mode again.
<!-- /rule-prespec -->

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.2
- 2026-09-09 updated: dispatches `ask-guppi` · raw/2026-09-09/ledger.md#case-26.1
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: a Case changing a page's contract names the page's Estimates; a stale criterion is a finding · [[decision-case-53.2]]
- 2026-09-12 updated: the skill runs guppi pretask --check on the plan file before ask-guppi; every decision line since hi has its item under its own Case, every item its line (the command lives in guppi/pretask.py under rule-pretask-hook, case 66) · [[decision-case-59.1]]
- 2026-09-12 updated: the check also reads the session's frontier.md — an open line or a closing Case absent from the plan is a finding (case 59.2) · [[decision-case-59.2]]
- 2026-09-12 updated: a Case without tasks and an Estimate without its reading task are findings (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: a file item on a governed path is a finding — a rendered file has no file route (case 59.6) · [[decision-case-59.6]]
- 2026-09-12 deferred · [[decision-case-68]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-12 updated: findings for a missing method, a missing contract, two contracts in one Case and a colliding derived slug; no line for an Estimate (case 72.5) · [[decision-case-72.5]]
- 2026-09-12 updated: the frontier of the session's folder (case 73.4) · [[decision-case-73.4]]
- 2026-09-12 defer by decision-case-68 superseded · [[decision-case-74]]
- 2026-09-12 updated: a Case with work, not a Case with lines: the defer-only exemption of the code is the wording (case 74, supersedes 68) · [[decision-case-74]]
- 2026-09-12 updated: a ledger line of the window that does not parse is a finding (case 75.2) · [[decision-case-75.2]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 updated: a fifth form finding: the Estimate of a contract change is named when the page's list does not name it alone (case 90.2) · [[decision-case-90.2]]
- 2026-09-12 updated: the item's key is named estimate_slug, as case 86 ratified (case 99) · [[decision-case-99]]
- 2026-09-13 updated: the window is the session's ledger plus the date-level ledgers of the window (case 103.4) · [[decision-case-103.4]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-14 deferred · [[decision-case-121]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 defer by decision-case-121 superseded · [[decision-case-128]]
- 2026-09-14 updated: the pre-task dispatch carries the plan file's path and the instruction to read every Case's when, then and then block, not a summary (case 128) · [[decision-case-128]]
- 2026-09-14 updated: the Recorded line dropped; guppi gate writes the stamped pretask mark (case 136.1) · [[decision-case-136.1]]
- 2026-09-15 updated: the question to ask-guppi is the one before a create without a ref, not one per Case (case 155) · [[decision-case-155]]
- 2026-09-16 deferred · [[decision-case-182]]
- 2026-09-16 updated: a deferred Case enters the ask-guppi dispatch by slug and type only; its body is not read (case 186.2) · [[decision-case-186.2]]
- 2026-09-16 defer by decision-case-182 superseded · [[decision-case-191]]
- 2026-09-16 deferred · [[decision-case-191]]
- 2026-09-16 updated: the first sentence of the list no longer asks a purpose of a defer, in line with 186.2 (case 198) · [[decision-case-198]]
- 2026-09-16 estimate estimate-pretask-checks-the-plan added · [[decision-case-203.1]]
- 2026-09-16 defer by decision-case-191 superseded · [[decision-case-203.2]]
- 2026-09-16 updated: the findings of --check by the Estimate model; the list for ask-guppi carries the page's estimates and the ones the Case names; supersedes 191 (case 203.2) · [[decision-case-203.2]]
- 2026-09-16 updated: the dispatch sentence names the two questions of 203.2 (case 208.3) · [[decision-case-208.3]]
- 2026-09-17 updated: the check takes --session with the stamp of the hi line (case 213.3) · [[decision-case-213.3]]
- 2026-09-17 status: built → draft · cascade
- 2026-09-18 status: draft → built · cascade
- 2026-09-20 updated: --session takes the eight-character session id, the second token of the hi: line; the first line of the output is read before the exit code (case 256) · [[decision-case-256]]
- 2026-09-20 deferred · [[decision-case-259]]
- 2026-09-20 defer by decision-case-259 superseded · [[decision-case-261]]
- 2026-09-20 renamed from `rule-pretask` · [[decision-case-261]]
- 2026-09-20 updated: renamed to rule-prespec — the skill /pre-spec, the command guppi prespec, the mark prespec (case 261, supersedes 259) · [[decision-case-261]]
- 2026-09-20 ref `estimate-pretask-reconciles` → `estimate-prespec-reconciles` · [[decision-case-261]]
- 2026-09-20 ref `estimate-pretask-checks-the-plan` → `estimate-prespec-checks-the-plan` · [[decision-case-261]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 estimate estimate-prespec-catches-bare-wikilinks added · [[decision-case-264.2]]
- 2026-09-20 updated: the Render names the finding of --check on a bare `[[slug]]` in the plan file that names no page; the guard of case 264.2 · [[decision-case-264.2]]
- 2026-09-20 status: draft → built · cascade
- 2026-09-20 updated: pre-spec flags a render or sprint task line the tickers would not match (case 279.2) · [[decision-case-279.2]]
- 2026-09-20 estimate estimate-prespec-catches-a-command-line-off-form added · [[decision-case-279.2]]
- 2026-09-21 deferred · [[decision-case-298]]
- 2026-09-22 defer by decision-case-298 superseded · [[decision-case-299.2]]
- 2026-09-22 updated: a supersedes of the window whose Case still stands in the plan is a finding; a line of the superseded Case needs no item (case 299.2) · [[decision-case-299.2]]
- 2026-09-22 estimate estimate-prespec-catches-a-superseded-case added · [[decision-case-299.2]]
- 2026-09-22 updated: the closer `· sprint` accepted on a `[-]` line, a finding on `[x]` (case 310.6) · [[decision-case-310.6]]
- 2026-09-22 updated: a Frontier line of the sprint closed by a Case needs an update of the sprint page under it (case 314.2) · [[decision-case-314.2]]
- 2026-09-22 estimate estimate-prespec-binds-a-sprint-line added · [[decision-case-314.2]]
- 2026-09-22 updated: the one promise per Case check names rule-atomicity (case 317) · [[decision-case-317]]
- 2026-09-22 updated: the vault's rules named as pages, not as index.md (case 318) · [[decision-case-318]]
- 2026-09-22 updated: any file item is a finding, not only one on a governed path (case 320) · [[decision-case-320]]
- 2026-09-23 updated: a finding for a Render written without the page's own markers (case 325.1) · [[decision-case-325.1]]
- 2026-09-23 estimate estimate-prespec-catches-an-unwrapped-render added · [[decision-case-325.1]]
- 2026-09-23 updated: a reading's task line is matched as generate ticks it — one line per slug (case 327) · [[decision-case-327]]
- 2026-09-23 estimate estimate-prespec-catches-a-method-without-a-form added · [[decision-case-331]]
- 2026-09-23 updated: a finding for a method that names none of the forms lint classifies (case 331) · [[decision-case-331]]
- 2026-09-23 updated: the sprint test reads the source segment of a Frontier line, not every segment (case 335) · [[decision-case-335]]
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 estimate estimate-prespec-simulates-the-pairs added · [[decision-case-351]]
- 2026-09-23 updated: the pairs of the Spec simulated in entry order, an anchor that misses or is not unique reported with its Case (case 351, supersedes 332.2 and 345) · [[decision-case-351]]
- 2026-09-23 updated: an open line under Work is no finding (case 356.1) · [[decision-case-356.1]]
- 2026-09-23 updated: a sprint line closed defer case N is a finding (case 356.2) · [[decision-case-356.2]]
- 2026-09-23 updated: a pair inside a Criterion is a finding (case 378.4) · [[decision-case-378.4]]
- 2026-09-23 estimate estimate-prespec-refuses-a-pair-inside-a-criterion added · [[decision-case-378.4]]
- 2026-09-23 updated: when, then and the then block stay inside the frame of given (case 378.7) · [[decision-case-378.7]]
- 2026-09-23 estimate estimate-prespec-checks-the-frame added · [[decision-case-378.7]]
- 2026-09-23 updated: a soft note on a long chain (case 378.8) · [[decision-case-378.8]]
- 2026-09-23 estimate estimate-prespec-notes-a-long-chain added · [[decision-case-378.8]]
- 2026-09-24 updated: pre-spec checks the plan against its ratified copy and finds untranslated prose (case 387.4) · [[decision-case-387.4]]
- 2026-09-24 estimate estimate-prespec-checks-the-ratified-copy added · [[decision-case-387.4]]
- 2026-09-24 updated: ask-guppi reads the plan and the context itself; the agent answers the findings with one report before any Case is shown again (case 388) · [[decision-case-388]]
