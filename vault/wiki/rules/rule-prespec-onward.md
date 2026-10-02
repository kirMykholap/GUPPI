---
type: rule
kind: Leaf
purpose: Prevents Plan Mode from stopping where no person is needed, between the reply that acknowledges the last ratification and /pre-spec, and between the ratification of the Cases built again on its findings and the exit
status: draft
enforcement: hook
implementation_ref: [guppi/onward.py, guppi/ledger.py, guppi/casecheck.py, tests/test_onward.py, tests/test_ledger.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-prespec-onward-sends-the-agent-on]]", "[[estimate-prespec-onward-reads-the-decisions-of-the-session]]"]
origin: raw/2026-09-30/2356/ledger.md#case-561.5
sprint: migration
created: 2026-09-30
tags: [session, workflow, hooks, harness]
---

## Purpose

Prevents Plan Mode from stopping where no person is needed: between the reply that acknowledges the last ratification of the Frontier and `/pre-spec`, and between the ratification of the Cases built again on its findings and the exit. In Claude Code the end of a reply hands the turn to the person, and a reply that carries a `LEDGER` block ends in that text, so that the ledger hook writes it; so the agent cannot call `/pre-spec` or exit Plan Mode in that reply. This hook, `uv run guppi onward --plan` on `Stop`, sends the agent on in the same turn, as `rule-retro-onward` does after Retro (case 561.5). It judges only the state of files, of the payload and of the transcript — the `hi` and `prespec` marks of the session in the event log, `spec.md`, the open lines under `## Cases` of `frontier.md`, the files under `cases/` against the times of the decision lines in `ledger.md` and in every reply of the main agent in the transcript, each at the time of its record, the reply that ended counted as now (cases 597.2, 604), its own refusals and those of the ledger hook in the stretch, from the person's last message, and the first word `STOP:` of the reply — and counts nothing. It fires once a stretch, and once more after each reply that the ledger hook refused: the agent answers that refusal with a reply that writes the refused lines again, a reply that must end. The flag `stop_hook_active` and the refusals of other hooks neither silence it nor send it on; with the flag set and a transcript it cannot read, it exits 0 (case 597.1). The ledger hook tells each refused line once a stretch, so the hook cannot loop. With no `prespec` line it sends the agent to `/pre-spec`; with the line it sends the agent to run the check and exit Plan Mode, where the hook of `rule-prespec-hook` refuses the exit while the check prints a finding. A reply that opens with `STOP:` ends, for the case where only the person can go on. An error of the hook itself after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to go on, at most once a stretch, judged by its own refusal in the stretch alone (case 597.1).

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
