## Case 788 — A Case id carries its sprint, and a sprint id is unique

> **context:**
> A Case id is one number that grows across all sessions, with a dot for each sub-case level. It names the Decision page `decisions/decision-case-<N>.md` written by `guppi/generate.py`, the Case file `cases/case-<N>.md`, and a later Case points back at it by `{supersedes:case N}`. The person plans a public repository where others run their own sprints on their own branches and send them to `main` by pull request. Two branches cut from the same `main` would both write a Case 786, so their pull requests would bring two different `decision-case-786` pages and a mark that can point at either. The person chose an id made of the sprint id, a hyphen and a number that starts again at 1 in each sprint, such as `kir-plugin-12.1`. The sprint id starts with its author's GitHub name, and the main agent asks for it before it dispatches the opening Case, which is `<id>-1`. The ledger hook refuses a sprint id whose page `has_page` finds live or archived, and does not check the name. The existing ids stay plain, every reader takes both forms for good, and the sprints `migration` and `plugin`, opened before this Case, keep plain ids to their close. One function counts the next free id from the Decision pages, the session's ledger, the store `<plan>.checked.json` and the session's Case files. The command `guppi caseid --next` holds the id it prints in that store, so that Cases dispatched together never share an id. The check of a Case built again uses the same function.
>
> The Case was ratified in two parts, then built again on the findings of `/pre-spec`, which the person accepted. The person then chose seven parts, one check each. The parts keep their ratified numbers, because a part that loses an item of its decision lines would need a new number. So 788.1 is the refusal of a taken sprint id, 788.2 the id form, its readers, the command and the dispatch, 788.3 the sprint id asked first, 788.4 the count of the next id, 788.5 `/box`, 788.6 the guard of a Case file, and 788.7 the check of an id that another agent holds. 788.1 keeps its update of `rule-skill-sprint-open` for the sentence on the refusal, and 788.3 updates the same page for the question before the dispatch, on other anchors. The Decision page of a new-form id is written by `guppi generate` only at a librarian's run in a later sprint, and no test of this session runs it, so 788.2 says nothing of that page beyond the Render of `rule-decisions-schema`.
>
> The readers that take only a plain id today come from a Grep for `isdigit\(\)|\(\\d\+\)|\[\\w\.\]` over `guppi/`. It printed `guppi/lint.py`, `guppi/gate.py`, `guppi/casecheck.py` and `guppi/box.py`. I read each such function whole. `case_key` of `guppi/gate.py` reads a part that is not a number as 0. `case_number` and `new_number` of `guppi/casecheck.py` take digits only, and `held_number` of `guppi/ratified.py` calls both. `DECISION_LINK`, `history_cases` and `spec_items` of `guppi/box.py` take digits only. `ORIGIN_CASE` and `DEFERRED_LINE` of `guppi/lint.py` take no hyphen. `top_case` of `guppi/casecheck.py`, `ancestors` of `guppi/ratified.py`, and `parse_line` and `_case_of` of `guppi/materialize.py` already read the new form, because a sprint id holds no dot. So the readers agree on a plain id and part on the new form, and 788.2 moves the grammar into `guppi/caseid.py`, which they all import, with a test that runs each of them over both forms, as `rule-one-judgment-one-implementation` and case 785 set it. `new_number` counts the ledger and the store, and the command was to count the Decision pages and the ledger: the two sides parted, so 788.4 puts the count into one function `next_id` of `guppi/caseid.py`, which both call. For the taken sprint id, a Grep for `entity-sprint` over `guppi/` printed `guppi/prespec.py`, `guppi/materialize.py`, `guppi/generate.py`, `guppi/ledger.py`, `guppi/lint.py`, `guppi/backlog.py`, `guppi/sprint_close.py` and `guppi/sprint.py`. I read whole `has_page` of `guppi/materialize.py`, `archived_sprint_pages` of `guppi/backlog.py`, the collision check of a `create` in `guppi/generate.py` and `is_sprint_page` of `guppi/ledger.py`. `has_page` finds a page live or in its category folder under `vault/archive/` outside `raw/`, and reads no frontmatter. `archived_sprint_pages` also finds a folder `entities/` under `raw/` and drops a page whose frontmatter fails to read. The check in `generate` sees only the live page. The person chose `has_page` where they part, so 788.1 imports it, with `is_sprint_page`. The check in `generate` keeps its own question, because the ledger hook refuses an archived id before `generate` runs.
>
> In `rule-ratification`, read whole, the sentence on the form of the id is the one sentence that says what an id is, and 788.2 extends it. The table keeps `case 12` as an example of the plain form. In `rule-decisions-schema`, read whole, the slug sentence and the field `case` give only plain examples, and they gain one of the new form. In `rule-orchestration`, read whole, only the sentence on the dispatch names where the Case id comes from. The Criteria of `estimate-orchestration-shows-the-built-case` and `estimate-orchestration-names-related-cases-in-the-dispatch` name the Case id in the prompt, not where it comes from, so both stand. In `rule-skill-sprint-open`, read whole, step 2 and its list ask the sprint id in the rounds of the opening Case, and step 5 says that `case-guppi` puts each answer to the person. 788.3 changes both, and the Criterion of `estimate-skill-sprint-open-asks-the-opening-questions`, which states them, is replaced whole. Its line on the close line is kept word for word, because Case 789.1 relies on it. Case 789 of this session changes steps 3 and 4 of the same Render. I read its file, and its anchors and mine do not overlap. Its new step 4 tells the owner from an author by the GitHub login, which fits the GitHub name that starts the sprint id. In the Purpose of `rule-ledger-write`, the sentence on the refusal while no sprint is open stays true, because a refused `create` opens no sprint. The Estimates of `rule-ledger-write` speak of other refusals, and `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` names the refusal while no sprint is open, which stays true. `estimate-ratification-ledger-line-form`, `estimate-ratification-loaded` and `estimate-decisions-schema-checked` stand, since the id stays `case N` and the files keep their lists and sections. A Grep for `gives no number|whole part|free number|new number` over `vault/wiki/`, `log.md` left out, printed 16 files. In them, "number" names the id of a Case, and with the new form the part that is counted is still a number. Four of them are changed by this Case: `estimate-spec-box-refuses-a-stale-spec` by 788.5, `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds` by 788.6, `estimate-case-check-sends-back-a-case-number-held-by-another-agent` by 788.7, and `estimate-case-check-sends-back-a-ratified-case-in-another-shape` by 788.4. The rest stand. `rule-case-build` and `estimate-case-build-writes-the-case` count a new Case beside a ratified one from the Case files and the ledger, and name the free number of the guard as the fallback, which still holds when the store holds a higher id. A Grep for `ROOT / "(vault|\.claude)"|REPO / "vault"|"\.claude" / "skills"` over `tests/` printed `tests/test_generate.py`, `tests/test_schemas.py`, `tests/test_recall.py`, `tests/test_orchestration.py`, `tests/test_guard.py` and `tests/test_case_schema.py`. `tests/test_recall.py` and `tests/test_guard.py` write under a temp folder. `tests/test_generate.py` writes its own decisions schema. `tests/test_schemas.py` reads the lists of the live schemas, which do not change. `tests/test_orchestration.py` and `tests/test_case_schema.py` run the checks over the examples of `orchestration.md` and `case-example.md`, whose ids `7` and `1` keep the plain form. So all six stand. The two new Estimates have free slugs: a Glob `vault/**/estimate-*{taken-sprint-id,case-id}*.md` printed nothing. Their tags stand in `vault/wiki/tags.md`. No part drops a section of a page. In the four Criteria that 788.3, 788.4, 788.6 and 788.7 replace, the lines that are not carried word for word are changed on purpose: the word number becomes id, the sources of the count are named, and the id asked first is stated. The lines are not dropped. The lines of 788.4, 788.5, 788.6 and 788.7 that share words with another part state the same steps of different hooks, the check of a Case file, `/box` and the guard. They are not one promise signed twice.

