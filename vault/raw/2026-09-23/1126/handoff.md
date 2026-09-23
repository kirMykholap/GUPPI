# Handoff — 2026-09-23, the known contradictions of 0034, the Case form in the chat

## Notes from memory

- At `/hi` the agent refused to write `frontier.md`, citing plan mode; the person said the write is allowed and done in every session. Case 363 puts that into the skill. A lesson of this session records the recurrence (`lesson-plan-mode-frontier-refused-at-hi-again`); the lesson of 2026-09-16 (`lesson-plan-mode-frontier-refused-on-the-client-text`) names the same refusal — a pair for the synthesis.
- Case 367 changed at the person's word: the agent first proposed to read only the lint lines of the Slice's pages; the person objected that lint must see the whole vault and signal every finding, and chose to drop lint from that Estimate altogether. Lint itself does not change.
- The pre-spec found 15-odd defects in ratified Cases; 363 and 367–374 were shown again and re-ratified, with four new decision lines on `estimate-case-protocol-loaded` (368, 370, 373) and `estimate-case-protocol-acknowledging-reply` (368). In Work Mode 365 and 367 were shown again once more: their grep matched stale `__pycache__/*.pyc`, now `--include='*.py'`.
- C7 (the archive paths of the Frontiers) closed `· work`: every live text and all 34 archived Frontiers agree on `<date>/<HHMM>/raw/`; the agent could not reconstruct what 0034's pre-spec had called a contradiction.
- C1 (`estimate-sprint-migration-leftovers-gone`, Slice 4) was put off `· sprint` by the person.
- The person valued two forms and had them written as rules: the heading `## Case N — name` in the chat (368) and the content of an item as sub-points `old` / `new` under its task line (370).
- At Retro the person found two defects in the report of `/retro` — the ratifications listed twice, the unticked boxes apart from "not done"; deferred as Case 375 on `rule-retro`.

## Direct instructions to the librarian

- Order of pairs on shared pages: `rule-case-protocol` takes pairs from 368, 370 (two), 373; `estimate-case-protocol-case-form` from 364.2, 368, 370, 373; `estimate-case-protocol-loaded` from 368, 370, 373 — all three insert a line before the same anchor "`render --check` after the render exits 0.", so the anchor stays for the next; `rule-materialize` gets 364.1 (a pair) and 365 (change alone); `rule-page-generation` 365 (change alone) and 369 (a pair). The pre-spec simulated every pair in entry order with no miss.
- `rule-rules-schema` is a Render: after 372 `vault/wiki/rules/schema.yaml` must be rendered; the task `uv run pytest tests/test_schemas.py -k rules` of 372 stays for the next session.
- 373 sets `insight-workflow-ratified-content-changed-on-the-agents-own-finding` `actioned` with `addressed_by: decision-case-373`, bare as 360 wrote it.
- Case 375 is a short defer under `## Deferred` of the Spec: `rule-retro`, type rule.
- Five lessons this session: `lesson-case-protocol-chat-case-without-heading` (addressed by 368), `lesson-case-check-command-signed-without-a-run`, `lesson-case-context-claim-wider-than-its-search`, `lesson-case-render-update-skipped-the-live-reading-estimate`, `lesson-plan-mode-frontier-refused-at-hi-again`. The last three share one pattern with the lessons of the Insight actioned by 373 only loosely; judge the clusters yourself.
- 14 readings in the ledger (L27–L40), all `passed`; `estimate-atomicity-rendered` was read after the line of Case 374, so its read line under 374 is the reading's.

## What actually got done

- Ratified: Cases 363, 364.1–364.3, 365–374; deferred: 375. Frontier C1–C15: C1 `· sprint`, C7 `· work`, C15 `· defer case 375`, the rest `· case N`; W1 and W2 stay open.
- Code, commit `23e9d11`: `guppi/materialize.py` — the Routing Table in the docstring, a `then` item found by `slug` alone; `guppi/generate.py` — no "Rule-class" in two docstrings; three test names renamed; a test for an `update` with no content. `make test` 582 passed, 2 skipped; `make style` clean.
- Readings passed: the five `*-schema-checked` but rules, `page-schemas-one-file-per-rule`, `lint-catches`, `claude-md-rendered`, `sprint-moves-a-passed-over-item`, `sprint-drops-an-emptied-milestone`, `generate-ticks-the-spec`, `brief-written`, `atomicity-rendered`, `prespec-checks-the-plan`.
- Not done: the pages and renders (the librarian's). Readings for the next session — the Criteria this Spec replaces: `hi-writes-frontier`, `prespec-reconciles`, `generate-fails-alone`, `sprint-migration-rule-class-files-dissolved`, `case-protocol-case-form`, `case-protocol-loaded`, `case-protocol-acknowledging-reply`, `prespec-binds-a-sprint-line`, `rules-schema-checked`; and `sprint-migration-index-dissolved`, whose measured texts the librarian writes. Not taken: `documentation-completes` (its live part — what the librarian read — was not checked against the event log; `make test-documentation` 167 passed), `one-judgment-one-implementation-followed` (the diff holds no code that judges a text), `agent-writing-followed` and `session-phases-in-order` (at the close), `carry-over-writes`, `synthesis-keeps-actioned-by-the-mark`, the four of `entity-sprint-migration`.
- `make lint` read in Work Mode: 100 findings, exit 1, unchanged from the last brief.
