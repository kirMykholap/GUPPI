---
type: insight
pattern: A call that is not read-only — a ! command of a skill, an Agent or SendMessage call in plan mode — is checked by Claude Code's server-side classifier before it runs; when that server gives no verdict the call is refused, and the same call passes once the server answers again; a call that a permission rule allows needs no verdict.
status: actioned
children: ["[[lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable]]", "[[lesson-hi-substitution-fails-when-the-login-has-lapsed]]", "[[lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier]]", "[[lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier]]"]
severity: 0
addressed_by: "[[decision-case-679]]"
origin: raw/2026-09-18/1252/ledger.md#L8
sprint: migration
created: 2026-09-18
tags: [harness, session, hooks]
---

## Pattern

Four lessons, one cause. At /hi of sessions 1119 and 1252 the `!` substitution of `uv run guppi render --sync` was refused with the model reported unavailable; the second lesson took a lapsed login for the cause, since a /hi after /login ran whole. On 2026-09-26, in session 1b191eaf, /hi failed at every run: since client 2.1.282 the server-side classifier gives no verdict for a `!` substitution the person types, and a fresh /login did not help. On 2026-09-28, in session 1318, Agent and SendMessage calls in plan mode were refused the same way, and the same calls passed unchanged once the server answered again. The check is Claude Code's, made on its server before the call runs; the harness neither makes it nor sees why it fails. A call that a permission rule allows needs no verdict.

## Proposal

Rejected (case 679): the refusal comes from Claude Code's server, and the harness has nothing to fix. /hi gets past the check, since the `allowed-tools` of `rule-skill-hi` names its `!` commands and an allowed command needs no verdict.

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#L8
- 2026-09-18 updated: rejected — the check of a `!` command is the client's, the harness has no guard for a lapsed login, and the cure stands in the pattern and in lesson 1252; rule-skill-hi unchanged (case 246) · [[decision-case-246]]
- 2026-09-26 updated: child lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier added; addressed_by decision-case-439, later than decision-case-246, status actioned kept · raw/2026-09-26/1745/ledger.md#L2
- 2026-09-27 deferred · [[decision-case-448]]
- 2026-09-28 updated: child lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier added, reopened from actioned (synthesis) · raw/2026-09-28/1318/ledger.md#L41
- 2026-10-06 defer by decision-case-448 superseded · [[decision-case-679]]
- 2026-10-06 updated: rejected — the cause rewritten: the server-side classifier of Claude Code gives no verdict, not a lapsed login; the /login cure removed; the harness has nothing to fix (case 679) · [[decision-case-679]]
