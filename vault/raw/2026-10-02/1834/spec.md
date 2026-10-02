<!-- approved 20:26:31 · session 9acd6cf3 -->

# Spec — session 1834, 2026-10-02

## Case 595 — The main agent's rules leave case-schema.md, and the pre-spec loop waits for the answers

> **context:**
> Today `/hi` loads `vault/wiki/case-schema.md` whole into the main agent's context. That file is the Render of `rule-case-protocol`. It mixes three things: the form of a Case, which only `case-guppi` uses; what the main agent alone does (the Frontier, the dispatch, the showing, the reply after a sign-off, the defers); and what both agents need (the one rule, the form of the ledger lines, atomicity, the harness). The main agent therefore carries a long form for Cases it never builds. Case 561.13 approved a three-file design for this and left it for a later session. Case 574 put it off again.
>
> The person opened the item with a related problem at `/pre-spec`. The loop of `rule-prespec`, from cases 561.2 and 581.1, sends each fix that needs no word from the person to its `case-guppi` in the same turn as the report. The report's own questions stay open while those agents work. The person reads a question while answers and new rounds of questions come back, loses track of what belongs where, and an answer can change a fix that has already gone out. Holding back a round that comes back while other answers are still out is already step 2 of the skill. Its check, `estimate-prespec-gathers-the-answers-after-findings`, passed at the `/pre-spec` of session 1202.
>
> State of the pages. `rule-orchestration` is a placeholder (`status: draft`, no `kind`) with `deferred_by` naming cases 424 and 574. A `create` fills a placeholder and keeps `deferred_by`, and the `{supersedes:case 424}{supersedes:case 574}` blocks on its line retire both defers. `rule-case-protocol` lists eleven Estimates. Eight of them check behaviours that move to `rule-orchestration`, and `estimate-case-protocol-ledger-line-form` checks a form that moves to `rule-ratification`. `rule-atomicity` renders into `case-schema.md` through a marker line of its parent. The Render of `rule-case-protocol` writes the languages as the placeholders `{{documentation_lang}}` and `{{chat_lang}}`, as `rule-guppi-config` and `rule-language` require. The new Renders keep them in the same places, so `estimate-guppi-config-fills-the-languages` stands: its Criterion speaks of every Render that holds a placeholder.
>
> The vault's answer, by the recipe of `ask-guppi.md` (Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`):
> - exists: none for a shared file of the one rule and the ledger.
> - near: `rule-case-protocol` holds that text today; `rule-ledger-write` is the hook that writes the lines; `rule-atomicity` is rendered into the same file.
> - rules: `rule-vault-layout`, through `check_layout` of `guppi/lint.py`, needs a live rule page to name each `.md` at the root of `vault/wiki/`. The `governs` field of the new rules names their files.
> - slugs: a Glob over `vault/wiki/` and `vault/archive/` found no `rule-ratification`, `orchestration.md`, `ratification.md`, `estimate-orchestration-*` or `estimate-ratification-*`.
>
> The purpose of `rule-case-protocol` is reworded so that each rule prevents its own thing. `rule-ratification` prevents acting without the one rule. `rule-case-protocol` prevents a Case from being built in a form that cannot be read, or shown without its content.
>
> Mechanics. `guppi generate` (its docstring) moves an Estimate by `rename`: the page keeps its History and Result, and every live page that names the old slug — a link, a ref field or the bare slug in a body, Decision pages included — is rewritten. A Grep of the old slugs (`estimate-case-protocol-(loaded|acknowledging-reply|ledger-line-form|shows-the-built-case|defers-in-one-reply|shows-the-frontier-after-a-closed-line|forwards-a-discussion-question|asks-in-the-grill-me-shape|puts-the-harness-before-plan-mode|names-related-cases-in-the-dispatch)`) over the repository outside `vault/raw/` and `vault/archive/` printed 199 files. Besides Decision pages, `brief.md`, `log.md`, the rule page and the Estimates themselves, it printed `estimate-case-protocol-case-form`, `estimate-spec-write-writes-a-defer`, `estimate-plan-mode-names-its-estimates`, `insight-case-build-promise-lines-compared-by-no-check` and `insight-workflow-contract-change-leaves-its-derived-text-stale`. The last four were not read, since the rename rewrites the name there. No step of `generate` moves an Estimate or a child to another rule, so this Case writes `target`, `parent`, `children` and `estimates` by hand under `set` or as fields of a `create`. The `estimates` of the two new rules name the Estimates by their current slugs: those pages exist when the `create` applies, and the rename of each one later in the same run rewrites the name in that list.
>
> Searches of the frame:
> - Grep `case-schema` over `vault/wiki/`, Decision pages included, printed 459 lines in 274 files, most of them Decision pages and `log.md`, which are records. The live hits the move makes false are fixed in the sub-cases: `rule-internal-context`, `rule-claude-md`, `rule-compact-recall`, `rule-atomicity`, `rule-case-build`, `rule-prespec`, `rule-ledger-write`, `entity-glossary`, and the Estimates replaced below.
> - Hits that stand:
>   - `rule-harness`, `rule-vault-layout` and the glossary row Harness name `case-schema.md` in a "such as" list that stays true.
>   - `rule-rules-schema` and `rules/schema.yaml` call it a file the agent reads in a working session, and `case-guppi` still reads it. Its other hit there is a sample page.
>   - `rule-language` points to the STE sentence, which stays in the `## Language` of `case-schema.md`.
>   - `rule-page-read` lists it among files with no History, which stays true.
>   - `estimate-glossary-ticks-the-spec` and `estimate-where-to-stop-stops-only-on-its-conditions` name task-line forms that stay in `case-schema.md`.
>   - `estimate-language-followed`, `estimate-case-build-records-the-rounds-in-recommend` and `estimate-case-protocol-case-form` name the form, which stays.
>   - `estimate-hi-no-read-calls` and `estimate-governed-files-hook-refuses` name it in their Result only.
>   - Lessons, Insights and `entity-sprint-migration` are records.
>   - `docs/migration/migration-plan.md` is a one-time plan to be discarded.
> - Grep `rule-case-protocol` over `vault/wiki/` outside the Decision pages printed 44 files. Of the live hits read:
>   - The schema pages, the three `schema.yaml` files, `rule-backlog` and `guppi/materialize.py` name the condition under which `generate` clears a defer. That condition stays in `case-schema.md`, so they stand.
>   - The glossary rows whose meaning moves, the row Case included, are 595.20.
>   - `estimate-skill-grill-me-asks-in-rounds` is 595.19.
>   - `estimate-case-build-writes-a-plain-round` names a numbering rule that stays.
>   - The rest are the pages this Case changes, the moved Estimates, `rule-plan-mode` (its `children`), and records.
> - Grep `case-schema` over `guppi/` and `tests/` printed 10 files. `guppi/ledger.py` (the refusal message), `guppi/prespec.py` (a comment) and `tests/test_ledger.py` change in 595.17. The other seven stand:
>   - `guppi/pageread.py` and the `hub_files` docstring of `guppi/lint.py` list it as an example of a root file.
>   - `tests/test_render.py`, `tests/test_recall.py`, `tests/test_lint.py`, `tests/test_pages.py` and `tests/test_generate.py` use the name in fixtures of their own.
>
> `guppi recall` prints the `@` lines of the skill, so after a compaction it reprints the new files with no code change. `estimate-claude-md-rendered` says the one rule is in the schema, which becomes false, and is replaced in 595.21.
>
> Hooks and readers. No hook is added. The ledger hook changes only the text of its refusal message, refuses no new line, and loses nothing between Work Mode and the render, so it keeps no old form. On `Stop`, `estimate-case-check-refuses-text-before-a-round` stands: the replies of the loop still open with the labelled waiting line.
>
> What done means. Each sub-case creates an Estimate or replaces a Criterion. The exception is 595.20, which `estimate-glossary-terms-defined` checks with its Criterion unchanged. `estimate-compact-recall-reloads` stands, since it reads the `@` lines of the skill. The related backlog items `rule-case-rebuild-cost` and `insight-session-vault-knowledge-not-loaded` are not touched. `insight-prespec-after-findings-loop-unruled` stays open for synthesis.

> **problem:**
> The main agent loads the form of a Case it does not build, and the design that moves its own rules into a file of their own was put off twice. At `/pre-spec` it sends fixes to the agents that rebuild the Cases before the person has answered the report's questions, so the chat moves on, new rounds arrive, and an answer may change a fix already sent.

> **recommend:**
> - **Its own Case, or part of the whole move**
>   - Recommended: (a) its own Case on `rule-prespec` now, the move left in the backlog.
>   - Answer: (b) part of the whole move, now.
> - **A report with no question, or a question left unanswered**
>   - Recommended: (a) send at once when the report has no question; otherwise hold everything until every question is answered, ask a skipped question again, then send every fix and answer together, one message to each `case-guppi`.
>   - Answer: (a).
> - **The agents' own questions that come back**
>   - Recommended: (a) keep step 2 of the loop as written; the change touches only the first step.
>   - Answer: (a).
> - **The names of the two new rules and their files**
>   - Recommended: (a) `rule-orchestration` rendered into `vault/wiki/orchestration.md`, a new `rule-ratification` rendered into `vault/wiki/ratification.md`, both under `rule-plan-mode`, both loaded by `/hi` in place of `case-schema.md`.
>   - Answer: the person first asked whether two files load at `/hi` in place of `case-schema.md`, whether `case-schema.md` goes to `case-guppi` alone, and whether its text moves or is referred to. Told that it is moved, each sentence in one file only, and that `case-schema.md` keeps its name, the person agreed with (a).
> - **Where the loop after the findings lives**
>   - Recommended: (a) the loop stays in the pre-spec skill, and `orchestration.md` points to it.
>   - Answer: (a).
> - **How the text of `case-schema.md` is shared out**
>   - Recommended: (a) by who acts, sentence by sentence; a sentence both agents need goes to the shared file.
>   - Answer: (a).
> - **How the checks of the moved behaviours move**
>   - Recommended: (b) each moved check is renamed and moved to its new rule, keeping its history and results; the script rewrites every mention.
>   - Answer: (b).

### Case 595.1 — The pre-spec loop sends nothing before the report is answered

> **given:**
> `rule-prespec` — the rule whose Render is the pre-spec skill; its loop after the findings changes
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from it
> **＋** `estimate-prespec-gathers-the-answers-after-findings` — the check of the loop; its Criterion is replaced
> **＋** `.claude/skills/grill-me/SKILL.md` — the question shape of the report's questions and of the rounds
> **＋** `vault/wiki/orchestration.md` — the file that sets the showing of a Case and the one-Case-at-a-time rule, named by the skill in place of `case-schema.md`
> **＋** `rule-case-check` — its `Stop` run, `uv run guppi casecheck`, lets a reply that opens with the labelled line pass

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
> **＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
> **＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
> **＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
> **＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop no Case is taken up before the current one is ratified or deferred.
> **－** A question that no answer settles stays in the next list under its number.

