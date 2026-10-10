---
type: decision
case: "477.2"
status: archived
create: ["[[rule-skill-wait-what]]", "[[estimate-skill-wait-what-re-pitches]]"]
origin: raw/2026-09-28/1318/ledger.md#case-477.2
sprint: migration
created: 2026-09-28
tags: [harness, workflow]
---

## Context

`estimate-agent-writing-followed` is `failed`. In session 0000 the person asked three times for a plain explanation of a round of `case-guppi`: once on Case 472 and twice on Case 473. The same happened twice on Case 467 and once on Case 476. Case 466.1 had already added a `**Context:**` paragraph to the first round, and the requests went on. The round of 473 was dense because it packed frame facts into the Context and the question bodies: case numbers, slug histories and words like "stamped writer". The main agent's own explanation, which the person understood, was different. It gave the problem in two points and one concrete example ("the hook refused 13 ledger lines, and they were lost"), and it said what each option changes. On 476 a before/after example answered the request. Today no text says who answers such a request. `rule-case-protocol` sends "a question or a change of the person on a shown Case" to `case-guppi`, but the main agent answered the requests itself. The Result of `estimate-orchestration-shows-the-built-case` records this.
The person decided in two rounds. A round gets a sentence in `rule-case-build`: the mechanism with an example, a before and after for each option, case numbers only in the `➡️` line, and an unknown term explained. A new Estimate reads that sentence against the text of a round. A request for a plain explanation becomes a legal skill, `wait-what`, taken from github.com/mattpocock/skills with its name kept. The person or the main agent starts it. Such a request is then its normal use, not a complaint, because requests like it can come without end. The main agent explains, and it asks the `case-guppi` of the Case only for a fact of the Case.
The vault's answer: no page or skill named `wait-what` or `explain` exists in `vault/wiki/`, `vault/archive/` or `.claude/skills/`. Every `create` carries a `ref`. `rule-skill-grill-me` is the pattern for the page of a skill.
The frame. The sentence of `rule-case-protocol` on a question on a shown Case, and the line of the Criterion of `estimate-orchestration-shows-the-built-case` that repeats it, would become false for a request for a plain explanation, so 477.3 changes both. `rule-case-build` tells `case-guppi` to answer every message with the Case or a round. A message of the main agent that asks for a fact would break that sentence, so 477.3 adds the answer to such a message. That answer opens with the line `**Fact:**`. Without the mark the main agent would show it as a round, because `rule-case-protocol` reads every answer with no Case heading as a round. So the sentence on a round and the line of the Criterion that repeats it except an answer with this mark. In that Criterion the `when` and three lines are changed on purpose, so the old wording of each is not carried: the line on the answers now excepts a request for a plain explanation, the line on a round now excepts an answer under `**Fact:**`, and the line on the request is new. Every other line is carried unchanged, "Russian" included, since Estimates keep this project's values (Case 476).
The hook of `rule-case-check` needs no new line. Its How it works already takes as the answer the newest output of `case-guppi` that holds a Case heading. After a built Case, a fact answer makes the hook check and store that Case again and write its file with the same text. Before any Case, it is neither checked nor stored.
Two Estimates stay untouched. The Criterion of `estimate-case-build-writes-the-case` states the form of a round and the messages that carry the person's words. The round sentence adds to that form, and the fact request is a message of the main agent outside its `when`, so no line of it becomes false. The person chose a separate promise for plainness. `estimate-skill-grill-me-asks-in-rounds` says the form of a round of `case-guppi` "is the promise of `estimate-case-build-writes-the-case`". Once 477.1 puts plainness into `estimate-case-build-writes-a-plain-round`, that line no longer names every promise on a round, but it is still true. It is not updated, because that Estimate is to be read in Work Mode of this session, and an update would push its reading to a later session (case 428.1).
The Render of `rule-agent-writing` does not change. Case 476.2 of this session changes three phrases of the Render of `rule-case-build` and one phrase in `## Who builds a Case` of `rule-case-protocol` ("which the agent shows translated into Russian line by line"). The anchors of this Case are other text. The Render of `rule-skill-wait-what` holds `{{chat_lang}}`: the render puts in the name of the language that the `## Render` of `rule-guppi-config` (476.1) sets, and both land at the same librarian's run. No reader in code changes.
Not done: no check counts the requests or reads a round by script. The Case file and the pages get no new sentence on plainness, because no request fell on them. The Render of `rule-agent-writing` stays as it is.

## Problem

The rounds of `case-guppi` carry frame facts where the person needs the mechanism and the effect of each option, so the person asks for a plain explanation again and again. Each request fails `estimate-agent-writing-followed`, and no text says who answers the request or in what form.

## Given

`rule-skill-wait-what` — the new Rule; its Render is the skill
**＋** `.claude/skills/wait-what/SKILL.md` — the skill, rendered in full from `rule-skill-wait-what`
**＋** `estimate-skill-wait-what-re-pitches` — the new promise
**＋** `rule-plan-mode` — the parent of the skills of Plan Mode
**＋** `vault/wiki/glossary.md` — the terms of the vault
**＋** `rule-guppi-config` — the code of `chat_lang` that the render puts in (case 476.1)
**＋** `.claude/agents/case-guppi.md` — the agent that holds the facts of its Case

## History

- 2026-09-28 created · raw/2026-09-28/1318/ledger.md#case-477.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
