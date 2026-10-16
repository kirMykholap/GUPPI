## Case 824 — The shipped rules name the languages by role and GUPPI's repository by name

> **context:**
> `guppi ship` of `.guppi/guppi/ship.py` copies each page with `core: true` into the clean version of GUPPI that other projects install. `estimate-clean-branch-ships-neutral-texts` (case 822.7, pending, target `rule-clean-branch`) promises that no sentence of those rules, entities and `CLAUDE.md` holds only in the repository of GUPPI. The `/pre-spec` of session 0553 found that its reading would fail on sentences that call the documentation language English or say "this repository" where the repository of GUPPI is meant (`vault/wiki/brief.md`, `## Next session`). The Renders of `rule-case-build` and `rule-case-protocol` say that the person's answer in `recommend` is written in English. The Purpose of `rule-spec-write` says that `case-guppi` writes the Case in English. The Purpose of `rule-language` says that the manner of the English in the vault is ASD-STE100. In a project whose documentation language is German, each of these sentences is wrong. `rule-morph` says that the copied `guppi.toml` holds the languages and commands "of this repository" and that the read rules name "this repository's" transcripts folder; in an installed project "this repository" is that project, but the values are GUPPI's.
>
> The person chose to reword the five named pages and `rule-permissions` (Q1). A Grep of `this repository|English|Russian|repository of GUPPI` over `vault/wiki/rules/` printed 33 hits in 17 files: `rule-claude-md`, `rule-case-build`, `rule-case-protocol`, `rule-clean-branch`, `rule-entities-schema`, `rule-github-repository`, `rule-guppi-config`, `rule-guppi-package`, `rule-harness`, `rule-morph`, `schema.yaml`, `rule-permissions`, `rule-where-to-stop`, `rule-language`, `rule-spec-write`, `rule-rules-schema` and `rule-skill-wait-what`. Each hit was read. These hits stand:
> - The History lines of `rule-claude-md`, `rule-case-build`, `rule-case-protocol`, `rule-language` and `rule-spec-write`; the Criterion leaves History out.
> - `rule-clean-branch` and `rule-github-repository`, which carry no `core: true` and do not ship.
> - `rule-guppi-config`, `rule-guppi-package` and `rule-harness`, which name the repository of GUPPI as such and so hold in any project.
> - `rule-where-to-stop`, whose sentence on what git in this repository cannot undo holds in any project.
> - `rule-skill-wait-what` and the `## Language` of `rule-case-protocol`, which say that ASD-STE100 is for English only and applies when that language is English.
> - The `core` line of `schema.yaml`, `rule-entities-schema` and `rule-rules-schema`, which this Case leaves to the Frontier item on `rule-rules-schema`.
>
> The same Grep over `vault/wiki/entities/` printed hits in `schema.yaml`, `entity-guppi` and `entity-guppi-repository`. `entity-guppi` already names the repository of GUPPI as such (case 822.7), and `entity-guppi-repository` carries no `core: true`. A Grep of `c--PROJECTS-GUPPI` over `vault/wiki/rules/` printed only `rule-permissions`: two of its hits are in its Render and the third is in its Purpose. The Render is a sample in a fenced block that the Criterion leaves out, and the setup Case of `rule-morph` sets its folder. The Purpose sentence enters this Case. Case 825 of this session renames the install Case of `rule-morph` to the setup Case and sets the whole Purpose of `rule-morph` after this Case. Its new Purpose already names the repository of GUPPI in the two sentences this Case rewords, so the two Cases agree there. This Case calls that Case the setup Case in each sentence it writes. The remaining words "at install" in `rule-permissions` are left to Case 825.
>
> The person chose `{{documentation_lang}}` in the two Renders and plain words in the Purposes (Q2). In this repository both rendered files, `.claude/agents/case-guppi.md` and `vault/wiki/case-schema.md`, read word for word as before, so `uv run --project .guppi guppi render --check` finds no drift. The Criteria of `estimate-case-build-records-the-rounds-in-recommend` and `estimate-case-build-writes-the-case` say "in English". They stand: they are true in this repository, and the Criterion of `estimate-clean-branch-ships-neutral-texts` lists such sentences of shipped Estimates for a later Case and does not fail on them. The Criterion of `estimate-permissions` names `c--PROJECTS-GUPPI` and stands for the same reason. An `update` of a Purpose or of a Render touches no Estimate of the live reading (`case-schema.md`, case 378.5). The person chose to name the repository of GUPPI rather than remove the sentences (Q3). A Grep of `case-schema\.md|case-guppi\.md|rule-case-build|rule-case-protocol|rule-language|rule-spec-write\.md|rule-morph|rule-permissions|in English` over `.guppi/tests/` printed `test_render.py`, `test_recall.py`, `test_guard.py`, `test_glossary.py`, `test_config.py` and `test_case_schema.py`. Each of these reads a copy under a temporary folder, except `test_case_schema.py`, which reads only the block tagged `case` of the live `case-example.md` or `case-schema.md`, and this Case does not change that block.
>
> The check is `estimate-clean-branch-ships-neutral-texts`, whose Criterion stands, since it already promises what this Case changes (Q4). Its `method` needs `uv run --project .guppi guppi ship --allow-draft`. The brief's `## Readings due` reports for the reading of `estimate-clean-branch-installs-as-a-plugin`: "`guppi ship --allow-draft` exits 1 with no tag `prod-x.y.z`". `run` of `.guppi/guppi/ship.py` prints "ship: no tag prod-x.y.z in the history of HEAD; nothing written" in that case. The `method` now waits for that tag as an event it names before a colon, the form that `case-schema.md` accepts (case 781). It carries its pointer in a closing bracket. Its target, `rule-clean-branch`, carries no `core: true`, so the widened `/pre-spec` of Case 823.6 does not judge it. The tag itself is another Frontier item of this session. The rule against which each option was judged is the Criterion of `estimate-clean-branch-ships-neutral-texts`. The new text of each pair keeps each pointer it held in a bracket at the end of its sentence (`case-schema.md`, case 807.4). The brief's `## Readings at the close` reports: "`make test`: 1 failed, 1699 passed, 6 skipped (exit 2)". That failure is in `test_guppi_package.py` on `tests/`, and no text of this Case touches it.

