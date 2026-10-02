---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec-onward]]"
purpose: Whether guppi onward --plan judges a Case out by the decision lines of ledger.md and of every reply of the main agent in the transcript, each at the time of its record, so that a re-ratification with lines the ledger already held counts at every later reply of the session
method: "uv run pytest tests/test_onward.py; by hand at the first Case ratified again with unchanged decision lines in Plan Mode after the change, at the reply that closes the last line under Cases after a later message of the person: the transcript, ledger.md and the times of the files under cases/, recorded in the estimate line"
origin: raw/2026-10-02/2049/ledger.md#case-597.2
sprint: migration
created: 2026-10-02
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run guppi onward --plan` judges, at the end of a reply of the main agent, whether a Case is still out.

Then:
A Case N is still out when a file `case-<N>.md` under `raw/<date>/<hi HHMM>/cases/` was written after the last decision line of Case N or of a sub-case of N.
**＋** The decision lines it reads are the timed lines of `raw/<date>/<hi HHMM>/ledger.md`, the lines inside a `LEDGER` block of each reply of the main agent in the transcript at `transcript_path`, and those of the reply that ended.
**＋** The replies of the transcript are its `assistant` records of the main agent, read by `transcript_records` of `guppi/ledger.py`, the reading the ledger hook makes. A reply before the person's last message counts like one after it.
**＋** A line of a reply of the transcript counts at the time of its record, read by `moment` of `guppi/casecheck.py`. A line of the reply that ended counts as written now.
**＋** A line of `ledger.md` counts at its time on the `hi` date, rolled to the next date when the time runs backwards.
**＋** So a Case built again and ratified by a reply whose decision lines the ledger already held is not out after that reply, and not at any later reply of the session, after a later message of the person too. This includes the reply that writes again a line the ledger hook refused.
**－** A file of a Case with no decision line is out.
**－** A record whose time cannot be read counts none of its lines. A transcript that cannot be read leaves `ledger.md` and the reply that ended as the only sources.
**－** Its own refusals and those of the ledger hook are still judged in the stretch, by `refusals` of `guppi/ledger.py`.

## History

- 2026-10-02 created · [[decision-case-597.2]]
- 2026-10-03 renamed from `estimate-prespec-onward-reads-the-decisions-of-the-stretch` · [[decision-case-604]]
- 2026-10-03 updated: renamed; the Criterion, purpose and method replaced — the decision lines of every reply of the transcript count, not only those of the stretch (case 604) · [[decision-case-604]]
