<!-- approved 02:34:14 · session f240d478 -->

# Session 0039 — the labels of the acknowledging reply in the language of the chat

## Case 997 — The acknowledging reply translates its headings and labels

> **context:**
> When the person ratifies a Case, the main agent writes an acknowledging reply: the `LEDGER` block, a heading that says the Case is ratified, a paragraph of changes, a paragraph of notes and the Frontier. `## The acknowledging reply` of `rule-orchestration` names these parts by their English words in code spans and in bold, and says only at the end of its paragraph, in one short sentence, that headings and labels are in the language of the chat. In session 2227 the agent translated only the Case heading and wrote **Changes:**, **Notes:** and `## Frontier` in English in every acknowledging reply, so the reading L21 of that session set `estimate-orchestration-acknowledging-reply` `failed`; `lesson-acknowledging-reply-labels-left-in-english` (L25 of that session) gives the root cause. The person chose to rewrite the text, not to let the Criterion accept English labels: the paragraph now says first that the reply stands in the language of the chat, that the words in code spans and in bold are the names of the parts in the language of the repository, and that the reply writes each one translated, while slugs, paths, the `LEDGER` tag, the ledger lines and the word `STOP:` that opens a reply keep their own words; the rest of the `STOP:` line stands in the language of the chat, since `rule-prespec-onward` asks only that the reply open with `STOP:`, and line 45 of `rule-orchestration` puts the agent's own text in the language of the chat (a finding of `/pre-spec`). The new text names the languages by `{{chat_lang}}` and `{{documentation_lang}}`, which the render fills from `rule-guppi-config` (`.guppi/guppi/render.py`, lines 14–21), so it writes no Russian word and keeps the promise of `estimate-clean-branch-ships-neutral-texts` that shipped texts name the languages by their role; the rule that governs the choice is `## Language` of `CLAUDE.md`, the Render of `rule-language`: the chat with the owner is in the language of the chat, and only technical terms stay in English, which these labels are not. By the person's choice the fix covers every reply of the Render that shows the Frontier: the reply that closes a Frontier line with no ratification, the reply that acknowledges Cases ratified together (`## Showing and signing a Case`), the reply that carries a defer (`## The short form — deferred decisions`) and the reply that acknowledges the opening Case of `/sprint-open` now point to the translation the acknowledging reply sets, and the old closing sentence of the paragraph is dropped, its source kept in the new sentence; the replies of Cases ratified together and of a defer came in by a finding of `/pre-spec`. The `method` waits for the librarian's render and reads any acknowledging reply written after it, with no word `first`, as `method` in `rule-estimates-schema` sets it. The Criterion of `estimate-orchestration-defers-in-one-reply` says the reply shows the Frontier and sets no language, so it stands.
>
> No code reads these labels literally. A Grep for `Changes:|## Frontier|Notes:|— ratified` over `.guppi/guppi/` printed one hit, `.guppi/guppi/generate.py`, a docstring on Cases ratified after a line, which names no label; over `.claude/` it printed nothing; over `.guppi/tests/` it printed 4 files, `test_onward.py`, `test_generate.py`, `test_casecheck.py` and `test_ratified.py`, whose hits are sample replies built in the test itself, read from no live file, so the Case changes none of them. A Grep for `orchestration\.md|rule-orchestration` over `.guppi/tests/` printed `test_orchestration.py` and `test_onward.py`: `test_orchestration.py`, read whole, reads the live `vault/wiki/orchestration.md` only through `example`, which takes the blocks tagged `showing` and `defer`, and no pair of this Case touches them; `test_onward.py` reads the word `orchestration.md` in the stderr of the hook, not the file. A Grep for `acknowledg` over `.claude/` printed 4 files, `.claude/skills/work/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and `.claude/skills/pre-spec/SKILL.md`: each names the moment of the acknowledging reply and points to `orchestration.md` for its form, and sets no heading or label, so each stands. A Grep for `## Frontier` over `vault/wiki/` printed `orchestration.md`, `brief.md`, `rules/rule-orchestration.md`, `lessons/lesson-acknowledging-reply-labels-left-in-english.md`, `estimates/estimate-orchestration-acknowledging-reply.md`, `estimates/estimate-orchestration-acknowledges-the-opening-with-the-frontier.md` and `estimates/estimate-orchestration-shows-the-frontier-after-a-closed-line.md`; a Grep for ``\*\*Changes:\*\*|\*\*Notes:\*\*|`Changes:` `` over `vault/wiki/` printed `brief.md`, `orchestration.md`, `lessons/lesson-acknowledging-reply-labels-left-in-english.md`, `estimates/estimate-orchestration-acknowledging-reply.md`, `rules/rule-orchestration.md` and `estimates/estimate-orchestration-says-when-a-rendered-change-lands.md`. The Criteria of `estimate-orchestration-shows-the-frontier-after-a-closed-line` (the form that `estimate-orchestration-acknowledging-reply` sets), `estimate-orchestration-acknowledges-the-opening-with-the-frontier` (the four parts of an acknowledging reply) and `estimate-orchestration-says-when-a-rendered-change-lands` (the paragraph `Changes:`) name the parts by those names and take their language from the Criterion this Case replaces, so they stand; `estimate-orchestration-asks-in-the-grill-me-shape` lets the labels of a question stand translated or not, a reply of another moment, and stands. The blocks of `rule-orchestration`, `vault/wiki/orchestration.md` and `estimate-orchestration-acknowledging-reply` in `.guppi/links.md` were read whole; no neighbour they name sets the language of these labels.
>
> `estimate-orchestration-acknowledging-reply` checks the change: its Criterion is replaced whole, its other lines kept, and the language line names each heading and label translated, so a reading cannot pass on the Case heading alone. Its `method` changes too, since `orchestration.md` changes only at the librarian's render after this session, and a reading at this Retro would read replies written under the old text: the reading waits for that render. Its `purpose` states no part of the language promise and stands. The last run of `uv run --project .guppi guppi check`, as `## Flags` of `vault/wiki/brief.md` reports it, printed `unread: failed` on `estimate-orchestration-acknowledging-reply` among 7 lines; the Estimate set `pending` leaves that line. The lesson stands in the ledger of session 2227, not of this session, so no `{addresses:...}` mark is written: a Grep of `vault/raw/2026-11-02/0039/` for `lesson\[error\]|\{addresses:` printed only `cases/case-997.md`, this file, whose `context` names the two patterns; the session's `ledger.md` does not stand yet.

