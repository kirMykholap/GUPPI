---
type: rule
kind: Leaf
purpose: Prevents Plan Mode from stopping where no person is needed after /pre-spec, in the loop after its findings and between the ratification of the Cases built again on them and the exit
status: built
enforcement: hook
implementation_ref: [guppi/onward.py, guppi/prespec.py, guppi/ledger.py, guppi/casecheck.py, tests/test_onward.py, tests/test_ledger.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-prespec-onward-sends-the-agent-on]]", "[[estimate-prespec-onward-reads-the-decisions-of-the-session]]", "[[estimate-prespec-onward-tells-the-loop-from-its-end]]"]
origin: raw/2026-09-30/2356/ledger.md#case-561.5
sprint: migration
created: 2026-09-30
tags: [session, workflow, hooks, harness]
core: true
---

## Purpose

Prevents Plan Mode from stopping where no person is needed after `/pre-spec`: in the loop after its findings, and between the ratification of the Cases built again on them and the exit. Before `/pre-spec` it stays silent, so the person may speak before `/pre-spec` runs (case 696.2). In Claude Code the end of a reply hands the turn to the person, and a reply that carries a `LEDGER` block ends in that text, so that the ledger hook writes it; so the agent cannot call `/pre-spec` or exit Plan Mode in that reply. This hook, `uv run guppi onward --plan` on `Stop`, sends the agent on in the same turn, as `rule-retro-onward` does after Retro (case 561.5). It judges only the state of files, of the payload and of the transcript — the `hi` and `prespec` marks of the session in the event log, `spec.md`, the open lines under `## Cases` of `frontier.md`, the files under `cases/` against the time of the last `prespec` mark (case 686.1) and the times of the decision lines in `ledger.md` and in every reply of the main agent in the transcript, each at the time of its record, the reply that ended counted as now (cases 597.2, 604), a Case that a `{supersedes:case N}` mark of one of those lines retires, or whose every sub-case with a decision line such marks retire, never out, by the judgment of `guppi/prespec.py` (case 696.1), a file under `cases/` that holds nothing but blank space, the file of a dropped Case, never out (case 701.1), its own refusals and those of the ledger hook in the stretch, from the person's last message, and the first word `STOP:` of the reply — and counts nothing. It fires once a stretch, and once more after each reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark (cases 685.1, 688.7): the agent answers with a reply that writes a line again, a reply that must end, or with a reply that holds no `LEDGER` block, such as the answer that no Case fixed the cause of a lesson, and the hook sends the agent on at the end of that answer too when every other condition holds (cases 686.1, 696.2). The flag `stop_hook_active` and the refusals of other hooks neither silence it nor send it on; with the flag set and a transcript it cannot read, it exits 0 (case 597.1). The ledger hook tells each refused or held line and each reminder once a stretch, so the hook cannot loop. With no `prespec` line it stays silent and sends the agent nowhere (case 696.2). With the line, when a file under `cases/` that holds more than blank space was written after the last `prespec` mark (case 701.2), it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding. When no file under `cases/` that holds more than blank space was written after that mark, no Case has been built again on the findings yet — the reply wrote a defer or a lesson in answer to the report — and it sends the agent on with the loop after the findings: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit (case 686.1). A reply that opens with `STOP:` ends, for the case where only the person can go on. An error of the hook itself after it has read the payload exits 0 before `/pre-spec`, or when the hook cannot read the `prespec` line, and does not send the reply back (case 696.2); after `/pre-spec` it exits 2 with `onward: not checked: <error>` on stderr and the advice to go on, at most once a stretch, judged by its own refusal in the stretch alone (case 597.1).

## History

- 2026-10-01 created · [[decision-case-561.5]]
- 2026-10-01 estimate estimate-prespec-onward-sends-the-agent-on added · [[decision-case-561.5]]
- 2026-10-01 deferred · [[decision-case-575]]
- 2026-10-01 status: draft → built · cascade
- 2026-10-02 updated: the run speaks again after each reply the ledger hook refused, judged by the refusals in the transcript, not by stop_hook_active (case 597.1) · [[decision-case-597.1]]
- 2026-10-02 defer by decision-case-575 superseded · [[decision-case-597.2]]
- 2026-10-02 updated: a Case is out by the decision lines of every reply of the stretch, so a re-ratification counts after a ledger refusal too; implementation_ref names the modules and tests the hook uses (case 597.2) · [[decision-case-597.2]]
- 2026-10-02 estimate estimate-prespec-onward-reads-the-decisions-of-the-stretch added · [[decision-case-597.2]]
- 2026-10-02 status: built → draft · cascade
- 2026-10-03 updated: a Case is judged out by the decision lines of every reply of the transcript, not only of the stretch, so a re-ratification with unchanged lines counts for the rest of the session (case 604) · [[decision-case-604]]
- 2026-10-03 ref `estimate-prespec-onward-reads-the-decisions-of-the-stretch` → `estimate-prespec-onward-reads-the-decisions-of-the-session` · [[decision-case-604]]
- 2026-10-04 status: draft → built · cascade
- 2026-10-05 deferred · [[decision-case-648]]
- 2026-10-06 defer by decision-case-648 superseded · [[decision-case-686.1]]
- 2026-10-06 updated: after /pre-spec the hook sends the agent to the check and the exit only when a Case file was written after the prespec mark, and on with the loop after the findings otherwise; it sends the agent on again after a line the ledger hook held and after its reminder of a lesson with no mark, as after a refused line; the defer of case 648 retired (case 686.1) · [[decision-case-686.1]]
- 2026-10-06 estimate estimate-prespec-onward-tells-the-loop-from-its-end added · [[decision-case-686.1]]
- 2026-10-07 updated: a Case that a supersedes mark retires, whole or sub-case by sub-case, is not out, so a Case replaced under a new number no longer keeps the hook silent (case 696.1) · [[decision-case-696.1]]
- 2026-10-07 updated: the hook sends the agent on at the end of the answer to a reply the ledger hook sent back, an answer with no LEDGER block too, and no longer sends it to /pre-spec (case 696.2) · [[decision-case-696.2]]
- 2026-10-07 updated: a Case file that holds nothing but blank space, the file of a dropped Case, is never out (case 701.1) · [[decision-case-701.1]]
- 2026-10-07 updated: the emptied file of a dropped Case is no Case built again after /pre-spec (case 701.2) · [[decision-case-701.2]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
