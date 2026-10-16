## Case 827 — A lesson line declares its own new tag

> **context:**
> A tag is a short label on a page. `vault/wiki/tags.md` lists each tag with its meaning and its Russian aliases, and `ask-guppi` maps a Russian question to tags by those aliases. Three guards keep a new tag out until a Case is ratified, read in the code. The ledger hook refuses a fresh lesson line whose tag `tags.md` does not hold and no tag line of a Case ratified in the session declares (`refused_tags` and `tag_message` of `.guppi/guppi/ledger.py`, case 703.2). The check of a Case file sends back a Case that uses such a tag without a tag line (`unlisted_tags` of `.guppi/guppi/casecheck.py`, case 703.1). `tags.md` gains a row only from the `new_tags` of the Spec, by `register_tags` of `.guppi/guppi/generate.py`, and its header says a tag enters only after a Case ratified it. Lessons are mostly written at Retro, where no Case is ratified, so the refusal message sends the tag to the handoff of a later session; at the Retro of session 1739 two lessons lost the tags `retro` and `box` that way, and Case 826 of this session adds them. The person agreed that a lesson line may declare its new tag itself by a block `{newtag:<tag>|<meaning>|<aliases>}`, which the ledger hook accepts and the librarian's run registers; that the check of a Case file stays; that the one rule names this exception; and that the header of `tags.md` changes by a one-off task by hand, with the exception written into every text that makes the script the only writer to `vault/wiki/`.
>
> The block is read once, by `parse_line` of `.guppi/guppi/materialize.py`: both the ledger hook (`refused_tags`) and the lift of `materialize` call that function today for a lesson line, so the two sides share one reading; a Grep of `newtag` over `.guppi/` printed 0 occurrences, so no other reading of the block exists. Until Work Mode changes the code, `parse_line` passes the new block by, so a line with it is refused for its tag as today and judged again at each `Stop`; no line is lost. A Grep of `the new tag goes as a line of the handoff` over the repository outside `vault/raw/` printed `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag.md`, `.guppi/tests/test_ledger.py`, `.guppi/guppi/ledger.py` and three files of `vault/archive/migration/2026-10-07/0636/raw/` (`materialize.yaml`, `spec.md`, `cases/case-703.md`); the first three change in Case 827.1, and the archived ones are records of their session and stand. A Grep of `only writer` over `.claude/`, `vault/wiki/` and `CLAUDE.md` printed `glossary.md`, `librarian-guppi.md`, `log.md`, `rule-page-generation.md`, `entity-glossary.md` and `rule-documentation.md`; `log.md` is a record and is not read, `glossary.md` and `librarian-guppi.md` are renders of the pages Case 827.4 changes, and `rule-vault-layout` says the same in other words (No file of `wiki/` is written by hand). A Grep of `registry of tags` over `vault/wiki/` printed `tags.md`, `glossary.md`, `entity-glossary.md` and `rule-vault-layout.md`, each changed in Case 827.4. The hand edit of the header runs in Work Mode, before the librarian's run writes the exceptions of Case 827.4 into `rule-vault-layout` and `rule-page-generation`; at that moment it rests on `rule-case-build`, which says that a page or a rendered file changes at the librarian's run or the render, or earlier only by a one-off task by hand in Work Mode that a Case names.
>
> These stand: `rule-case-check` and `estimate-case-check-sends-back-an-unlisted-tag`, since the person kept the check of a Case file; the sentence of `rule-case-protocol` and `case-schema.md` on how a Case declares a new tag, and the tag line of `rule-spec-write`, which speak of a Case and claim no other way is closed; `estimate-generate-writes`, whose Criterion says a tag of `new_tags` lands in `tags.md` whatever wrote it there; `estimate-materialize-assembles`, whose line on `new_tags` speaks of Cases; `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, which names the refusal by slug; `estimate-ratification-loaded`, whose `uv run --project .guppi guppi render --check` covers the new sentences of `ratification.md`; the aliases line of `.claude/agents/ask-guppi.md`; the merge sentence of `.claude/skills/merge-main/SKILL.md`, which speaks of what a merge writes; and the context of Case 826, which states the guard as it stood. `.guppi/tests/test_ledger.py` asserts the old words of the refusal, so Case 827.1 changes that test. The new Criterion of `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` keeps each line of the old one but two, which change on purpose: the words of the refusal, and the line on a refused line from an earlier text, which now also lands once its tag is declared. `.guppi/tests/test_guppi_package.py` reads the live pages and every file under `.claude/` for `uv run guppi`, `uv run pytest`, `guppi/` and `tests/`; the new texts write those paths only as `.guppi/guppi/` and `.guppi/tests/`, which its pattern does not match, so it stands. By the person's answer, Case 827.4 creates no Estimate: `estimate-glossary-terms-defined` reads that each row of the glossary agrees with the page it points to, which covers its rows Ratification, Working files and Librarian against `rule-ratification`, `rule-vault-layout` and `rule-documentation`; its Criterion stands, since it already speaks of that agreement, and the header of `tags.md` and the sentences of `rule-vault-layout`, `rule-page-generation` and `rule-documentation` are read by no Estimate.

> **problem:**
> A lesson that needs a new tag cannot have it where most lessons are written: from `/work` to the end of Retro no Case is ratified, so the ledger hook refuses the line, and the tag waits for a Case of a later session.

> **recommend:**
> - **How may a new tag enter outside a Case**
>   - Recommended: (a) a lesson line declares its new tag with its meaning and Russian aliases; the librarian's run registers it, and the one rule and the header of `tags.md` name this way.
>   - Answer: agreed, (a).
> - **Does the check of a Case file change too**
>   - Recommended: (a) the check of a Case file stays; a Case still declares a new tag by a tag line.
>   - Answer: agreed, (a).
> - **How a lesson line writes its new tag**
>   - Recommended: (a) one block `{newtag:<tag>|<meaning>|<aliases>}` per new tag, the tag also in `{tags:...}`, read by `parse_line`.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) three sub-cases: the ledger hook with the Criterion of `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` replaced, the lift with a new Estimate, and the texts with the Criterion of `estimate-ratification-ledger-line-form` replaced.
>   - Answer: agreed, (a).
> - **How the header of `tags.md` changes**
>   - Recommended: (a) a one-off edit by hand in Work Mode, and an exception for that header alone in the pages that make the script the only writer.
>   - Answer: agreed, (a).
> - **Where the exception for the header of `tags.md` is written**
>   - Recommended: (a) a fourth sub-case writes it into `rule-vault-layout`, `rule-page-generation`, `rule-documentation` and `entity-glossary`.
>   - Answer: agreed, (a).
> - **How the fourth sub-case is checked**
>   - Recommended: (a) a new Estimate on `rule-vault-layout`, read by hand after the librarian's run.
>   - Answer: (b) no new Estimate; `estimate-glossary-terms-defined` checks it.
> - **Change**
>   - Asked: a finding of `/pre-spec`: the hand edit of the header of `tags.md` runs in Work Mode, before the exceptions of Case 827.4 land; `context` should name the sentence of `rule-case-build` that allows it at that moment.
>   - Taken: `context` names that sentence of `rule-case-build`; nothing else changed.

### Case 827.1 — The ledger hook writes a lesson whose new tag a lesson line declares

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, whose Purpose names the refusal of an unlisted tag.
> **＋** `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/ledger.py`: the hook, `refused_tags` and `tag_message`.
> **＋** `.guppi/guppi/tags.py`: the one reading of the listed tags.
> **＋** `.guppi/guppi/materialize.py`: `parse_line`, the one reading of a ledger line.
> **＋** `.guppi/guppi/casecheck.py`: the check of a Case file, which reads the same tags.
> **＋** `.guppi/tests/test_ledger.py`: the tests of the refusal.
> **＋** `vault/wiki/tags.md`: the registry of tags.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session whose `{tags:...}` holds a tag.

> **then:**
> A fresh lesson line stays out of the ledger while its `{tags:...}` names something outside `vault/wiki/tags.md`.
> **＋** Such a line lands once this session ratified a Case declaring each such name, the decision line of that Case written earlier or in the same `Stop`.
> **＋** Such a line lands when a `{newtag:<tag>|<meaning>|<aliases>}` block declares each such tag, on the line itself or on a lesson line of the session's ledger or of the same `Stop`.
> **＋** A block declares its tag only when that tag stands in the `{tags:...}` of its line and its meaning and aliases are not empty, as `parse_line` of `.guppi/guppi/materialize.py` reads it.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — tag <tag> is not in tags.md and nothing of this session declares it: write the line again with a tag of tags.md, or declare the tag on the line by {newtag:<tag>|<meaning>|<aliases>}, the tag also in its {tags:...}."
> **＋** A refused line from an earlier text of the transcript is judged again at every `Stop` without a word, and is written at the first `Stop` where each of its tags is listed or declared.
> **＋** The ledger hook takes its known tags from `.guppi/guppi/tags.py`, the same source as `.guppi/guppi/casecheck.py`.
> **－** A line that the hook cannot read, or refuses for its prefix, is not judged for its tags.
> **－** The blocks of such a line declare no tag.
> **－** `estimate[...]` and `decision[...]` lines are not judged for their tags, and a line already in the ledger of any session is not judged again.
> **－** In a project with no `vault/wiki/tags.md`, the ledger hook refuses no lesson for its tags.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `` so that an unlisted tag reaches no page through a lesson; from `/work` to the end of Retro, where no Case is ratified, its stderr line asks for a tag of `tags.md` and for the new tag as a line of the handoff to a later session; with no `tags.md` no tag is judged (case 703.2). ``
>   - new: `` so that an unlisted tag reaches no page through a lesson; a `{newtag:<tag>|<meaning>|<aliases>}` block of the line itself, or of a lesson line of the session's ledger or of the same `Stop`, declares the tag too, read by `parse_line` of `.guppi/guppi/materialize.py`, when the tag stands in the `{tags:...}` of its line and its meaning and aliases are not empty, so that a lesson brings its new tag with its meaning and aliases at any phase; its stderr line asks for a tag of `tags.md` or for that block; with no `tags.md` no tag is judged (as set in case 703.2, and in case 827.1). ``
>   - change: `a newtag block of a lesson line declares a new tag for the ledger hook (case 827.1)`
> - [ ] update `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the ledger hook refuses a fresh lesson line with a tag that tags.md does not hold and that neither a ratified Case of the session nor a newtag block of a lesson line declares, and says why only for the reply just finished
>     ```
>   - change: `the Criterion replaced whole — a newtag block of a lesson line declares a tag (case 827.1)`
> - [ ] `.guppi/guppi/materialize.py`: `parse_line` gives a lesson record `new_tags`, one entry of `tag`, `meaning` and `aliases` per `{newtag:<tag>|<meaning>|<aliases>}` block before `trigger:` whose tag stands in the line's `{tags:...}` and whose meaning and aliases are not empty; its docstring says so.
> - [ ] `.guppi/guppi/tags.py`: `lesson_tags` gives the tags of the `new_tags` of the lesson records it is given; the module docstring names it.
> - [ ] `.guppi/guppi/ledger.py`: `refused_tags` adds to the listed tags `lesson_tags` of the records of the session's ledger and of the fresh lines not in `skip`; `tag_message` gives the new stderr line; the module docstring says so.
> - [ ] `.guppi/tests/test_ledger.py`: `test_unlisted_tag_in_the_finished_reply_is_refused_aloud_and_the_rest_lands` asserts the new words in place of the words of the handoff; new tests named `test_unlisted_tag_...`: a tag declared on the line itself lands; a tag declared on a lesson line of the session's ledger lands; a block whose tag is not in the `{tags:...}` of its line, or whose aliases are empty, declares nothing; a block on a line refused for its prefix declares nothing.
> - [ ] read `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`

> **ratification:**
> ```
> - decision[case 827.1][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 827.1][update][estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag]{ref:rule-ledger-write}
> ```

### Case 827.2 — materialize lifts the tag a lesson line declares

> **given:**
> `rule-materialize`: the rule of the lift, whose Purpose names what a lesson line carries.
> **＋** `estimate-materialize-lifts-a-tag-of-a-lesson`: the new check of the lift of the block.
> **＋** `.guppi/guppi/materialize.py`: the lift and `parse_line`.
> **＋** `.guppi/tests/test_materialize.py`: the tests of the lift.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of a unit, which holds the lesson line.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the unit, whose Cases declare tags by tag lines.
> **＋** `raw/<date>/<hi HHMM>/materialize.yaml`: the yaml whose `new_tags` gains the tag.

> **when:**
> `uv run --project .guppi guppi materialize` lifts a `lesson[...]` line of the `raw/<date>/<hi HHMM>/ledger.md` of a unit that carries a `{newtag:<tag>|<meaning>|<aliases>}` block.

> **then:**
> The `new_tags` of the `raw/<date>/<hi HHMM>/materialize.yaml` of the unit hold the tag once, with its meaning and its aliases.
> **＋** The tags that the Cases of the `raw/<date>/<hi HHMM>/spec.md` of the unit declare stand first, and a tag that one of them declares keeps the meaning and aliases of that Case.
> **＋** A tag that two lesson lines declare keeps the declaration of the earlier line.
> **＋** The lesson entry carries its tags, its trigger and its root cause as before.
> **－** The yaml gains no entry from a lesson record of `.guppi/guppi/materialize.py` that holds no `new_tags`.

> **tasks:**
> - [ ] update `rule-materialize`
>   - old: `` and `incomplete: [addressed_by]` otherwise (case 377.3). ``
>   - new: `` and `incomplete: [addressed_by]` otherwise (case 377.3). A lesson line's `{newtag:<tag>|<meaning>|<aliases>}` block, read by `parse_line` when its tag stands in the line's `{tags:...}` and its meaning and aliases are not empty, adds the tag with its meaning and aliases to the yaml's `new_tags` once, after the tags that the Cases of the Spec declare, a tag already there passed by, so that `generate` adds its row to `tags.md` (as set in case 827.2). ``
>   - change: `a newtag block of a lesson line adds its tag to new_tags (case 827.2)`
> - [ ] create `estimate-materialize-lifts-a-tag-of-a-lesson`
>   - ref: `rule-materialize`
>   - kind: `QA`
>   - purpose: `Whether a tag that a newtag block of a lesson line declares reaches the new_tags of materialize.yaml once, with its meaning and aliases`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_materialize.py -k newtag`
>   - tags: `[harness, workflow, ledger]`
> - [ ] `.guppi/guppi/materialize.py`: after the `new_tags` of the Cases of the Spec, the `new_tags` of each lesson record of the unit join the yaml's `new_tags` in ledger order, a tag already there passed by; the module docstring says so.
> - [ ] `.guppi/tests/test_materialize.py`: tests named `test_newtag_...` over the Criterion of `estimate-materialize-lifts-a-tag-of-a-lesson`.
> - [ ] read `estimate-materialize-lifts-a-tag-of-a-lesson`

