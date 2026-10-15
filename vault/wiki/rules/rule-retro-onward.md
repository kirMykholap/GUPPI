---
type: rule
kind: Leaf
purpose: Prevents the run from stopping between the reply that ends Retro and /handoff, where no person is needed
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/onward.py, .guppi/guppi/ledger.py, .guppi/tests/test_onward.py, .guppi/tests/test_ledger.py, .claude/settings.json]
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-onward-sends-the-agent-to-the-handoff]]", "[[estimate-retro-onward-exits-2-on-an-error]]"]
origin: raw/2026-09-29/2024/ledger.md#case-531.9
sprint: migration
created: 2026-09-29
tags: [session, workflow, hooks, harness]
core: true
---

## Purpose

Prevents the run from stopping between the reply that ends Retro and /handoff, where no person is needed. In Claude Code the end of a reply hands the turn to the person, and the ledger hook writes the lines of a reply only when it ends; so Retro ends one reply with its `LEDGER` block, and this hook sends the agent on to `/handoff` in the same turn (case 531.9). It judges only the state of files, of the payload and of the transcript — the mark `retro` of the session in the event log, the absence of `handoff.md`, its own refusals and those of the ledger hook after the person's last message in the transcript, and the first word `STOP:` of the reply — and counts nothing. It fires once a stretch, from one message of the person to the next, and once more after each reply that the ledger hook refused: the agent answers that refusal with a reply that writes the refused record lines again, a reply that must end — or, when only lines that are no record were refused, with a reply that writes none and calls `/handoff` itself (case 695.2) —, and the run once stopped there (in session 1834, case 596). The ledger hook tells each refused line once a stretch, so the hook cannot loop. A refusal of another `Stop` hook earlier in the stretch does not silence it, and neither does the flag `stop_hook_active`, which Claude Code keeps set from that refusal until the person's next message (as the transcript of session 1237 shows); with the flag set and a transcript it cannot read, it exits 0. The stretch and the refusals in it are judged by `.guppi/guppi/ledger.py`, whose function of the stretch the ledger hook calls too (cases 577.1, 596). An error of the hook itself after it has read the payload — an exception while it reads the reply, the session folder, the event log or the transcript — exits 2 with `onward: not checked: <error>` on stderr and the advice to commit the session folder and call `/handoff` if Retro has ended and `handoff.md` does not stand, so the agent sees it, before Retro too; once its own refusal stands in the stretch it exits 0, and so it does with `stop_hook_active` set when it cannot tell whether one stands, so this too fires at most once a stretch (cases 555.3, 577.2). A deliberate stop is a reply that opens with `STOP:`, on a condition of `rule-where-to-stop`.

## History

- 2026-09-30 created · [[decision-case-531.9]]
- 2026-09-30 estimate estimate-retro-onward-sends-the-agent-to-the-handoff added · [[decision-case-531.9]]
- 2026-09-30 updated: the hook exits 2 on its own error after the payload is read, with the advice to call /handoff (case 555.3) · [[decision-case-555.3]]
- 2026-09-30 estimate estimate-retro-onward-exits-2-on-an-error added · [[decision-case-555.3]]
- 2026-10-01 status: draft → built · cascade
- 2026-10-01 updated: the hook fires once a stretch, judged by its own refusal after the person's last message in the transcript; stop_hook_active no longer silences it (case 577.1) · [[decision-case-577.1]]
- 2026-10-01 updated: an error of the hook exits 2 once a stretch, judged by its own refusal in the transcript, which is among its reads (case 577.2) · [[decision-case-577.2]]
- 2026-10-01 status: built → draft · cascade
- 2026-10-02 updated: the hook sends the agent on again after each reply that the ledger hook refused; tests/test_ledger.py joins implementation_ref (case 596) · [[decision-case-596.1]]
- 2026-10-04 status: draft → built · cascade
- 2026-10-07 updated: the answer to a refusal of the ledger hook may write no line and call /handoff itself when only lines that are no record were refused · [[decision-case-695.2]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: each session stands in a bracket · [[decision-case-809]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
