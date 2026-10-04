## Case 629 — The check of a built Case compares it with the session's other Cases, and a Case built again comes back by its changed sub-cases

> **context:**
> Two items are taken together, at the person's word. The first is C6. Each time `case-guppi` finishes an answer, the `SubagentStop` hook `guppi casecheck --subagent` runs `prespec.judge` over a Spec text built from the Cases of that one answer. So it never compares an answer with the session's other Cases. The comparison of two Cases that write one part of one page is `check_same_target` in `guppi/prespec.py`. It runs only at `/pre-spec`, and after ratification in the `Stop` hook `guppi ratified`, by `prespec.written_findings`. In this session, Cases 627 and 628 were ratified in one batch. The `Stop` hook then printed that case 628.1 writes the section Purpose of `rule-sprint-close` that case 627.1 writes too, and both Cases were built and ratified again. When Case 628 was built, Case 627 stood only in the store `<plan>.checked.json`, not in the plan file. So a check of the plan alone would have missed it.
>
> The second item is C4, `rule-case-rebuild-cost`. It is a placeholder page with one Purpose, deferred by cases 566 and 570. `case-guppi` is told to answer with the whole Case again after a finding of the hook and after any message. In session 2356 a Case with fourteen sub-cases came back whole three times for a change of a few lines of one sub-case. Its `context` also lists searches that changed nothing. The hook can already write an answer of sub-cases alone into the Case file: it replaces only their sections there (`write_case_files`). But it judges such a sub-case without its parent, so it reads no `given` for its frame and no earlier `recommend` for the titles of the rounds.
>
> The person chose these answers. The early check compares an answer with the plan's Cases and with the stored Cases not yet ratified. It leaves out a stored Case with findings, a Case that a `{supersedes}` mark retired, and the answer's own earlier parts. A clash is a finding, and the check after ratification stays as a backstop (Q1–Q4). `case-guppi` answers again by its changed sub-cases alone while the parent's own parts stand, and with the whole Case otherwise (Q5, Q8). `context` keeps only the searches the Case rests on (Q6). No rule splits a large item (Q7). The changes go on `rule-case-build` and `rule-case-check`, and the placeholder is retired by a `delete` that carries `{supersedes:case 566}` and `{supersedes:case 570}` (Q9). One Case holds five sub-cases, one promise each (Q10).
>
> The frame. A Grep of `SubagentStop` over `vault/wiki/rules/` printed `rule-orchestration`, `rule-case-check`, `rule-case-rebuild-cost`, `rule-hook-registry` and `rule-spec-reconcile`. Over `.claude/` it printed `.claude/settings.json`, where `guppi casecheck --subagent` is the only hook on that event. `rule-orchestration` and `rule-spec-reconcile` say the hook writes the Case file from the answer, and that stays true. A Grep of `whole again|Case whole|sub-cases? alone|holds sub-cases|holds that sub-case` ran over `vault/wiki/*.md`, `vault/wiki/rules/`, `vault/wiki/estimates/`, `.claude/` and `guppi/*.py`. It printed 12 files. `rule-case-build`, `.claude/agents/case-guppi.md` and `estimate-case-build-writes-the-case` change (629.2). The other hits stand: `log.md`, which is not read; `case-schema.md`, `rule-case-protocol` and `estimate-spec-write-removes-a-superseded-case`, on a `{supersedes}` mark of a sub-case; `estimate-case-check-sends-back-a-faulty-round` and `guppi/casecheck.py`, on a round answered whole; `estimate-case-check-sends-back-a-faulty-case`, on the file of a lone sub-case; `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, which gives an answer of sub-cases alone no finding, as Q8 needs; and `rule-language`, on the file sent whole. `orchestration.md`, read whole, sends a Case again whole in its file and lists the Cases of the answer. The file stays whole, so it stands. A Grep of `rule-case-rebuild-cost` over the repository outside `vault/archive/` and `vault/raw/` printed `brief.md`, `backlog.md`, `log.md` and the Decision pages 566 and 570. `backlog.md` is written from `deferred_by`, so the item leaves it after the `delete`.
>
> The findings of `/pre-spec`. A Case stored with a finding cannot be shown or written into the Spec. So when the other Case is the one that should change (Q2), `case-guppi` still bounds its own Case so that the finding goes, and its `context` names the other Case and the change it needs. The main agent then asks the person whether that Case is built again. 629.1 says so in `then` and adds it to `rule-orchestration`. `estimate-orchestration-signs-a-batch-together` already sets the batch when the person's word asks that a ratified Case change, and `estimate-orchestration-shows-the-built-case` sets the showing, which does not change. Both stand. Case 628, built again in this session, changes another sentence of `rule-orchestration`, on the ticks of Work Mode, so the two anchors do not meet. The new tests of 629.1 run under `-k session_clash`, because `-k clash` is the selector of `estimate-case-check-sends-back-a-case-number-held-by-another-agent`. 629.1 reads a stored entry under its number alone, as that Estimate, 629.3 and 629.4 do.
>
> The Estimates. `estimate-case-check-sends-back-a-faulty-case` says the hook runs `judge` over the answer's Cases. It says nothing of other Cases or a stored parent, so it stands. `estimate-case-check-notes-a-then-line-shared-by-siblings` says a lone sub-case gets no sibling note from the hook. 629.3 adds only the stored parent, not the siblings, so it stands. `estimate-case-build-records-the-rounds-in-recommend` already lets an item stand under a sub-case's heading, so it stands.
>
> The notes of the hook. One line of the Criterion of `estimate-case-check-requires-each-question-of-the-rounds` is not carried: the line that looked for a title only in the answer. 629.4 replaces it with the line that also reads the store, which is the change itself. Four `then` lines share words with a line of a sibling: 629.4 with 629.1 and 629.3, and 629.5 with 629.2 twice. In each pair the two lines speak of different things: a title of a round against a clash between Cases or a lone sub-case, and the frame check of a finished Case against the answer again. The lines of 629.2 and 629.5 are also carried word for word from the Criteria they replace. So each line stays in its own sub-case.
>
> No refused text is lost between the render and the code. An answer of sub-cases alone that the old hook judges gets at worst a finding, and `case-guppi` answers again with the whole Case. The `then` of 629.2 and 629.5 carry the Criteria they replace word for word but one line, so they hold more than seven `**＋**` lines.
>
> Not done: no rule splits a large item into several Cases (Q7). `case-guppi` does not write the Case file itself (Q5). A search that `context` keeps still lists each file it printed (case 557.1).

> **problem:**
> A clash between two Cases of one session is found only after the person ratified both, so they are built and ratified twice. And a Case changed in one sub-case is written and returned whole, its `context` full of searches that changed nothing. The question is how the early check sees the session's other Cases, how a Case comes back by its changed parts, and what `context` keeps.

> **recommend:**
> - **Which other Cases does the early check compare an answer with?**
>   - Recommended: (b) the ratified Cases of the plan file and the Cases built but not yet ratified in the store, leaving out a stored Case with findings, one a supersedes mark replaced, and the answer's own earlier version.
>   - Answer: agreed.
> - **What does the early check do when an answer clashes with another Case?**
>   - Recommended: (a) a finding: `case-guppi` changes its own Case, and where the other Case should change the main agent asks the person.
>   - Answer: agreed.
> - **Does the late check, after ratification, stay?**
>   - Recommended: (a) keep it as a backstop.
>   - Answer: agreed.
> - **What will check that the early check compares an answer with the other Cases?**
>   - Recommended: (a) a new Estimate on `rule-case-check`, the Criterion of `estimate-case-check-sends-back-a-faulty-case` standing.
>   - Answer: agreed.
> - **How does a Case come back when only a sub-case changed?**
>   - Recommended: (b) the changed sub-cases alone, plus the parent when its own parts changed, the hook checking them with the parent's stored parts and merging them into the store and the file.
>   - Answer: agreed; its part on the parent was replaced by the question on the parent's own text.
> - **What does a Case's `context` say about the searches it ran?**
>   - Recommended: (b) only the searches the Case rests on, each with its pattern and paths.
>   - Answer: agreed.
> - **Is a large item split into several Cases?**
>   - Recommended: (a) no rule for this now; the context names it as not done.
>   - Answer: agreed.
> - **When the parent's own text changes, what comes back?**
>   - Recommended: (a) the whole Case; the changed sub-cases alone only while the parent's `context`, `problem` and `recommend` stand as they were.
>   - Answer: agreed.
> - **Where does the decision on the cost of rebuilding a Case live?**
>   - Recommended: (a) on `rule-case-build` and `rule-case-check`, the placeholder retired by a `delete` with both supersedes marks.
>   - Answer: agreed.
> - **How are the two items cut, and what checks each part?**
>   - Recommended: (a) one Case with five sub-cases: the clash with other Cases, a new Estimate; the answer by changed sub-cases with the placeholder retired, the Criterion of `estimate-case-build-writes-the-case` replaced; a lone sub-case judged with its stored parent, a new Estimate; the titles of the rounds read in the stored `recommend` too, the Criterion of `estimate-case-check-requires-each-question-of-the-rounds` replaced; `context` keeping only the searches the Case rests on, the Criterion of `estimate-case-build-checks-the-finished-case` replaced.
>   - Answer: agreed.

### Case 629.1 — The check of an answer compares its Cases with the session's other Cases

> **given:**
> `rule-case-check` — the check of the answer of `case-guppi` at `SubagentStop`; its Purpose gains a sentence
> **＋** `estimate-case-check-sends-back-a-clash-with-another-case` — the new promise, on `rule-case-check`
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — the hook and its tests
> **＋** `guppi/prespec.py` — `check_same_target`, the one judgment of a clash, run by `/pre-spec` too
> **＋** `guppi/ratified.py` — the `Stop` hook of `rule-spec-write`, which runs the same judgment after ratification
> **＋** the plan file of the session, `<plan>.checked.json` beside it and `raw/<date>/<hi HHMM>/ledger.md` — what the hook reads
> **＋** `rule-orchestration` — what the main agent does with a built Case, rendered into `vault/wiki/orchestration.md`; one sentence is added
> **＋** `rule-case-build` — the instructions of `case-guppi`, which fix a finding in the Case and say in `context` why a page stands
> **＋** `vault/raw/2026-10-04/1439/cases/case-628.md` — Case 628, which changes another sentence of `rule-orchestration`
> **＋** `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — the checks of the answer's own Cases and of a number held by another agent

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
> **＋** Or `tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.
> **＋** The main agent receives the answer of `case-guppi` that passed, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `guppi/prespec.py`, imported, not copied: each Case of the plan file, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
> **＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
> **＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
> **＋** Where the other Case should change rather than its own, `case-guppi` still changes its own Case so that no finding stands, and its `context` names the other Case and the change it needs; the main agent shows the Case as it stands and asks the person whether that other Case is built again, and on the person's yes sends it to its `case-guppi` by `SendMessage`, in a batch when it is ratified.
> **－** A stored Case that has findings, an entry joined with an agent id, and a Case whose number a `{supersedes:case N}` mark of the session's ledger names are not compared.
> **－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
> **－** Two other Cases that clash with each other give this answer no finding.
> **－** The `Stop` hook `uv run guppi ratified` keeps its check of the Cases it writes, by the same function.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `the Case reaches the person in a file the hook writes from the answer that passed them (case 452.1).`
>   - new: `` the Case reaches the person in a file the hook writes from the answer that passed them (case 452.1). The check of an answer compares its Cases with the other Cases of the session, ratified or not, by the judgment the check after ratification runs, so a Case that writes what another Case writes goes back to `case-guppi` before the person first sees it (case 629.1). ``
>   - change: `the check of an answer compares its Cases with the other Cases of the session, from the plan file and the store (case 629.1)`
> - [ ] update `rule-orchestration`
>   - old: `` an answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before it is shown (case 561.9); ``
>   - new: `` an answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before it is shown (case 561.9); a Case whose `context` says that another Case of the session, which it was bounded around after a clash, should change instead is shown as it stands, and the main agent asks the person, in the shape of a question it puts itself, whether that other Case is built again, and on the person's yes sends it to its `case-guppi` by `SendMessage`, in a batch when it is ratified, as `## Showing and signing a Case` sets it (case 629.1); ``
>   - change: `the main agent asks the person whether a Case that another Case was bounded around after a clash is built again (case 629.1)`
> - [ ] create `estimate-case-check-sends-back-a-clash-with-another-case`
>   - kind: `QA`
>   - purpose: `Whether the check of an answer of case-guppi sends back a Case that sets one field, writes one section or replaces one Criterion that another Case of the session, ratified or only stored, sets, writes or replaces too, and whether the main agent asks the person when the other Case should change instead`
>   - method: `uv run pytest tests/test_casecheck.py -k session_clash; then by hand a live answer of case-guppi that the hook sends back for a clash with another Case of the session, that Case shown and ratified once, and, where its context names another Case that should change, the main agent's question to the person and its SendMessage on a yes`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: `check_answer` judges the Cases of the answer with the other Cases of the session by `prespec.check_same_target` — the plan's Cases, then the store's entries under the number alone that the plan does not hold, built by `ratified.case_section`, without an entry with findings, one a `{supersedes}` mark of the ledger names, and the answer's own ids and the family of a top-level Case it holds, then the answer's Cases last — keeping each finding that opens with a Case of the answer; `subagent` passes the plan text; the docstring
> - [ ] `guppi/prespec.py`: the docstring of `check_same_target` names its second caller, the check of the answer of `case-guppi`
> - [ ] `tests/test_casecheck.py`: `-k session_clash` — a clash with a Case of the plan and with a stored Case not yet ratified, each sent back; none with a stored Case with findings, an entry joined with an agent id, one a supersedes mark names, the answer's own earlier version, or two other Cases that clash with each other
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-case-check-sends-back-a-clash-with-another-case`

> **ratification:**
> ```
> - decision[case 629.1][update][rule-case-check]{ref:rule-case-check}
> - decision[case 629.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 629.1][create][estimate-case-check-sends-back-a-clash-with-another-case]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 629.2 — `case-guppi` answers again by its changed sub-cases while the parent's own parts stand

