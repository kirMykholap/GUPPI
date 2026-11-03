---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, and from the transcript that a method names, found by the stamp of that session's spec.md and read in parts, never whole, leaves each other open W line open under Work with no Cases line, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, with the place of a text the question asks the person to judge, searched for in the files of the repository when the question names no path, and a quotation of it when it stands in a file, writes the answer and that place as its reading line, and opens no page but the Estimates of its open W lines and the file it quotes
method: by hand, the text of the skill file rendered from rule-skill-hi, or, at the Retro of the session that changes it, the new Render of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-11-03
origin: raw/2026-09-29/1134/ledger.md#case-508.1
sprint: migration
created: 2026-09-29
tags: [session, harness, workflow]
---

## Criterion

When:
The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

Then:
Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
**＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
**＋** Where the method reads the transcript of a session under `~/.claude/projects/` and its event came in an earlier session, it takes the stamp of that session from the first line of its `raw/<date>/<hi HHMM>/spec.md`, or of `vault/archive/<sprint>/<date>/<HHMM>/raw/spec.md` once the session is archived, opens the transcript under `~/.claude/projects/` whose name opens with that stamp, or the transcript of one of its agents in the folder `subagents/` inside the folder of the same name, searches it by a Grep with lines of context and reads only the parts around the hits.
**＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
**＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
**＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question. When that question asks the person to judge a text and names no path, the agent looks for the text by a Grep or a Glob over the files of the repository, such as `vault/wiki/brief.md`, the handoff of the session and the page of the Estimate. When the text is in a file of the repository, it names the path and the section of that file and quotes the part the question judges. When it finds no such file, it names the session by its date and the time of its `hi:` line and the reply that showed the text, and says in a plain sentence that it does not open that chat.
**＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result and the place it named for the text as its source, in a `LEDGER` block of the reply, which ends in text.
**－** It reads no transcript whole, and no transcript that the method of an open `W` line does not name.
**－** A session with no `spec.md`, neither `raw/<date>/<hi HHMM>/spec.md` nor `vault/archive/<sprint>/<date>/<HHMM>/raw/spec.md`, gives no stamp, and the `W` line of its reading stays open.
**－** An open `W` line whose reading cannot run now stays open under `## Work` and is no line under `## Cases`.
**－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
**－** The Frontier is still assembled with no page opened. The step that reads the open `W` lines opens the page of the Estimate of each of them and the transcript its method names. The step that puts the `A` lines opens the file it found or the question names, to quote it, and never a saved chat.
**－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

## Result

2026-11-03, Retro of session 1825, the new Render of rule-skill-hi in the Spec (vault/raw/2026-11-03/1825/spec.md, Case 1019.1, its two replace pairs) read against the Criterion of Case 1019.1: the W step reads from the brief, git log, git status and the files and commands the method names; where the method reads a transcript under ~/.claude/projects/ and its event came in an earlier session, it takes the stamp from the first line of spec.md, live under vault/raw/<date>/<HHMM>/ or archived under vault/archive/<sprint>/<date>/<HHMM>/raw/, opens the transcript whose name opens with it or an agent transcript in subagents/ inside the folder of the same name, searches it by a Grep with lines of context and reads only the parts around the hits, never the whole file; a session with no spec.md in either place leaves its line open; the A step says it does not open that chat; the other lines of the Criterion stand in the unchanged text of the Render

## History

- 2026-09-29 created · [[decision-case-508.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L30
- 2026-09-30 updated: the Criterion replaced whole — the Ask lines put to the person in the first reply, the answer written as the reading line (case 531.13) · [[decision-case-531.13]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1306/ledger.md#L45
- 2026-09-30 status: failed → passed · raw/2026-09-30/1736/ledger.md#L18
- 2026-10-03 updated: the Criterion replaced whole — /hi reads a moment of an earlier session from its transcript (case 613.2) · [[decision-case-613.2]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L2
- 2026-10-05 updated: the Criterion replaced whole — /hi reads no transcript, and an open Work line it cannot read becomes a Cases line (case 670.5) · [[decision-case-670.5]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/2103/ledger.md#L5
- 2026-10-08 updated: the Criterion replaced whole — an Ask line that waits for the close of a sprint, or the session after it, stays open and is not asked; the purpose set anew · [[decision-case-732]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/0213/ledger.md#L7
- 2026-10-10 updated: the Criterion replaced whole — the readings come with the Frontier, which at an opening is not the first reply · [[decision-case-769.3]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1913/ledger.md#L36
- 2026-10-12 updated: the Criterion replaced whole — an open W line of an Estimate of the live sprint page whose reading cannot run now stays open under Work and is no Cases line · [[decision-case-778]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1449/ledger.md#L8
- 2026-10-12 updated: the Criterion replaced whole — an open W line whose reading cannot run now stays open under Work and is no Cases line · [[decision-case-781.8]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1604/ledger.md#L28
- 2026-10-30 updated: the Criterion replaced whole — an Ask question that asks the person to judge a text names its place and quotes it when it stands in a file, and the reading line names that place · [[decision-case-921]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/0304/ledger.md#L36
- 2026-11-03 updated: the Criterion replaced whole — /hi reads the transcript that a method names, found by the stamp of its session and read in parts; the purpose set anew · [[decision-case-1019.1]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/1825/ledger.md#L12
