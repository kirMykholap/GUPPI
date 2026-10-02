---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame and answers with it alone
method: "by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case, one Case with a create without a ref and one that changes a hook; the tokens and seconds of each dispatch in the estimate line"
origin: raw/2026-09-24/1303/ledger.md#case-391.1
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.

Then:
`case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
**＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
**＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
**＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
**＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
**＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification`, and nothing else.
**＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
**＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
**－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
**－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
**－** It writes no file and no ledger line.

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
