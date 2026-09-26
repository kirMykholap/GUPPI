# Handoff — 2026-09-25, the findings of Case 412 answered; the scheme of case-guppi deferred with a live probe

## Notes from memory

- Case 414 took defer 412 up and kept of Case 407 only the check of each Case right after it is written. The guard, the fragment and the comparison without `given` were withdrawn: five of the eight findings of 412 fell on them. There is no option `prespec --check --case N`: the hook imports the checks (`prespec.judge`, `prespec.written_findings`).
- The person proposed a new scheme and deferred it whole under Case 416, to be decided next session with the probe results below:
  - the main agent triages a Frontier item from its source only;
  - every Case is built by `case-guppi` (the renamed `frame-guppi`, Opus, effort medium), checked on `SubagentStop`, asked again by `SendMessage`;
  - the plan is written by hooks alone, a guard until the Frontier's Cases are closed, then translation;
  - `ask-guppi` at pre-spec only;
  - the orchestration becomes a rule of its own loaded by `/hi`, `case-schema.md` goes to `case-guppi`.
  The question of 408 went into it (`{supersedes:case 408}`); the question of 410, when prose is translated, stands in its `rule-spec-reconcile` item.
- The live probe W24, in `scratchpad/probe` of this session: the sessions `6bb485fc` (CLI) and `e56498c1` (VS Code) under `~/.claude/projects/C--Users-kir-AppData-Local-Temp-claude-c--PROJECTS-GUPPI-df1dd1da-...-scratchpad-probe/`.
  - `SubagentStop` exit 2 sends the subagent back ("Stop hook feedback"), in CLI and VS Code; its payload holds `agent_type`, `agent_transcript_path`, the raw `last_assistant_message`.
  - A `SubagentStop` `systemMessage` is shown nowhere.
  - A `Stop` `systemMessage` is shown whole, but in VS Code each line prefixed "Stop says:" and no markdown. The person judged it unusable for showing a Case.
  - The `Stop` `systemMessage` stands in the main transcript as `attachment` `hook_system_message`.
  - Python on Windows reads hook stdin as cp1252 unless told utf-8.
  - Consequence for 416: the check before the showing works; the showing stays the main agent's copy in the chat, compared by a hook with the checked answer.
- Cost of subagents this session:
  - `frame-guppi` on 414: 74 122 tokens, 178 s.
  - `frame-guppi` on 417: 46 228 tokens, 177 s.
  - A `SendMessage` after about 40 minutes: 75 160 tokens, 14 s, cache written anew.
  - `ask-guppi` at pre-spec: 88 728 tokens, 204 s.
- Pre-spec found two Case-form faults the agent made at the showing: counts of items in the context of 414, a bookkeeping `－` line in the `then` of 415. 414 was fixed as prose, 415 shown again and ratified again. Reading of `estimate-case-protocol-case-form` is `failed`.
- C6 (a `paths:` rule for vault text outside a Case) closed as `work` with a lesson only, at the person's word. C9 deferred again (418). C1 and C2 (Slice 3g) left `[-] · sprint`.

## Direct instructions to the librarian

- One unit: `raw/2026-09-25/0051/`.
- Case 415 was ratified twice; the ledger holds its line once. Its Spec section is the second showing: the `then` has no line on the frame.
- `{supersedes:case 412}` (414.1), `{supersedes:case 413}` (415) and `{supersedes:case 408}` (416) name Cases of session 2214. They clear the `deferred_by` of `rule-spec-write`, `rule-spec-reconcile` and `rule-prespec` from 412 and 413, and of `rule-frame-check` from 408; 416 defers `rule-frame-check`, `rule-case-protocol`, `rule-spec-write`, `rule-spec-reconcile` and `rule-ask` anew. Defer 403 on `rule-frame-check` stays.
- 414.1 and 414.2 update pages Case 416 of the same Spec defers: known and chosen — 414 is the step now, 416 the scheme after it.
- `estimate-prespec-checks-the-ratified-copy` has its reading `passed` in the ledger after its Criterion is replaced by 417; `estimate-case-protocol-case-form` has a `failed` reading after its Criterion is replaced by 415.
- Renders due: `vault/wiki/case-schema.md` (414.2) and `.claude/skills/pre-spec/SKILL.md` (417).

## What actually got done

- Closed in Plan Mode: Cases 414 (414.1, 414.2), 415, 417 ratified; defers 416 and 418. Frontier C3, C7, C10, C11 by Cases; C6 and W24 as work; C4, C5, C8, C12, C13, C14 deferred by 416, C9 by 418; C1, C2 left for the sprint.
- Code, commit 5c945b4:
  - `guppi/prespec.py`: `judge`, the checks of the plan's Cases shared by `check` and `written_findings`; `check_ratified` excepts a parent whose sub-cases in the copy are all superseded.
  - `guppi/ratified.py`: `stop` runs `written_findings` on each Case written, the reply's decision records added.
  - `tests/test_ratified.py`: `-k checks_the_written` 5 tests, the fixture `working` gained the page `rule-x`.
  - `tests/test_prespec.py`: two tests of 417.
  - `make test` 633 passed, 2 skipped; `make style` clean.
- Not done:
  - The pages and renders of the Spec — the librarian's.
  - The reading of `estimate-spec-write-checks-the-written-case`: the page does not exist yet, and its method has a live part — the first ratification after the change; `pytest -k checks_the_written` gave 5 passed.
  - The reading of `estimate-case-protocol-acknowledging-reply`: by hand, at the first acknowledging reply a `Stop` hook refuses.
  - The Work list of the brief: the 22 pending readings and the unapplied ledger lines of 2214. Not taken.