> **problem:**
> The text of the acknowledging reply names its labels by English words and gives their language only at the end, so the agent copied the English words into a chat in another language, and the check of that reply failed.

> **recommend:**
> - **How the fix works**
>   - Recommended: (a) rewrite the text of `orchestration.md` so it says first that each heading and label is translated into the language of the chat, the words in code spans being only the English names of the parts.
>   - Answer: agreed, (a).
> - **Which replies the fix covers**
>   - Recommended: (a) every reply in `orchestration.md` that shows the Frontier.
>   - Answer: agreed, (a).
> - **How done is checked**
>   - Recommended: (a) replace the Criterion of `estimate-orchestration-acknowledging-reply`, naming each label, and make its reading wait for the librarian's render.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: the Rule page whose Render sets the acknowledging reply and the replies that show the Frontier.
> **＋** `vault/wiki/orchestration.md`: the file rendered from it, which the main agent follows.
> **＋** `estimate-orchestration-acknowledging-reply`: its Criterion and its `method` are replaced.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier that the reply shows.
> **＋** `rule-ledger-write`: the ledger hook that writes the `LEDGER` block.
> **＋** `rule-prespec-onward`: the hook that sends the agent on after `/pre-spec`.
> **＋** `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: the check of the `STOP:` line.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: the check of a decision line the ledger hook holds.
> **＋** `CLAUDE.md`: its `## Language` sets the language of the chat.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block, before which stands nothing but the `STOP:` line that `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` checks. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** Each heading and label of the reply stands translated into the language of the chat that `CLAUDE.md` sets: the heading `## Case N — ratified`, the labels `Changes:` and `Notes:` and the heading `## Frontier` stand in that language, not in the English words by which this Criterion names them.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply.
> **＋** When none is open before `/pre-spec`, the question whether to go on to `/pre-spec` ends the reply, in the plain form of the question which item is next. The agent calls `/pre-spec` only after the person says to go on. A reply that answers a question of the person instead ends with the same question again.
> **＋** When none is open after `/pre-spec`, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** Slugs, paths, the tag of the `LEDGER` block, the ledger lines and the word `STOP:` that opens a reply keep their own words in any language of the chat; the rest of the `STOP:` line stands in the language of the chat.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

```then
update:
- slug: rule-orchestration
  replace:
  - old: 'comes in the turn that the answer `**Dropped:**` of that `case-guppi` opens (case 701.6): a heading `## Frontier`, the lines of `frontier.md` as a checklist in its form'
    new: 'comes in the turn that the answer `**Dropped:**` of that `case-guppi` opens (case 701.6): a heading `## Frontier`, its word translated into {{chat_lang}} as `## The acknowledging reply` sets it, the lines of `frontier.md` as a checklist in its form'
  - old: 'The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first,'
    new: 'The reply that acknowledges a ratification stands in {{chat_lang}}, its headings and labels too: the words of its headings and labels in this paragraph, in code spans and in bold, are their names in {{documentation_lang}}, and the reply writes each one translated into {{chat_lang}} — the heading `## Case N — ratified`, the labels **Changes:** and **Notes:** and the heading `## Frontier` alike —, while slugs, paths, the `LEDGER` tag, the ledger lines and the word `STOP:` that opens a reply keep their own words, the rest of that line standing in {{chat_lang}} (as set in cases 167 and 997). It has four parts, in this order: the `LEDGER` block first,'
  - old: Headings and labels in the language of the chat (case 167, supersedes 157). The reply that acknowledges the opening Case
    new: The reply that acknowledges the opening Case
  - old: its `## Frontier` shows the new Frontier;
    new: its `## Frontier`, translated as the acknowledging reply sets it above, shows the new Frontier;
  - old: one heading `## Case N — ratified` naming their ids, one **Changes:** paragraph and one Frontier (case 598.2)
    new: one heading `## Case N — ratified` naming their ids, one **Changes:** paragraph and one Frontier, each heading and label translated as `## The acknowledging reply` sets it (case 598.2)
  - old: then the Frontier with the line closed `[-] … · defer case N`
    new: then the Frontier, its heading translated as `## The acknowledging reply` sets it, with the line closed `[-] … · defer case N`
  change: the acknowledging reply and each reply that shows the Frontier write their headings and labels translated into the language of the chat, the English words named as the names of the parts
