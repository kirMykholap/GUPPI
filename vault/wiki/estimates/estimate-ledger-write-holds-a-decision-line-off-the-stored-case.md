---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook holds a decision line other than a defer that is not a line of the stored ratification of its Case, an addresses mark set aside, tells the agent once a stretch, and writes it once a copy equal to a stored line stands
method: uv run pytest tests/test_ledger.py — piped payloads, a session ledger and a store beside a plan file in a temp vault
origin: raw/2026-10-06/0104/ledger.md#case-688.7
sprint: migration
created: 2026-10-06
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds, in a `LEDGER` block of a session with a `hi`, a decision line of a kind other than `defer` that no ledger holds yet.

Then:
The hook compares the line, a `{addresses:<slug>}` block and trailing spaces set aside, with the ledger lines of the `ratification` of the entry stored under its Case id alone in `<plan>.checked.json`, read by the function of `guppi/casecheck.py` by which the `Stop` check of a showing reads them.
**＋** A line equal to one of them lands as before.
**＋** A line equal to none of them, a line of a Case the store holds no text for, and a line of a session with no plan file is not written; the other lines of the `Stop` land.
**＋** For such a line of the reply just finished, the hook exits 2 and prints: "ledger: decision[case <N>] not written — it is not a line of the ratification case-guppi stored for case <N>: copy it again as the summary of case-guppi holds it, alone in a LEDGER block, or send the Case back to its case-guppi when the stored line is wrong."
**＋** The stderr line is printed only when it does not already stand in a refusal of the hook since the person's last message.
**＋** A held line is judged again at every `Stop` while it stands in a text of the transcript, and never lands while it differs; a line written again that equals a stored line lands.
**＋** A line written again with `{addresses:<slug>}` added, as Case 685 asks, lands when the line without the mark equals a stored line.
**－** A `defer` line, an `estimate` line and a `lesson` line are not compared.
**－** A line that `parse_line` of `guppi/materialize.py` cannot read, and a line the hook refuses while no live sprint page stands, get that refusal alone and are not compared.
**－** With `stop_hook_active` set the hook judges the line the same; with the flag set and a transcript it cannot read, the line does not land and the hook prints nothing.

## Result

2026-10-06, uv run pytest tests/test_ledger.py: 119 passed, the 11 tests of the hold among them — a copy equal to the store lands, a differing copy, a Case with no stored text and a session with no plan file are held with the rest landing, a copy written again equal lands, a copy with the addresses mark lands, a defer is not compared, a held line of an earlier text stays out silently, told once a stretch, the flag with no transcript stays out silently and with a transcript is held

## History

- 2026-10-06 created · [[decision-case-688.7]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L34