> **ratification:**
> ```
> - decision[case 827.2][update][rule-materialize]{ref:rule-materialize}
> - decision[case 827.2][create][estimate-materialize-lifts-a-tag-of-a-lesson]{ref:rule-materialize}{tags:harness,workflow,ledger}
> ```

### Case 827.3 — ratification.md sets the block that declares a tag

> **given:**
> `rule-ratification`: the one rule and the form of the ledger lines.
> **＋** `vault/wiki/ratification.md`: the Render of `rule-ratification`.
> **＋** `estimate-ratification-ledger-line-form`: its Criterion is replaced whole.
> **＋** `vault/wiki/tags.md`: the registry of tags.

> **when:**
> The agent writes the ledger lines of a session — the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists — with `vault/wiki/ratification.md` rendered from `rule-ratification`.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
> **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **＋** A lesson line whose tag `vault/wiki/tags.md` does not hold carries one `{newtag:<tag>|<meaning>|<aliases>}` block per such tag before `trigger:`, the tag also in its `{tags:...}`, the meaning one line and the aliases the words of the chat language for it.
> **－** A lesson whose fix is ratified in another session gets no mark.

> **tasks:**
> - [ ] update `rule-ratification`
>   - old: `When unsure whether something needs ratification: it does.`
>   - new: `` When unsure whether something needs ratification: it does. A new tag needs no Decision when a lesson line declares it with its meaning and its {{chat_lang}} aliases, and the librarian's run adds it to `tags.md` (as set in case 827.3). ``
>   - old: `` A `create` line carries the ratified tags: `{tags:a,b}`. ``
>   - new: `` A `create` line carries the ratified tags: `{tags:a,b}`. A lesson line whose tag `tags.md` does not hold declares it by one `{newtag:<tag>|<meaning>|<aliases>}` block per new tag, before `trigger:`, the tag also in its `{tags:...}`, the meaning one line and the aliases the {{chat_lang}} words for it; the ledger hook writes the line, and the librarian's run adds the row to `tags.md` (as set in case 827.3). ``
>   - change: `the one rule names a new tag a lesson line declares; the lesson line declares it by a newtag block (case 827.3)`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/ratification.md`
> - [ ] update `estimate-ratification-ledger-line-form`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after a session whose ledger holds a lesson and the Case that closes its cause together, a Case that takes up a decision with more than one Case in its deferred_by, and a lesson line that declares a new tag: those lines and their preview read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — a lesson line declares a new tag by a newtag block (case 827.3)`
> - [ ] read `estimate-ratification-ledger-line-form`