- slug: estimate-orchestration-acknowledging-reply
  set:
    status: pending
    method: 'by hand, after the librarian''s render that writes into vault/wiki/orchestration.md the paragraph of rule-orchestration that names the headings and labels of the acknowledging reply as translated: an acknowledging reply and a reply that acknowledges Cases ratified together in one answer, each written after that render, each read against the Criterion in the transcript of its session under ~/.claude/projects/'
  change: the Criterion replaced whole — each heading and label of the reply stands translated into the language of the chat; the reading waits for the render
```

```tasks
- [x] update `rule-orchestration`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] update `estimate-orchestration-acknowledging-reply`
- [x] read `estimate-orchestration-acknowledging-reply`
```

## Case 998 — A missed reader of a changed step counts only when it gets past the approved Spec

> **context:**
> `estimate-case-build-reads-the-readers-of-a-changed-step` checks that `case-guppi` finds every step, skill or place of code that reads the output of a step its Case changes. Its `method` reads the findings of `ask-guppi` at `/pre-spec` and fails on a single reader that `case-guppi` missed, even one that `/pre-spec` caught before the Spec was approved. Its History shows four failures: `raw/2026-10-30/2005/ledger.md#L54`, `raw/2026-10-31/0431/ledger.md#L43`, `raw/2026-11-01/0141/ledger.md#L18` and `raw/2026-11-01/2227/ledger.md#L19`. After each of the first three, a Case added a sentence to `rule-case-build` (948.1, 966 and 985, by the History of that page), and the page was set `pending` again (948.2, 966 and 985, by the History of the Estimate). The last reading counts 4 of 11 findings of `ask-guppi` at the `/pre-spec` of session 2038, such as Case 990, which missed `## The acknowledging reply` of `rule-orchestration` (the Result of the page, and line 19 of that ledger). The person chose to measure only what gets past `/pre-spec`: a reader that both `case-guppi` and `ask-guppi` missed and that comes to light later. The person chose to look for it in the Work Mode and Retro of the session and of the session after it, in one reading taken after that later session. The Case replaces the Criterion whole and sets the `purpose` and `method` anew, since both state the old promise. No line of the old Criterion is carried: each one described the searches `case-guppi` runs before its summary, and those searches stay in the Render of `rule-case-build`, not in this Estimate. It changes only this Estimate: the other Estimates of `rule-case-build` keep their readings, and the Render of `rule-case-build` stands, since the person chose the new measure over a new sentence in the rule. The rule that governs the change is `rule-estimates-schema`: an Estimate is one promise and one way to check it, and a reading by hand names its moment and the place of its evidence. That a `method` waits for a later session only through a part that opens with `after`, or with `by hand, after`, and names its event before a colon is set in `case-schema.md`, the Render of `rule-case-protocol` (case 781), and judged by `waits_for_an_event` of `.guppi/guppi/lint.py`. The Retro rule, `rule-retro`, keeps such an Estimate `pending` at Retro and takes its reading once, whole, after the event; for that reason the person chose one reading over two. `case-guppi` read `.guppi/guppi/lint.py` for the new `method`: `waits_for_an_event` matches its one part, which opens with `by hand, after` and closes its event at the first colon. So `waits_for_another_session` gives `/pre-spec` no finding on it, and `tied_to_a_one_off_moment`, which `check_moment` calls, finds no `first`. `check_unread`, through `waits_for_a_later_moment`, gives no `unread` finding on a `pending` page whose `method` waits for an event. The brief reports the last lint run (`## Flags`, `guppi check`, exit 1) as holding `unread: failed` on this page; that finding leaves once the page is `pending`. The block of the page in `.guppi/links.md` names `rule-case-build`, the target, and `rule-orchestration` and `rule-prespec-onward`, which only its Result names; the Result stays until the next reading, so none of them is made false. A Grep for `readers-of-a-changed-step` over the repository outside `vault/archive/` printed 12 files: `vault/raw/2026-11-02/0039/ledger.md`, `vault/raw/2026-11-02/0039/cases/case-998.md`, `vault/raw/2026-11-02/0039/cases/note-998.md`, `vault/raw/2026-11-02/0039/frontier.md`, `vault/raw/2026-11-01/2227/report.md`, `vault/wiki/brief.md`, `vault/raw/2026-11-01/2227/materialize.yaml`, `vault/wiki/log.md`, `vault/wiki/rules/rule-case-build.md`, `vault/raw/2026-11-01/2227/handoff.md`, `vault/raw/2026-11-01/2227/ledger.md` and `vault/raw/2026-11-01/2227/frontier.md`. Of the live pages, `rule-case-build` lists the slug only in `estimates`, which stands, and no test of `.guppi/tests/` names it. The session's ledger holds no `error` lesson, so the Case carries no `{addresses:...}` mark.

> **problem:**
> The Estimate has failed four times on readers that `/pre-spec` caught before the Spec was approved. Each failure added one more sentence to `rule-case-build`. The check does not measure whether a missed reader actually gets through: it fails on any miss by `case-guppi` alone, however the next check handles it.

