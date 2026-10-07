<!-- approved 01:45:49 · session 9a16bfe9 -->

# Spec — session 0050, 2026-10-08

## Case 727 — A Case taken back closes its Frontier line as orchestration sets it

> **context:**
> When a newer Case replaces an earlier one in the same session, `case-schema.md` says that the Frontier line the earlier Case closed is closed again by the replacing Case. That holds when a Case is built again under a new number: the line then names the new number. It does not hold when the person takes back a ratified Case. The main agent then writes a short Case that puts the targets off and replaces the Case taken back. But `orchestration.md` closes the line of a sprint item `[-] … · sprint · defer` and the line of a backlog item `[-] … · backlog · kept`, and neither closer names the short Case; when a part of the Case stays in the plan, the line keeps `· case N` (cases 713, 723.1). Pre-spec found this as F5 of Case 713, and Case 722.3 put `rule-case-protocol` off again for it, so the page holds `decision-case-722.3` in its `deferred_by`. The person chose to keep the general sentence and add the take-back as an exception that points to `orchestration.md`, so the closers of a take-back stand in one file only. A Grep for `closed again|closes again|close again` over `vault/wiki/`, `.claude/`, `guppi/` and `tests/` printed `vault/wiki/brief.md`, `vault/wiki/case-schema.md` and `vault/wiki/rules/rule-case-protocol.md`; the hit in the brief only reports this item, and the librarian writes the brief again. The Case takes up the deferred decision, so its decision line carries `{supersedes:case 722.3}` and names the page by an `update`; this sets `decision-case-722.3` `superseded`, and the change of Splitting that the History of the page records for 722.3 stays on the page, since a mark removes no text. No Estimate is touched: `estimate-case-protocol-loaded` checks after the render that `case-schema.md` equals the Render, and `estimate-orchestration-takes-back-a-ratified-case` already checks the closers of a take-back; neither Criterion speaks of a change that this Case makes, so both stand, and `estimate-case-protocol-case-form` speaks of the form of a Case file, not of the Frontier.

> **problem:**
> `case-schema.md` says that a Frontier line is always closed again by the Case that replaces the earlier one. A Case taken back from a sprint or a backlog item closes its line by a closer that names no Case, and so the schema contradicts `orchestration.md`.

> **recommend:**
> - **How the sentence on the Frontier line is fixed**
>   - Recommended: (a) keep the sentence and add the take-back as an exception that points to `orchestration.md`.
>   - Answer: agreed, (a).
> - **What checks that the fix is done**
>   - Recommended: (a) no new check; `estimate-case-protocol-loaded` checks the render and `estimate-orchestration-takes-back-a-ratified-case` keeps checking the behaviour.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-protocol`: the page whose Render holds the sentence on the Frontier line.
> **＋** `vault/wiki/case-schema.md`: the file rendered from `rule-case-protocol`.
> **＋** `rule-orchestration`: the rule that sets the closers of the line of a Case taken back.

> **when:**
> `case-guppi` reads `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, on a Case that replaces an earlier Case in its own session.

> **then:**
> The schema says that a Frontier line the earlier Case closed is closed again by the replacing Case.
> **＋** The schema says that the line of the item of a Case taken back closes as `rule-orchestration` sets it for a take-back.
> **－** The schema does not list the closers of a take-back.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: a Frontier line it closed is closed again by the superseding Case, and pre-spec catches a superseded Case still in the plan (case 299.1)
    new: a Frontier line it closed is closed again by the superseding Case, but the line of the item of a Case taken back closes as `orchestration.md` sets it for a take-back (cases 713, 727), and pre-spec catches a superseded Case still in the plan (case 299.1)
  change: the take-back is an exception to the Frontier line closed again by the superseding Case, its closer set in orchestration.md (case 727, supersedes the defer of 722.3)
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Case 728 — The check of the put-off reply reads the new Render at Retro

