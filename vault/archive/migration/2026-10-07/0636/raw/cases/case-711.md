## Case 711 — The check of a Case file reads its edit pairs against the session and the reads of case-guppi

> **context:**
> An edit pair is the old and the new words that a Case signs to change a page: a `replace` changes one place, a `reword` changes a word on every live page. Today the `SubagentStop` check of a Case file runs `judge` of `guppi/prespec.py` over the Cases of the file alone, so `check_pairs` looks for each old text on the page as it stands on disk. Only `/pre-spec` applies the pairs of every Case of the session in order. No script looks at two Cases whose pairs change one sentence while both still match, and no script checks that `case-guppi` read the sentence around a match, though `case-schema.md` asks for that read (case 353). `insight-workflow-edit-pair-signed-from-a-grep-fragment` names both gaps. Case 351 set it `actioned` with the simulation at `/pre-spec`, and `lesson-case-build-related-cases-same-sentence-missed` reopened it: two Cases of session 0104 changed one sentence of `rule-orchestration` so that it named one reply twice, and only `/pre-spec` found it, after the person had approved both. The person asked whether the check could be made by a script, and chose three checks in the hook, each a sub-case with its own Estimate. Case 711.1 applies the pairs of the other Cases of the session first and those of the file last, by `check_pairs`, imported. Case 711.2 sends a note once when a pair of the file changes a sentence that a pair of another Case wrote into. Case 711.3 sends back a pair whose sentence came back whole from no `Read` call of `case-guppi`, and sets the Insight `actioned`. A sentence runs to a full stop followed by a space and a capital letter, or to the end of its paragraph, by one function that 711.2 and 711.3 share. Pairs of the file's own Cases in one sentence give no note, since `case-guppi` already reads the new texts of its own sub-cases side by side by its instructions, and the person's choice named another Case.
>
> `estimate-prespec-simulates-the-pairs` checks the run at `/pre-spec`, which does not change, so its Criterion stands; its line that the meaning of the words is not judged by a machine stays true, since a note judges no meaning. `estimate-case-check-sends-back-a-faulty-case` says that `judge` runs over the Cases of the file, which stays true: 711.1 replaces only its pair findings on the Cases of the file by those of the run in session order, so an old text that matches only after another Case's pair is no longer a wrong finding. `estimate-case-check-sends-back-a-clash-with-another-case` judges clashes by `check_same_target`, and says nothing of pairs, so it stands. The notes of 711.2 go where the notes of `estimate-case-check-notes-a-criterion-line-not-carried` go, and that Criterion speaks only of its own note, so it stands. The test of `estimate-case-protocol-example-passes-the-check` calls the check of `guppi/casecheck.py` with no record of an agent, so 711.3 judges no read there, the example gets no finding, and that Criterion stands. When the read shows that a pair holds, `case-guppi` changes no line and answers with the summary again. The Criterion of `estimate-case-build-writes-the-case` speaks of the lines that change, so it stands. With the Insight `actioned`, the cascade of `estimate-generate-cascades` archives its `clustered` child at the librarian's run; the lesson is of another session, so no decision line carries `{addresses:...}`.
>
> The sentence of the Purpose of `rule-case-check` that the checks of a Case are those of pre-spec and of the Spec hook becomes false with the read check, and 711.3 changes it. A Grep `checks of a Case are the ones of pre-spec` over the repository with the glob `!vault/{raw,archive}/**` printed `vault/wiki/rules/rule-case-check.md` alone. A Grep `SubagentStop` over `vault/wiki/rules/` printed `rule-orchestration.md`, `rule-case-check.md`, `rule-case-protocol.md`, `rule-hook-registry.md` and `rule-spec-reconcile.md`, and over `.claude/` printed `.claude/settings.json`. `rule-orchestration` and `rule-spec-reconcile` name the hook and the file it checks, `rule-hook-registry` registers it, and `rule-case-protocol` says the example passes the check, which stays true as above; all stand. `.claude/settings.json` registers only `uv run guppi casecheck --subagent` on `SubagentStop`. Case 703.1 of this session adds a finding of an unlisted tag to the same hook and changes `rule-case-check` with a pair on the sentence that ends with case 688.1. The pairs of this Case anchor on other sentences of that Purpose, and this Case covers pairs only. The two Cases still meet on the sentence that the checks of a Case are those of pre-spec and of the Spec hook: the tag finding of 703.1 reads `tags.md` through `guppi/tags.py` and is no check of either, so 711.3 names it there as a second exception beside the read check. 703.1 sets `implementation_ref` of the page, which this Case leaves alone. `estimate-prespec-catches-an-indent-added-twice` says that the hook of `rule-case-check` runs `judge` over an answer and sends back a pair that adds an indent twice. Under 711.1 that finding of the answer comes from the run in session order instead of from `judge`, and `check_pairs` still gives it, so the hook still sends the Case back and that Criterion stands; 711.2 adds a record of spans to `check_pairs` and changes none of its findings. A finding of 711.3, or a note of 711.2, may name a Case of the session that the prompt of `case-guppi` did not name, such as a `reword` that hits a page the item does not name. `rule-case-build` lets `case-guppi` read only the case files of the Cases its prompt names, so it could not clear such a finding. So Case 711.4 lets it read the case file of a Case that the check of its file names in a finding or a note. It replaces the Criterion of `estimate-case-build-checks-the-finished-case`, whose line on the Cases it reads says no other Case, and sets its `purpose` anew, since the `purpose` lists the Cases its prompt names; its `method` counts the clashes with a Case named in the prompt, which stays true, so it stands. Case 705.1 of this session changes the paragraph of `rule-case-build` on the drop of a Case, and 711.4 changes the sentence on related Cases in the paragraph of the checks before the summary, so the two pairs do not touch one sentence. The rendered `case-guppi.md` changes at the librarian's render, while the hook runs from the working tree at once: in the Work Mode of this session a Case built again could be sent back for a part written by a Case its prompt does not name, and it stays unshown until that file is read; no line is lost, so no old form is kept. The `addressed_by` of the Insight stands bare, `decision-case-711.3`, because the check of this file refused the quoted wikilink with `case 711.3: [[decision-case-711.3]] outside a code span names no page`, the Decision page not standing before the librarian's run. The person chose the bare form in that case. The Criterion that 711.4 writes changes on purpose one line of the old one, the line on the case files it reads, which the check noted as not carried. The new line adds the Cases that a finding or a note of the check names, and every other line is carried word for word. The hook runs from the working tree as soon as Work Mode changes it, and the writer, `case-guppi`, does not change. A pair sent back is fixed by `case-guppi`, so no refusal loses a line and no old form is kept. The check noted that two `then` lines of 711.3 share most of their words with a `then` line of 711.2. Both sub-cases speak of the sentence around a match of a pair of the file and of text another Case's pair wrote, but 711.2 promises a note on such a sentence and 711.3 promises a finding when it was not read, so the lines stay in both.