> **recommend:**
> - **Where and when a miss is looked for**
>   - Recommended: (a) at the Retro of the same session.
>   - Answer: (b) at Retro, and again after the next session.
> - **What the Criterion promises**
>   - Recommended: (a) replace the Criterion whole with the outcome.
>   - Answer: (a).
> - **Which Estimates change**
>   - Recommended: (a) this Estimate only.
>   - Answer: (a), after the main agent explained the question in plain words.
> - **One reading or two**
>   - Recommended: (a) one reading, after the next session, covering both sessions.
>   - Answer: (a).

> **given:**
> `estimate-case-build-reads-the-readers-of-a-changed-step`: the Estimate whose Criterion, `purpose` and `method` are replaced.
> **＋** `rule-case-build`: the target of the Estimate, the rule of `.claude/agents/case-guppi.md`.
> **＋** `rule-prespec`: the rule of `/pre-spec`, whose findings come before the approval.
> **＋** `rule-estimates-schema`: the rule of one promise, one way to check it, and the field `method`.
> **＋** `rule-case-protocol`: the rule of a `method` part that waits for an event it names.
> **＋** `rule-retro`: the rule of Retro, which keeps a reading that waits for an event `pending`.
> **＋** `.guppi/guppi/`: the harness code, whose functions may do a step a Case changes.

> **when:**
> The person approves the Spec of a session whose Cases `case-guppi` built, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, and checked by `/pre-spec`, and a Case of that Spec changes what a step of a skill, an agent, a hook or a function of `.guppi/guppi/` writes, copies or shows, or adds a path on which a step does so.

> **then:**
> Each step, skill or place of code that reads that output or does the same step, and that the change makes false, stands in a Case of the approved Spec, or the `context` of a Case names it and says why it stands.
> **＋** A reader that a finding of `/pre-spec` named and that a Case built again took in counts as found.
> **＋** No such reader comes to light in the Work Mode or the Retro of that session or of the session after it, by a Case built again, a task added by hand, a red test or check, or an `error` lesson.
> **－** A text in a History line, in `log.md` or in `brief.md` is not such a reader.

```then
update:
- slug: estimate-case-build-reads-the-readers-of-a-changed-step
  set:
    status: pending
    purpose: Whether no step, skill or place of code that reads the output of a step a Case changes, or does the same step, and that the change makes false, gets past the approved Spec unnamed by both case-guppi and /pre-spec and comes to light in the Work Mode or Retro of that session or of the session after it
    method: 'by hand, after the Retro of the session that follows a session whose approved Spec holds a Case of case-guppi that changes what a step writes, copies or shows or adds a path on which a step does so: the Work Mode and Retro of both sessions, read in their ledgers and in the transcripts of their main agents under ~/.claude/projects/, for a step, a skill or a place of code that reads the output of the changed step or does the same step, that the change makes false and that no Case and no context of the approved Spec named, such as a Case built again in Work Mode, a task added by hand, a red test or check or an error lesson for it, the count and the transcripts in the estimate line'
  change: the Criterion replaced whole — a missed reader of a changed step counts only when it gets past the approved Spec and comes to light in that session or the session after it; pending again after the failed reading of session 2227
```

```tasks
- [x] update `estimate-case-build-reads-the-readers-of-a-changed-step`
- [ ] read `estimate-case-build-reads-the-readers-of-a-changed-step`
```

## Case 999 — The graph of links is dropped, and case-guppi searches the names of what it changes