> **context:**
> When the person puts off a decision whose Frontier item comes from neither the sprint nor the backlog, the main agent shows a short Case in the same reply, carries its ledger line, closes the line `[-] … · defer case N` and asks what comes next. `estimate-orchestration-defers-in-one-reply` checks that reply, and its `method` waits for such a reply live. Case 723.2 of session 2114 replaced its Criterion; in that session only the sprint items C1 and C2 were put off, so Retro set it `failed` with the result "not read" (ledger L22 of 2114), and by the cascade `rule-orchestration` went from `built` to `draft`, though no fault was seen. `rule-retro` reads an Estimate of a rule whose Render a Case of the Spec changes from the new Render in the Spec, and a Grep for `^(method|status|checked):` over `vault/wiki/estimates/` with the glob `estimate-orchestration-*` printed the lines of 16 files: the method of `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-takes-back-a-ratified-case`, `estimate-orchestration-marks-each-round-of-a-batch` and `estimate-orchestration-says-when-a-rendered-change-lands` reads that new Render at Retro, and every Estimate but this one stands `passed`. The person chose the same method for this Estimate, and chose to set it `passed` by their decision now, since `case-guppi` read the Render of `rule-orchestration` as it stands against the Criterion and found each line of the Criterion stated there: the short form, the `LEDGER` block with no tool call after it, the Frontier with its closer, the closing question, the corrected wording, the `**Waiting:**` turn of a dropped Case, no short defer at Retro, and the sprint and backlog closers. The update writes the Criterion back unchanged, so the promise stands and nothing is signed twice; `estimate-prespec-hook-reports-a-method-that-waits-for-another-session` already checks that a new `method` holds only what runs in its own session, and its Criterion stands, since this Case adds no form of method. With every live Estimate of `rule-orchestration` `passed`, the cascade of `generate` sets the rule `built`. By `rule-retro`, the Retro of this session neither reads this Estimate nor sets it `failed`, since its update sets `passed` by the person's decision.

> **problem:**
> `estimate-orchestration-defers-in-one-reply` can be read only on a live reply that puts off a decision of another source than the sprint or the backlog. A session with no such reply leaves it `failed` with no fault seen, and keeps `rule-orchestration` in `draft`.

> **recommend:**
> - **What the method reads**
>   - Recommended: (b) read the new Render of `rule-orchestration` in the Spec at Retro of the session that changes the Estimate, as sibling Estimates do.
>   - Answer: agreed, (b).
> - **How the check leaves `failed`**
>   - Recommended: (a) set it `passed` now by the person's decision, its Criterion written back unchanged, after the Render as it stands was read against the Criterion.
>   - Answer: agreed, (a).

> **given:**
> `estimate-orchestration-defers-in-one-reply`: its `method` is set and its status is set by the person's decision.
> **＋** `rule-orchestration`: the rule whose Render the method reads.
> **＋** `rule-retro`: the rule that reads at Retro the Estimates the session changes.

> **when:**
> The Retro of a session whose Spec replaces the Criterion of `estimate-orchestration-defers-in-one-reply` takes its reading.

> **then:**
> Retro reads the new Render of `rule-orchestration` in the Spec against that Criterion and writes the result in the estimate line.
> **－** The reading does not wait for a decision that the person puts off in Plan Mode.

```then
update:
- slug: estimate-orchestration-defers-in-one-reply
  set:
    status: passed
    checked: 2026-10-08
    method: 'by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line'
  sections:
    Criterion: |-
      When:
      In Plan Mode, the person asks in the chat to put off a decision: an item of `raw/<date>/<hi HHMM>/frontier.md` whose source is neither the sprint nor the backlog, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

      Then:
      In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
      **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
      **＋** The person's words asking for the defer are its ratification: no question asks for it.
      **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
      **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
      **＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply. The agent calls `/pre-spec` only after the person says to go on.
      **＋** When no line under `## Cases` is open after `/pre-spec`, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on with the loop after the findings.
      **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
      **＋** When the item has a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, the drop goes to that `case-guppi` first and the turn of the person's words ends with one `**Waiting:**` line; the short Case, its `LEDGER` block and the Frontier come in the turn that the answer `**Dropped:**` opens.
      **－** No text follows the question, or the Frontier when no question stands.
      **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
      **－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line but for the short Case of a take-back of a ratified Case, which is the moment of `estimate-orchestration-takes-back-a-ratified-case`, and a reply that closes only such lines with no take-back is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.
    Result: |-
      2026-10-08, the person's decision, case 728: the Render of rule-orchestration as it stands read against the Criterion; each line of the Criterion is stated in it
      2026-10-07, Retro, not read: its method needs a decision of a source other than the sprint or the backlog put off with its line closed [-] … · defer case N; in session 2114 only the sprint items C1 and C2 were put off, closed · sprint · defer, which the method excludes
  change: the method reads the new Render of rule-orchestration in the Spec at Retro; passed by the person's decision, the Criterion written back unchanged (case 728)
