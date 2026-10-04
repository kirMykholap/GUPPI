---
type: estimate
kind: QA
status: passed
target: "[[rule-ratification]]"
purpose: The written shape of a ledger line and of its marks, as the agent writes them
method: "by hand: the ledger and the preview of a session where a lesson and the Case that closes its cause stand together, and of a Case that takes up a decision with more than one Case in its deferred_by"
checked: 2026-10-04
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Criterion

When:
The agent writes the ledger lines of a session — the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists — with `vault/wiki/ratification.md` rendered from `rule-ratification`.

Then:
A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
**＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
**＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
**＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
**＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
**＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
**－** A lesson whose fix is ratified in another session gets no mark.

## Result

2026-10-04, at the /hi of session 1934, by hand: archive/migration/2026-10-03/0317/raw/ledger.md: the decision lines of 613.2 (L13-L14) stand first and carry no {addresses}, and the lesson line L54, lesson-estimates-reading-tied-to-a-one-off-moment, written in the LEDGER block of Retro, carries {addressed_by:case 613.2}, the sub-case, one mark for the pair; raw/2026-10-04/1439/ledger.md L36: `decision[case 629.2][delete][rule-case-rebuild-cost]{ref:rule-case-rebuild-cost}{supersedes:case 566}{supersedes:case 570}`, one block per Case of the page's deferred_by ["decision-case-566", "decision-case-570"], side by side, and the same line in the ratification fence of the showing at 18:58:11 (transcript 8b8ce20f); create lines carry {tags} (L17, L18, L21, L33, L37); not exercised: {addresses} on a decision line after its lesson, a lesson whose fix is ratified in another session

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L38
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-20 updated: the Criterion replaced whole — the table and the ledger paragraph are one document since 273.1, two documents read, not three (case 277.6) · [[decision-case-277.6]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L3
- 2026-09-21 updated: the Criterion replaced whole — the mark {addresses:<lesson slug>} beside {source} and {supersedes} (case 284.2) · [[decision-case-284.2]]
- 2026-09-21 status: pending → passed · raw/2026-09-21/0019/ledger.md#L1
- 2026-09-22 updated: the Criterion reads case-schema.md alone; the second copy in index.md is gone (case 318) · [[decision-case-318]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/0034/ledger.md#L61
- 2026-09-23 updated: the Criterion replaced whole — the shape of a decision line and the two marks, by the order of the lines (case 379) · [[decision-case-379]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1228/ledger.md#L39
- 2026-09-25 updated: the Criterion replaced whole — one {supersedes:case N} block per Case, never a list; a deferred decision taken up names every Case of its deferred_by (case 429) · [[decision-case-429]]
- 2026-09-29 updated: the Criterion replaced whole — for a Case with sub-cases the mark names the sub-case (case 497.4) · [[decision-case-497.4]]
- 2026-10-02 renamed from `estimate-case-protocol-ledger-line-form` · [[decision-case-595.16]]
- 2026-10-02 updated: moved to rule-ratification; the Criterion replaced whole - the form as ratification.md holds it (case 595.16) · [[decision-case-595.16]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/1934/ledger.md#L3
