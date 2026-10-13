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

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` and the code they point to by `governs`, `implementation_ref` or `code_ref`. ``
>   - new: `` and the code they point to by `governs`, `implementation_ref` or `code_ref`. Where the item points to code, a file, a module or a function the person's words name, that no live page covers, since no page names its file, or a folder that holds it, in `code_ref`, `implementation_ref` or `governs`, read that code as this paragraph sets for a module of code, and search the pages by meaning for the thing it does; then offer in a round a page only for the thing the Case changes, described from the code you read: where a page already describes that thing, the path added to the field of that page that lists its code; otherwise a new page, its category by the check that the schema of the category sets, with its slug, its one-line purpose, its parent and its paths. The person decides: where the person turns both down, you ask in a round which page the Case changes. The page, or the path added, is a task of the same Case, and the Estimate of the Case stands on that page; code the Case does not change gets no page (case 803). ``
>   - change: `for code that the Case changes and no page covers, case-guppi reads the code and offers in a round a page, or the path added to a page that describes the thing (case 803)`
> - [ ] update `rule-case-protocol`
>   - old: `` `children`, `code_ref`, `deferred_by` — are filled mechanically ``
>   - new: `` `children`, `deferred_by` — are filled mechanically ``
>   - old: `` `guppi materialize` reads the blocks, and what is not in a block was signed by nobody. ``
>   - new: `` `code_ref` is no such field: a Case writes it, on a `create` or by `set` on an `update`, when it gives a page the path of its code (case 803). `guppi materialize` reads the blocks, and what is not in a block was signed by nobody. ``
>   - change: `code_ref leaves the list of derivable fields: a Case writes it when it gives a page the path of its code (case 803)`
> - [ ] create `estimate-case-build-offers-a-page-for-code-no-page-covers`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi, on an item that points to code no page covers, reads that code and offers in a round a page only for the thing the Case changes, or the path added to a page that describes it, and puts the chosen page into the same Case`
>   - method: `by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-build-offers-a-page-for-code-no-page-covers`

> **ratification:**
> ```
> - decision[case 803][update][rule-case-build]{ref:rule-case-build}
> - decision[case 803][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 803][create][estimate-case-build-offers-a-page-for-code-no-page-covers]{ref:rule-case-build}{tags:session,workflow,harness}
> ```
