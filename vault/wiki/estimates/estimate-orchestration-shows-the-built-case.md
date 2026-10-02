---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: A Case is built by case-guppi and shown by the main agent unchanged
method: by hand, the Cases of a session at its close, their context against the Agent calls and their showings against the SendUserFile calls of the transcript, and each request for a plain explanation against the Skill and SendMessage calls
checked: 2026-10-01
origin: raw/2026-09-24/1303/ledger.md#case-391.2
sprint: migration
created: 2026-09-24
tags: [session, workflow]
---

## Criterion

When:
The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
**＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
**＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
**＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
**＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer. In the same reply it writes the heading of the top-level Case with its name in Russian and, under it, one list with an item per Case and sub-case of the answer: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the Case creates or whose Criterion it replaces, or from the Estimate its `context` names as already checking the change. Then it writes one `ratification` with the ledger lines of every Case of the list as the answer holds them, and its own text after one horizontal rule. An answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
**＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it; a reply that shows a round and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
**＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
**＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
**－** The main agent writes no context of its own before the first question of a round.
**－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
**－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

## Result

2026-10-01, by hand, session 1237: the plan file stood with its title line (Write 12:48:59) before the first dispatch; each dispatch carried the Case id, the Frontier item, its source and the person's words, and nothing of a Case stood in the chat before its answer; each answer to a round and the person's question on a shown round went by SendMessage verbatim; the request to explain Q2 was answered by the main agent through wait-what with no SendMessage for a fact; each round was shown translated question by question with the agent's text after one rule; each Case was sent by SendUserFile with display render on cases/case-<N>.md, with the heading in Russian, one list per Case and sub-case with what done means and how it is checked, one ratification as the answer holds it, and own text after one rule; the Cases built again after /pre-spec were rebuilt by their case-guppi and ratified again; A1 and the W readings closed with no dispatch; ask-guppi once, at /pre-spec; the short-form defers written in English with no dispatch; not exercised: a refused showing

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
