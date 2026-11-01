## Case 978 — A bare link in the root cause of the bare-link lesson

> **context:**
> `guppi lint` of `.guppi/guppi/lint.py` reads every `[[…]]` in the body of a live page as a link to a page, after `links_of` deletes each code span, and `check_refs` reports a link that no live or archived page carries as a `ref` finding; it reads the frontmatter only for its link fields, and `root_cause` is not one of them. The `## Flags` of `vault/wiki/brief.md` report that `guppi check` printed 15 lines, one of them `lessons/lesson-ledger-reading-writes-a-bare-wikilink: ref: body names slug, which no live or archived page carries`, and that the `## Root cause` of that page, at its line 18, holds the bare `[[slug]]` copied from line 19 of `vault/raw/2026-10-31/2307/ledger.md`. The lesson records that very form: `materialize.py` puts the `root_cause:` text of a lesson line both into the field `root_cause` and into the section `## Root cause`, and `generate` writes them as they stand, so the field holds the same bare link. The field is the purpose line of the page in `.guppi/links.md`, written by `.guppi/guppi/links.py`, and the schema of `rule-lessons-schema` says the section expands the field. Case 973 fixed the same defect on `estimate-link-graph-prints-the-neighbours` by putting the bare link in a code span; this Case does the same on the lesson. The person chose to change the section and the field alike: in each, `[[slug]]` goes into a code span, and the rest of the text, the trigger and the status stand; the History gains the one line that `update` of `generate.py` appends for the `change`, as the `## History` of `rule-lessons-schema` says it is appended by hook. The description of `rule-lessons-schema` says that a Lesson is a recorded fact, not a ratified decision, that does not go through a Case, and that nothing about it is checked again. Both sentences stand. They speak of how a lesson is born and of the fact it records: the ledger hook writes it with no Case, and its trigger is not checked again. This Case leaves the fact as recorded and changes only the form of one link that lint reads, and the one rule of `ratification.md` lets nothing in the vault change without a ratified Decision, as earlier Cases did when they updated lesson pages. The new Estimate is a one-time reading of the data on the sprint page, not a check of the lesson, and the lesson gets no `estimates` field. A `replace` pair cannot do it, since its `old` would hold the bare link, which `check_bare_links` of `.guppi/guppi/prespec.py` reports in the plan; so the `update` writes the section whole by `sections` and the field by `set`, both handled by `update` of `.guppi/guppi/generate.py` for any category, and `SUB_POINT` and `put` of `.guppi/guppi/ratified.py` read a section name with a space. A lesson carries no Estimate, so the check is a new one-time Estimate with `once: true` on the live sprint page `entity-sprint-plugin`, as `rule-estimates-schema` sets for a check of one state of the data; it is read by hand after the librarian's run that applies the `update`, since `guppi check` sees the change only then. `estimate-sprint-plugin-check-finds-no-bare-slug-link` stands: its Criterion speaks only of the page of Case 973. The Purpose of `entity-sprint-plugin` lists the goals of the sprint; it stands, since the new Estimate is no goal and is read before the close. A Glob `vault/**/estimate-sprint-plugin-lesson-*.md` printed nothing, so the slug is free. The block of the lesson in `.guppi/links.md` names one neighbour, `estimate-link-graph-prints-the-neighbours`, whose purpose line speaks of `guppi links` and does not change. A Grep of `lesson-ledger-reading|wiki/lessons` over `.guppi/tests/` printed `test_generate.py` and `test_prespec.py`; each builds a lesson in a temporary folder, and no test reads the live page. This Case changes no code and no hook: whether the ledger hook refuses a reading line with a bare link is Case 977, built at the same time, and this Case does not cover the moment a ledger line is written. Case 977 changes `.guppi/guppi/lint.py` in Work Mode, before the librarian's run of this reading: it moves the judgment of a body link into one function that the hook and `.guppi/guppi/prespec.py` share, and keeps its answer on every input but a `[[schema]]` with a `schema.md` in a category folder. The lesson holds no such link, so lint reads the lesson after that change as it reads it now, and the `when` and `then` of this Case stand. Under Case 977 the hook also refuses an estimate line whose text holds a bare link to no page, so the reading of the new Estimate writes `[[slug]]` in a code span. The lesson stands in the ledger of session 2307, not of this session, so no `addresses` mark is written.

