<!-- approved 20:14:01 · session c3e1bea8 -->

# Session 1753 — sprint plugin

## Case 800 — case-guppi and ask-guppi close the gaps behind two lessons

> **context:**
> Session 1426 left two lessons with no fix. In `lesson-case-build-gave-a-sub-case-no-estimate`, the person answered that Case 795.1 creates no new Estimate. `case-guppi` read this as "no Estimate" and wrote the sub-case with no check. It never looked for an Estimate that already checked the change, though its frame sentence of case 561.11 asks it to name such an Estimate in `context`. The main agent sent the summary back before the showing, by case 561.9 of `rule-orchestration`. The cause is the round question on the promise: its "no new Estimate" option named no existing Estimate, so the answer could be read two ways. In `lesson-ask-guppi-read-a-decision-page-without-a-reason`, at the /pre-spec of session 1426, `ask-guppi` opened `decision-case-616`, the Decision behind the `deferred_by` of `entity-guppi`, though no finding named `entity-guppi`. Ledger line 3 of session 1426 shows that Case 795.1 updated `entity-guppi`. The frame of `ask-guppi` allows that read only when "a page in your answer" carries `deferred_by`. At /pre-spec the answer is a list of findings, and the text does not say whether the read may come before a finding names the page. The governing rule is `rule-search-leaves-out-decisions`: a Decision page is read only for a reason the frame of the agent names. A hook that refuses such reads cannot see the findings before the answer is written, so the person chose to fix the text of the rule, not to add a hook on the agent.
>
> Case 800.1 adds one sentence to the Render of `rule-case-build`. It replaces the Criterion, `purpose` and `method` of `estimate-case-build-answers-what-done-means`, the one Estimate of that page whose Criterion speaks of how a Case is checked. I read the Criterion of every Estimate the page lists. Case 800.2 adds one clause to the Render of `rule-ask`, and creates `estimate-ask-opens-a-decision-only-for-a-finding` on `rule-ask`. A Glob `vault/**/estimate-ask-opens-a-decision-only-for-a-finding.md` printed nothing, so the slug is free. The `create` has a `ref`, so no vault query runs before it. The line of `estimate-ask-finds` that a finding on a page with `deferred_by` gives the `## Problem` of its Decision stands, and the new Estimate does not repeat it. The reason of `estimate-search-leaves-out-decisions-in-every-agent`, that a page of the answer carries `deferred_by`, stays true, since a page a finding names is a page of the answer, so its Criterion stands. The `－` line of `estimate-ask-searches-at-prespec` hands Decision reads to that Estimate and stays true. The `.claude/skills/pre-spec/SKILL.md` that dispatches `ask-guppi` sets nothing about Decision reads. A Grep of `case-guppi\.md|ask-guppi\.md|rule-case-build|rule-ask\b|agents/` over `tests/` printed nothing, so no test reads the two rendered files or the two rule pages live. The `Purpose` of each rule names neither behaviour and stays. Both lessons were written in session 1426, so no decision line carries `{addresses:...}` for them (case 284.2). They stay `new` until a later lesson joins them or the close of the sprint archives them.

> **problem:**
> Two agents read a gap in their frame as permission. `case-guppi` closed the check of a sub-case on an answer that named no Estimate. `ask-guppi` opened a Decision page before any finding of its own named the page.

> **recommend:**
> - **How should case-guppi stop reading "no new Estimate" as "no Estimate"?**
>   - Recommended: (a) the question on the promise names the existing Estimate by slug, and an answer of no new Estimate closes the promise only with that Estimate named in `context`.
>   - Answer: agreed, (a).
> - **When may ask-guppi open the Decision behind a put-off page during the review?**
>   - Recommended: (a) restrict the rule: at /pre-spec, the Decision is opened only after a finding names the page, never to judge whether a finding stands.
>   - Answer: (a). In the first round the person asked why the agent opened that Decision at all, and whether the agent or the rule should be restricted.
> - **Should the two fixes be one Case with two parts, or two separate Cases?**
>   - Recommended: (a) one Case with two sub-cases.
>   - Answer: agreed, (a).
> - **How is the case-guppi fix checked?**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-answers-what-done-means`, read at the Retro of this session against the new Render.
>   - Answer: agreed, (a).
> - **How is the ask-guppi fix checked?**
>   - Recommended: (a) a new narrow Estimate on `rule-ask`, read after the next /pre-spec on the new text.
>   - Answer: agreed, (a).

### Case 800.1 — An answer of no new Estimate names the existing one

> **given:**
> `rule-case-build`: the rule of `case-guppi`; one sentence of its Render changes.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `estimate-case-build-answers-what-done-means`: its Criterion, `purpose` and `method` replaced.
> **＋** `rule-orchestration`: the main agent sends back a summary in which a Case gives no Estimate.

> **when:**
> `case-guppi` writes a Case into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`.

> **then:**
> Each Case and sub-case of the file creates an Estimate or replaces the Criterion of one, or its `context`, or its parent's, names by slug the Estimate that already checks the change and says why its Criterion stands.
> **＋** The summary that `case-guppi` answers with names that Estimate under the item of each Case and sub-case.
> **＋** A question of a round before the Case on how it is checked gives an option that names by slug the Estimate that already checks the change, where one in the `estimates` of a page the Case changes does.
> **＋** After the person answers that no new Estimate is created, the `context` names by slug the Estimate that checks the change, taken from the `estimates` of a page the Case changes.
> **＋** When the person's words and the frame give neither, `case-guppi` asks in a round, before it writes the Case, what the Estimate will check, and the `recommend` of the Case holds that question.
> **－** A deferred decision in the short form is not written by `case-guppi` and carries no such Estimate.

```then
update:
- slug: rule-case-build
  replace:
  - old: a Case that can give neither has the promise open, and you ask in a round what its Estimate will check (case 561.11).
    new: 'a Case that can give neither has the promise open, and you ask in a round what its Estimate will check (case 561.11). A question of a round on how a Case is checked gives, beside the option of a new Estimate or a replaced Criterion, an option that names by slug the Estimate that already checks the change, found in the `estimates` of each page the Case changes, where one there does; an answer that no new Estimate is created closes the promise only with that Estimate: before the summary you name it in `context` and say why its Criterion stands, and where none of those Estimates checks the change you ask again in a round what its Estimate will check (case 800.1).'
  change: an answer that no new Estimate is created closes the promise only with the existing Estimate named by slug in the round and in context (case 800.1)
- slug: estimate-case-build-answers-what-done-means
  set:
    status: pending
    purpose: Whether each Case case-guppi builds creates or replaces an Estimate or names the one that already checks the change, offers that Estimate by slug in a round on the promise, names it in context after an answer that no new Estimate is created, and asks in a round when it can do neither
    method: 'by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the round on the promise names the existing Estimate, and an answer of no new Estimate closes the promise only with it named (case 800.1)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-answers-what-done-means`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-answers-what-done-means`
```

### Case 800.2 — ask-guppi opens a deferred Decision only for a page a finding names

> **given:**
> `rule-ask`: the rule of `ask-guppi`; one sentence of its Render changes.
> **＋** `.claude/agents/ask-guppi.md`: the file rendered from `rule-ask`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill that dispatches `ask-guppi` at `/pre-spec`.
> **＋** `vault/wiki/decisions/`: the folder of the Decision pages.
> **＋** `estimate-ask-opens-a-decision-only-for-a-finding`: the new check of when `ask-guppi` opens a Decision at `/pre-spec`.
> **＋** `rule-search-leaves-out-decisions`: a Decision page is read only for a reason the frame of the agent names.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the check of Decision reads in every agent, which stands.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> Each page under `vault/wiki/decisions/` that `ask-guppi` reads, by a Read or by a Grep inside that folder, for a page that carries `deferred_by`, is the Decision of a page that a finding of its answer names.
> **＋** A page that carries `deferred_by` and stands in no finding has its Decision left unread, also when a Case of the plan changes that page.
> **－** A Decision read because the question asks why something was decided, reached through the `origin` of a page, is outside this promise.
> **－** Decision reads by the main agent and by `case-guppi` are outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads them.

```then
create:
- slug: estimate-ask-opens-a-decision-only-for-a-finding
  ref: rule-ask
  kind: QA
  purpose: Whether ask-guppi at /pre-spec opens the Decision behind a page with deferred_by only for a page that a finding of its answer names
  method: 'by hand, after a /pre-spec whose ask-guppi runs on .claude/agents/ask-guppi.md as rendered by case 800.2: the Read and Grep calls of ask-guppi on vault/wiki/decisions/ in its agent transcript and the findings of its answer read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-ask
  replace:
  - old: since a deferred decision is something already decided; or the question asks why something was decided
    new: since a deferred decision is something already decided; at `/pre-spec` you open it only after a finding of yours names the page, never to judge whether a finding stands, and a page that carries `deferred_by` and stands in no finding has its Decision left closed (case 800.2); or the question asks why something was decided
  change: at /pre-spec the Decision of a page with deferred_by is opened only after a finding names the page (case 800.2)
```

```tasks
- [ ] update `rule-ask`
- [ ] create `estimate-ask-opens-a-decision-only-for-a-finding`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] read `estimate-ask-opens-a-decision-only-for-a-finding`
```

## Case 801 — case-guppi quotes the last output of a check with its source

