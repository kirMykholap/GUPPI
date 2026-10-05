---
type: rule
kind: Leaf
purpose: Prevents a set of ratified decisions from reaching the Spec with a contradiction between them or with the vault
status: draft
enforcement: render
governs: .claude/skills/pre-spec/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-prespec-reconciles]]", "[[estimate-prespec-checks-the-plan]]", "[[estimate-prespec-catches-bare-wikilinks]]", "[[estimate-prespec-catches-a-command-line-off-form]]", "[[estimate-prespec-catches-a-superseded-case]]", "[[estimate-prespec-binds-a-sprint-line]]", "[[estimate-prespec-catches-an-unwrapped-render]]", "[[estimate-prespec-catches-a-method-without-a-form]]", "[[estimate-prespec-simulates-the-pairs]]", "[[estimate-prespec-refuses-a-pair-inside-a-criterion]]", "[[estimate-prespec-checks-the-frame]]", "[[estimate-prespec-notes-a-long-chain]]", "[[estimate-prespec-matches-lines-and-items]]", "[[estimate-prespec-checks-the-frontier]]", "[[estimate-prespec-requires-a-task-line]]", "[[estimate-prespec-checks-the-form-of-an-item]]", "[[estimate-prespec-requires-a-backlog-item-decided-on-its-page]]", "[[estimate-prespec-catches-a-broken-fence]]", "[[estimate-prespec-catches-an-indent-added-twice]]", "[[estimate-prespec-gathers-the-answers-after-findings]]", "[[estimate-prespec-catches-two-cases-on-one-target]]", "[[estimate-prespec-confirms-the-findings-once]]"]
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Purpose

Prevents a set of ratified decisions from reaching the Spec with a contradiction between
them or with the vault. The vault query of `case-guppi` before a `create` without a `ref` asks "does this exist"; this
one asks, once, "does this set hold together". Its run is recorded by `guppi gate` on the `Skill` call, one `prespec` line with the session's stamp, which is what the pre-spec hook looks for (case 136.1).

## Render

<!-- rule-prespec -->
---
name: pre-spec
description: Check this Plan Mode's ratified decisions against each other and the vault before the Spec is approved.
---

Run `uv run guppi prespec --check <the plan file of this Plan Mode> --session <id>`, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder (cases 213.3, 256). Read the first line of the output before the exit code: 'no hi recorded for session …; nothing checked' means the wrong value, and the check did not run. Each line it prints is a finding, except a line that opens with `note:`, which is no finding: it sets no exit code and is answered in one line in the chat (case 378.8). What the check compares is written in the module docstring of `guppi/prespec.py`, beside its code (case 561.1). Fix a finding in the Frontier or in a ledger line yourself, and run the check again until it prints no finding of that kind. A finding in a Case — its prose or its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case in the loop below; do not edit the text of a Case in the plan (cases 438, 441).

At the first run of `/pre-spec` in the session only, dispatch one `ask-guppi` agent for each top-level Case outside the `## Deferred` heading — of the plan, or, when the plan's title line names a conserved Spec, of that Spec — all in one message, each with the absolute path of the plan file, the id of the Case it judges — that Case and its sub-cases, the other Cases read only to find a clash with them (case 634.1) — and the instruction to read for every Case there outside the `## Deferred` heading its `context`, its `when` and `then` sections and its `then` block — `replace` old and new, `set`, `sections` — and, for an `update` of a rule or an entity, the page's `estimates`, before judging a page, so that a finding can name a wrong wording or a wrong place, and of a Case under `## Deferred` only the slugs of its `defer` items; the agent writes no list of the decisions — the plan is the list (case 388). Three questions: which of these contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes — one that does is a finding (case 203.2); which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out (case 388). A later run in the session dispatches no `ask-guppi`: each Case built again is checked against the vault and its frame by its own `case-guppi` (case 561.1), and the findings that sent it back are confirmed once in the loop below (case 634.2). The body of a Case under `## Deferred` is not read: the session that takes the defer up judges it with its own pre-spec. A Case of this plan that changes a page another Case of this plan defers is still a finding (case 186.2).

Answer the findings with one report before any Case is sent back: for each `ask-guppi` run, the Case it judged and its list of what it did not check, with no claim that the whole Spec is checked (case 634.1); each finding numbered, with the fix you propose or, in one line, why it is already known; the findings that need no word of the person apart from those that need one; and each decision you need from the person as a question in the shape of `.claude/skills/grill-me/SKILL.md` (case 561.13). Then run the loop (case 561.2):

