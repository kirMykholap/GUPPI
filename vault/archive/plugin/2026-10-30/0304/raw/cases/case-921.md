## Case 921 — An Ask question at /hi names the place of the text it asks about

> **context:**
> At `/hi` the main agent puts each open `A` line of the Frontier to the person as a question: the Estimate by slug and the question as the brief gives it. When that question asks the person to judge a text, it names no place where the text stands and quotes none of it, and `/hi` reads no saved chat of an earlier session (case 670.5), so it cannot quote a reply that stood only in such a chat. At the `/hi` of session 2341 the line A2 asked whether "the report that `/handoff` showed after the librarian's run of session 1930" gave the counts, the flags and the lint total; the person read another report, the main agent wrote a failed reading on it, and only `case-guppi` of Case 913 showed the report held the flags and other counts (ledger of session 2341, lines 3 and 5). Lesson L41 of that session, `lesson-hi-asks-a-reading-of-a-text-it-names-no-place-of`, records it; the rule it breaks is `rule-agent-writing`, which tells the agent to name a real source. The person chose that `/hi` names the place of such a text: a file by its path and section, with a quotation of the part the question judges, or a reply shown only in the chat of an earlier session by that session, its date and the reply, with a plain sentence that the agent cannot open that chat; the reading line names that place as its source. Only `rule-skill-hi` changes: every Ask question reaches the person at `/hi`, whoever wrote it, and the reply that acknowledges the opening Case of a sprint puts the `A` lines "as `/hi` does" in `orchestration.md`, so it follows the new text with no change; `rule-handoff` and the librarian's frame `rule-brief` keep the form of the question they write. A Grep for `the Estimate by slug and its question` over `vault/wiki/` printed `orchestration.md`, `rule-orchestration.md`, `estimate-orchestration-asks-in-the-grill-me-shape.md`, `estimate-orchestration-acknowledges-the-opening-with-the-frontier.md`, `rule-skill-hi.md` and `estimate-hi-takes-its-readings.md`, and over `.claude/` printed `.claude/skills/hi/SKILL.md`. The person chose that the texts of `rule-orchestration` and its two Estimates stand: they say which form an Ask question keeps, its own and not the question template, and that the reply puts the `A` lines as `rule-skill-hi` sets it; the question still holds the Estimate by slug and its question, and none of them says what else it holds. The Criterion of `estimate-hi-takes-its-readings` holds the line on how an `A` line is put to the person, so this Case replaces it whole, with its `purpose`; its `method`, a reading of the new Render of `rule-skill-hi` in the Spec at the Retro of the session that changes it, stands. Its line that only the reading step opens pages becomes false once `/hi` opens the file it quotes. A question such as A2 names a report and no path, and the handoff and the brief keep that form, so on a finding of `/pre-spec` the person chose that the step that puts the `A` lines looks for the text by a Grep or a Glob over the files of the repository, never a saved chat, and takes a text it finds in no file as one shown only in a chat. The new Render and the new Criterion both name that step as the one that opens the file it quotes, beside the step that reads the `W` lines. `estimate-hi-writes-frontier` keeps its Criterion: the `A` line in `raw/<date>/<hi HHMM>/frontier.md` keeps its form, since the place stands in the question of the chat and in the reading line alone. `estimate-hi-no-read-calls` speaks of the blocks of the skill and stands. `rule-skill-hi` has `core: true`, so its new sentences carry the pointer to this Case in a bracket at their end, which `.guppi/tests/test_guppi_package.py` reads through a live run of `guppi ship`. The ledger of this session holds no `lesson[error]` line, so no `{addresses:...}` mark stands; lesson L41 belongs to session 2341, and its fix ratified in this session gets no mark.

> **problem:**
> An Ask question at `/hi` that asks the person to judge a text names no place where the text stands and quotes none of it, so the person's answer and the reading line written on it can rest on another text than the one the Estimate means.