> **problem:**
> Shipped rule pages call the documentation language English and say "this repository" where they mean the repository of GUPPI, so they read false in an installed project, and the check that should catch this is due but cannot run without a version tag.

> **recommend:**
> - **Which pages does this Case rewrite?**
>   - Recommended: (b) the five pages and `rule-permissions`.
>   - Answer: agreed, (b).
> - **How does a sentence name the language?**
>   - Recommended: (a) the placeholder in rendered text, plain words elsewhere.
>   - Answer: agreed, (a).
> - **How is a sentence about GUPPI's own repository reworded?**
>   - Recommended: (a) name GUPPI's repository.
>   - Answer: agreed, (a).
> - **How is the fix checked?**
>   - Recommended: (b) that check stands, and its method waits for a tag.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: a `/pre-spec` finding: Case 825 renames the install Case to the setup Case, so this Case should use that name in the sentences it writes.
>   - Taken: the `then` lines on `rule-morph` and `rule-permissions` and the `context` say "setup Case", and `given` names the file of Case 825.

> **given:**
> `rule-language`: the rule of the two languages, whose Purpose names the manner of the vault's text.
> **＋** `rule-case-build` and `rule-case-protocol`: the rules whose Renders say in which language the person's answer stands in `recommend`.
> **＋** `.claude/agents/case-guppi.md` and `vault/wiki/case-schema.md`: the files rendered from those two Renders.
> **＋** `rule-spec-write`: the rule of the Spec hook, whose Purpose says in which language `case-guppi` writes a Case.
> **＋** `rule-morph`: the rule of the setup Case, whose Purpose says what the copied settings hold.
> **＋** `rule-permissions`: the rule of the allow list, whose Purpose names the folder of saved transcripts.
> **＋** `vault/raw/2026-10-15/1959/cases/case-825.md`: the Case that names the setup Case of `rule-morph` and sets its whole Purpose after this Case.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the check of the texts of the clean version, whose `method` is set anew.
> **＋** `rule-clean-branch`: the rule of `guppi ship`, the target of that check.

> **when:**
> Someone reads `rule-language`, `rule-case-build`, `rule-case-protocol`, `rule-spec-write`, `rule-morph` and `rule-permissions` in the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it, writes into an empty folder.