> **context:**
> Where an option of a round rests on whether a check passes, such as `make lint`, `case-guppi` reads what that check printed at its last run, as the brief reports it, before it recommends the option. Case 798.2 put this into the Render of `rule-case-build` and created `estimate-case-build-reads-the-last-output-of-a-check`. The two texts part on one word. The Render says that `context` names that output. The first Then line of the Criterion says that `case-guppi` quotes it with its source in the `context`. At the Retro of session 1426 the reading of the new Render against the Criterion was `failed` for this gap (ledger line 28 of session 1426). The brief reports the last `make lint` under `## Flags` as two lines, one of them `estimates/estimate-case-build-reads-the-last-output-of-a-check: unread: failed`. By the person's answers, the Render takes the word of the Criterion, and the Criterion stands as it is written.
>
> The governing rule is `rule-agent-writing`: a claim names a real source, and is no wider than the output it rests on. Quoting the output with its source keeps to it. A bare name of the output would also name a source, but the person could not see what the output said. This Case replaces one sentence of the Render, the sentence of case 798.2, and adds case 801 to its source mark. The other sentences of the Render that speak of reading before a recommendation stand. The sentence of case 798.1 says that `context` names the rule, not an output. The sentence of case 797.1 sets the state at the moment a check runs, which the sentence of case 798.2 still points to. Case 800.1 of this session adds a sentence to the same Render, after the sentence of case 561.11. Its `old` and this Case's `old` share no words, and the two new texts speak of different things. The update of the Estimate writes its Criterion back whole as this Case's `when` and `then`, the same text as now, so that it is `pending` again. Its `purpose` says that `case-guppi` names the output, so the update sets it anew. Its `method`, a reading of the new Render in the Spec at the Retro of the session, stands. The `## Result` keeps the failed reading until the next reading. A Grep `names that output|last output of a check|reads-the-last-output` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `.claude/agents/case-guppi.md`, `vault/wiki/log.md`, `vault/wiki/insights/insight-case-build-recommends-without-reading-the-governing-rule.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-reads-the-last-output-of-a-check.md`. The hit in the insight is a History line, and the brief and the log are not read. The render writes the agent file again. A Grep `case-guppi\.md|rule-case-build|reads-the-last-output` over `tests/` printed nothing, so no test reads the agent file or the two pages live.

> **problem:**
> The instruction of `case-guppi` and the Estimate that checks it disagree. The instruction lets `context` only name the last output of a check, while the Criterion asks that `context` quotes it with its source. The reading failed, and `make lint` flags the Estimate.

> **recommend:**
> - **Which text changes: the instruction or the check?**
>   - Recommended: (a) the instruction says that `context` quotes the output with its source; the Criterion stands.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (a) set the same Estimate back to `pending`, and read it again at the Retro of this session against the new instruction text.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`; one sentence of its Render changes.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `vault/wiki/brief.md`: its `## Flags` and `## Readings at the close` hold the last output of `make lint` and `make test`.
> **＋** `estimate-case-build-reads-the-last-output-of-a-check`: its Criterion is written again whole and its `purpose` is set anew.
> **＋** `rule-agent-writing`: a claim names a real source.
> **＋** `rule-case-protocol`: the form of `context`.
> **＋** `vault/raw/2026-10-13/1753/cases/case-800.md`: Case 800.1 changes another sentence of the same Render.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, writes a round with an option that rests on whether a check passes, such as `make lint`, `make test` or a check on GitHub.

> **then:**
> Before it recommends that option, it reads what that check printed at its last run, as `## Flags` and `## Readings at the close` of `vault/wiki/brief.md` report it, judges the option against that output, and quotes it with its source in the `context`.
> **＋** Where another Case of the same session changes that check or the pages it reads, it judges the option by the state at the moment the check runs, as `rule-case-build` sets it for such a Case, and not by the last output alone.
> **＋** Where the brief does not report that output, the `**After:**` line of the option and the `context` say that its last output was not read.
> **－** An option whose last output was not read may still be recommended.

```then
update:
- slug: rule-case-build
  replace:
  - old: '`context` names that output, and where the brief does not report it, the `**After:**` line of the option and `context` say that its last output was not read, and the option may still be recommended (case 798.2).'
    new: '`context` quotes that output with its source, and where the brief does not report it, the `**After:**` line of the option and `context` say that its last output was not read, and the option may still be recommended (cases 798.2, 801).'
  change: context quotes the last output of a check with its source, as the Criterion of estimate-case-build-reads-the-last-output-of-a-check asks (case 801)
- slug: estimate-case-build-reads-the-last-output-of-a-check
  set:
    status: pending
    purpose: Whether case-guppi, before it recommends an option that rests on whether a check passes, reads what that check printed at its last run, from the brief, judges the option against it, or by the state at the moment the check runs where another Case of the session changes the check or the pages it reads, and quotes it with its source in context, or says in the After line and context that the output was not read
  change: the Criterion written again whole and the purpose set to quote the output with its source, after the failed reading of session 1426 (case 801)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-reads-the-last-output-of-a-check`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-reads-the-last-output-of-a-check`
```

## Case 802 — The first /hi of a new install sets the project up through one Case

> **context:**
> `rule-morph` is the step that sets GUPPI up when someone installs it in their own project. Since case 239 it has been a placeholder with only a Purpose, and it was put off four times. Some settings name this one machine or this one project. The read rules of `rule-permissions` name the folder `c--PROJECTS-GUPPI` of the saved transcripts. `guppi/box.py` holds the branch name `main` as `SHARED_NEVER`. On another person's machine these values are wrong. In the first round the person agreed with each recommendation. The install step is a skill whose answers become one Case that the person ratifies, so nothing changes outside a ratified Decision, as `rule-ratification` sets it. It runs at the first `/hi` in a project whose settings lack the answers. It finds the branch, the remote and the transcripts folder for itself, and asks only for the rest. The category set leaves `rule-morph` for a backlog line of its own. A project with code of its own gets its pages one Case at a time, not at install. That growth is a change to `rule-case-build`, which the main agent dispatches as a Case of its own. This session writes the design and the check. The skill is built in the milestone The plugin of `entity-sprint-plugin`. In the second round the person agreed with two more points. A Case lives only inside a session that `/hi` opened, so the install Case is the first Case of the first session. The category set waits as a plain line in the `## Backlog` of `entity-sprint-plugin`.
>
> This Case takes up the deferred page. Its decision line on `rule-morph` carries one `{supersedes:case N}` for each Case in its `deferred_by`: 239, 745, 750 and 758. Its Purpose and its `purpose` are written anew. Once the marks clear `deferred_by` and the page gains an Estimate, `is_placeholder` of `guppi/lint.py` no longer holds, and the schema of `rule-rules-schema` requires `kind` and `tags`, which the placeholder lacks; the `update` sets `kind: Leaf` and the tags. The page names no `enforcement`, which the schema leaves optional, since the Case that builds the skill sets how the rule has force. Case 804.5 of this session sets `core: true` on the same page by a decision line of its own, a field that this Case does not touch (`vault/raw/2026-10-13/1753/cases/case-804.md`). The milestone The plugin of `entity-sprint-plugin` named no line for the install step, so the `update` adds the line `[[rule-morph]]` under it, beside the line on the clean version made into a plugin, and `guppi sprint` writes `sprint.md` again. Case 804 changes other lines of that page. The last `make lint`, under `## Flags` of `vault/wiki/brief.md`, printed `rules/rule-morph: deferred: 4 times since case 239`; the marks clear that defer at the librarian's run. `estimate-morph-sets-up-the-project-at-the-first-hi` is the check. A Glob `vault/**/estimate-morph*` printed nothing, so the slug is free. The `create` has a `ref`, so no vault query runs before it. Its `method` waits for the session whose Work Mode builds the skill, in the `after` form of case 781. A Grep `category set|categories as data|at install|initiation` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `vault/wiki/backlog.md`, `vault/wiki/rules/rule-morph.md`, `vault/wiki/rules/rule-permissions.md` and `vault/wiki/rules/rule-guppi-config.md`. The same Grep over `.claude/` printed nothing. The Purpose of `rule-guppi-config` says that the category set stays with `rule-morph`, so this Case changes that sentence. Its one Estimate, `estimate-guppi-config-fills-the-languages`, speaks of the render of the languages, not of the install, and stands. The sentence of `rule-permissions` that leaves the folder name of another install to `rule-morph` stays true. `vault/wiki/backlog.md` is written by `guppi backlog` at the librarian's run, from the pages and the sprint Backlog. `/hi`, set by `rule-skill-hi`, changes only when the skill is built. The Criterion of `estimate-sprint-plugin-installs-as-a-plugin`, that `/hi` opens a working session in an empty project, stays true: the install Case comes inside that session. No other Estimate of `entity-sprint-plugin` speaks of its Backlog. A Grep `rule-morph|rule-guppi-config|entity-sprint-plugin` over `tests/` printed `tests/test_config.py`, `tests/test_lint.py`, `tests/test_prespec.py` and `tests/test_render.py`. Each one names a slug in a string, or writes a copy of a page under a temporary folder. No test reads the three pages live.

> **problem:**
> GUPPI has no step that sets a new install up. A second person's project would run on the settings of this machine, and the plan for that step is still a placeholder that has been put off again and again.

