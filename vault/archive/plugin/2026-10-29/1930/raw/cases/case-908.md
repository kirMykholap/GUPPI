## Case 908 — Three checks name the transcripts folder and the chat language by role

> **context:**
> `guppi ship` writes each `passed` Estimate whose target page it ships into the clean version of GUPPI, with its Criterion as it stands here. The reading of `estimate-clean-branch-ships-neutral-texts` at the `/hi` of this session (ledger line 1, `passed`) lists Criterion sentences that hold only in the repository of GUPPI, for a Case of a later session to rewrite. Six of them stand under the defer of `decision-case-893.1` on `rule-clean-branch`, which waited because a replaced Criterion sets its Estimate `pending`, and the cascade of `generate` sets its rule `built` only once every Estimate passes (`vault/wiki/rules/schema.yaml`, the `status` field); while a rule with `core: true` stands `draft`, `guppi ship <folder>` writes nothing to `prod`, as `rule-clean-branch` sets it. The brief names a seventh Estimate, `estimate-glossary-terms-defined`; this session's reading does not list it, so its Criterion stands. The person chose to rewrite now only the two whose cost is small. `estimate-permissions` names the transcripts folder of GUPPI, `c--PROJECTS-GUPPI`, in four sentences; its `method` waits for a Case file that `case-guppi` writes in Plan Mode, which this session holds, so the Retro of this session can read it and `rule-permissions` stands `draft` only until then. The Purpose of `rule-permissions` says that the clean version brings the read rules of GUPPI's folder until the setup Case of `rule-morph` sets the project's own, so the new sentences name the folder that the Render of `rule-permissions` names. `estimate-permissions` carries no `purpose`, which `vault/wiki/estimates/schema.yaml` keeps optional, and its `method` names the folder by role already, so both stand. `estimate-orchestration-forwards-a-discussion-question` says that the answer is shown translated into Russian; `rule-orchestration` already stands `draft`. Its `method` waited for "a later session", which `vault/wiki/case-schema.md` does not accept for a `method` (cases 670.4, 781), and it read the evidence in a transcript, which `/hi` may not open, since `.claude/skills/hi/SKILL.md` says that `/hi` reads no transcript of an earlier session (case 670.5). So, by the person's answer to a finding of `/pre-spec`, Case 908.2 sets it to be read at the Retro of a session that holds such a question, from the tool calls of that session. I read `waits_for_an_event`, `waits_for_another_session`, `waits_for_a_later_moment`, `tied_to_a_one_off_moment` and `check_unread` of `.guppi/guppi/lint.py`: the new `method` names no later session, the librarian or `/hi`, so `waits_for_another_session` does not match it; it holds no "first", so `tied_to_a_one_off_moment` does not match; and it does not open with `after`, so `waits_for_a_later_moment` is false and `check_unread` gives `unread: pending` on the page until its reading, which is red by design. By the person's answer to another finding of `/pre-spec`, Case 908.3 replaces the Criterion of `estimate-orchestration-shows-the-built-case`, which names Russian as the language in which the main agent shows a round, the name of a Case and its short text. That page already stands `pending` and `rule-orchestration` already stands `draft`, so no status changes. Its `method` and `purpose` speak of the reading of the Render and of the showing, not of the language, so both stand. Its Criterion and that of `estimate-orchestration-forwards-a-discussion-question` already share their lines on a plain explanation, on a `**Fact:**` answer and on the translation of what `case-guppi` answers: one checks every showing of the main agent, the other the path of a discussion question alone, so each sub-case keeps the lines of the Criterion it replaces, and the two new texts name the language alike, by role. The other four, `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`, `estimate-ask-query-before-a-create` and `estimate-compact-recall-reloads`, keep their text: their readings wait for events that may not come for a long time, and their rules stand `built` with `core: true`. So the defer of `decision-case-893.1` stays, and no line of this Case carries a mark that retires it; its text still names the two Estimates rewritten here, and the next reading of `estimate-clean-branch-ships-neutral-texts` no longer lists them. The Render of `rule-orchestration` on its rule page says that the main agent shows that reply translated into `{{chat_lang}}`, a value that the render fills from `rule-guppi-config`; only the rendered `vault/wiki/orchestration.md` holds the word Russian, so the rule names the language by role already, and this Case changes no rule page. A Grep of `estimate-permissions|estimate-orchestration-forwards-a-discussion-question|estimate-orchestration-shows-the-built-case` over `vault/wiki/` printed `brief.md`, `log.md`, `estimates/estimate-case-protocol-case-form.md`, `estimates/estimate-clean-branch-ships-neutral-texts.md`, `rules/rule-permissions.md` and `rules/rule-orchestration.md`; the hits in the two rules are their `estimates` field and a History line, the one in `estimate-case-protocol-case-form` is a History line, and the one in `estimate-clean-branch-ships-neutral-texts` is its Result, so all stand; over `.claude/` and `.guppi/` it printed nothing. A Grep of `wiki_root\(REPO|read_vault\(.*REPO|REPO / "vault"|ship\.ship\(REPO|estimates/estimate-` over `.guppi/tests/` printed `test_ship.py`, `test_generate.py`, `test_sprint_close.py`, `test_lint.py`, `test_guppi_package.py` and `test_schemas.py`. Of them, `test_ship.py` and `test_guppi_package.py` read the live vault: the live build of `test_ship.py` asserts no line on a page under `vault/wiki/estimates/`, and a `pending` Estimate is not shipped; `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` looks for old commands and paths that the new texts do not add. The others build pages of their own. No new Estimate is created: each sub-case replaces the Criterion of the Estimate it rewrites, and that Estimate checks it.