> **problem:**
> A pair is signed against the page as it stands, not as the earlier Cases of the session leave it, and nothing makes `case-guppi` read the sentence around a match or the new text of another Case in the same sentence. The fault is found at `/pre-spec`, after the person approved the Case.

> **recommend:**
> - **Should the check of a Case file apply the other Cases' pairs first?**
>   - Recommended: (a) apply the other Cases' pairs first and those of the file last, by `check_pairs`, so an old text that then misses or matches twice goes back to `case-guppi`.
>   - Answer: agreed, (a).
> - **What happens when two Cases change the same sentence?**
>   - Recommended: (a) a note sent back once, naming the other Case, the page and the start of the sentence; a sentence runs to a full stop followed by a space and a capital letter, or to the end of its paragraph.
>   - Answer: agreed, (a).
> - **Should my own instructions repeat the rule on reading the whole sentence?**
>   - Recommended: (c) a script checks the read: a pair whose sentence came back whole from no read of the page file in the record of `case-guppi` goes back to it; a search result does not count.
>   - Answer: agreed, (c), after the person asked whether the check could be made by a script.
> - **One promise or three?**
>   - Recommended: (a) three sub-cases, each with a new Estimate read by `tests/test_casecheck.py`.
>   - Answer: agreed, (a).
> - **Does the read check cover a word swapped across the vault too?**
>   - Recommended: (a) both `replace` and `reword`, every match.
>   - Answer: agreed, (a).
> - **What counts as a read when my old words stand in another Case's new text?**
>   - Recommended: (a) a read of the other Case's file whose output holds that Case's new text.
>   - Answer: agreed, (a).
> - **What happens to the item's page once these checks are approved?**
>   - Recommended: (a) the same Case sets it `actioned`, its decision named as the one that acted on it.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the findings of `/pre-spec`. Name the tag check of Case 703.1 as a second exception where the Purpose of `rule-case-check` says the checks of a Case are those of pre-spec and of the Spec hook. Write `addressed_by` as a quoted wikilink, as `rule-insights-schema` sets it, unless the check of the Case file refuses a link to a decision of this session. Let `case-guppi` read the case file of a Case that the check of its file names in a finding or a note, by an update of `rule-case-build` (the person agreed, option (a)). Name `estimate-prespec-catches-an-indent-added-twice` and say why it stands. Confirm or fix the notes on the `then` lines that 711.3 shares with 711.2.
>   - Taken: 711.3 names the tag check in its new wording, and its `given` names `case-703.md`. `addressed_by` stays bare, since the check refused the quoted wikilink, and the `context` gives the refusal. The new Case 711.4 updates `rule-case-build` and replaces the Criterion of `estimate-case-build-checks-the-finished-case`. The `context` names the indent Estimate and says why it stands. The shared `then` lines stay, and the `context` says why. The finding of 711.3 also names the file of the other Case.

