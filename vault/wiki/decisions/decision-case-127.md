---
type: decision
case: "127"
status: current
create: [rule-bash-guard]
update: [rule-hook-registry]
supersedes: [decision-case-120]
origin: raw/2026-09-14/1029/ledger.md#case-127
sprint: migration
created: 2026-09-14
tags: [hooks, harness, render]
---

## Context

`lesson-bash-tool-heredoc-escapes-interpreted` (H), `lesson-heredoc-trap-hit-twice-with-its-lesson-live` (L), `lesson-heredoc-trap-hit-a-third-time-in-work-mode` (M): a heredoc passed to the Bash tool has its backslash escapes interpreted, and the agent reaches for a heredoc first every session, with the lesson live. The Insight's Proposal — pages of a phase carry its traps — is Case 119's; the trap itself has a mechanical fix. (Case 120 as it stands.)

## Problem

A lesson the agent has to remember is not a rule. A `PreToolUse Bash` hook that refuses a command whose heredoc body carries a backslash escape — or refuses a heredoc that writes a file at all, pointing at Write and Edit — makes the trap impossible instead of remembered. (Case 120 as it stands.)

## Given

`rule-bash-guard` is a placeholder (`draft`, `deferred_by: [decision-case-120]`, no `kind`, `estimates` or `tags`: 4 `schema` and 1 `orphan` lint findings). `generate` fills a placeholder on a `create` and keeps its `deferred_by` (`generate.py:400`); a `supersedes` clears it. The slug is taken by the placeholder itself — that is the target.
**＋** `rule-harness` (`MOC`): children `rule-render-harness, rule-settings, rule-lint, rule-index, rule-governed-files-hook, rule-claude-md`; `rule-governed-files-hook` (`guppi/guard.py`) is the model: `PreToolUse` on `Edit|Write|MultiEdit`, a line in the event log before the refusal, exit 2 with the reason, never raises, exit 0 on an unreadable payload.
**＋** `rule-hook-registry` (`Leaf`, `built`, `estimate-hook-registry-rendered`): the Render's `PreToolUse` holds three matchers; a new matcher `Bash` is `contract: same`, as 111.2 was: the Estimate checks that the render reproduces the file, not which hooks it holds.
**＋** Today's case: `cat >> plan.md <<'EOF'` with the body of a Case failed with "unexpected EOF while looking for matching quote" — the second face of the same trap, a file written by a heredoc; Edit worked.
**－** Tags `hooks`, `harness`; no new tag.
**－** Not refused: a `<<<` here-string; a heredoc without a backslash whose output goes to a pipe or the screen; `python - <<'EOF'` with a clean body.
**－** The Frontier line F6 closes on this Case.

## Criterion

- [[estimate-bash-guard]] § case 127

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#case-127