```

```tasks
- [ ] update `estimate-orchestration-defers-in-one-reply`
```

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

```then
update:
- slug: rule-skill-hi
  replace:
  - old: the `Cases` list of the brief's Next session; a hand edit shown by `Render:`
    new: 'the `Cases` list of the brief''s Next session, but for a line that names the same item as a line of the current milestone, which makes no line of its own: the milestone line stands as the sprint page gives it, with the source `sprint` alone, and the agent judges the sameness by meaning from the sprint page and the brief in its context, no page opened (case 729); a hand edit shown by `Render:`'
  change: a line of the brief's Next session that repeats an item of the current milestone makes no Frontier line of its own (case 729)
- slug: estimate-hi-writes-frontier
  set:
    status: pending
  change: the Criterion replaced whole — a brief line that repeats an item of the current milestone makes no line of its own (case 729)
```

```tasks
- [ ] update `rule-skill-hi`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] update `estimate-hi-writes-frontier`
- [ ] read `estimate-hi-writes-frontier`
```

## Case 730 — Cases out at once are a batch, and a change asked of another Case points to the promise

> **context:**
> Two lessons of session 2114 have no fix. First, `lesson-orchestration-showed-a-case-while-a-round-stood-open`: `rule-orchestration` makes Cases a batch only when one answer of the person takes up two or more items, or when the person's word asks that a ratified Case change while another Case is built (cases 598.1, 684.1); a Case the person questions or changes is shown again "alone or in a new batch". In session 2114, after the person dropped a change to Case 722, its `case-guppi` undid the change and 722 came back while a question of Case 723 stood unanswered; the main agent showed 722 for ratification in the same reply as that question. The person chose that any Cases out at the same time are a batch, by whatever route, with no hook: the fault came from a gap in the rule. Case 730.1 writes that into the Render of `rule-orchestration` under a new Estimate, and Case 730.2 turns the line of `estimate-orchestration-signs-a-batch-together` that allowed the Case alone into a pointer to it and sets its method to read the new Render at Retro, so that the reading does not wait for a live moment. Second, `lesson-orchestration-recommended-a-rebuild-that-signed-a-promise-twice`: the `case-guppi` of Case 725 named, in its `context`, the change Case 722.1 needed as an exception written into the Criterion of 722.1, though 725.2 created `estimate-case-check-leaves-out-a-case-the-file-supersedes` for that exception; the main agent recommended the rebuild, and `/pre-spec` found the promise signed twice. The person chose to fix it where the wording is born: Case 730.3 makes `case-guppi` word that change as a pointer to its own Estimate. The main agent, which does not load `case-schema.md`, passes the wording on as it stands. The lessons belong to session 2114, so no decision line carries an `{addresses:...}` mark (case 284.2). Each lesson reopened its Insight, so 730.1 sets `insight-orchestration-items-taken-together-unruled` `actioned` and 730.3 sets `insight-workflow-case-written-without-reading-the-pages-it-changes` `actioned`, as case 699.5 did.
>
> A Grep for `alone or in a new batch|shown again alone|shown alone` over `vault/wiki/`, `.claude/`, `guppi/` and `tests/` printed `vault/wiki/orchestration.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-signs-items-taken-together.md`, `vault/wiki/estimates/estimate-orchestration-signs-a-batch-together.md` and `vault/wiki/estimates/estimate-orchestration-marks-each-round-of-a-batch.md`. `orchestration.md` is the file rendered from `rule-orchestration`. The line of `estimate-orchestration-signs-items-taken-together` that an item the person takes up alone is shown alone stands, since the main agent takes up no next item while another Case is out, and its other hit is its Result. The line of `estimate-orchestration-marks-each-round-of-a-batch` on a round shown alone speaks of the Context label, which this Case does not touch. A Grep for `Other Case` over `.claude/` printed `.claude/agents/case-guppi.md`, the file rendered from `rule-case-build`, and over `vault/wiki/rules/` printed `vault/wiki/rules/rule-case-build.md` and `vault/wiki/rules/rule-orchestration.md`; `rule-orchestration` sets how the main agent asks the person about another Case, and that stands, since only the wording of the change in `case-guppi`'s `context` changes. A Grep for `Other Case|other Case` over `vault/wiki/estimates/` with the glob `estimate-case-build-*` printed `estimate-case-build-writes-the-case.md` and `estimate-case-build-checks-the-finished-case.md`: the first states the `**Other Case:**` line, so 730.3 replaces its Criterion whole with one line added, its `purpose` and `method` standing, since the method already reads the new Render at Retro; the hit of the second speaks of reading the Cases of the session, not of the wording of a change, and stands. A Glob `vault/wiki/**/estimate-orchestration-batches-*.md` printed nothing, so the new slug is free. The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.
>
> `/pre-spec` found three more sentences of the Render of `rule-orchestration` that state the batch without the new route, and 730.1 gives each the condition: the routes of a batch in `## Plan Mode and the Frontier`, the showing of a Case whose dropped change is undone (case 705.2), and a sub-case shown again alone (case 355.2). `estimate-orchestration-shows-the-built-case` says that the main agent shows the Case again "as after a change" when a dropped change is undone. Its Criterion stands, since it promises the showing of the Case and not when it is shown; the showing after a change now takes the condition of 730.1, and `estimate-orchestration-batches-cases-out-at-once` checks that condition. Writing the condition into that Criterion too would sign it twice.