> **problem:**
> A bare `[[slug]]` in the `## Root cause` of `lesson-ledger-reading-writes-a-bare-wikilink` names no page, so `guppi check` reports a `ref` finding at each run, and the field `root_cause` holds the same bare form.

> **recommend:**
> - **What the fix changes on the lesson page**
>   - Recommended: (b) the section and the field alike, the bare `[[slug]]` put in a code span in both.
>   - Answer: agreed, (b).
> - **How the fix is checked**
>   - Recommended: (a) a new one-time Estimate on `entity-sprint-plugin`, read by hand after the librarian's run.
>   - Answer: agreed, (a).

> **given:**
> `lesson-ledger-reading-writes-a-bare-wikilink`: the page whose section and field hold the bare link.
> **＋** `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link`: the new one-time check.
> **＋** `entity-sprint-plugin`: the live sprint page, the target of the new check.
> **＋** `.guppi/guppi/lint.py`: the `ref` class that reads the link.
> **＋** `vault/wiki/`: the live pages that the lint reads.
> **＋** `rule-estimates-schema`: a one-time Estimate targets the live sprint page.

> **when:**
> `uv run --project .guppi guppi check` runs the lint of `.guppi/guppi/lint.py` over the live pages of `vault/wiki/`, after the librarian's run that applies the `update` of `lesson-ledger-reading-writes-a-bare-wikilink`.
> **＋** The last change of the file of `lesson-ledger-reading-writes-a-bare-wikilink` is read by `git log -p -1` on its path.

> **then:**
> It prints no `ref` line for `lesson-ledger-reading-writes-a-bare-wikilink`.
> **＋** The `## Root cause` and the field `root_cause` of `lesson-ledger-reading-writes-a-bare-wikilink` hold `[[slug]]` inside a code span, and the rest of their text as it stood.
> **－** The `## Trigger`, the status and the other fields of `lesson-ledger-reading-writes-a-bare-wikilink` do not change, and its `## History` changes only by the line the update appends.

> **tasks:**
> - [ ] update `lesson-ledger-reading-writes-a-bare-wikilink`
>   - set:
>     ```
>     root_cause: "the main agent wrote a bare `[[slug]]` into the text of an estimate line at the Retro of session 1831, generate copied that text into the ## Result as it stood, and nothing checks the text of a reading for a bare wikilink before it reaches a page, so the librarian's flag guessed a cause from the page instead of reading the line"
>     ```
>   - sections.Root cause:
>     ```
>     the main agent wrote a bare `[[slug]]` into the text of an estimate line at the Retro of session 1831, generate copied that text into the ## Result as it stood, and nothing checks the text of a reading for a bare wikilink before it reaches a page, so the librarian's flag guessed a cause from the page instead of reading the line
>     ```
>   - change: `the bare link of the root cause put in a code span, in the section and the field, so lint reads no link to a page`
> - [ ] create `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link`
>   - ref: `entity-sprint-plugin`
>   - kind: `QA`
>   - purpose: `Whether guppi check prints no ref line for lesson-ledger-reading-writes-a-bare-wikilink once the bare link of its root cause stands in a code span, in the section and the field, the rest of that page as it stood but the line its History gains`
>   - method: `by hand, after the librarian's run that applies the update of lesson-ledger-reading-writes-a-bare-wikilink: the output of uv run --project .guppi guppi check and the output of git log -p -1 -- vault/wiki/lessons/lesson-ledger-reading-writes-a-bare-wikilink.md, the diff of the Root cause and the root_cause field, one line added to the History, and of no other field or section, read against the Criterion, both outputs in the estimate line`
>   - once: `true`
>   - tags: `[sprint, harness]`
> - [ ] read `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link`

> **ratification:**
> ```
> - decision[case 978][update][lesson-ledger-reading-writes-a-bare-wikilink]{ref:lesson-ledger-reading-writes-a-bare-wikilink}
> - decision[case 978][create][estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link]{ref:entity-sprint-plugin}{tags:sprint,harness}
> ```