> **context:**
> A hook on `SessionStart` runs `uv run --project .guppi guppi links --write`, which writes `.guppi/links.md`: one block per live page and per file, each neighbour out and in with its purpose line. `case-guppi` must read whole the block of each page and file its Case changes. The blocks of busy pages are long, most of their lines the purposes of the page's own Estimates, and the builders read them with a fixed limit and stopped before the end: `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed at the Retro of session 0141 (2 of 4 Cases, one block read by `-A 40` of 96 lines) and again in session 2227 (0 of 2 Cases, the block of `rule-orchestration` read with limit 80; its Result and the brief, `## Readings due`). The person chose to drop the graph whole. Out-links of a page stand in its own frontmatter and links, which `case-guppi` reads already; for in-links `case-guppi` now takes every name of the page or file it changes and runs one Grep that prints only the paths of the files that hold any of them, then one Grep that prints the purpose line of each page on that list, and opens the files that bear on the change. The names are the slug, the file name of each path of `governs`, `implementation_ref` and `code_ref`, the name of the agent or of the skill with its slash, and `guppi <command>` for each command of a module among those paths, since `guppi links` linked a page to a text that names it by any of these. The Grep runs over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`: the person's proposal named `.guppi/`, and the Case keeps to the code and the tests in it, so that the environment `.guppi/.venv/`, which `.guppi/.gitignore` names, stays out of the search; the hook of `rule-search-leaves-out-decisions` adds `!**/decisions/**` to a Grep whose path is the root of the repository. The purpose line of a neighbour, the one thing of a block worth keeping, comes back by the second Grep over the short list. Case 999.1 removes the graph: the two pages, their two Estimates, the code, its tests, the hook and the lines that name them; a new one-time Estimate of the sprint page checks the state once after the librarian's run, since `rule-estimates-schema` sets `once: true` for an Estimate that checks one state of the data once, whose target is the live sprint page. Case 999.2 changes the two sentences of the Render of `rule-case-build` that name `.guppi/links.md`, and renames and replaces the Criterion of the failed Estimate, whose `purpose` and `method` state the old promise and are set anew; its `method` waits for the `/pre-spec` of a session on the new Render through a part that opens with `by hand, after` and names its event before a colon, as `case-schema.md`, the Render of `rule-case-protocol`, sets it (case 781), with no word `first`, which `rule-estimates-schema` keeps for an event that has never happened. No line of the old Criterion is carried word for word, since each one speaks of a block of `.guppi/links.md`, a neighbour of a block or a page with no block: the new Criterion carries what they promised in the terms of the search, the second search at the check of the finished Case, the opening of each file that bears on the change and the entry of each one the change makes false, and drops the lines on a missing file and on a page with no block, since the search needs no file. The other Estimates of `rule-case-build` stand: of their Criteria only the failed one speaks of the graph, by the Grep below. `estimate-sprint-plugin-check-finds-no-bare-slug-link`, a one-time Estimate of `entity-sprint-plugin`, waits for the librarian's run that applies the update of `estimate-link-graph-prints-the-neighbours`; the History of that page holds the line `2026-11-01 updated: the bare link of the Result put in a code span` of Case 973, so the event has come, and the brief of session 2227 (`## Flags`, `guppi check`, exit 1, 7 lines) lists no `ref` line on that page. Once that page moves to the archive, `git log -p -1` on its old path shows the move, not the fix, and the Criterion fails, so the person chose to read it at the Retro of this session, before the librarian's run; whether the git log holds the diff of the Result alone was not read here. `case-guppi` read for its claims on code: `main` of `.guppi/guppi/cli.py`, which prints `guppi: unknown command` and exits 2 for a name outside `COMMANDS`; `run` of `.guppi/guppi/links.py`; `Vault.delete` of `.guppi/guppi/generate.py`, which sets a page `archived`; `Cleanup.unlink` and `Cleanup.flag_dangling` of `.guppi/guppi/cleanup.py`, which take an archived slug out of the `children` lists of live pages and the `estimates` lists of entities and rules and report a live page whose `parent` or `target` is archived, so `rule-harness`, `entity-guppi` and `rule-case-build` need no task for their lists, and the four pages are deleted together so that no `target` dangles; and `tree_files` of `.guppi/guppi/ship.py`, which walks the working tree, so the task that drops `.guppi/links.md` from `LEFT_OUT` comes with a task that deletes the local file by hand. Between the Work Mode that removes `links.py` and the render of `.claude/settings.json` at the librarian's run, a `SessionStart` of this session, such as after a compaction, runs the old hook and gets exit 2; `lesson-hooks-sessionstart-cannot-block` holds that exit 2 is a no-op there, so no session stops and nothing is lost, and the file is deleted after the code so that no hook writes it again. Between the same two moments a `case-guppi` of this session runs on the old Render, finds `.guppi/links.md` missing and says so in `context`, as that Render sets. A Grep for `links\.md|guppi links|link-graph|links\.py|link graph` over the repository with the glob `!vault/{archive,raw}/**` printed 22 files: `vault/wiki/brief.md`, `vault/wiki/sprint.md`, `vault/wiki/log.md`, `vault/wiki/entities/entity-link-graph.md`, `vault/wiki/entities/entity-guppi.md`, `vault/wiki/estimates/estimate-case-build-reads-the-link-graph-of-what-it-changes.md`, `vault/wiki/estimates/estimate-case-build-reads-the-readers-of-a-new-files-folder.md`, `vault/wiki/lessons/lesson-ledger-reading-writes-a-bare-wikilink.md`, `.claude/settings.json`, `.guppi/tests/test_links.py`, `vault/wiki/rules/rule-case-build.md`, `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-link-graph-at-session-start.md`, `vault/wiki/rules/rule-hook-registry.md`, `vault/wiki/rules/rule-harness.md`, `.guppi/.gitignore`, `.guppi/guppi/links.py`, `.guppi/guppi/ship.py`, `vault/wiki/estimates/estimate-link-graph-prints-the-neighbours.md`, `vault/wiki/estimates/estimate-link-graph-at-session-start-writes-the-file.md`, `vault/wiki/estimates/estimate-materialize-lifts-a-create-value-by-the-schema.md` and `vault/wiki/estimates/estimate-sprint-plugin-check-finds-no-bare-slug-link.md`. Each enters the Case but these, which stand: `brief.md` and `log.md`, not read; `sprint.md`, whose line `guppi sprint` writes from the sprint Estimate; the `## Result` of `estimate-case-build-reads-the-readers-of-a-new-files-folder` and of `estimate-materialize-lifts-a-create-value-by-the-schema` and the body of `lesson-ledger-reading-writes-a-bare-wikilink`, records of past readings and events, whose slugs lint still counts as known once archived, as the docstring of `cleanup.py` says; the History and `children` of `rule-harness`, which cleanup changes; and the sprint Estimate, read before the move. The `## Purpose` of `rule-harness` also lists among the parts of the harness the hook that writes the graph of the links at the start of a session, citing case 967.3, in words the pattern does not match; `/pre-spec` found it, and 999.1 removes that part and that case from the sentence, so the Criterion of the new Estimate also covers a text that counts the graph among the parts of GUPPI or of its harness, and excepts the Decision pages under `vault/wiki/decisions/`, the record of past decisions, which the Grep of its `method` does not print under the hook of `rule-search-leaves-out-decisions`. The two Greps of the new Render were tried in this build: a Grep for `prespec\.py` at the root of the repository with the glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed 74 files, under `vault/wiki/`, `.claude/` and `.guppi/guppi/`, none under `vault/wiki/decisions/`; and a Grep for `^(purpose|root_cause|pattern):` over `vault/wiki/` with the glob `**/{rule-harness,entity-guppi,lesson-hooks-sessionstart-cannot-block}.md` printed the three purpose lines; and the glob `{rule-harness,entity-guppi}.md` printed two; but the glob `{rules/rule-harness.md,entities/entity-guppi.md}`, a brace list of paths with their folders, printed nothing, which fits what `ask-guppi` saw in its run of `/pre-spec`; so the new Render gives the second Grep the form `**/{<slug>,<slug>}.md`, bare slugs with no folder, and says so. The appended `!**/decisions/**` took nothing from either Grep that worked. A Grep for `links` over `.guppi/guppi/` with the glob `!links.py` printed 10 files: `lint.py`, `ship.py`, `pages.py`, `prespec.py`, `generate.py`, `ledger.py`, `materialize.py`, `cli.py`, `cleanup.py` and `caseid.py`; of their hits read around the line, `cli.py` and `pages.py` name the module `links` and enter the Case, `ship.py` is named above, and the rest name `links_of`, `body_links`, `unknown_links`, wikilinks or backlinks, which the Case does not touch. A Grep for `links\.md|guppi links|links --write|from guppi import.*links|guppi\.links|links\.run|import links` over `.guppi/tests/` printed only `.guppi/tests/test_links.py`, which reads no live file and goes with the module. A Grep for `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed only `.guppi/tests/test_guppi_package.py`, in its docstring, so no test reads the Render live; that file reads `.claude/settings.json` live, and its test asserts that the commands of four hooks stand there, none of them `links`, so it passes before and after the render. The blocks of `.guppi/links.md` of the pages and files the Case changes were read; their neighbours that bear on the change are those above, and the rest, such as the Estimates of `rule-case-build` and the rules whose `implementation_ref` names `.claude/settings.json`, are not made false. Case 998, whose finished file was read whole once its build ended, replaces the Criterion, `purpose` and `method` of `estimate-case-build-reads-the-readers-of-a-changed-step` and leaves the Render of `rule-case-build` alone, so the two Cases change no sentence in common; its `context` speaks of the block of that Estimate in `.guppi/links.md` as a reading of its own build, which the removal of the file does not make false. A Glob for `vault/**/estimate-*{searches-the-names,link-graph-is-gone,graph-removed}*` printed nothing, so both new slugs are free. The ledger of the session holds no `error` lesson, so the Case carries no `{addresses:...}` mark.

> **problem:**
> `case-guppi` must read whole a block of a generated file of about seven thousand lines to find what points to a page it changes, and the long blocks get cut. The graph meant to make that search quick and cheap became a long list read in full, and the step it serves has failed twice.

> **recommend:**
> - **Which names the search takes**
>   - Recommended: (b) the slug, the file name of each path, the name of the agent or the skill with its slash, and `guppi <command>` for each module that carries a command.
>   - Answer: (b).
> - **The purpose line beside each neighbour**
>   - Recommended: (b) a second search over the pages on the list that prints the purpose line of each.
>   - Answer: (b).
> - **How the new search step is checked**
>   - Recommended: (a) rename the failed Estimate and replace its Criterion by the new step.
>   - Answer: (a).
> - **How the removal of the graph is checked**
>   - Recommended: (a) a new one-time Estimate on the sprint page.
>   - Answer: (a).
> - **The sprint Estimate on the bare link**
>   - Recommended: (a) read it now, before the page moves.
>   - Answer: (a).

### Case 999.1 — The graph of links and its hook are removed

> **given:**
> `estimate-sprint-plugin-link-graph-is-gone`: the new one-time Estimate of the removal.
> **＋** `entity-link-graph`, `rule-link-graph-at-session-start`, `estimate-link-graph-prints-the-neighbours` and `estimate-link-graph-at-session-start-writes-the-file`: the pages deleted.
> **＋** `rule-hook-registry`: the Render of the hooks of `.claude/settings.json`, which loses the hook.
> **＋** `entity-guppi`: the page of GUPPI, which names the graph as a part.
> **＋** `rule-harness`: the rule of the harness, whose Purpose lists the hook that writes the graph.
> **＋** `.guppi/guppi/links.py` and `.guppi/tests/test_links.py`: the code of `guppi links` and its tests, removed.
> **＋** `.guppi/guppi/cli.py`, `.guppi/guppi/pages.py`, `.guppi/guppi/ship.py` and `.guppi/.gitignore`: the files that name the module or `.guppi/links.md`.
> **＋** `entity-sprint-plugin` and `estimate-sprint-plugin-check-finds-no-bare-slug-link`: the sprint page and its one-time Estimate that reads a page deleted here.
> **＋** `rule-estimates-schema`: the rule of a one-time Estimate and of a `method`.
> **＋** `vault/wiki/`: the live pages, searched for a text that still names the graph.
> **＋** `vault/wiki/decisions/`: the Decision pages, the record of past decisions, left out of that search.

> **when:**
> The librarian's run applies the `delete` of `entity-link-graph` and `rule-link-graph-at-session-start` and renders `.claude/settings.json` from `rule-hook-registry`, after the Work Mode that removes `.guppi/guppi/links.py`.

> **then:**
> No file `.guppi/links.md` stands, and no `SessionStart` hook of `.claude/settings.json` runs `guppi links --write`.
> **＋** `uv run --project .guppi guppi links` prints that the command is unknown and exits 2.
> **＋** `entity-link-graph`, `rule-link-graph-at-session-start`, `estimate-link-graph-prints-the-neighbours` and `estimate-link-graph-at-session-start-writes-the-file` stand in the archive, and no live page lists them in a field.
> **＋** No live page of `vault/wiki/`, no file of `.claude/` and no file of `.guppi/guppi/` or `.guppi/tests/` names `.guppi/links.md` or `guppi links`, or counts the graph of the links among the parts of GUPPI or of its harness, outside History lines, a `## Result`, a lesson, the pages under `vault/wiki/decisions/`, `log.md`, `brief.md` and `estimate-sprint-plugin-link-graph-is-gone`.
> **＋** `uv run --project .guppi guppi test` reports no failed test.

