---
type: decision
case: "458"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-orchestration-shows-the-built-case]]"]
origin: raw/2026-09-27/1819/ledger.md#case-458
sprint: migration
created: 2026-09-27
tags: [session, workflow, ledger]
---

## Context

When `case-guppi` has a fork open, it answers with a round of questions in the form of `.claude/skills/grill-me/SKILL.md`. Each question opens with `❓ **Qn** - **<title>**:` and closes with a `➡️` line that holds the recommended answer. The main agent translates the round into Russian and shows it. In session 1819, for Case 457, the main agent rebuilt the rounds into its own bold headings and a "Recommendation" line, and the markers were gone (`lesson-case-show-grill-round-reformatted-in-translation`). The Render of `rule-case-protocol` says only that a round is shown "translated into Russian, slugs, paths and quotations unchanged". It names no form to keep, and no hook reads a round: `casecheck --subagent` does not check or store an answer that has no Case heading, and the `Stop` hook compares only Cases.
In the rounds, the person chose three answers. The rule is text only, with no hook. The round is kept line by line. The promise is the replaced Criterion of `estimate-orchestration-shows-the-built-case`, whose round line already speaks of the showing. Its purpose is that a built Case is shown unchanged, and its method is by hand on the showings of a session, so its method stays. The Render sentence "In the chat one horizontal rule at most, after the Case or its last sub-case" would forbid a horizontal rule after a round, so the Case changes it too. `estimate-case-protocol-loaded` promises only that the file equals the Render, so it is not touched (case 378.5). `estimate-language-followed` speaks of the language of a round, not its form, so it stays as it is. `.claude/skills/grill-me/SKILL.md` and `.claude/agents/case-guppi.md` already write the form, so they do not change. No `create`, so no vault query ran.

## Problem

The main agent can meet the rule and still lose the form of a round: it translates the round but rebuilds its questions into its own headings. The person then sees the questions without the `❓ **Qn**` and `➡️` markers. The agent's recommended answer also no longer stands apart from the question. No sentence of the vault tells the main agent to keep that form.

## Given

`rule-case-protocol` — its Render, the paragraphs "Who builds a Case" and "Language", where a round is shown
**＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
**＋** `estimate-orchestration-shows-the-built-case` — the promise of the showing, its Criterion replaced whole
**＋** `.claude/agents/case-guppi.md` — the agent that builds a Case and writes a round
**＋** `.claude/skills/grill-me/SKILL.md` — the form of a question in a round
**＋** `rule-case-check` — the hooks that write the file of a Case and compare its showing
**＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a Case that the main agent sends
**＋** `.claude/agents/ask-guppi.md` — the vault query the main agent dispatches at pre-spec

## History

- 2026-09-27 created · raw/2026-09-27/1819/ledger.md#case-458