> **problem:**
> A Case id is one global number, so two people who run sprints on parallel branches write the same ids, and their pull requests clash on Decision pages, Case files and `{supersedes:case N}` marks.

> **recommend:**
> - **What should a Case id look like when it carries its sprint?**
>   - Recommended: (a) the sprint id, a hyphen, then the number, such as `plugin-12.1`, one spelling in ledger lines, page names, file names and branch names.
>   - Answer: agreed, (a).
> - **How does a sprint id stay unique when two people open sprints at the same time?**
>   - Recommended: (a) the sprint id starts with its author's GitHub name, such as `kir-plugin`, and the opening Case refuses an id that a live or archived sprint page holds.
>   - Answer: agreed, (a).
> - **What happens to the Case numbers that already exist?**
>   - Recommended: (a) they stay as they are; a plain number means a Case from before sprint ids, and every reader takes both forms for good.
>   - Answer: agreed, (a).
> - **When does the new numbering start?**
>   - Recommended: (a) at the next sprint that `/sprint-open` opens; `plugin` keeps global numbers to its close.
>   - Answer: agreed, (a).
> - **Is this one Case or two?**
>   - Recommended: (a) one Case with two sub-cases: one for `/sprint-open` and its check of the id, one for the id form and every reader of it.
>   - Answer: agreed, (a); later replaced by the answer to the question whether Case 788 should split into more parts.
> - **How does the main agent find the next Case number inside a sprint?**
>   - Recommended: (a) one function in code gives the next number from the Decision pages of the open sprint, live and archived, and the session's ledger; a command prints it, the main agent runs it before it dispatches a new Case, and the check of a Case file uses the same function for a Case built again.
>   - Answer: agreed, (a).
> - **What checks that a new sprint id is unique?**
>   - Recommended: (a) the ledger hook refuses the `create` of a sprint page whose id a live or archived sprint page already holds; `case-guppi` asks for an id that starts with the author's GitHub name, and no code checks the name.
>   - Answer: agreed, (a).
> - **Which checks confirm the two sub-cases?**
>   - Recommended: (a) two new Estimates, each checked by a test: one on `rule-skill-sprint-open` for the ledger hook and a taken or free sprint id, one on `rule-ratification` for each reader of a Case id over both forms; the existing Estimates stay as they are.
>   - Answer: agreed, (a); later changed by the answers on the check of the opening questions and on the split.
> - **Which id does the opening Case of a new sprint take?**
>   - Recommended: (a) the main agent asks the sprint id first, in one plain question before the dispatch; the opening Case is `<id>-1`; the command reads the open sprint from the `create` line of the sprint page in the session's ledger, else from `sprint.md`.
>   - Answer: agreed, (a).
> - **How does the command know that a sprint keeps plain numbers?**
>   - Recommended: (a) a fixed list in `guppi/caseid.py`: `migration` and `plugin` keep plain numbers, and every other sprint takes the new form.
>   - Answer: agreed, (a).
> - **Which judgment says that a sprint id is taken?**
>   - Recommended: (a) the ledger hook calls `has_page`: an id is taken when its page stands live, or archived outside a `raw/` folder, even with a broken header.
>   - Answer: agreed, (a).
> - **Should the check of the opening questions be rewritten now that the main agent asks for the sprint id first?**
>   - Recommended: (a) rewrite `estimate-skill-sprint-open-asks-the-opening-questions` whole: the main agent asks the id first, the prompt gives it to the opening Case `<id>-1`, `case-guppi` asks the rest; read by hand at the Retro of this session.
>   - Answer: agreed, (a).
> - **Should Case 788 split into more parts after the review findings?**
>   - Recommended: (a) seven parts, one check each: the taken sprint id, the id asked first, the id form and its readers, the count of the next id, `/box`, the guard of a Case file, and the check of an id held by another agent.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the findings of `/pre-spec`, with the person's answers: set which id the opening Case takes and how the open sprint is known; count the next id by one function that also sees Cases dispatched but not ratified; judge a taken sprint id by the judgment the code already shares; name the checks of `/box`, of the guard of a Case file and of the check of an id held by another agent; let the test of the new check run what its Criterion states.
>   - Taken: the parts 788.3 to 788.7 hold these fixes. The command holds the id it prints in the store. The test of 788.2 runs `held_number` and the naming of a Case file, and the line on the Decision page of a new-form id left its Criterion.

