## Case 703 — An unlisted tag is stopped where its line is born

> **context:**
> A tag reaches a page from a lesson line, from the `tags` of a `create`, or from a `set` of `tags` in an `update`. No check compares it with `vault/wiki/tags.md`, the list of tags a Case ratified. `register_tags` of `guppi/generate.py` prints a warning that a tag is used but not registered only in the librarian's run, after the page is written. A Grep for `\{tags:[^}]*orchestration` over `vault/raw/2026-10-07/0211/ledger.md` printed a count of 2: two lesson lines carried `orchestration`, which the list does not hold, and the brief flagged it only after the run. Case 702 gave the Case file a tag line that declares a new tag, and its Q2 (a) left this check out. The person chose two checks, one where each line is born. The check of the Case file in `guppi/casecheck.py` sends back a Case whose `create`, `set` of `tags` or decision line carries an unlisted tag, so `case-guppi` declares the tag or picks a listed one before the person sees the Case (Case 703.1). The ledger hook in `guppi/ledger.py` refuses a fresh lesson line with an unlisted tag (Case 703.2). A tag counts as listed when a row of `tags.md` holds it, when a tag line of the same Case file declares it, or when a tag line of a Case of the session with a decision line in the session's ledger declares it. Both checks, and `register_tags`, read the rows through one new module, `guppi/tags.py`. Where `tags.md` does not stand, no tag is judged: the seed of `tests/test_case_schema.py` writes no `tags.md`, and the example Case of `case-schema.md` carries `cart`, `checkout`, `payment` and `performance`. So the example and `estimate-case-protocol-example-passes-the-check` stand. The tags of an Insight that the librarian takes from its lessons are not checked, since the lessons that give them are checked.
>
> Both readers run from the working tree as soon as Work Mode changes them. The text they read, `tags.md`, changes at the librarian's run of this session only by Case 704, which declares `orchestration` by a tag line. That only widens what passes, and once Case 704 is ratified its tag line already counts as declared in this session. A Case that is sent back is fixed by `case-guppi`. A refused lesson line stays in the transcript and is judged again at each `Stop`. In Plan Mode a Case may first declare the new tag. From `/work` to the end of Retro, `rule-orchestration` puts the lesson lines in the one reply that ends Retro, where no Case is ratified. There, by the person's answer to a finding of `/pre-spec`, the lesson takes a tag of `tags.md` and the new tag goes as a line of the handoff to a later session, and the stderr line says so. So a refusal loses no lesson, only its new tag waits for a later session, and no old form is kept. The lesson lines that already stand in a ledger are not fresh and are not judged. Case 704 registers `orchestration`, which `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` carries.
>
> The Criterion of `estimate-case-check-sends-back-a-faulty-case` lists the checks of a file without saying it lists all of them, so it stands, and the new finding is the promise of a new Estimate. `estimate-spec-write-reads-a-new-tag` says that `guppi/casecheck.py` reads the tag line by the same function of `guppi/ratified.py`. Case 703.1 takes the tags declared in the same file from that reading, so the Criterion stays true and stands. Its method, `-k tag` over `tests/test_casecheck.py`, also selects the new tests whose names hold `unlisted_tag`, and they pass when Case 703.1 holds. Among the Estimates of `rule-ledger-write`, `estimate-ledger-write-lifts` says that a line any refusal of the rule refuses does not land. `estimate-ledger-write-refuses-a-lesson-without-its-prefix` says that a line refused for its prefix gets that refusal, and `estimate-ledger-write-refuses-a-line-it-cannot-read` says that a line the grammar does not read gets no other refusal. Case 703.2 judges neither kind of line for its tags, so both Criteria stand. `estimate-ledger-write-refuses-a-mark-with-no-decision-line` says that a line whose mark has a decision line before it is written as before. The other refusals of the hook already stood beside it, and the Criterion of `estimate-ledger-write-lifts` bounds it, so it stands. `estimate-ledger-write-asks-for-the-mark-of-a-lesson` says that an unmarked line lands as it stands when it is written again or stands only in an earlier text, and it lists the lines it does not hold. Case 703.2 keeps a line refused for its tag out, and Case 703.3 says that such a line is not held. So Case 703.3 replaces that Criterion whole, keeps its lines, and adds one line for each, and it sets anew its `purpose`, which states that the line written again is written. `estimate-generate-writes` says that a used and undeclared tag goes to stderr, and that stays true.
>
> Case 711 of this session changes `rule-case-check` and `guppi/casecheck.py` too. Its pairs anchor on other sentences of the Purpose than the sentence that ends with case 688.1, after which Case 703.1 adds its own. Read side by side, the new texts do not contradict each other. The Purpose sentence that the checks of a Case are those of pre-spec and of the Spec hook, imported, not copied, is made false by Case 703.1 too, since the tag check is the hook's own. Case 711.3 rewords that sentence to name the check of the read of the pairs as an exception, and it should name the tag check of Case 703.1 as a second exception. This Case leaves that sentence to Case 711.3, so that two Cases do not change one sentence.