### Case 711.1 — The check of a Case file applies the pairs of the session in order

> **given:**
> `rule-case-check`: the rule of the check of the file of a Case, whose Purpose gains the run in session order.
> **＋** `guppi/casecheck.py`: `check_answer` and `other_blocks` give the other Cases of the session.
> **＋** `guppi/prespec.py`: `check_pairs` applies the pairs in order.
> **＋** `tests/test_casecheck.py`: the tests of the run.
> **＋** `<plan>.checked.json`: the store of the checked Cases of the session, beside the plan file.
> **＋** `estimate-case-check-applies-the-pairs-of-the-session-in-order`: the new check of the run.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `raw/2026-10-07/0636/cases/case-703.md`: Case 703.1 adds another finding to the same hook.

> **when:**
> The `SubagentStop` hook `uv run guppi casecheck --subagent` of `guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` whose Case carries a `replace` or `reword` pair, while the plan file of the session or `<plan>.checked.json` holds other Cases of the session.

> **then:**
> The hook applies the `replace` and `reword` pairs of the other Cases of the session first, in the order `other_blocks` gives them, and the pairs of the Cases of the file last, to copies of the pages in memory, by `check_pairs` of `guppi/prespec.py`, imported; nothing is written to disk.
> **＋** An old text of a Case of the file that then misses, or hits more than once, is a finding of that Case in the words `check_pairs` gives it.
> **＋** An old text of a Case of the file that hits once only after a pair of another Case is no finding, though the page on disk does not hold it.
> **－** A finding of that run that opens with another Case is no finding of the file.
> **－** The other Cases are those `other_blocks` gives: a dropped Case, a Case a `{supersedes:case N}` mark names, a stored Case with findings and the family of a Case of the file are not among them.
> **－** With no other Case of the session, the pairs are judged against the pages on disk as before.