> **problem:**
> Outside the two kinds of batch, nothing stops the main agent from showing a Case that comes back while a round of another Case stands unanswered, so one reply asks two things. And a `case-guppi` that names the change another Case needs may word as a new promise what an Estimate of its own Case already promises, so the rebuild it leads to signs one promise twice.

> **recommend:**
> - **One Case or two parts**
>   - Recommended: (a) one Case with sub-cases, one for each lesson.
>   - Answer: agreed, (a).
> - **What the main agent does with a Case that comes back while another Case's question is open**
>   - Recommended: (a) any Cases out at the same time, by any route, are a batch until each is ratified or deferred.
>   - Answer: agreed, (a).
> - **Is the rule enforced by a hook**
>   - Recommended: (a) the rule text only, read at the Retro of this session.
>   - Answer: agreed, (a).
> - **Where the double-signed promise is stopped**
>   - Recommended: (a) the Case that asks for the change words it as a pointer to its own Estimate (`rule-case-build`).
>   - Answer: agreed, (a).
> - **Which check covers Cases that are out at the same time**
>   - Recommended: (a) a new Estimate of `rule-orchestration`, read on the new Render at Retro; the line of `estimate-orchestration-signs-a-batch-together` that allows a Case alone becomes a pointer to it, and its method reads the new Render at Retro.
>   - Answer: agreed, (a).
> - **Which check covers the pointer wording of an "Other Case" request**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-writes-the-case` whole, with one line added.
>   - Answer: agreed, (a).
> - **What happens to the two Insights**
>   - Recommended: (a) each sub-case sets its Insight `actioned`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the findings of `/pre-spec` asked that 730.1 give the new condition to three more sentences of `rule-orchestration` and say why `estimate-orchestration-shows-the-built-case` stands, and that 730.2 replace the old line of its Criterion instead of keeping it beside a pointer.
>   - Taken: 730.1 gains three replace pairs and a paragraph of `context` on that Estimate; in 730.2 the old line is replaced by the conditioned line.

### Case 730.1 — Cases out at the same time are a batch

> **given:**
> `rule-orchestration`: the rule whose Render sets when Cases are a batch.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-batches-cases-out-at-once`: the new check of Cases out at the same time.
> **＋** `estimate-orchestration-signs-items-taken-together`: the check of the batch of items taken up in one answer.
> **＋** `estimate-orchestration-signs-a-batch-together`: the check of the batch of a ratified Case asked to change.
> **＋** `rule-prespec`: the rule of the loop after the findings of `/pre-spec`.
> **＋** `insight-orchestration-items-taken-together-unruled`: the Insight that the lesson of this sub-case reopened; set `actioned`.