```then
create:
- slug: estimate-sprint-plugin-link-graph-is-gone
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether, after the librarian's run that deletes the graph of links, no .guppi/links.md, no command guppi links and no SessionStart hook for it stand, its pages and Estimates are archived, no live text names them and the tests pass
  method: 'by hand, after the librarian''s run that applies the delete of entity-link-graph and renders .claude/settings.json: the output of uv run --project .guppi guppi links entity-guppi, of git status, of uv run --project .guppi guppi test and of a Grep for links.md, guppi links and graph of the links over vault/wiki/, .claude/, .guppi/guppi/ and .guppi/tests/, and the SessionStart key of .claude/settings.json, read against the Criterion, the outputs in the estimate line'
  once: true
  tags:
  - sprint
  - harness
update:
- slug: rule-hook-registry
  replace:
  - old: '{ "type": "command", "command": "uv run --project .guppi guppi render --sync", "timeout": 60 }, { "type": "command", "command": "uv run --project .guppi guppi links --write", "timeout": 60 } ] },'
    new: '{ "type": "command", "command": "uv run --project .guppi guppi render --sync", "timeout": 60 } ] },'
  change: the SessionStart hook guppi links --write removed with the graph of links
- slug: entity-guppi
  set:
    purpose: GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint and the glossary, and in the repository of GUPPI also that repository on GitHub
  replace:
  - old: Its parts are the sprint as a kind (`entity-sprint`), the glossary (`entity-glossary`) and the graph of the links between the pages and the harness files (`entity-link-graph`), the things of GUPPI that are not rules (as set in case 967.1).
    new: Its parts are the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of GUPPI that are not rules.
  change: the graph of links is no longer a part of GUPPI
- slug: rule-harness
  replace:
  - old: the hooks that read a page of the vault without its History, the hook that writes the graph of the links between the pages and the harness files at the start of a session, and the file under
    new: the hooks that read a page of the vault without its History, and the file under
  - old: 796, 967.3; in the repository of GUPPI
    new: 796; in the repository of GUPPI
  change: the hook that writes the graph of links at the start of a session is no longer a part of the harness
delete:
- slug: entity-link-graph
  impact: the graph of links goes; case-guppi searches the names of what it changes instead (case 999.2); estimate-link-graph-prints-the-neighbours goes with it
- slug: rule-link-graph-at-session-start
  impact: the SessionStart hook guppi links --write goes from rule-hook-registry; estimate-link-graph-at-session-start-writes-the-file goes with it
- slug: estimate-link-graph-prints-the-neighbours
  impact: its target entity-link-graph is deleted; estimate-sprint-plugin-check-finds-no-bare-slug-link is read before the move
- slug: estimate-link-graph-at-session-start-writes-the-file
  impact: its target rule-link-graph-at-session-start is deleted
```