> **tasks:**
> - [ ] create `estimate-case-check-applies-the-pairs-of-the-session-in-order`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of the file of a Case applies the pairs of the other Cases of the session first and those of the file last, and sends back an old text of the file that then misses or hits more than once`
>   - method: `uv run pytest tests/test_casecheck.py -k session_pairs`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-case-check`
>   - old: `` goes back to `case-guppi` before the person first sees it (case 629.1). ``
>   - new: `` goes back to `case-guppi` before the person first sees it (case 629.1). The check of the file of a Case also applies the `replace` and `reword` pairs of the other Cases of the session first and those of the file last, to copies of the pages in memory by `check_pairs` of `guppi/prespec.py`, so an old text that a Case of the session already rewrote, or that then matches twice, goes back to `case-guppi` before the person approves the Case, not at `/pre-spec` (case 711.1). ``
>   - change: `the check of the file of a Case applies the pairs of the session in order, those of the file last (case 711.1)`
> - [ ] `guppi/casecheck.py`: `check_answer` runs `check_pairs` over the blocks of `other_blocks` and then those of the answer, keeps the findings that open with a Case of the answer, and leaves out the pair findings of `judge` on the answer that the run of the answer alone gives; the module docstring says so.
> - [ ] `tests/test_casecheck.py`: an old text that another Case of the plan or the store rewrote is a finding; an old text that hits only after another Case's pair is none; a miss between two other Cases is none; a dropped Case and a Case a mark retires are not applied.
> - [ ] read `estimate-case-check-applies-the-pairs-of-the-session-in-order`

> **ratification:**
> ```
> - decision[case 711.1][create][estimate-case-check-applies-the-pairs-of-the-session-in-order]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 711.1][update][rule-case-check]{ref:rule-case-check}
> ```

### Case 711.2 — The check of a Case file notes a sentence that two Cases change

> **given:**
> `rule-case-check`: the rule of the check of the file of a Case, whose Purpose gains the note.
> **＋** `guppi/casecheck.py`: `check_answer` gives the note.
> **＋** `guppi/prespec.py`: `check_pairs` records the text each pair writes, and one function gives the sentence around a place.
> **＋** `guppi/generate.py`: `replace_hits` and `reword_text` find the places a pair changes.
> **＋** `tests/test_casecheck.py`: the tests of the note.
> **＋** `<plan>.checked.json`: the store of the checked Cases of the session, which keeps the notes sent.
> **＋** `estimate-case-check-notes-a-sentence-two-cases-change`: the new check of the note.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.

> **when:**
> The `SubagentStop` hook `uv run guppi casecheck --subagent` of `guppi/casecheck.py` applies the pairs of the other Cases of the session and then those of a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `check_pairs` of `guppi/prespec.py`.