> **given:**
> `rule-case-build` — the instructions of `case-guppi`, rendered into `.claude/agents/case-guppi.md`; one sentence changes
> **＋** `estimate-case-build-writes-the-case` — its Criterion replaced whole, its `method` set anew
> **＋** `rule-case-rebuild-cost` — the placeholder of the deferred decision, retired
> **＋** `rule-case-check` — the hook that checks the answer and writes the file of the Case
> **＋** `.claude/skills/grill-me/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/ratification.md`, `.claude/agents/ask-guppi.md` and `.claude/settings.json` — what `case-guppi` loads and reads
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — the check of a ratified Case built again, which gives an answer of sub-cases alone no finding

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends its answer back with findings.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification`, and nothing else.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** Asked again after the hook of `rule-case-check` sent findings back, or by a message, it answers with the changed sub-cases alone, each from its heading to the fence of its `ratification`, when the parent's `context`, `problem` and `recommend` stand as they were; an item of `recommend` whose answer changed only that sub-case stands under its heading, and the hook writes the sub-cases into the file of the Case beside the parts that did not change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file and no ledger line.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `when it sends findings back, fix the Case and answer with it whole again. Asked again by a message, answer with the Case whole again, changed as asked, or with a round when the message opens a fork.`
>   - new: `` when it sends findings back, fix the Case and answer with it again. Asked again by a message, answer with the Case again, changed as asked, or with a round when the message opens a fork. An answer again holds the Case whole, or, where the parent's `context`, `problem` and `recommend` stand as they were, the changed sub-cases alone, each from its heading to the fence of its `ratification`, an item of `recommend` whose answer changed only that sub-case under its heading; the hook writes them into the file of the Case beside the parts that did not change (case 629.2). ``
>   - change: `case-guppi answers again by its changed sub-cases alone while the parent's own parts stand (case 629.2)`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending, method: "by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case, one Case with a create without a ref, one that changes a hook, and a change the person asked for on one sub-case of a Case with sub-cases, answered by that sub-case alone; the tokens and seconds of each dispatch in the estimate line"}`
>   - change: `the Criterion replaced whole — asked again, case-guppi answers by its changed sub-cases alone while the parent's own parts stand (case 629.2)`
> - [ ] delete `rule-case-rebuild-cost`
>   - impact: `the placeholder of the decision deferred by cases 566 and 570; the answer by changed sub-cases lands on rule-case-build and rule-case-check, the context's searches on rule-case-build, and the split of a large item is not done`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 629.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 629.2][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> - decision[case 629.2][delete][rule-case-rebuild-cost]{ref:rule-case-rebuild-cost}{supersedes:case 566}{supersedes:case 570}
> ```

### Case 629.3 — The check judges a lone sub-case with its stored parent

> **given:**
> `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` — the new promise, on `rule-case-check`
> **＋** `rule-case-check` — the check of the answer of `case-guppi`
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — the hook and its tests
> **＋** `guppi/prespec.py` — `judge`, whose frame check reads a sub-case's `given` from its parent; `/pre-spec`, which runs it over the plan
> **＋** `<plan>.checked.json` — the store of checked answers

> **when:**
> `SubagentStop` fires when `case-guppi` answers with sub-cases of a Case N alone, and `<plan>.checked.json` beside the plan file of the session holds Case N under its number alone.
> **＋** Or `tests/test_casecheck.py` runs `uv run guppi casecheck --subagent` over such an answer and a made-up store.

> **then:**
> The hook builds the Spec text it judges with the stored section of Case N before the sub-cases of the answer, so `prespec.judge` of `guppi/prespec.py` reads the `given` and `context` of Case N for a sub-case of the answer that has none of its own, as `/pre-spec` reads them in the plan.
> **＋** A slug or a path in a code span of the `when` or `then` of such a sub-case, or a slug of its `then` block, that the `given` of Case N does not name is a finding of that sub-case, stored and sent back as any other finding.
> **－** A finding or a note on Case N itself is not given to the answer, and Case N is neither stored nor written again from this answer.
> **－** With no stored Case N, the sub-cases are judged alone, and a sub-case with no `given` of its own gets no finding on its frame.

> **tasks:**
> - [ ] create `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
>   - kind: `QA`
>   - purpose: `Whether the check of an answer of case-guppi that holds sub-cases alone judges their frame against the given of their stored parent, and gives the answer no finding of the parent itself`
>   - method: `uv run pytest tests/test_casecheck.py -k lone; then by hand a live answer of case-guppi with sub-cases alone, its stored entries and the findings sent back read against the Criterion`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: `check_answer` puts the section of the stored top-level Case of a lone sub-case, built by `ratified.case_section` from its entry under the number alone, before the sub-cases in the Spec text it judges, and keeps only the findings and notes of the answer's Cases; the docstring
> - [ ] `tests/test_casecheck.py`: `-k lone` — a lone sub-case whose `then` names a slug the stored parent's `given` does not name gets a finding; one whose names stand there gets none; a finding of the stored parent is not given to the answer; with no stored parent, no frame finding
> - [ ] read `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`

> **ratification:**
> ```
> - decision[case 629.3][create][estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 629.4 — The titles of the rounds are looked for in the stored `recommend` too

> **given:**
> `estimate-case-check-requires-each-question-of-the-rounds` — its Criterion replaced whole, its `method` set anew
> **＋** `rule-case-check` — the check of the answer of `case-guppi`
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — the hook and its tests
> **＋** `.claude/skills/grill-me/SKILL.md` — the title line of a question of a round
> **＋** `<plan>.checked.json` — the store of checked answers

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `agent_transcript_path` holds the agent's earlier outputs with no Case heading, which are its rounds of questions on that Case.

> **then:**
> `uv run guppi casecheck --subagent` takes the title of each question of those rounds from its line `❓ **Q<n>** - **<title>**:`, the title line of the template of `.claude/skills/grill-me/SKILL.md`.
> **＋** It takes titles only from a round that the function of `guppi/casecheck.py` that judges the form of a round finds in form, the function the check of 601.1 sends a round back by; a round out of form gives no title.
> **＋** A title that no item of a `recommend` opens with, in bold, among the Cases of the answer and the entries of `<plan>.checked.json` under the number alone of each Case of their family that the answer does not hold, is a finding of the top-level Case — of the first Case of the answer when it holds sub-cases alone — that names the title, sent back and stored as any other finding.
> **－** An answer with no earlier round gives no such finding.
> **－** A title asked in more than one round is looked for once.
> **－** The words of an item after its title are not judged.
> **－** A round out of form that came back unchanged, passed the check of its form and was shown gives no title either.

> **tasks:**
> - [ ] update `estimate-case-check-requires-each-question-of-the-rounds`
>   - set: `{status: pending, method: "pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round, and an answer of sub-cases alone whose titles stand in the recommend of its stored parent; then by hand a Case the hook sends back for a missing title"}`
>   - change: `the Criterion replaced whole — a title held in the stored recommend of a Case of the family that the answer does not hold is no finding (case 629.4)`
> - [ ] `guppi/casecheck.py`: `check_rounds` reads the titles of the `recommend` of each stored entry, under the number alone, of the family of the answer's Cases that the answer does not hold; the docstring
> - [ ] `tests/test_casecheck.py`: `-k rounds` — an answer of sub-cases alone whose round titles stand in the stored parent's `recommend` gets no finding; a title in neither gets one
> - [ ] read `estimate-case-check-requires-each-question-of-the-rounds`

> **ratification:**
> ```
> - decision[case 629.4][update][estimate-case-check-requires-each-question-of-the-rounds]{ref:rule-case-check}
> ```

### Case 629.5 — `context` keeps only the searches the Case rests on

> **given:**
> `rule-case-build` — the instructions of `case-guppi`, rendered into `.claude/agents/case-guppi.md`; one sentence is added
> **＋** `estimate-case-build-checks-the-finished-case` — its Criterion replaced whole, its `purpose` and `method` set anew
> **＋** `.claude/agents/ask-guppi.md` — the recipe whose index lines it reads for a fact no slug marks
> **＋** `vault/wiki/rules/` and `.claude/` — where it searches for the words that name a moment
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the case files of the Cases its prompt names

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
> **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
> **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
> **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
> **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; it claims nothing the search did not print.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` A claim of `context` about a search names its pattern and the paths it ran over, ``
>   - new: `` `context` names a search only when the Case rests on it: a search with a hit that enters the Case, with a hit that stands and needs the reason why, or that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out (case 629.5). A claim of `context` about a search names its pattern and the paths it ran over, ``
>   - change: `the context of a Case keeps only the searches the Case rests on (case 629.5)`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set: `{status: pending, purpose: "Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, the Cases of the session its prompt names, the purpose and method of an Estimate whose Criterion it replaces, what each search printed and that the context keeps only the searches the Case rests on, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec", method: "by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict; the count of each in the reading line"}`
>   - change: `the Criterion replaced whole — the context names only the searches the Case rests on (case 629.5)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-checks-the-finished-case`

> **ratification:**
> ```
> - decision[case 629.5][update][rule-case-build]{ref:rule-case-build}
> - decision[case 629.5][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}
> ```