> **when:**
> In Plan Mode before `/pre-spec`, a Case of the session goes back to its `case-guppi` — the person questions or changes it, or the person drops a change to it and its `case-guppi` undoes the change — while the `case-guppi` of another Case has not answered or a round of another Case stands unanswered, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The Cases out at the same time are one batch, and take the steps of a batch that `vault/wiki/orchestration.md` sets until each is ratified or deferred.
> **＋** The main agent shows no Case while a round of another Case of the batch stands unanswered: a Case that comes back built waits, and is not shown.
> **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line under the bold label `**Waiting:**`, translated, that names the Cases that have answered and those still out, and nothing else.
> **＋** It shows every round that came back in one list, each question numbered `<Case id>.Q<n>`, and sends each answer to the `case-guppi` of its Case, all in one message.
> **＋** It shows every Case of the batch in one reply, for one ratification.
> **－** A Case that goes back while no other Case of the session is out is shown again alone.
> **－** A batch of items that one answer of the person takes up, and a batch of a ratified Case asked to change while another Case is built, are the moments of `estimate-orchestration-signs-items-taken-together` and `estimate-orchestration-signs-a-batch-together`.
> **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

```then
create:
- slug: estimate-orchestration-batches-cases-out-at-once
  ref: rule-orchestration
  kind: QA
  purpose: Whether Cases out at the same time by a route other than the two batches already set are a batch, so that no Case is shown while a round of another Case stands unanswered
  method: 'by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
update:
- slug: rule-orchestration
  replace:
  - old: a Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or in a new batch with each Case it asks to change (case 598.1).
    new: 'a Case the person questions or changes goes back to its `case-guppi` and is shown again, alone when no other Case of the session is out, or in a new batch with each Case it asks to change (case 598.1). Before `/pre-spec`, Cases out at the same time by any other route — a Case the person questions or changes, or a Case whose dropped change its `case-guppi` undoes, while the `case-guppi` of another Case has not answered or a round of another Case stands unanswered — are a batch too, and take its steps until each is ratified or deferred: a Case that comes back built while a round of another Case stands unanswered waits, and is not shown, and every Case of the batch is shown in one reply (case 730.1).'
  - old: or when the person's word asks that a Case already ratified change while another Case is built, as `## Showing and signing a Case` sets it (cases 598.1, 684.1)
    new: or when the person's word asks that a Case already ratified change while another Case is built, or when Cases are out at the same time by any other route, as `## Showing and signing a Case` sets it (cases 598.1, 684.1, 730.1)
  - old: the agent shows the Case again as after a change, and the person ratifies it again
    new: the agent shows the Case again as after a change — in a batch while another Case of the session is out (case 730.1) — and the person ratifies it again
  - old: a sub-case the person questions or changes is shown again alone (case 355.2)
    new: a sub-case the person questions or changes is shown again alone when no other Case of the session is out, and otherwise in a batch (cases 355.2, 730.1)
  change: Cases out at the same time by any route are a batch, so no Case is shown while a round of another Case stands unanswered (case 730.1)
- slug: insight-orchestration-items-taken-together-unruled
  set:
    status: actioned
  change: 'actioned: Cases out at the same time by any route are a batch, so no Case is shown while a round of another Case stands unanswered (case 730.1)'
