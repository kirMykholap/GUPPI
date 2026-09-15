---
type: decision
case: "177"
status: current
update: ["[[rule-materialize]]"]
supersedes: ["[[decision-case-130.2]]"]
origin: raw/2026-09-15/1809/ledger.md#case-177
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

`estimate-materialize-assembles` holds one block per contract change of `rule-materialize`. Block 130.2 (session N) signed two things: the `superseded_by` mark lands on the entries of Case N "decision kinds", and lands in the yaml of any session under `raw/`, a foreign yaml written with that mark only. Case 175 of this session dropped the filter by kind and restated the foreign-yaml rule in its own `then`. A block leaves the page only by `{supersedes:case N}` on a decision line (case 72.1), and the line of 175 is written without one. In `rule-materialize` the sentence "A line with `{supersedes:case N}` marks the entries of case N `superseded_by`" stands twice — 175 edits one, the other stays in the description of the yaml.

## Problem

After the librarian's run the Estimate would carry block 130.2 with the filter by kind and block 175 without it — two signed criteria that contradict each other; the reading of 175 cannot pass against 130.2. A line with `{supersedes:case 130.2}` is needed, and it must carry a decision of its own.

## Given

`estimate-materialize-assembles`, block 130.2: "The entries of Case N (decision kinds) are marked `superseded_by` in the yaml of the unit that holds them — its own or any other under `raw/` — and in the `decisions` list of that unit; a foreign yaml is written with that mark only."
**＋** Case 175, `then`: every entry with `case: N` — the lines and the derived ones; a foreign yaml by the same rule; block 175 added, `pending`.
**＋** `rule-materialize`, How it works, second occurrence: "A line with `{supersedes:case N}` marks the entries of case N `superseded_by`." — untouched by 175; `replace` matches whitespace-insensitive, exactly once — the sentence ending in a full stop is one, the sentence 175 edits (line 50) differs in its words.
**＋** The entries of 130.2 lie in the archived yaml of `2026-09-14`; `mark_superseded_elsewhere` walks `raw/` only — "a case no yaml holds changes nothing"; `decision-case-130.2` becomes `superseded` and is archived by the cascade (case 104.1).
**＋** Precedent: Case 171 (session R) — `contract: same` with `{supersedes:case 124.2}`, found at pre-task.
**－** No contract change: the contract is 175's; no `### case 177` block.

## History

- 2026-09-15 created · raw/2026-09-15/1809/ledger.md#case-177