### Case 788.1 — The ledger hook refuses a sprint id that is already taken

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, whose Purpose gains the refusal.
> **＋** `guppi/ledger.py`: the ledger hook.
> **＋** `guppi/materialize.py`: `has_page`, the one judgment whether a page stands live or archived.
> **＋** `entity-sprint-<id>`, the page `vault/wiki/entities/entity-sprint-<id>.md`: the sprint page whose `create` the hook judges.
> **＋** `rule-skill-sprint-open`: its Render, `.claude/skills/sprint-open/SKILL.md`, says what follows a refusal.
> **＋** `tests/test_ledger.py`: the tests of the ledger hook.
> **＋** `estimate-skill-sprint-open-refuses-a-taken-sprint-id`: the new check.

> **when:**
> The ledger hook `guppi ledger` of `rule-ledger-write`, in `guppi/ledger.py`, reads at a `Stop` a fresh `create` decision line of a page `entity-sprint-<id>`.

> **then:**
> The ledger hook refuses the line when `has_page` of `guppi/materialize.py` finds the page `entity-sprint-<id>` live or archived.
> **＋** For such a line of the reply just finished, it exits 2 with one stderr line that names the id and asks for another id.
> **＋** A `create` of a sprint page that `has_page` does not find is written.
> **＋** `.claude/skills/sprint-open/SKILL.md` says that after such a refusal the main agent asks the person for another id, and the opening Case is built again under it.
> **－** A refused `create` does not open the next sprint, so the other decision lines of the session stay refused while no sprint is open.
> **－** The ledger hook does not check the GitHub name.

