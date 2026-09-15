<!-- approved 20:23:04 · session d7d2276d -->

# Spec — 2026-09-15, session S (hi 18:09)

## Readings carried from `raw/2026-09-15/1448/spec.md` (F1, work)

Taken in Plan Mode: `estimate-case-protocol-loaded` (167) and `estimate-cleanup-moves` (166.4), both `passed`, their ledger lines written; their boxes in `1448/spec.md` are ticked in Work Mode. Left for Work Mode and Retro, each a `- estimate[...]` line the moment it is measured:

- [x] tick the boxes of 167 and 166.4 in `raw/2026-09-15/1448/spec.md`
- [x] read `estimate-generate-writes` (blocks 166.2, 166.3, 172), one line for the page, `passed` in Plan Mode: the agent's half (377 green; the Insight of R without `## Children`; no `insight section derived` line of 2026-09-15 in `log.md`; 0 derived headings over the four folders) and the owner's half (in Obsidian the backlinks of `rule-documentation` and of `insight-retro-typed-command-is-never-a-tool-call` in place, `unresolved` empty); its boxes in `1448/spec.md` (lines 138, 165, 463) are ticked in Work Mode with those of 167 and 166.4
- [x] read `estimate-hook-registry-rendered` (169.2), `estimate-retro-loads` (169.3): the first typed `/retro` of this session — the gate's check, the mark `retro` in the event log from the `UserPromptSubmit` entry, then the agent's own call with a second mark; `settings.json` already carries both commands, `hi` at 18:09:02 — both `passed` at Retro, marks 20:31:22 and 21:12:53
- [ ] read `estimate-retro-commit-gates` (169.1): left `pending` by the owner at Retro — the live refusal of a typed `/retro` on a Spec item without its line did not happen this session; the next session types `/retro` before the plan is written, to see what the gate says
- [ ] `estimate-brief-written` (168): the brief of this session's librarian run, "Readings due" as its second section — read at the start of the next session, a handoff note

## Case 173 — `insight-retro-typed-command-is-never-a-tool-call`

> **context:**
> `insight-retro-typed-command-is-never-a-tool-call` is an Insight, `open`, severity 2, with two children: the lessons of sessions O and Q. Its pattern: a slash command typed by the person is expanded by the client into the prompt and is never a Skill tool call; a hook on the Skill tool sees only the agent's own calls, and a cure aimed at the skill's settings (case 150) changed the agent's path and left the typed one as it was. Its Proposal: treat the two paths as two — the agent's call gated on `PreToolUse Skill`, the typed command on `UserPromptSubmit`; a `then` on a slash command names which path it covers, and its reading takes both. The librarian created the Insight in the run of session R, after 169.1–169.3 had ratified most of the Proposal in that session: `guppi gate` is the second command on `UserPromptSubmit` and reads a typed `/pre-task`, `/retro` or `/handoff`; `rule-retro` names both paths; the reading of `estimate-retro-loads` (169.3) takes both — typed and called, two `retro` marks in the event log.

> **problem:**
> The Insight stands first in the Deferred list of the brief and must end in this Plan Mode as `actioned`, a rejection or a `defer`. The mechanics of the Proposal exist since 169.1–169.3, but one sentence of it is ratified nowhere: the rule that a `when` on a slash command names its path and the reading of a `then` covering both takes both. Without it the next Case on `/hi` or `/ask` can again write a `then` that assumes both paths go through the Skill tool — the root of the lessons of O and Q.