> **recommend:**
> - **What is the install step, and how do its answers become settings?**
>   - Recommended: (a) a skill whose answers become the project's first Case; the person ratifies it, and the render writes the settings files.
>   - Answer: agreed, (a).
> - **When does the install step run?**
>   - Recommended: (a) `/hi` starts it when the settings are missing.
>   - Answer: agreed, (a).
> - **What does the install step ask, and what does it find for itself?**
>   - Recommended: (a) it finds the branch, the remote and the transcripts folder, asks the rest, and shows every value in the one Case.
>   - Answer: agreed, (a).
> - **Does choosing the category set stay part of the install step?**
>   - Recommended: (a) move it out to its own backlog item; every project uses the development set.
>   - Answer: agreed, (a).
> - **How do pages grow in a project that already has code?**
>   - Recommended: (a) each Case covers the code it touches: `case-guppi` reads code that no page covers, and offers in a round a page for the thing the Case changes alone.
>   - Answer: agreed, (a).
> - **One Case or two?**
>   - Recommended: (a) two separate Cases: this one on the install step, page growth as its own Case on `rule-case-build`.
>   - Answer: agreed, (a).
> - **What does this session deliver for the install step?**
>   - Recommended: (a) write the design now and the check the built skill must pass; build it in the milestone The plugin.
>   - Answer: agreed, (a).
> - **Where does the install step run in relation to the session that `/hi` opens?**
>   - Recommended: (a) the install Case is the first Case of the first session, and the Work Mode of that session writes the settings.
>   - Answer: agreed, (a).
> - **Where does the category set wait as its own backlog item?**
>   - Recommended: (a) a plain line in the `## Backlog` of `entity-sprint-plugin`.
>   - Answer: agreed, (a).

> **given:**
> `rule-morph`: the install step; its Purpose is written anew.
> **＋** `estimate-morph-sets-up-the-project-at-the-first-hi`: the new check of the install step.
> **＋** `rule-skill-hi`: the skill `/hi`, which opens the session and writes `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** `rule-guppi-config`: renders `guppi.toml`, which holds `documentation_lang` and `chat_lang`; one sentence of its Purpose changes.
> **＋** `rule-permissions`: renders the read rules of the folder of saved transcripts under `~/.claude/projects`.
> **＋** `entity-sprint-plugin`: the sprint page; its milestone The plugin names `rule-morph`, and its `## Backlog` takes the category set.
> **＋** `rule-ratification`: nothing changes without a ratified Decision.
> **＋** `vault/raw/2026-10-13/1753/cases/case-804.md`: Case 804 sets `core` on `rule-morph` and changes other lines of `entity-sprint-plugin`.

> **when:**
> In a project with GUPPI installed, whose settings hold no answers of the install step of `rule-morph`, the person types `/hi`.

> **then:**
> `/hi` opens the session as `rule-skill-hi` sets it, and puts the install Case first, before the items of `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** The install step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
> **＋** It asks the person only for the values it cannot find, such as `documentation_lang` and `chat_lang`.
> **＋** Every value stands in that one install Case, which the person ratifies or corrects.
> **＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config` and the read rules of the saved transcripts from `rule-permissions`.
> **－** No settings file changes before the person ratifies the install Case.
> **－** The install step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
> **－** The install step reads no code of the project and creates no page for it.
> **－** A project whose settings hold the answers gets no install Case at `/hi`.

```then
create:
- slug: estimate-morph-sets-up-the-project-at-the-first-hi
  ref: rule-morph
  kind: QA
  purpose: Whether the first /hi of a project with no answers in its settings puts one install Case first, with the values it finds and the values the person gives, and whether the settings change only by the render after that Case is ratified
  method: 'by hand, after the session whose Work Mode builds the install skill of rule-morph: /hi typed in an empty project with GUPPI installed and no answers in its settings, the transcript of that session and the files its Work Mode writes read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - harness
  - plugin
update:
- slug: rule-morph
  set:
    kind: Leaf
    purpose: 'Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi of a project with no answers in its settings, one install Case that the person ratifies sets them'
    tags:
    - session
    - harness
    - plugin
  sections:
    Purpose: |-
      Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` of a project with no answers in its settings, one install Case that the person ratifies sets them. Some settings name one machine or one project until then: the read rules of [[rule-permissions]] name the folder of this repository's saved transcripts under `~/.claude/projects`, and the code takes the main branch to be `main` (case 693).

      The install step is a skill. `/hi` opens the session as always and, while the settings hold no answers of the install, puts the install Case first, before the Frontier: a Case lives only inside a session that `/hi` opened. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml` and [[rule-permissions]] for the read rules. No settings file changes outside that Case ([[rule-ratification]]).

      The install step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The skill is built in the milestone The plugin of [[entity-sprint-plugin]] (case 802).
  change: 'taken up: the install step is a skill at the first /hi whose answers become one ratified Case; the category set leaves for the Backlog of entity-sprint-plugin (case 802)'
- slug: rule-guppi-config
  replace:
  - old: The questions asked at install and the category set stay with `rule-morph` (case 476.1).
    new: The questions asked at install stay with `rule-morph` (cases 476.1, 802); the category set as data waits as a line of the `## Backlog` of `entity-sprint-plugin` (case 802).
  change: the category set leaves rule-morph for the Backlog of entity-sprint-plugin (case 802)
- slug: entity-sprint-plugin
  replace:
  - old: '- the clean version made into a Claude Code plugin'
    new: |-
      - the clean version made into a Claude Code plugin
      - [[rule-morph]] — the install step that the first `/hi` of a new install runs
  sections:
    Backlog: '- The category set as data: the person sets the categories of a project, the development set entity, rule, estimate by default, and the harness holds them as data, so a changed set rewrites no rule; taken out of rule-morph (case 802); the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md'
  change: the milestone The plugin names rule-morph, the install step; the Backlog takes the category set as data, out of rule-morph (case 802)
```

```tasks
- [ ] update `rule-morph`
- [ ] create `estimate-morph-sets-up-the-project-at-the-first-hi`
- [ ] update `rule-guppi-config`
- [ ] update `entity-sprint-plugin`
- [ ] `uv run guppi sprint`
- [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`
```

## Case 803 — case-guppi offers a page for code that the Case changes and no page covers

> **context:**
> Today `case-guppi` starts from the pages an item names, and reaches code only through a page field: `governs`, `implementation_ref` or `code_ref`. In a project that already has code and few pages, an item on that code finds no page, so `case-guppi` never reads the code and has nothing to build the Case on. On item C3 the person proposed that each Case read the code it touches and offer a page for it, so the pages grow Case by Case. In the round of Case 802 the person chose this over a scan of the whole codebase at install, and chose a separate Case for it. With the person's answers to the round below, the Render of `rule-case-build` gains one sentence after the sentence that reads the code a page points to. Code counts as covered when a live page names its file, or a folder that holds it, in one of the three fields. For code that no page covers, `case-guppi` reads the code, searches the pages by meaning, and offers in a round either the path added to a page that already describes the thing, or a new page for the thing the Case changes. That page is a task of the same Case, and the Estimate of the Case stands on it.
>
> The rule that governs the options is `rule-entities-schema`: a thing the developer builds is an Entity, and a part comes only from the person's words, through a Case. The new step only offers, and the person decides in the round, so the sentence on parts stands, by the person's answer. Its clause on the cut that the agent proposes in Retro is about splitting a page that already exists, not about a first page for code. The frame showed one sentence that the change makes false. The Render of `rule-case-protocol`, which is `vault/wiki/case-schema.md`, lists `code_ref` among the derivable fields that are filled mechanically and not written in a Case. A Grep `code_ref` over `guppi/` printed only `guppi/generate.py`, where the field stands in the order of the fields of an Entity, so no code fills it. The schema of entities lists it as an optional field, so a `create` or a `set` carries it. This Case takes `code_ref` out of that list and says that a Case writes it. I read that paragraph of `rule-case-protocol` whole: its first sentence names the derivable fields and the one exception, the `status` and `checked` an Estimate gets by the person's decision, and its second says that `guppi materialize` reads the blocks; the first pair leaves the list and the exception as they are without `code_ref`, and the second pair puts the sentence on `code_ref` between the two. Case 801 names `rule-case-protocol` in its `given` and writes nothing into it. Case 804.5, ratified, updates `rule-case-protocol` and `rule-case-build` by `set: {core: true}` alone, a field and no sentence, so both pairs of this Case still find their anchors once and the two Cases do not clash. A Grep `filled mechanically` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/case-schema.md` and `vault/wiki/rules/rule-case-protocol.md`, the two texts of that sentence. Neither `estimate-case-protocol-loaded` nor `estimate-case-protocol-case-form` speaks of derivable fields in its Criterion, so both stand. A Grep `code_ref` over `.claude/` printed `.claude/agents/case-guppi.md`, the rendered sentence that this Case extends.
>
> No Estimate of `rule-case-build` checks this step: I read the `purpose` of each Estimate the page lists, and the Criterion of `estimate-case-build-reads-by-need-and-in-parts` and `estimate-case-build-writes-the-case`, which speak of reading code and of the frame; the new step reads code in parts as the first one sets, so both stand. This Case creates `estimate-case-build-offers-a-page-for-code-no-page-covers`; a Glob `vault/**/estimate-case-build-offers-a-page-for-code-no-page-covers.md` printed nothing, so the slug is free. The `create` has a `ref`, so no vault query runs before it. In this project `entity-guppi` lists `guppi/` and `.claude/` in `code_ref`, so the step does not fire here, and the reading checks the text of the Render, by the person's answer. Case 800.1 and Case 801 of this session change other sentences of the same Render; their `old` texts and this one share no words, and the three new texts speak of different things. A Grep `case-guppi\.md|rule-case-build|offers-a-page` over `tests/` printed nothing. A Grep `case-schema|rule-case-protocol|Derivable` over `tests/` printed `tests/test_case_schema.py`, `tests/test_generate.py`, `tests/test_guard.py`, `tests/test_glossary.py`, `tests/test_lint.py`, `tests/test_pages.py`, `tests/test_render.py` and `tests/test_recall.py`. Only `tests/test_case_schema.py` reads the live `vault/wiki/case-schema.md`, and only while `vault/wiki/case-example.md` does not stand, for its block tagged `case`, which this Case does not touch. The other hits print the name inside seed text or a file under a temporary folder.

> **problem:**
> In a project with code that no page covers, an item on that code gives `case-guppi` no page to start from, and nothing lets it read the code or offer a page. The pages cannot grow with the Cases.

> **recommend:**
> - **When does code count as covered by a page?**
>   - Recommended: (a) a live page names its file, or a folder that holds it, in `code_ref`, `implementation_ref` or `governs`.
>   - Answer: agreed, (a).
> - **What does the round offer for code no page covers?**
>   - Recommended: (a) the path added to a page that already describes the thing, or else a new page for the thing the Case changes, its category by the schema check, with its slug, purpose, parent and paths; where the person turns both down, `case-guppi` asks which page the Case changes.
>   - Answer: agreed, (a).
> - **Where does the new page stand?**
>   - Recommended: (a) in the same Case, as a task, with the Estimate of the change on that page.
>   - Answer: agreed, (a).
> - **Does the schema sentence on page parts change?**
>   - Recommended: (a) it stands; only `rule-case-build` changes for the new step.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) a new Estimate, read by hand at the Retro of this session against the new Render in the Spec.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`; one sentence of its Render is extended.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `estimate-case-build-offers-a-page-for-code-no-page-covers`: the new check of the offer.
> **＋** `rule-case-protocol`: its Render lists the fields that a Case does not write.
> **＋** `vault/wiki/case-schema.md`: the file rendered from `rule-case-protocol`.
> **＋** `rule-entities-schema`: the category check of a new page, and a part only from the person's words.
> **＋** `vault/raw/2026-10-13/1753/cases/case-800.md`: Case 800.1 changes another sentence of the same Render.
> **＋** `vault/raw/2026-10-13/1753/cases/case-801.md`: Case 801 changes another sentence of the same Render.
> **＋** `vault/raw/2026-10-13/1753/cases/case-804.md`: Case 804.5 sets a field on `rule-case-build` and `rule-case-protocol`.

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md` as rendered from `rule-case-build`, builds a Case on an item whose words point to code, a file, a module or a function, that no live page under `vault/wiki/` names, by its file or by a folder that holds it, in `code_ref`, `implementation_ref` or `governs`.