> **then:**
> The Purposes of `rule-language` and `rule-spec-write` and the Renders of `rule-case-build` and `rule-case-protocol` name the language of a Case and of the person's answer in it as the documentation language, or by `{{documentation_lang}}`, never as English.
> **＋** `rule-language` says that ASD-STE100 Simplified Technical English is the manner of the vault's text when the documentation language is English.
> **＋** `rule-morph` says that, until the setup Case, `guppi.toml` holds the languages and the commands of the repository of GUPPI, and the read rules of `rule-permissions` name the folder of its saved transcripts.
> **＋** `rule-permissions` says that the folder of saved transcripts is named after the path of the project, and that its read rules name the folder of the repository of GUPPI until the setup Case of `rule-morph` sets the project's own.
> **＋** In the repository of GUPPI each changed sentence keeps its meaning, and `.claude/agents/case-guppi.md` and `vault/wiki/case-schema.md` render word for word as before.
> **－** The Render of `rule-permissions`, the History of each page and the Estimates these pages list do not change.

> **tasks:**
> - [ ] update `rule-language`
>   - old: `manner of the English that lands in the vault — ASD-STE100 Simplified Technical English — is the`
>   - new: `manner of the text that lands in the vault — ASD-STE100 Simplified Technical English when the documentation language is English — is the`
>   - change: `the Purpose names ASD-STE100 only for a documentation language that is English`
> - [ ] update `rule-spec-write`
>   - old: `` `case-guppi` writes the whole Case in English, and a hook copies ``
>   - new: `` `case-guppi` writes the whole Case in the documentation language, and a hook copies ``
>   - change: `the Purpose names the language of a Case by its role`
> - [ ] update `rule-case-build`
>   - old: `` a sub-item `Answer:` with the person's answer in English, both as they stood ``
>   - new: `` a sub-item `Answer:` with the person's answer in {{documentation_lang}}, both as they stood ``
>   - change: `the Render names the language of an answer in recommend by its placeholder`
> - [ ] update `rule-case-protocol`
>   - old: `what it recommended, the person's answer in English, both as they stood when the person answered it`
>   - new: `what it recommended, the person's answer in {{documentation_lang}}, both as they stood when the person answered it`
>   - old: `` a sub-item `Answer:`, the person's answer in English, both as they stood ``
>   - new: `` a sub-item `Answer:`, the person's answer in {{documentation_lang}}, both as they stood ``
>   - change: `the Render names the language of an answer in recommend by its placeholder`
> - [ ] update `rule-morph`
>   - old: `` the commands of the keys `test` and `style` of this repository, ``
>   - new: `` the commands of the keys `test` and `style` of the repository of GUPPI, ``
>   - old: `` name the folder of this repository's saved transcripts under `~/.claude/projects`, ``
>   - new: `` name the folder of the saved transcripts of the repository of GUPPI under `~/.claude/projects`, ``
>   - change: `the Purpose names the repository of GUPPI where it meant it by this repository`
> - [ ] update `rule-permissions`
>   - old: `` The saved transcripts of this project, under `~/.claude/projects/c--PROJECTS-GUPPI/` outside the repository, are on the list for reading only: ``
>   - new: `` The saved transcripts of the project, under a folder of `~/.claude/projects/` named after the path of the project outside the repository, such as `c--PROJECTS-GUPPI` for the repository of GUPPI, are on the list for reading only: ``
>   - old: `The folder name follows where this repository sits on the person's disk:`
>   - new: `The read rules name the folder of the repository of GUPPI, after where that repository sits on the person's disk:`
>   - change: `the Purpose names the folder of saved transcripts by how it is named, and the repository of GUPPI where it meant it by this repository`
> - [ ] update `estimate-clean-branch-ships-neutral-texts`
>   - set:
>     ```
>     method: "by hand, after a tag prod-x.y.z stands in the history of HEAD and after the librarian's run of the session that set this method: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and the pages and the files it wrote read against the Criterion, each sentence that holds only in the repository of GUPPI listed in the estimate line (the session of case 824)"
>     ```
>   - change: `the method waits for a tag prod-x.y.z, without which guppi ship writes nothing`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`

> **ratification:**
> ```
> - decision[case 824][update][rule-language]{ref:rule-language}
> - decision[case 824][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 824][update][rule-case-build]{ref:rule-case-build}
> - decision[case 824][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 824][update][rule-morph]{ref:rule-morph}
> - decision[case 824][update][rule-permissions]{ref:rule-permissions}
> - decision[case 824][update][estimate-clean-branch-ships-neutral-texts]{ref:rule-clean-branch}
> ```