```

```tasks
- [ ] update `rule-orchestration`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] create `estimate-orchestration-batches-cases-out-at-once`
- [ ] update `insight-orchestration-items-taken-together-unruled`
- [ ] read `estimate-orchestration-batches-cases-out-at-once`
```

### Case 730.2 — A Case shown again alone only when no other Case is out

> **given:**
> `estimate-orchestration-signs-a-batch-together`: the check of the batch of a ratified Case asked to change; its Criterion is replaced whole and its method set.
> **＋** `estimate-orchestration-batches-cases-out-at-once`: the check that a Case shown again while another Case is out points to.
> **＋** `rule-orchestration`: the rule whose Render the method reads.

> **when:**
> In a batch of a ratified Case asked to change, the person questions or changes a Case of the batch after it is shown, and it goes back to its `case-guppi`.

> **then:**
> While another Case of the session is out, the Case is shown as `estimate-orchestration-batches-cases-out-at-once` sets it.
> **－** The main agent does not show it alone while that other Case is out.

```then
update:
- slug: estimate-orchestration-signs-a-batch-together
  set:
    status: pending
    method: 'by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line'
  sections:
    Criterion: |-
      When:
      In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

      Then:
      The main agent sends the ratified Case back to its `case-guppi` by `SendMessage`, and shows neither that Case nor the Case being built alone: the two are one batch.
      **＋** A Case that a Case of the batch asks to change in the same way joins the batch.
      **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
      **＋** It shows one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
      **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
      **＋** The person ratifies the batch at once or names the ids. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone only when no other Case of the session is out, or in a new batch with each Case it asks to change; while another Case is out, it is shown as `estimate-orchestration-batches-cases-out-at-once` sets it.
      **－** Outside a batch and the loop after the findings of `/pre-spec`, the main agent does not take up the next item of `raw/<date>/<hi HHMM>/frontier.md` before the shown Case is ratified or deferred.
      **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.
  change: the Criterion replaced whole — a Case is shown again alone only when no other Case is out, and otherwise as estimate-orchestration-batches-cases-out-at-once sets it; the method reads the new Render at Retro (case 730.2)
```

```tasks
- [ ] update `estimate-orchestration-signs-a-batch-together`
- [ ] read `estimate-orchestration-signs-a-batch-together`
```

### Case 730.3 — A change asked of another Case points to the promise

> **given:**
> `rule-case-build`: the rule whose Render sets how `case-guppi` names the change another Case needs.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-case-build-writes-the-case`: the check of the `**Other Case:**` line; its Criterion is replaced whole.
> **＋** `vault/wiki/case-schema.md`: the schema that says nothing is signed twice.
> **＋** `insight-workflow-case-written-without-reading-the-pages-it-changes`: the Insight that the lesson of this sub-case reopened; set `actioned`.

> **when:**
> `case-guppi` of `.claude/agents/case-guppi.md` names in the `context` of its Case another Case of the session and the change that Case needs, and again on a line `**Other Case:**` of its summary.

> **then:**
> Where an Estimate that its own Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate.
> **－** It does not word that promise again as a change the other Case needs, since `vault/wiki/case-schema.md` says that nothing is signed twice.

```then
update:
- slug: rule-case-build
  replace:
  - old: name in `context` the other Case and the change it needs, and again on a line
    new: name in `context` the other Case and the change it needs — where an Estimate your own Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it needs is a pointer to that Estimate, never that promise written again, since nothing is signed twice (case 730.3) — and again on a line
  change: the change another Case needs is a pointer to an Estimate of the Case that names it, when that Estimate already makes its promise (case 730.3)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
      **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
      **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.

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
      **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it builds that behaviour as a new top-level Case beside it, in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
      **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
      **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
      **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
      **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
      **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
      **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
      **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
      **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
      **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
      **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
      **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
      **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.
  change: the Criterion replaced whole — the change another Case needs is a pointer to an Estimate of the Case that names it, when that Estimate already makes its promise (case 730.3)
- slug: insight-workflow-case-written-without-reading-the-pages-it-changes
  set:
    status: actioned
  change: 'actioned: case-guppi words the change another Case needs as a pointer to its own Estimate when that Estimate already makes the promise (case 730.3)'
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] update `estimate-case-build-writes-the-case`
- [ ] update `insight-workflow-case-written-without-reading-the-pages-it-changes`
- [ ] read `estimate-case-build-writes-the-case`
```

## Case 731 — The method of the Frontier check is spelled as a reading by hand