1. When the report asks the person no question, go on to step 2 at once. Otherwise send nothing to any `case-guppi` until the person has answered every question of the report, since an answer may change a fix. A question the person leaves unanswered you ask again, in its grill-me shape and under its number, and everything stays held (case 595.1).
2. Send each finding in a Case, with each answer of the person that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, all of them in one message.
3. Wait for every `case-guppi` you sent to answer, and pass on no answer of one `case-guppi` alone. An answer to `SendMessage` comes back as a notice that opens a turn of its own, and each turn ends with a reply: end each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer is still out, with one line that opens with a bold label ending in a colon — `**Waiting:**`, translated — and names the Cases that have answered and the Cases still out. Write nothing else in the chat while an answer is out: nothing of what an answer says, and no question; a round that came back waits for the list of step 4, and the label lets the reply pass the check of `rule-case-check` (case 581.1).
4. Show the person one list of what to answer: every round that came back, each question in its grill-me shape, translated as a round of `case-guppi` is, and numbered `<Case id>.Q<n>` — the id of its Case and its number in the round — so that each answer goes back to its `case-guppi`.
5. Send each answer to the `case-guppi` of its Case, all in one message, and go on from step 3 until every `case-guppi` you sent has answered with its Case.
6. Send each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and ask only whether each of its findings is closed: the message invites no new finding and no new judgment of a Case beyond those findings (case 638); wait for every answer as step 3 sets it. Then ask the person a question after the confirmation, in its grill-me shape: whether each finding not closed is fixed or left; a finding to be fixed goes to the `case-guppi` of its Case as in steps 2 to 5. No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched (case 634.2).
7. Show every Case built again in one reply, what step 6 found closed and not closed standing in your own text after the horizontal rule, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.