> **tasks:**
> - [ ] update `rule-skill-sprint-open`
>   - old: `so the opening Case is the first Case the session ratifies.`
>   - new: `` so the opening Case is the first Case the session ratifies. It also refuses that `create` when a live or archived sprint page already holds the id: ask the person for another id, and send the opening Case back to its `case-guppi` to be built again under it (case 788.1). ``
>   - change: `the ledger hook refuses the create of a sprint page whose id a live or archived sprint page holds, and the opening Case is built again under another id (case 788.1)`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-open/SKILL.md`
> - [ ] update `rule-ledger-write`
>   - old: `` so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). ``
>   - new: `` so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). It refuses a fresh `create` decision line of a page `entity-sprint-<id>` when `has_page` of `guppi/materialize.py` finds that page live or archived, with one stderr line that names the id and asks for another, and such a refused line opens no sprint (case 788.1). ``
>   - change: `refuses the create of a sprint page whose id a live or archived sprint page already holds (case 788.1)`
> - [ ] `guppi/ledger.py`: a function `refused_taken_sprint` refuses a fresh `create` of a slug that `is_sprint_page` judges a sprint page when `has_page` of `guppi/materialize.py` finds it under `entities`, imported inside the function; `refused_without_sprint` does not count a refused line; one stderr line per refused line of the reply just finished.
> - [ ] `tests/test_ledger.py`: tests named `taken_sprint`: a live id, an archived id, a free id, and a refused `create` that leaves the other decision lines of the session refused while no sprint is open.
> - [ ] create `estimate-skill-sprint-open-refuses-a-taken-sprint-id`
>   - ref: `rule-skill-sprint-open`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook refuses the create of a sprint page that has_page finds live or archived, writes one that it does not find, and opens no sprint by a refused line`
>   - method: `uv run pytest tests/test_ledger.py -k taken_sprint; by hand at the Retro of this session: the new Render of rule-skill-sprint-open in raw/<date>/<hi HHMM>/spec.md read against the Criterion`
>   - tags: `[sprint, ledger, hooks]`
> - [ ] read `estimate-skill-sprint-open-refuses-a-taken-sprint-id`

> **ratification:**
> ```
> - decision[case 788.1][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}
> - decision[case 788.1][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 788.1][create][estimate-skill-sprint-open-refuses-a-taken-sprint-id]{ref:rule-skill-sprint-open}{tags:sprint,ledger,hooks}
> ```

### Case 788.2 — A Case id carries its sprint and starts again at 1 in each sprint