> **given:**
> `insight-retro-typed-command-is-never-a-tool-call`: `status: open`, `severity: 2`, no `addressed_by`, no `deferred_by`; an `update` with a `ref`, the page read, no vault query needed.
> **＋** `rule-retro-commit` (169.1): the gate on `UserPromptSubmit` reads the payload's `prompt` for `/pre-task`, `/retro`, `/handoff`, the same two checks and the same mark; `rule-hook-registry` (169.2): `guppi gate` is the second command on `UserPromptSubmit`; `rule-retro` (169.3): both paths behind the gate, the reading of `estimate-retro-loads` takes both.
> **＋** The readings of 169.1–169.3 stand `pending` until the first typed `/retro` of this session; `actioned` is not terminal — a new lesson with the same root cause reopens the Insight (insights schema, §8), so a failed reading reopens it by itself.
> **＋** `case-schema.md` is a Rule-class file: an `update` with `file` and `change`, applied by hand in Work Mode (case 166.1); ledger line `[case-schema]{ref:case-schema}` (cases 92, 123, 149.2). The section "`when` and `then` are the criterion" says nothing today about the paths of a slash command.
> **＋** `generate`: an `update` of an Insight with `status: actioned` goes as any update; the cascade archives the `clustered` children and recounts `severity` (case 168 went the same way).
> **－** No new Rule page: the sentence has no hook, check or render — it is a rule for writing a Case, and its place is `case-schema.md`.

> **when:**
> The person ratifies this Case; the librarian runs `generate` and `cleanup`; in Work Mode the agent edits `case-schema.md` by hand.
> **＋** Later: the agent writes the `when` and `then` of a Case on a slash command, with `case-schema.md` loaded through `CLAUDE.md`.

> **then:**
> The Insight stands `actioned`, `addressed_by: decision-case-173`; both child lessons are `archived` and moved by `cleanup` to `vault/archive/migration/2026-09-15/1809/lessons/`; `severity` recounted by the cascade.
> **＋** `case-schema.md`, section "`when` and `then` are the criterion", holds one sentence: a `when` on a slash command names the path it covers — the person's typed command on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`, or both; the reading of a `then` that covers both takes both (case 173).
> **＋** A new lesson with the same root cause reopens the Insight — as today, unchanged.
> **－** `rule-retro`, `rule-retro-commit`, `rule-hook-registry` do not change: their contracts stand since 169.1–169.3, their readings are F1.

```then
update:
  - slug: insight-retro-typed-command-is-never-a-tool-call
    set: {status: actioned, addressed_by: decision-case-173}
    change: "actioned: the two paths of a slash command are two since 169.1–169.3, and case-schema.md now asks a when on a slash command to name its path and a then covering both to be read on both (case 173)"
  - file: vault/wiki/case-schema.md
    change: "the section 'when and then are the criterion' gains one sentence: a when on a slash command names the path it covers — the person's typed command on UserPromptSubmit, the agent's call on PreToolUse Skill, or both; the reading of a then that covers both takes both (case 173)"
```

```tasks
- [ ] `insight-retro-typed-command-is-never-a-tool-call` `update`: `set: {status: actioned, addressed_by: decision-case-173}`; the cascade archives the two children
- [x] `vault/wiki/case-schema.md` `update`, `file` + `change`: one sentence in the section "`when` and `then` are the criterion", by hand in Work Mode; `CLAUDE.md` untouched — the section arrives through `@vault/wiki/case-schema.md`
- [x] no Estimate: an Insight and a Rule-class file carry none
```

## Case 174 — F17: the stale texts after 147.6, 166.2, 166.4 and 169.1

> **context:**
> `estimate-generate-writes` and `estimate-cleanup-moves` are the Estimate pages of `rule-page-generation` and `rule-cleanup`. Their Criterion is a head text — the criterion signed at creation (cases 32, 33) and edited directly in case 57 — and `### case N` blocks, one per contract change. A `supersedes` removes a block only; nobody touches the head. `rule-ledger-write` describes the second refusal of `guppi gate` — a Spec item without its ledger line — and quotes its text whole. Since 169.1 the gate has two texts: for the agent "end this reply in text with the LEDGER block, then call /<skill> in the next reply", for the person "Ask the agent to end its reply with the LEDGER block, then type /<skill> again".

