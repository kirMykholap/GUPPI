---
type: decision
case: "443.1"
status: current
create: ["[[rule-skill-grill-me]]", "[[estimate-skill-grill-me-asks-in-rounds]]"]
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-09-26/2300/ledger.md#case-443.1
sprint: migration
created: 2026-09-26
tags: [harness, workflow, sprint]
---

## Context

Today the main agent takes up a Frontier item that needs a decision and dispatches `case-guppi` with the person's words. `case-guppi` reads the vault and the frame and answers with the Case. When the words do not give a choice, it answers with one question alone and no Case heading. Forks that the person would want to discuss are found only when the Case is shown, so there is no time to discuss them first. The person has long wanted `/grill-me` adapted to this. `/grill-me` asks in rounds: numbered questions, each with a recommended answer, then a wait for the answers. It stands as `.claude/skills/grill-me/SKILL.md`, and no rule page governs it. The Closed section of the sprint says it is kept without a page. Two of its sentences do not fit `case-guppi`. One tells the agent to dispatch a sub-agent for a fact, and `case-guppi` cannot dispatch. The other makes the user's word the only confirmation, but for `case-guppi` the showing of the Case and its ratification are the confirmation. The Render of `rule-case-build` has `case-guppi` answer with that one question alone. The Render of `rule-case-protocol`, `vault/wiki/case-schema.md`, has the main agent put a heading-less answer to the person as a question.

The vault query on `rule-skill-grill-me` gives this. Exists: none. Near: `rule-skill-hi` is the rule page of another skill and the pattern for this one. `rule-case-build` governs the agent that will load the skill. `rule-orchestration`, deferred by its decision, would move the triage of a Frontier item and the dispatch out of `case-schema.md` into a rule of its own. This Case does not take that defer up: it changes the triage text where it stands today. Missing: a page that governs `.claude/skills/grill-me/SKILL.md`. Rules: `rule-rules-schema` requires `governs`, `render_mode`, a `## Render` and an Estimate on a render rule. `rule-render-harness` and `rule-governed-files-hook` make the page the one source of the file. Tags: `harness`, `workflow`. The slug `rule-skill-grill-me` is free, and no archived page carries it.

The frame gives this. The `skills` field of a subagent's frontmatter puts the full text of a skill into the subagent's context at startup. It works with `tools: Read, Grep, Glob` and needs no Skill tool. It does not work for a skill with `disable-model-invocation: true`, and `grill-me` has none (https://code.claude.com/docs/en/sub-agents.md, as the person gave it). The sentence of the sprint's Closed section on `/grill-me` would become false, so 443.1 replaces it on `entity-sprint-migration`, and `vault/wiki/sprint.md` is rendered again. The `SubagentStop` check of `rule-case-check` does not check or store an answer with no Case heading. If a round follows a Case the agent already built, the check takes that earlier Case again and stores the same text, so a round breaks nothing there. The question template of the skill becomes an indented code block. The chat form of a Case cannot carry a fence inside a fenced value, and that limit is a Frontier item of its own. `estimate-language-followed` is not touched: a round shown in Russian is chat with the owner, as its Criterion says. `estimate-case-protocol-case-form` reads the Cases shown, and a round is no Case. `estimate-case-protocol-loaded` promises only that the file equals the Render. The Case splits by promise: the skill, the agent's answer and the main agent's showing are three Estimates.

## Problem

How `case-guppi` discusses the forks of a Frontier item with the person before it builds the Case, and where the rules of that round live: in the skill, in the agent's instructions, or in the Case schema.

## Given

`rule-skill-grill-me` — the new rule page, the source of the skill's text
**＋** `.claude/skills/grill-me/SKILL.md` — the skill it renders
**＋** `estimate-skill-grill-me-asks-in-rounds` — the promise of the skill
**＋** `rule-plan-mode` — the parent of the new page
**＋** `rule-render-harness` — `uv run guppi render` and its `--check`
**＋** `entity-sprint-migration` — the Closed section, which names `/grill-me` as kept without a page
**＋** `vault/wiki/sprint.md` — rendered from `entity-sprint-migration`

## History

- 2026-09-27 created · raw/2026-09-26/2300/ledger.md#case-443.1