```tasks
- [x] delete `entity-link-graph`
- [x] delete `rule-link-graph-at-session-start`
- [x] delete `estimate-link-graph-prints-the-neighbours`
- [x] delete `estimate-link-graph-at-session-start-writes-the-file`
- [x] update `rule-hook-registry`
- [x] update `entity-guppi`
- [x] update `rule-harness`
- [x] create `estimate-sprint-plugin-link-graph-is-gone`
- [x] `.guppi/guppi/links.py` and `.guppi/tests/test_links.py`: deleted.
- [x] `.guppi/guppi/cli.py`: the import of `links`, the entry `"links"` of `COMMANDS` and the words on `links --write` in the module docstring removed.
- [x] `.guppi/guppi/pages.py`: `links` removed from the list of readers in the module docstring.
- [x] `.guppi/guppi/ship.py`: the entry `.guppi/links.md` of `LEFT_OUT` and its comment removed.
- [x] `.guppi/.gitignore`: the line `links.md` removed.
- [x] by hand, in Work Mode after the code tasks above: the local file `.guppi/links.md` deleted.
- [x] `uv run --project .guppi guppi render`: `.claude/settings.json`
- [x] `uv run --project .guppi guppi sprint`
- [x] read `estimate-sprint-plugin-check-finds-no-bare-slug-link`
- [ ] read `estimate-sprint-plugin-link-graph-is-gone`
```

### Case 999.2 — case-guppi searches the names of each page and file it changes