```then
update:
- slug: rule-prespec
  replace:
  - old: 1. Send each finding in a Case that needs no word of the person to the `case-guppi` of that Case by `SendMessage`, all of them in one message. Hold back a finding whose fix waits for the person's answer.
    new: |-
      1. When the report asks the person no question, go on to step 2 at once. Otherwise send nothing to any `case-guppi` until the person has answered every question of the report, since an answer may change a fix. A question the person leaves unanswered you ask again, in its grill-me shape and under its number, and everything stays held (case 595.1).
      2. Send each finding in a Case, with each answer of the person that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, all of them in one message.
  - old: 2. Wait for every `case-guppi` you sent to answer,
    new: 3. Wait for every `case-guppi` you sent to answer,
  - old: waits for the list of step 3
    new: waits for the list of step 4
  - old: '3. Show the person one list of what to answer: your own questions still open and every round that came back, each question in its grill-me shape, translated as a round of `case-guppi` is, and numbered `<Case id>.Q<n>` — the id of its Case and its number in the round, or in your report for your own — so that each answer goes back to its `case-guppi`.'
    new: '4. Show the person one list of what to answer: every round that came back, each question in its grill-me shape, translated as a round of `case-guppi` is, and numbered `<Case id>.Q<n>` — the id of its Case and its number in the round — so that each answer goes back to its `case-guppi`.'
  - old: 4. Send each answer, and each finding held back for it, to the `case-guppi` of its Case, all in one message, and go on from step 2 until every `case-guppi` you sent has answered with its Case.
    new: 5. Send each answer to the `case-guppi` of its Case, all in one message, and go on from step 3 until every `case-guppi` you sent has answered with its Case.
  - old: 5. Show every Case built again in one reply, each in the showing that `vault/wiki/case-schema.md` sets, for one ratification.
    new: 6. Show every Case built again in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
  - old: Inside this loop the rule of `vault/wiki/case-schema.md` that no Case is taken up
    new: Inside this loop the rule of `vault/wiki/orchestration.md` that no Case is taken up
  change: the loop after the findings sends nothing to a case-guppi until the person has answered every question of the report; the findings and the answers then go out together; the showing named in orchestration.md (case 595.1)
- slug: estimate-prespec-gathers-the-answers-after-findings
  set:
    status: pending
    purpose: Whether after the findings of pre-spec the main agent sends nothing to a case-guppi until the person has answered every question of the report, then sends each case-guppi its findings with the answers in one message, ends each waiting turn with one labelled line and writes nothing else while answers are out, gathers every round into one numbered list, and shows the Cases built again in one reply
    method: by hand at the /pre-spec of a later session after the render whose report asks the person a question and sends findings to two or more case-guppi, the replies between the report and the showing again, the SendMessage calls and any refusal of guppi casecheck read in the transcript
  change: the Criterion replaced whole - nothing goes to a case-guppi before every question of the report is answered (case 595.1)
```

```tasks
- [ ] update `rule-prespec`
- [ ] update `estimate-prespec-gathers-the-answers-after-findings`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-gathers-the-answers-after-findings`
```

### Case 595.2 — `rule-orchestration` renders what the main agent alone does

> **given:**
> `rule-orchestration` — the placeholder that becomes the rule of what the main agent alone does, rendered in full; its defers are retired
> **＋** `vault/wiki/orchestration.md` — the file it renders, at the root of `vault/wiki/`
> **＋** `rule-case-protocol` — the rule whose Render held this text until now
> **＋** `rule-plan-mode` — the parent rule of the phase
> **＋** `rule-render-harness` — the renderer, `uv run guppi render` and its `--check`
> **＋** `rule-guppi-config` — sets the languages that fill the placeholders of the Render
> **＋** `rule-vault-layout` — a root file of `vault/wiki/` needs a live rule page that names it
> **＋** `.claude/skills/hi/SKILL.md` — the skill that loads the file
> **＋** `CLAUDE.md`, `vault/wiki/case-schema.md`, `vault/wiki/ratification.md` — the other texts, none of which repeats it
> **＋** `estimate-orchestration-loaded` — the new check of the rule

> **when:**
> `/hi` opens a session after `uv run guppi render` wrote `vault/wiki/orchestration.md` from `rule-orchestration`.

> **then:**
> The context of the session holds `vault/wiki/orchestration.md` from the first turn after `/hi`, expanded by `.claude/skills/hi/SKILL.md` with no read call.
> **＋** `uv run guppi render --check` exits 0: the file equals the Render of `rule-orchestration`, its language placeholders filled from `rule-guppi-config`.
> **＋** The file holds what the main agent alone does: the Frontier and Plan Mode, the dispatch of `case-guppi`, the showing and the signing of a Case, the moment each ledger line is written, the short form of a defer and the acknowledging reply.
> **－** `CLAUDE.md`, `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` repeat no paragraph of `vault/wiki/orchestration.md`.

```then
create:
- slug: rule-orchestration
  ref: rule-plan-mode
  kind: Leaf
  enforcement: render
  governs: vault/wiki/orchestration.md
  render_mode: full
  purpose: 'Prevents the main agent from loading the form of a Case it does not build: what it alone does in a working session - the Frontier, the dispatch of case-guppi, the showing and signing of a Case, the moment of each ledger line, the defers and the acknowledging reply - stands in orchestration.md, which /hi loads'
  estimates:
  - '[[estimate-case-protocol-acknowledging-reply]]'
  - '[[estimate-case-protocol-shows-the-frontier-after-a-closed-line]]'
  - '[[estimate-case-protocol-defers-in-one-reply]]'
  - '[[estimate-case-protocol-shows-the-built-case]]'
  - '[[estimate-case-protocol-forwards-a-discussion-question]]'
  - '[[estimate-case-protocol-asks-in-the-grill-me-shape]]'
  - '[[estimate-case-protocol-puts-the-harness-before-plan-mode]]'
  - '[[estimate-case-protocol-names-related-cases-in-the-dispatch]]'
  tags:
  - session
  - workflow
  - harness
  sections:
    Render: |-
      <!-- rule-orchestration -->
      # Orchestration — what the main agent does

      `wiki/orchestration.md` — the Render of `rule-orchestration`, loaded by `/hi` with `sprint.md`, `backlog.md`, `brief.md`, `ratification.md` and `glossary.md`, so what the main agent does is present from the first turn of a working session. The main agent builds no Case and does not load its form: the form of a Case is `case-schema.md`, read by `case-guppi` alone; the one rule, the form of the ledger lines, atomicity and the harness are `ratification.md` (case 595). The layout of the vault is [[rule-vault-layout]] and the phases of a session [[rule-session]].

      **One agent response ≈ one Case.**

      ## Plan Mode and the Frontier

      One reply shows one Case, in the form of `case-schema.md` as `case-guppi` built it. That is the form of Plan Mode. In a working session the rules the harness loads come before the Plan Mode instructions of Claude Code: the main agent launches no Explore or Plan agent — `case-guppi` builds each Case and `ask-guppi` asks the vault at `/pre-spec` —, asks the person by a plain question in the chat, never by a picker tool, except where a rule names one, such as the choice between `/work` and `/carry` after the Spec is written, and calls `ExitPlanMode` only after `/pre-spec` (case 561.14). The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`; close its line in the reply that ends the item — `[x]` for an item ended: `· case N` when ratified, `· work` when it needed no decision; `[-]` for an item put off: `[-] … · sprint · defer` for an item of the sprint left for later — no Case, never `· defer case N` (case 356.2) — `[-] … · backlog · kept` for an item of `backlog.md` left as it stands, and `[-] … · defer case N` for a decision of any other source put off (case 451.1). A reply after the first reply of `/hi` and before the end of Plan Mode that closes a line of `frontier.md` with no ratification and no defer — an `A` line by the person's answer, a `W` line by a reading, a `C` line that needs no decision, an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept` — ends as the acknowledging reply ends: a heading `## Frontier`, the lines of `frontier.md` as a checklist in its form, and, last, the question which open item is next; when no line under `## Cases` is open, it asks nothing: a reply with no `LEDGER` block calls `/pre-spec` after the Frontier, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on (case 561.6); a reply that closes several lines shows one Frontier; the first reply of `/hi` keeps the form `rule-skill-hi` sets, and a line closed in Work Mode or at Retro shows none (case 547). Plan Mode does not end while a line under `## Cases` is open — a `W` line closes when its work is done (case 356.1); `/pre-spec` checks it. Never move to the next Case until this one is ratified or deferred — but in the loop after the findings of `/pre-spec`, where the Cases built again go out together and come back for one ratification, as `rule-prespec` sets it (case 561.2).

      ## Who builds a Case

      Every Case, in Plan Mode and in Work Mode, at its first showing and at every showing again — a ratified Case that changed included — is built by the agent `case-guppi` (`rule-case-build`): the agent dispatches it with the Case id, the Frontier item and its source, and the person's words on it, and each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment, such as a reply, a hook event or a command, by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the main agent judging which Cases are related and `case-guppi` reading no other Case of the session (case 579.1) — in the prompt of the call, not in the chat — and creates the plan file with its title line before the first dispatch of the session. A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`, and so do the person's answers to a round of questions, verbatim and untranslated. A request for a plain explanation — of a round, of the short text on a Case or of a reply, by `/wait-what` or in the person's words — is not such a question: the main agent answers it itself by the skill `wait-what` (`rule-skill-wait-what`), and asks the `case-guppi` of the Case by `SendMessage` only for a fact of the Case it does not hold; `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading (case 477.3). A question of the person that asks to discuss an item, or to learn something of it, while its `case-guppi` builds its Case or after it showed it, the main agent does not answer from its own reading: it sends the question to that `case-guppi` by `SendMessage`, verbatim and untranslated, and `case-guppi` answers in plain words under a first line `**Fact:**`, or with a round when the question opens a fork; the main agent shows that answer translated into {{chat_lang}} and asks again the question that stood open (case 561.12). The agent shows the Case of the answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, the file the `SubagentStop` hook of `rule-case-check` writes from the answer; in the same reply it writes the heading of the top-level Case, its name in {{chat_lang}}, and under it one list — an item per Case and sub-case of the answer, its id, its name in {{chat_lang}} and a short text in {{chat_lang}} on what done means and how it is checked, taken from the Estimate the Case creates or whose Criterion it replaces, or from the Estimate its `context` names as already checking the change — then one `ratification` section whose fence holds the ledger lines of every Case of the list as the answer holds them, never its `given`, `when`, `then` or `tasks`, then its own text after one horizontal rule; an answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before it is shown (case 561.9); a reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it (case 452.4); a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question (case 561.9); an answer with no Case heading and no first line `**Fact:**` is a round of questions by the skill `grill-me` (`rule-case-build`), which the agent shows translated into {{chat_lang}} line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule — and no Case is shown; a round may come at the first answer on an item, after a question or a change on a shown Case, and in Work Mode when a ratified Case is built again, and the showing of the Case and its ratification confirm the rounds, with no step of their own. An item that needs no decision — Work, a reading again — the agent closes alone, with no dispatch. `case-guppi` asks the vault before a `create` and reads the frame itself; the agent dispatches `ask-guppi` once, at pre-spec. A deferred decision in the short form is the agent's own, written with no dispatch (case 419.1). A question the main agent puts to the person itself — a decision it needs in the report of `/pre-spec`, a question at `/hi`, a question at a stop of Work Mode — takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered title line, the `**Now:**` line, the options under `**Options:**`, each with its `**After:**` item, and the recommended answer on the `➡️` line, in {{chat_lang}}, the labels translated or not; the question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question, which asks for a reading and not a choice —, the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` keep their own form (case 561.13).

      ## Showing and signing a Case

      In the chat the heading of the top-level Case stands with its name in {{chat_lang}}, over the list of its Cases (cases 452.4, 561.9). The agent's own text stands after the Case, after one horizontal rule, and the turn ends with a plain question in the chat, never a picker tool (case 355.1). In the chat one horizontal rule at most, after the Case, its last sub-case or the last question of a round, and only when the agent's own text follows. A Case the person changed, or one whose text or scope the agent finds wrong or too narrow after its ratification — in the Spec, at pre-spec or in Work Mode — is shown again. A Case not yet ratified is sent again whole, in its file (case 452.4). A ratified Case changes through its `case-guppi`, in its prose as in its body; the agent does not edit the plan file, and the hook of `rule-spec-reconcile` refuses its edit, the title line that creates the file excepted (case 445.1). Its new answer is sent again whole, in its file, in Plan Mode as in Work Mode, and ratified again, since the hook of `rule-spec-write` writes a Case only from its stored answer after a reply that carries its lines; until then nothing of the change is acted on (cases 438, 441).

      {{chat_lang}} in the chat with the owner for the name and the short text of each Case and sub-case in the list that goes with the file, a round of questions of `case-guppi`, translated from the answer, and the agent's own text; the ledger lines of `ratification` stand in the chat as the answer holds them, the words the vault will hold (cases 387.1, 441, 452.5). The main agent writes a short-form Case in {{documentation_lang}} in the chat, and the hook writes it as shown (case 441).

      A Case with sub-cases is shown in one reply, its file and one list under the heading of the parent, as `Who builds a Case` sets it; the person ratifies them all at once or names the ids, and the acknowledging reply carries one `LEDGER` block with the lines of every sub-case ratified, one heading `## Case N — ratified` naming those ids, and one Frontier; a sub-case the person questions or changes is shown again alone (case 355.2).

      Work Mode ticks the boxes on code, tests, migrations and `by hand` checks in `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73), in the reply that finishes the task; `generate` ticks the page lines and the `read` lines whose reading stands in the ledger, `render`, `sprint` and `glossary` the render, sprint and glossary lines (cases 226, 250, 270, 306); Retro counts the unticked (case 59.3).

      ## The short form — deferred decisions

      A deferred decision is its own Case in the short form — `## Case N — name`, then `context`, `problem`, and a `then` block with `defer:` carrying `slug`, `type` and `purpose` — a value that holds a `#` after a space or a tab stands in quotes, since YAML drops the rest of the line at a `#` after a space, PyYAML, the library the scripts use, refuses the whole block at a `#` after a tab, and the `Stop` hook of `rule-spec-write` refuses a block that holds either (cases 521.4, 526); no `recommend`, `given`, `when`, `then` or `ratification` section. It has one moment: the close of Plan Mode, when the person defers the items left open; Retro runs without the person and puts nothing off — what it would put off is a line of `## For the next session` of `handoff.md` (case 531.14). The person's words asking for the defer are its ratification: in the same reply the agent shows it and carries its ledger line, and the `Stop` hook of `rule-spec-write` writes it under the `## Deferred` heading of the plan file — the agent writes none of it (case 421.2) — then the Frontier with the line closed `[-] … · defer case N` and, last, the question which open item is next, with no text after it — or, when no line under `## Cases` is open, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on to `/pre-spec` (case 561.7); it asks nothing about the defer itself (case 461); a wording the person corrects is a new short Case with `{supersedes:case N}`, written the same way (case 405). It stands there with one item per target, so `materialize` finds it like any other Case; a defer line without its Case is marked `incomplete`. Two or more pages share one Case only when one context and one problem hold for all of them. A page-less Slice task goes to `sprint.md`, not into a defer. An item of `backlog.md` left as it stands is no decision: no short Case, no ledger line; its Frontier line closes `[-] … · backlog · kept`, its source stays as it is — the `deferred_by` of its page, the `open` status of its Insight, or its line in the sprint page's `## Backlog` — and the item stays in the backlog, its count grown by one (cases 421.4, 451.1). The target of a short Case enters `backlog.md` through the `deferred_by` that `generate` writes. How a deferred decision is taken up is `case-schema.md`. A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5).

      ## Writing the ledger lines

      The form of each line is `ratification.md`. Write the `- decision[...]` lines only in the reply that acknowledges ratification; `- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson exists, but from `/work` to the end of Retro in the one reply that ends Retro, which carries them all (case 531.8) — a reading of an Estimate that a decision line of this session creates or updates waits for a later session, and the ledger hook refuses it (case 428.1) — an `estimate[...]` line opening with the date of the reading and the command or the place it was read (case 199). Without `/hi` the hook refuses and says so: tell the person, do not retry. A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call waits for the next `Stop` of the session, and the last reply of a session has none. When a `Stop` hook other than the ledger hook refuses a reply that carries a `LEDGER` block — exit 2 — the ledger hook has written the block at that same `Stop`: the agent's answer to the refusal is a reply of its own and may call tools (case 414.2). A block a tool call did follow is not lost until that `Stop` has passed: check the ledger then, and only a line missing there is a lesson.

      ## The acknowledging reply

      The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first; a heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open `W` lines folded into one line that lists their ids, the other open ones one per line with a short title (case 578.2), the lines put off as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N` — and, last, the question which item is next, or, when no line under `## Cases` is open, no question: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on (case 561.8). Headings and labels in the language of the chat (case 167, supersedes 157). The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification: the ledger hook does not append a line it already holds, and the hook of `rule-spec-write` writes a Case into the Spec only after a reply that carries its lines (case 390).
      <!-- /rule-orchestration -->
