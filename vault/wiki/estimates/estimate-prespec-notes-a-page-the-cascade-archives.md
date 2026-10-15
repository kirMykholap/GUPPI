---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether guppi prespec --check prints a note, without blocking, for an update of a page that the cascade of generate archives once the items of the plan apply, whether the item that sets off the archive stands in another Case or in the same one
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k cascade
origin: raw/2026-10-08/2134/ledger.md#case-739.1
sprint: migration
created: 2026-10-08
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the `then` blocks of the plan and the decision lines of the session's window.
**＋** Or `.guppi/tests/test_prespec.py` runs it over a made-up plan.

Then:
For each `update` item of the plan whose page the cascade of `.guppi/guppi/generate.py` archives once the items of the plan apply, the check prints one line that opens with `note:` and names the Case of the `update`, the page and the Case whose item sets off the archive.
**＋** The pages archived are: each lesson standing `clustered` among the `children` of an Insight that an `update` of the plan sets `status: actioned`; each Insight standing `open` whose every child stands `archived` once the items of the plan apply; and the Decision page of each Case that a `{supersedes:case N}` mark on a decision line of the session names.
**＋** The pages are judged by one function of `.guppi/guppi/generate.py`, which the cascade of `uv run --project .guppi guppi generate` calls too.
**＋** An `update` and the item that sets off its archive in one Case, or in two sub-cases of one Case, give the note too.
**＋** The note is no finding: it does not change the exit code, and the hook of `rule-prespec-hook` does not block the exit from Plan Mode on it.
**＋** The agent answers the note in one line in the chat, and the person may change a Case or keep the `update`.
**－** A `create`, `delete` or `defer` item of such a page gives no note.
**－** A rule or an entity that the cascade moves between `built` and `draft` gives no note.

## Result

2026-10-08, Retro, uv run pytest tests/test_prespec.py -k cascade: 8 passed — an update of a clustered lesson under another Case gives one note and exit 0 by --check; one Case and two sub-cases give it; an open Insight left with no live child and a superseded Decision page give it; create, delete, defer, a built/draft move and a page archived before the plan give none; judged by generate.archived_by_cascade, which cascade calls

## History

- 2026-10-08 created · [[decision-case-739.1]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/2134/ledger.md#L11
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
