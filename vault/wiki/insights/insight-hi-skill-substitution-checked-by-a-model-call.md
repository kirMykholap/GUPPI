---
type: insight
pattern: "A `!` command of a skill is checked by a model call before it runs; when that call fails — a lapsed login, reported as the model unavailable — the substitution is refused and the Render: line comes back empty, while the SessionStart hook is not affected."
status: actioned
children: ["[[lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable]]", "[[lesson-hi-substitution-fails-when-the-login-has-lapsed]]", "[[lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier]]"]
severity: 0
addressed_by: "[[decision-case-439]]"
deferred_by: ["[[decision-case-448]]"]
origin: raw/2026-09-18/1252/ledger.md#L8
sprint: migration
created: 2026-09-18
tags: [harness, session, hooks]
---

## Pattern

Two lessons, one cause. At /hi of session 1119 the `!` substitution of `uv run guppi render --sync` was refused with "claude-opus-5[1m] is temporarily unavailable, so auto mode cannot determine the safety of Bash"; the lesson named the permission classifier's model. At the first /hi of session 1252 the same refusal came with the client's login prompt beside it, and a second /hi after /login ran whole. The check of a skill's `!` command is a model call, and the call fails when the login has lapsed; the older lesson saw the symptom, the newer the cause.

## Proposal

One sentence in `rule-skill-hi`: a refused `!` substitution at /hi is a lapsed login — the cure is `/login` and `/hi` again, not `render --check` by hand and not an allow entry for the command. A suggestion, not a decision.

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#L8
- 2026-09-18 updated: rejected — the check of a `!` command is the client's, the harness has no guard for a lapsed login, and the cure stands in the pattern and in lesson 1252; rule-skill-hi unchanged (case 246) · [[decision-case-246]]
- 2026-09-26 updated: child lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier added; addressed_by decision-case-439, later than decision-case-246, status actioned kept · raw/2026-09-26/1745/ledger.md#L2
- 2026-09-27 deferred · [[decision-case-448]]