- slug: estimate-orchestration-loaded
  ref: rule-orchestration
  kind: QA
  purpose: What the main agent alone does is present in a session from the first turn after /hi, as one text, the Render of rule-orchestration, repeated in no other file the session holds
  method: uv run guppi render --check; by hand at the first /hi of a later session after the render, vault/wiki/orchestration.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and ratification.md
  tags:
  - session
  - harness
```

```tasks
- [ ] create `rule-orchestration`
- [ ] create `estimate-orchestration-loaded`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-loaded`
```

### Case 595.3 — `rule-ratification` renders what both agents need

> **given:**
> `rule-ratification` — the new rule of the one rule, the form of the ledger lines, atomicity and the harness, rendered in full
> **＋** `vault/wiki/ratification.md` — the file it renders, at the root of `vault/wiki/`
> **＋** `rule-atomicity` — its child, spliced into its marker line
> **＋** `rule-case-protocol` — the rule whose Render held this text until now
> **＋** `rule-plan-mode` — the parent rule of the phase
> **＋** `rule-render-harness` — the renderer, `uv run guppi render` and its `--check`
> **＋** `rule-vault-layout` — a root file of `vault/wiki/` needs a live rule page that names it
> **＋** `.claude/skills/hi/SKILL.md` — the skill that loads the file
> **＋** `CLAUDE.md`, `vault/wiki/case-schema.md`, `vault/wiki/orchestration.md` — the other texts, none of which repeats it
> **＋** `estimate-ratification-loaded` — the new check of the rule

> **when:**
> `/hi` opens a session after `uv run guppi render` wrote `vault/wiki/ratification.md` from `rule-ratification`.

> **then:**
> The context of the session holds `vault/wiki/ratification.md` from the first turn after `/hi`, expanded by `.claude/skills/hi/SKILL.md` with no read call.
> **＋** `uv run guppi render --check` exits 0: the file equals the Render of `rule-ratification`, the text of `rule-atomicity` between its markers.
> **＋** The file opens with the one rule and holds the form of the ledger lines, atomicity and the harness.
> **－** `CLAUDE.md`, `vault/wiki/case-schema.md` and `vault/wiki/orchestration.md` repeat no paragraph of `vault/wiki/ratification.md`.

```then
create:
- slug: rule-ratification
  ref: rule-plan-mode
  kind: MOC
  enforcement: render
  governs: vault/wiki/ratification.md
  render_mode: full
  children:
  - '[[rule-atomicity]]'
  estimates:
  - '[[estimate-case-protocol-ledger-line-form]]'
  purpose: 'Prevents an agent of a working session from acting without the one rule and the form of the ledger lines: the one rule, the form of the ledger lines, atomicity and the harness stand in ratification.md, which /hi loads and case-guppi reads'
  tags:
  - session
  - workflow
  - ledger
  - harness
  sections:
    Render: |-
      <!-- rule-ratification -->
      # Ratification — the one rule and the ledger

      ## The one rule

      Nothing in the vault or the codebase changes without a Decision ratified by the human. The agent has full autonomy over *how* to implement something once its contract is ratified, and none over the contract itself. When unsure whether something needs ratification: it does. The vault is the only memory: no note outside the repository — not the harness's memory directory, not a file outside `vault/`; what is worth keeping is a `lesson` line or a Case on a Rule page (case 272.1).

      `wiki/ratification.md` — the Render of `rule-ratification`, loaded by `/hi` and read whole by `case-guppi`, so both agents hold what each of them needs: the one rule, the form of the ledger lines, atomicity and the harness (case 595). What the main agent alone does is `orchestration.md`; the form of a Case is `case-schema.md`. A session without `/hi` holds no Case: the ledger hook refuses it. A Case is ratified by the person's reply in the chat — a sign-off, a question or their own alternative —, never by a picker tool, and ratifying a parent does not ratify its children.

      <!-- rule-atomicity -->

      ## What a Case produces

      | Outcome | Ledger line |
      |---|---|
      | ratified decision | `- decision[case 12][update][rule-x]{ref:rule-x}` or `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` |
      | a measurement taken | `- estimate[slug][passed\|failed] <date, command or place; the result>` (case 199) |
      | something learned | `- lesson[error\|knowledge][slug]{tags:a,b} trigger: <...> root_cause: <...>` |

      The id is `case N` — the word and a space — in the first bracket and in `{supersedes:case N}` alike; `{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1), and a line carries one `{supersedes:case N}` block per Case it supersedes, several side by side, never a list inside one block (case 429); `{addresses:<lesson slug>}` stands on a decision line whose Case closes the root cause of a lesson of this session — written when the lesson line already stands in the session's ledger, one mark per lesson; a lesson line written after the Case of this session that closed its cause carries `{addressed_by:case N}` instead, naming that Case — for a Case with sub-cases the sub-case whose decision line closes the cause, since the parent has no decision line and the ledger hook refuses a mark with no decision line of its Case before it (case 497.4) — one of the two marks per pair, by the order of the lines (case 379); a lesson whose fix is ratified in another session gets no mark (case 284.2).

      **Decision lines are markup only** — their content already sits ratified in the Spec, so the
      line just names what happens to which page, and the tags a `create` was ratified with.

      **Estimate and lesson lines carry their text inline.** Their content is born in the moment
      and exists nowhere else: a measurement taken after the tests were written, a failure
      understood while still fresh. There is nothing in the Spec to point at.

      An `estimate[...]` line does not replace the `decision[...]` that created the page — the
      decision made it exist, the estimate line fills it.

      Only the **main agent** writes ledger lines. A subagent that takes a measurement returns it; the main agent records it. A subagent that hits a fork stops and returns — it never decides.

      Ledger lines are written by the `Stop` hook, from the reply, verbatim, each with the time of writing. A record is a `- decision[...]`, `- estimate[...]` or `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag; the same line anywhere else — bare, or in a block with another tag or none — is a preview and is never written. A `create` line carries the ratified tags: `{tags:a,b}`. A `knowledge` lesson line carries `{source:...}`, the url or reference the lesson studied — a file of the harness, a probe, a client version; the schema requires it, and a line without it is `incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson never carries one. When each line is written, and what a reply that carries a `LEDGER` block does after it, is `orchestration.md`.

      ## The harness

      The harness — hooks, skills, agents, `settings.json`, `CLAUDE.md`, this file, `orchestration.md` and `case-schema.md` — is rendered from `rules/`. A harness file changes through an `update` of its Rule page, never by hand; a hook refuses the edit.
      <!-- /rule-ratification -->
