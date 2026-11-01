---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether guppi prespec --check prints a note, without blocking, for an update of a page that the cascade of generate archives once the items of the plan apply, whether the item that sets off the archive stands in another Case or in the same one
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k cascade
checked: 2026-11-01
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
**＋** The pages archived are: each lesson standing `clustered` among the `children` of an Insight that an `update` of the plan sets `status: actioned`; each Insight standing `open` whose every child stands `archived` once the items of the plan apply; and the Decision page of each Case that a `{supersedes:case N}` mark on a decision line of the session names, but for one that a live page other than a Decision page still names in `deferred_by` or `addressed_by`.
**＋** A name in `deferred_by` no longer keeps a Decision page when a decision line of the Case that carries the mark names that page, as `generate` clears it.
**＋** The pages are judged by `archived_by_cascade` and the keep judgment of `.guppi/guppi/generate.py`, which the cascade of `uv run --project .guppi guppi generate` calls too.
**＋** An `update` and the item that sets off its archive in one Case, or in two sub-cases of one Case, give the note too.
**＋** The note is no finding: it does not change the exit code, and the hook of `rule-prespec-hook` does not block the exit from Plan Mode on it.
**＋** The agent answers the note in one line in the chat, and the person may change a Case or keep the `update`.
**－** A `create`, `delete` or `defer` item of such a page gives no note.
**－** A rule or an entity that the cascade moves between `built` and `draft` gives no note.

## Result

2026-11-01, Retro of session 1721: uv run --project .guppi pytest .guppi/tests/test_prespec.py -k cascade 10 passed, among them a mark on a Decision page that a live page names in deferred_by or addressed_by gives no note, and the same mark gives the note when the Case of the mark names the deferring page; cascade_notes passes kept_decisions over without_cleared to archived_by_cascade

## History

- 2026-10-08 created · [[decision-case-739.1]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/2134/ledger.md#L11
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-11-01 updated: the Criterion replaced whole — a superseded Decision page that a live page still names is not archived, by the keep judgment of generate · [[decision-case-982.2]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/1721/ledger.md#L31
