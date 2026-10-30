## Case 940 — The Leaf rules lose How it works, its facts in their code

> **context:**
> A Rule page of one rule, a Leaf, still carries the section `## How it works` on eleven pages. The schema of Rule pages keeps that section for a MOC, a workflow page, and puts the mechanism of a Leaf in the docstring of its code or in its Render; it lets a Leaf keep the section until its next touch. The section can drift from the code it describes: the one of `rule-retro-commit` restates when `guppi gate` blocks the `handoff` skill, which `.guppi/guppi/gate.py` decides. Earlier Cases moved such facts into the docstring and removed the section by hand, such as cases 589.2, 632.1 and 904.1. Session 1713 added `drop`, the key of an `update` that removes a section with its heading (cases 931, 935). The person chose to remove the section from all eleven Leaf pages now. Each fact it holds moves first into the docstring of the code that the page's `implementation_ref` names, and for `rule-internal-context`, which has no code, into its `## Purpose`. A remark on what stood before some Case leaves with the section, since the History of each page and its Decision pages keep it. One new Estimate on `rule-rules-schema` checks the whole change, and the schema says that a Leaf carries no such section.
>
> A Grep `^## How it works` over `vault/wiki/rules/` printed 15 files: `rule-skill-hi`, `rule-git-context`, `rule-documentation`, `rule-spec-write`, `rule-raw-archive`, `rule-event-log`, `rule-page-read`, `rule-tests-clock-pinned`, `rule-claude-md`, `rule-retro-commit`, `rule-ledger-tail`, `rule-governed-files-hook`, `rule-compact-recall`, `rule-internal-context` and `rule-session-start`. A Grep `^kind: MOC` over those 15 files printed 4: `rule-skill-hi`, `rule-documentation`, `rule-claude-md` and `rule-session-start`. These keep the section, as the schema allows. The other eleven are Leaves, and each carries `core: true`, so each pointer to a Case in new text stands in a bracket at the end of its sentence. Case 937 of this session updates `rule-skill-hi`, a MOC, and no page of this Case. I read `drop` of `.guppi/guppi/generate.py` whole. It removes each named section with its heading. It fails the item when the page lacks the section, or when the removal adds a schema finding, and `## How it works` is optional on a Rule page. I also read `replace_hits` of the same module, which joins the words of an `old` by any whitespace. So the pairs of `rule-rules-schema` below match across the line breaks and the indent of its examples. Its Render holds the examples as one section.
>
> A Grep `How it works` over `vault/wiki/`, without `log.md` and `brief.md`, printed 39 files. Besides the 15 pages above, the hits that are no History line are these. In `rule-rules-schema` and `vault/wiki/rules/schema.yaml`, the description of the section and the three examples of a Leaf that still carry it enter the Case by four pairs. `rule-entities-schema`, `vault/wiki/entities/schema.yaml`, `glossary.md`, `entity-glossary.md` and `estimate-entities-schema-checked` speak of the section of an Entity, which this Case does not touch. The Criterion of `estimate-rules-schema-checked` lists `## How it works` as optional, which stays true, and the update of a Render touches no Estimate of the live reading (case 378.5). So its Criterion, `purpose` and `method` stand. `estimate-generate-writes` and `estimate-materialize-assembles` hold it in a Result line, a record. A Grep `How it works` over `.claude/` printed nothing, so no harness file changes. A Grep `How it works|docstring` over the Estimates of the eleven pages printed nothing. Their Criteria speak of behaviour that this Case leaves as it is, so none of them changes.
>
> A Grep `schema\.yaml` over `.guppi/tests/` printed 10 files: `test_generate.py`, `test_materialize.py`, `test_ratified.py`, `test_ship.py`, `test_case_schema.py`, `test_casecheck.py`, `test_prespec.py`, `test_lint.py`, `test_schemas.py` and `test_orchestration.py`. `test_schemas.py` reads the live `vault/wiki/rules/schema.yaml` for its lists and conditions alone. `test_generate.py`, `test_materialize.py`, `test_case_schema.py` and `test_orchestration.py` copy the live schema files into a temporary folder, and their tests rest on the lists, which this Case leaves as they are. The rest write their schema under a temporary folder. `test_the_live_code_holds_no_pointer_outside_a_bracket` of `test_ship.py` reads the live code of `.guppi/`, the new docstrings among it. The brief reports `uv run --project .guppi guppi check` at the close of session 1713 as 13 lines, exit 1, each a page with `core: true` that stands `draft`, none a schema finding; this Case sets no status. The session's ledger holds no `lesson[error]` line, so no line carries `{addresses:...}`.

> **problem:**
> Eleven Leaf rules describe their mechanism in a section that the schema keeps for a MOC, beside the code that decides it, so the two texts can part.