> **problem:**
> Three texts contradict ratified contracts. The head of `estimate-generate-writes` asks for `## Children` and `## Estimates`, which 166.2 removed. The head of `estimate-cleanup-moves` asks for "their sections" when a slug leaves (removed by 166.4) and "the four category indexes are rewritten" (removed by 147.6). `rule-ledger-write` quotes one refusal text where the gate has two. The readings of 166.2 and 166.4 stand in F1 and read the whole page; the reader meets a head that says one thing and a block that says the opposite. This is the pattern of `insight-workflow-contract-change-leaves-its-derived-text-stale` (`actioned`), left in the handoff of session R as F17.

> **given:**
> `estimate-generate-writes`, head Criterion: "the parent's children and ## Children in order, the target's estimates and ## Estimates" — once on the page; block 166.2 says no section is derived from a ref field.
> **＋** `estimate-cleanup-moves`, head Criterion: "its slug leaves the children lists of live pages and the estimates lists of entities and rules, and their sections, with a History line there" and "the four category indexes are rewritten without the moved page, and an archived Estimate leaves no line anywhere" — once each; block 147.6: no index is written; block 166.4: the field only, no section rebuilt.
> **＋** `rule-ledger-write`, How it works: one quoted refusal text — the advice to the agent; `guppi/gate.py` prints `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B).` and then one of two advices by `typed(payload)`.
> **＋** `generate` applies `replace` on a page of any category: `old` matched whitespace-insensitive over every section but History, exactly one hit (case 57 edited `estimate-cleanup-moves` the same way).
> **＋** Both Estimates are `pending` already (blocks 166.2, 166.3, 172 and 166.4); their reading is F1, over the whole page.
> **－** No contract changes: an Estimate page has none, `rule-ledger-write` is `contract: same`; no `### case 174` block appears.

> **when:**
> The librarian runs `generate` over the yaml of this session.
> **＋** Later: the reading of `estimate-generate-writes` or `estimate-cleanup-moves` (F1) reads the head Criterion; someone reads `rule-ledger-write` to understand a refusal of the gate.

> **then:**
> The head of `estimate-generate-writes` says: three pages pass their `schema.yaml`, the parent's `children` in order and the target's `estimates`, and no section is derived from either.
> **＋** The head of `estimate-cleanup-moves` says: the slug leaves the `children` lists of live pages and the `estimates` lists of entities and rules — the field only, no section rebuilt; no index file is written.
> **＋** `rule-ledger-write` quotes the refusal and both advices: to the agent — the text before a tool call is never kept, end the reply in text with the LEDGER block and call the skill in the next; to the person — ask the agent to end its reply with the LEDGER block and type the command again.
> **＋** Every replacement is marked `(case 174)`; the History of the three pages gains a line.
> **－** The `### case N` blocks of the three pages do not change; no status changes.

```then
update:
  - slug: estimate-generate-writes
    replace:
      - old: "the parent's children and ## Children in order, the target's estimates and ## Estimates;"
        new: "the parent's children in order and the target's estimates, no section derived from either (case 174);"
    change: "head Criterion: no ## Children, no ## Estimates — the text of 166.2 (case 174)"
  - slug: estimate-cleanup-moves
    replace:
      - old: "its slug leaves the children lists of live pages and the estimates lists of entities and rules, and their sections, with a History line there;"
        new: "its slug leaves the children lists of live pages and the estimates lists of entities and rules, the field only and no section rebuilt, with a History line there (case 174);"
      - old: "the four category indexes are rewritten without the moved page, and an archived Estimate leaves no line anywhere;"
        new: "no index file is written (case 174);"
    change: "head Criterion: the field only, no section rebuilt (166.4); no index file (147.6) (case 174)"
  - slug: rule-ledger-write
    contract: same
    replace:
      - old: "an item with no decision line of its Case refuses the call with exit 2 — `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B). The text before a tool call is never kept: end this reply in text with the LEDGER block, then call /<skill> in the next reply.` — and every item with its line, or no source found, passes silently (case 122)."
        new: "an item with no decision line of its Case refuses the call with exit 2 — `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B).` followed by the advice of the path: to the agent `The text before a tool call is never kept: end this reply in text with the LEDGER block, then call /<skill> in the next reply.`, to the person `Ask the agent to end its reply with the LEDGER block, then type /<skill> again.` (case 174) — and every item with its line, or no source found, passes silently (case 122)."
    change: "the refusal on an unwritten ledger line quoted with both advices, the agent's and the person's (case 174)"
```

