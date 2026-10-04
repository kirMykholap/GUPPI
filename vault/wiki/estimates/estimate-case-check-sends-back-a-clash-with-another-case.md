---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether the check of an answer of case-guppi sends back a Case that sets one field, writes one section or replaces one Criterion that another Case of the session, ratified or only stored, sets, writes or replaces too, and whether the main agent asks the person when the other Case should change instead
method: uv run pytest tests/test_casecheck.py -k session_clash; then by hand a live answer of case-guppi that the hook sends back for a clash with another Case of the session, that Case shown and ratified once, and, where its context names another Case that should change, the main agent's question to the person and its SendMessage on a yes
origin: raw/2026-10-04/1439/ledger.md#case-629.1
sprint: migration
created: 2026-10-04
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
**＋** Or `tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.
**＋** The main agent receives the answer of `case-guppi` that passed, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `guppi/prespec.py`, imported, not copied: each Case of the plan file, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
**＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
**＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
**＋** Where the other Case should change rather than its own, `case-guppi` still changes its own Case so that no finding stands, and its `context` names the other Case and the change it needs; the main agent shows the Case as it stands and asks the person whether that other Case is built again, and on the person's yes sends it to its `case-guppi` by `SendMessage`, in a batch when it is ratified.
**－** A stored Case that has findings, an entry joined with an agent id, and a Case whose number a `{supersedes:case N}` mark of the session's ledger names are not compared.
**－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
**－** Two other Cases that clash with each other give this answer no finding.
**－** The `Stop` hook `uv run guppi ratified` keeps its check of the Cases it writes, by the same function.

## History

- 2026-10-04 created · [[decision-case-629.1]]
