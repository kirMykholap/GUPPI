---
type: decision
case: "134"
status: current
update: [insight-session-vault-knowledge-not-loaded]
origin: raw/2026-09-14/1229/ledger.md#case-134
sprint: migration
created: 2026-09-14
tags: [harness, workflow]
---

## Context

An Insight of severity 5, `open` since 2026-09-12, five children. Pattern: a fact the vault holds does not reach the session that needs it — only `brief.md`, `CLAUDE.md`, the skills and the agent frames are loaded, and everything else waits for a read the agent must first think to make. The page's Proposal: a second channel beside the brief — the ledger tail at `/hi`, and a way for a Rule page to name the lessons that bear on it; prompt or hook, a Case of its own.

## Problem

The children fall into two groups, and each has a mechanical answer already. The first child (readings after the librarian invisible to the next `/hi`) is closed by `rule-ledger-tail` (101.2, `built`, `estimate-ledger-tail` `passed`; the `Tail:` line of `/hi`). The four heredoc children are closed by `rule-bash-guard` (127): the hook refuses instead of the agent remembering a lesson; the first live refusal today at 12:34. What stays open is the second half of the Proposal — "a Rule page names its lessons". Decide: is the Insight actioned, and what becomes of that half.

## Given

`insight-session-vault-knowledge-not-loaded`: `open`, `severity: 5`, children `lesson-readings-after-librarian-invisible-to-next-hi`, `lesson-vault-lesson-absent-at-the-moment-it-applies`, `lesson-heredoc-trap-hit-twice-with-its-lesson-live`, `lesson-heredoc-trap-hit-a-third-time-in-work-mode`, `lesson-heredoc-trap-hit-a-fourth-time-in-the-session-that-ratified-its-hook`; all `clustered`.
**＋** `rule-ledger-tail` `built`, `estimate-ledger-tail` `passed`: `/hi` prints the unmaterialized ledger tail — the answer to the first child.
**＋** `rule-bash-guard` `built`, `estimate-bash-guard` `passed` (the test of 127, the live refusal at 12:34 today) — the answer to the four heredoc children.
**＋** `insights/schema.md`: `addressed_by` is one decision slug, "the ratified decision that fixed the pattern, or rejected it (case 124)"; `## Addressed by` is derived by `generate` from the field (124.2).
**＋** The cascade of `generate` (104.2): the children of an actioned Insight go `archived`; `cleanup` moves the five lesson pages to the archive; `severity` is recomputed over the live children.
**＋** `actioned` is not an end state: a new lesson with the same root cause returns the Insight to `open`, the old children stay archived (schema.md).
**－** An Insight is not a Leaf: no `contract`, no Estimate; `generate` accepts an `update` of an Insight, not a `create` or `delete` (124.2).
**－** The first `update` of an Insight under 124: the `then` block carries `set` with `status` and `addressed_by`, and `change` for History.

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#case-134
