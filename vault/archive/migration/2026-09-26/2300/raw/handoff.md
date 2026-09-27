# Handoff — 2026-09-26, rounds before a Case, the fence standard, the guard on the plan

## Notes from memory

- The person wanted the forks of an item discussed before a Case is built; that became Case 443 (grill-me rounds through `case-guppi`). Its render is not live yet: in this session the rounds were run by prompt, and they worked (Cases 445 and 447 each went through two or three rounds).
- The person grouped C3–C6 and then dropped the mechanical checks of a list in `context` and of transliteration as not important; C3, C5 and C6 closed as Work, their Estimates read again at the close (W30, W31 both `failed`).
- C14 (the ticks out of the Spec into a work file) was built into a round of seven questions and eight sub-cases, then deferred by the person to the sprint's Work Mode (Case 447, target `rule-work-mode`). The round's answers were not given; the proposal stands in the chat only.
- Case 444 was ratified, rebuilt after Case 445 removed the ratified copy, and ratified again; Cases 443–446 were all rebuilt and ratified again after pre-spec (15 findings of `ask-guppi`). The first 445.5 created `estimate-skill-hi-opens-only-in-plan-mode`; the person moved the promise of the `/hi` refusal into 445.6 alone, so 445.7 supersedes 445.5 (ledger L31 over L23–L24).
- The person chose to refuse a `/hi` whose payload has no `permission_mode` (fail closed), knowing `/hi` has broken before and a session can be repaired without it.
- The session passed 400 000 tokens of context during the re-ratification; Work Mode was delegated to one subagent.

## Direct instructions to the librarian

- Render `rule-hook-registry` (`.claude/settings.json`) in this run: until it is rendered the `PostToolUse` hook `uv run guppi ratified --edit` fails on every Edit/Write ("unrecognized arguments: --edit") and the `--guard` hook of 445.1 is not registered.
- `rule-case-protocol` gets `replace` pairs from 443.3, 444.3 and 445.2; `rule-spec-write` from 444.2 and 445.2 (the first pair of 445.2 and the pair of 444.2 stand in one sentence and do not overlap). Apply each page's pairs in one run.
- 445.1 renames `estimate-spec-reconcile-shows-a-changed-case` to `estimate-spec-reconcile-refuses-an-edit-of-the-plan`; 445.4 deletes `estimate-prespec-checks-the-ratified-copy` and creates `estimate-language-spec-prose-in-english` on `rule-language`.
- Case 445.1 carries `{supersedes:case 423}` (the defer of `rule-spec-reconcile`); 445.7 carries `{supersedes:case 445.5}`, so both lines of 445.5 are superseded and `estimate-skill-hi-opens-only-in-plan-mode` is not created.
- Cases 447 and 448 are short defers under `## Deferred` of the Spec: `rule-work-mode` and `insight-hi-skill-substitution-checked-by-a-model-call`.
- Three lessons in the ledger: `lesson-case-build-a-list-in-context` may pair with the failed reading of `estimate-case-protocol-case-form` (session 1745 and this one); `lesson-case-build-one-promise-signed-in-two-sub-cases` is near `lesson-case-build-a-criterion-replaced-whole-drops-a-line`.

## What actually got done

- Ratified: 443 (443.1–443.3), 444 (444.1–444.3), 445 (445.1–445.4, 445.6, 445.7), 446. Deferred: 447, 448. Frontier: C1, C2 left for the sprint; C8, C10, C11 deferred and kept.
- Code, commit b2825a0: `guppi/materialize.py` (`fence_opening`, `closes_fence`, `fenced_lines`, `fence_for`), `guppi/ratified.py` (`--guard`, no copy, no `--edit`, no marks, no `differences`; `untranslated` reads `## Deferred`), `guppi/prespec.py`, `guppi/casecheck.py`, `guppi/ledger.py` (`is_plan_file`), `guppi/event.py` (`hi_refusal`), `guppi/cli.py` (docstring); tests in `test_materialize.py`, `test_ratified.py`, `test_prespec.py`, `test_event.py`. `make test`: 734 passed, 2 skipped; `make style` clean.
- Choices the subagent made inside the Cases: the guard's event-log line `- HH:MM:SS <stamp> ratified refused <Tool> <path>`; `plan_path` requires `.md`; `ratified.normal` and some parameters removed with the comparison.
- Readings: `estimate-case-protocol-case-form` failed, `estimate-agent-writing-followed` failed (W30, W31).
- Not done: every page change and render (the librarian's); the `read` lines of the 11 Estimates this session creates or updates (next session); W1–W29 of the Frontier (the brief's readings, the `read` boxes of 1745 and 1337, the check of Case 440, the Work lines of 1745); W32 `estimate-language-followed` (its Criterion replaced by 446, read next session).
- Known defect not taken up: `materialize.case_text` and `ratified.quoted_sections` are two copies of one section reader, against "one judgment, one implementation"; both now judge fences by the same functions.