> **problem:**
> A tag that `tags.md` does not hold can reach a page through a lesson line or a Case, and nothing stops it before the librarian's run.

> **recommend:**
> - **Whether a check stops an unlisted tag, and where**
>   - Recommended: (a) two checks: the check of the Case file sends back a `create` with an unlisted tag, and the ledger hook refuses a new lesson line with one; both read the list through one shared function.
>   - Answer: agreed, (a).
> - **Which tags count as listed**
>   - Recommended: (a) a row of `tags.md`, or a tag declared by a `tag` line of a Case of this session.
>   - Answer: agreed, (a).
> - **What happens to a line with an unlisted tag**
>   - Recommended: (a) refuse the line until the tag is fixed: exit 2 with one stderr line, or a finding sent back to `case-guppi`.
>   - Answer: agreed, (a).
> - **Which lines the check covers**
>   - Recommended: (a) lesson lines, `create` lines and a `set` of `tags` in an `update`; the tags of an Insight are left out.
>   - Answer: agreed, (a).
> - **One promise or two**
>   - Recommended: (a) two sub-cases, each with a new Estimate: `estimate-case-check-sends-back-an-unlisted-tag` and `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`.
>   - Answer: agreed, (a).
> - **Which `tag` lines of this session count as declared**
>   - Recommended: (a) a `tag` line in the same Case file, or in a Case of this session that is already approved, a decision line of it standing in the session's ledger.
>   - Answer: agreed, (a).
> - **What the checks do when `tags.md` is missing**
>   - Recommended: (a) no `tags.md`, no tag judged.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: from `/work` to the end of Retro no Case is ratified, so a lesson there takes a tag of `tags.md`, and the new tag goes as a line of the handoff to a later session; the stderr line says so, and `context` no longer claims without that condition that no refusal loses a line.
>   - Taken: the stderr line of Case 703.2 and the new text of `rule-ledger-write` say so, and `context` says that only the new tag waits.

### Case 703.1 — The check of a Case file sends back an unlisted tag

> **given:**
> `rule-case-check`: the rule of the check of the file of a Case, whose Purpose gains the finding.
> **＋** `guppi/casecheck.py`: `check_answer` gives the finding.
> **＋** `guppi/tags.py`: the new module that reads the rows of `tags.md` and the tags that tag lines declare, which `register_tags` of `guppi/generate.py` also uses.
> **＋** `vault/wiki/tags.md`: the list of registered tags.
> **＋** `tests/test_casecheck.py`: the tests of the finding.
> **＋** `estimate-case-check-sends-back-an-unlisted-tag`: the new check of the finding.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `raw/2026-10-07/0636/cases/case-711.md`: Case 711 changes the same hook and other sentences of the Purpose of `rule-case-check`.

> **when:**
> The `SubagentStop` hook `uv run guppi casecheck --subagent` of `guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` whose Case carries a tag in the `tags` of a `create`, in `tags` under the `set` of an `update`, or in a `{tags:...}` block of a decision line of its `ratification`.

> **then:**
> A tag that no row of `vault/wiki/tags.md` holds is a finding of its Case: "case <N>: tag <tag> is not in tags.md: use a tag of tags.md, or declare it by a tag line in this Case."
> **＋** A tag that a `tag` line of the same file declares is no finding.
> **＋** A tag that a `tag` line of another Case of the session declares is no finding when a decision line of that Case stands in the session's ledger; the hook reads that tag line from the text of that Case as the check stored it.
> **＋** `guppi/casecheck.py` and `guppi/generate.py` read the rows of `vault/wiki/tags.md` by one function of `guppi/tags.py`.
> **－** A tag line of a Case of the session with no decision line in the session's ledger does not make a tag listed.
> **－** Where `vault/wiki/tags.md` does not stand, no tag is judged.

