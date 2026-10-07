---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-onward]]"
purpose: Whether guppi onward --plan judges a Case out by the decision lines of ledger.md and of every reply of the main agent in the transcript, each at the time of its record, so that a re-ratification with lines the ledger already held counts at every later reply of the session, and whether a Case file that holds nothing but blank space, the file of a dropped Case, never counts as out
method: "uv run pytest tests/test_onward.py; by hand at a Case ratified again with unchanged decision lines in Plan Mode, at the reply that closes the last line under Cases after a later message of the person: the transcript, ledger.md and the times of the files under cases/, recorded in the estimate line"
checked: 2026-10-07
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
**＋** A Case N is not out, whenever its file was written, when a `{supersedes:case N}` mark of one of those decision lines, read by `parse_line` of `guppi/materialize.py`, retires N, or when such marks retire each sub-case of N that has a decision line. The marks are judged by `superseded_in_window` and `retired_by` of `guppi/prespec.py`, and the judgment of a parent by one function of the same module. So a Case that the person replaced by a Case under a new number, whole or sub-case by sub-case, does not keep the hook silent.
**＋** A file `case-<N>.md` that holds nothing but blank space is the file of a dropped Case: it never makes Case N out, whatever its time and whether or not a decision line names N.
**－** Marks that retire some sub-cases of N, but not each one that has a decision line, leave the file `case-<N>.md` judged as before.
**－** A file of a Case with no decision line that holds more than blank space is out, unless such a mark retires the Case.
**－** A record whose time cannot be read counts none of its lines. A transcript that cannot be read leaves `ledger.md` and the reply that ended as the only sources.
**－** Its own refusals and those of the ledger hook are still judged in the stretch, by `refusals` of `guppi/ledger.py`.

## Result

2026-10-07, uv run pytest tests/test_onward.py tests/test_casecheck.py tests/test_ratified.py: 365 passed, among them an empty and a blank Case file with no decision line not out, a file of text with no decision line out, an empty file after the last decision line of its Case not out; by hand in session 0425: the reply at 06:09:14 ratified Case 701 again with the lines of 701.1 that ledger.md held since 04:52:59, cases/case-701.md written after 04:52:59, and guppi onward --plan exited 2 with its reason to run the check and exit, so Case 701 was not out

## History

- 2026-10-02 created · [[decision-case-597.2]]
- 2026-10-03 renamed from `estimate-prespec-onward-reads-the-decisions-of-the-stretch` · [[decision-case-604]]
- 2026-10-03 updated: renamed; the Criterion, purpose and method replaced — the decision lines of every reply of the transcript count, not only those of the stretch (case 604) · [[decision-case-604]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/0115/ledger.md#L16
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-07 updated: the Criterion replaced whole — a Case that a supersedes mark retires, whole or sub-case by sub-case, is not out · [[decision-case-696.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L34
- 2026-10-07 updated: the Criterion replaced whole — a Case file that holds nothing but blank space, the file of a dropped Case, is never out (case 701.1) · [[decision-case-701.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0425/ledger.md#L19
