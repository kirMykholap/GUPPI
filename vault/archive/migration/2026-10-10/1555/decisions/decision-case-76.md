---
type: decision
case: "76"
status: archived
update: ["[[rule-materialize]]"]
supersedes: ["[[decision-case-69]]"]
origin: raw/2026-09-12/ledger.md#case-76
sprint: migration
created: 2026-09-12
tags: [harness, workflow, ledger]
---

## Context

In Work Mode of session I the agent ran `uv run guppi materialize --date 2026-09-12`
to see how the day's lines would parse. The command has one mode: it wrote
`raw/2026-09-12/materialize.yaml`, the librarian's artifact, which the agent deleted
at once. Deferred as Case 69.

## Problem

The only way to see what the ledger and the Spec will become is to write the yaml.

## Given

`guppi/materialize.py` `parser()` has `--date` only; `run` builds the entries and
writes the yaml, printing one line per date. `rule-materialize` `deferred_by:
[decision-case-69]`; `estimate-materialize-walks-dates` Criterion: "walks every
`raw/<date>/` with a `ledger.md` in date order, extends or writes each yaml, prints one
line per date"; `estimate-materialize-assembles` is `pending` since 72.3.
**＋** An existing yaml is extended, never rewritten (case 41): with `--show` the
extension is computed and printed, the file untouched.
**＋** 72.3 and 73.5 update `rule-materialize` this session; each `replace` its own
sentence.
**－** `--show` prints the full yaml of the date, entries already `applied` included;
what is new is visible by the absence of `applied`.

## Criterion

- [[estimate-materialize-assembles]] § case 76

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-76
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
