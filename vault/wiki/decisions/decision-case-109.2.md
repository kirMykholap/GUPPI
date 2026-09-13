---
type: decision
case: "109.2"
status: current
update: [rule-claude-md]
origin: raw/2026-09-13/ledger.md#case-109.2
sprint: migration
created: 2026-09-13
tags: [harness, render]
---

## Context

Pre-task of Case 103: two Renders and one schema name the date-level ledger or do not know the cascade. `rule-retro` (`draft`, Render → `.claude/skills/retro/SKILL.md`): line 39 `Ledger of today: !`cat "vault/raw/$(date +%F)/ledger.md"``, line 58 the revert patch at `raw/<date>/patch-<slug>.diff`. `rule-claude-md` (`draft`, Render → `CLAUDE.md`): line 59 "the `Stop` hook writes them into `vault/raw/<date>/ledger.md`". `insights/schema.md`: `archived` in the status list with no rule for when it is set (104.2 and 104.3 bring one); `lessons/schema.md` already says "Archived when its Insight is `actioned`".

## Problem

After 103.1 Retro reads a file the hook no longer writes; `CLAUDE.md` misstates the path; the Retro patch lands at the date level, which 100.1 moves with the date-level ledger and which future dates do not have. Renders are not edited by hand (`rule-governed-files-hook`).

## Given

`rule-retro`: Estimate `estimate-retro-loads` (`pending`); the Render is a skill, `$(date +%F)` a shell substitution; only the hook knows the session folder (`session_dir`), a shell does not — `vault/raw/$(date +%F)/*/ledger.md` reads the ledgers of every session of the day, and the date-level one while it exists; a session across midnight reads its own through the same glob on its `hi` date.
**＋** `rule-claude-md`: Estimate `estimate-claude-md-rendered` (`pending`); the Migration paragraph, line 59; the criterion of the Estimate is about the render reproducing the file, not about the text: `contract: same`.
**＋** `insights/schema.md` is a Rule-class file, slug `insights-schema`; its `status` row (17) and "The archive is not searched" (30) agree with 104.
**－** `rule-handoff`, `rule-spec-capture`, `rule-event-log` do not name the date-level ledger — checked by ask-guppi.

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-109.2
