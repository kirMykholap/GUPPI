## Case 729 — A brief line that repeats a sprint item makes no second Frontier line

> **context:**
> At `/hi` the agent builds the Cases list of the Frontier from several sources. Each item of the sprint page's current milestone becomes a line, and each line of the `Cases` list of the brief's Next session becomes a line too. Nothing checks whether two lines name one item. In this session the sprint page held the close of `migration` as a milestone item, and the brief held the same item, which the librarian carried over from `## For the next session` of the last handoff as `rule-brief` tells it to. So the Frontier got C2 from the sprint and C6 from the brief, and C6 was closed `· work` by hand. The person chose to stop the repeat at `/hi`: it has the sprint page and the brief in its context side by side, so one check there catches a repeat whatever route the brief line came by. The librarian and the handoff stay as they are, so `rule-brief`, `rule-handoff` and `estimate-brief-written` are not touched. The second paragraph of the Render of `rule-brief` already says that a sprint item reaches `/hi` through the sprint page, and the change agrees with it. The rule covers only a repeat of an item of the current milestone. The milestone line stands as it is, with the source `sprint` alone, so the closers of a sprint item do not change. A Grep for `brief's Next session` over `vault/wiki/` printed `vault/wiki/log.md`, `vault/wiki/estimates/estimate-hi-writes-frontier.md` and `vault/wiki/rules/rule-skill-hi.md`, and over `.claude/` printed `.claude/skills/hi/SKILL.md`. The log is history. The skill file is rendered from `rule-skill-hi`. `estimate-hi-writes-frontier` lists the sources of the Cases lines, so its Criterion is replaced whole with one line added. Its `method`, which is the person's answer at the `/hi` after the close of a sprint, stays as it is. At that `/hi` the brief opens with `open the next sprint` and no milestone item becomes a line, so the person reads the new line there only by the fact that no line repeats. The other Estimates of `rule-skill-hi` check the reading step, the loaded context and the conserved Spec, and none of their Criteria speaks of a repeated line, so they stand.

> **problem:**
> A brief line that names the same item as a line of the sprint's current milestone becomes a second Frontier line, and the person has to close it by hand.

> **recommend:**
> - **Where is the repeat stopped?**
>   - Recommended: (a) `/hi` merges the lines (`rule-skill-hi`): it has both texts in its context, so one check there catches a repeat from any route.
>   - Answer: agreed, (a).
> - **Which repeats count?**
>   - Recommended: (a) only an item of the current milestone, the repeat that happened.
>   - Answer: agreed, (a).
> - **What is left of the brief's line?**
>   - Recommended: (a) nothing: the sprint line stands as it is, with its one source, so the closers do not change.
>   - Answer: agreed, (a).
> - **Which Estimate checks the merge?**
>   - Recommended: (a) replace the Criterion of `estimate-hi-writes-frontier` with one line added, and keep its `method`.
>   - Answer: agreed, (a).

> **given:**
> `rule-skill-hi`: the rule whose Render sets how `/hi` assembles the Frontier.
> **＋** `.claude/skills/hi/SKILL.md`: the skill rendered from `rule-skill-hi`.
> **＋** `estimate-hi-writes-frontier`: the check of the Frontier; its Criterion is replaced whole.
> **＋** `vault/wiki/sprint.md`: the source of the items of the current milestone.
> **＋** `vault/wiki/brief.md`: the source of the `Cases`, `Work` and `Ask the person` lists of Next session.
> **＋** `vault/wiki/backlog.md`: the source of the conserved Specs and the backlog count.
> **＋** `vault/wiki/orchestration.md`: the rule of the short Case of a take-back.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the file the Frontier is written to.

> **when:**
> The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an open `W` line whose reading cannot run now, written by the reading step of `/hi`; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** A line of the `Cases` of the brief's Next session that names the same item as a line of the current milestone makes no line of its own. The milestone line stands as the sprint page gives it, with the source `sprint` alone. The agent judges the sameness by meaning from the sprint page and the brief in its context, with no page opened.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line, but for the short Case of a take-back of a ratified Case, as `vault/wiki/orchestration.md` sets it. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of the current milestone is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** Pre-spec finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` the `Cases` list of the brief's Next session; a hand edit shown by `Render:` ``
>   - new: `` the `Cases` list of the brief's Next session, but for a line that names the same item as a line of the current milestone, which makes no line of its own: the milestone line stands as the sprint page gives it, with the source `sprint` alone, and the agent judges the sameness by meaning from the sprint page and the brief in its context, no page opened (case 729); a hand edit shown by `Render:` ``
>   - change: `a line of the brief's Next session that repeats an item of the current milestone makes no Frontier line of its own (case 729)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] update `estimate-hi-writes-frontier`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a brief line that repeats an item of the current milestone makes no line of its own (case 729)`
> - [ ] read `estimate-hi-writes-frontier`

> **ratification:**
> ```
> - decision[case 729][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 729][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```
