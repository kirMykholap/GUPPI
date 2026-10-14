---
type: rule
kind: Leaf
purpose: Prevents Plan Mode from stopping where no person is needed after /pre-spec, in the loop after its findings and between the ratification of the Cases built again on them and the exit
status: built
enforcement: hook
implementation_ref: [guppi/onward.py, guppi/prespec.py, guppi/ledger.py, guppi/casecheck.py, tests/test_onward.py, tests/test_ledger.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, hooks, harness]
core: true
---

## Purpose

Prevents Plan Mode from stopping where no person is needed after `/pre-spec`: in the loop after its findings, and between the ratification of the Cases built again on them and the exit. Before `/pre-spec` it stays silent, so the person may speak before `/pre-spec` runs. In Claude Code the end of a reply hands the turn to the person, and a reply that carries a `LEDGER` block ends in that text, so that the ledger hook writes it; so the agent cannot call `/pre-spec` or exit Plan Mode in that reply. This hook, `uv run guppi onward --plan` on `Stop`, sends the agent on in the same turn, as `rule-retro-onward` does after Retro. It judges only the state of files, of the payload and of the transcript — the `hi` and `prespec` marks of the session in the event log, `spec.md`, the open lines under `## Cases` of `frontier.md`, the files under `cases/` against the time of the last `prespec` mark and the times of the decision lines in `ledger.md` and in every reply of the main agent in the transcript, each at the time of its record, the reply that ended counted as now, a Case that a `{supersedes:case N}` mark of one of those lines retires, or whose every sub-case with a decision line such marks retire, never out, by the judgment of `guppi/prespec.py`, a file under `cases/` that holds nothing but blank space, the file of a dropped Case, never out, its own refusals and those of the ledger hook in the stretch, from the person's last message, and the first word `STOP:` of the reply — and counts nothing. It fires once a stretch, and once more after each reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark: the agent answers with a reply that writes a line again, a reply that must end, or with a reply that holds no `LEDGER` block, such as the answer that no Case fixed the cause of a lesson, and the hook sends the agent on at the end of that answer too when every other condition holds. The flag `stop_hook_active` and the refusals of other hooks neither silence it nor send it on; with the flag set and a transcript it cannot read, it exits 0. The ledger hook tells each refused or held line and each reminder once a stretch, so the hook cannot loop. With no `prespec` line it stays silent and sends the agent nowhere. With the line, when a file under `cases/` that holds more than blank space was written after the last `prespec` mark, it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding. When no file under `cases/` that holds more than blank space was written after that mark, no Case has been built again on the findings yet — the reply wrote a defer or a lesson in answer to the report — and it sends the agent on with the loop after the findings: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit. A reply that opens with `STOP:` ends, for the case where only the person can go on. An error of the hook itself after it has read the payload exits 0 before `/pre-spec`, or when the hook cannot read the `prespec` line, and does not send the reply back; after `/pre-spec` it exits 2 with `onward: not checked: <error>` on stderr and the advice to go on, at most once a stretch, judged by its own refusal in the stretch alone.

## History

- 2026-10-14 shipped with GUPPI