> **given:**
> `rule-ratification`: its Render, `vault/wiki/ratification.md`, sets the form of a Case id, and it governs the new module.
> **＋** `rule-decisions-schema`: its Render, `vault/wiki/decisions/schema.yaml`, names the slug and the field `case` of a Decision page.
> **＋** `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, sets how the main agent dispatches a new Case.
> **＋** `guppi/caseid.py` and its command in `guppi/cli.py`: the one grammar of a Case id and the command for the next id.
> **＋** `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` and `guppi/materialize.py`: the readers of a Case id.
> **＋** `vault/wiki/sprint.md`, `raw/<date>/<hi HHMM>/ledger.md`, `<plan>.checked.json` and `/sprint-open`: where the command reads the open sprint and holds the id, and the skill that sets the id of the opening Case.
> **＋** `tests/test_caseid.py`: the test of both forms over each reader.
> **＋** `estimate-ratification-case-id-carries-the-sprint`: the new check.

> **when:**
> `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` or `guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
> **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run guppi caseid --next` before it dispatches a new top-level Case.

> **then:**
> A Case id of a sprint opened after this Case is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case.
> **＋** The readers read a Case id through `guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
> **＋** The sprints `migration` and `plugin`, opened before this Case, keep plain ids to their close, by a fixed list in `guppi/caseid.py`.
> **＋** `uv run guppi caseid --next` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md`, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
> **＋** It holds the id it prints in `<plan>.checked.json`, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
> **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
> **－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.

> **tasks:**
> - [ ] update `rule-ratification`
>   - old: `` The id is `case N` — the word and a space — in the first bracket and in `{supersedes:case N}` alike; ``
>   - new: `` The id is `case N` — the word and a space — in the first bracket and in `{supersedes:case N}` alike. N is the id of the sprint, a hyphen and the number of the Case in that sprint, from 1 in each sprint, with a dot for each sub-case level, such as `case kir-plugin-12.1`; a sprint id holds no dot and starts with the GitHub name of its author, so two people never share one. An N with no sprint part, such as `case 785.1`, is a Case from before sprint ids, and the sprints `migration` and `plugin` keep that form to their close: every reader takes both forms, and no such id is renamed. `uv run guppi caseid --next` prints the id of the next Case of the open sprint and holds it, and the opening Case of a sprint is `<id>-1` (case 788.2). In a line, ``
>   - set:
>     ```
>     implementation_ref: [guppi/caseid.py, tests/test_caseid.py]
>     ```
>   - change: `a Case id carries the id of its sprint and starts again at 1 in each sprint; a plain id is a Case from before sprint ids (case 788.2)`
> - [ ] `uv run guppi render`: `vault/wiki/ratification.md`
> - [ ] update `rule-decisions-schema`
>   - old: `` Slug. `decision-case-<N>`: `decision-case-18.1`. Mechanical, ``
>   - new: `` Slug. `decision-case-<N>`: `decision-case-kir-plugin-12.1`, or `decision-case-18.1` for a Case from before sprint ids (case 788.2). Mechanical, ``
>   - old: `` required; case id, e.g. `18.1`. The Case this page records. ``
>   - new: `` required; case id, e.g. `kir-plugin-12.1`, or `18.1` for a Case from before sprint ids. The Case this page records. ``
>   - change: `the slug and the field case show an id that carries its sprint (case 788.2)`
> - [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] update `rule-orchestration`
>   - old: `the agent dispatches it with the Case id, the Frontier item and its source,`
>   - new: `` the agent dispatches it with the Case id — for a new top-level Case the id that `uv run guppi caseid --next` prints and holds, but the opening Case of a sprint, whose id `/sprint-open` sets (case 788.2) —, the Frontier item and its source, ``
>   - change: `the main agent takes the id of a new top-level Case from uv run guppi caseid --next (case 788.2)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `guppi/caseid.py`: the one grammar of a Case id — its parse into sprint, number and sub-case levels, the top-level Case, a sort key, and the fixed list of the sprints `migration` and `plugin` — and the command `guppi caseid --next`, which takes the open sprint from `opened_sprint` of `guppi/materialize.py` over the session's ledger, else from `sprint_id`, prints the id that `next_id` gives and holds it in the store; registered in `guppi/cli.py`.
> - [ ] `guppi/casecheck.py`: `top_case`, `CASE_NAME` and `case_number` read by the grammar of `guppi/caseid.py`.
> - [ ] `guppi/lint.py`: `ORIGIN_CASE` and `DEFERRED_LINE` take an id with a sprint part, by the grammar of `guppi/caseid.py`.
> - [ ] `guppi/gate.py`: `case_key` sorts by the sort key of `guppi/caseid.py`.
> - [ ] `tests/test_caseid.py`: runs `parse_line` of `guppi/materialize.py`, `top_case`, `case_file` and `case_number` of `guppi/casecheck.py`, `held_number` of `guppi/ratified.py`, `check_origin` of `guppi/lint.py` and `case_key` of `guppi/gate.py` over `kir-plugin-12.1` and `785.1` and asserts they read both alike; runs `guppi caseid --next` twice over a temp vault of a new sprint, of a session that creates a sprint page, and of the sprint `plugin`, and asserts the two runs print two ids.
> - [ ] create `estimate-ratification-case-id-carries-the-sprint`
>   - ref: `rule-ratification`
>   - kind: `QA`
>   - purpose: `Whether every reader of a Case id takes an id that carries its sprint and a plain id from before sprint ids alike, and guppi caseid --next prints and holds the next id of the open sprint, which the main agent uses`
>   - method: `uv run pytest tests/test_caseid.py; by hand at the Retro of this session: the new Renders of rule-ratification and rule-orchestration in raw/<date>/<hi HHMM>/spec.md read against the Criterion`
>   - tags: `[ledger, harness, session]`
> - [ ] read `estimate-ratification-case-id-carries-the-sprint`

> **ratification:**
> ```
> - decision[case 788.2][update][rule-ratification]{ref:rule-ratification}
> - decision[case 788.2][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 788.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 788.2][create][estimate-ratification-case-id-carries-the-sprint]{ref:rule-ratification}{tags:ledger,harness,session}
> ```

### Case 788.3 — The main agent asks the sprint id first, and the opening Case is its Case 1

> **given:**
> `rule-skill-sprint-open`: its Render, `.claude/skills/sprint-open/SKILL.md`, sets what the opening Case asks.
> **＋** `estimate-skill-sprint-open-asks-the-opening-questions`: its Criterion, `purpose` and `method` are set anew.
> **＋** `vault/wiki/brief.md`: holds the line `open the next sprint`.
> **＋** `vault/wiki/backlog.md`: the backlog the opening Case counts.
> **＋** `vault/wiki/sprint.md`: marks the last sprint closed.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `entity-sprint-<id>` and `/sprint-close`: the page of the new sprint and the skill its close line names.

