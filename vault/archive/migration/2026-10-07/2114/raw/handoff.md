# Handoff — 2026-10-07, the Case-file check, the take-back and pre-spec after session 1804

## Notes from memory

- Case 722, Q3: the person chose a second sub-case for the pre-spec half against the recommendation. The frame then showed that `/pre-spec` no longer reports such a parent, and the fix moved to the Spec hook (722.2).
- Case 722, Q6: the person first chose to fix the `## Splitting` sentence of `rule-case-protocol` on a Frontier line closed again by the superseding Case inside 722, which meant dropping 722.3's defer line. The rebuild could not pass the Case-file check while the first build stood in the plan (722.Q8). On the agent's proposal the person kept 722 as first ratified, its defer of `rule-case-protocol` included, and Case 723 changed its Q3 answer to leaving that sentence out. That sentence (F5 of Case 713) stays wrong and put off.
- The person's answers twice named a Case by the wrong number ("722 : b", then "724.q5", both meant Q5 of Case 723; "Мы меняем 722", meant "722 is not changed"). The agent asked once and the person confirmed.
- The person asked why Case 722 was shown for ratification before a question of Case 723 was answered (lesson L29).
- Case 722 was ratified three times with the same ledger lines: first; after its file was restored; after 722.1 was rebuilt for the exception of 725.2, and once more after the pre-spec findings. Its `recommend` holds `**Change**` items for each.
- At pre-spec the person chose that 722.1 names the exception of a mark in the answer's own file only as a pointer to `estimate-case-check-leaves-out-a-case-the-file-supersedes` (lesson L30).
- The `case-guppi` of Case 726, asked whether "The body of a deferred decision is not read" stays in the new Criterion of `estimate-prespec-reconciles`, answered without saying; the Spec holds it as the last `－` line of 726.2.

## Direct instructions to the librarian

- Case 722.3 holds both an `update` and a `defer` of `rule-case-protocol` in one sub-case, on purpose: apply the update, which carries `{supersedes:case 721}` and so clears `decision-case-721` from that page, then let the defer add `decision-case-722.3`'s page to its `deferred_by`. The page must end with a `deferred_by` again.
- Case 723.1 carries `{supersedes:case 713}{supersedes:case 721}`: `decision-case-713` goes `superseded`; `decision-case-721` leaves the `deferred_by` of `rule-orchestration` only, since 723.1 names that page alone.
- Case 722.1 carries `{supersedes:case 720}`: `decision-case-720` leaves the `deferred_by` of `rule-case-check`.
- `rule-case-check` takes two pairs, from 722.1 and from 725.2, on two different sentences of its Purpose; check both anchors hit after each other.
- `estimate-hi-writes-frontier` gets a new `method` from 723.3 and stays `pending`.
- Renders this run must write: `vault/wiki/case-schema.md`, `vault/wiki/orchestration.md`, `.claude/skills/hi/SKILL.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md`.
- `raw/2026-10-07/2114/cases/case-724.md` stands empty: no Case 724 exists; it is the leftover of a rebuild of Case 722 that was undone.

## What actually got done

- Cases ratified: 722 (722.1, 722.2, 722.3), 723 (723.1, 723.2, 723.3), 725 (725.1, 725.2), 726 (726.1, 726.2). No Case of the session is superseded by another.
- Code: `guppi/casecheck.py` (`other_blocks` leaves out a stored part its top-level file no longer holds, by the new `left_by_its_file`, and a Case a `{supersedes}` mark of the answer's own `ratification` names); `guppi/ratified.py` (`remove_superseded` also removes a parent whose every sub-case with a decision line is retired, by `prespec.retired_whole`, when the parent holds no decision line of its own; new `ancestors`; `stop` passes the session's ledger records); `guppi/prespec.py` (new `defer_notes`, called by `plan_findings`).
- Tests: `tests/test_casecheck.py` (2 tests of a stored part, 4 `superseded_by_the_file`), `tests/test_ratified.py` (3 `superseded` tests of a parent), `tests/test_prespec.py` (4 `defers_a_page`).
- `make test`: 1428 passed, 6 skipped. `make style`: clean.
- Readings: L19–L26 — seven `passed`, `estimate-orchestration-defers-in-one-reply` `failed` (L22, Retro, not read).
- Lessons: L27–L30. L27 carries `{addressed_by:case 725.1}`, L28 `{addressed_by:case 725.2}`; L29 and L30 none.

## Debt

- No box of code or test is left; no patch.
- 32 boxes wait for the librarian: the page, render and `read` lines of the ten sub-cases.
- `estimate-hi-takes-a-conserved-spec` — a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — a `/work` that `/box` calls and the `/work` of the session that closes a sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone` — the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-lint-clean` — the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-merges` — the Work Mode of the session that closes the sprint.

## Observations

- `make lint` was red before the work, exit 2, 13 finding lines: 11 `unread`, 1 `deferred` (`rules/rule-morph`), and `backlog: vault/wiki/backlog.md differs from its sources`, which the brief of session 1804 did not list. Not run at Retro.
- No expected red: no task changed a check over a page this Spec updates.
- The Case-file check refused a build of a ratified Case under a new number while the first build stood in the plan (L28); Case 725.2 fixes it in code this session, but the check that ran in this session was the old one.
- The sprint items of the close of `migration` were put off again; the close was not prepared.
- `ask-guppi` at pre-spec narrowed its lessons Grep against its frame, as it reported; no finding rested on it.
- Each turn in Plan Mode carried a system reminder to end with a picker or `ExitPlanMode`; the agent kept to `rule-orchestration` and called `ExitPlanMode` only after `/pre-spec`.

## For the next session

- F5 of Case 713: the sentence of `rule-case-protocol` that a Frontier line is closed again by the superseding Case does not hold for a sprint or backlog item whose Case is taken back; put off again by Case 722.3.
- `estimate-orchestration-defers-in-one-reply` is `failed`, not read: no decision of a source other than the sprint or the backlog was put off; a Case decides whether its method waits for such a defer or reads the Render.
- Lessons L29 and L30 have no fix: how the main agent holds a Case that comes back while another Case's round is open, outside a batch; and a recommendation to widen a Criterion checked against "nothing is signed twice" before it is given.
- The close of the sprint `migration`: a session of its own.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back?
