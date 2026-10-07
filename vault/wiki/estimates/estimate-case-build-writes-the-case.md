---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame, writes it into its file and answers with a short summary, and empties the file of a Case it drops
method: "by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case written into its file and a summary, one Case with a create without a ref, one that changes a hook, a Case the hook sent back and fixed by Edit, a change the person asked for on one sub-case, made by Edit of that sub-case, and a Case dropped by a message of the main agent, its file emptied and its answer opening with Dropped, the file written in Plan Mode with no prompt; the tokens and seconds of each dispatch in the estimate line"
checked: 2026-10-07
origin: raw/2026-09-24/1303/ledger.md#case-391.1
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
**＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
**＋** Or the main agent sends it by `SendMessage` the drop of the Case it built.

Then:
`case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
**＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
**＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
**＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
**＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
**＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
**＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
**＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
**＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
**＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
**＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
**＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way.
**－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
**－** It does not write the whole Case again to fix a finding or make a change.
**－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
**－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
**－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case included, and no ledger line.
**－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`: sent its drop, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.

## Result

2026-10-07, Retro, not read: the Criterion of case 701.3 adds the drop, which reaches .claude/agents/case-guppi.md only at the librarian's render after this session, and no Case with a create without a ref, no Case the hook sent back and fixed by Edit and no change on one sub-case came up; live dispatches of session 0425 in Plan Mode, each file written with no permission prompt by the person's word: case 701 round 78789 tokens 186.0 s, round 84559 tokens 42.3 s, built 164892 tokens 497.3 s, built again on the findings 212248 tokens 413.7 s; case 702 round 85031 tokens 234.2 s, round 105696 tokens 84.7 s, round 122763 tokens 59.6 s, built 147670 tokens 173.8 s, built again 153889 tokens 44.3 s; C4 round 80320 tokens 169.0 s, a Fact with no Case 81484 tokens 13.2 s

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
- 2026-10-05 updated: the Criterion replaced whole — case-guppi writes its Case into its file in permissionMode acceptEdits, fixes it by Edit and answers with a summary; the purpose and the method follow (case 645.1) · [[decision-case-645.1]]
- 2026-10-05 updated: the Criterion replaced whole — the summary carries a line **Case:** with the id and the name of the top-level Case as the file heads it (case 662.1) · [[decision-case-662.1]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.9]]
- 2026-10-07 updated: the Criterion replaced whole — case-guppi runs in permissionMode auto; the other lines stand (case 698) · [[decision-case-698.1]]
- 2026-10-07 status: pending → failed · raw/2026-10-07/0211/ledger.md#L40
- 2026-10-07 updated: the Criterion replaced whole — case-guppi empties the file of a Case it drops and answers with a first line Dropped (case 701.3) · [[decision-case-701.3]]
- 2026-10-07 status: pending → failed · raw/2026-10-07/0425/ledger.md#L24