> **when:**
> The main agent starts the skill `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, in a session whose `vault/wiki/sprint.md` marks the last sprint closed.

> **then:**
> Before any Frontier is assembled and before any dispatch, the main agent asks the person in one plain question for the id of the sprint, which names the page `entity-sprint-<id>` and starts with the GitHub name of its author, such as `kir-plugin`, with lower-case letters, digits and hyphens and no dot.
> **＋** The main agent then dispatches `case-guppi` with the Case id `<id>-1` for the line `open the next sprint` of the `Cases` of Next session in `vault/wiki/brief.md`, with the id of the sprint and the questions of the opening in the prompt of the call: its goal in one sentence, its Definition of done as Estimates, and the first milestone and its items.
> **＋** The prompt asks that the opening Case say how many items `vault/wiki/backlog.md` holds and ask the person whether to take any of them.
> **＋** The prompt asks that the opening Case write, as the last item of the last milestone of the new sprint page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``.
> **＋** The opening Case is the first Case the session ratifies.
> **－** No Frontier is assembled, written to `raw/<date>/<hi HHMM>/frontier.md` or shown, and no other item is taken up, before the person ratifies the opening Case.
> **－** The opening Case goes through no item of `vault/wiki/backlog.md` that the person does not name.
> **－** The skill decides none of the answers: the main agent asks the person for the id, and `case-guppi` puts each other question to the person in a round.

> **tasks:**
> - [ ] update `rule-skill-sprint-open`
>   - old: `` 2. Dispatch `case-guppi` at once for the line `open the next sprint` of the brief, as `vault/wiki/orchestration.md` sets it, and write into the prompt of the call that the opening Case asks the person, in its rounds: ``
>   - new: `` 2. Ask the person first, in one plain question, for the id of the sprint, which names the page `entity-sprint-<id>`, the branch of the sprint and every Case id of the sprint: it starts with the GitHub name of its author, such as `kir-plugin`, and holds lower-case letters, digits and hyphens and no dot. Then dispatch `case-guppi` at once for the line `open the next sprint` of the brief, as `vault/wiki/orchestration.md` sets it, with the Case id `<id>-1` and the id of the sprint, and write into the prompt of the call that the opening Case asks the person, in its rounds (case 788.3): ``
>   - old:
>     ```
>        - the id of the sprint, which names the page `entity-sprint-<id>`;
>        - its goal in one sentence, the `purpose` and the `## Purpose` of the page;
>     ```
>   - new:
>     ```
>        - its goal in one sentence, the `purpose` and the `## Purpose` of the page;
>     ```
>   - old: `` 5. The skill decides none of the answers: `case-guppi` puts each to the person, ``
>   - new: `` 5. The skill decides none of the answers: the main agent asks the person for the id, and `case-guppi` puts each other question to the person, ``
>   - change: `the main agent asks the sprint id before the dispatch, and the opening Case is Case <id>-1 (case 788.3)`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-open/SKILL.md`
> - [ ] update `estimate-skill-sprint-open-asks-the-opening-questions`
>   - set:
>     ```
>     status: pending
>     purpose: Whether /sprint-open has the main agent ask the sprint id first, then the opening Case dispatched as Case <id>-1 before any Frontier, ask its goal, its Definition of done, its first milestone and whether to take an item of the backlog, and write the close line
>     method: "by hand, at the Retro of this session, the new Render of rule-skill-sprint-open in raw/<date>/<hi HHMM>/spec.md read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the main agent asks the sprint id before the dispatch, and the opening Case is Case <id>-1 (case 788.3)`
> - [ ] read `estimate-skill-sprint-open-asks-the-opening-questions`

> **ratification:**
> ```
> - decision[case 788.3][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}
> - decision[case 788.3][update][estimate-skill-sprint-open-asks-the-opening-questions]{ref:rule-skill-sprint-open}
> ```

### Case 788.4 — One function counts the next free id

> **given:**
> `guppi/caseid.py`: `next_id`, the one count of the next free id.
> **＋** `guppi/casecheck.py`: `new_number`, which calls it for a Case built again.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` and `raw/<date>/<hi HHMM>/ledger.md`: the Case files and the ledger of the session.
> **＋** `<plan>.checked.json`: the store of the checked Cases beside the plan file.
> **＋** `vault/wiki/decisions/` and `vault/archive/`: the Decision pages, live and archived.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: its Criterion is replaced whole.
> **＋** `rule-one-judgment-one-implementation`: the rule that one judgment lives in one module.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`, and `<plan>.checked.json` beside the plan file.

> **then:**
> For a file that holds a top-level Case N, the hook reads the decision lines of a kind other than `defer` in the session's ledger that belong to the family of Case N, which is Case N and its sub-cases at any depth.
> **＋** Case N gets a finding when a number of its family that has such a line has no section in the file, or when a number that has such a line has a sub-case in the file.
> **＋** The finding names each such number and a new id of the sprint of Case N: one above the highest number of that sprint that the Decision pages under `vault/wiki/decisions/` and `vault/archive/`, the decision lines of the session's ledger, the keys of `<plan>.checked.json` and the names of the files under `raw/<date>/<hi HHMM>/cases/` hold.
> **＋** The judgment comes from one function of `guppi/casecheck.py`, and the new id from `next_id` of `guppi/caseid.py`, which the command for the next id runs too.
> **＋** The finding tells `case-guppi` to build the Case under the new id. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr, and `case-guppi` fixes the file or writes the Case under the new id.
> **－** An answer on the old path that holds sub-cases of Case N without Case N gets no finding of this check.
> **－** A Case whose family has no decision line other than `defer` in the session's ledger gets no finding of this check. Neither does a Case built again with a section for each number of its family that has such a line and no sub-case under any of them.

