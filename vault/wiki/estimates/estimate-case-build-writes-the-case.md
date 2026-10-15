---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: case-guppi asks about the forks of an item in rounds by the skill grill-me, then builds the Case against the vault and its frame, writes it into its file and answers with a short summary, empties the file of a Case it drops, and undoes a change the person dropped on a ratified Case
method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the tokens and seconds of each dispatch of case-guppi in that session, when there was one, in the estimate line
checked: 2026-10-14
origin: raw/2026-09-24/1303/ledger.md#case-391.1
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
**＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
**＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
**＋** Or, in Work Mode, the main agent dispatches it with the id of a new top-level Case, the path of the file of a ratified Case of the approved Spec, the sub-case of it that must change and the reason.

Then:
`case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
**＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
**＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
**＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
**＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
**＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
**＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
**＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
**＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
**＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
**＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it builds that behaviour as a new top-level Case beside it, in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `.guppi/guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
**＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
**＋** Dispatched in Work Mode with a ratified Case and the sub-case of it that must change, it reads the file of that Case whole and builds under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand: each page change, task and Estimate of that sub-case that still holds, with the change.
**＋** Each decision line of that new Case carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases, and the file of the ratified Case stays as it is.
**＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
**＋** In Work Mode a round may also come when it builds a new Case that replaces a sub-case of a ratified Case.
**＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
**＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
**＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
**－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
**－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
**－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
**－** It does not write the whole Case again to fix a finding, make a change or undo a change.
**－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
**－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
**－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
**－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.

## Result

2026-10-14, Retro, the new Render of rule-case-build in raw/2026-10-13/2118/spec.md (Case 806.2) read against the Criterion: 5 replace anchors stand once each, the description line included; 31 Criterion lines met — the Work Mode dispatch with the file, the sub-case and the reason, the file read whole, a new top-level Case holding each replaced sub-case whole with supersedes marks, never the ratified Case under its own number; the guard of guppi/ratified.py and the round-form judgment of guppi/casecheck.py bear out the two lines that name code

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
- 2026-10-07 updated: the Criterion replaced whole — case-guppi undoes a change the person dropped on a ratified Case and answers with the summary again (case 705.1) · [[decision-case-705.1]]
- 2026-10-07 status: pending → failed · raw/2026-10-07/0636/ledger.md#L37
- 2026-10-07 updated: the method reads the Render of rule-case-build against the Criterion at the Retro of the session that changes it, with the tokens and seconds of that session's dispatches; the Criterion written back unchanged; pending again (case 716) · [[decision-case-716.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/1804/ledger.md#L22
- 2026-10-07 updated: the Criterion replaced whole — a second behaviour of a ratified Case is a new Case beside it, and the file of a ratified Case left behind is not emptied (case 725.1) · [[decision-case-725.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/2114/ledger.md#L23
- 2026-10-08 updated: the Criterion replaced whole — the change another Case needs is a pointer to an Estimate of the Case that names it, when that Estimate already makes its promise (case 730.3) · [[decision-case-730.3]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/0050/ledger.md#L15
- 2026-10-14 updated: the Criterion replaced whole — in Work Mode case-guppi builds a new Case that replaces the sub-case of a ratified Case, never that Case under its own number (case 806.2) · [[decision-case-806.2]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L25
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
