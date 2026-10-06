# Handoff — 2026-10-06, the backlog groups: the ledger, pre-spec and the showing of a Case

## Notes from memory

- Case 685: the person turned down a hold of the decision lines ("the agent should not stop to work out whether to mark a lesson") and chose a reminder after the write; the person asked whether the agent stops, and agreed once told that the agent goes on in the same turn.
- Case 688: the person asked whether the agent could show the ledger lines first, in a reply of their own, so that a wrong line is caught before the rest; told that a `Stop` hook runs only at the end of a turn, the person dropped it and declined a separate question on passing the lines through a tool call. The person needed a plain explanation of Q2 (the second copy of the lines at ratification) before choosing to bring it in.
- Case 686: the person chose (b) on Q2 against the recommendation, so 686.1 changes one sentence of `rule-prespec` while 687 changes no rule.
- Case 689: the third round changed the method of `estimate-internal-context-loaded` from a later `/hi` to the rendered skill file or the Spec at Retro, since the check refuses a method that waits for a later `/hi`; the person agreed.
- `/pre-spec`: twelve findings over Cases 685–690; all were sent back with no word of the person; the confirmation left one open — the reply to a held line named twice in one sentence of `rule-orchestration` — and the person chose that 688.7 keeps its clause and 685.1 drops its mention. The contexts of 686 and 688 were brought to one answer on `estimate-prespec-onward-reads-the-decisions-of-the-session` (it stands).
- The backlog items of `rule-work-mode`, `rule-spec-box`, `entity-guppi` and `rule-morph` were kept as they stand by the person's word; `rule-sprint-close` and the close of migration were left on the sprint page for the session that closes the sprint.

## Direct instructions to the librarian

- `rule-orchestration` takes replace pairs from five Cases: 685.1, 686.1, 688.7 (two pairs), 689.1 and 690.2. The anchor of 688.7 starts right after the text 685.1 replaces (`` `- estimate[...]` and `- lesson[...]` lines the moment``); apply 685.1 first or check that both land, and that the sentence names the reply to a held line once.
- `rule-ledger-write` takes pairs from 685.1 and 688.7 on two different sentences; 688.7 also sets `implementation_ref` (adds `guppi/casecheck.py`).
- `rule-prespec-onward` takes 686.1 with `{supersedes:case 648}`: its `deferred_by` names `decision-case-648`, which this retires.
- `rule-case-check` takes a new `purpose` and two replace pairs from 688.1.
- The Insights `insight-prespec-after-findings-loop-unruled` (687), `insight-case-show-built-case-retyped-by-hand` (688.8), `insight-session-vault-knowledge-not-loaded` (689.2) and `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` (690.3) are set `actioned`; their lessons go to the archive by the cascade.
- Renders: `vault/wiki/orchestration.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/agents/case-guppi.md`.

## What actually got done

- Cases ratified: 685 (685.1, 685.2), 686 (686.1, 686.2), 687, 688 (688.1–688.9), 689 (689.1, 689.2), 690 (690.1–690.3); each built again at `/pre-spec` and ratified again, 688.9 added there.
- Code: `guppi/materialize.py` (`unlinked_lessons`); `guppi/ledger.py` (the reminder after the write — `unaddressed`, `reminder_message`; the hold of a decision line off the store — `off_store`, `off_store_message`; the docstring); `guppi/onward.py` (`TO_LOOP`, `built_after`, `plan_onward` reads the `prespec` line by `prespec_mark`; the docstring); `guppi/prespec.py` (`prespec_mark`, which `window` uses); `guppi/casecheck.py` (the `Stop` run judges every reply whatever `stop_hook_active` says, guarded by its own refusals — `own_told`, `times_given`, `give`, a limit of three; the error path under the same count; the docstring).
- Tests: `tests/test_ledger.py` (a plan file and a store in the fixture, so the decision lines of the tests are copies of a stored Case; the reminder and the hold tests); `tests/test_onward.py` (the loop tests; the old test after `/pre-spec` now has a Case file after the line); `tests/test_casecheck.py` (the re-fire tests changed to the count; the loop-guard tests).
- `make test`: 1316 passed, 6 skipped. `make style`: clean.
- Readings L33–L46 and L49, all `passed`. Lessons L47, L48.

## Debt

- No box of code or test is debt.
- 55 boxes wait for the librarian: page lines, renders and `read` lines.
- `estimate-hi-writes-frontier` — the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec` — a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — a `/work` that `/box` calls and the `/work` of a session that closes a sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — `backlog.md` after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges` — the Work Mode of the session that closes the sprint.

## Observations

- Red before the work: `make lint` exit 2 in the Baseline — `backlog: vault/wiki/backlog.md differs from its sources`, `rules/rule-morph: deferred: 1 time since case 239`, and 11 `unread: pending` lines.
- The hooks changed in Work Mode run from the working tree at once: from this Retro on, the ledger hook holds a decision line that is not a copy of the stored Case and reminds of unmarked lessons, and `guppi casecheck` judges a showing after a refusal. The Retro reply carried no decision line, so neither met a live case here.
- One reading line of Retro was written with `- estimate-` and no `[`, so it was no ledger line and was lost silently; it was written again with the lessons (L49). No hook tells a near-miss prefix from prose.
- The hold of case 682.1 named all nineteen Cases of the session in its question for each of the two Retro lessons.
- `make lint` was not run in Retro; nothing of this Spec is marked under `## Expected red`.

## For the next session

- Plan Mode and pre-spec group is done (685–688); the knowledge group is done (689, 690). Left in the backlog by the person: `rule-work-mode`, `rule-spec-box`, `entity-guppi`, `rule-morph`.
- `rule-sprint-close` and the close of migration stay for the session that closes the sprint.
- Whether a line inside a `LEDGER` block that opens with `- decision`, `- estimate` or `- lesson` but not with the bracket should be refused aloud rather than dropped.
- The question of the 682.1 hold names every Case of the session; whether it should name fewer.

## Ask the person