> **then:**
> It reads that code in parts, the functions the Case changes and the places that call them, and searches the pages under `vault/wiki/` by meaning for the thing that code does.
> **＋** Before it writes the Case, a round offers a page only for the thing the Case changes, described from the code it read: where a page already describes that thing, the path added to the field of that page that lists its code; otherwise a new page, its category by the check of the schema of that category, with its slug, its one-line purpose, its parent and its paths.
> **＋** Where the person turns down both, it asks in a round which page the Case changes.
> **＋** The page the person chose, created or given the path, is a task of the same Case, and the Estimate that checks the change stands on that page.
> **－** Code that the Case does not change gets no page offered.
> **－** Code that a page names, by its file or by a folder that holds it, gets no page offered.

```then
create:
- slug: estimate-case-build-offers-a-page-for-code-no-page-covers
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi, on an item that points to code no page covers, reads that code and offers in a round a page only for the thing the Case changes, or the path added to a page that describes it, and puts the chosen page into the same Case
  method: 'by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: and the code they point to by `governs`, `implementation_ref` or `code_ref`.
    new: 'and the code they point to by `governs`, `implementation_ref` or `code_ref`. Where the item points to code, a file, a module or a function the person''s words name, that no live page covers, since no page names its file, or a folder that holds it, in `code_ref`, `implementation_ref` or `governs`, read that code as this paragraph sets for a module of code, and search the pages by meaning for the thing it does; then offer in a round a page only for the thing the Case changes, described from the code you read: where a page already describes that thing, the path added to the field of that page that lists its code; otherwise a new page, its category by the check that the schema of the category sets, with its slug, its one-line purpose, its parent and its paths. The person decides: where the person turns both down, you ask in a round which page the Case changes. The page, or the path added, is a task of the same Case, and the Estimate of the Case stands on that page; code the Case does not change gets no page (case 803).'
  change: for code that the Case changes and no page covers, case-guppi reads the code and offers in a round a page, or the path added to a page that describes the thing (case 803)
- slug: rule-case-protocol
  replace:
  - old: '`children`, `code_ref`, `deferred_by` — are filled mechanically'
    new: '`children`, `deferred_by` — are filled mechanically'
  - old: '`guppi materialize` reads the blocks, and what is not in a block was signed by nobody.'
    new: '`code_ref` is no such field: a Case writes it, on a `create` or by `set` on an `update`, when it gives a page the path of its code (case 803). `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.'
  change: 'code_ref leaves the list of derivable fields: a Case writes it when it gives a page the path of its code (case 803)'
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `rule-case-protocol`
- [ ] create `estimate-case-build-offers-a-page-for-code-no-page-covers`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-build-offers-a-page-for-code-no-page-covers`
```

## Case 804 — CI writes a clean version of GUPPI to the branch prod