> **recommend:**
> - **Which Leaf rules lose the section, and where its facts go**
>   - Recommended: (a) all eleven now, each fact the docstring of the page's code lacks moved into it first, a rendered Leaf with no code taking it into its Purpose or its Render, then a `drop`.
>   - Answer: (a).
> - **How the removal is checked**
>   - Recommended: (a) a new Estimate on `rule-rules-schema`, read by hand at Retro against the Spec and after the librarian's run by a search, and the schema sentence reworded.
>   - Answer: agreed, (a).
> - **Where the facts of `rule-internal-context` go**
>   - Recommended: (a) into its `## Purpose`.
>   - Answer: agreed, (a).
> - **Whether remarks on what stood before a Case move too**
>   - Recommended: (b) they are left out; the History of each page and its Decision pages keep them.
>   - Answer: agreed, (b).
> - **One Case for all eleven pages, or one part per page**
>   - Recommended: (a) one Case, one Estimate.
>   - Answer: (a).

> **given:**
> `vault/wiki/rules/`: the Rule pages, MOC and Leaf.
> **＋** `rule-rules-schema`: its Render describes the section and holds the examples.
> **＋** `vault/wiki/rules/schema.yaml`: rendered from `rule-rules-schema`.
> **＋** `estimate-rules-schema-leaf-carries-no-how-it-works`: the new check.
> **＋** `rule-tests-clock-pinned`: a Leaf whose section leaves.
> **＋** `.guppi/tests/conftest.py`: the code of `rule-tests-clock-pinned`.
> **＋** `rule-spec-write`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/ratified.py`: the code of `rule-spec-write`.
> **＋** `rule-compact-recall`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/recall.py`: the code of `rule-compact-recall`.
> **＋** `rule-event-log`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/event.py`: the code of `rule-event-log`.
> **＋** `rule-retro-commit`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/gate.py`: the code of `rule-retro-commit`, and of the marks of `rule-event-log`.
> **＋** `rule-raw-archive`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/archive.py`: the code of `rule-raw-archive`.
> **＋** `rule-git-context`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/gitstate.py`: the code of `rule-git-context`.
> **＋** `rule-ledger-tail`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/tail.py`: the code of `rule-ledger-tail`.
> **＋** `rule-page-read`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/pageread.py`: the code of `rule-page-read`.
> **＋** `rule-governed-files-hook`: a Leaf whose section leaves.
> **＋** `.guppi/guppi/guard.py`: the code of `rule-governed-files-hook`.
> **＋** `rule-internal-context`: a Leaf with no code, whose section leaves for its Purpose.
> **＋** `.guppi/tests/test_ship.py`: its test of pointers reads the live code.

> **when:**
> After Work Mode writes the new docstrings and the librarian's run applies the updates of the session, an agent reads a Leaf page of `vault/wiki/rules/`, the docstring of its code, and `vault/wiki/rules/schema.yaml`.

> **then:**
> No Leaf page of `vault/wiki/rules/` carries a section `## How it works`.
> **＋** Each fact that such a section held stands in the docstring of the code that the page's `implementation_ref` names, and for `rule-internal-context` in its `## Purpose`.
> **＋** Each pointer to a Case in that new text stands in a bracket at the end of its sentence.
> **＋** `vault/wiki/rules/schema.yaml` says that the section is for a MOC alone and that a Leaf carries none, and no example of a Leaf in it carries the section.
> **－** A remark on what stood before some Case does not move into the docstrings or the Purpose.
> **－** A MOC page of `vault/wiki/rules/` keeps its `## How it works`.