> **ratification:**
> ```
> - decision[case 827.3][update][rule-ratification]{ref:rule-ratification}
> - decision[case 827.3][update][estimate-ratification-ledger-line-form]{ref:rule-ratification}
> ```

### Case 827.4 — The header of tags.md changes by a one-off task

> **given:**
> `vault/wiki/tags.md`: the registry of tags, whose header changes by hand.
> **＋** `rule-vault-layout`: the rule that no file of `wiki/` is written by hand.
> **＋** `rule-page-generation`: the rule that the script is the only writer to `wiki/`.
> **＋** `rule-documentation`: the frame of the librarian.
> **＋** `.claude/agents/librarian-guppi.md`: the Render of `rule-documentation`.
> **＋** `entity-glossary`: the terms, with the rows Ratification, Working files and Librarian.
> **＋** `vault/wiki/glossary.md`: the render of `entity-glossary`.

> **when:**
> Work Mode runs the one-off task on `vault/wiki/tags.md`, and a reader reads it, `rule-vault-layout`, `rule-page-generation`, `.claude/agents/librarian-guppi.md` and `vault/wiki/glossary.md` after the librarian's run.

> **then:**
> The header of `vault/wiki/tags.md` says that a tag enters its table from a tag line of a ratified Case or from a `{newtag:...}` block of a lesson line, and that the librarian's run writes each row and invents none.
> **＋** `rule-vault-layout`, `rule-page-generation` and `.claude/agents/librarian-guppi.md` name that header as the text above the table that a one-off task by hand of a ratified Case changes.
> **＋** The rows Ratification, Working files and Librarian of `vault/wiki/glossary.md` agree with those texts and with `rule-documentation`.
> **－** The one-off task changes no row of the table of `vault/wiki/tags.md`.