> **context:**
> Other people will install GUPPI from a clean copy of this project. That copy has no pointers to the decisions of this repository and none of its session records. Today nothing builds such a copy. `.github/workflows/checks.yml` runs the style, test and lint checks, and it skips a push to `prod`. The ruleset on `prod` that `rule-github-repository` sets lets only the owner write that branch, and that page plans to add the CI that writes `prod` to the bypass list. The texts carry these pointers everywhere. A Grep `\(cases? [0-9]` over `.claude/` counted 66 in 13 files, and a Grep `case [0-9]` over `guppi/` counted 894 in 32 files. Some sit inside a sentence, such as a link from `rule-page-read` to a Lesson page that names session 0051. The person chose, in this order:
> - the copy holds the code, the harness, the pages marked by a new optional field `core` and the files rendered from them (the person proposed the field, so that a page can stay in `main` while it is tried live)
> - a command removes what it can safely remove and fails on the rest
> - a push to `main`, or a push of a tag `prod-*` on a commit of another branch, writes `prod` as one commit on top of the last (at pre-spec the person put the tag in place of a run the owner starts by hand)
> - a deploy key with write access goes on the bypass list, and the workflow pushes to `prod` with it (in Work Mode, the GitHub Actions app could not be put on the bypass list of this repository, which belongs to a personal account, so the person chose the key in place of the app)
> - a new rule page, `rule-clean-branch`, which applies only to this repository and does not ship
> - the schema of rules says that a page with `core: true` comes into a new project without its Estimates, which that project writes through its own Cases (at pre-spec)
> - `entity-guppi`, `entity-sprint`, `entity-glossary` and every rule page but `rule-github-repository` get `core` now; no Estimate does
> - a shipped page carries `origin: guppi`, `sprint: guppi` and a History of one line, and the schemas and lint accept that
> - a later Case of this sprint rewords the text the command refuses
> - the copy leaves out `guppi.toml`, so the install step of Case 802 starts in a new project
> - the put-off question on the future shape of GUPPI, decision 616 on `entity-guppi`, stays open
>
> The rule that governs the options is `rule-ratification`: every page that ships carries a signed `core`, set by a decision line of its own, and no script marks a page. The removal and the check are new code that judges text. `rule-one-judgment-one-implementation` sets that they share the judgments that exist. A Grep `\\\(cases?` over `guppi/` printed nothing, so no code judges a parenthesis of case references today. A Grep `WIKILINK\s*=|CODE_SPAN\s*=` over `guppi/` printed `guppi/glossary.py`, `guppi/lint.py` and `guppi/sprint.py`. The check of body links calls `links_of` of `guppi/lint.py`, the function that the `ref` check of lint calls. The pattern of `guppi/glossary.py` reads one table cell, and the one of `guppi/sprint.py` reads a milestone line, so neither judges a page body. A Grep `^(ID|CASE_ID)\s*=|import ID as CASE_ID` over `guppi/` printed `guppi/caseid.py`, `guppi/box.py` and `guppi/lint.py`, so the pattern of a case reference is built on `ID` of `guppi/caseid.py`. The value `guppi` and the test for `core` are new. Both live in `guppi/pages.py`, which lint and the new `guppi/ship.py` import. The session folder patterns of `guppi/generate.py` and `guppi/materialize.py` judge a folder name, not a sentence, so the pattern of a session mention in prose is new.
>
> The frame showed four Criteria that the change makes false. `estimate-entities-schema-checked`, `estimate-rules-schema-checked` and `estimate-estimates-schema-checked` list every optional field of their schema, and `estimate-lint-finds-a-broken-link` calls an `origin` of another form a finding. Sub-cases 804.1 to 804.4 replace them, by the person's answer. Their `purpose` and `method` do not state the old promise, so they stand. A Grep `check_origin|ORIGIN_CASE|ORIGIN_LINE` over `guppi/` and `tests/` printed `guppi/lint.py`, `guppi/caseid.py` and `tests/test_caseid.py`. The test there reads both forms of a ledger origin, and that still holds. A Grep `` `origin` `` over `vault/wiki/` without `log.md` and `brief.md` printed 27 files. Two other sentences state the form of the field. The row `origin` of `entity-glossary` speaks of a page a Case created, which a shipped page in a new project is not, so it stands. The sentence of `rule-vault-layout` that `ref` and `origin` name filenames speaks of references to pages, and `guppi` names no page, so it stands. A Grep `\bcore\b` over `vault/wiki/` without `log.md` and `brief.md`, and over `.claude/`, printed nothing, so the new field clashes with no term.
>
> A Grep `schema\.yaml|rule-github-repository|estimate-lint-finds-a-broken-link|estimate-sprint-plugin-ci|checks\.yml` over `tests/` printed `tests/test_lint.py`, `tests/test_prespec.py`, `tests/test_casecheck.py`, `tests/test_ratified.py`, `tests/test_generate.py`, `tests/test_schemas.py`, `tests/test_materialize.py`, `tests/test_orchestration.py` and `tests/test_case_schema.py`.
> - `tests/test_schemas.py` reads the live schema files. Its value test takes the first entry of `values`, which stays `kind`. `core` adds no conditional.
> - `tests/test_generate.py`, `tests/test_materialize.py`, `tests/test_orchestration.py` and `tests/test_case_schema.py` copy the live schema files into a temporary folder. An optional field more lets a `create` key `core` through, and none of them writes that key. The stray-key test of `tests/test_materialize.py` uses `contract_note`.
> - The other files write schemas of their own.
>
> A Grep `\bprod\b` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `.github/workflows/checks.yml`, `vault/wiki/entities/entity-guppi-repository.md`, `vault/wiki/rules/rule-github-repository.md` and `vault/wiki/estimates/estimate-sprint-plugin-pull-requests-reviewed-on-github.md`. The sentence of `rule-github-repository` that plans the bypass changes in 804.7. So do its sentences on who writes `prod` and who pushes, and its `purpose`. The Purpose of `entity-guppi-repository` names `rule-github-repository` as its only rule, and 804.6 changes it. The Criterion on pull requests from a second account, which cannot push to `prod`, stays true. `checks.yml` keeps skipping a push to `prod`.
>
> Before the `create` of `rule-clean-branch`, which has no `ref`, the vault query of `ask-guppi` ran. The Greps `^(purpose|deferred_by):` over the rules and the entities show no page on a clean version. The nearest page is `rule-github-repository`, which holds the settings of the repository. `entity-guppi` carries the put-off decision 616, which the person left open. A Glob `vault/**/*clean-branch*` printed only `vault/wiki/estimates/estimate-sprint-plugin-ci-writes-a-clean-branch.md`, so `rule-clean-branch` and `estimate-clean-branch-writes-a-clean-copy` are free. The tags `ci`, `git` and `plugin` stand in `tags.md`.
>
> In 804.5 the marking adds one field and no sentence, and it changes no Render. I did not read the rule pages whole. A Grep `\bcore\b` over them printed nothing. Cases of this session change the text of some of them:
> - Case 802 changes `rule-morph` and `rule-guppi-config`.
> - Case 803 changes `rule-case-build` and `rule-case-protocol`.
> - Cases 800 and 801 change `rule-ask` and `rule-case-build`, by the ledger.
>
> A field beside their text contradicts none of them. The marks of 804.5 are checked by `estimate-sprint-plugin-ci-writes-a-clean-branch`, whose Criterion in 804.7 gains the line that `prod` holds each page with `core: true` and no other page: the live run reads exactly the set the marks choose, so a missing or stray mark shows there, by the person's answer at pre-spec. The new text of `rule-morph` from Case 802 links `entity-sprint-plugin` in its body. That link does not ship, so the check of 804.6 will refuse it, and it goes to the rewording Case. The pages get `core` at the librarian's run, after Work Mode. So the Work Mode run of `guppi ship` lists only the leftovers of the code and the harness. The leftovers of the pages come from the first CI run, which the owner starts by a tag `prod-*` on a commit of `plugin` after pushing the librarian's commit, by the person's answer.
>
> At pre-spec the check of the plan asked for an update of the sprint page, since this Case works on an item of the sprint. 804.7 gives the item of the milestone The clean branch of `entity-sprint-plugin` two links, `rule-clean-branch` and `estimate-sprint-plugin-ci-writes-a-clean-branch`. By the person's answer, the item ticks only when the rule is `built` and the live run has passed, which comes after the rewording Case. Case 802, as its file stands, updates the same page in its `## Backlog`. The pair of 804.7 changes only the line of the item of The clean branch, so the two changes do not touch the same text. Its Estimate `estimate-sprint-plugin-ci-writes-a-clean-branch` gets a new trigger in 804.7. Its `purpose` still states the promise and stands. Its `method` is set anew to name the run by tag and the reading of the `on:` block. The last brief, under `## Readings at the close`, reports `make test` at 1587 passed and 6 skipped, and `make lint` at 2 lines: the defer count of `rule-morph`, and the failed reading of `estimate-case-build-reads-the-last-output-of-a-check`. No check of this Case rests on lint over the copy.

> **problem:**
> Nothing builds the version of GUPPI that other people install. Every text points to this repository's decisions and sessions, nothing marks which pages belong to GUPPI itself, and the schemas and lint have no shape for a page that shipped.

> **recommend:**
> - **What does the clean version hold?**
>   - Recommended: (a) code, harness and rule pages, with history fields and links to pages left out removed; no Entity, Estimate, Lesson, Insight or Decision page, and no session records.
>   - Answer: agreed, (a). The person asked whether the Entity page of the sprint as a kind should ship too, since it is part of how GUPPI works. A later question took that up.
> - **How do the pointers to past decisions leave the text?**
>   - Recommended: (a) a script removes them, and a check fails on the rest.
>   - Answer: agreed, (a).
> - **What starts a run, and from which branch?**
>   - Recommended: (a) a push to `main`, plus a run by hand on any branch.
>   - Answer: agreed, (a).
> - **How does `prod` keep its history?**
>   - Recommended: (a) one new commit per run, on top of the last one.
>   - Answer: agreed, (a).
> - **How does CI get the right to write `prod`?**
>   - Recommended: (a) the built-in GitHub Actions account on the bypass list.
>   - Answer: agreed, (a).
> - **Which page sets the rule of the clean branch?**
>   - Recommended: (a) a new rule page, `rule-clean-branch`.
>   - Answer: agreed, (a).
> - **Which Entity pages go into the clean version?**
>   - Recommended: (a) the three pages that describe GUPPI as a tool: `entity-guppi`, `entity-sprint` and `entity-glossary`.
>   - Answer: agreed, (a).
> - **Do the rules that apply only to this repository ship?**
>   - Recommended: (a) a rule that applies only to a page left out stays out.
>   - Answer: agreed, (a). The person proposed an explicit page field, `core`, that tells the build which pages ship, so that a page can stay in `main` while it is tried live. The next question took it up.
> - **Does each page carry an explicit flag that says it ships?**
>   - Recommended: (a) an opt-in `core` field on Entity, Rule and Estimate pages.
>   - Answer: agreed, (a).
> - **What do shipped pages carry in place of their history fields?**
>   - Recommended: (a) the copy writes neutral values, and the schema accepts them.
>   - Answer: agreed, (a).
> - **Do any Estimate pages ship?**
>   - Recommended: (a) none now.
>   - Answer: agreed, (a).
> - **Which pages get `core` now, and how?**
>   - Recommended: (a) all of them in this Case, in a sub-case of their own.
>   - Answer: agreed, (a).
> - **What happens to text the script cannot clean on the first run?**
>   - Recommended: (a) a later Case of this sprint rewords them.
>   - Answer: agreed, (a).
> - **How does the Case split, and how is each part checked?**
>   - Recommended: (a) four sub-cases, each with its own check.
>   - Answer: agreed, (a).
> - **Does this Case settle the put-off question on GUPPI's future shape?**
>   - Recommended: (a) it stands open.
>   - Answer: agreed, (a).
> - **What else does the check refuse in the copy?**
>   - Recommended: (a) both a link in the text to a page left out and a mention of a session fail the run.
>   - Answer: agreed, (a).
> - **How does the part on the schemas and lint split?**
>   - Recommended: (a) four sub-cases, each replacing one existing Criterion, and no new Estimate.
>   - Answer: agreed, (a).
> - **Does the copy carry this project's `guppi.toml`?**
>   - Recommended: (a) the copy leaves out `guppi.toml`.
>   - Answer: agreed, (a).
> - **Where does the list of leftovers for the pages come from?**
>   - Recommended: (a) code and harness from Work Mode, pages from the first run on GitHub.
>   - Answer: agreed, (a).
> - **Do the Estimates of the shipped rules ship after all?**
>   - Recommended: (a) no Estimate ships, and the schema of rules says why.
>   - Answer: agreed, (a): let us try it that way.
> - **When does the milestone The clean branch count as done?**
>   - Recommended: (a) the item links the rule and the sprint's check of the live run.
>   - Answer: agreed, (a).
> - **How does the workflow get the right to write `prod`?**
>   - Recommended: (a) a deploy key on the bypass list.
>   - Answer: agreed, (a); the person asked what to do, and the steps stand as `stop:` tasks of 804.7.
> - **Change**
>   - Asked: at pre-spec, the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` names that `prod` holds exactly the pages with `core: true`, so that the marks of 804.5 are checked.
>   - Taken: 804.7 adds that line to the Criterion, and the `context` names it.
> - **Change**
>   - Asked: at pre-spec, a push of a tag `prod-*` on a commit of `plugin` starts the run in place of a run by hand; a push to `main` still starts it, and that line is checked by reading the `on:` block of the workflow.
>   - Taken: the `when` and `then` of 804.7, the `method` of its Estimate, the workflow task and the Purpose of `rule-clean-branch` say so.

### Case 804.1 — The Entity schema carries the field core and the shipped values

> **given:**
> `rule-entities-schema`: renders the schema of Entity pages.
> **＋** `vault/wiki/entities/schema.yaml`: the file rendered from it.
> **＋** `estimate-entities-schema-checked`: its Criterion is replaced whole.
> **＋** `tests/test_schemas.py`: the tests of the live schema files.

> **when:**
> `guppi render` writes `vault/wiki/entities/schema.yaml` from `rule-entities-schema`, and `guppi lint` reads a page of `vault/wiki/entities/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `parent, children, code_ref, deferred_by, rules, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `core: true`; conditional — `Leaf` requires `parent`, `MOC` requires `children`; the sections `## Purpose` and `## History` required, `## How it works`, `## Milestones`, `## Backlog`, `## Closed`, `## Terms` optional.
> **＋** The file also holds `computed: [rules]`, which lint does not read.
> **＋** An Entity page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; an Entity with `rules` on live Rules has none; the glossary page with `## Terms` has none.
> **＋** An Entity page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `rules`, `core` and `## Terms` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, the Slug, `built`, `How it works` and Constraints notes, the sentence on the edge Rule → Entity and the one on the glossary page; `examples` holds the example pages.