Inside this loop the rule of `vault/wiki/orchestration.md` that no Case is taken up before the current one is ratified does not hold: the Cases built again go out together and come back together. After their ratification do not call `/pre-spec` again: run the check above and fix what it prints; when it prints no finding, exit Plan Mode. The hook of `rule-prespec-onward` sends you on after the reply that acknowledges the ratification, and the hook of `rule-prespec-hook` refuses the exit while the check prints a finding (cases 561.3, 561.5).
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
- 2026-09-25 estimate estimate-prespec-matches-lines-and-items added · [[decision-case-399.2]]
- 2026-09-25 estimate estimate-prespec-checks-the-frontier added · [[decision-case-399.3]]
- 2026-09-25 estimate estimate-prespec-requires-a-task-line added · [[decision-case-399.4]]
- 2026-09-25 estimate estimate-prespec-checks-the-form-of-an-item added · [[decision-case-399.5]]
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 deferred · [[decision-case-413]]
- 2026-09-25 defer by decision-case-412 superseded · [[decision-case-414.1]]
- 2026-09-25 defer by decision-case-413 superseded · [[decision-case-415]]
- 2026-09-25 updated: a parent whose every sub-case is superseded is no finding of the ratified copy (case 417) · [[decision-case-417]]
- 2026-09-25 updated: the question before a create is case-guppi's (case 419.1) · [[decision-case-419.1]]
- 2026-09-25 updated: the closer kept, clean on [-] after the source deferred (case 421.3) · [[decision-case-421.3]]
- 2026-09-25 updated: the Render names the finding of a second item of one kind and slug under one Case (case 426) · [[decision-case-426]]
- 2026-09-25 updated: the Render: the read line of a renamed Estimate names its new slug (case 432) · [[decision-case-432]]
- 2026-09-26 updated: a key of an item outside the keys item_keys gives it is a finding (case 436.2) · [[decision-case-436.2]]
- 2026-09-26 deferred · [[decision-case-438]]
- 2026-09-26 defer by decision-case-438 superseded · [[decision-case-441.4]]
- 2026-09-26 updated: nothing is translated before the run; a finding in a Case goes to its case-guppi and a new ratification (case 441.4, supersedes 438) · [[decision-case-441.4]]
- 2026-09-27 updated: pre-spec compares the plan with no ratified copy; the Cyrillic finding reads Deferred too (case 445.4) · [[decision-case-445.4]]
- 2026-09-27 estimate estimate-prespec-checks-the-ratified-copy archived · cleanup
- 2026-09-27 updated: the Frontier check ties the box, the closer and the source both ways — defer after sprint, kept after backlog, defer case N after any other source (case 451.2) · [[decision-case-451.2]]
- 2026-09-27 updated: the finding on a backlog item decided without its page named and its defers superseded (case 467.1) · [[decision-case-467.1]]
- 2026-09-27 estimate estimate-prespec-requires-a-backlog-item-decided-on-its-page added · [[decision-case-467.1]]
- 2026-09-28 updated: pre-spec prints a note for a line of a Criterion replaced whole that the new Criterion does not carry (case 472.1) · [[decision-case-472.1]]
- 2026-09-28 updated: pre-spec prints a note for two then lines of sibling sub-cases that share most of their words (case 472.2) · [[decision-case-472.2]]
- 2026-09-28 updated: pre-spec counts every Estimate item that replaces a Criterion, written or lifted, by names_a_part (case 472.3) · [[decision-case-472.3]]
- 2026-09-28 updated: the finding reads guppi.toml and looks for a letter outside the script of documentation_lang, not for Cyrillic (case 476.3) · [[decision-case-476.3]]
- 2026-09-28 status: draft → built · cascade
- 2026-09-28 status: built → draft · cascade
- 2026-09-29 updated: pre-spec reports a code fence that a pair or a written section breaks, by fence_breaks of guppi/materialize.py (case 487.1) · [[decision-case-487.1]]
- 2026-09-29 estimate estimate-prespec-catches-a-broken-fence added · [[decision-case-487.1]]
- 2026-09-29 deferred · [[decision-case-503]]
- 2026-09-29 status: draft → built · cascade
- 2026-09-30 updated: an open line under ## Ask is no finding of pre-spec, as one under ## Work (case 531.12) · [[decision-case-531.12]]
- 2026-09-30 status: built → draft · cascade
- 2026-09-30 status: draft → built · cascade
- 2026-09-30 updated: pre-spec reports a replace pair whose new opens with spaces or tabs while its old does not (case 543.4) · [[decision-case-543.4]]
- 2026-09-30 estimate estimate-prespec-catches-an-indent-added-twice added · [[decision-case-543.4]]
- 2026-09-30 status: built → draft · cascade
- 2026-09-30 updated: the reason of the backlog check points to rule-case-protocol for when generate clears a defer (case 549) · [[decision-case-549]]
- 2026-09-30 status: draft → built · cascade
- 2026-10-01 defer by decision-case-503 superseded · [[decision-case-561.1]]
- 2026-10-01 updated: the skill gives the order - the check, the fixes, ask-guppi at the first run of the session only, one numbered report that sets apart the findings that need the person, the loop after the findings, no second call; what the check compares moves to the docstring of guppi/prespec.py; the defer of case 503 retired (cases 561.1, 561.2) · [[decision-case-561.1]]
- 2026-10-01 estimate estimate-prespec-gathers-the-answers-after-findings added · [[decision-case-561.2]]
- 2026-10-01 estimate estimate-prespec-catches-two-cases-on-one-target added · [[decision-case-561.4]]
- 2026-10-01 status: built → draft · cascade
- 2026-10-01 updated: step 2 of the loop after the findings: each waiting turn ends with one line under a bold label naming the Cases answered and still out, and nothing else is written (case 581.1) · [[decision-case-581.1]]
- 2026-10-02 status: draft → built · cascade
- 2026-10-02 updated: the loop after the findings sends nothing to a case-guppi until the person has answered every question of the report; the findings and the answers then go out together; the showing named in orchestration.md (case 595.1) · [[decision-case-595.1]]
- 2026-10-02 status: built → draft · cascade
- 2026-10-03 status: draft → built · cascade
- 2026-10-04 updated: the Frontier check takes defer case N from a defer Case of the conserved Spec that the plan's title line names (case 620.2) · [[decision-case-620.2]]
- 2026-10-04 status: built → draft · cascade
- 2026-10-04 status: draft → built · cascade
- 2026-10-04 updated: the first run of /pre-spec sends one ask-guppi per top-level Case of the plan or of the conserved Spec its title line names, all at once; the report names the Case each run judged and what it did not check, never the whole Spec as checked (case 634.1) · [[decision-case-634.1]]
- 2026-10-04 updated: the loop after the findings: the same ask-guppi runs confirm their own findings once before the Cases built again are shown; a finding not closed is fixed or left by the person's answer to a question after the confirmation; the result stands after the horizontal rule; no second confirmation (case 634.2) · [[decision-case-634.2]]
- 2026-10-04 estimate estimate-prespec-confirms-the-findings-once added · [[decision-case-634.2]]
- 2026-10-04 status: built → draft · cascade
- 2026-10-05 updated: the confirmation message of step 6 asks only whether each finding is closed and invites no new finding (case 638) · [[decision-case-638]]