- slug: estimate-ratification-loaded
  ref: rule-ratification
  kind: QA
  purpose: The one rule, the form of the ledger lines, atomicity and the harness are present in a session from the first turn after /hi, as one text, the Render of rule-ratification, repeated in no other file the session holds
  method: uv run guppi render --check; by hand at the first /hi of a later session after the render, vault/wiki/ratification.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and orchestration.md
  tags:
  - session
  - harness
```

```tasks
- [ ] create `rule-ratification`
- [ ] create `estimate-ratification-loaded`
- [ ] `uv run guppi render`: `vault/wiki/ratification.md`
- [ ] read `estimate-ratification-loaded`
```

### Case 595.4 — `/hi` loads the two files in place of `case-schema.md`

> **given:**
> `rule-internal-context` — the rule of the `@` lines of `/hi`
> **＋** `.claude/skills/hi/SKILL.md` — the skill that holds the lines
> **＋** `estimate-internal-context-loaded` — the check of what the first turn holds; its Criterion is replaced
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/ratification.md`, `vault/wiki/glossary.md`, `vault/wiki/case-schema.md` — the files the lines name, and the one they no longer name
> **＋** `rule-compact-recall` — `guppi recall` prints the paths of these lines after a compaction; its purpose names what `/hi` loads
> **＋** `rule-claude-md` — its Purpose and How it works say what arrives with `/hi`
> **＋** `librarian-guppi`, `ask-guppi` — subagents that carry none of these texts

> **when:**
> The person invokes `/hi`, with `.claude/skills/hi/SKILL.md` rendered from `rule-internal-context`.

> **then:**
> The text of `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/ratification.md` and `vault/wiki/glossary.md` is in the context of the first turn, in that order, without a read call.
> **＋** `vault/wiki/case-schema.md` is not in it.
> **＋** The glossary and the backlog reach a session through this block alone. After a compaction, the paths of these files are in the list of `guppi recall`.
> **－** A subagent, such as `librarian-guppi`, `ask-guppi` or one of Work Mode, carries none of these texts. Its prompt names what it needs.

```then
update:
- slug: rule-internal-context
  replace:
  - old: '@vault/wiki/case-schema.md'
    new: |-
      @vault/wiki/orchestration.md
      @vault/wiki/ratification.md
  - old: '`case-schema.md` is listed since case 273: the Render of `rule-case-protocol`, it reaches a working session here and not through `CLAUDE.md`, so a session without `/hi` carries no Case text.'
    new: '`orchestration.md` and `ratification.md` are listed since case 595, in place of `case-schema.md`, listed from case 273: they reach a working session here and not through `CLAUDE.md`, so a session without `/hi` carries none of their text, and the form of a Case, `case-schema.md`, reaches only `case-guppi`, which reads it itself.'
  change: /hi loads orchestration.md and ratification.md in place of case-schema.md (case 595.4)
- slug: estimate-internal-context-loaded
  set:
    status: pending
    purpose: The text of sprint.md, backlog.md, brief.md, orchestration.md, ratification.md and glossary.md is present in the first turn's context after /hi, without a read call, and case-schema.md is not
  change: the Criterion replaced whole - orchestration.md and ratification.md in place of case-schema.md (case 595.4)
- slug: rule-claude-md
  replace:
  - old: the glossary and the Case schema arrive with `/hi`, the one rule opens the schema (cases 272, 273.3, 288.3).
    new: the glossary, `orchestration.md` and `ratification.md` arrive with `/hi`, the one rule opens `ratification.md`, and the Case schema reaches `case-guppi` alone (cases 272, 273.3, 288.3, 595).
  - old: The glossary and the Case schema arrive with `/hi` through `rule-internal-context`, and the one rule opens the schema (case 288).
    new: The glossary, `orchestration.md` and `ratification.md` arrive with `/hi` through `rule-internal-context`, and the one rule opens `ratification.md` (cases 288, 595).
  change: the texts that arrive with /hi are orchestration.md and ratification.md, the one rule opens ratification.md (case 595.4)
- slug: rule-compact-recall
  set:
    purpose: Prevents a working session from going on after a compaction without the texts /hi loads, the Frontier and the Spec in its context
  replace:
  - old: Prevents a working session from going on after a compaction without the Case schema, the Frontier and the Spec in its context.
    new: Prevents a working session from going on after a compaction without the texts `/hi` loads, the Frontier and the Spec in its context.
  change: the purpose names the texts /hi loads, no longer the Case schema (case 595.4)
```

```tasks
- [ ] update `rule-internal-context`
- [ ] update `estimate-internal-context-loaded`
- [ ] update `rule-claude-md`
- [ ] update `rule-compact-recall`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-internal-context-loaded`
```

### Case 595.5 — Atomicity renders into `ratification.md`

> **given:**
> `rule-atomicity` — the rule of when a unit splits; its file and parent change
> **＋** `rule-ratification` — its new parent, a MOC with a marker line for it
> **＋** `rule-case-protocol` — its parent until now
> **＋** `vault/wiki/ratification.md` — the file its text renders into
> **＋** `/hi` — the command whose skill loads that file at the start of a working session
> **＋** `estimate-atomicity-rendered` — its check; its Criterion is replaced
> **＋** `rule-governed-files-hook` — the hook that refuses a hand edit of a rendered file
> **＋** `rule-prespec` — holds the one mechanical refusal of two promises in one Case

> **when:**
> `uv run guppi render` writes the governed files, and `/hi` loads `vault/wiki/ratification.md` at the start of a working session.

> **then:**
> `vault/wiki/ratification.md` holds the text of `rule-atomicity` between its markers: the statement, the pair test — list the conditions of "done", and for each pair ask whether one could fail while the other passes and needs a different fix — and the scope: Case, Entity, Rule, Estimate; not a Lesson, a recorded fact does not split; not an Insight, which is born by clustering, the same rule in reverse; depth is not fixed in advance.
> **＋** `uv run guppi render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
> **＋** `rule-ratification` is a MOC with the child `rule-atomicity` and a marker line for it in its Render.
> **－** The rule has no refusal of its own in substance: the refusal of two promises in one Case stays with `rule-prespec`.

```then
update:
- slug: rule-atomicity
  set:
    governs: vault/wiki/ratification.md
    parent: '[[rule-ratification]]'
  replace:
  - old: the text stands in the file the agent reads — `case-schema.md`, loaded by `/hi` in every working session —
    new: the text stands in the file both agents read — `ratification.md`, loaded by `/hi` in every working session and read by `case-guppi` —
  change: rendered into ratification.md under rule-ratification (case 595.5)
- slug: estimate-atomicity-rendered
  set:
    status: pending
    purpose: The text of rule-atomicity stands between its markers in ratification.md, identical to the page, and a hand edit of the file is refused
    method: uv run guppi render --check exit 0; the text between the markers of ratification.md read by hand after the librarian's render
  change: the Criterion replaced whole - the text renders into ratification.md under rule-ratification (case 595.5)
```

```tasks
- [ ] update `rule-atomicity`
- [ ] update `estimate-atomicity-rendered`
- [ ] read `estimate-atomicity-rendered`
```

### Case 595.6 — `case-schema.md` keeps the form of a Case alone

> **given:**
> `rule-case-protocol` — the rule whose Render is the form of a Case; the text that moves leaves it, and its purpose is reworded
> **＋** `vault/wiki/case-schema.md` — the file it renders
> **＋** `vault/wiki/orchestration.md`, `vault/wiki/ratification.md` — the files that take the text that moves
> **＋** `rule-guppi-config` — sets the languages that fill the placeholders of the Render
> **＋** `.claude/skills/hi/SKILL.md` — the skill that no longer loads the file
> **＋** `.claude/agents/case-guppi.md` — the agent that reads it
> **＋** `CLAUDE.md` — the system prompt, which repeats none of it
> **＋** `estimate-case-protocol-loaded` — the check of the file; its Criterion is replaced
> **＋** `estimate-case-protocol-case-form` — the check of the form, which stays on the rule

> **when:**
> `uv run guppi render` wrote `vault/wiki/case-schema.md` from `rule-case-protocol`, and a session opened by `/hi` dispatches `case-guppi` by `.claude/agents/case-guppi.md`.

> **then:**
> `uv run guppi render --check` exits 0: the file equals the Render of `rule-case-protocol`, its language placeholders filled from `rule-guppi-config`.
> **＋** The file holds the form of a Case: its sections, operands and language, the `then` block, the task lines, the taking up of a deferred decision, the sub-cases and the slug.
> **＋** `.claude/skills/hi/SKILL.md` holds no `@` line for `vault/wiki/case-schema.md`, and the main agent reads none of it in the session.
> **－** The file repeats no paragraph of `vault/wiki/orchestration.md` or `vault/wiki/ratification.md`, and `CLAUDE.md` repeats none of its paragraphs.