```then
update:
- slug: rule-entities-schema
  replace:
  - old: 'optional: [parent, children, code_ref, deferred_by, rules]'
    new: 'optional: [parent, children, code_ref, deferred_by, rules, core]'
  - old: 'status: [draft, built, archived]'
    new: |-
      status: [draft, built, archived]
          core: [true]
  - old: (case 103.6). The ratified decision that created it.
    new: '(case 103.6). The ratified decision that created it. On a page with `core: true` in the clean version that `guppi ship` writes, it is `guppi`, and lint accepts it there (case 804).'
  - old: required; the sprint id.
    new: |-
      required; the sprint id; `guppi` on a page with `core: true` in the clean version that `guppi ship` writes (case 804).
        core: |
          optional; `true`. The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. Set by a Case, never by hand (case 804).
  change: the field core, and the value guppi of origin and sprint on a page of the clean version (case 804)
- slug: estimate-entities-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — the field core and the shipped values (case 804)
```

```tasks
- [ ] update `rule-entities-schema`
- [ ] update `estimate-entities-schema-checked`
- [ ] `uv run guppi render`: `vault/wiki/entities/schema.yaml`
- [x] `tests/test_schemas.py`: the case `entities` of a test that a page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
- [ ] read `estimate-entities-schema-checked`
```

### Case 804.2 — The Rule schema carries the field core and the shipped values

> **given:**
> `rule-rules-schema`: renders the schema of Rule pages.
> **＋** `vault/wiki/rules/schema.yaml`: the file rendered from it.
> **＋** `estimate-rules-schema-checked`: its Criterion is replaced whole.
> **＋** `tests/test_schemas.py`: the tests of the live schema files.

> **when:**
> `guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`, `core: true`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
> **＋** The file also holds `ordered_children: true`, which lint does not read.
> **＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
> **＋** A Rule page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity, the one on the guard of the agent's own conduct and the one that a page with `core: true` comes into a new project without its Estimates, which that project writes through its own Cases; `examples` holds the example pages.

```then
update:
- slug: rule-rules-schema
  replace:
  - old: Every Rule requires an Estimate.
    new: 'Every Rule requires an Estimate; a page with `core: true` comes into a new project without its Estimates, and that project writes its own through its Cases (case 804).'
  - old: 'optional: [enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to]'
    new: 'optional: [enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core]'
  - old: 'render_mode: [full, partial]'
    new: |-
      render_mode: [full, partial]
          core: [true]
  - old: on pages born before 2026-09-13 (case 103.6).
    new: 'on pages born before 2026-09-13 (case 103.6). On a page with `core: true` in the clean version that `guppi ship` writes, it is `guppi`, and lint accepts it there (case 804).'
  - old: required; the sprint id.
    new: |-
      required; the sprint id; `guppi` on a page with `core: true` in the clean version that `guppi ship` writes (case 804).
        core: |
          optional; `true`. The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. Set by a Case, never by hand (case 804).
  change: the field core, and the value guppi of origin and sprint on a page of the clean version (case 804)
- slug: estimate-rules-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — the field core and the shipped values (case 804)
```

```tasks
- [ ] update `rule-rules-schema`
- [ ] update `estimate-rules-schema-checked`
- [ ] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
- [x] `tests/test_schemas.py`: the case `rules` of a test that a page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
- [ ] read `estimate-rules-schema-checked`
```

### Case 804.3 — The Estimate schema carries the field core and the shipped values

> **given:**
> `rule-estimates-schema`: renders the schema of Estimate pages.
> **＋** `vault/wiki/estimates/schema.yaml`: the file rendered from it.
> **＋** `estimate-estimates-schema-checked`: its Criterion is replaced whole.
> **＋** `tests/test_schemas.py`: the tests of the live schema files.

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked, deferred_by, core`; values `kind: QA | Research`, `status: pending | passed | failed`, `core: true`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
> **＋** An Estimate page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
> **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

```then
update:
- slug: rule-estimates-schema
  replace:
  - old: 'optional: [purpose, checked, deferred_by]'
    new: 'optional: [purpose, checked, deferred_by, core]'
  - old: 'status: [pending, passed, failed]'
    new: |-
      status: [pending, passed, failed]
          core: [true]
  - old: (case 103.6). The ratified decision that created it.
    new: '(case 103.6). The ratified decision that created it. On a page with `core: true` in the clean version that `guppi ship` writes, it is `guppi`, and lint accepts it there (case 804).'
  - old: required; the sprint id.
    new: |-
      required; the sprint id; `guppi` on a page with `core: true` in the clean version that `guppi ship` writes (case 804).
        core: |
          optional; `true`. The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. Set by a Case, never by hand (case 804).
  change: the field core, and the value guppi of origin and sprint on a page of the clean version (case 804)
- slug: estimate-estimates-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — the field core and the shipped values (case 804)
```

```tasks
- [ ] update `rule-estimates-schema`
- [ ] update `estimate-estimates-schema-checked`
- [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] `tests/test_schemas.py`: the case `estimates` of a test that a page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
- [ ] read `estimate-estimates-schema-checked`
```

### Case 804.4 — Lint accepts the origin guppi on a page marked core

> **given:**
> `guppi/lint.py`: `check_origin` judges the `origin` of a page.
> **＋** `guppi/pages.py`: holds the value `guppi` and the test of `core: true`, which lint and `guppi/ship.py` import.
> **＋** `tests/test_lint.py`: the tests of lint.
> **＋** `estimate-lint-finds-a-broken-link`: its Criterion is replaced whole.
> **＋** `rule-lint`: the rule of lint, whose `implementation_ref` names `guppi/lint.py`.
> **＋** `vault/wiki/`: the live pages lint reads.
> **＋** `vault/raw/` and `vault/archive/`: where the ledger of an `origin` stands.
> **＋** `raw/<date>[/<HHMM>]/ledger.md#case-N`: the form of an `origin` that names a ledger.
> **＋** `guppi/materialize.py`: `category_of`, which gives the category of a slug by its prefix, `decision-` included.

> **when:**
> `uv run guppi lint` follows the links of the live pages under `vault/wiki/`.

> **then:**
> `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
> **＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
> **＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate.
> **＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
> **＋** An `origin` `#case-N` of a Case that has no ledger line of its own is found by a line of one of its sub-cases, `[case N.M]`.
> **＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer` and no `children`, or with `kind` or `target_slug`; a slug of its lists that `category_of` of `guppi/materialize.py` gives a category — the prefix `decision-` included — and that no live or archived page carries.
> **＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.
> **－** A `### case N` line under an Estimate's `## Criterion` is not read as a link.
> **－** An `origin` `guppi` on a page with `core: true` is no finding; on a page without `core: true` it is an `origin` of another form.

```then
update:
- slug: estimate-lint-finds-a-broken-link
  set:
    status: pending
  change: 'the Criterion replaced whole — the origin guppi on a page with core: true is no finding (case 804)'
```

```tasks
- [x] `guppi/pages.py`: `SHIPPED = "guppi"`, the value of `origin` and `sprint` on a page of the clean version, and `is_core(page)`, true when the page carries `core: true` — the one judgment of both, which `guppi/lint.py` and `guppi/ship.py` import.
- [x] `guppi/lint.py`: `check_origin` returns no finding for an `origin` equal to `SHIPPED` on a page that `is_core` accepts; the docstring names it.
- [x] `tests/test_lint.py`: a page with `core: true` and `origin: guppi` has no `origin` finding, and a page with `origin: guppi` and no `core` has one.
- [ ] update `estimate-lint-finds-a-broken-link`
- [ ] read `estimate-lint-finds-a-broken-link`
```

### Case 804.5 — The pages that ship carry core

