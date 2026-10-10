---
type: decision
case: "497.2"
status: archived
update: ["[[estimate-ledger-write-lifts]]"]
origin: raw/2026-09-29/0137/ledger.md#case-497.2
sprint: migration
created: 2026-09-29
tags: [session, hooks, harness, ledger]
---

## Context

A lesson line written after the Case that fixed its cause carries `{addressed_by:case N}`. The librarian's run (`materialize`) links the lesson to the decision only when a decision line of Case N stands before the lesson line in the session's ledger. Nothing checks the pointer when the line is written. A Case with sub-cases has no decision line of its own: its lines are N.1, N.2 and so on, and each has its own Decision page. So a pointer to the parent number never resolves. In session 2229, ledger line 52 pointed at `case 487`, whose lines are 487.1 to 487.4. The lesson `lesson-prespec-judged-a-pair-by-its-anchor-alone` went out without its link, and only the next morning's brief showed it. This is the pattern of `insight-ledger-line-written-unchecked`: a line written verbatim and read back only by `materialize`.
The person chose three things. The ledger hook refuses such a line at once, the way it already refuses a lesson slug without its prefix (case 460.5). The rule text of `rule-case-protocol` says which number to name. The lesson of line 52 stays as it is. Nothing reads the mark once synthesis has run, the lesson joined no Insight, and the handoff of 2229 names the fix. Its `incomplete: [addressed_by]` stays in the yaml of 2229. Case 442 deferred a neighbour on `rule-ledger-write`: a lesson line with no mark at all, although a Case of the session closed its cause. The person chose to leave it deferred. This Case catches a mark that names the wrong Case, not a missing mark.
The vault's answer: the only `create` is an Estimate with a `ref`, so no vault query ran. The ledgers under `vault/raw` hold exactly one `{addressed_by:...}` mark and no `{addresses:...}` mark. The first is the line of 2229. The frame:
- The hook and `materialize` judge the mark by one function in `guppi/materialize.py`, by `CLAUDE.md` ("one judgment, one implementation"). The function reads the ledger lines in order, and one test runs both callers on the same lines. The order matters. `materialize` links a lesson only to a decision line that stands before it, so the hook asks the same thing. A decision line later in the same `LEDGER` block does not count.
- `materialize` keeps its behaviour: `rule-materialize` and the Criterion of `estimate-materialize-carries-addresses` ("no decision line of Case N earlier in the unit") stay true and are not touched.
- `estimate-ledger-write-lifts` lists each refusal of the hook in its `－` lines. It gains one line, so its Criterion is replaced whole (497.2).
- `estimate-ledger-write-refuses-a-lesson-without-its-prefix` says that a lesson line with the prefix "is written as before". This Case would make that false for a line with a bad mark. So its Criterion is replaced whole (497.3), and that one sentence is not carried: it becomes "is not refused for its prefix", and the mark is judged apart. The prefix is judged first. A line refused for its prefix is not judged for its mark, so it gets one stderr line, not two.
- `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` speaks only of `estimate[...]` lines and stands.
- `estimate-ratification-ledger-line-form` promises the form of the mark. It gains the sub-case rule, and its Criterion is replaced whole (497.4). `estimate-case-protocol-loaded` is not touched by a change of a Render (case 378.5).
- The other `Stop` hooks, `guppi ratified`, `guppi casecheck` and `guppi context`, do not read lesson lines.
- The prefix refusal refuses a line at every `Stop`, since its slug never changes. The mark refusal depends on the ledger. A line refused from an earlier text is judged again at every `Stop` until it stands in the ledger. It is written at the first `Stop` where a decision line of its Case stands before it. The hook speaks only for the line in the reply just finished. A line whose Case never gets a decision line stays unwritten at the end of the session, and Retro sees it.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` stays true, and the Case does not update it. The hook runs from the working tree at once, and the text of 497.4 lands at the render. But that Criterion asks for the old form only where the reader refuses, in between, what the old text asks for, and the refused line is lost.
  - Neither holds here. The old text says to name "that Case", and a mark with no decision line of its Case did not link under the old text either. A line that names a Case without sub-cases passes, as before.
  - A refused line is not lost. In the reply just finished, the hook exits 2 and the agent writes the line again. From an earlier text, the line is judged again until its decision line stands.
- Not done: the hook does not judge the `{addresses:<lesson slug>}` mark of a decision line, it does not catch a missing mark (case 442, still deferred), and the lesson of line 52 is not repaired.
- The new Estimate and the three set `pending` are read in a later session (case 428.1).

This Case is built again after pre-spec found these faults: the hook ignored the order of lines, a later `Stop` was said to skip a line it in fact writes, a line with both faults got two stderr lines, the Estimate of old forms was not named, and defer 442 was not named. The answer check noted that some `then` lines of 497.2, 497.3 and 497.4 share words with 497.1 and with each other. This is expected. All four speak of the same hook and the same mark. 497.1 is modelled on the prefix refusal that 497.3 keeps. 497.2 and 497.4 keep the other lines of their old Criteria word for word.

## Problem

A lesson line can point to a Case that has no decision line before it in the session, such as the parent of sub-cases. The mark then never links, and nobody sees it until the librarian's run of the next day.

## Given

`estimate-ledger-write-lifts` — the promise of the hook; its Criterion replaced whole
**＋** `guppi/ledger.py` — the hook it reads
**＋** `guppi/gate.py` — the gate it names
**＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the session's ledger the hook writes
**＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — a refusal it names
**＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — a refusal it names
**＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the refusal it gains

## History

- 2026-09-29 created · raw/2026-09-29/0137/ledger.md#case-497.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