````then
update:
- slug: rule-case-protocol
  set:
    purpose: Prevents a Case from being built in a form the scripts cannot read, or shown for ratification without its content in view
    kind: Leaf
    children: []
    estimates:
    - '[[estimate-case-protocol-loaded]]'
    - '[[estimate-case-protocol-case-form]]'
  sections:
    Purpose: 'Prevents a Case from being built in a form the scripts cannot read, or shown for ratification without its content in view. This is instruction, not enforcement — no hook can judge a whole Case in substance — so it is written where the agent that builds a Case reads it: `vault/wiki/case-schema.md`, the Render of this page, which `case-guppi` reads whole with `ratification.md` before it answers. Until case 595 `/hi` loaded the file into the main agent''s context with what the main agent does and the one rule; those moved to `rule-orchestration` and `rule-ratification`, with the child `rule-atomicity` and the Estimates of the behaviours that moved, so the main agent no longer carries the form of a Case it does not build. Until case 273 the Render was a section of `CLAUDE.md` and the schema a file edited by hand; the two said the same thing twice and were signed twice. `parent: rule-plan-mode` is the rule of the phase in which a Case is held (case 188).'
    Render: |-
      <!-- rule-case-protocol -->
      # Case — schema

      `wiki/case-schema.md` — the Render of `rule-case-protocol`: the form of a Case, read whole by `case-guppi` with `ratification.md` before it answers. The main agent does not load it; what the main agent does with a Case — the dispatch, the showing, the acknowledging reply, the Frontier and the defers — is `orchestration.md`, the Render of `rule-orchestration` (case 595). The layout of the vault is [[rule-vault-layout]] and the phases of a session [[rule-session]].

      A Case is the unit of dialogue, not a vault page. It lives only inside a session. This schema exists because the Case is where content gets ratified: whatever is not in a Case was never signed by anyone.

      ## Sections

      Eight, in this order, under the heading `## Case N — name` — in the file of the Case at every showing and in the Spec, in {{documentation_lang}} (case 452.4); in the file and in the Spec a sub-case under `### Case N.M — name` beneath its parent (case 368). Each section is one blockquote: the first line `**name:**`, the text on the following quoted lines.

      | Section | Required | Content |
      |---|---|---|
      | `context` | yes | What this is about, in plain words: prose only — the mechanism, where it goes wrong, the state of the pages, the vault's answer; no list of what the Case touches, that is `given` (case 378.1). In Work Mode this may shrink to a one-line reference back to an earlier Case; it is never omitted. |
      | `problem` | yes | What requires a decision. |
      | `recommend` | yes | The record of the choices: one item per question of the rounds of `case-guppi` — the question, what it recommended, the person's answer in English, both as they stood when the person answered it, or a note that it was not answered (case 557.2) — one per change the person asked for on the shown Case, and, with no round, one item of the recommendation ratified as built; an item may stand on the parent whatever it changed, and a sub-case carries only items whose answer changed it alone (cases 544.2, 568). Carried onto the Decision page as `## Recommend` (case 544.7). |
      | `given` | yes | The frame of the Case, one thing per line: each page the Case creates or changes, each module, file and test its `tasks` touch, and the rule that constrains — its slug or path in a code span and a few words on its role, never its state; `when` and `then` name only what `given` names. It stays in the Case, in its Case file and in the Spec, and never enters an Estimate or a Decision page (cases 378.1, 513). |
      | `when` | yes | The action that triggers the behaviour: a hook fires, a script runs, the person invokes a skill. For a change to a document, the moment someone reads it. |
      | `then` | yes | What holds after the action, once the recommendation is accepted. Behaviour only: no Estimate block, no reading, no `supersedes` — those are lines of `tasks` (cases 159, 188). |
      | `tasks` | yes | The work the Case leaves: a checklist, one line per page `update`, file, test, command, one-off migration and reading, a task that waits for the person's word before it runs opening its text with `stop:` (`rule-where-to-stop`, case 531.7); no `contract` line, no "block N" line (case 188). In the file of the Case a blockquote with the checklist, and under a line whose item writes content that content as sub-points — `old` and `new` of each `replace` or `reword` pair, the value of a `set`, the text of a `sections`, the fields of a `create` — each on its own sub-point (case 370); in the Spec the block tagged `tasks`, the same lines without the sub-points, whose content is the `then` block (case 159). |
      | `ratification` | yes | In the chat, the preview of the ledger lines in an untagged fence and nothing else, each line in the form of the table of `ratification.md`; how a Case is shown, signed and shown again is `orchestration.md` (cases 355.1, 452.4). |

      ## Operands

      In `given`, `when` and `then`, the first line stands alone. Every further line starts with a bold operand. **＋** is "and", in any of the three: one more thing in the frame, one more action of the trigger, one more result. **－** is "but", most often in `then`: an effect that must not occur, or an exception — only about what `given` or `when` names; a line that names nothing of them is not written. One statement per line. More than seven **＋** lines in `given` or `then` are a sign the Case is not atomic (`rule-atomicity`). `context`, `problem` and `recommend` carry no operand (case 378.6).

      ## Language

      Short sentences. One idea per sentence. Active voice. A common word over a term. `case-guppi` writes the whole Case in {{documentation_lang}} (case 441). A Case it built reaches the person whole in {{documentation_lang}}, in the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that the agent sends (case 452.4); what the chat shows of it, and in which language, is `orchestration.md`. {{documentation_lang}} in everything that lands in the vault, in the manner of ASD-STE100 Simplified Technical English when that language is English: the Spec is written from the {{documentation_lang}} answer and the {{documentation_lang}} short form, slugs, field names and ledger lines unchanged (cases 123, 387.1, 441, 476.2). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`; the two are set in `rule-guppi-config`, rendered into `guppi.toml`.

      The story sections — `context`, `problem`, `recommend` — name the slug of the thing described only; no count of sentences, the shape of each bounds it: `context` is prose: it opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages, and closes with the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame, and why an Estimate of the rule is not touched; the list of what the Case touches is `given` (case 378.1); `context`, `problem` and `recommend` explain briefly — a sentence per part where one is enough, a part with nothing to say left out — and may name a case number as the source of a claim; no script judges their text but for the titles of the items of `recommend`, which the hook of `rule-case-check` compares with the questions of the rounds (case 544.3): the person does, and a complaint of their length or clarity is what changes them (case 449); `problem` says what is wrong, or the question answered, in one paragraph; `recommend` is a list, one item per question of the rounds: its first line the title of the question in bold as the round wrote it, then a sub-item `Recommended:` and a sub-item `Answer:`, the person's answer in English, both as they stood when the person answered that question; a later question that replaced an earlier one is an item of its own, a question asked in more than one round is one item, of the last round in which the person answered it, and a question never answered says so in its `Answer:` sub-item (case 557.2); a change the person asked for on the shown Case is an item `**Change**` with the lines `Asked:` and `Taken:`; a Case with no round has one item, a line `Recommended:` and the line `Answer: ratified as built` (case 544.2). `given` holds the frame, one thing per line: the pages, modules, files and tests the Case touches and the rule that constrains; no state, no history, no quotation (case 378.1). `then` holds behaviour only; the bookkeeping is `tasks`. `given`, `when` and `then` hold no count of items — pages, lines, Estimates, Cases, tests — since `when` and `then` become the Criterion of an Estimate and a count goes stale there first; a number that states a condition or a limit, such as more than 400 000 tokens, stands (case 449). Slugs, file names and field values sit in code spans; bold is for section labels and operands only, and for the title of a question of a round and the title of an item of `recommend`, as the grill-me template sets it (case 544.2). The Spec keeps its form — the blockquotes in {{documentation_lang}}, the `then` and `tasks` blocks — and the hook of `rule-spec-write` reads the chat form: a task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block, its sub-points its keys — `old` and `new` in pairs, `reword old` and `reword new`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, with as many backticks as the value needs — a value that holds a backtick takes its outer span padded by one space on each side, and the hook refuses one unpadded (case 402) — or a fenced block under the sub-point, its opening fence longer than any fence of the same character inside it (case 444.3); a Case off this form is not written, and the hook says why (cases 159, 387.2).

      ## `when` and `then` are the Criterion

      The Case that creates an Estimate writes its Criterion; the Case that changes a promise names the Estimate by slug and replaces its Criterion whole. The scripts copy the Case's `when` and `then`, verbatim with their operands, as the Estimate's `Criterion` — `When:`, `Then:`; `given` stays in the Case file and in the Spec, so `when` names the trigger and the input it acts on, each thing by its slug or path, and the Estimate reads without the Case (case 378.2) — replacing what stood there and setting the page `pending`, unless the item wrote the Criterion under `sections` itself, which then stands, on an `update` as on a `create` (case 204); no `### case N` block, nothing appended, and nothing removed by a `{supersedes:case N}` — the replaced text stays in the Spec of its session and in History. A Case superseded in its own session leaves the Spec — no heading, no section, no `then` or `tasks` block: the `Stop` hook of `rule-spec-write` removes it from the plan file and, once it stands, `raw/<date>/<hi HHMM>/spec.md` (case 441) — and the superseding Case is written whole; its text is not kept — its ledger lines name its targets, the `context` of the superseding Case says what it replaced — a Frontier line it closed is closed again by the superseding Case, and pre-spec catches a superseded Case still in the plan (case 299.1). Only a replaced Criterion sets `pending`: an `update` of a rule's `Purpose` touches no Estimate, an `update` of its `Render` touches no Estimate of the live reading — that Estimate promises only that the file equals the Render and is loaded; the behaviour a changed paragraph describes is named in the Estimate of that behaviour (case 378.5). One promise per Case or sub-case: a Case that touches two promises is two sub-cases, and pre-spec asks for the split. Nothing is signed twice, and nothing is signed in two wordings (cases 72.1, 188). A `when` on a slash command names the path it covers — the person's typed command on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`, or both; the reading of a `then` that covers both takes both (case 173).

      ## The `then` block lives in the Spec

      Ratifying "create entity-x" without seeing what that page will claim is an empty ratification. The human signs content, not the fact that a decision occurred. The content is a YAML block tagged `then` under the Case in the Spec — the plan the human approves at the end of Plan Mode — not in the chat, where its content stands as sub-points of `tasks` (case 370). A list under each decision type present, one entry per target, `slug` first.

      ```then
      create:
        - slug: entity-cart
          type: entity
          kind: MOC
          purpose: Lets a buyer review an order before paying
          tags: [cart, checkout]
          sections:
            Purpose: |
              Until now items went straight from the catalogue to payment.
        - slug: estimate-cart-renders-in-time
          type: estimate
          ref: entity-cart
          kind: Research
          purpose: Whether the cart renders within 200ms, and what dominates the time if not
          method: measure the render at 10, 50 and 200 line items, against a seeded database
          tags: [cart, performance]
      update:
        - slug: entity-checkout
          set: {tags: [cart, checkout, payment]}
          change: the cart precedes payment
        - slug: estimate-checkout-orders-the-steps
          set: {status: pending}
          change: the Criterion replaced whole — the cart precedes payment
      ```

      A `create` holds the fields the target schema needs a judgment for; prose for a body section goes under `sections`, keyed by the section name. A new promise is an explicit `create` of an Estimate: its own item, `ref` naming the target, its slug written in the Case — `estimate-<target minus its prefix>-<promise>` — with `kind`, `purpose`, `method` and `tags`; its Criterion is the Case's `when` and `then`, lifted by the scripts, or the text the item writes under `sections: Criterion` (cases 188, 194.1). A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate. An `update` holds `set` (fields), `sections` (the whole new text of a section), `replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects; an `old` matches inside one `##` section of the page — a render block is one section with its headings — never in History, a line break matching any whitespace, and hits the page once: an anchor that crosses a section heading never matches, and one that misses or hits twice fails the entry; an `old` that opens with spaces or tabs takes the spaces and tabs before its first word on the page too, so the indent of `new` replaces them, and a `new` that opens with spaces or tabs takes an `old` that opens with them, or pre-spec reports the pair — case 543), `reword` (a list of `{old, new}` pairs replaced as whole words over every live page of `wiki/`, the page of the item being the owner, for a word that changes everywhere — a slug goes through `rename`, case 274.1), `change` (one line for History) and, when the page changes its slug, `rename` (the new slug, the same category prefix; the page moves and every link to it in the live pages follows, `origin`, History and Result kept — case 258.1). An `update` of an Estimate carries `slug`, `set: {status: pending}` and `change`; the scripts replace its Criterion with the Case's `when` and `then`, or keep the text the item wrote under `sections: Criterion` (case 204). An `update` that names a part alone — a field under `set` other than `status`, a `replace` pair, a section other than `Criterion` — carries no `set.status`: the scripts change that part, and the Criterion and the status stand; a part inside the Criterion is refused — a promise changes only whole, by a Criterion replaced whole (case 378.4). A pair under `replace` or `reword` is signed only after the sentence around every match is read whole and what it names there is said, never from the line a grep printed (case 353). A Case that changes the behaviour of an existing page reads the page's `estimates` and gives an `update` to each one whose Criterion speaks of the change — read as the `then` block is written, not at pre-spec; an Estimate whose Criterion speaks of something else is left alone, since naming a spare one replaces a sound Criterion (cases 53.2, 353). One promise per Case or sub-case: two touched promises are two sub-cases, and pre-spec asks for the split. A `delete` holds `impact`, a `defer` a `type` and a `purpose`. `CLAUDE.md`, this file, `orchestration.md` and `ratification.md` are rendered from `rule-claude-md`, `rule-case-protocol`, `rule-orchestration` and `rule-ratification` and change by an `update` of one of them (cases 59.8, 273.1, 595). New tags are declared under `new_tags` with a meaning and a {{chat_lang}} alias, under any Case of the Spec (case 61).

      **The Spec is written as each Case is ratified**, by the `Stop` hook of `rule-spec-write`, after the reply that carries the Case's ledger lines: it copies the Case as `case-guppi` answered it — the answer the check of `rule-case-check` stored, never a showing that differs from it, which is refused (case 437) — into the plan file, outside the repository, and, once `raw/<date>/<hi HHMM>/spec.md` stands, into it too, the ticks of its unchanged task lines kept (case 441). The Case holds `context`, `problem`, `recommend`, `given`, `when`, `then`, the `then` block and a block tagged `tasks` — one `- [ ] <what>` per file to change, test to write, command to run, one-off migration, and one per reading of an Estimate the Case creates or sets `pending`, by its slug. `ratification` stays in the chat (case 544.5); code is Work Mode. Who ticks which line is `orchestration.md`. A render line is `- [ ] `uv run guppi render`: `<file>``, a sprint line `- [ ] `uv run guppi sprint``, a glossary line `- [ ] `uv run guppi glossary`` — the command in the first code span is what the ticker matches (case 235); a line of another form stays debt at Retro (case 279.1).

      Derivable fields — `origin`, `status`, `parent` from `ref`, `children`, `code_ref`, `deferred_by` — are filled mechanically and are not written here. `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.

      **The slug is written in the Case**, and pre-spec checks it. Meaningful, never an index: `entity-cart`, `lesson-hooks-sessionstart-cannot-block`. The page's category comes from its prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`. Decision pages are the one exception: `decision-case-<N>`, one per Case, written by the script.

      ## Who builds a Case

      Every Case, in Plan Mode and in Work Mode, at its first showing and at every showing again, is built by the agent `case-guppi` (`rule-case-build`); how the main agent dispatches it, passes on the person's words and shows its answer is `orchestration.md`.

      ## Taking up a deferred decision

      A deferred decision is written by the main agent in the short form that `orchestration.md` sets. Taking a deferred decision up means building its full Case from its page — `context` and `problem` as they stand, then `recommend`, `given` — the frame — `when`, `then`, the vault's answer in `context` (case 378.1) — and writing on one of its decision lines one `{supersedes:case N}` block for each Case in the page's `deferred_by`, so that every defer of the page is retired (case 429); the Case, or the sub-case, that carries the blocks also names the page on a decision line other than a `defer` — an `update` with only `change` when nothing on the page changes — since `generate` clears a defer only from the pages the superseding Case names. `/pre-spec` reports a Case that closes a Frontier line of the source `backlog` when no Case among it and its sub-cases both names the page and carries each block; the check of the answer of `case-guppi` sends back a Case that names the page of an open `backlog` line when no Case among it and its sub-cases in the answer both names the page and carries each block (case 467).

      ## Splitting

      If the human's reply to a Case is a follow-up question, the Case was not atomic. Detect this and propose splitting into sub-cases — recursive dotted ids, `1.1`, `1.1.1`; whether a unit splits is the rule of atomicity in `ratification.md`. A sub-case is `### Case N.M — name` under its parent, with its own `when`, `then`, `tasks` and `ratification` (case 159), and its own `given` unless it is the parent's word for word — `materialize` takes a sub-case's `given` as it stands, so a sub-case with the parent's lines and more writes them all out, never a pointer to the parent's; `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing `context` or `given` there (case 60); `problem` stands on the parent only, and the parent's `recommend` may carry every item, and a sub-case may carry its own `recommend` with items whose answer changed that sub-case alone (cases 544.2, 568). A Case with sub-cases stands in one file: the parent's `context`, `problem`, `recommend`, then every sub-case whole (case 355.2).

      A question that only asks you to justify a choice already on the table ("why this approach?") does **not** split the Case. A question whose answer requires a new choice with its own consequences ("how will we handle X?") **does**.

      ## Slug collisions

      Pre-spec checks the slug when the Case is formed. If it is nonetheless taken by generation time — a second decision in the same session claimed it, or a page was created by hand — **the generation script errors rather than renaming.**

      Silently producing `entity-cart-2` would put a name in the vault that nobody ratified, and break the correspondence between a decision and its page. The librarian runs the script, so the librarian sees the error and judges what to do.

      ## Not schema-governed

      `brief.md`, `sprint.md`, `tags.md` and `log.md` are not pages and have no schema. Lint must not check them against the page template.
      <!-- /rule-case-protocol -->
  change: the Render keeps the form of a Case alone; the main agent's part moves to rule-orchestration, the one rule, the ledger lines, atomicity and the harness to rule-ratification; the file is read by case-guppi and no longer loaded by /hi; the purpose names what this rule alone prevents (case 595.6)
