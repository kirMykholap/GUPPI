## Case 507 — The Frontier at `/hi` shown as a checklist

> **context:**
> At `/hi` the agent writes the Frontier, the session's list of items, to `frontier.md` as checkbox lines, and then shows it in the chat. `rule-skill-hi` says only that the chat shows the Cases "one line each with its detail", so the agent chooses the look each session. This session showed each Case as a bold line with a paragraph of detail under it. The reply that acknowledges a ratification shows the same list as a checklist, which `rule-case-protocol` fixes. So one list had two looks in one session. The person saw today's Frontier in four looks and chose the checkbox list with the detail under each line. The person also kept the backlog item `rule-orchestration` out of this Case. It is a `draft` page with only a Purpose, and its defer stands. `estimate-hi-writes-frontier` promises the chat look in one line of its Criterion. So this Case replaces the Criterion whole, word for word except for that line. The old line, "In the chat the Cases are shown as a list with their detail, the backlog count and the near items; the Work is shown as one block; …", is not carried on purpose. The checklist line and the new `－` line of `then` take its place, and they keep its parts on the backlog count, the near items, the Work block, the sub-cases and the `W` and `C` closers. `estimate-hi-no-read-calls` speaks only of read calls at `/hi` and is left alone. The Criterion of `estimate-case-protocol-acknowledging-reply` already describes the checklist form and does not change. No page says the Frontier stands as bold lines.

> **problem:**
> The chat look of the Frontier at `/hi` is not fixed, so it changes from session to session and differs from the Frontier shown after each ratification.

> **recommend:**
> Show the Cases at `/hi` as the checklist of `frontier.md`, with the detail of each line on an indented line and the `- near` line under that. This is the form of the acknowledging reply, so the list keeps one look from `/hi` to the last ratification. The rejected option is a new Estimate for the chat look alone. The old Criterion would still need to be replaced whole to drop its chat line, so a new Estimate adds a page and promises nothing more.

> **given:**
> `rule-skill-hi` — the page whose Render is the `/hi` skill and says how the Frontier is shown in the chat
> **＋** `.claude/skills/hi/SKILL.md` — the skill file rendered from `rule-skill-hi`
> **＋** `estimate-hi-writes-frontier` — the promise of the Frontier at `/hi`, its chat look included
> **＋** `rule-case-protocol` — fixes the checklist form of the `## Frontier` of the acknowledging reply
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` — the sources of the Frontier
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the file of the Frontier

> **when:**
> The person invokes `/hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, and `## Work`, with lines `- [ ] W<n> — <title> · <source>`. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist, the checklist form of the `## Frontier` in the acknowledging reply of `rule-case-protocol`. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** `Pull:` and `Open issues:` are a Cases item only when `vault/wiki/sprint.md` names no decision on them.
> **－** Pre-spec finds an open line under `## Cases`. A `W` line stands open until its work is done and closes `· work` in Work Mode. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi` — the Cases shown in the chat as the checklist of `frontier.md`
>   - old: `In the chat the Cases are the agenda of Plan Mode, one line each with its detail; the Work is one block; sub-cases are cut in Cases only;`
>   - new: `` In the chat the Cases are the agenda of Plan Mode, shown as a checklist, the form of the `## Frontier` of the acknowledging reply: each line as `frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, its detail on an indented line under it and the `- near` line under that, the line `Backlog: N items` last; no Case stands as a bold line or with its detail as a paragraph (case 507); the Work is one block; sub-cases are cut in Cases only; ``
>   - change: `the Cases shown in the chat at /hi as the checklist of frontier.md, the detail on an indented line (case 507)`
> - [ ] update `estimate-hi-writes-frontier` — the Criterion replaced whole: the chat shows the Cases as a checklist
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Cases shown in the chat at /hi as the checklist of frontier.md, no bold line (case 507)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-writes-frontier` — by hand, at the first `/hi` of the next session

> **ratification:**
> ```
> - decision[case 507][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 507][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```
