---
type: decision
case: "561"
status: archived
children: ["[[decision-case-561.1]]", "[[decision-case-561.2]]", "[[decision-case-561.3]]", "[[decision-case-561.4]]", "[[decision-case-561.5]]", "[[decision-case-561.6]]", "[[decision-case-561.7]]", "[[decision-case-561.8]]", "[[decision-case-561.9]]", "[[decision-case-561.10]]", "[[decision-case-561.11]]", "[[decision-case-561.12]]", "[[decision-case-561.13]]", "[[decision-case-561.14]]"]
origin: raw/2026-09-30/2356/ledger.md#case-561
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, hooks, ledger, render]
---

## Problem

After `/pre-spec` the main agent has no rule for the loop over the findings. It passes on answers one by one, runs `ask-guppi` again on each call, and asks its own questions in a shape of its own. Before the Spec it stops for questions with only one possible answer. Its exit from Plan Mode is not tied to a clean check. It shows a Case without saying what done means. And it reads the pages itself to discuss an item. The question is how the main agent runs from the Frontier to the approved Spec, in the texts that govern it today.

## Recommend

- **Where do the main agent's rules live?**
  Recommended: (a) a rule of its own for the main agent, `rule-orchestration`, loaded by `/hi` in place of `case-schema.md`, with `case-guppi` alone reading `case-schema.md`.
  Answer: (a). Carried out in a later session, as the later question on the size of this session decided.
- **What happens after the pre-spec findings?**
  Recommended: (a) one gathered loop. The main agent sorts the findings, sends the fixes that need no answer at once in one message, waits quietly for every answer, gathers every question into one numbered list in the grill-me shape, sends the answers back, and shows all the rebuilt Cases in one reply for one ratification.
  Answer: (a).
- **Which of the main agent's own questions take the grill-me shape?**
  Recommended: (a) every question the main agent asks the person itself, at pre-spec, at `/hi` and at a stop of Work Mode.
  Answer: (a).
- **What does the reply before ratification hold?**
  Recommended: (a) the file and its path, one list of the Case and its sub-cases by name, a short answer under each name on what done means and how it is checked, and the ledger lines; the main agent asks `case-guppi` when a Case gives no such answer.
  Answer: (a).
- **How does every Case answer "what does done mean"?**
  Recommended: (a) every Case creates or changes an Estimate, or names the Estimate that already checks the change and says why its Criterion stands; with neither, `case-guppi` asks in a round what the Estimate will check.
  Answer: (a).
- **Does the main agent ask before `/pre-spec`?**
  Recommended: (a) run it at once when no line under `## Cases` is open.
  Answer: (a).
- **What blocks leaving Plan Mode?**
  Recommended: (a) the hook on the exit runs the mechanical check itself and refuses while it prints a finding; a note does not block.
  Answer: (a). The person added the order: the skill runs the check and, when it is clean, `ask-guppi`; the hook makes sure the check is clean, and the skill itself can be shortened.
- **Does the main agent call `/pre-spec` again after the rebuilt Cases?**
  Recommended: (a) no second call: after the rebuilt Cases are ratified, the main agent runs the check alone, fixes what it prints and exits Plan Mode, and the hook runs the check again at the exit.
  Answer: (a).
- **How is this item split?**
  Recommended: (a) one Case with one sub-case per promise.
  Answer: (a).
- **Where does the text both agents need go?**
  Recommended: (b) the parts both agents need in a third small file of its own rule, loaded by `/hi` and read by `case-guppi`; the main agent's file for what it alone does; `case-schema.md` for the form of a Case.
  Answer: (b), agreed. The person had first asked whether option (a) duplicated text and why `case-guppi` would read the orchestration text. The question was asked again with this option. Carried out in a later session.
- **What happens to the checks of the behaviours that move?**
  Recommended: (a) new Estimates on `rule-orchestration` for the behaviours that move, the old ones withdrawn, and the check of the loaded file rewritten.
  Answer: (a). Carried out in a later session.
- **What form does the list in the reply take?**
  Recommended: (a) one heading, one list with an item per sub-case and its line on what done means, and one block of ledger lines; the two hooks that read a showing learn this form.
  Answer: (a).
- **Does the whole item stay in this session?**
  Recommended: (b) the behaviours now, in the texts where they stand today; the split into three files and the move of the checks in a later session.
  Answer: (b), agreed. The decisions on where the rules live and on the three files stand and are carried out later.
- **How does `/pre-spec` start with no question?**
  Recommended: (a) a `Stop` hook sends the agent on, in the same way as the hook after Retro: once, after the reply that leaves no Case open, with the ledger lines already written.
  Answer: (a), agreed.

## History

- 2026-10-01 created · raw/2026-09-30/2356/ledger.md#case-561
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