- slug: estimate-case-protocol-loaded
  set:
    status: pending
    purpose: The form of a Case stands in one text, the Render of rule-case-protocol, which /hi does not load and the main agent does not read, with nothing of orchestration.md or ratification.md repeated in it and nothing of it repeated in CLAUDE.md
    method: uv run guppi render --check; by hand after the librarian's render, case-schema.md, orchestration.md and ratification.md compared paragraph by paragraph, and at the first /hi of a later session the first turn's context and the main agent's read calls in the transcript
  change: the Criterion replaced whole - the file holds the form of a Case alone and is not loaded by /hi (case 595.6)
````

```tasks
- [ ] update `rule-case-protocol`
- [ ] update `estimate-case-protocol-loaded`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-loaded`
```

### Case 595.7 — `case-guppi` reads `ratification.md` with `case-schema.md`

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the agent file rendered from it
> **＋** `vault/wiki/case-schema.md`, `vault/wiki/ratification.md` — the files it reads before it answers
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill loaded by its `skills` field
> **＋** `.claude/agents/ask-guppi.md` — the vault query it runs before a `create` without a `ref`
> **＋** `.claude/settings.json` — the hooks it reads for a Case that changes a hook
> **＋** `rule-case-check` — the hook that checks and stores its answer
> **＋** `rule-orchestration` — the rule of the showing, named in the Purpose of `rule-case-build`
> **＋** `estimate-case-build-writes-the-case` — its check; its Criterion is replaced

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification`, and nothing else.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round.
> **－** It writes no file and no ledger line.

```then
update:
- slug: rule-case-build
  replace:
  - old: 'Read `vault/wiki/case-schema.md` whole first: it is the form, the language and the operands of your answer.'
    new: 'Read `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole first: the first is the form, the language and the operands of your answer, the second the one rule and the form of the ledger lines of its `ratification`.'
  - old: reads `vault/wiki/case-schema.md`, runs the vault query
    new: reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md`, runs the vault query
  - old: with a short Russian text ([[rule-case-protocol]])
    new: with a short Russian text ([[rule-orchestration]])
  change: case-guppi reads ratification.md with case-schema.md; the showing is rule-orchestration (case 595.7)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  change: the Criterion replaced whole - case-guppi reads case-schema.md and ratification.md (case 595.7)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-writes-the-case`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-the-case`
```

### Case 595.8 — The check of the acknowledging reply moves to `rule-orchestration`

> **given:**
> `estimate-case-protocol-acknowledging-reply` — the check, renamed `estimate-orchestration-acknowledging-reply` and moved to `rule-orchestration`
> **＋** `rule-orchestration`, `vault/wiki/orchestration.md` — its new rule and the file that now sets the reply
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier the reply shows
> **＋** `rule-ledger-write` — the ledger hook
> **＋** `rule-prespec-onward` — the hook that sends the agent on when no `## Cases` line is open

> **when:**
> The person ratifies a Case, or ratifies again a Case shown again after its ratification, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply; when none is open, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names the ids, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written.

```then
update:
- slug: estimate-case-protocol-acknowledging-reply
  rename: estimate-orchestration-acknowledging-reply
  set:
    status: pending
    target: '[[rule-orchestration]]'
  change: moved to rule-orchestration; the Criterion replaced whole - the reply as orchestration.md sets it (case 595.8)
```

```tasks
- [ ] update `estimate-case-protocol-acknowledging-reply`
- [ ] read `estimate-orchestration-acknowledging-reply`
```

### Case 595.9 — The check of the Frontier after a closed line moves to `rule-orchestration`

> **given:**
> `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — the check, renamed `estimate-orchestration-shows-the-frontier-after-a-closed-line` and moved to `rule-orchestration`
> **＋** `rule-orchestration`, `vault/wiki/orchestration.md` — its new rule and the file that now sets the reply
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier the reply shows
> **＋** `estimate-orchestration-acknowledging-reply` — the check whose form of the Frontier this one follows
> **＋** `rule-skill-hi` — sets the first reply of `/hi`
> **＋** `rule-prespec-onward` — the hook that sends the agent on
> **＋** `/pre-spec` — the skill the reply calls when no `## Cases` line is open

> **when:**
> After the first reply of `/hi` and before the end of Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

> **then:**
> The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-orchestration-acknowledging-reply` sets.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as they are closed.
> **＋** The open `W` lines are folded into one line that lists their ids.
> **＋** Each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open, no question follows the Frontier: a reply with no `LEDGER` block calls `/pre-spec` after it, and a reply with a `LEDGER` block ends with the Frontier, for the hook of `rule-prespec-onward` to send the agent on.
> **＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
> **－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
> **－** A line closed in Work Mode or at Retro shows no Frontier.
> **－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-orchestration-acknowledging-reply` sets it.

```then
update:
- slug: estimate-case-protocol-shows-the-frontier-after-a-closed-line
  rename: estimate-orchestration-shows-the-frontier-after-a-closed-line
  set:
    status: pending
    target: '[[rule-orchestration]]'
  change: moved to rule-orchestration; the Criterion replaced whole - the reply as orchestration.md sets it (case 595.9)
```

