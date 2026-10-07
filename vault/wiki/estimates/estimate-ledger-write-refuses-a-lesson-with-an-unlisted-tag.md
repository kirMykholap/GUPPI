---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a fresh lesson line with a tag that tags.md does not hold and no ratified Case of the session declares, and says why only for the reply just finished
method: uv run pytest tests/test_ledger.py -k unlisted_tag
origin: raw/2026-10-07/0636/ledger.md#case-703.2
sprint: migration
created: 2026-10-07
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session whose `{tags:...}` holds a tag.

Then:
A fresh lesson line stays out of the ledger while its `{tags:...}` names something outside `vault/wiki/tags.md`.
**＋** Such a line lands once this session ratified a Case declaring each such name, the decision line of that Case written earlier or in the same `Stop`.
**＋** The other lines of the `Stop` are written as before.
**＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — tag <tag> is not in tags.md and no ratified Case of this session declares it: write the line again with a tag of tags.md; in Plan Mode a Case may first declare the tag by a tag line, and from /work to the end of Retro the new tag goes as a line of the handoff to a later session."
**＋** A refused line from an earlier text of the transcript is judged again at every `Stop` without a word, and is written at the first `Stop` where each of its tags is listed.
**＋** The ledger hook takes its known tags from `guppi/tags.py`, the same source as `guppi/casecheck.py`.
**－** A line that the hook cannot read, or refuses for its prefix, is not judged for its tags.
**－** `estimate[...]` and `decision[...]` lines are not judged for their tags, and a line already in the ledger of any session is not judged again.
**－** In a project with no `vault/wiki/tags.md`, the ledger hook refuses no lesson for its tags.

## Result

2026-10-07, Retro of session 0636, uv run pytest tests/test_ledger.py -k unlisted_tag; 9 passed

## History

- 2026-10-07 created · [[decision-case-703.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0636/ledger.md#L30