> **context:**
> `make lint` sorts the `method` of each Estimate into the forms that `rule-estimates-schema` names. For an Estimate of a MOC, `check_method` in `guppi/lint.py` passes a `make <target>` of the Makefile, or the words `by hand` when no counted Estimate of the children names a test. `rule-skill-hi` is a MOC with `render_mode: full`, and its three children have `enforcement: render`, so none of their Estimates is counted. Case 723.3 set the `method` of `estimate-hi-writes-frontier` to the person's answer at the `/hi` after the close of a sprint, with no words `by hand`, so lint did not read it as a reading and printed the `method` finding that a MOC's Estimate names no `make <target>`. The person chose to put the words `by hand` at the head of the method and keep the rest word for word, since `rule-estimates-schema` calls them the one spelling of a reading. Only the `method` field changes: the update names a part, so the Criterion and the status stay as Case 729 of this session leaves them, and Case 729 kept the method's meaning, which this Case keeps too. The new method names the person in the part that names `/hi`, so `waits_for_another_session` does not judge it a wait, and the `tests/` path keeps it a form for pre-spec. `estimate-lint-checks-the-method` checks the change: its Criterion says that `by hand` passes on a MOC when every counted Estimate of the children is a reading, and on a MOC with `render_mode: full` the Estimates of a child with `enforcement: render` are not counted. That Criterion covers this page as it stands, so it is not replaced, and the `make lint` of the librarian's run, which the brief reports, shows the finding gone. Pre-spec and the check of the Case file leave the MOC branch to lint, and the person chose to leave that gap as it is. A Grep of `` names no `make `` over the repository, `vault/raw/` and `vault/archive/` left out, printed `guppi/lint.py` and `vault/wiki/brief.md`; the brief names the finding and the librarian writes it anew. A Grep of `the person's answer at the /hi` over the same paths printed `vault/wiki/estimates/estimate-hi-writes-frontier.md`, `tests/test_prespec.py`, `tests/test_lint.py` and `vault/wiki/estimates/estimate-context-size-shown-after-each-reply.md`. The test hits are fixtures of methods of their own, and the last hit is a Result line, so they stand.

> **problem:**
> The `method` of `estimate-hi-writes-frontier` names a reading by the person without the words `by hand`, so `make lint` reports that the Estimate of a MOC names no `make <target>`.

> **recommend:**
> - **How is the lint finding removed?**
>   - Recommended: (a) put "by hand" back into the method; only the `method` field changes.
>   - Answer: agreed, (a).
> - **Which check proves the fix?**
>   - Recommended: (a) no new check: `estimate-lint-checks-the-method` stands, and the `make lint` of the librarian's run shows the finding gone.
>   - Answer: agreed, (a).
> - **Is the gap that let the wording through closed too?**
>   - Recommended: (a) leave it: this Case fixes only the one method.
>   - Answer: agreed, (a).

> **given:**
> `estimate-hi-writes-frontier`: the check of the Frontier of `/hi`; its `method` is set anew.
> **＋** `rule-skill-hi`: the MOC the Estimate checks, with `render_mode: full`.
> **＋** `guppi/lint.py`: `check_method` judges the `method` of an Estimate of a MOC.
> **＋** `tests/test_prespec.py`: the unit tests the method names.
> **＋** `rule-estimates-schema`: sets `by hand` as the one spelling of a reading.
> **＋** `estimate-lint-checks-the-method`: the check of the judgment of `check_method`; its Criterion stands.
> **＋** `vault/raw/2026-10-08/0050/cases/case-729.md`: the Case of this session that replaces the Criterion of the same Estimate.

> **when:**
> `make lint` runs `check_method` of `guppi/lint.py` over the `method` of `estimate-hi-writes-frontier`, an Estimate of the MOC `rule-skill-hi`.

> **then:**
> The method opens with the words `by hand`, and `check_method` takes it as a reading.
> **＋** Lint prints no `method` finding for `estimate-hi-writes-frontier`.
> **＋** The method still names the person's answer at the `/hi` of the session after the close of a sprint, and the frontier findings of `guppi prespec --check` in `tests/test_prespec.py`.
> **－** The Criterion and the status of `estimate-hi-writes-frontier` do not change.

```then
update:
- slug: estimate-hi-writes-frontier
  set:
    method: 'by hand: the person''s answer at the /hi of the session after the close of a sprint, on whether the Frontier came out as the Criterion says, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py'
  change: the method opens with "by hand", the one spelling of a reading, so lint reads it as one (case 731)
```

```tasks
- [ ] update `estimate-hi-writes-frontier`
```
