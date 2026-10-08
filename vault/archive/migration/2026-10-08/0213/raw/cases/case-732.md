## Case 732 — An Ask line waits for the close of a sprint

> **context:**
> At `/hi` the agent writes the brief's `Ask the person` lines under `## Ask` of `frontier.md` and puts each open `A` line to the person as a question in its first reply. Nothing checks whether the moment of that reading has come. At the `/hi` of session 0213 the line of `estimate-hi-writes-frontier` was put to the person, though its question names the `/hi` of the session after the close of a sprint, and no sprint has closed; it would come back the same way at every `/hi` until then. `rule-skill-hi` already lets a `W` line whose `method` names the session that closes a sprint, or the session after that close, stay open and wait (case 670.5); an `A` line had no such rule. The person chose to mirror that rule at `/hi`: an `A` line whose question names one of those two moments stays open under `## Ask` and is not asked until its moment, judged from the line as the brief gives it, with no page opened; the session after a close is the one whose brief opens its `Cases` with `open the next sprint`. The Criterion of `estimate-hi-takes-its-readings` says that each open `A` line is put to the person, so this Case replaces it whole and sets its `purpose` anew; its `method`, the skill text read against the Criterion, stays true. Retro, `rule-handoff` and `rule-brief` stay as they are: they still pass the line on each session, and a waiting line stays open, so `/carry` still carries it as an open `A` line. A Grep of `` `A` line|Ask line|A<n>|## Ask\b `` over `vault/wiki/` printed 20 files and over `.claude/` 5 files. Three hits stand as they are. The first is the sentence of `orchestration.md` that sets the form of the question of an open `A` line at `/hi`, which now covers only the lines that are put. The second is the Criterion of `estimate-orchestration-asks-in-the-grill-me-shape` speaks of the same question in an exception line: the question of an open `A` line at `/hi` keeps its own form. That Criterion stands, since it sets the form of a question that is put, not which lines are put. The third is the exception line of `estimate-hi-writes-frontier` that an `A` line stands open until its work is done, which a waiting line keeps. The rendered `.claude/skills/hi/SKILL.md` follows at the librarian's render, and no code reads this text.

> **problem:**
> `/hi` asks the person for a reading that the person cannot give before a sprint closes, and it asks again at every session until then.

> **recommend:**
> - **Where an Ask line that waits for a later moment is held back**
>   - Recommended: (a) at `/hi`: the line stays under `## Ask`, open, and is not put to the person until its moment, as the rule for a waiting `W` line does.
>   - Answer: agreed, (a).
> - **What the agent reads to judge whether the moment has come**
>   - Recommended: (a) the question on the Ask line as the brief gives it, with no page opened; a question that names no moment is asked as today.
>   - Answer: agreed, (a).
> - **Which moments make an Ask line wait, and how the agent knows a moment has come**
>   - Recommended: (a) the same two moments as the `W` rule: the line is asked at the `/hi` whose brief opens its `Cases` with `open the next sprint`, or in the session the person names as the one that closes the sprint.
>   - Answer: agreed, (a).
> - **Which check proves the change**
>   - Recommended: (a) replace the Criterion of `estimate-hi-takes-its-readings` whole, with an exception line for a waiting `A` line, and set its purpose anew.
>   - Answer: agreed, (a).

> **given:**
> `rule-skill-hi`: the rule whose Render is the skill `/hi`.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from `rule-skill-hi`.
> **＋** `estimate-hi-takes-its-readings`: its Criterion is replaced whole.
> **＋** `vault/wiki/brief.md`: the brief whose Next session gives the `Work` and `Ask the person` lines.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
> **＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. ``
>   - new: `` Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person: it is put at the `/hi` whose brief opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint; judge this from the line as the brief gives it, no page opened (case 732). ``
>   - change: `an Ask line whose question names the close of a sprint, or the session after it, stays open and is not asked until that session`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] update `estimate-hi-takes-its-readings`
>   - set:
>     ```
>     status: pending
>     purpose: Whether /hi takes, in its first reply, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, writes the answer as its reading line, and opens no page but the Estimates it reads
>     ```
>   - change: `the Criterion replaced whole — an Ask line that waits for the close of a sprint, or the session after it, stays open and is not asked; the purpose set anew`
> - [ ] read `estimate-hi-takes-its-readings`

> **ratification:**
> ```
> - decision[case 732][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 732][update][estimate-hi-takes-its-readings]{ref:rule-skill-hi}
> ```