> **tasks:**
> - [ ] `.guppi/tests/conftest.py`: its module docstring takes each fact of the `## How it works` of `rule-tests-clock-pinned` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/ratified.py`: its module docstring takes each fact of the `## How it works` of `rule-spec-write` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/recall.py`: its module docstring takes each fact of the `## How it works` of `rule-compact-recall` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/event.py`: its module docstring takes each fact of the `## How it works` of `rule-event-log` that it does not hold, but for a remark on what stood before some Case and for the marks that `guppi gate` writes; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/gate.py`: its module docstring takes each fact of the `## How it works` of `rule-retro-commit`, and the facts of the `## How it works` of `rule-event-log` on the marks `prespec`, `retro` and `handoff`, that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/archive.py`: its module docstring takes each fact of the `## How it works` of `rule-raw-archive` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/gitstate.py`: its module docstring takes each fact of the `## How it works` of `rule-git-context` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/tail.py`: its module docstring takes each fact of the `## How it works` of `rule-ledger-tail` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/pageread.py`: its module docstring takes each fact of the `## How it works` of `rule-page-read` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `.guppi/guppi/guard.py`: its module docstring takes each fact of the `## How it works` of `rule-governed-files-hook` that it does not hold, but for a remark on what stood before some Case; each pointer to a Case in a bracket at the end of its sentence.
> - [ ] `uv run --project .guppi guppi test`: exit 0, `test_the_live_code_holds_no_pointer_outside_a_bracket` of `.guppi/tests/test_ship.py` among the passed.
> - [ ] update `rule-tests-clock-pinned`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/tests/conftest.py`
> - [ ] update `rule-spec-write`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/ratified.py`
> - [ ] update `rule-compact-recall`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/recall.py`
> - [ ] update `rule-event-log`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstrings of .guppi/guppi/event.py and .guppi/guppi/gate.py`
> - [ ] update `rule-retro-commit`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/gate.py`
> - [ ] update `rule-raw-archive`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/archive.py`
> - [ ] update `rule-git-context`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/gitstate.py`
> - [ ] update `rule-ledger-tail`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/tail.py`
> - [ ] update `rule-page-read`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/pageread.py`
> - [ ] update `rule-governed-files-hook`
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/guard.py`
> - [ ] update `rule-internal-context`
>   - sections.Purpose: `` Prevents work starting without the current sprint and the previous session's handover. Both are vault files, both fail the same way — missing file or wrong path — so they are one rule rather than two. `orchestration.md` and `ratification.md` are listed here and not in `CLAUDE.md`, so a session without `/hi` carries none of their text, and `case-schema.md`, the form of a Case, is not listed, since it reaches only `case-guppi`, which reads it itself (as set in case 595). `glossary.md` is listed here and not in the `@` import of `CLAUDE.md`, which every subagent loads and none of them needs (as set in case 288.1). The category schemas are not listed: they are read when a page of their category is written. After a compaction `guppi recall` prints the paths of these lines back (as set in case 287). `where-to-stop.md` is listed after `orchestration.md`: the run from the approved Spec to the librarian stops for the person only on its conditions, and Plan Mode, which plans that run with the person, holds the same list, so the main agent promises no turn of the person inside it (as set in case 689.1). ``
>   - drop: `[How it works]`
>   - change: `## How it works left the Leaf, its reasons in the Purpose`
> - [ ] update `rule-rules-schema`
>   - old: `optional. MOC only: why the steps are in this order, and what breaks if they are reordered. On a Leaf the promise lives in its Estimates and the mechanism in the docstring of its code, or in its Render; a Leaf that still carries the section keeps it until its next touch, when the section leaves (cases 193, 200.2).`
>   - new: `optional. MOC only: why the steps are in this order, and what breaks if they are reordered. A Leaf carries none: its promise lives in its Estimates and its mechanism in the docstring of its code, or in its Render (as set in cases 193, 200.2 and 940).`
>   - old: `` one rule rather than two. ## How it works `case-schema.md` is listed here (since case 273); the glossary arrives through `@import` in `CLAUDE.md`, the category schemas are read when a page of their category is written, and re-reading either would duplicate context that is already present. ``
>   - new: `one rule rather than two.`
>   - old: `` workspace resolves would silently land outside the session. ## How it works PreToolUse, matched on writes to `ledger.md`. Reads the readiness flag written when the workspace was resolved; exits 2 and blocks the write if it is missing. ``
>   - new: `workspace resolves would silently land outside the session.`
>   - old: `` it produces a partially applied price. ## How it works A lint rule flags `async def` and `await` under `src/pricing/`. Runs in CI, so the violation surfaces at the change that introduces it rather than at the next incident. ``
>   - new: `it produces a partially applied price.`
>   - change: `a Leaf carries no How it works; the section leaves the three examples of a Leaf`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/rules/schema.yaml`
> - [ ] create `estimate-rules-schema-leaf-carries-no-how-it-works`
>   - ref: `rule-rules-schema`
>   - kind: `QA`
>   - purpose: `Whether no Leaf page of vault/wiki/rules/ carries How it works, each fact it held standing in the docstring of its code or, for rule-internal-context, in its Purpose, and whether the rendered schema says that a Leaf carries none`
>   - method: `by hand at Retro of the session that changes it: each new docstring and the new Purpose of rule-internal-context read against the How it works it takes, and the new Render of rule-rules-schema in the Spec read against the Criterion, recorded in the estimate line; by hand, after the librarian's run of that session: a Grep for ^## How it works over vault/wiki/rules/ and the kind of each page it prints, no Leaf among them, and vault/wiki/rules/schema.yaml read against the Criterion`
>   - tags: `[harness, schema]`
> - [ ] read `estimate-rules-schema-leaf-carries-no-how-it-works`

> **ratification:**
> ```
> - decision[case 940][update][rule-tests-clock-pinned]{ref:rule-tests-clock-pinned}
> - decision[case 940][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 940][update][rule-compact-recall]{ref:rule-compact-recall}
> - decision[case 940][update][rule-event-log]{ref:rule-event-log}
> - decision[case 940][update][rule-retro-commit]{ref:rule-retro-commit}
> - decision[case 940][update][rule-raw-archive]{ref:rule-raw-archive}
> - decision[case 940][update][rule-git-context]{ref:rule-git-context}
> - decision[case 940][update][rule-ledger-tail]{ref:rule-ledger-tail}
> - decision[case 940][update][rule-page-read]{ref:rule-page-read}
> - decision[case 940][update][rule-governed-files-hook]{ref:rule-governed-files-hook}
> - decision[case 940][update][rule-internal-context]{ref:rule-internal-context}
> - decision[case 940][update][rule-rules-schema]{ref:rule-rules-schema}
> - decision[case 940][create][estimate-rules-schema-leaf-carries-no-how-it-works]{ref:rule-rules-schema}{tags:harness,schema}
> ```