> **tasks:**
> - [ ] create `estimate-case-check-sends-back-an-unlisted-tag`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of the file of a Case sends back a Case whose create, set of tags or decision line carries a tag that tags.md does not hold and no tag line of the file or of a ratified Case of the session declares`
>   - method: `uv run pytest tests/test_casecheck.py -k unlisted_tag`
>   - tags: `[hooks, harness, workflow]`
> - [ ] update `rule-case-check`
>   - old: `the Spec hook comparing it at ratification (case 688.1).`
>   - new: `` the Spec hook comparing it at ratification (case 688.1). The check of the file of a Case also sends back a Case whose `create`, `set` of `tags` in an `update` or decision line carries a tag that no row of `vault/wiki/tags.md` holds and that no tag line of the same file, or of a Case of the session with a decision line in the session's ledger, declares, so that an unlisted tag reaches no page through a Case; with no `tags.md` no tag is judged, and the rows are read by `guppi/tags.py`, the one reading that `guppi/ledger.py` and `guppi/generate.py` share (case 703.1). ``
>   - set: `{implementation_ref: [guppi/casecheck.py, guppi/tags.py, tests/test_casecheck.py, .claude/settings.json]}`
>   - change: `the check of the file of a Case sends back a tag that tags.md does not hold and no tag line declares (case 703.1)`
> - [ ] `guppi/tags.py`: `registered_tags` reads the rows of `vault/wiki/tags.md`, empty or None when the file does not stand; `declared_tags` gives the tags of the `new_tags` of a `then` block, read by `read_tasks` of `guppi/ratified.py`; `ratified_tags` gives the tags declared by the stored Cases whose decision line stands in a list of ledger lines; the docstring says that the checks and `generate` share them.
> - [ ] `guppi/casecheck.py`: `check_answer` gives the finding for each tag of a `create`, of a `set` of `tags` and of a `{tags:...}` block of a decision line that `registered_tags`, the tag lines of the answer and `ratified_tags` over the session's ledger do not hold; no finding when `tags.md` does not stand.
> - [ ] `guppi/generate.py`: `register_tags` reads the known rows by `registered_tags` of `guppi/tags.py`.
> - [ ] `tests/test_casecheck.py`: an unlisted tag on a `create`, on a `set` of `tags` and on a decision line is a finding; a tag declared by a tag line of the same file, or of a Case of the session with a decision line in the ledger, is none; a tag declared by a Case with no decision line is a finding; no `tags.md`, no finding.
> - [ ] read `estimate-case-check-sends-back-an-unlisted-tag`

> **ratification:**
> ```
> - decision[case 703.1][create][estimate-case-check-sends-back-an-unlisted-tag]{ref:rule-case-check}{tags:hooks,harness,workflow}
> - decision[case 703.1][update][rule-case-check]{ref:rule-case-check}
> ```

### Case 703.2 — The ledger hook refuses a lesson with an unlisted tag

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, whose Purpose gains the refusal.
> **＋** `guppi/ledger.py`: the hook that refuses the line.
> **＋** `guppi/tags.py`: the module that reads the rows of `tags.md` and the tag lines of the Cases that `guppi/casecheck.py` stored.
> **＋** `vault/wiki/tags.md`: the list of registered tags.
> **＋** `tests/test_ledger.py`: the tests of the refusal.
> **＋** `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`: the new check of the refusal.
> **＋** `rule-orchestration`: lesson lines from `/work` to the end of Retro stand in the one reply that ends Retro.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session whose `{tags:...}` holds a tag.

> **then:**
> A fresh lesson line stays out of the ledger while its `{tags:...}` names something outside `vault/wiki/tags.md`.
> **＋** Such a line lands once this session ratified a Case declaring each such name, the decision line of that Case written earlier or in the same `Stop`.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — tag <tag> is not in tags.md and no ratified Case of this session declares it: write the line again with a tag of tags.md; in Plan Mode a Case may first declare the tag by a tag line, and from /work to the end of Retro the new tag goes as a line of the handoff to a later session."
> **＋** A refused line from an earlier text of the transcript is judged again at every `Stop` without a word, and is written at the first `Stop` where each of its tags is listed.
> **＋** The ledger hook takes its known tags from `guppi/tags.py`, the same source as `guppi/casecheck.py`.
> **－** A line that the hook cannot read, or refuses for its prefix, is not judged for its tags.
> **－** `estimate[...]` and `decision[...]` lines are not judged for their tags, and a line already in the ledger of any session is not judged again.
> **－** In a project with no `vault/wiki/tags.md`, the ledger hook refuses no lesson for its tags.

> **tasks:**
> - [ ] create `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook refuses a fresh lesson line with a tag that tags.md does not hold and no ratified Case of the session declares, and says why only for the reply just finished`
>   - method: `uv run pytest tests/test_ledger.py -k unlisted_tag`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] update `rule-ledger-write`
>   - old: `so a record with a broken opening is not lost unseen (case 695.1).`
>   - new: `` so a record with a broken opening is not lost unseen (case 695.1). It refuses a fresh lesson line whose `{tags:...}` holds a tag that no row of `vault/wiki/tags.md` holds and that no tag line of a Case of the session declares, a decision line of that Case standing in the session's ledger or in the same `Stop`, read by `guppi/tags.py`, the reading the check of `rule-case-check` shares, so that an unlisted tag reaches no page through a lesson; from `/work` to the end of Retro, where no Case is ratified, its stderr line asks for a tag of `tags.md` and for the new tag as a line of the handoff to a later session; with no `tags.md` no tag is judged (case 703.2). ``
>   - set: `{implementation_ref: [guppi/ledger.py, guppi/materialize.py, guppi/gate.py, guppi/casecheck.py, guppi/tags.py, tests/test_ledger.py, tests/test_gate.py, .claude/settings.json]}`
>   - change: `the ledger hook refuses a lesson line with a tag that tags.md does not hold and no ratified Case of the session declares (case 703.2)`
> - [ ] `guppi/ledger.py`: a function beside `refused_lessons` gives each fresh lesson line, not refused for its prefix or its grammar, with a tag that `registered_tags` and `ratified_tags` of `guppi/tags.py` over the session's ledger and the lines of the `Stop` do not hold; `run` keeps it out and prints its stderr line only for the reply just finished; the module docstring says so.
> - [ ] `tests/test_ledger.py`: an unlisted tag in the reply just finished is refused aloud and the other lines land; one in an earlier text is skipped without a word and lands once a ratified Case declares the tag; a tag declared by a Case with a decision line in the ledger or in the same `Stop` passes; a line refused for its prefix gets that refusal alone; no `tags.md`, no refusal.
> - [ ] read `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`

> **ratification:**
> ```
> - decision[case 703.2][create][estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> - decision[case 703.2][update][rule-ledger-write]{ref:rule-ledger-write}
> ```

### Case 703.3 — A lesson refused for its tag is not held for its mark

> **given:**
> `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: its Criterion is replaced whole.
> **＋** `rule-ledger-write`: the rule of the ledger hook.
> **＋** `guppi/ledger.py`: `run` leaves a line refused for its tag out of the lines held for their mark.
> **＋** `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`: the Estimate of the refusal for a tag.
> **＋** `tests/test_ledger.py`: the tests of the hold.
> **＋** `estimate-ledger-write-lifts`: the Estimate of the lines any refusal of the rule keeps out.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: the Estimate of the reminder after the write.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

> **then:**
> At the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
> **＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did a Case of this session fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged."
> **＋** The stderr line names no Case, however many decision lines stand before the lesson line.
> **＋** The line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript.
> **＋** Neither way lands it while another refusal of the hook keeps it out, as `estimate-ledger-write-lifts` sets it.
> **＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
> **－** An unmarked line never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
> **－** The hook holds no lesson line that precedes every decision line of the session, no line it refuses for its prefix or cannot parse, and no line that the ledger of some session already holds.
> **－** Nor is a line held that `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` keeps out.
> **－** The hook never holds a decision line for its `{addresses:...}`: it writes it, and the reminder after the write is `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`.
> **－** A session with no `hi` gets no question. The flag `stop_hook_active` changes nothing here, but when it is set and the transcript is unreadable, the hook lets the line land as it stands.

> **tasks:**
> - [ ] update `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the ledger hook holds once a lesson line with no addressed_by mark written after a decision line of the session, asks for the mark, and then writes the line written again unless another refusal of the hook keeps it out
>     ```
>   - change: `the Criterion replaced whole — a line refused for a tag outside tags.md is not held for its mark and does not land (case 703.3)`
> - [ ] `guppi/ledger.py`: `run` passes the lines refused for their tags to `unmarked_lessons` beside those refused for their prefix, so they are not held; the module docstring says so.
> - [ ] `tests/test_ledger.py`: an unmarked lesson refused for its tag after a decision line is not held for its mark and does not land when written again; an unmarked lesson with listed tags is held as before.
> - [ ] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`

> **ratification:**
> ```
> - decision[case 703.3][update][estimate-ledger-write-asks-for-the-mark-of-a-lesson]{ref:rule-ledger-write}
> ```
