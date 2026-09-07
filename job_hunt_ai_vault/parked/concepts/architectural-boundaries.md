---
title: "AST tests hold the layering, and each states what it does not catch"
type: concept
status: current
authority: boundary-tests
basis: code
sprint: S0
created: 2026-08-13
sources: ["CLAUDE.md", "archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [architecture, testing, web]
---

# Seven AST tests hold the layering

| Test | Rule |
|---|---|
| `tests/unit/test_web_boundary.py` | web routes never touch the database directly — all SQL lives in `web/data/` |
| `tests/unit/test_web_templating_boundary.py` | one Jinja environment only, in `web/templating.py`, with `auto_reload` off |
| `tests/unit/test_vacancy_write_boundary.py` | only `ingest/upsert.py` writes `Vacancy` fields |
| `tests/unit/test_network_boundary.py` | network access stays in the HTTP client |
| `tests/unit/test_batch_write_boundary.py` | collection batches are written only by `ingest/batches.py` |
| `tests/unit/test_parser_boundaries.py` | `parsers/` does not import `jobhunt.db`, `jobhunt.ingest`, `jobhunt.web` or `sqlalchemy` |
| `tests/unit/test_normalize_boundaries.py` | the same for `normalize/` — see [[normalisation-layer]] |

**There are seven.** The two beyond the original five are what keep the value dictionary single
across sources.

*Line updated 2026-08-14.* It read «`CLAUDE.md` names five; there are **seven**» — true when it was
written, and the correction was right: the corpus was right and the rule file was wrong, which is
the direction this project had never checked. `CLAUDE.md` now names no count at all — the table
moved here when it was cut to a map ([[claude-md-is-a-map-and-four-rules]]) — so the sentence had
begun describing a file that no longer says that. **This page is the survivor and simply states
seven.** The shape of that failure, and the twelve other instances of it:
[[a-stated-count-drifts-from-the-list-it-heads]].

**Seven survived a challenge on 2026-08-15 and the challenge was wrong.** A recount by globbing the
filename gave **eight**; the eighth is `tests/unit/_ast_boundary.py`, the shared helper, which is
not a boundary test. The page was right and the correction was the error — which is now its own
lesson, because the same session's other measurement failed in the opposite direction
([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]).

**If one of them fails, fix the cause, never the test.**

## What they do not catch, stated because a boundary must not be trusted past its reach

- a computed field name — `setattr` with a variable;
- raw SQL text;
- a write from another process.

Exclusion lists are given as a path from the package root rather than by filename, so a **new**
`web/upsert.py` does not pass the boundary. And the single narrow exception to the vacancy-write
boundary is `renormalize_all`; the width of that exception is pinned by a **synthetic** source —
text and path handed to the check rather than read from disk — because a check run against a file
that is already clean proves nothing.

Two more rules of the same family, not AST-checked: web routes take a session through
`Depends(get_session)` and never `session_scope()`; and the web layer may write
`ProfileVacancy.status` and `ProfileTag.is_enabled`, nothing else on those tables and nothing at
all on `Vacancy`.

A third rule of the family cannot be AST-shaped at all, because it is about two artefacts agreeing
at runtime rather than about what a module imports: **migrations must not drift from the models**,
held by `tests/integration/test_migrations.py` and by nothing else in the suite —
[[migrations-do-not-drift-from-the-models]].

## Why each boundary carries a list of what it misses

The wave-2 boundaries let through `Vacancy as V`, `models.Vacancy(...)`, `setattr`,
`update(Vacancy)` and `from urllib import request` — while the handoff claimed that "no file
writes its objective fields". **A boundary described more strongly than its implementation is
more dangerous than no boundary at all**, because the next session trusts it more than it is
worth. Every boundary now states explicitly what it does not catch.

See [[a-boundary-stronger-in-prose-than-in-code]] for the lesson this produced, and
[[javascript-policy]] for the boundary that is agreed but not yet written as a test.
