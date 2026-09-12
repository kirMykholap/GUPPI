---
type: decision
case: "61"
status: current
update: [rule-materialize, estimate-materialize-assembles]
origin: raw/2026-09-12/ledger.md#case-61
sprint: migration
created: 2026-09-12
tags: [harness, workflow, ledger]
---

## Context

`guppi generate` reported one line in session H: the tag `tests` is used and not in
`tags.md`. It came from two ledger lessons of that session and the Insight the librarian
made over them. A tag enters `tags.md` only through a Case that declares it under
`new_tags`; a lesson is written by the hook, without a Case, so a tag it brings has no
way in.

## Problem

`materialize` collects `new_tags` only from the `then` block of a Case that has decision
lines; a Case whose only content is a tag declaration is never read. So the way in has to
be a Case with some line, or `materialize` reads every Case block for `new_tags`.

## Given

`guppi/materialize.py` (`assemble`) walks `by_case`, the Cases that have decision entries,
and appends each block's `new_tags` to the yaml's top-level list; `generate` registers
them and reports a tag used without registration on stderr.
**＋** `tags.md` holds nine tags; `tests` is on `lesson-tests-generate-history-date-unpinned`
and `insight-tests-clock-not-pinned`; `lesson-tests-cli-date-pinned` carries `harness`
only.
**＋** `rule-materialize` says nothing of `new_tags`; `estimate-materialize-assembles` is
`pending` by case 60 and reads "new_tags are kept" in its unit test only.
**－** The librarian never invents a tag (`rule-documentation`); it reported and left it.

## When

`guppi materialize` reads a Spec; `guppi generate` runs after it.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-61
