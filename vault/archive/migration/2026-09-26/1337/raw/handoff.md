# Handoff — 2026-09-26, the check of case-guppi and the keys of an item

## Notes from memory

- `/hi` did not run as a skill: its `!` command lines failed the permission check of Claude Code 2.1.282 in VS Code (the detail was withheld). The agent ran the four commands by hand. The session began in auto mode, so the first plan file was `~/.claude/plans/session-2026-09-26-1337.md`. When plan mode came on, the plan, its `.ratified.md` and its `.checked.json` were copied to `steady-inventing-gadget.*`, the name Claude Code gave the plan. From then on the hooks read that file.
- Case 434 was ratified three times. First with "the last handback after the last received message". Then it was rebuilt after the W28 probe with rounds of the conversation, and the person did not ratify that version. Then it was rebuilt with the person's rule, "the newest output of the subagent that holds a Case, handback or text", and ratified. The ledger holds its lines once.
- Case 436 was ratified first with sub-cases 436.1–436.3. Pre-spec (ask-guppi) found faults. 436.1 and 436.2 were rebuilt, and 436.4 was added and ratified. After the last 434, 436.4 was rebuilt again so that it carries 434's new `then` lines, and ratified again. Its Criterion of `estimate-case-check-sends-back-a-faulty-case` is the one `generate` must leave standing: 436.4 comes after 434.
- Cases 434 and 436.4, re-ratified in Work Mode, reached only the plan file, not `spec.md`. With the person's consent the agent replaced their sections in `raw/2026-09-26/1337/spec.md` by hand with the re-ratified versions from the plan. The name, `context` and `problem` were translated to English, and the ticks were kept. `spec.md` is the source; the plan file is not.
- The person asked that two open questions go to the next session as Cases:
  1. A Case re-ratified in Work Mode does not reach `spec.md`. A possible fix: the Spec hook writes into `spec.md` once it stands, as it already does for a defer at Retro.
  2. The agent can forget the mark `{addressed_by:case N}` or `{addresses:…}` on a lesson line. The line `lesson-hooks-subagentstop-fires-before-and-after-the-handback` (ledger L19) carries none, though Case 434 closes its cause. The person chose to keep the line as written.
- Case 438 defers `rule-prespec`: after case 437 a pre-spec finding in the body of a Case goes to its `case-guppi` and a new ratification, and the translation is the last step. The ratified 437 writes a parent's prose from the store, where it is in Russian, so a translation can be undone.
- A consequence of 436.2 nobody ratified on its own: the old key `contract` on an `update` item is now a pre-spec finding. Before, case 194.1 let it pass. The test `test_the_keys_of_the_old_shape_are_not_read` was changed to that. On a `create` the old keys still pass.
- Context passed 400 000 tokens in Work Mode. The person chose to finish the code of 434, 436 and 437 in this session.

## Direct instructions to the librarian

- Read `raw/2026-09-26/1337/spec.md`, not the plan file. The sections of 434 and 436.4 there are the last ratified ones.
- Order in `estimate-case-check-sends-back-a-faulty-case`: 434, then 436.4. The Criterion of 436.4 stands last, and it carries 434's lines word for word.
- In `estimate-spec-write-copies-the-ratified-case`: 436.1, then 437. The Criterion of 437 stands last, and it carries 436.1's lines.
- `rule-spec-write` gets three `replace` pairs, from 436.1, 436.3 and 437. `rule-case-check` gets three pairs from 434 and one from 436.4, and the anchor of 436.4 must still match after 434. `rule-case-protocol` gets one pair each from 435 and 437. The pre-spec of the plan found no missed or doubled anchor; `spec.md` was edited afterwards for 434 and 436.4 only.
- Case 433: after `generate`, check by hand that the `## Trigger` of `lesson-case-show-sub-case-ratification-retyped` names the comparison on `Stop` and holds no `SubagentStop`. This is task line 43 of `spec.md`.
- Lessons of the session: `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback` (L2, addressed by 434 on L3), `lesson-hooks-subagentstop-fires-before-and-after-the-handback` (L19, no mark, by the person's choice), and `lesson-case-show-ref-of-a-ratification-line-retyped` (L20). The last one shares its root cause with `lesson-case-show-sub-case-ratification-retyped`: the main agent retyped a shown Case. Consider the pair for an Insight.
- `raw/2026-09-25/1228/spec.md` line 151 and `raw/2026-09-25/1654/spec.md` line 46 were ticked by hand as work: C5 and C6 of the Frontier.

## What actually got done

- Ratified: 433, 434 (three times; the last version stands), 435, 436.1, 436.2, 436.3, 436.4 (twice), 437. Deferred: 438 (`rule-prespec`). Frontier: C3–C6 and C9–C11 closed by Cases or work; C1 and C2 `· sprint`; C7 and C8 `· deferred · kept`; C12 `· defer case 438`.
- Code, commit 95e9619:
  - `guppi/materialize.py`: `ITEM_KEYS`, `accepted_keys`, `item_keys`; `schema_changed` also takes records.
  - `guppi/generate.py`: the keys of an `update` come from `ITEM_KEYS`.
  - `guppi/ratified.py`: `put` refuses a foreign key; `key_judge` and `window_schema_free`; a `defer` key checked; the write from the stored answer, compared by `casecheck.against_store`.
  - `guppi/prespec.py`: `check_keys` in `judge`.
  - `guppi/casecheck.py`: `answer_of`, the newest output with a Case; the store guards the loop, not `stop_hook_active`; with no plan file nothing is sent back; `against_store`.
  - `guppi/ledger.py`: `read_records`.
  - Tests in `test_casecheck.py`, `test_ratified.py`, `test_prespec.py`, `test_materialize.py`. `make test` gave 694 passed, 2 skipped; `make style` was clean.
- W28 is done: the payload of `SubagentStop` in 2.1.282 carries `agent_transcript_path`. The probe in `guppi/casecheck.py` was removed.
- Not done:
  - The pages and renders of every Case (the librarian's work).
  - The readings of the Estimates this session changed, in a later session: `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-protocol-shows-the-built-case`, `estimate-spec-write-copies-the-ratified-case`, `estimate-prespec-checks-the-form-of-an-item`, `estimate-spec-write-writes-a-defer`. The failed `estimate-case-protocol-shows-the-built-case` is closed by the new Criterion of 435 and waits for its reading.
  - Frontier Work lines W1–W27: the readings of the brief, not taken this session. They include `estimate-sprint-migration-*` and the other by-hand readings.
  - The manual part of 434: not measured whether an exit 2 with `stop_hook_active: true` reaches the subagent.
