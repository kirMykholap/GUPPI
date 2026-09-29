---
type: estimate
kind: QA
status: passed
target: "[[rule-brief]]"
purpose: Whether the brief ends the Readings due line of each pending Estimate read at the librarian's run with the facts its method and Criterion name, the stdout of guppi archive included, with no comparison or verdict, one line per Estimate
method: "by hand at the /hi of the session after the first librarian run whose frame holds this Render: vault/wiki/brief.md read against the run's report in the previous transcript, recorded in the estimate line"
checked: 2026-09-29
origin: raw/2026-09-29/1134/ledger.md#case-508.4
sprint: migration
created: 2026-09-29
tags: [harness, workflow, librarian]
---

## Criterion

When:
The librarian `librarian-guppi` writes `vault/wiki/brief.md` in its run, and then runs `uv run guppi archive`.

Then:
For each `pending` Estimate whose `method` names the librarian's run, its line under Readings due of `vault/wiki/brief.md` ends with the facts that its `method` and `## Criterion` name, as the steps of the run before the brief printed or left them.
**＋** After `uv run guppi archive`, the librarian adds its stdout lines at the end of the Readings due line of each `pending` Estimate whose `method` names the archive step, and the close of `rule-close` commits the brief with them.
**＋** Each Estimate keeps one line under Readings due, with the Estimate, its `draft` rule and where it is read.
**－** The line compares nothing and carries no passed or failed, and the librarian writes no ledger line.
**－** The order of the steps does not change: the brief, then `uv run guppi archive`, then the close.
**－** No line of the brief names the commit of the close.

## Result

2026-09-29, by hand at the /hi of session 1753, vault/wiki/brief.md against the report of the run d8c1f17 in the transcript of session 1432: the five pending Estimates whose method names the librarian's run (brief-carries-the-run-facts, generate-renames, generate-rewords, generate-writes-the-decision-page, glossary-ticks-the-spec) each keep one Readings due line with the rule and where it is read, ending with the facts of the run and no passed or failed; the report gives guppi archive exit 0 with empty stdout and no pending Estimate whose method names the archive step, and the brief says so and that it was written before the archive; grep of brief.md for d8c1f17 counts 0; the append of archive stdout was not exercised

## History

- 2026-09-29 created · [[decision-case-508.4]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1753/ledger.md#L1
