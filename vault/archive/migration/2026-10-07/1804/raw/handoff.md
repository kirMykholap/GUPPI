# Handoff — 2026-10-07, the cost of a Case and the checks before ratification

## Notes from memory

- The person raised the cost of a `case-guppi` dispatch themselves: each Case reached 86k–138k tokens of context before `/pre-spec`. Case 717 came out of that talk. In it the agent first claimed that every answer rewrites the subagent's cache. The transcripts showed that only a pause longer than five minutes does, and the agent corrected itself before the Case was built.
- Case 717, Q4: the person took the one-hour cache for `case-guppi` on the recommendation. The agent's own numbers showed it costs about 60% more on a dispatch with no long pause and slightly less on one with a long pause. Option (c), keep five minutes, was named as the choice with no risk.
- Case 717, Q5: the person chose to rewrite the existing promise. The hook then refused two wordings of `estimate-case-build-writes-the-case` in one session, since 716.1 rewrites it, so 717.2 creates its own Estimate instead. The person ratified it with that change named.
- Case 716 came from the person's question why Estimates hang `pending` though nobody touched them. The answer: only a Case that replaces a Criterion sets `pending`, and a `method` that waits for another session leaves it `failed` at Retro. The person agreed to fix the `method` of the two checks of `case-guppi` only, not the reading rule of every Estimate.
- At `/pre-spec` the person did not follow what happened with the stale store entries and asked for a plain explanation. They chose to remove the entries; the auto mode classifier denied it. They then chose to leave everything as it is: Case 719 was dropped, Case 713 stays as first ratified with the faults F2–F6 that pre-spec found, and both the store problem (Case 720) and the fixes (Case 721) were put off to the next session.
- The close of the sprint `migration` was put off again: this session ratified Cases that do not prepare it, so it cannot be the closing session.

## Direct instructions to the librarian

- The plan holds Case 713 as first ratified. Case 719 was dropped and its file `cases/case-719.md` is empty; it has no decision line. Apply 713's four pairs on `rule-orchestration` as they stand.
- Case 721 puts off `rule-orchestration` and `rule-case-protocol`, which Cases 713 and 717.1 update in the same session: apply the updates, and let the defer add `deferred_by`.
- Cases 716 and 717 were ratified twice, the second time after the pre-spec fixes, with the same ledger lines; the plan holds the second text.
- Case 717.1 creates `rule-case-example`, `render_mode: full`, governing `vault/wiki/case-example.md`, and moves both examples out of `case-schema.md`. Check after the render that `case-example.md` holds one block tagged `case` and that `case-schema.md` holds none; `uv run pytest tests/test_case_schema.py` then reads the new file.
- Case 717.2 adds `experimental:` with `cacheTtl: "1h"` by a pair anchored on `skills: [grill-me]` in the Render of `rule-case-build`. Check that it lands in the frontmatter of `.claude/agents/case-guppi.md`.
- Case 717.1 deletes `estimate-case-protocol-example-passes-the-check` and sets the `estimates` of `rule-case-protocol` without it.
- The one `create` that is not an Estimate is `rule-case-example`; its nearest page is `rule-case-protocol`.

## What actually got done

- Cases ratified: 712, 713, 714, 715, 716 (716.1, 716.2), 717 (717.1, 717.2, 717.3); short defers 718, 720, 721. Case 719 was dropped with no decision line.
- Code: `guppi/lint.py` (`holds`, `unmet_conditions`; `check_schema` reports through it; `matches` removed); `guppi/prespec.py` (`check_conditions`, `created_page`, `kept_method_waits`; `judge` runs `check_conditions` after `check_keys`; the docstring list gains both findings). Tests: `tests/test_prespec.py` (the `condition` and `kept_method` tests, and a test that runs `created_page` and `Vault.create` over the same items), `tests/test_lint.py` (`unmet_conditions`), `tests/test_case_schema.py` (reads `case-example.md`, or `case-schema.md` until the render writes it).
- `make test`: 1415 passed, 6 skipped. `make style`: clean.
- Readings: L19–L26, eight Estimates `passed`. Lessons: L27–L30.

## Debt

- No box of code, test, command or migration is left unticked; no patch.
- 27 boxes wait for the librarian: page, render and read lines.
- `estimate-hi-writes-frontier`: the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec`: a session that takes a conserved Spec, and the `/hi` after the close of a sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: a `/work` from `/box` and the `/work` of the session that closes a sprint.
- `estimate-brief-written`: the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders`: `backlog.md` after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run`: after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint`: the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups`: after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`: the Work Mode of the session that closes `migration`.

## Observations

- `make lint` was red before the work, exit 2, 14 finding lines: 1 `deferred` (`rules/rule-morph`) and 13 `unread`. It was not run in Retro.
- The store of the Case-file check, `C:\Users\kir\.claude\plans\adaptive-gathering-dewdrop.checked.json`, still holds the entries 713.1 and 713.2. They leave the check only when a ledger line carries `{supersedes:case 713}`.
- Case 713 goes into the vault with the faults pre-spec found: the short-form paragraph of `rule-orchestration` still names only the closer `[-] … · defer case N`, one sentence says both that the `defer` lines add to the source and that the source stays as it is, and `estimate-orchestration-defers-in-one-reply` still says a sprint or backlog item takes no short Case.
- `/pre-spec` gave no finding on Cases 713 and 717.1 updating `rule-orchestration` and `rule-case-protocol`, which Case 721 of the same plan defers, though `rule-prespec` says such a pair is a finding.
- `ask-guppi` at `/pre-spec` reached 170k–201k tokens of context, as much as a `case-guppi` dispatch.
- `cacheTtl: "1h"` under `experimental` rests on the Claude Code docs as the claude-code-guide agent read them (v2.1.248 and later; 2.1.292 is installed); it was not tried live. Every dispatch of this session ran with the five-minute cache.
- `created_page` of `guppi/prespec.py` repeats the derivation of `Vault.create` of `guppi/generate.py`, since the Case left `generate` unchanged; one test runs both over the same items.
- `tests/test_case_schema.py` keeps the path that reads `case-schema.md` while `case-example.md` does not stand; its Criterion says a Case of a later session removes it.

## For the next session

- The stale entries of the store of the Case-file check (Case 720): the person removes the keys `713.1` and `713.2` by hand or adds a permission rule, and a Case decides how the store drops a sub-case that a Case built again no longer holds.
- The pre-spec fixes of Case 713 (Case 721): F2–F6, taken up as a new Case that supersedes 713.
- `rule-case-build` sets no step for a fix that adds a second behaviour to a ratified Case with no sub-cases.
- The close of the sprint `migration`: a session of its own (Case 718).

## Ask the person