> **given:**
> `rule-case-build`: the Render of `.claude/agents/case-guppi.md`, whose step on the graph is replaced.
> **＋** `estimate-case-build-reads-the-link-graph-of-what-it-changes`: the failed Estimate, renamed, its Criterion, `purpose` and `method` replaced.
> **＋** `.guppi/guppi/cli.py`: `COMMANDS`, which maps each command to its module.
> **＋** `rule-search-leaves-out-decisions`: the hook that leaves the Decision pages out of a Grep over the repository.
> **＋** `rule-estimates-schema`: the rule of the field `method` and of the word `first` in it.
> **＋** `rule-case-protocol`: the rule of a `method` part that waits for an event it names.
> **＋** `vault/wiki/`: the live pages, which the search of names covers.
> **＋** `.guppi/tests/`: the tests, which the search of names covers.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and answers with its summary.

> **then:**
> For each page and file the Case changes that exists before the Case, it searches in one Grep that prints only the paths of the files, over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/`, for all its names.
> **＋** The names of a page are its slug, the file name of each path of its `governs`, `implementation_ref` and `code_ref`, the name of the agent or of the skill with its slash whose file its `governs` names, and `guppi <command>` for each command that `COMMANDS` of `.guppi/guppi/cli.py` maps to a module of those paths; the names of a file are its file name and the agent, skill or command it carries.
> **＋** It prints the purpose line of each page on that list by one more Grep over those pages.
> **＋** It opens each file of the list whose purpose line, or whose path where it has none, bears on the change.
> **＋** At the check of the finished Case, it searches the names of each page and file the tasks of the Case change that it has not searched in that build.
> **＋** Each file that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in `log.md` or `brief.md` is not opened.

```then
update:
- slug: rule-case-build
  replace:
  - old: 'Read too, for each page and file the Case changes that exists before the Case, its block in `.guppi/links.md`, the graph of the links between the pages and the harness files that a hook writes at the start of the session: find its line `## <slug or path>` by a Grep with its line number, read the block whole by a Read from that line to the next line that opens with `## `, and read on where the block goes past the limit of that Read; read the purpose line of each neighbour it names, out and in, and open each neighbour whose purpose line bears on the change, whole or in parts as the paragraph that opens with the reading of `vault/wiki/case-schema.md` sets for its kind of text; each one the change makes false enters the Case, or `context` names it and says why it stands, and where the file is missing or holds no block of such a page or file, `context` says so; a page or file the Case creates has no block yet, and `context` says nothing of it (as set in cases 967.2 and 986).'
    new: 'Find too, for each page and file the Case changes that exists before the Case, each file that names it, since a text may point to it by another name than its slug: take its names — for a page its slug, the file name of each path of its `governs`, `implementation_ref` and `code_ref`, such as `prespec.py` for `.guppi/guppi/prespec.py`, the name of the agent, such as `case-guppi`, or of the skill with its slash, such as `/pre-spec`, whose file its `governs` names, and `guppi <command>` for each command that `COMMANDS` of `.guppi/guppi/cli.py` maps to a module of those paths; for a file its file name and the name of the agent, the skill or the command it carries — and search for all the names of the Case at once by one Grep in the mode that prints only the paths of the files, its path the root of the repository and its glob `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**`; then print the purpose line of each page on that list by one Grep of `^(purpose|root_cause|pattern):` in the mode that prints the lines, its path `vault/wiki/` and its glob `**/{<slug>,<slug>}.md` with the bare slug of each page on the list and no folder before it, since a brace list of paths with their folders matches nothing, and open each file of the list whose purpose line, or whose path where it has none, bears on the change, whole or in parts as the paragraph that opens with the reading of `vault/wiki/case-schema.md` sets for its kind of text, leaving out `log.md` and `brief.md`; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in case 999.2).'
  - old: List each page and file that the tasks of the Case change, and read the block in `.guppi/links.md` of each one that exists before the Case and whose block you have not read in this build, as the paragraph on the frame of the Case sets it (as set in case 986).
    new: List each page and file that the tasks of the Case change, and search the names of each one that exists before the Case and whose names you have not searched in this build, as the paragraph on the frame of the Case sets it (as set in cases 986 and 999.2).
  change: case-guppi finds what points to a page or file it changes by one Grep for all its names and the purpose lines of the pages it lists, instead of the block of .guppi/links.md
- slug: estimate-case-build-reads-the-link-graph-of-what-it-changes
  rename: estimate-case-build-searches-the-names-of-what-it-changes
  set:
    status: pending
    purpose: Whether case-guppi searches in one Grep that prints only file paths for all the names of each page and file its Case changes that exists before the Case, again at the check of the finished Case for each one it has not searched, prints the purpose lines of the pages on that list, and opens each file that bears on the change
    method: 'by hand, after the /pre-spec of a session whose case-guppi runs on the Render of rule-case-build that searches the names of each page and file a Case changes: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether one Grep that prints file paths covers all the names of each existing page and file the tasks of the Case change, whether a Grep printed the purpose lines of the pages on its list, and whether each file that bears on the change is opened or named in context; the count and the transcripts in the estimate line'
  change: renamed and the Criterion replaced whole — case-guppi searches the names of what it changes, since the graph of links is dropped; pending again after the failed reading of session 2227
```

```tasks
- [x] update `rule-case-build`
- [x] update `estimate-case-build-reads-the-link-graph-of-what-it-changes`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-searches-the-names-of-what-it-changes`
```
