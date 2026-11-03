---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a fresh lesson line with a tag that tags.md does not hold and that neither a ratified Case of the session nor a newtag block of a lesson line declares, and says why only for the reply just finished
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py -k unlisted_tag
checked: 2026-10-15
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, ledger]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session whose `{tags:...}` holds a tag.

Then:
A fresh lesson line stays out of the ledger while its `{tags:...}` names something outside `vault/wiki/tags.md`.
**＋** Such a line lands once this session ratified a Case declaring each such name, the decision line of that Case written earlier or in the same `Stop`.
**＋** Such a line lands when a `{newtag:<tag>|<meaning>|<aliases>}` block declares each such tag, on the line itself or on a lesson line of the session's ledger or of the same `Stop`.
**＋** A block declares its tag only when that tag stands in the `{tags:...}` of its line and its meaning and aliases are not empty, as `parse_line` of `.guppi/guppi/materialize.py` reads it.
**＋** The other lines of the `Stop` are written as before.
**＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — tag <tag> is not in tags.md and nothing of this session declares it: write the line again with a tag of tags.md, or declare the tag on the line by {newtag:<tag>|<meaning>|<aliases>}, the tag also in its {tags:...}."
**＋** A refused line from an earlier text of the transcript is judged again at every `Stop` without a word, and is written at the first `Stop` where each of its tags is listed or declared.
**＋** The ledger hook takes its known tags from `.guppi/guppi/tags.py`, the same source as `.guppi/guppi/casecheck.py`.
**－** A line that the hook cannot read, or refuses for its prefix, is not judged for its tags.
**－** The blocks of such a line declare no tag.
**－** `estimate[...]` and `decision[...]` lines are not judged for their tags, and a line already in the ledger of any session is not judged again.
**－** In a project with no `vault/wiki/tags.md`, the ledger hook refuses no lesson for its tags.

## Result

2026-10-15, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