```tasks
- [ ] `estimate-generate-writes` `update`: one `replace`, `change`
- [ ] `estimate-cleanup-moves` `update`: two `replace`, `change`
- [ ] `rule-ledger-write` `update`, `contract: same`: one `replace`, `change`
- [x] no new reading: the pages are `pending` already, F1 reads them with the corrected head
```

## Case 175 — `rule-materialize`: a `supersedes` marks every entry of the earlier Case

> **context:**
> `guppi materialize` builds the session's `materialize.yaml` from the ledger and the Spec: one entry per ledger line, the word of the second bracket as `kind`, plus derived entries with no line of their own — the Estimate's `create` from `method`, its `update` with a block from `contract: changed`, the removal of a `### case N` block from `{supersedes:case N}` under the internal word `remove_criterion`. A line with `{supersedes:case N}` marks the entries of Case N `superseded_by` — in this yaml or in the yaml of another session (case 130.2); `generate` does not apply a marked entry, it only writes the Decision page of N as `superseded`. `mark_superseded` sets the mark by the filter "an entry of Case N whose `kind` is one of the four decision kinds". In session R 166.2 superseded 164: two entries of 164 were marked, the third — the removal of block 124.2 — was not; `generate` applied it in the name of the superseded 164.

> **problem:**
> A superseded Case keeps acting through one of its entries. The filter by kind is superfluous: when Case N is superseded, everything it yielded is superseded. `estimate` and `lesson` entries carry no Case number, so a mark by the number alone catches nothing else.

> **given:**
> `guppi/materialize.py`, `mark_superseded`: marks an entry when `entry.case == N` and `entry.kind in DECISION_KINDS`; `mark_superseded_elsewhere` calls the same for a foreign yaml.
> **＋** `derived_entries` gives a derived entry the line's `case` and `derived: true`; the block-removal entry is `kind: remove_criterion`, `case_removed: N`, no `slug`.
> **＋** `estimate_entry` and `lesson_entry` write an entry without a `case` key.
> **＋** `guppi generate`: an entry with `superseded_by` is not applied (case 151); a `remove_criterion` with no block prints `no Estimate holds a block` and does not fail.
> **＋** `rule-materialize` is `built`, `estimates: [estimate-materialize-assembles, estimate-materialize-walks-dates]`, both `passed`, the first named by `estimate_slug` (a fact corrected at pre-task: the Case said one Estimate); `tests/test_materialize.py`: `test_a_supersedes_chain_marks_the_earlier_entry`, `test_a_supersedes_marks_the_earlier_entry_in_another_units_yaml`, the `seed` fixture.
> **－** `1448/materialize.yaml` and the History of `estimate-generate-writes` are not rewritten: block 124.2 is gone, which 171 wanted; the History says what the script did.

> **when:**
> `guppi materialize` reads a line with `{supersedes:case N}`, and the entries of Case N lie in this yaml or in the yaml of another session under `raw/`.

> **then:**
> Every entry with `case: N` gets `superseded_by` — the lines of Case N and everything derived from them: the Estimate, the criterion block, the block removal; the `decisions` record of Case N as today.
> **＋** `generate` applies none of them; the block a superseded Case meant to remove stands until a live Case removes it.
> **＋** A foreign yaml is marked by the same rule.
> **－** An entry without `case` — `estimate`, `lesson` — gets no mark.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-assembles
    replace:
      - old: "a later `supersedes` adds `superseded_by` to the entries of the earlier Case in whichever unit's yaml holds them — this one or any other under `raw/` — and to that unit's `decisions` list, and changes nothing else;"
        new: "a later `supersedes` adds `superseded_by` to every entry of the earlier Case — every entry carrying its `case`, the lines' own and the derived ones, the block removal included, whatever its `kind` (case 175) — in whichever unit's yaml holds them — this one or any other under `raw/` — and to that unit's `decisions` list, and changes nothing else;"
    change: "a supersedes marks every entry of the earlier Case by its case number, the derived block removal included; the filter by kind is gone (case 175)"
