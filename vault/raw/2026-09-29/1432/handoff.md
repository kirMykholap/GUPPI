# Handoff — 2026-09-29, Slice 4 closed; the round and the Decision page made readable

## Notes from memory

- The person thinks of the round of `case-guppi` as the layer they read, and of the `context` of a Case as the agent's record; Cases 512 and 513 follow from that. They want to keep thinking about the readability of a Case.
- "Executable plan" is a term for a future Work Mode: a map of tasks written after the Spec is approved. It is not decided yet and left the glossary until it is.
- The person asked to see an example of a round in the new form before Case 511 was built, and accepted it.
- The session passed 400 000 tokens of context in Work Mode.

## Direct instructions to the librarian

- Case 510 stands twice in the ledger: `decision[case 510][update][estimate-sprint-migration-leftovers-gone]` from its first ratification, and `decision[case 510][update][entity-sprint-migration]` added at the ratification again after /pre-spec. Its Spec section is the rebuilt Case with both items; apply both once.
- Case 511.2 is superseded by Case 512 in this session and left the Spec; its lines L9–L10 carry no item. Case 512 carries the change of 511.2.
- Case 513.2 changes what `generate` writes on a Decision page from this run on: `## Problem`, and `## Context` only for a Case without `given`. The pages of this session's Cases are written in the new shape; `vault/wiki/decisions/schema.yaml` is rendered from 513.1 in the same run. A `schema: missing section ## Context` on a page of this session before the render is expected.
- Case 514 changes `generate`: the failed entry L67 of `raw/2026-09-29/1134/materialize.yaml` repeats L15 of case 508.2 and should now close as applied, with one stdout line.
- Case 515 rewrites rows of `entity-glossary` that rest on pages Case 513 changes; both land in this run.

## What actually got done

Ratified: 510, 511.1, 512, 513.1, 513.2, 513.3, 514, 515, 516, 517, 518, 519.

What got done: commits d2ad75d (code of 513.2, 514, 516, and the deletions of 510: `vault/parked/` and every file under `docs/` but `docs/migration/migration-plan.md` — the commit message names the code only) and 9c8075f (the session folder); `guppi/generate.py`, `tests/test_generate.py`, `tests/test_schemas.py`, `tests/test_materialize.py` changed; make test 905 passed, 3 skipped; make style clean; readings L1–L5 and L25–L31; lessons L32–L35.

What is not done:
- The reading of `estimate-glossary-terms-defined` under Case 515 waits for a session after this run renders the table; its reading of this session stands before the Case.
- The Render of `rule-estimates-schema` says the frame of a Case stays on its Decision page — short defer, Case 519.
- A repeat of Case 514 ticks its line of the Spec, as an applied entry does; the task line said "apply nothing". Without the tick the test of two entries of one kind and slug ticking two lines went red.
- Case 510 closed a sprint item with no update of the sprint page — lesson.
- Case 512 quoted the person in Russian in its context — lesson.
- Counts and claims in the contexts of Cases 510, 513 and 515 the vault did not bear out — lesson.
- Case 510 split into sub-cases at its rebuild though its first line stood in the ledger — lesson.

21 boxes wait for the librarian.
Read in a later session: `estimate-sprint-migration-leftovers-gone`, `estimate-skill-grill-me-asks-in-rounds`, `estimate-case-build-writes-a-plain-round`, `estimate-decisions-schema-checked`, `estimate-generate-writes-the-decision-page`, `estimate-generate-fails-alone`.
