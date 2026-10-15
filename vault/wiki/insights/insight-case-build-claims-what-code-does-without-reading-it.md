---
type: insight
pattern: case-guppi states what a function or a script of the code does, and builds a Case or a recommendation on that claim, without reading the function that decides it, so the claim proves false after the person has signed it and the Case is built again
status: open
children: ["[[lesson-case-build-reused-judgment-not-checked-against-the-other-side]]", "[[lesson-case-build-recommended-on-a-claim-about-code-it-did-not-read]]"]
severity: 2
deferred_by: ["[[decision-case-835]]"]
origin: raw/2026-10-13/2118/ledger.md#L27
sprint: plugin
created: 2026-10-13
tags: [workflow, ci, session, harness]
---

## Pattern

Two lessons, one cause. In session 2252 case-guppi named page_exists of guppi/materialize.py as the judgment that /pre-spec and guppi generate share, without reading the find that generate calls, and the ask-guppi run found that the two answer differently, so Case 783 was built again. In session 2118 case-guppi of Case 807 recommended rewording the pages from the run of guppi ship, saying that run shows every page line that holds a pointer, without reading clean_parenthesis of guppi/ship.py, which cuts a pointer out of a longer bracket without printing a line; a later round withdrew the answer. In both a claim about what code does was stated and not read in the code.

## Proposal

One sentence in rule-case-build that before case-guppi states in a round or a context what a function or a script does or prints, it reads the function that decides it and names that function in context. A suggestion, not a decision.

## History

- 2026-10-14 created · raw/2026-10-13/2118/ledger.md#L27
- 2026-10-15 deferred · [[decision-case-835]]
