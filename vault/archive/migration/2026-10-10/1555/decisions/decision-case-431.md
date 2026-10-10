---
type: decision
case: "431"
status: archived
update: ["[[estimate-case-protocol-case-form]]"]
origin: raw/2026-09-25/1654/ledger.md#case-431
sprint: migration
created: 2026-09-25
tags: [session, workflow]
---

## Context

`estimate-case-protocol-case-form` promises the form of a Case shown in the chat. It is read by hand over the Cases of a session at its close. The last reading, in session 0051, stands `failed`. The `context` of one Case held a count of items, and the Case was not about it. The `then` of another Case held a `－` line that described bookkeeping, not behaviour. `ask-guppi` found these faults at pre-spec, that is after the person had seen the Case.
Now the agent `case-guppi` builds each Case. Before the showing the hook `guppi casecheck --subagent` (`rule-case-check`) runs its answer through `judge` of `guppi/prespec.py` and through the check of the chat form. The script catches the order of sections and a missing section, anything extra in the `ratification` fence, a `then` item without a decision line, an Estimate without a `read` line. `check_frame` also catches a slug or path in `when` and `then` that `given` does not name. No check catches a count in `context`: the Purpose of `rule-case-check` and the docstring of `guppi/casecheck.py` say plainly that the script does not tell a count from other words. The script catches a bookkeeping `－` line only when it names a slug or path that `given` does not name. A line that names a thing of `given` but speaks of a record, not of behaviour, passes. The new finding of `judge` of this session, a second item of one slug, does not touch these faults. So only `case-guppi`'s own reading of the schema holds these faults, and only this Estimate checks them.
The Criterion of the Estimate nearly matches the Render of `rule-case-protocol`, but it has fallen behind it. `When:` says that the agent shows the Case. Now `case-guppi` builds the Case, and the main agent shows it unchanged. The line on `context` does not ask what the Render asks: that `context` says what `case-guppi` found in the frame. The other lines of the Criterion match the Render and stay as they are.
What the frame check showed. The Render of `rule-case-protocol` and the Purpose of `rule-case-check` stay true: the Case changes neither the form nor the checks. The Criterion of `estimate-case-check-sends-back-a-faulty-case` speaks of the findings of `judge` in general, and the Criterion of `estimate-case-build-writes-the-case` speaks of what `case-guppi` reads and what it answers. The Case does not touch them. `estimate-orchestration-shows-the-built-case` also holds the phrase on the agent's text after the horizontal rule. There it describes the same behaviour from the side of the showing, so it stays in both Estimates. The Case changes no code, and no second copy of one judgment appears. There is no `create` here, so no vault query is due. By the rule of this session a reading of an Estimate the session changes waits for the next session.

## Problem

The reading of the form of a Case stands `failed`. No check catches a count in `context` or a bookkeeping `－` line, and the Criterion has fallen behind the Render. It must be decided whether to keep the Criterion and read it again, to replace it, or to move a part of the form into a check.

## Given

`estimate-case-protocol-case-form` — the promise of the form of a Case shown in the chat
**＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — the form of a Case in the chat
**＋** `.claude/agents/case-guppi.md` — the agent that builds each Case
**＋** `rule-case-check` — the checks that run on an answer of `case-guppi` before it is shown

## History

- 2026-09-25 created · raw/2026-09-25/1654/ledger.md#case-431
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
