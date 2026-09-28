# Handoff — 2026-09-27, the Case form, the standard of putting off, the backlog

## Notes from memory

- The person reframed C15 (a closer check) into one standard for putting an item off and a single backlog; the rounds ran five times. The brief's Deferred list and its cap of seven go; `backlog.md`, rendered by `guppi backlog`, holds every deferred item, conserved Specs first.
- The person wants short story sections and judges them by complaint; the only complaint so far is the length of `context` (Case 449). The Cases of this session still had long contexts, built under the old rule.
- The person works from a phone: from Case 452 on, a built Case is sent as a file by `SendUserFile` with `display: render`, and the chat holds a short Russian text and the ledger lines. The person tested it on the phone this session (lesson line).
- `/pre-spec` found 12 wordings through `ask-guppi`; Cases 449, 450, 451 (451.1, 451.2, 451.4 changed, 451.14 and 451.15 new) and 452 (452.2–452.4) were ratified again. The item of `rule-insights-schema` stayed in 451.4 so that its ledger line keeps its item; 451.15 replaces only the Criterion of `estimate-insights-schema-checked`.
- Context passed 400 000 tokens before Work Mode; the code was delegated to three subagents.

## Direct instructions to the librarian

- In this run, after `uv run guppi sprint`, run `uv run guppi backlog` (Case 451.13 adds that step to your frame, but your prompt was loaded before the render). Without it `vault/wiki/backlog.md` does not exist: `make lint` reports it, and the next `/hi` loads a missing `@vault/wiki/backlog.md`.
- The re-ratified Cases repeat decision lines the ledger already holds; the ledger hook did not append them twice. The new lines of the re-ratification are L50–L52 (451.14, 451.15).
- `rule-case-protocol` gets `replace` pairs from 449, 451.1, 451.10, 452.4 and 452.5; `rule-case-check` from 449, 452.1 and 452.2. `ask-guppi` found no overlap of anchors, and `prespec --check` simulated them clean.
- The Frontier of this session closes with the old closers (`· sprint`, `· deferred · kept`); the new check of 451.2 applies from the next session.
- Carry into the brief as not done: the Frontier Work lines W1–W34 of this session (the readings and boxes of the previous brief); every `read` line of the Estimates this session creates or updates.
- Carry as flags:
  - The store `<plan>.checked.json` of this session holds no `stored` time; ratifying one of its Cases again needs `case-guppi` again first (the Spec hook refuses "no time held").
  - Unmeasured risk: `SubagentStop` may fire twice, and a second store newer than the sending of the file makes the Spec hook refuse; check it at the first live Case of the next session.
  - `make style` fails under PowerShell on `< /dev/null` of the Makefile; it runs under Bash.

## What actually got done

- Ratified: 449, 450, 451.1–451.15, 452.1–452.5, 453; deferred: 454 (`rule-claude-md`), 455 (`rule-one-judgment-one-implementation`), 456 (`rule-page-generation`). C5 closed `· work`; C1, C2 `· sprint`; C10, C12, C13, C14 `· deferred · kept`.
- Code, commit e1ea55c: `guppi/prespec.py` (451.2, 451.3), `guppi/backlog.py`, `guppi/cli.py`, `Makefile`, `guppi/sprint.py` (451.4–451.6), `guppi/casecheck.py`, `guppi/ratified.py` (449, 452.1–452.3, 453); tests `test_prespec.py`, `test_backlog.py`, `test_sprint.py`, `test_casecheck.py`, `test_ratified.py`. `make test`: 811 passed, 2 skipped; `make style` clean. The 20 code, test and Makefile lines of `spec.md` are ticked.
- Readings: `estimate-case-protocol-defers-in-one-reply` `failed` again — text followed the Frontier in the defer reply. One `knowledge` lesson: `harness-senduserfile-renders-a-markdown-file-on-the-phone`.
- Not done: the pages, renders, `sprint` and `glossary` lines (yours); the readings of the Estimates this session changed (later sessions); W1–W34.
