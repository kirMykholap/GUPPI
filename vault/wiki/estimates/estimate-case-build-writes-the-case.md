---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame and answers with it alone
method: "by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case, one Case with a create without a ref, one that changes a hook, and a change the person asked for on one sub-case of a Case with sub-cases, answered by that sub-case alone; the tokens and seconds of each dispatch in the estimate line"
checked: 2026-10-03
origin: raw/2026-09-24/1303/ledger.md#case-391.1
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
**＋** Or the hook of `rule-case-check` sends its answer back with findings.

Then:
`case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
**＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
**＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
**＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
**＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
**＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification`, and nothing else.
**＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
**＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
**－** Asked again after the hook of `rule-case-check` sent findings back, or by a message, it answers with the changed sub-cases alone, each from its heading to the fence of its `ratification`, when the parent's `context`, `problem` and `recommend` stand as they were; an item of `recommend` whose answer changed only that sub-case stands under its heading, and the hook writes the sub-cases into the file of the Case beside the parts that did not change.
**－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
**－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
**－** It writes no file and no ledger line.

## Result

2026-10-03, by hand at the Work readings of session 0317, the dispatches of case-guppi in Plan Mode read against their transcripts under subagents/ and the chat: `.claude/agents/case-guppi.md` carries model opus, effort medium, tools Read, Grep, Glob and skills [grill-me]; each of the three agents read vault/wiki/case-schema.md and vault/wiki/ratification.md whole as its first two calls; an item with a fork (611, 612, 613) was answered by a round in the grill-me form, the first round on each item opening with a `**Context:**` paragraph and the later rounds (612 Q6, Q7–Q9; 613 Q6–Q7, Q8–Q9) with none, then by the Case alone; Case 612 makes a create without a ref (`rule-sprint-close`) and its context gives the vault query of ask-guppi (exists none, near, rules, tags); Case 611 changes the Stop hook of guppi casecheck and its builder grepped `.claude/settings.json` for the Stop hooks, the context naming the six commands on Stop; no file and no ledger line written by case-guppi. Tokens and seconds per dispatch: 611 round 61,745 / 70.6 s, Case 99,751 / 200.4 s, rebuild after pre-spec 116,156 / 84.9 s; 612 round 74,257 / 158.4 s, Q6 76,735 / 19.8 s, Q7–Q9 91,142 / 67.5 s, Case 168,393 / 342.6 s, rebuild 179,771 / 70.5 s; 613 round 94,175 / 153.7 s, Q6–Q7 103,885 / 50.5 s, Q8–Q9 109,831 / 40.9 s, Case 184,880 / 468.4 s, rebuild 201,458 / 110.7 s

## History

- 2026-09-24 created · [[decision-case-391.1]]
- 2026-09-25 renamed from `estimate-frame-check-finds-a-contradiction` · [[decision-case-419.2]]
- 2026-09-25 updated: renamed; the Criterion replaced whole — case-guppi builds the Case; the method measures its cost (case 419.2) · [[decision-case-419.2]]
- 2026-09-25 ref `rule-frame-check` → `rule-case-build` · [[decision-case-425]]
- 2026-09-26 updated: the Criterion replaced whole — the answer is the whole Case in English (case 441.1) · [[decision-case-441.1]]
- 2026-09-27 updated: the Criterion replaced whole — case-guppi answers with a round of questions while a fork is open (case 443.2) · [[decision-case-443.2]]
- 2026-09-27 updated: the Criterion replaced whole — the first round on an item opens with a Context paragraph (case 466.1) · [[decision-case-466.1]]
- 2026-10-02 updated: the Criterion replaced whole - case-guppi reads case-schema.md and ratification.md (case 595.7) · [[decision-case-595.7]]
- 2026-10-03 updated: the Criterion replaced whole — the hook of rule-case-check judges the form of the questions of a round, not its context, and stores nothing of it (case 601.3) · [[decision-case-601.3]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/0317/ledger.md#L52
- 2026-10-04 updated: the Criterion replaced whole — asked again, case-guppi answers by its changed sub-cases alone while the parent's own parts stand (case 629.2) · [[decision-case-629.2]]