```

```tasks
- [ ] `rule-materialize` `update`, `contract: changed`, the `replace` above; `estimate-materialize-assembles` block 175, `pending`
- [x] `guppi/materialize.py`: `mark_superseded` without the filter by `kind`; docstring
- [x] `tests/test_materialize.py`: a Case with `supersedes`, superseded later in the same yaml — its block-removal entry carries `superseded_by`; the same in a foreign yaml
- [ ] read `estimate-materialize-assembles` (block 175): the tests green; live — the first `supersedes` of a Case whose own line carried a `supersedes`: every entry of it marked in the yaml, `generate` prints no line for them
```

## Case 177 — `rule-materialize`: block 130.2 leaves the Criterion

> **context:**
> `estimate-materialize-assembles` holds one block per contract change of `rule-materialize`. Block 130.2 (session N) signed two things: the `superseded_by` mark lands on the entries of Case N "decision kinds", and lands in the yaml of any session under `raw/`, a foreign yaml written with that mark only. Case 175 of this session dropped the filter by kind and restated the foreign-yaml rule in its own `then`. A block leaves the page only by `{supersedes:case N}` on a decision line (case 72.1), and the line of 175 is written without one. In `rule-materialize` the sentence "A line with `{supersedes:case N}` marks the entries of case N `superseded_by`" stands twice — 175 edits one, the other stays in the description of the yaml.

> **problem:**
> After the librarian's run the Estimate would carry block 130.2 with the filter by kind and block 175 without it — two signed criteria that contradict each other; the reading of 175 cannot pass against 130.2. A line with `{supersedes:case 130.2}` is needed, and it must carry a decision of its own.

> **given:**
> `estimate-materialize-assembles`, block 130.2: "The entries of Case N (decision kinds) are marked `superseded_by` in the yaml of the unit that holds them — its own or any other under `raw/` — and in the `decisions` list of that unit; a foreign yaml is written with that mark only."
> **＋** Case 175, `then`: every entry with `case: N` — the lines and the derived ones; a foreign yaml by the same rule; block 175 added, `pending`.
> **＋** `rule-materialize`, How it works, second occurrence: "A line with `{supersedes:case N}` marks the entries of case N `superseded_by`." — untouched by 175; `replace` matches whitespace-insensitive, exactly once — the sentence ending in a full stop is one, the sentence 175 edits (line 50) differs in its words.
> **＋** The entries of 130.2 lie in the archived yaml of `2026-09-14`; `mark_superseded_elsewhere` walks `raw/` only — "a case no yaml holds changes nothing"; `decision-case-130.2` becomes `superseded` and is archived by the cascade (case 104.1).
> **＋** Precedent: Case 171 (session R) — `contract: same` with `{supersedes:case 124.2}`, found at pre-task.
> **－** No contract change: the contract is 175's; no `### case 177` block.

> **when:**
> The librarian runs `materialize` and `generate` over the ledger of this session.
> **＋** Later: the reading of `estimate-materialize-assembles` (block 175).

> **then:**
> Block `### case 130.2` is removed from `estimate-materialize-assembles`, History `criterion: case 130.2 removed`; block 175 stands alone with its rule, `pending`.
> **＋** `rule-materialize`, the description of the yaml: "A line with `{supersedes:case N}` marks every entry carrying `case: N` `superseded_by`, whatever its `kind` (case 175, supersedes 130.2)."
> **＋** `decision-case-130.2` is `superseded`, archived; `rule-materialize` carries no `deferred_by` from it — it never did.
> **－** Code and tests do not change: that is the work of 175.

