# Handoff — 2026-09-15, session S: the Insight actioned, the stale heads caught up, the supersedes marks every entry (Cases 173–179)

## Notes from memory

- Case 175 went through three forms before ratification. The owner rejected the first (a
  new kind in the filter of `mark_superseded`) and the second (`kind: delete` for the block
  removal — "we do not even have `kind: delete`; a Decision page has lists `create`,
  `update`, `delete`, `defer`"). The ratified form drops the filter: every entry carrying
  `case: N` is marked, whatever its `kind`; `remove_criterion` stays an internal word of
  the yaml. The History line of `estimate-generate-writes` that credits 164 with the
  removal of block 124.2 is left as it is, on purpose.
- Case 177 exists because pre-task (`ask-guppi`) found that block 130.2 of
  `estimate-materialize-assembles` signs the filter by kind that 175 drops; the line of
  175 was already in the ledger, so 177 carries `{supersedes:case 130.2}` with a
  `contract: same` and one `replace` — the route Case 171 took in session R. The `given`
  of 175 in the Spec was corrected after ratification: `rule-materialize` carries two
  Estimates, not one; `estimate_slug` names `estimate-materialize-assembles`.
- The owner's reading of the pattern behind 171 and 177: the Criterion of an Estimate
  accumulates one block per contract change, written by a script with no judgment on
  contradiction; only pre-task judges, after the signature. Deferred as Case 178 on
  `rule-plan-mode` for the next Plan Mode, with the librarian-at-generate alternative in
  the `purpose`. The lesson of the session records the same fact.
- `estimate-retro-commit-gates` (169.1) stays `pending` by the owner's choice: the live
  refusal of a typed `/retro` on a Spec item without its line did not happen this session.
  The owner wants to type `/retro` at the start of the next session, before the plan is
  written, to see what the gate says.
- 173 actions the Insight on the strength of 169.1–169.3, whose readings were `pending`
  at the time (169.2, 169.3 passed at Retro; 169.1 still pending). `actioned` is not
  terminal, so a failed reading reopens it.
- Case 179 (`rule-case-protocol`, "six" → eight) was a side note of `ask-guppi` at
  pre-task that the agent put in Notes instead of raising as a Case; the owner asked why,
  and it became a Retro defer.

## Direct instructions to the librarian

- Check first: `estimate-materialize-assembles` after the run — block 130.2 gone (177),
  block 175 present and `pending`, no block 177. `rule-materialize` — both `replace`
  applied: the one of 175 in the line about a later `supersedes` (…"every entry carrying
  its `case`"…), the one of 177 in the description of the yaml ("marks every entry
  carrying `case: N`"). `decision-case-130.2` `superseded` → archived by the cascade.
- The live half of the reading of 175 is this run: Case 176 supersedes 170, whose line
  itself carried `{supersedes:case 162}`, so `raw/2026-09-15/1448/materialize.yaml` holds
  three entries of 170 — two `defer` and one `remove_criterion` of 162. After `materialize`
  all three must carry `superseded_by: '176'`, and `generate` must print no line for them.
  Report the three entries as you find them; the agent reads `estimate-materialize-assembles`
  block 175 on that report next session. Do not write the estimate line yourself.
- 174: three `replace` on `estimate-generate-writes` (one), `estimate-cleanup-moves`
  (two), `rule-ledger-write` (one, `contract: same`). Each `old` was verified to match
  once. The two Estimates were read `passed` this session (lines L8, L9 of the ledger)
  before 174 applies; a `passed` reading and a head-text `replace` on the same page in one
  run — the reading sets `status`/`Result`, the `replace` edits the head; the order in the
  yaml is the ledger order (174 lines before the readings). Confirm the page ends
  `passed` with the corrected head.
- 173: the Insight `insight-retro-typed-command-is-never-a-tool-call` → `actioned`,
  `addressed_by: decision-case-173`; the cascade archives its two lessons
  (`lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate`,
  `lesson-retro-typed-still-bypasses-the-skill-tool-after-150`), `cleanup` moves them to
  `archive/migration/2026-09-15/1809/lessons/`. The `case-schema.md` entry is a `file`,
  applied by hand already (the sentence at the end of "`when` and `then` are the
  criterion").
- The lesson `lesson-plan-mode-contract-change-skips-the-estimates-blocks` (`error`):
  compare against `insight-workflow-contract-change-leaves-its-derived-text-stale`
  (`actioned`) and `insight-ledger-line-written-unchecked` at synthesis — the root cause
  here is the unread Estimate at Case time, not stale derived text; likely no match, but
  judge on the index line. No second lesson with this root cause exists yet: session R
  wrote none for 171.
- 176: defers on the two live placeholders, `deferred_by` 170 → 176 by the supersedes;
  `decision-case-170` archived. 178 and 179: defers with pages (`rule-plan-mode`,
  `rule-case-protocol`), `deferred_by` set, no placeholder.
- Readings `pending` after this run, for "Readings due": `estimate-materialize-assembles`
  (175, this run's report), `estimate-retro-commit-gates` (169.1, the owner's typed
  `/retro` before the plan of the next session), `estimate-brief-written` (168 — your
  brief: "Readings due" as its second section; the agent reads it next session).
- Expect lint to move: −2 `ref`… no: the two placeholders keep their 6 `schema` + 2
  `orphan`; the 62 findings of Cases 1–28 stay. No page loses or gains a required field
  by this session; expect 70 unchanged unless the archived lessons change a count.
- `sprint.md`: no change.

## What actually got done

- Ratified: 173 (Insight `actioned`; `case-schema.md`), 174 (`estimate-generate-writes`,
  `estimate-cleanup-moves` head texts; `rule-ledger-write` both advices, `contract:
  same`), 175 (`rule-materialize`, `contract: changed`, `estimate_slug:
  estimate-materialize-assembles`), 176 (defer Slice 3b, supersedes 170), 177
  (`rule-materialize`, `contract: same`, supersedes 130.2), 178 (defer `rule-plan-mode`),
  179 (defer `rule-case-protocol`).
- Readings `passed`: `estimate-case-protocol-loaded` (167), `estimate-cleanup-moves`
  (166.4), `estimate-generate-writes` (166.2, 166.3, 172 — one line; the owner checked
  the Obsidian backlinks), `estimate-hook-registry-rendered` (169.2), `estimate-retro-loads`
  (169.3 — typed 20:31:22 and called 21:12:53, two `retro` marks).
- Lesson: `lesson-plan-mode-contract-change-skips-the-estimates-blocks` (`error`).
- Code, commit `e88a357` on `migration`: `guppi/materialize.py` (`mark_superseded` by
  case number, docstrings), `tests/test_materialize.py` (+2: the same yaml, a foreign
  yaml). 379 green, `make style` clean.
- By hand: `vault/wiki/case-schema.md`, one sentence (case 173).
- `raw/2026-09-15/1448/spec.md`: five reading boxes ticked (166.2, 166.3, 166.4, 167,
  172). `raw/2026-09-15/1809/spec.md`: the agent's boxes ticked; the librarian's `update`
  boxes of 173, 174, 175, 177 and the readings 169.1, 175, 168 open.
- Not done: the pages of 173, 174, 175, 177 (this run); the reading of 175 (this run's
  report, read next session); 169.1 `pending` on purpose; 168 (this brief); Slice 3b
  (176); F6–F8 of the frontier are Slice 5 tasks in `sprint.md`, closed as `work`.
