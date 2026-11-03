---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-hi]]"
purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, leaves each other open W line open under Work with no Cases line, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, with the place of a text the question asks the person to judge, searched for in the files of the repository when the question names no path, and a quotation of it when it stands in a file, writes the answer and that place as its reading line, and opens no page but the Estimates of its open W lines and the file it quotes
method: by hand, the text of the skill file rendered from rule-skill-hi, or, at the Retro of the session that changes it, the new Render of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness, workflow]
core: true
---

## Criterion

When:
The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

Then:
Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
**＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
**＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
**＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
**＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
**＋** When that question asks the person to judge a text and names no path, the step that puts the `A` lines looks for the text by a Grep or a Glob over the files of the repository, such as `vault/wiki/brief.md`, the handoff of the session and the page of the Estimate. When the text is in a file of the repository, the agent names the path and the section of that file and quotes the part the question judges. When it finds no such file, it takes the text as one shown only in the chat of an earlier session: it names that session by its date and the time of its `hi:` line and the reply that showed the text, and says in a plain sentence that it cannot open that chat.
**＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result and the place it named for the text as its source, in a `LEDGER` block of the reply, which ends in text.
**－** It reads no transcript of an earlier session.
**－** An open `W` line whose reading cannot run now stays open under `## Work` and is no line under `## Cases`.
**－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
**－** The Frontier is still assembled with no page opened. Only two steps open pages: the step that reads the open `W` lines opens the page of the Estimate of each of them, and the step that puts the `A` lines opens the file it found or the question names, to quote it. Neither opens a saved chat.
**－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