```then
update:
  - slug: rule-materialize
    contract: same
    replace:
      - old: "A line with `{supersedes:case N}` marks the entries of case N `superseded_by`."
        new: "A line with `{supersedes:case N}` marks every entry carrying `case: N` `superseded_by`, whatever its `kind` (case 175, supersedes 130.2)."
    change: "the second statement of the supersedes mark says every entry by case number; block 130.2 with its filter by kind leaves the Estimate (case 177, supersedes 130.2)"
```

```tasks
- [ ] `rule-materialize` `update`, `contract: same`, the one `replace` above — the second occurrence of the sentence; `{supersedes:case 130.2}` removes block 130.2
- [x] no reading of its own: block 175 is read by the tasks of 175, with no block 130.2 beside it
```

## Deferred

## Case 176 — Slice 3b: Work Mode, deferred again

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since Case 29, `draft`, `deferred_by: [[decision-case-170]]`, without `kind`, `estimates` or `tags` — 6 `schema` and 2 `orphan` findings. Slice 3b is the Spec as tasks with code, the ticked boxes, the readings taken in Work Mode, what a subagent may do and the fork that comes back as a Case; `sprint.md` says "3b before 4"; the Plan Mode of a session of its own.

> **problem:**
> The owner opened session S on the Deferred list and the Flags of the brief — Cases 173–175 and the readings of F1 — and left Slice 3b for a session of its own. The two pages stay placeholders one more session; the postponement count goes to 14.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: "Slice 3b — Work Mode: the Spec as tasks with code, the ticked boxes in spec.md, the readings taken in Work Mode; the Plan Mode of a session of its own, before Slice 4"
  - slug: rule-subagent-guppi
    type: rule
    purpose: "Slice 3b — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; with rule-work-mode"
```

F6 (`git pull` without an upstream, owner's decision 11.1), F7 (`gh` not logged in, 11.2) and F8 (lint 70: the decision pages of Cases 1–28, the two placeholders) are page-less tasks of Slice 5 and stand in `sprint.md` already; no defer Case.

## Retro

## Case 178 — `rule-plan-mode`: who judges the blocks of a Criterion

> **context:**
> The Criterion of an Estimate page is a head text plus one `### case N` block per contract change; the script appends the blocks one after another and removes one only by `{supersedes:case N}` on a decision line. No judgment says whether a new block contradicts an old one: a script writes. The one check that catches a contradiction is pre-task through `ask-guppi`, at the exit of Plan Mode; in sessions R and S it caught 124.2 (Case 171) and 130.2 (Case 177), and both times a Case of its own was added to carry the `supersedes`.

> **problem:**
> Old criteria pile up on the page even when they are no longer needed, and the removal is decided after the signature, not before. Who reads the blocks and names the removal: the Case at its forming — `given` carries the blocks of the Estimate and the `supersedes` of the contradicting one, the plan file checked by `pretask --check` before the ratification question — or the librarian at `generate`, by what it received. A question of the next Plan Mode.

```then
defer:
  - slug: rule-plan-mode
    type: rule
    purpose: "decide who reads the blocks of an Estimate's Criterion and names the block a contract change supersedes — the Case at its forming (given carries the blocks, pretask --check before the ratification question) or the librarian at generate; today only pre-task catches the contradiction, after the signature (cases 171, 177)"
```

## Case 179 — `rule-case-protocol`: six sections in How it works

> **context:**
> `rule-case-protocol` is the rule whose Render enters `CLAUDE.md`. The Render says "eight sections" (case 163); the How it works of the same page says "The six Case sections are not repeated here: they arrive through `case-schema.md`".

> **problem:**
> The text of the page went stale after a contract change — the pattern of `insight-workflow-contract-change-leaves-its-derived-text-stale`. One `replace`; found at the pre-task of session S by `ask-guppi`, not raised as a Case there.

```then
defer:
  - slug: rule-case-protocol
    type: rule
    purpose: "one replace in How it works: 'The six Case sections' → eight, the count of case 163; found by ask-guppi at the pre-task of session S"
```
