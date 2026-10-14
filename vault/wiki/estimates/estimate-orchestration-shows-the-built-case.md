---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: A Case is built by case-guppi and shown by the main agent unchanged
method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-10-14
origin: raw/2026-09-24/1303/ledger.md#case-391.2
sprint: migration
created: 2026-09-24
tags: [session, workflow]
---

## Criterion

When:
The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
**＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
**＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
**＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

Then:
The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
**＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
**＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
**＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
**＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
**＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
**＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
**＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
**＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
**＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
**＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
**＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
**＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
**＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
**－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
**－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
**－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
**－** The heading carries no name of the main agent's own and not the words of the Frontier item.
**－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
**－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
**－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
**－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.

## Result

2026-10-14, session 0232, the new Render of rule-orchestration in spec.md of session 0232: the Work Mode sentence gives the dispatch of a new top-level Case under the id that `uv run guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the hi: line, as the replaced Criterion line says; this session changes no other sentence the Criterion reads

## History

- 2026-09-24 created · [[decision-case-391.2]]
- 2026-09-25 renamed from `estimate-case-protocol-checks-its-frame` · [[decision-case-419.1]]
- 2026-09-25 updated: renamed; the Criterion replaced whole — the Case built by case-guppi and shown unchanged (case 419.1) · [[decision-case-419.1]]
- 2026-09-25 status: pending → failed · raw/2026-09-25/1654/ledger.md#L25
- 2026-09-26 updated: the Criterion replaced whole — the Case the person answers is the answer unchanged; a showing the Stop comparison refuses is followed by the answer shown unchanged (case 435) · [[decision-case-435]]
- 2026-09-26 updated: the Criterion replaced whole — the prose translated for the chat, every showing whole, a changed Case through its case-guppi, the short form in English (case 441.2) · [[decision-case-441.2]]
- 2026-09-27 updated: the Criterion replaced whole — a round shown translated, the answers passed verbatim, no step of confirmation (case 443.3) · [[decision-case-443.3]]
- 2026-09-27 updated: the Criterion replaced whole — the Case sent as the file the hook writes, a short Russian text and the ratification in the chat, nothing retyped (case 452.4) · [[decision-case-452.4]]
- 2026-09-27 updated: the Criterion replaced whole — a round is shown in Russian line by line, in the form of grill-me (case 458) · [[decision-case-458]]
- 2026-09-27 updated: the Criterion replaced whole — the context of a first round shown translated before its first question (case 466.2) · [[decision-case-466.2]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/0000/ledger.md#L34
- 2026-09-28 updated: the Criterion replaced whole — a request for a plain explanation is answered by the main agent with the skill wait-what, and case-guppi gives only a fact, under a Fact line that is not a round (case 477.3) · [[decision-case-477.3]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/2000/ledger.md#L24
- 2026-09-29 updated: the Criterion replaced whole — a round shown with each quotation in its blockquote (case 524.3) · [[decision-case-524.3]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1736/ledger.md#L40
- 2026-09-30 deferred · [[decision-case-560]]
- 2026-10-01 updated: the Criterion replaced whole - the showing is one list with what done means and one ratification; a Case with no such Estimate goes back to its case-guppi; a refused round is shown again with nothing before it; the defer of case 560 retired (case 561.9) · [[decision-case-561.9]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L34
- 2026-10-02 renamed from `estimate-case-protocol-shows-the-built-case` · [[decision-case-595.11]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the showing as orchestration.md sets it (case 595.11) · [[decision-case-595.11]]
- 2026-10-02 status: pending → failed · raw/2026-10-02/2049/ledger.md#L30
- 2026-10-03 status: failed → failed · raw/2026-10-03/0115/ledger.md#L18
- 2026-10-03 deferred · [[decision-case-617]]
- 2026-10-04 deferred · [[decision-case-622]]
- 2026-10-04 status: failed → passed · raw/2026-10-04/0112/ledger.md#L9
- 2026-10-04 updated: the Criterion replaced whole — ask-guppi only at pre-spec, one run per top-level Case, asked again only to confirm its findings (case 634.3) · [[decision-case-634.3]]
- 2026-10-05 status: pending → passed · raw/2026-10-04/2245/ledger.md#L17
- 2026-10-05 updated: the Criterion replaced whole — the Case is shown from the summary of case-guppi, the file written by case-guppi, another Case asked about from the Other Case line, and a round known by no Built and no Fact first line (case 645.6) · [[decision-case-645.6]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/1343/ledger.md#L36
- 2026-10-05 updated: the Criterion replaced whole — the heading of a showing is the id and the name of the Case line of the summary, translated (case 662.2) · [[decision-case-662.2]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.10]]
- 2026-10-05 updated: the Criterion replaced whole — ask-guppi only at pre-spec, one run over the whole plan, asked again only to confirm its findings; the method a reading of the new Render in the Spec at Retro (case 674.2) · [[decision-case-674.2]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/2103/ledger.md#L22
- 2026-10-07 updated: the Criterion replaced whole — a round or a Case with a layout fault is not shown again, and the Context label of a round in a batch names its Case · [[decision-case-699.4]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L44
- 2026-10-07 updated: the Criterion replaced whole — an answer that opens with Dropped is no round, and the drop of a Case not ratified goes to its case-guppi, the agent waiting for its answer before it goes on with the item · [[decision-case-701.4]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0425/ledger.md#L23
- 2026-10-07 updated: the Criterion replaced whole — a change the person drops on a ratified Case goes to its case-guppi, and the Case is shown and ratified again with the same lines (case 705.2) · [[decision-case-705.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0636/ledger.md#L36
- 2026-10-14 updated: the Criterion replaced whole — in Work Mode a new Case replaces the sub-case of a ratified Case that must change, and only that sub-case leaves the Spec (case 806.1) · [[decision-case-806.1]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L24
- 2026-10-14 updated: the Criterion replaced whole — the Work Mode dispatch names guppi caseid --next with --session and the stamp of the hi: line · [[decision-case-812.2]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/0232/ledger.md#L13