> **problem:**
> Two shipped checks hold a sentence that is false in a project that installed GUPPI: one names GUPPI's own transcripts folder, the other names Russian as the language of the chat, and a third check, of how a built Case is shown, names Russian too. The other four under the same defer wait, since a replaced Criterion would hold their rules `draft` for a long time.

> **recommend:**
> - **Which checks this Case rewrites**
>   - Recommended: (a) the six of the defer; the glossary check keeps its text, since this session's reading did not list it.
>   - Answer: agreed, (a).
> - **When the new texts come in**
>   - Recommended: (b) now only `estimate-permissions`, read at the Retro of this session, and `estimate-orchestration-forwards-a-discussion-question`, whose rule is already `draft`; the other four keep their text under the defer.
>   - Answer: agreed, (b).
> - **When the discussion-question check is read**
>   - Recommended: (a) the `method` names its event: by hand, after a question of the person to discuss an item.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the allow list holds one Read rule for all the paths under the transcripts folder, not one per path.
>   - Taken: the first `then` line of Case 908.1 says a Read rule for the paths under it.
> - **Change**
>   - Asked: at `/pre-spec`, the Render on the page of `rule-orchestration` names the language by a placeholder; only the rendered file holds Russian.
>   - Taken: the `context` states that fact.
> - **Change**
>   - Asked: at `/pre-spec`, the discussion-question check is read at the Retro of a session that holds such a question, from the tool calls of that session, since `/hi` reads no transcript of an earlier session.
>   - Taken: Case 908.2 sets its `method` so.
> - **Change**
>   - Asked: at `/pre-spec`, `estimate-orchestration-shows-the-built-case` names Russian as the chat language too; add a sub-case that replaces its Criterion whole, with no change of status.
>   - Taken: Case 908.3 replaces it with the chat language named by role.

### Case 908.1 — The permissions check names the transcripts folder by role

> **given:**
> `estimate-permissions`: its Criterion is replaced whole.
> **＋** `rule-permissions`: the rule whose Render writes the allow list and names the transcripts folder.
> **＋** `.claude/settings.json`: the settings file whose allow list the check reads.
> **＋** `.guppi/tests/test_render.py`: its JSON case fixes the shape of the block.
> **＋** `rule-spec-reconcile`: its guard writes the file of a Case of `case-guppi`.
> **＋** `vault/raw/**`: the working files of the session.
> **＋** `vault/wiki/brief.md`: the brief that the session writes.
> **＋** `cases/`: the folder of the files of the Cases, kept off the allow list.
> **＋** `~/.claude/projects/`: the folder that holds the saved transcripts of each project.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder of saved transcripts under `~/.claude/projects/` that the Render of `rule-permissions` names, that folder itself as its path or a path under it.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, a Read rule for the folder of saved transcripts that the Render of `rule-permissions` names, and a Read rule for the paths under it.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `.guppi/tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only: the reading line records it from the person, never from the agent, whose reply does not tell an approved call from one not asked.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** A Read, Grep or Glob whose path is that folder itself or a path under it runs with no prompt, in Plan Mode too.
> **＋** `case-guppi` writes the file of its Case with no prompt in Plan Mode, since the guard of `rule-spec-reconcile` makes the write and stops its call.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** An error of the guard of `rule-spec-reconcile` while it writes that file lets the call run, and the client may ask the person that one time; that prompt is not a finding and not a `failed`.
> **－** A Read, Grep or Glob of `case-guppi` on a path outside the project that no rule of the allow list names is not bound by this Criterion: it may ask the person.
> **－** `deny` and `ask` are empty; nothing else under `vault/wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names that folder.

