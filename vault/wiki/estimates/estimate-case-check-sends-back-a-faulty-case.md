---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: A Case of case-guppi that the checks refuse goes back to it before the main agent sees it
method: uv run pytest tests/test_casecheck.py -k subagent, then by hand the first answer of case-guppi the hook sends back
origin: raw/2026-09-25/1228/ledger.md#case-419.3
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers.

Then:
`uv run guppi casecheck --subagent` reads each Case of `last_assistant_message` in the chat form, by the functions of `guppi/ratified.py`.
**＋** It builds each Case's section of the Spec in memory, as the Spec hook writes it, and runs `judge` of `guppi/prespec.py` over them, the decision lines of the `ratification` fence standing for the ledger.
**＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
**＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` answers again.
**＋** Each Case of the answer is stored with its findings in `<plan>.checked.json` beside the plan file of the session.
**＋** On the re-fire (`stop_hook_active`) the findings are stored, and it exits 0.
**－** An answer with no Case heading, or an answer of another agent, is not checked, not stored, and exits 0.

## History

- 2026-09-25 created · [[decision-case-419.3]]