```tasks
- [ ] update `estimate-case-protocol-shows-the-frontier-after-a-closed-line`
- [ ] read `estimate-orchestration-shows-the-frontier-after-a-closed-line`
```

### Case 595.10 — The check of the defer in one reply moves to `rule-orchestration`

> **given:**
> `estimate-case-protocol-defers-in-one-reply` — the check, renamed `estimate-orchestration-defers-in-one-reply` and moved to `rule-orchestration`
> **＋** `rule-orchestration`, `vault/wiki/orchestration.md` — its new rule and the file that now sets the short form
> **＋** `rule-spec-write` — the `Stop` hook that writes the short Case into the plan file
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier the reply shows
> **＋** `rule-prespec-onward` — the hook that sends the agent on
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — where Retro puts what it would put off

> **when:**
> The person asks in the chat to defer an item in Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows the question, or the Frontier when no question stands.
> **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.

```then
update:
- slug: estimate-case-protocol-defers-in-one-reply
  rename: estimate-orchestration-defers-in-one-reply
  set:
    status: pending
    target: '[[rule-orchestration]]'
  change: moved to rule-orchestration; the Criterion replaced whole - the short form as orchestration.md sets it (case 595.10)
```

```tasks
- [ ] update `estimate-case-protocol-defers-in-one-reply`
- [ ] read `estimate-orchestration-defers-in-one-reply`
```

### Case 595.11 — The check of the showing of a built Case moves to `rule-orchestration`

> **given:**
> `estimate-case-protocol-shows-the-built-case` — the check, renamed `estimate-orchestration-shows-the-built-case` and moved to `rule-orchestration`
> **＋** `rule-orchestration`, `vault/wiki/orchestration.md` — its new rule and the file that now sets the showing
> **＋** `case-guppi`, `ask-guppi` — the agents the main agent dispatches
> **＋** `.claude/skills/wait-what/SKILL.md` — the skill of a plain explanation
> **＋** `.claude/skills/grill-me/SKILL.md` — the shape of a round
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a built Case
> **＋** `rule-case-check` — the hook that writes the file and checks the showing

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer. In the same reply it writes the heading of the top-level Case with its name in Russian and, under it, one list with an item per Case and sub-case of the answer: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the Case creates or whose Criterion it replaces, or from the Estimate its `context` names as already checking the change. Then it writes one `ratification` with the ledger lines of every Case of the list as the answer holds them, and its own text after one horizontal rule. An answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it; a reply that shows a round and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: estimate-case-protocol-shows-the-built-case
  rename: estimate-orchestration-shows-the-built-case
  set:
    status: pending
    target: '[[rule-orchestration]]'
  change: moved to rule-orchestration; the Criterion replaced whole - the showing as orchestration.md sets it (case 595.11)
```

```tasks
- [ ] update `estimate-case-protocol-shows-the-built-case`
- [ ] read `estimate-orchestration-shows-the-built-case`
```

### Case 595.12 — The check of a forwarded discussion question moves to `rule-orchestration`

> **given:**
> `estimate-case-protocol-forwards-a-discussion-question` — the check, renamed `estimate-orchestration-forwards-a-discussion-question` and moved to `rule-orchestration`
> **＋** `rule-orchestration`, `vault/wiki/orchestration.md` — its new rule and the file that now sets the forwarding
> **＋** `case-guppi` — the agent the question goes to
> **＋** `.claude/skills/wait-what/SKILL.md` — the skill of a plain explanation
> **＋** `rule-case-check` — the hook that reads a `**Fact:**` answer as no Case

> **when:**
> In Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to discuss an item whose `case-guppi` is building its Case or has shown it, or to learn something of that item, and the question is no request for a plain explanation of the agent's text.

> **then:**
> The main agent sends the question to that `case-guppi` by `SendMessage`, verbatim and untranslated, and makes no `Read`, `Grep` or `Glob` call of its own to answer it.
> **＋** `case-guppi` answers in plain words under a first line `**Fact:**`, with no Case heading and no round, from the pages it read, or with a round when the question opens a fork.
> **＋** The main agent shows the answer translated into Russian, then asks again the question that stood open: the open question of the round, or the sign-off of the shown Case.
> **－** A request for a plain explanation of a round, of the short text on a Case or of a reply stays with `.claude/skills/wait-what/SKILL.md`.
> **－** A `**Fact:**` answer changes nothing of the round or of the Case, and the hook of `rule-case-check` reads it as no Case.

```then
update:
- slug: estimate-case-protocol-forwards-a-discussion-question
  rename: estimate-orchestration-forwards-a-discussion-question
  set:
    status: pending
    target: '[[rule-orchestration]]'
  change: moved to rule-orchestration; the Criterion replaced whole - the forwarding as orchestration.md sets it (case 595.12)
```

```tasks
- [ ] update `estimate-case-protocol-forwards-a-discussion-question`
- [ ] read `estimate-orchestration-forwards-a-discussion-question`
```

### Case 595.13 — The check of the main agent's own questions moves to `rule-orchestration`

> **given:**
> `estimate-case-protocol-asks-in-the-grill-me-shape` — the check, renamed `estimate-orchestration-asks-in-the-grill-me-shape` and moved to `rule-orchestration`
> **＋** `rule-orchestration`, `vault/wiki/orchestration.md` — its new rule and the file that now sets the question shape
> **＋** `.claude/skills/grill-me/SKILL.md` — the question shape
> **＋** `case-guppi` — whose rounds are not the main agent's own questions
> **＋** `/pre-spec`, `/hi` — the moments of the main agent's own questions, with a stop of Work Mode
> **＋** `/work`, `/carry` — the choice after the Spec is written
> **＋** `rule-spec-capture` — sets that choice

> **when:**
> The main agent puts a question to the person itself, outside a round of `case-guppi`: a decision it needs in the report of `/pre-spec`, a question at `/hi`, or a question at a stop of Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
> **＋** It stands in Russian, and its labels may stand translated.
> **－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.

```then
update:
- slug: estimate-case-protocol-asks-in-the-grill-me-shape
  rename: estimate-orchestration-asks-in-the-grill-me-shape
  set:
    status: pending
    target: '[[rule-orchestration]]'
  change: moved to rule-orchestration; the Criterion replaced whole - the question shape as orchestration.md sets it (case 595.13)
```

```tasks
- [ ] update `estimate-case-protocol-asks-in-the-grill-me-shape`
- [ ] read `estimate-orchestration-asks-in-the-grill-me-shape`
```

### Case 595.14 — The check of the harness before Plan Mode moves to `rule-orchestration`

> **given:**
> `estimate-case-protocol-puts-the-harness-before-plan-mode` — the check, renamed `estimate-orchestration-puts-the-harness-before-plan-mode` and moved to `rule-orchestration`
> **＋** `rule-orchestration`, `vault/wiki/orchestration.md` — its new rule and the file that now sets the order
> **＋** `case-guppi`, `ask-guppi` — the agents of Plan Mode
> **＋** `/hi`, `/pre-spec`, `ExitPlanMode` — the moments the check reads
> **＋** `/work`, `/carry` — the choice after the Spec is written
> **＋** `rule-spec-capture` — sets the picker for that choice

> **when:**
> A working session opened by `/hi` runs in Plan Mode, the Plan Mode instructions of Claude Code stand in the main agent's context, and `vault/wiki/orchestration.md` is rendered from `rule-orchestration`.

> **then:**
> The main agent launches no Explore or Plan agent: `case-guppi` builds each Case, and `ask-guppi` asks the vault at `/pre-spec`.
> **＋** It asks the person by a plain question in the chat and calls no picker tool while Plan Mode lasts.
> **＋** It calls `ExitPlanMode` only after `/pre-spec` has run.
> **－** The choice between `/work` and `/carry` after the Spec is written stays a picker, as `rule-spec-capture` sets it.

```then
update:
- slug: estimate-case-protocol-puts-the-harness-before-plan-mode
  rename: estimate-orchestration-puts-the-harness-before-plan-mode
  set:
    status: pending
    target: '[[rule-orchestration]]'
  change: moved to rule-orchestration; the Criterion replaced whole - the order as orchestration.md sets it (case 595.14)
```

```tasks
- [ ] update `estimate-case-protocol-puts-the-harness-before-plan-mode`
- [ ] read `estimate-orchestration-puts-the-harness-before-plan-mode`
```

### Case 595.15 — The check of related Cases in the dispatch moves to `rule-orchestration`

> **given:**
> `estimate-case-protocol-names-related-cases-in-the-dispatch` — the check, renamed `estimate-orchestration-names-related-cases-in-the-dispatch` and moved to `rule-orchestration`
> **＋** `rule-orchestration`, `vault/wiki/orchestration.md` — its new rule and the file that now sets the dispatch
> **＋** `case-guppi` — the agent dispatched
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the case file a related Case is named by

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of a Frontier item, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names and acts at another moment need not stand in the prompt.
> **－** When no Case of the session is related, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

```then
update:
- slug: estimate-case-protocol-names-related-cases-in-the-dispatch
  rename: estimate-orchestration-names-related-cases-in-the-dispatch
  set:
    status: pending
    target: '[[rule-orchestration]]'
  change: moved to rule-orchestration; the Criterion replaced whole - the dispatch as orchestration.md sets it (case 595.15)
```

```tasks
- [ ] update `estimate-case-protocol-names-related-cases-in-the-dispatch`
- [ ] read `estimate-orchestration-names-related-cases-in-the-dispatch`
```

### Case 595.16 — The check of the ledger line form moves to `rule-ratification`

> **given:**
> `estimate-case-protocol-ledger-line-form` — the check, renamed `estimate-ratification-ledger-line-form` and moved to `rule-ratification`
> **＋** `rule-ratification`, `vault/wiki/ratification.md` — its new rule and the file that now holds the form of the lines

> **when:**
> The agent writes the ledger lines of a session — the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists — with `vault/wiki/ratification.md` rendered from `rule-ratification`.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
> **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **－** A lesson whose fix is ratified in another session gets no mark.

```then
update:
- slug: estimate-case-protocol-ledger-line-form
  rename: estimate-ratification-ledger-line-form
  set:
    status: pending
    target: '[[rule-ratification]]'
  change: moved to rule-ratification; the Criterion replaced whole - the form as ratification.md holds it (case 595.16)
