---
type: decision
case: "577"
status: archived
children: ["[[decision-case-577.1]]", "[[decision-case-577.2]]", "[[decision-case-577.3]]", "[[decision-case-577.4]]", "[[decision-case-577.5]]", "[[decision-case-577.6]]", "[[decision-case-577.7]]", "[[decision-case-577.8]]"]
origin: raw/2026-10-01/1441/ledger.md#case-577
sprint: migration
created: 2026-10-01
tags: [session, workflow, hooks, harness, ledger]
---

## Problem

After any `Stop` hook refuses a reply, Claude Code keeps `stop_hook_active` set until the person writes again. Every `Stop` hook reads that flag as "do nothing". When the run goes on from Plan Mode through Work Mode to Retro in one stretch, the reply that ends Retro writes no ledger line and nothing sends the agent to `/handoff`. The question was how to answer this, and how the checks that change keep themselves from looping.

## Recommend

- **How to deal with the silent end of Retro**
  - Recommended: (a) fix the checks on the path. They no longer trust the mark and keep themselves from looping by what they can see themselves, so at the end of Retro the readings reach the ledger and the agent is sent to `/handoff`, even in a long stretch.
  - Answer: (a), as recommended.
- **Whether to confirm the cause before the change**
  - Recommended: (a) take the transcript as enough. The Case states the cause as the transcript shows it, the tests cover a reply that ends with the mark on, and a live reading at the end of Retro after a long stretch confirms the fix.
  - Answer: (a), as recommended.
- **Which checks stop trusting the mark**
  - Recommended: (b) the check that sends the agent to `/handoff` and the ledger writer. The other four checks stay as they are.
  - Answer: (b), as recommended.
- **How the check that sends the agent to `/handoff` avoids looping**
  - Recommended: (a) once per stretch, by its own earlier message. It stops a reply only when its own message does not already stand in the transcript since the person's last message, and a stop by another check earlier in the stretch no longer silences it.
  - Answer: (a), as recommended.
- **How the ledger writer reports a refused line while the mark is on**
  - Recommended: (a) once per stretch, like the check that sends the agent to `/handoff`. With the mark on it writes the good lines, and it stops the reply to report a refused line or an error of its own only when its own message does not already stand since the person's last message. One module holds this judgment for both checks.
  - Answer: (a), as recommended.
- **Change**
  - Asked: on the finding of `/pre-spec` that a second faulty line in the same stretch would be lost without a word, the person chose to report each refused line once per stretch. The hook exits 2 when a refused line of the reply just finished is not already named in its own refusals of the stretch, and a repeat of the same line stays silent. An error of the hook itself and a missing `hi` stay once a stretch.
  - Taken: 577.3 and the rule text tell each refused line once in a stretch, and 577.5 to 577.8 point their exit to that rule.

## History

- 2026-10-01 created · raw/2026-10-01/1441/ledger.md#case-577
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