> **given:**
> `vault/wiki/rules/`: each rule page but `rule-github-repository` gains `core: true`.
> **＋** The rule pages that gain `core: true`: `rule-agent-writing`, `rule-ask`, `rule-atomicity`, `rule-backlog`, `rule-bash-guard`, `rule-brief`, `rule-carry-over`, `rule-case-build`, `rule-case-check`, `rule-case-example`, `rule-case-protocol`, `rule-claude-md`, `rule-cleanup`, `rule-close`, `rule-compact-recall`, `rule-context-size`, `rule-decisions-schema`, `rule-default-mode`, `rule-documentation`, `rule-end-of-work`, `rule-entities-schema`, `rule-estimates-schema`, `rule-event-log`, `rule-git-context`, `rule-glossary`, `rule-governed-files-hook`, `rule-guppi-config`, `rule-handoff`, `rule-harness`, `rule-hook-registry`, `rule-index-check`, `rule-insights-schema`, `rule-internal-context`, `rule-language`, `rule-ledger-tail`, `rule-ledger-write`, `rule-lessons-schema`, `rule-lint`, `rule-materialize`, `rule-morph`, `rule-one-judgment-one-implementation`, `rule-orchestration`, `rule-page-generation`, `rule-page-read`, `rule-page-schemas`, `rule-permissions`, `rule-plan-mode`, `rule-powershell-guard`, `rule-prespec`, `rule-prespec-hook`, `rule-prespec-onward`, `rule-python-utf8`, `rule-ratification`, `rule-raw-archive`, `rule-render-harness`, `rule-retro`, `rule-retro-commit`, `rule-retro-onward`, `rule-rules-schema`, `rule-search-leaves-out-decisions`, `rule-session`, `rule-session-start`, `rule-settings`, `rule-shell-write-check`, `rule-skill-grill-me`, `rule-skill-hi`, `rule-skill-merge-main`, `rule-skill-pr-review`, `rule-skill-sprint-close`, `rule-skill-sprint-open`, `rule-skill-wait-what`, `rule-spec-box`, `rule-spec-capture`, `rule-spec-reconcile`, `rule-spec-write`, `rule-sprint`, `rule-sprint-close`, `rule-synthesis`, `rule-tests-clock-pinned`, `rule-vault-layout`, `rule-where-to-stop` and `rule-work-mode`.
> **＋** `entity-guppi`, `entity-sprint` and `entity-glossary`: each gains `core: true`.
> **＋** `rule-github-repository`, `rule-clean-branch`, `entity-guppi-repository` and `entity-sprint-plugin`: the pages of this repository alone, with no `core`.
> **＋** `rule-clean-branch`: the rule of `guppi ship`, which chooses the pages by `core`.
> **＋** `vault/raw/2026-10-13/1753/cases/case-802.md`: Case 802 changes the text of `rule-morph` and `rule-guppi-config`.
> **＋** `vault/raw/2026-10-13/1753/cases/case-803.md`: Case 803 changes the text of `rule-case-build` and `rule-case-protocol`.

> **when:**
> `uv run guppi ship`, as `rule-clean-branch` sets it, reads the pages under `vault/wiki/` to choose the pages of the clean version.

> **then:**
> Each rule page under `vault/wiki/rules/` but `rule-github-repository` and `rule-clean-branch`, and `entity-guppi`, `entity-sprint` and `entity-glossary`, carries `core: true`, and the clean version holds it.
> **－** `rule-github-repository`, `rule-clean-branch`, `entity-guppi-repository`, `entity-sprint-plugin` and every Estimate carry no `core`, and the clean version does not hold them.

```then
update:
- slug: rule-agent-writing
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-ask
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-atomicity
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-backlog
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-bash-guard
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-brief
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-carry-over
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-case-build
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-case-check
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-case-example
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-case-protocol
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-claude-md
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-cleanup
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-close
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-compact-recall
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-context-size
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-decisions-schema
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-default-mode
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-documentation
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-end-of-work
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-entities-schema
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-estimates-schema
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-event-log
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-git-context
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-glossary
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-governed-files-hook
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-guppi-config
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-handoff
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-harness
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-hook-registry
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-index-check
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-insights-schema
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-internal-context
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-language
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-ledger-tail
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-ledger-write
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-lessons-schema
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-lint
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-materialize
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-morph
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-one-judgment-one-implementation
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-orchestration
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-page-generation
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-page-read
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-page-schemas
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-permissions
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-plan-mode
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-powershell-guard
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-prespec
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-prespec-hook
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-prespec-onward
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-python-utf8
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-ratification
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-raw-archive
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-render-harness
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-retro
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-retro-commit
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-retro-onward
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-rules-schema
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-search-leaves-out-decisions
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-session
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-session-start
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-settings
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-shell-write-check
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-skill-grill-me
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-skill-hi
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-skill-merge-main
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-skill-pr-review
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-skill-sprint-close
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-skill-sprint-open
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-skill-wait-what
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-spec-box
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-spec-capture
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-spec-reconcile
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-spec-write
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-sprint
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-sprint-close
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-synthesis
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-tests-clock-pinned
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-vault-layout
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-where-to-stop
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: rule-work-mode
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: entity-guppi
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: entity-sprint
  set:
    core: true
  change: ships in the clean version (case 804)
- slug: entity-glossary
  set:
    core: true
  change: ships in the clean version (case 804)
```

```tasks
- [ ] update `rule-agent-writing`
- [ ] update `rule-ask`
- [ ] update `rule-atomicity`
- [ ] update `rule-backlog`
- [ ] update `rule-bash-guard`
- [ ] update `rule-brief`
- [ ] update `rule-carry-over`
- [ ] update `rule-case-build`
- [ ] update `rule-case-check`
- [ ] update `rule-case-example`
- [ ] update `rule-case-protocol`
- [ ] update `rule-claude-md`
- [ ] update `rule-cleanup`
- [ ] update `rule-close`
- [ ] update `rule-compact-recall`
- [ ] update `rule-context-size`
- [ ] update `rule-decisions-schema`
- [ ] update `rule-default-mode`
- [ ] update `rule-documentation`
- [ ] update `rule-end-of-work`
- [ ] update `rule-entities-schema`
- [ ] update `rule-estimates-schema`
- [ ] update `rule-event-log`
- [ ] update `rule-git-context`
- [ ] update `rule-glossary`
- [ ] update `rule-governed-files-hook`
- [ ] update `rule-guppi-config`
- [ ] update `rule-handoff`
- [ ] update `rule-harness`
- [ ] update `rule-hook-registry`
- [ ] update `rule-index-check`
- [ ] update `rule-insights-schema`
- [ ] update `rule-internal-context`
- [ ] update `rule-language`
- [ ] update `rule-ledger-tail`
- [ ] update `rule-ledger-write`
- [ ] update `rule-lessons-schema`
- [ ] update `rule-lint`
- [ ] update `rule-materialize`
- [ ] update `rule-morph`
- [ ] update `rule-one-judgment-one-implementation`
- [ ] update `rule-orchestration`
- [ ] update `rule-page-generation`
- [ ] update `rule-page-read`
- [ ] update `rule-page-schemas`
- [ ] update `rule-permissions`
- [ ] update `rule-plan-mode`
- [ ] update `rule-powershell-guard`
- [ ] update `rule-prespec`
- [ ] update `rule-prespec-hook`
- [ ] update `rule-prespec-onward`
- [ ] update `rule-python-utf8`
- [ ] update `rule-ratification`
- [ ] update `rule-raw-archive`
- [ ] update `rule-render-harness`
- [ ] update `rule-retro`
- [ ] update `rule-retro-commit`
- [ ] update `rule-retro-onward`
- [ ] update `rule-rules-schema`
- [ ] update `rule-search-leaves-out-decisions`
- [ ] update `rule-session`
- [ ] update `rule-session-start`
- [ ] update `rule-settings`
- [ ] update `rule-shell-write-check`
- [ ] update `rule-skill-grill-me`
- [ ] update `rule-skill-hi`
- [ ] update `rule-skill-merge-main`
- [ ] update `rule-skill-pr-review`
- [ ] update `rule-skill-sprint-close`
- [ ] update `rule-skill-sprint-open`
- [ ] update `rule-skill-wait-what`
- [ ] update `rule-spec-box`
- [ ] update `rule-spec-capture`
- [ ] update `rule-spec-reconcile`
- [ ] update `rule-spec-write`
- [ ] update `rule-sprint`
- [ ] update `rule-sprint-close`
- [ ] update `rule-synthesis`
- [ ] update `rule-tests-clock-pinned`
- [ ] update `rule-vault-layout`
- [ ] update `rule-where-to-stop`
- [ ] update `rule-work-mode`
- [ ] update `entity-guppi`
- [ ] update `entity-sprint`
- [ ] update `entity-glossary`
```

### Case 804.6 — guppi ship builds and checks the clean version

> **given:**
> `rule-clean-branch`: the new rule of the clean version, applied to `entity-guppi-repository`.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: the new check of the command.
> **＋** `guppi/ship.py`: the new command that builds and checks the clean version.
> **＋** `guppi/cli.py`: registers the command `ship`.
> **＋** `tests/test_ship.py`: the tests of the command over a sample tree.
> **＋** `guppi/lint.py`, `guppi/caseid.py` and `guppi/pages.py`: the judgments the command imports — `links_of`, `ID`, `HISTORY`, `MARKER`, `SHIPPED` and `is_core`.
> **＋** `entity-guppi-repository`: its Purpose names its rules.
> **＋** `rule-one-judgment-one-implementation`: one judgment, one implementation.
> **＋** `.claude/`, `vault/wiki/` and `vault/wiki/tags.md`: the harness, the pages and the tag registry the command copies.
> **＋** `vault/raw/`, `vault/archive/` and `.github/`: the session records and the workflows the command leaves out.

> **when:**
> `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

> **then:**
> It writes `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
> **＋** In each file it writes, it removes a parenthesis that holds only references to cases, the references to cases inside a longer parenthesis, and each `[[decision-case-N]]` link.
> **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
> **＋** It exits 1, and prints the file and the line, for each reference to a case, each link in a text to a page or a file it does not write, and each mention of a session of this repository by its id that remains.
> **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
> **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
> **－** It writes no file that a page without `core: true` renders in full.
> **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.

