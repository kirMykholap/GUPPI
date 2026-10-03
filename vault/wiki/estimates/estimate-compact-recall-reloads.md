---
type: estimate
kind: QA
status: passed
target: "[[rule-compact-recall]]"
purpose: After a compaction of a working session the hook's header, the paths of the /hi files, the Spec and the Frontier's text stand in the context; an ordinary session and another source get nothing
method: pytest tests/test_recall.py on a temp project; live — a compaction of a working session, by hand, the hook's text in the context after it
checked: 2026-10-03
origin: raw/2026-09-21/0019/ledger.md#case-287
sprint: migration
created: 2026-09-21
tags: [session, hooks, harness]
---

## Criterion

When:
The client compacts the context of a session, on the person's command or on its own, and `SessionStart` fires with `source: compact` and runs `guppi/recall.py`.

Then:
With a `hi` in the session's window, stdout holds a header line, "recall: the context was compacted at HH:MM:SS; the session is" followed by the session folder under the vault, such as raw/2026-09-28/2229/, and "Read before the next reply:". Then comes one path per line: the `@` files of `.claude/skills/hi/SKILL.md` in their order, the session's `frontier.md` when it exists, and the Spec when one exists. Last come the line `Frontier:` and the text of `frontier.md` as it stands.
**＋** The Spec is the `spec.md` of the folder, or before the approval the plan file the event log names last.
**＋** The list of paths is the `@` lines of the skill file at the moment the hook fires, with no copy in the code: a file added to those lines is in the list without a change to the hook.
**＋** The texts of the files, the Frontier apart, are not printed, only the paths; the output stays under 10,000 characters.
**－** Without a `hi` in the window, nothing is printed on stdout, and the exit is 0.
**－** Another `source` gives nothing: the matcher keeps the hook from firing, and the code checks `source` itself.
**－** Exit 0 always; an error prints nothing and blocks nothing; the hook writes no file and no event line — `session-start compact` is written by `guppi event`.

## Result

2026-10-03, session 1416: `uv run pytest -q tests/test_recall.py` 7 passed; live, the compaction the person ran by /compact in the working session 682b0e2f: the event log holds `14:25:05 682b0e2f session-start compact` after `14:16:59 682b0e2f hi`; the hook's text in the context opens "recall: the context was compacted at 14:25:05; the session is raw/2026-10-03/1416/. Read before the next reply:", then the six `@` paths of .claude/skills/hi/SKILL.md in their order — sprint, backlog, brief, orchestration, ratification, glossary —, then vault/raw/2026-10-03/1416/frontier.md and no Spec path, no plan file and no spec.md existing, then `Frontier:` and the text of frontier.md as it stood, W1, W6, W8, W15, W19 and W21 closed; no file text printed but the Frontier, frontier.md 3550 bytes and the rest eight short lines; the session folder holds only frontier.md and ledger.md, both written before 14:25:05; not exercised live: a session without hi and another source, covered by the tests only

## History

- 2026-09-21 created · [[decision-case-287]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L2
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given, the docs and the lesson out (case 493.1) · [[decision-case-493.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L7
