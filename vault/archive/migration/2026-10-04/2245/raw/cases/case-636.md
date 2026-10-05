## Case 636 — case-guppi runs each cited search again before it answers

> **context:**
> `case-guppi` searches the vault while it builds a Case and then says in `context` what each search found. Since case 557.1, its instructions say to name the pattern and the paths of each search, to list the files or give the count the search printed, and to claim nothing the search did not print. The instruction still fails. `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` has eleven children, and the four still live came after that instruction. Three of them share one cause: the agent wrote a fact from its own reading, not from the output of the command it cites. They are `lesson-case-build-a-count-in-context-not-from-a-run` (Case 611 said seven calls where a Grep printed six), `lesson-case-build-hits-counted-as-lines` (Case 620 counted lines, not hits) and `lesson-case-build-a-grep-cited-for-files-it-did-not-print` (Case 632 said a Grep printed three files when it printed one). The pre-spec check of `ask-guppi` caught each one. The pages record a rebuild for Case 620 and Case 632, and none for the Cases of session 0317.
>
> This Case adds one step at the moment that cause acts. Just before it answers with a Case, `case-guppi` runs each search that `context` names again, as `context` writes it, and takes the files and counts from that output. The fourth live child, `lesson-case-build-a-page-judged-true-by-its-mark-not-its-moment` (Case 620), gives two other causes in its `root_cause`, and this Case closes neither. The first is that the agent did not search the moment the change acts at. The Criterion line of `estimate-case-build-checks-the-finished-case` on searching `vault/wiki/rules/` and `.claude/` for the words that name that moment (case 557.1) covers it. The second is that the agent did not search the cascade that the `set` of an Insight sets off. No line of that Criterion covers it. The lesson is archived with the Insight all the same, and if the fault happens again it raises the pattern again. The Case covers the contexts of Cases only. The reading lines and ledger lines of the main agent stay under the writing rule of `CLAUDE.md` (case 359), and none of the later children is about them. A hook that runs the searches again was set aside for now. Under `rule-case-check`, no script judges the text of the story sections (cases 449, 537), and that sentence stays true.
>
> With the change, the Insight is `actioned` and leaves `backlog.md` at the librarian's next run. The cascade of `generate` then archives its four `clustered` children, as the Criterion of `estimate-generate-cascades` says. This Case does not change the cascade, so that Criterion stands. Case 637.2 of this session also changes `rule-case-build`. It adds a sentence on what `case-guppi` does when the hook sends its Case back for a clash with another Case. That sentence sits where the instructions say what to do with findings the hook sends back. This Case's pair anchors on the sentence about a claim of `context` about a search, in the paragraph on the checks made before the answer. The two pairs do not touch one sentence. Running the searches again before each answer, an answer again after a send-back included, does not contradict that sentence. The case file of 637 is in `given`.
>
> The frame: a Grep of `the search did not print|search printed` over the repository, leaving out `vault/raw/` and `vault/archive/`, printed `vault/wiki/log.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/estimates/estimate-case-build-checks-the-finished-case.md`, `.claude/agents/case-guppi.md`, `vault/wiki/decisions/decision-case-557.1.md` and `vault/wiki/decisions/decision-case-557.md`. The hit in `log.md` is not read, and the two Decision pages state their own moment and stay. The other hits are in `given`. A Grep of ``answer of `?case-guppi`` over `vault/wiki/rules/` printed `rule-case-check.md`, `rule-case-protocol.md`, `rule-spec-write.md` and `rule-spec-reconcile.md`. The same Grep over `.claude/` printed nothing. These four rules set what the hook and the Spec do with the answer once it is given. The new step comes before the answer and changes none of them, so they stand. A Grep of `(?i)search|grep|count` over `vault/wiki/estimates/estimate-case-build-*.md` printed `estimate-case-build-checks-the-finished-case.md`, `estimate-case-build-writes-the-case.md` and `estimate-case-build-writes-a-plain-round.md`. The hits in the last two are about the agent's tools and the shape of a round, so their Criteria stand. The Criterion of `estimate-case-build-checks-the-finished-case` is replaced whole. Only its line on a claim about a search changes, and the rest is carried word for word. Its `purpose` (what each search printed) and its `method` (a claim of context that its search did not print) still state the promise, which this Case only makes stricter, so both stand.

> **problem:**
> A Case's `context` states files and counts of searches that the searches did not print, because `case-guppi` writes them from its own reading during the build. The instruction to claim nothing a search did not print has failed in three sessions since it was set, and only the pre-spec check catches the fault.

> **recommend:**
> - **How should the fix work?**
>   - Recommended: (a) just before answering with a Case, `case-guppi` runs each search it cites again, exactly as the context writes it, and copies the files or the count from that output; the Criterion of `estimate-case-build-checks-the-finished-case` replaced to match.
>   - Answer: agreed with the recommendation, (a).
> - **Which texts does the fix cover?**
>   - Recommended: (a) Case contexts only; reading and ledger lines stay under the writing rule of `CLAUDE.md`.
>   - Answer: agreed with the recommendation, (a).
> - **Change**
>   - Asked: at pre-spec, on the archive of the Insight's children by the cascade and on the lesson of Case 620 with another cause: (a) name the cascade in `context` and keep the rest as it is, with `context` saying that the four lessons are archived, that the lesson of Case 620 has another cause which this Case does not close, and that the Criterion line of `estimate-case-build-checks-the-finished-case` on searching the rules of the same moment already covers that cause; or (b) take that lesson out of the Insight's `children`. Recommended (a); the person agreed, (a).
>   - Taken: `context` names `estimate-generate-cascades` and the archive of the four children, and says which three children share the cause this Case closes; `given`, `then`, the pairs and the ledger lines are unchanged.
> - **Change**
>   - Asked: at the second pre-spec run, on the lesson of Case 620, whose `root_cause` gives two causes: (a) fix the wording so that `context` says the moment-search line of the Criterion covers the first cause, that no line covers the second (the cascade of a `set` not searched), that this Case does not close it, and that the lesson is archived with the Insight all the same and a recurrence raises it again; or (b) leave it as it is. Recommended (a); the person agreed, (a).
>   - Taken: `context` says so; `given`, `then`, the pairs and the ledger lines are unchanged.

> **given:**
> `rule-case-build` — the instructions of `case-guppi`, its Render
> **＋** `.claude/agents/case-guppi.md` — the agent file rendered from `rule-case-build`
> **＋** `estimate-case-build-checks-the-finished-case` — the check of what `case-guppi` checks before it answers
> **＋** `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — the pattern this Case actions
> **＋** `.claude/agents/ask-guppi.md` — the recipe of the index lines that `case-guppi` reads
> **＋** `vault/wiki/rules/` — the rules searched for the moment a change sets
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the case files of the related Cases of the session
> **＋** `raw/2026-10-04/2245/cases/case-637.md` — Case 637.2 also changes `rule-case-build`, at the moment a Case is sent back for a clash

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
> **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` A claim of `context` about a search names its pattern and the paths it ran over, and lists each file the search printed, a file it does not read included, or gives the count the search printed; it claims nothing the search did not print (case 557.1). ``
>   - new: `` A claim of `context` about a search names its pattern and the paths it ran over, and lists each file the search printed, a file it does not read included, or gives the count the search printed; it claims nothing the search did not print (case 557.1). Just before you answer with the Case, run again each search that `context` names, with the pattern and the paths that `context` writes, and take the files and the counts of `context` from the output of that run, never from the files you read during the build; a file or a count that the run does not print leaves `context` (case 636). ``
>   - change: `case-guppi runs each search its context names again just before it answers, and takes the files and counts from that run (case 636)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — each search the context names is run again just before the answer, and its files and counts come from that run (case 636)`
> - [ ] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`
>   - set: `{status: actioned, addressed_by: decision-case-636}`
>   - change: `actioned: case-guppi runs each search its context names again just before it answers (case 636)`
> - [ ] read `estimate-case-build-checks-the-finished-case`

> **ratification:**
> ```
> - decision[case 636][update][rule-case-build]{ref:rule-case-build}
> - decision[case 636][update][estimate-case-build-checks-the-finished-case]{ref:estimate-case-build-checks-the-finished-case}
> - decision[case 636][update][insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]{ref:insight-workflow-fact-signed-from-a-check-that-does-not-cover-it}
> ```