> **tasks:**
> - [ ] `guppi/caseid.py`: `next_id` takes a sprint and the ids of the Decision pages live and archived, of the decision lines of the session's ledger, of the keys of the store and of the files under `cases/`, and gives one above the highest number of that sprint, or of the plain ids for a sprint of the fixed list.
> - [ ] `guppi/casecheck.py`: `new_number` gives the id of `next_id` over the same sources; the shape judgment stays in its one function of `guppi/casecheck.py`.
> - [ ] `tests/test_casecheck.py`: a test named `shape` whose new id stands above an id that only the store holds, one that only a Case file holds and one that only a Decision page holds, and one that runs `new_number` and `guppi caseid --next` over the same folder and asserts they give the same id.
> - [ ] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the new id is counted by next_id of guppi/caseid.py over the Decision pages, the ledger, the store and the Case files of the session (case 788.4)`
> - [ ] read `estimate-case-check-sends-back-a-ratified-case-in-another-shape`

> **ratification:**
> ```
> - decision[case 788.4][update][estimate-case-check-sends-back-a-ratified-case-in-another-shape]{ref:rule-case-check}
> ```

### Case 788.5 — `/box` judges a later Case across sprints

> **given:**
> `guppi/box.py`: the check of a conserved Spec.
> **＋** `guppi/caseid.py`: the grammar of a Case id.
> **＋** `vault/raw/<date>/<HHMM>/` and its branch `spec/<date>-<HHMM>`: the folder and the branch of a conserved Spec.
> **＋** `guppi/materialize.py`: `is_carried_over`, which judges the folder marked.
> **＋** `tests/test_box.py`: the tests of the check.
> **＋** `estimate-spec-box-refuses-a-stale-spec`: its Criterion is replaced whole.

> **when:**
> Someone runs `uv run guppi box --check <folder> --session <id>`, where `<folder>` is a folder `vault/raw/<date>/<HHMM>/` and `<id>` is the session id of a `hi` line.

> **then:**
> It prints one line for each reason the Spec cannot run now, and exits 1 when it prints any; with no reason it prints nothing and exits 0.
> **＋** A folder that `is_carried_over` of `guppi/materialize.py` does not judge marked is one reason, and so is a folder for which no branch `spec/<date>-<HHMM>` exists.
> **＋** A current branch `main` is one reason: the shared branch is never `main`.
> **＋** A decision line other than a `defer` in the ledger of the session's folder is one reason, naming its Case.
> **＋** A live page named by an `update`, `delete` or `defer` item of the folder's `spec.md` is one reason when a line of its History names the Decision page of a later Case, read by `guppi/caseid.py`: a plain id whose whole part is higher than that of every Case of that Spec with a plain id, when the Spec holds one; an id of a sprint whose number is higher than that of every Case of that Spec of the same sprint; or an id of a sprint of which the Spec holds no Case, on a History line dated on or after the date of the folder. The line names the page and that Decision page.
> **＋** A slug that a `create` item of that Spec names and a live page carries is one reason, naming the slug.
> **－** The check writes nothing, switches no branch, and opens no page beyond those the Spec names.

> **tasks:**
> - [ ] `guppi/box.py`: `DECISION_LINK`, `history_cases` and `spec_items` read both forms by `guppi/caseid.py`, and a History line names a later Case as the Criterion sets it.
> - [ ] `tests/test_box.py`: tests of a later Case of the same sprint, of another sprint dated on or after the folder, of a plain id after a Spec of plain ids, and of a plain id beside a Spec with no plain id.
> - [ ] update `estimate-spec-box-refuses-a-stale-spec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a later Case is judged by the sprint and the number of its id, or by the date of its History line for another sprint (case 788.5)`
> - [ ] read `estimate-spec-box-refuses-a-stale-spec`

> **ratification:**
> ```
> - decision[case 788.5][update][estimate-spec-box-refuses-a-stale-spec]{ref:rule-spec-box}
> ```

### Case 788.6 — The guard of a Case file reads a name in either form

> **given:**
> `guppi/ratified.py`: `held_number`, the guard of a Case file.
> **＋** `guppi/casecheck.py` of `rule-case-check`: `case_number`, `clashes` and `new_number`, which the guard calls.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `tests/test_ratified.py`: the tests of the guard.
> **＋** `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`: its Criterion, `purpose` and `method` are set anew.
> **＋** `estimate-spec-write-exits-2-on-an-error`: the error rule of the guard.

> **when:**
> `case-guppi` calls `Edit`, `Write` or `MultiEdit` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi ratified --guard` on `PreToolUse` reads the path, the agent type and the `agent_id` of the call from the hook input, and `<plan>.checked.json` beside the plan file of the session.

