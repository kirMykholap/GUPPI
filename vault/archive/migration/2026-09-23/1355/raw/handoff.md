# Handoff — 2026-09-23, the model of the Criterion

## Notes from memory

- The session began on C6 (`rule-retro`) and C5, and turned on C4 into a revision of the model: the person read the operands `＋`/`－` as Gherkin "and"/"but", saw that `given` served two readers — the history of the Case and the contract of the Estimate — and chose: `given` is the frame of the Case (the list of what it touches), `context` is prose, an Estimate is `When:` and `Then:` only. Case 378 records it.
- The person wants the one pass over the 104 Estimates as a session of its own: Slice 3g on the sprint page (Case 381). The person also asked for the check "when/then name only what given names" to be hard, and the long-chain signal to be soft.
- The change of the model made three Cases of this session wrong in their text: 376 and 377.3 were shown again and ratified again; 377.2 was replaced whole by Case 379 with `{supersedes:case 377.2}`, since its ledger line on `estimate-case-protocol-loaded` could not be taken back otherwise. The person found the re-showing correct but not convenient — worth a thought on how to lighten it.
- Pre-spec: `ask-guppi` found wrong facts in the context of Case 378 (a Case number not yet taken, `rule-plan-mode` called `draft`, a count stated wider than its grep) and gaps in 378.1, 378.3, 378.7 and 381; all were fixed by showing the Cases again. The context of Case 377 (parent) and 377.3 were fixed the same way.
- The person asked for the bashguard refusal not to be reported at Retro any more: deferred as Case 382 on `rule-bash-guard`.
- An open thought of the person: a mechanism "if you touch something in `given`, look at it" without drowning the agent. My answer: put the fact about the tool into the schema instead — one sentence that a `replace` pair acts inside one section of a page (lesson `lesson-generate-replace-anchor-stays-in-one-section`); a candidate Case for the next Plan Mode.

## Direct instructions to the librarian

- Case 377.2 is superseded by Case 379 in its own session and has left the Spec: its three ledger lines (L4–L6) are marked by the `{supersedes:case 377.2}` of L31; nothing of 377.2 is applied, `estimate-case-protocol-loaded` is not touched by this session.
- Several Cases change `rule-case-protocol` in order (378.1, 378.2, 378.4, 378.5, 378.6, 379), and `rule-prespec` (378.4, 378.7, 378.8), `rule-materialize` (377.3, 378.2, 378.4), `rule-estimates-schema` (378.2, 378.4), `entity-glossary` (378.2, 378.3); `guppi prespec --check` simulated all pairs in entry order and found every anchor once.
- The code of 378.2 is built: an Estimate created or updated in this Spec carries a Criterion of `When:`/`Then:` only. Case 376, 377.3 and 379 write their Criterion under `sections` themselves.
- The new decision pages carry `## Given` (378.3, code built).
- The lesson `lesson-case-appended-a-line-inside-another-criterion` carries `{addressed_by:case 378.4}` — the first live use of the mark of 377.3; its root cause belongs with `insight-workflow-contract-change-leaves-its-derived-text-stale`, which 378.5 sets `actioned`: the Insight should stay `actioned`.
- `lesson-case-context-bookkeeping-written-from-memory` shares its root cause with `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (deferred by Case 380).
- The sprint page gets Slice 3g ahead of Slice 4 (Case 381): a plain line, no wikilink.

## What actually got done

- Ratified: 376, 377.1, 377.3, 378.1–378.8, 379, 381; deferred: 380 (Plan Mode), 382 (Retro). Frontier: C4–C8 closed by cases, C3 deferred, C1 and C2 left on the sprint; W1–W3 stay open.
- Code, commit `0e48e5d`: `guppi/materialize.py` (the lesson line's mark through one function `address`, `CRITERION_SECTIONS = ("when", "then")`, a pair inside a Criterion `incomplete: [criterion]`), `guppi/generate.py` (`## Given` on the decision page), `guppi/prespec.py` (the pair inside a Criterion, the frame check, the `note:` lines), with tests. `make test`: 596 passed, 2 skipped; `make style` clean.
- Readings taken, all `passed`: `estimate-materialize-carries-addresses`, `estimate-materialize-lifts-when-and-then`, `estimate-generate-writes-the-given`, `estimate-prespec-refuses-a-pair-inside-a-criterion`, `estimate-prespec-checks-the-frame`, `estimate-prespec-notes-a-long-chain`, `estimate-hi-writes-frontier`.
- Not done: the pages and renders (the librarian's); the readings of `estimate-retro-report-holds-each-fact-once` (by hand at the first `/retro` after the render) and `estimate-case-protocol-ledger-line-form` (the first session where a lesson and the Case that closes its cause stand together); the one pass over the Estimates (Slice 3g); the reading of `estimate-sprint-migration-index-dissolved` (C2, an `rg` over four trees read by hand); the other pending readings of the brief (W1–W3).