```then
create:
- slug: rule-clean-branch
  kind: Leaf
  purpose: Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install
  enforcement: check
  implementation_ref:
  - guppi/ship.py
  - tests/test_ship.py
  - .github/workflows/prod.yml
  applies_to:
  - '[[entity-guppi-repository]]'
  tags:
  - ci
  - git
  - plugin
  sections:
    Purpose: |-
      Prevents a reference to a case, a mention of a session of this repository or a page that stays in this repository from reaching the clean version of GUPPI that other people install. `guppi ship` builds that version from the working tree into an empty folder: `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page with `core: true` and each file rendered from such a page, but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project. It removes a parenthesis that holds only references to cases, the references to cases inside a longer parenthesis, and each `[[decision-case-N]]` link. It gives each page `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line, and keeps in its link fields only the pages it writes. It exits 1 on each reference to a case, link to a page or a file it does not write, mention of a session of this repository, or section of a page without `core: true` that remains; a Case rewords that text at its source.

      The workflow `.github/workflows/prod.yml` runs it on each push to `main`, and on each push of a tag `prod-*`, such as `prod-1`, on a commit of another branch. It writes the result to the branch `prod` as one new commit on top of the last, whose message names the commit it was built from, and writes none when nothing changed or when the command exits 1. It pushes with a deploy key of this repository with write access, whose private half is the repository secret `PROD_DEPLOY_KEY`; deploy keys stand on the bypass list of the ruleset on `prod` that [[rule-github-repository]] sets. This rule and the workflow belong to this repository: neither carries `core`, and `.github/` is not part of the clean version (case 804).
- slug: estimate-clean-branch-writes-a-clean-copy
  ref: rule-clean-branch
  kind: QA
  purpose: 'Whether guppi ship writes only the code, the harness and the pages with core: true, removes the references to cases, writes the shipped values, and exits 1 on what it cannot clean'
  method: uv run pytest tests/test_ship.py
  tags:
  - ci
  - plugin
update:
- slug: entity-guppi-repository
  replace:
  - old: 'Its rules are those of `rule-github-repository`, which names this page in `applies_to`: the rulesets on `main` and `prod`, the workflow of checks, and the approval of the runs of an outside contributor.'
    new: Its rules are `rule-github-repository` — the rulesets on `main` and `prod`, the workflow of checks and the approval of the runs of an outside contributor — and `rule-clean-branch`, the workflow that writes the clean version of GUPPI to `prod`; each names this page in `applies_to` (case 804).
  change: its rules name rule-clean-branch beside rule-github-repository (case 804)
```

```tasks
- [ ] create `rule-clean-branch`
- [ ] create `estimate-clean-branch-writes-a-clean-copy`
- [ ] update `entity-guppi-repository`
- [x] `guppi/ship.py`: the command `guppi ship <folder>` as the `then` of this Case sets it. It reads pages by `read_vault`, `HISTORY` and `is_core` of `guppi/pages.py`, body links by `links_of` of `guppi/lint.py`, markers by `MARKER` of `guppi/pages.py`, and a case id by `ID` of `guppi/caseid.py`, and writes `SHIPPED` of `guppi/pages.py`; its own patterns are the parenthesis of case references and the mention of a session in prose, which no module of `guppi/` judges today.
- [x] `guppi/cli.py`: registers `ship`.
- [x] `tests/test_ship.py`: over a sample tree under a temporary folder, one test per line of the `then` of this Case, and one test that runs `guppi/lint.py` over a page that `guppi ship` wrote and asserts no `origin` finding.
- [x] `uv run guppi ship` over the working tree into a temporary folder: the files and lines it refuses go into the handoff, with the note that the leftovers of the pages come from the first CI run, which the owner starts by a tag `prod-*` on a commit of `plugin` after the push of the librarian's commit.
- [ ] read `estimate-clean-branch-writes-a-clean-copy`
```

### Case 804.7 — CI writes the clean version to prod

> **given:**
> `.github/workflows/prod.yml`: the new workflow that writes `prod`.
> **＋** `estimate-sprint-plugin-ci-writes-a-clean-branch`: its Criterion is replaced whole.
> **＋** `rule-clean-branch`: the rule of the clean version.
> **＋** `rule-github-repository`: the rulesets on `main` and `prod`, and who writes them.
> **＋** `.github/workflows/checks.yml`: the checks, which skip a push to `prod`.
> **＋** `entity-sprint-plugin`: the sprint page; the item of its milestone The clean branch links the rule and the Estimate.
> **＋** `vault/raw/2026-10-13/1753/cases/case-802.md`: Case 802 updates the same sprint page elsewhere.
> **＋** `PROD_DEPLOY_KEY`: the repository secret that holds the private half of the deploy key that writes `prod`.

> **when:**
> In a session of the sprint `plugin` before its close, the owner pushes a tag `prod-*`, such as `prod-1`, on a commit of the branch `plugin` to the repository of the project on GitHub, and the workflow `.github/workflows/prod.yml` runs on that commit.

> **then:**
> The run writes the clean version that `uv run guppi ship` builds to the branch `prod`, as one new commit on top of its last commit, or as its first commit when `prod` does not stand yet, whose message names the commit it was built from.
> **＋** The run pushes to `prod` with the deploy key whose private half is the secret `PROD_DEPLOY_KEY`, which the bypass list of the ruleset on `prod` lets through.
> **＋** `prod` holds each page with `core: true` and no other page.
> **＋** No text of the clean version holds a reference to a case or a decision, a link to a page that the clean version leaves out, or a mention of a session of this repository.
> **＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
> **＋** The `on:` block of `.github/workflows/prod.yml` starts the same run on a push to `main`.
> **－** A run whose `uv run guppi ship` exits 1 fails and writes nothing to `prod`.
> **－** A run whose clean version equals the last commit of `prod` adds no commit.

```then
update:
- slug: rule-github-repository
  set:
    purpose: Prevents a pull request from reaching main unchecked, and an account other than the owner's from writing to main, or to prod, which only the owner and the workflow of rule-clean-branch write
  replace:
  - old: Prevents a pull request from reaching `main` unchecked, and an account other than the owner's from writing to `main` or `prod`.
    new: Prevents a pull request from reaching `main` unchecked, and an account other than the owner's from writing to `main`, or to `prod`, which only the owner and the workflow of [[rule-clean-branch]] write.
  - old: Only the owner bypasses it, so a pull request into `prod` cannot be merged. The item The clean branch of [[entity-sprint-plugin]] adds the CI that writes `prod` to that bypass list.
    new: Only the owner and the deploy keys of the repository bypass it, so a pull request into `prod` cannot be merged, and besides the owner only the workflow `.github/workflows/prod.yml` of [[rule-clean-branch]] writes `prod`, with the one deploy key whose private half is the secret `PROD_DEPLOY_KEY` (case 804).
  - old: Only the owner pushes, by hand when the owner wants, by `! git push`.
    new: Only the owner pushes, by hand when the owner wants, by `! git push`; the one other push is that of the workflow of [[rule-clean-branch]] to `prod` (case 804).
  change: deploy keys on the bypass list of prod, and the workflow of rule-clean-branch writes prod with the key of the secret PROD_DEPLOY_KEY (case 804)
- slug: entity-sprint-plugin
  replace:
  - old: '- CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint'
    new: '- [[rule-clean-branch]], [[estimate-sprint-plugin-ci-writes-a-clean-branch]] — CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint'
  change: the item of The clean branch links rule-clean-branch and the Estimate of the live run (case 804)
- slug: estimate-sprint-plugin-ci-writes-a-clean-branch
  set:
    status: pending
    method: 'by hand, in a session of the sprint plugin before its close: the CI run that a tag prod-* on a commit of plugin starts, its push with the deploy key of the secret PROD_DEPLOY_KEY, the branch prod it wrote and the on: block of .github/workflows/prod.yml read against the Criterion'
  change: 'the Criterion replaced whole — the run on a tag prod-* of plugin, the commit on top of prod, prod holds exactly the pages with core: true, the push with the deploy key of PROD_DEPLOY_KEY (case 804)'
```

```tasks
- [x] `.github/workflows/prod.yml`: runs on a push to `main` and on a push of a tag `prod-*`, with `contents: write`; runs `uv run guppi ship` into an empty folder; when it exits 0, commits that folder to `prod` on top of its last commit with a message that names the commit it was built from, adds no commit when nothing changed, and pushes over SSH with the private key of the secret `PROD_DEPLOY_KEY`, never with the token of the run; when it exits 1, fails and pushes nothing; its header comment names the deploy key in place of the GitHub Actions app.
- [ ] update `rule-github-repository`
- [ ] update `entity-sprint-plugin`
- [ ] `uv run guppi sprint`
- [x] stop: the owner makes an SSH key pair on the owner's machine, such as by `ssh-keygen -t ed25519 -N "" -C prod-deploy -f prod_deploy_key`, outside the repository.
- [x] stop: the owner adds the public half, `prod_deploy_key.pub`, as a deploy key of the repository on GitHub, with write access, under Settings, Deploy keys.
- [x] stop: the owner stores the private half, `prod_deploy_key`, as the repository secret `PROD_DEPLOY_KEY` under Settings, Secrets and variables, Actions, and then deletes both files from the machine.
- [x] stop: the owner adds `Deploy keys` to the bypass list of the ruleset `prod`, with the mode always, in the settings of the repository on GitHub.
- [ ] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
- [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`
```