> **then:**
> The guard reads the id N from the file name by `case_number` of `guppi/casecheck.py`, a plain id such as `785` or an id of a sprint such as `kir-plugin-12` alike.
> **＋** The call is refused when `<plan>.checked.json` holds Case N, or a sub-case of it, under its id alone with an `agent_id` other than the one of the call: exit 2 with the reason on stderr, and the call does not run.
> **＋** The reason names the file and a free id, and tells `case-guppi` to build its Case under that id.
> **＋** The holder is judged by `clashes` and the free id is counted by `new_number` of `guppi/casecheck.py`, the judgments that the check of `rule-case-check` runs.
> **＋** A call that passes while `<plan>.checked.json` holds no entry under N alone writes there, under N, an entry with the `agent_id` of the call and the time, and no text, so the id is held before the agent stops.
> **＋** A refusal writes one line of the refusal to the day's event log.
> **－** A call whose `agent_id` is the one of the entry under N, and an entry with no `agent_id`, are not refused by this check.
> **－** A call with no `agent_id`, a file whose name gives no id, and a session with no plan file are not judged by this check, and nothing is written into `<plan>.checked.json`.
> **－** An error of the guard while it finds the plan file or reads or writes `<plan>.checked.json` lets the call run: exit 0 with one line on stderr, as `estimate-spec-write-exits-2-on-an-error` sets it for the guard.

> **tasks:**
> - [ ] `tests/test_ratified.py`: tests named `number_held` over a file `case-kir-plugin-12.md` held by another agent and by the same agent.
> - [ ] update `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the first call of case-guppi on the file of a Case, its name in either form of the id, holds its id in the store, and a call of another case-guppi on that file is refused with a free id
>     method: uv run pytest tests/test_ratified.py -k number_held
>     ```
>   - change: `the Criterion replaced whole — the guard reads a file name in either form of the id and names a free id (case 788.6)`
> - [ ] read `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`

> **ratification:**
> ```
> - decision[case 788.6][update][estimate-spec-reconcile-refuses-a-case-file-another-agent-holds]{ref:rule-spec-reconcile}
> ```

### Case 788.7 — The check of a Case file names a free id when another agent holds one

> **given:**
> `guppi/casecheck.py`: the check of the file of a Case.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `<plan>.checked.json`: the store beside the plan file.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `estimate-case-check-sends-back-a-case-number-held-by-another-agent`: its Criterion and `purpose` are set anew.
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape`: the count of the free id.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, `agent_id` of the payload, and `<plan>.checked.json`.

> **then:**
> The hook stores each Case of the file in `<plan>.checked.json` with the `agent_id` of the payload beside its text, its findings and the time of the store.
> **＋** A top-level Case N of the file, N a plain id or an id of a sprint, is sent back when the store holds Case N, or a sub-case of it, under its id from an answer with another `agent_id`.
> **＋** Its message gives `case-guppi` a free id, counted as `estimate-case-check-sends-back-a-ratified-case-in-another-shape` counts it, to build the Case under, and the exit code is 2.
> **＋** Each Case of that file is stored apart, under its id joined with its `agent_id`, and the entry of the other agent under the id alone stays as it was.
> **＋** The Spec hook, the `Stop` comparison and the comparison of a case file with the store read the entry under the id alone.
> **－** An unchanged file whose text its entry apart already holds with this finding is stored again and exits 0, so it is not sent back twice.
> **－** An entry with no `agent_id`, stored before the change or held by `uv run guppi caseid --next`, gives no finding of this check, and neither does a file whose `agent_id` is the one of the entry under the id.

> **tasks:**
> - [ ] `tests/test_casecheck.py`: tests named `subagent_clash` over a Case `kir-plugin-12` held by another agent, and over an id that `guppi caseid --next` held with no `agent_id`.
> - [ ] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
>   - set:
>     ```
>     status: pending
>     purpose: A Case of case-guppi under an id, plain or of a sprint, that the store holds from the answer of another agent goes back to it with a free id, and the other agent's entry is kept
>     ```
>   - change: `the Criterion replaced whole — an id of a sprint is judged as a plain one, and an id held by guppi caseid --next gives no finding (case 788.7)`
> - [ ] read `estimate-case-check-sends-back-a-case-number-held-by-another-agent`

> **ratification:**
> ```
> - decision[case 788.7][update][estimate-case-check-sends-back-a-case-number-held-by-another-agent]{ref:rule-case-check}
> ```