> **recommend:**
> - **What should `/hi` say beside an Ask question that asks the person to judge a text?**
>   - Recommended: (a) name the place, and quote the text when it is in a file; for a text shown only in the chat of an earlier session, name that session by its date and start time and the reply, and say that the agent cannot open that chat; the reading line names the same place.
>   - Answer: agreed, (a).
> - **Which page sets this: `/hi` alone, or also the writers of the Ask question?**
>   - Recommended: (a) `/hi` alone; only `rule-skill-hi` changes.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) replace the Criterion of `estimate-hi-takes-its-readings`, its `purpose` with it; its `method` stands.
>   - Answer: agreed, (a).
> - **Do the words in `orchestration.md` on the form of an Ask question change too?**
>   - Recommended: (a) leave them and their two Estimates as they are; `context` says why they stand.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: on a finding of `/pre-spec`, the person agreed that when the question names no path, `/hi` looks for the text by a Grep or a Glob over the files of the repository, such as the brief, the handoff of the session and the page of the Estimate, never a saved chat; when it finds the text it names the path and the section and quotes it, and when it does not, it takes the text as one shown only in a chat; the Render and the Criterion name alike the step that opens the file.
>   - Taken: the new Render and `then` say that the step that puts the `A` lines searches for the text and opens the file it finds; the `－` line on the pages opened names both steps and no saved chat; the `purpose` names the search.

> **given:**
> `rule-skill-hi`: the rule of `/hi`, whose Render sets how an `A` line is put to the person and how its answer is written.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from `rule-skill-hi`.
> **＋** `estimate-hi-takes-its-readings`: its Criterion and `purpose` are replaced.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose `## Ask` lines `/hi` puts to the person.
> **＋** `vault/wiki/brief.md`: the brief, whose `Ask the person` list gives the `A` lines and their questions.
> **＋** `rule-agent-writing`: the rule that tells the agent to name a real source.
> **＋** `.guppi/tests/test_guppi_package.py`: runs `guppi ship` over the live repository, which removes the bracket of a pointer to a Case.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
> **＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When that question asks the person to judge a text and names no path, the step that puts the `A` lines looks for the text by a Grep or a Glob over the files of the repository, such as `vault/wiki/brief.md`, the handoff of the session and the page of the Estimate. When the text is in a file of the repository, the agent names the path and the section of that file and quotes the part the question judges. When it finds no such file, it takes the text as one shown only in the chat of an earlier session: it names that session by its date and the time of its `hi:` line and the reply that showed the text, and says in a plain sentence that it cannot open that chat.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result and the place it named for the text as its source, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** An open `W` line whose reading cannot run now stays open under `## Work` and is no line under `## Cases`.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only two steps open pages: the step that reads the open `W` lines opens the page of the Estimate of each of them, and the step that puts the `A` lines opens the file it found or the question names, to quote it. Neither opens a saved chat.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. ``
>   - new: `` Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. When that question asks the person to judge a text, name its place. When the question names no path, this step looks for the text by a Grep or a Glob over the files of the repository, such as the brief, the handoff of the session and the page of the Estimate, and opens the file it finds, never a saved chat. For a text in a file of the repository, name the path and the section of the file, with a quotation of the part the question judges. For a text it finds in no file, take it as one shown only in the chat of an earlier session: name that session by its date and the time of its `hi:` line and the reply that showed it, such as the reply after `/handoff` that showed the report of the librarian, with a plain sentence that you cannot open that chat (as set in case 921). ``
>   - old: `` then write its reading line in a `LEDGER` block of the reply, which ends in text, the answer as its result (case 531.13). ``
>   - new: `` then write its reading line in a `LEDGER` block of the reply, which ends in text, the answer as its result and the place you named for the text as its source (cases 531.13, 921). ``
>   - change: `an Ask question that asks the person to judge a text names its place and quotes it when it stands in a file; the reading line names that place as its source`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] update `estimate-hi-takes-its-readings`
>   - set: `{status: pending, purpose: "Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, leaves each other open W line open under Work with no Cases line, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, with the place of a text the question asks the person to judge, searched for in the files of the repository when the question names no path, and a quotation of it when it stands in a file, writes the answer and that place as its reading line, and opens no page but the Estimates of its open W lines and the file it quotes"}`
>   - change: `the Criterion replaced whole — an Ask question that asks the person to judge a text names its place and quotes it when it stands in a file, and the reading line names that place`
> - [ ] read `estimate-hi-takes-its-readings`

> **ratification:**
> ```
> - decision[case 921][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 921][update][estimate-hi-takes-its-readings]{ref:rule-skill-hi}
> ```