> **tasks:**
> - [ ] update `estimate-permissions`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the transcripts folder is named as the one the Render of rule-permissions names, not by the folder name of the repository of GUPPI`
> - [ ] read `estimate-permissions`

> **ratification:**
> ```
> - decision[case 908.1][update][estimate-permissions]{ref:rule-permissions}
> ```

### Case 908.2 — The discussion-question check names the chat language by role

> **given:**
> `estimate-orchestration-forwards-a-discussion-question`: its Criterion and its `method` are replaced.
> **＋** `rule-orchestration`: the rule rendered into `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: the Render that sets how a discussion question is passed on.
> **＋** `case-guppi`: the agent that built the Case of the item.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill that explains a text in plain words.
> **＋** `rule-case-check`: the rule of the hook that reads the answers of `case-guppi`.

> **when:**
> In Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to discuss an item whose `case-guppi` is building its Case or has shown it, or to learn something of that item, and the question is no request for a plain explanation of the agent's text.

> **then:**
> The main agent sends the question to that `case-guppi` by `SendMessage`, verbatim and untranslated, and makes no `Read`, `Grep` or `Glob` call of its own to answer it.
> **＋** `case-guppi` answers in plain words under a first line `**Fact:**`, with no Case heading and no round, from the pages it read, or with a round when the question opens a fork.
> **＋** The main agent shows the answer translated into the language of the chat, then asks again the question that stood open: the open question of the round, or the sign-off of the shown Case.
> **－** A request for a plain explanation of a round, of the short text on a Case or of a reply stays with `.claude/skills/wait-what/SKILL.md`.
> **－** A `**Fact:**` answer changes nothing of the round or of the Case, and the hook of `rule-case-check` reads it as no Case.

> **tasks:**
> - [ ] update `estimate-orchestration-forwards-a-discussion-question`
>   - set:
>     ```
>     status: pending
>     method: "by hand, at the Retro of a session that holds a question of the person in the chat to discuss an item whose case-guppi is building its Case or has shown it: the SendMessage call, the tool calls of the main agent and the answer, read in that session"
>     ```
>   - change: `the Criterion replaced whole — the answer is shown in the language of the chat, not named as Russian; the method is read at the Retro of a session that holds such a question, from its own tool calls, not in the transcript of a later session`
> - [ ] read `estimate-orchestration-forwards-a-discussion-question`

> **ratification:**
> ```
> - decision[case 908.2][update][estimate-orchestration-forwards-a-discussion-question]{ref:rule-orchestration}
> ```

### Case 908.3 — The showing check names the chat language by role

> **given:**
> `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `rule-orchestration`: the rule rendered into `vault/wiki/orchestration.md`, which sets how a Case is dispatched and shown.
> **＋** `case-guppi`: the agent that builds each Case and its rounds, and `ask-guppi`, which runs only at pre-spec.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`, `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the session the showing reads or closes.
> **＋** `.claude/skills/wait-what/SKILL.md` and `.claude/skills/grill-me/SKILL.md`: the skills of a plain explanation and of the shape of a round.
> **＋** `rule-case-check`, `rule-prespec-onward` and `rule-spec-box`: the rules of the hooks of a showing, of the count of a ratified Case, and of a `/work` that `/box` calls.
> **＋** `uv run --project .guppi guppi caseid --next --session <stamp>`: the command that prints the id of a new Case.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
> **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
> **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
> **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into the language of the chat line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in the language of the chat translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in the language of the chat, and a short text in the language of the chat on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands. In Plan Mode the main agent asks the person no question on it: it sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch; in a send of Cases built at the same time it does so after the second pass that `vault/wiki/orchestration.md` sets. Where the `case-guppi` of the other Case answers with a round instead, the round stands in the list of the rounds of the batch, as any round does. In Work Mode it asks the person whether that other Case changes.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
> **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
> **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
> **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
> **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
> **－** The main agent writes the heading, the list, the `ratification` and the send of another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
> **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.

> **tasks:**
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the round, the name of a Case and its short text are shown in the language of the chat, not named as Russian`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 908.3][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```