> **tasks:**
> - [ ] `vault/wiki/tags.md`: a one-off edit by hand in Work Mode of its header above the table: the sentence that a tag enters only after a Case ratified it says instead that a tag enters from a tag line of a ratified Case or from a `{newtag:...}` block of a lesson line with its meaning and aliases, and that the librarian's run writes each row and invents none; the table stays as it is.
> - [ ] update `rule-vault-layout`
>   - old: `` which git joins by their `merge=union` lines in `.gitattributes` (case 790). A file is ``
>   - new: `` which git joins by their `merge=union` lines in `.gitattributes` (case 790). The header of `tags.md` above its table is written by hand too: a one-off task that a ratified Case names changes it in Work Mode (as set in case 827.4). A file is ``
>   - old: `` `tags.md` the registry of tags already ratified in a Case. ``
>   - new: `` `tags.md` the registry of tags, each declared by a tag line of a ratified Case or by a `{newtag:...}` block of a lesson line, its rows written by `generate`. ``
>   - change: `the header of tags.md changes by a one-off task by hand; a tag enters from a Case or a lesson line (case 827.4)`
> - [ ] update `rule-page-generation`
>   - old: `` which git joins by their `merge=union` lines in `.gitattributes` (case 790). It lays ``
>   - new: `` which git joins by their `merge=union` lines in `.gitattributes` (case 790). The header of `tags.md` above its table is not written by the script: a one-off task by hand that a ratified Case names changes it in Work Mode (as set in case 827.4). It lays ``
>   - change: `the header of tags.md is changed by a one-off task by hand, not by the script (case 827.4)`
> - [ ] update `rule-documentation`
>   - old: `and you write only through the scripts named below.`
>   - new: `` and you write only through the scripts named below. The header of `tags.md` above its table is not yours either: a one-off task by hand that a ratified Case names changes it in Work Mode (as set in case 827.4). ``
>   - change: `the header of tags.md is changed by a one-off task by hand, not by the librarian (case 827.4)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] update `entity-glossary`
>   - old: `| Human sign-off on a Decision; nothing in vault or code changes without one |`
>   - new: `| Human sign-off on a Decision; nothing in vault or code changes without one, but a new tag that a lesson line declares with its meaning and aliases |`
>   - old: `` `tags.md`, the registry of tags ratified in a Case; ``
>   - new: `` `tags.md`, the registry of tags, each from a ratified Case or from a lesson line that declares it, its header changed only by a one-off task by hand that a Case names; ``
>   - old: `` and the lines of `log.md` and `tags.md` that git joins (case 790); ``
>   - new: `` and the lines of `log.md` and `tags.md` that git joins (case 790), and the header of `tags.md`, which a one-off task by hand that a Case names changes; ``
>   - change: `the rows Ratification, Working files and Librarian: a new tag a lesson line declares, and the header of tags.md changed by a one-off task by hand (case 827.4)`
> - [ ] `uv run --project .guppi guppi glossary`

> **ratification:**
> ```
> - decision[case 827.4][update][rule-vault-layout]{ref:rule-vault-layout}
> - decision[case 827.4][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 827.4][update][rule-documentation]{ref:rule-documentation}
> - decision[case 827.4][update][entity-glossary]{ref:entity-glossary}
> ```