> **then:**
> `check_pairs` records the text that each pair writes into a page, with the Case of the pair.
> **＋** The sentence around a place runs back to the last full stop before it that a space and a capital letter follow, or to the start of its paragraph, and on to the next such full stop or to the end of its paragraph, by one function of `guppi/prespec.py`.
> **＋** When the sentence around the match of a pair of a Case of the file holds text that a pair of another Case of the session wrote, the hook gives a note of the Case of the file that names the other Case, the page and the opening of the sentence: "case <N>: <slug>: a pair changes a sentence that case <M> changes too: <opening>: read both new texts side by side, and fix the pair or say in context why the two fit."
> **＋** The note goes where a note of a Criterion line not carried goes: it is sent back once by exit 2 beside any findings, stored under `notes` in `<plan>.checked.json`, and not sent again for the same Case id.
> **－** The note is no finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` does not refuse a showing for it.
> **－** Two pairs of the Cases of the file in one sentence give no note, and neither do two pairs of other Cases.
> **－** `uv run guppi prespec --check` does not print the note.

> **tasks:**
> - [ ] create `estimate-case-check-notes-a-sentence-two-cases-change`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of the file of a Case sends a note once when a pair of the file changes a sentence into which a pair of another Case of the session wrote`
>   - method: `uv run pytest tests/test_casecheck.py -k shared_sentence`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-case-check`
>   - old: `([[insight-case-form-chat-form-read-by-no-script]]).`
>   - new: `` ([[insight-case-form-chat-form-read-by-no-script]]). When a pair of the file changes a sentence into which a pair of another Case of the session wrote, the check sends `case-guppi` a note once that names the other Case, the page and the sentence, so the two new texts are read side by side before the person sees the Case (case 711.2). ``
>   - change: `the check of the file of a Case notes a sentence that a pair of the file and a pair of another Case change (case 711.2)`
> - [ ] `guppi/prespec.py`: one function gives the sentence around a place of a section; `check_pairs` records the span each pair writes and its Case, by `replace_hits` and the word pattern of `reword_text` of `guppi/generate.py`, imported, and gives the note for a pair of a Case named as the answer's; its docstring says so.
> - [ ] `guppi/casecheck.py`: `check_answer` adds the notes of the run of 711.1 to the notes of the Cases of the answer; the module docstring says so.
> - [ ] `tests/test_casecheck.py`: a pair of the answer in a sentence another Case wrote into is a note, sent once; a pair in another sentence of the same paragraph is none; two pairs of the answer in one sentence are none; the note is no finding.
> - [ ] read `estimate-case-check-notes-a-sentence-two-cases-change`

> **ratification:**
> ```
> - decision[case 711.2][create][estimate-case-check-notes-a-sentence-two-cases-change]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 711.2][update][rule-case-check]{ref:rule-case-check}
> ```

### Case 711.3 — The check of a Case file sends back a pair whose sentence was not read

> **given:**
> `rule-case-check`: the rule of the check of the file of a Case, whose Purpose gains the read check.
> **＋** `guppi/casecheck.py`: the hook reads the `Read` calls of the subagent and gives the finding.
> **＋** `guppi/prespec.py`: the function of the sentence around a place, and `check_pairs`, which records the text each pair writes.
> **＋** `tests/test_casecheck.py` and `tests/test_case_schema.py`: the tests of the read check, and the test that runs the check over the example of `vault/wiki/case-schema.md` with no record of an agent.
> **＋** `raw/2026-10-07/0636/cases/case-703.md`: Case 703.1 adds the tag check to the same Purpose.
> **＋** `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read`: the new check of the read.
> **＋** `insight-workflow-edit-pair-signed-from-a-grep-fragment`: the pattern this Case acts on.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case, and the file of another Case of the session.

> **when:**
> The `SubagentStop` hook `uv run guppi casecheck --subagent` of `guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` whose Case carries a `replace` or `reword` pair on a page that stands on disk, and reads the record of the subagent at `agent_transcript_path`.

> **then:**
> For each match of each pair of the Cases of the file — the one match of a `replace`, and each match of a `reword` on each live page — the hook takes the sentence around it on the page as the earlier pairs leave it, by the function of the sentence of `guppi/prespec.py`.
> **＋** The sentence counts as read when each part of it that no pair wrote stands whole in the outputs of the `Read` calls of the subagent on the page file, the line numbers of the output and the whitespace set aside.
> **＋** A part of the sentence that a pair of another Case of the session wrote counts as read when it stands whole in the outputs of the `Read` calls of the subagent on the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of that Case.
> **＋** A sentence not read is a finding of its Case: "case <N>: <slug>: the sentence around a pair was not read whole: <opening>: Read the page around it, and the file of each other Case that wrote into it, and check the pair."
> **－** The output of a `Grep` call, or of any other tool than `Read`, is no read.
> **－** A part of the sentence that a pair of the Cases of the file wrote is not judged.
> **－** A transcript the hook cannot read, and a call of the check with no record of an agent, such as `tests/test_case_schema.py` over the example of `vault/wiki/case-schema.md`, judge no read.

> **tasks:**
> - [ ] create `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of the file of a Case sends back a pair whose sentence around a match no Read call of case-guppi on the page file, or on the file of the other Case that wrote into it, returned whole`
>   - method: `uv run pytest tests/test_casecheck.py -k unread_sentence`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-case-check`
>   - old: `imported, not copied ([[rule-one-judgment-one-implementation]]),`
>   - new: `` imported, not copied ([[rule-one-judgment-one-implementation]]), but for the check of the read of its pairs set out below and the check of a tag that `vault/wiki/tags.md` does not hold set out at the end of this text, ``
>   - old: `the person judges the text (cases 449, 537).`
>   - new: `` the person judges the text (cases 449, 537). The check of the read of its pairs is the hook's own, since only the hook reads the record of the calls of `case-guppi`: a pair whose sentence around a match came back whole from no `Read` call on the page file, or, for the words that another Case's pair wrote into it, on the file of that Case, goes back to `case-guppi`, and the output of a search is no read, so that no pair is signed from the line a search printed (case 711.3). ``
>   - change: `the check of the file of a Case sends back a pair whose sentence no Read call of case-guppi returned whole (case 711.3)`
> - [ ] update `insight-workflow-edit-pair-signed-from-a-grep-fragment`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-711.3
>     ```
>   - change: `actioned: the check of the file of a Case applies the pairs of the session in order, notes a sentence two Cases change, and sends back a pair whose sentence case-guppi did not read (case 711)`
> - [ ] `guppi/casecheck.py`: a function reads the outputs of the `Read` calls of the subagent in `agent_transcript_path`, by the tool use and its tool result, keyed by the file, paths compared after they are resolved; `check_answer` takes them, None when the transcript cannot be read, and gives the finding for each sentence not read; the module docstring says so.
> - [ ] `tests/test_casecheck.py`: a pair whose sentence a `Read` output holds passes; one whose sentence only a `Grep` output holds is a finding; a `reword` match on a page not read is a finding; a part another Case wrote passes only with a read of that Case's file; a part the answer wrote is not judged; no transcript, no finding.
> - [ ] read `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read`

> **ratification:**
> ```
> - decision[case 711.3][create][estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 711.3][update][rule-case-check]{ref:rule-case-check}
> - decision[case 711.3][update][insight-workflow-edit-pair-signed-from-a-grep-fragment]{ref:insight-workflow-edit-pair-signed-from-a-grep-fragment}
> ```

### Case 711.4 — case-guppi reads the file of a Case that the check of its file names

> **given:**
> `rule-case-build`: its Render, the agent file of `case-guppi`, lets it read the file of a Case that a finding or a note names.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `estimate-case-build-checks-the-finished-case`: its Criterion is replaced whole and its `purpose` set anew.
> **＋** `.claude/agents/ask-guppi.md`: the recipe of the index lines that `case-guppi` reads.
> **＋** `vault/wiki/rules/` and `.claude/`: the rules and the harness searched for the moment a change sets.
> **＋** `rule-case-check`: the check of the file of a Case, whose findings and notes name another Case.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the case files of the Cases of the session.
> **＋** `raw/2026-10-07/0636/cases/case-705.md`: Case 705.1 changes the paragraph of `rule-case-build` on the drop of a Case.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
> **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and of each Case of the session that the check of `rule-case-check` names in a finding or a note on its file, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
> **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
> **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
> **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `Read the case file of each Case of the session that the caller's prompt names, and no other Case of the session:`
>   - new: `Read the case file of each Case of the session that the caller's prompt names, and the case file of each Case of the session that the check of your file names in a finding or a note (case 711.4), and no other Case of the session:`
>   - change: `case-guppi reads the case file of a Case of the session that the check of its file names in a finding or a note (case 711.4)`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, the Cases of the session its prompt names or the check of its file names in a finding or a note, the purpose and method of an Estimate whose Criterion it replaces, what each search printed and that the context keeps only the searches the Case rests on, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec"
>     ```
>   - change: `the Criterion replaced whole — case-guppi also reads the case file of a Case that the check of its file names in a finding or a note; purpose set anew (case 711.4)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-checks-the-finished-case`

> **ratification:**
> ```
> - decision[case 711.4][update][rule-case-build]{ref:rule-case-build}
> - decision[case 711.4][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}
> ```
