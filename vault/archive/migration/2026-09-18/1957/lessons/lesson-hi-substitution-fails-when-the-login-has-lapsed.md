---
type: lesson
kind: knowledge
root_cause: the session's login had lapsed — the client checks a `!` command of a skill by a model call, and on a lapsed login that call fails as "unavailable"; the lesson of session 1119 named the classifier's model as the cause, the cause is the login; the fix is /login and /hi again, not `render --check` by hand, and not an allow entry for the command; the client's "auto mode" in the message is its name for that check, the session's defaultMode is plan
status: archived
source: the person's report at /hi of session 1252, 2026-09-18 12:52, with the local-command-stderr of that /hi
insight: "[[insight-hi-skill-substitution-checked-by-a-model-call]]"
origin: raw/2026-09-18/1252/ledger.md#L8
sprint: migration
created: 2026-09-18
tags: [harness, session, hooks]
---

## Trigger

at the first /hi of the session the skill's `!` substitution of `uv run guppi render --sync` failed with "claude-opus-5[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash" while the client showed its login prompt at the same moment; after /login a second /hi ran whole, both substitutions included

## Root cause

the session's login had lapsed — the client checks a `!` command of a skill by a model call, and on a lapsed login that call fails as "unavailable"; the lesson of session 1119 named the classifier's model as the cause, the cause is the login; the fix is /login and /hi again, not `render --check` by hand, and not an allow entry for the command; the client's "auto mode" in the message is its name for that check, the session's defaultMode is plan

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#L8
- 2026-09-18 updated: clustered by librarian under insight-hi-skill-substitution-checked-by-a-model-call · raw/2026-09-18/1252/ledger.md#L8
- 2026-09-18 archived · insight actioned
- 2026-09-18 archived · cleanup
