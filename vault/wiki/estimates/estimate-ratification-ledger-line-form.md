---
type: estimate
kind: QA
status: passed
target: "[[rule-ratification]]"
purpose: The written shape of a ledger line and of its marks, as the agent writes them
method: "by hand, at Retro: the decision and lesson lines that carry an addresses or addressed_by mark in vault/archive/plugin/2026-10-14/0232/raw/ledger.md, vault/archive/plugin/2026-10-14/1536/raw/ledger.md, vault/archive/plugin/2026-10-16/2104/raw/ledger.md, vault/archive/plugin/2026-10-17/2307/raw/ledger.md and vault/archive/plugin/2026-10-29/2341/raw/ledger.md, and the line in vault/archive/migration/2026-10-04/1439/raw/ledger.md that takes up a page with two Cases in its deferred_by, each with its preview in the transcript of its session under ~/.claude/projects/, read against the Criterion, all recorded in one estimate line (the take-up line is that of case 629.2)"
checked: 2026-11-01
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

2026-11-01, Retro of session 1721: the marked lines of the five archived plugin ledgers the method names — 0232 L15 lesson {addressed_by:case 812.1} after the decision lines of 812.1 (L7-9), the sub-case; 1536 L5 decision {addresses:lesson-ship-example-file-exempt-whole-left-case-pointers} after its lesson (L4); 2104 L51 lesson {addressed_by:case 872.1} after the lines of 872.1 (L25-27); 2307 L35 and L41 decision lines of 884 with one {addresses:...} per lesson after each lesson line (L26, L40), {supersedes:case 876} one block; 2341 L40 lesson {addressed_by:case 914}, a Case with no sub-cases, after L9 — and 1439 L36 of case 629.2 with {supersedes:case 566}{supersedes:case 570} side by side; each mark stands in the LEDGER block of its session's transcript (cfcb07e8, f5b00c55, 563a8403, 392fc00e, 958b7a22, 8b8ce20f) and each decision mark also in the ratification preview there

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
- 2026-10-15 updated: the Criterion replaced whole — a lesson line declares a new tag by a newtag block (case 827.3) · [[decision-case-827.3]]
- 2026-10-31 updated: the method reads the marks and the take-up line in archived ledgers and waits only for a lesson line that declares a new tag, the Criterion written back unchanged · [[decision-case-961.5]]
- 2026-11-01 updated: the Criterion replaced whole — the new-tag block of a lesson line is left to the check of the ledger hook; the method reads the archived ledgers and waits for no new tag · [[decision-case-988]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/1721/ledger.md#L33