```

```tasks
- [ ] update `estimate-case-protocol-ledger-line-form`
- [ ] read `estimate-ratification-ledger-line-form`
```

### Case 595.17 — The ledger hook's refusal names `ratification.md`

> **given:**
> `rule-ledger-write` — the rule of the ledger hook; its Purpose names where the instruction lives
> **＋** `guppi/ledger.py` — the hook `uv run guppi ledger`; its refusal message names the file of the table
> **＋** `tests/test_ledger.py` — the tests that assert the message
> **＋** `guppi/prespec.py` — a comment that names the file of the line form
> **＋** `guppi/materialize.py` — `parse_line`, the grammar of a ledger line
> **＋** `vault/wiki/ratification.md` — the file that now holds the table
> **＋** `estimate-ledger-write-lifts` — sets how often the message is told
> **＋** `estimate-ledger-write-refuses-a-line-it-cannot-read` — the check of the refusal; its Criterion is replaced

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh line `- decision[`, `- estimate[` or `- lesson[` in a `LEDGER` block of the session, and `parse_line` of `guppi/materialize.py` returns None for it.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: line not written — the grammar of a ledger line does not read it: <line>. Write it again in the form of the table in ratification.md."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A refused line gets no other refusal of the hook and no other stderr line.
> **－** A line already in the ledger of any session is not judged again.
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

```then
update:
- slug: rule-ledger-write
  replace:
  - old: lives in `case-schema.md`, the Render of `rule-case-protocol` that `/hi` loads (case 273),
    new: lives in `ratification.md` and `orchestration.md`, the Renders of `rule-ratification` and `rule-orchestration` that `/hi` loads (cases 273, 595),
  change: the instruction to write the ledger lines lives in ratification.md and orchestration.md (case 595.17)
- slug: estimate-ledger-write-refuses-a-line-it-cannot-read
  set:
    status: pending
  change: the Criterion replaced whole - the refusal names the table in ratification.md (case 595.17)
```

```tasks
- [ ] update `rule-ledger-write`
- [ ] update `estimate-ledger-write-refuses-a-line-it-cannot-read`
- [x] `guppi/ledger.py`: the refusal message names `ratification.md` in place of `case-schema.md`
- [x] `tests/test_ledger.py`: the asserted message names `ratification.md`
- [x] `guppi/prespec.py`: the comment on the line form names `ratification.md`
- [x] `uv run pytest tests/test_ledger.py`
- [ ] read `estimate-ledger-write-refuses-a-line-it-cannot-read`
```

### Case 595.18 — The check of the fork after the Spec names `ratification.md`

> **given:**
> `estimate-spec-capture-offers-the-fork` — the check of the line after the Spec is written; one of its lines names the file that says a Case is ratified by a reply; its Criterion is replaced
> **＋** `rule-spec-capture` — the rule of the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the Spec the hook writes or finds
> **＋** `vault/raw/` — the folder of the sessions, where a conserved Spec stands
> **＋** `/hi` — the opening of the session, without which the hook exits 2
> **＋** `/work`, `/carry` — the two options of the fork
> **＋** `guppi/materialize.py` — `is_carried_over`, which judges a Spec marked by `carry.md`
> **＋** `.claude/skills/box/SKILL.md`, `.claude/skills/work/SKILL.md`, `.claude/skills/carry/SKILL.md` — the skills the line sends the agent to
> **＋** `vault/wiki/ratification.md` — the file that now says a Case is ratified by the person's reply, never by a picker tool
> **＋** `estimate-spec-capture-appends` — the check of the writing of the Spec

> **when:**
> `guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec, or found it already there.

> **then:**
> The stdout of the hook is one JSON object, `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, that holds one line with the session folder and the Spec file `raw/<hi date>/<hi HHMM>/spec.md`.
> **＋** For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
> **＋** The agent sees this line in the `ExitPlanMode` result.
> **＋** When the approved plan names the `spec.md` of a folder under `vault/raw/` that `is_carried_over` of `guppi/materialize.py` judges marked by `carry.md`, the line names that folder and tells the agent to call `.claude/skills/box/SKILL.md` with it, and to ask the person nothing.
> **＋** For any other plan the line is the fork. The fork line tells the agent to ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (the Spec conserved for a later session), and to start nothing until the person answers.
> **＋** On the answer, the agent calls `.claude/skills/work/SKILL.md` or `.claude/skills/carry/SKILL.md`, the skill of the option picked.
> **－** A `PostToolUse` hook blocks nothing: the tool has run.
> **－** Without a Spec, nothing, as before.
> **－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.
> **－** A Case is still ratified by the person's reply in the chat, never by a picker tool, as `vault/wiki/ratification.md` says: the picker is for the end of the session only.
> **－** The writing of the Spec does not change: that is the promise of `estimate-spec-capture-appends`.

```then
update:
- slug: estimate-spec-capture-offers-the-fork
  set:
    status: pending
  change: the Criterion replaced whole - ratification.md says a Case is ratified by the person's reply (case 595.18)
```

```tasks
- [ ] update `estimate-spec-capture-offers-the-fork`
- [ ] read `estimate-spec-capture-offers-the-fork`
```

### Case 595.19 — The check of grill-me names `rule-orchestration` for the showing of a round

> **given:**
> `estimate-skill-grill-me-asks-in-rounds` — the check of the skill grill-me; one of its lines names the rule by which the main agent shows a round; its Criterion is replaced
> **＋** `rule-skill-grill-me` — the rule whose Render is the skill
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill
> **＋** `rule-orchestration` — the rule that now sets how the main agent shows a round
> **＋** `uv run guppi render` — the renderer and its `--check`

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer, together with the lines of a list under it. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
> **＋** The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark `🔹` and its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
> **＋** A list stands one item per line, never inside a sentence. This covers items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things. Under an `**After:**` item a list stands nested inside that item.
> **＋** A quotation, words taken from a page, a file or a reply, stands as a blockquote on its own line under the sentence that introduces it and names its source, a fragment of a few words too; it never stands inside a sentence in quote marks. Under an `**After:**` item it stands indented to the text of the item, inside that item, and is no second item.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
> **－** A short series of words inside a sentence stays in the sentence.
> **－** No line of a question except an option starts with `🔹`.
> **－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `rule-orchestration`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
> **－** The `**Context:**` paragraph of a round of `case-guppi`, its lists and quotations included, and the place of its case numbers are not read here. They are the promises of the Estimates of the rule of `.claude/agents/case-guppi.md`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

```then
update:
- slug: estimate-skill-grill-me-asks-in-rounds
  set:
    status: pending
  change: the Criterion replaced whole - the main agent shows a round by rule-orchestration (case 595.19)
```

```tasks
- [ ] update `estimate-skill-grill-me-asks-in-rounds`
- [ ] read `estimate-skill-grill-me-asks-in-rounds`
```

### Case 595.20 — The glossary points the moved terms to their new rules

> **given:**
> `entity-glossary` — the page of the terms; rows whose meaning moved change their `where` or their wording
> **＋** `vault/wiki/glossary.md` — the file `uv run guppi glossary` writes from it
> **＋** `rule-glossary` — the rule of that file
> **＋** `rule-ratification`, `rule-orchestration`, `rule-case-protocol` — the pages the rows point to
> **＋** `/hi` — the command whose loading the row of `case-schema.md` describes
> **＋** `estimate-glossary-terms-defined` — the check that each row's `where` page says what its term is; its Criterion stands

> **when:**
> `uv run guppi glossary` writes `vault/wiki/glossary.md` from `entity-glossary`, and a reader follows a row to its `where` page.

> **then:**
> The rows Ratification, Contract vs implementation and Main agent, Subagent name `[[rule-ratification]]` in `where`, and the row Plan Mode names `[[rule-orchestration]]`.
> **＋** The row Case keeps `[[rule-case-protocol]]` and says that its sub-cases are each ratified on their own as `rule-ratification` sets.
> **＋** The row of `CLAUDE.md` and `case-schema.md` says that `/hi` loads `orchestration.md` and `ratification.md` and that `case-schema.md` reaches `case-guppi` alone.
> **＋** Each row names in `where` a page that says what its term is.

```then
update:
- slug: entity-glossary
  replace:
  - old: '| Ratification | Human sign-off on a Decision; nothing in vault or code changes without one | [[rule-case-protocol]] |'
    new: '| Ratification | Human sign-off on a Decision; nothing in vault or code changes without one | [[rule-ratification]] |'
  - old: '| Contract vs implementation | A Decision fixes what "done" means, never how; a contract change is a new Case | [[rule-case-protocol]] |'
    new: '| Contract vs implementation | A Decision fixes what "done" means, never how; a contract change is a new Case | [[rule-ratification]] |'
  - old: executes plan tasks, never decides, a fork returns | [[rule-case-protocol]] |
    new: executes plan tasks, never decides, a fork returns | [[rule-ratification]] |
  - old: (cases 356.1, 356.2, 421.4, 451.1) | [[rule-case-protocol]] |
    new: (cases 356.1, 356.2, 421.4, 451.1) | [[rule-orchestration]] |
  - old: splits into dotted sub-cases the parent's sign-off never covers | [[rule-case-protocol]] |
    new: splits into dotted sub-cases, each ratified on its own as `rule-ratification` sets | [[rule-case-protocol]] |
  - old: the Case schema is the Render of `rule-case-protocol`, opened by the one rule, and it arrives with `/hi` together with the glossary (cases 273, 288)
    new: the Case schema is the Render of `rule-case-protocol`, read by `case-guppi` alone; `/hi` loads, together with the glossary, `orchestration.md`, the Render of `rule-orchestration`, and `ratification.md`, the Render of `rule-ratification`, which the one rule opens (cases 273, 288, 595)
  change: the rows Ratification, Contract vs implementation, Main agent and Plan Mode point to rule-ratification and rule-orchestration; the row Case says each sub-case is ratified on its own; the row of case-schema.md says what /hi loads (case 595.20)
```

```tasks
- [ ] update `entity-glossary`
- [ ] `uv run guppi glossary`
```

### Case 595.21 — The check of `CLAUDE.md` places the one rule in `ratification.md`

> **given:**
> `estimate-claude-md-rendered` — the check of `CLAUDE.md`; one of its lines says where the one rule stands; its Criterion is replaced
> **＋** `rule-claude-md` — the rule whose Render is `CLAUDE.md`
> **＋** `CLAUDE.md` — the system prompt every session and subagent loads
> **＋** `rule-language`, `rule-agent-writing`, `rule-one-judgment-one-implementation` — its children, in their markers
> **＋** `rule-governed-files-hook` — the hook that refuses a hand edit of the file
> **＋** `guppi render` — the renderer and its `render --check`
> **＋** `vault/`, `vault/wiki/glossary.md`, `/hi`, `index.md` — the folder, the path, the skill and the old page the Criterion names
> **＋** `vault/wiki/ratification.md` — the file that now holds the one rule

> **when:**
> `guppi render` writes `CLAUDE.md` from `rule-claude-md` and its children, and a session or a subagent starts and loads the file.

> **then:**
> `CLAUDE.md` is: `# GUPPI`; one paragraph, "A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. The vault is vault/; its terms are vault/wiki/glossary.md. A working session opens with /hi.", whose words the file holds with the folder, the path and the skill in code spans; then the text of `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers.
> **＋** `render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
> **＋** Every session and every subagent loads this text.
> **－** No `@` import, no "What is loaded here", no paragraph on `index.md`, no "Migration mode", no "Commands", no one rule and no sentence on memory — the one rule is in `vault/wiki/ratification.md`; the `children` of `rule-claude-md` are `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation`.

```then
update:
- slug: estimate-claude-md-rendered
  set:
    status: pending
  change: the Criterion replaced whole - the one rule is in ratification.md (case 595.21)
```

```tasks
- [ ] update `estimate-claude-md-rendered`
- [ ] read `estimate-claude-md-rendered`
```
