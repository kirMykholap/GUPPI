## Case 476 — The two languages as settings in guppi.toml, and the chat out of the promise of rule-language

> **context:**
> `rule-language` keeps the repository in English and the chat with the owner in Russian. The rule is text. Its Render stands in `CLAUDE.md`, and the words English and Russian are also written into four more rendered texts: `case-schema.md`, `case-guppi.md`, `ask-guppi.md` and the `pre-spec` skill. The pre-spec finding `ratified.untranslated` looks for Cyrillic. A project with another pair of languages would have to rewrite each of these. `estimate-language-followed` also promises that the agent's own text in the chat is Russian. The reply that acknowledged Case 471 was English, and the Estimate failed, as it had failed on 2026-09-26. `insight-session-reply-language-follows-the-english-text-read` (`open`, severity 2) found that no guard reads the language of a reply.
> The person decided in four rounds. There is no check and no reminder on the reply: a slip in the chat costs one request to rewrite it and lands nothing in the vault. So the chat leaves the promise of the Estimate, and that decision answers the Insight. The two languages become settings, `documentation_lang` and `chat_lang`. They are set in the `## Render` of a new Rule, `rule-guppi-config`, which is rendered into `guppi.toml`, guppi's one settings file. A Render may hold `{{documentation_lang}}` or `{{chat_lang}}`. The render reads the codes from the `## Render` of `rule-guppi-config` and puts the name of the language into the output file. It does not read `guppi.toml`, because that file is itself an output of the render. The page keeps the placeholder, so a changed code reaches every text at the next render. The checks read `guppi.toml`: the pre-spec finding takes the script of `documentation_lang` from it through the same module, `guppi/config.py`.
> The vault's answer: no page describes a settings file of guppi. `rule-settings` governs Claude Code's `.claude/settings.json`, which is another file. `rule-morph` holds the questions asked at install and the category set as data. It is deferred by case 239 and stays untouched here, because naming it would take up its defer. The install questions and the category set stay with it. Both `create` lines carry a `ref`, and a Glob of `vault/**/` finds no page for `rule-guppi-config` or `estimate-guppi-config-fills-the-languages`.
> The frame. The Purpose of `rule-harness` counts the pages that belong to it and run in no pipeline, with the list of their cases. 476.1 adds the new page and case 476.1 to that sentence. `rule-render-harness` is a Leaf that still carries `## How it works`, and the Rule schema says the section leaves at its next touch (cases 193, 200.2). `generate` replaces a section but cannot remove one. So 476.1 removes the section as a one-off migration and moves its text into the docstring of `guppi/render.py`, where the schema puts the mechanism of a Leaf. The docstring already holds most of that text. It gains the sentence of case 139.1, the librarian's commit of case 89.2, and the placeholders.
> The Criterion of `estimate-render-harness-reproduces` says that the diff of each file equals the text of its page's Render; with a placeholder, the file holds the Render with the names put in. Its block of case 139.1 also says that the How it works of the page gains a sentence, and that sentence now stands in the docstring. That Estimate is still in the shape before case 193 and waits for a later recut in Slice 3g. Its lines stand until then, and the new Estimate states the fill.
> `estimate-case-protocol-shows-the-built-case`, `estimate-case-build-writes-the-case`, `estimate-ask-finds` and `estimate-spec-write-checks-the-written-case` name English or Russian as this project's values. With `en` and `ru` they stay true, so none is touched. The Purpose sections that say English stay for the same reason.
> Four lines of the old Criterion of `estimate-language-followed` read the chat, and the new Criterion drops them by the person's decision: the Russian of the agent's text, the ledger lines as they stand in the chat, the short form in the chat, and transliteration. A short form written in another language would still fail the line on the Spec, because the hook writes it there as shown. Every other line is carried, with `documentation_lang` in place of English. The Criterion of `estimate-language-spec-prose-in-english` keeps each of its lines, with a letter outside the script of `documentation_lang` in place of a Cyrillic letter and `guppi.toml` read in its `when`.
> The render code lands at once and the pages land at the librarian's run: a render with no placeholder needs no `rule-guppi-config` (476.1). The pre-spec finding reads `guppi.toml`, which exists only after the librarian's render. Before that the finding only goes red and loses nothing, so it keeps no old form.
> Not done: transliteration of English terms into Cyrillic (the failure of 2026-09-26) is not checked. The language of the chat has no guard. The install questions stay with `rule-morph`. The aliases of `tags.md` and `glossary.md` stay Russian data. The slug `estimate-language-spec-prose-in-english` stays as it is. The other Leafs that still carry `## How it works` are not touched.

> **problem:**
> The language pair is written by hand into several rendered texts and one check, so another pair means rewriting each of them. `estimate-language-followed` also promises the language of the agent's replies in the chat. Only the agent guards that, so a slip the person fixes with one request fails a rule whose output in the repository was right.

> **recommend:**
> Four sub-cases. 476.1 creates `rule-guppi-config`, whose Render is `guppi.toml`, and makes the render fill `{{documentation_lang}}` and `{{chat_lang}}` from that Render through `guppi/config.py`. 476.2 moves the Renders of `rule-case-protocol`, `rule-case-build` and `rule-ask` to the placeholders and touches no promise. 476.3 makes the pre-spec finding read `guppi.toml` and look for a letter outside the script of `documentation_lang`, with that judgment in `guppi/config.py`. 476.4 moves the Render of `rule-language` to the placeholders, replaces the Criterion of `estimate-language-followed` with one that leaves out the chat, and sets the Insight `actioned`. The rejected option was a `Stop` check that counts the letters of each reply; the person found it a system built around a slip they fix with one request.

### Case 476.1 — guppi.toml, rendered from rule-guppi-config, fills the language placeholders

> **given:**
> `rule-guppi-config` — the new Rule; its Render sets the codes and is guppi's settings file
> **＋** `guppi.toml` — the settings file, rendered in full from `rule-guppi-config`; the checks read it
> **＋** `guppi/config.py` and `tests/test_config.py` — read the settings; the table of each code's name and script
> **＋** `guppi/render.py` and `tests/test_render.py` — the renderer, which fills the placeholders; its docstring holds the mechanism
> **＋** `rule-render-harness` — the renderer's page: its `implementation_ref`, and its `## How it works`, which leaves
> **＋** `rule-rules-schema` — a Leaf's `## How it works` leaves at its next touch
> **＋** `rule-harness` — the parent: its Purpose names the pages that run in no pipeline
> **＋** `estimate-guppi-config-fills-the-languages` — the new promise

> **when:**
> `guppi render` builds the governed files from the `## Render` of the render pages.

> **then:**
> Each `{{documentation_lang}}` and `{{chat_lang}}` in the `## Render` of a render page becomes, in the file it governs, the name of the language whose code the `## Render` of `rule-guppi-config` sets for that key, by the table of `guppi/config.py`.
> **＋** The page keeps the placeholder, so the next render after a changed code writes the new name.
> **＋** `guppi.toml` is written from the `## Render` of `rule-guppi-config`, like any file rendered in full.
> **＋** A placeholder whose name is not a key, a key missing from `rule-guppi-config`, or a code the table does not hold stops the run: nothing is written, the page and the placeholder or key go to stderr, `guppi render` exits 1, and `guppi render --sync` exits 0 with the same line.
> **＋** `guppi render --check` compares each governed file with the filled text.
> **－** A run in which no `## Render` holds a placeholder reads no `rule-guppi-config` and needs none.
> **－** The render reads the codes from the `## Render` of `rule-guppi-config`, never from `guppi.toml`, which is its own output.

> **tasks:**
> - [ ] create `rule-guppi-config`
>   - type: `rule`
>   - ref: `rule-harness`
>   - kind: `Leaf`
>   - purpose: `Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision`
>   - enforcement: `render`
>   - governs: `guppi.toml`
>   - render_mode: `full`
>   - implementation_ref: `[guppi/config.py, tests/test_config.py]`
>   - tags: `[harness, render]`
>   - sections.Purpose:
>     ```
>     Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision. This page's Render is `guppi.toml`, guppi's one settings file: a change is an `update` of the Render, and the governed-files hook refuses a hand edit of the file. It sets the language of the repository, `documentation_lang`, and the language of the chat with the owner, `chat_lang`, as codes; `guppi/config.py` holds the table of each code's name and script. The render reads the codes from this Render and puts the name where another Render writes `{{documentation_lang}}` or `{{chat_lang}}`; the checks, such as the pre-spec finding, read `guppi.toml`. The questions asked at install and the category set stay with `rule-morph` (case 476.1).
>     ```
>   - sections.Render:
>     ```
>     <!-- rule-guppi-config -->
>     # guppi settings, rendered from vault/wiki/rules/rule-guppi-config.md
>     documentation_lang = "en"
>     chat_lang = "ru"
>     <!-- /rule-guppi-config -->
>     ```
> - [ ] create `estimate-guppi-config-fills-the-languages`
>   - type: `estimate`
>   - ref: `rule-guppi-config`
>   - kind: `QA`
>   - purpose: `Whether the render puts the names of the languages set in the Render of rule-guppi-config in place of the placeholders of every Render, and stops with nothing written on a placeholder, key or code it cannot resolve`
>   - method: `uv run pytest tests/test_config.py and uv run pytest tests/test_render.py -k placeholder; by hand, the first render after the librarian's run: CLAUDE.md names English and Russian where rule-language holds the placeholders, and guppi.toml holds documentation_lang and chat_lang`
>   - tags: `[harness, render]`
> - [ ] update `rule-render-harness`
>   - set: `{implementation_ref: [guppi/render.py, guppi/config.py, tests/test_render.py, .claude/settings.json]}`
>   - change: `the render fills the language placeholders of a Render from rule-guppi-config; How it works left for the docstring of guppi/render.py (cases 193, 476.1)`
> - [ ] update `rule-harness`
>   - old: `` Eight more belong here and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1). ``
>   - new: `` Nine more belong here and run in no pipeline: the settings file of guppi, `guppi.toml`, the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1). ``
>   - change: `rule-guppi-config, the settings file of guppi, belongs to the harness (case 476.1)`
> - [ ] one-off migration: `vault/wiki/rules/rule-render-harness.md` — the `## How it works` section removed; what the docstring of `guppi/render.py` does not hold yet moves into it: the `Render:` line of `/hi` (case 115), the librarian's commit of the rendered files (case 89.2), and the sentence of case 139.1 on when Claude Code reads an agent file
> - [ ] `guppi/config.py` — read `guppi.toml` and the text of a Render with `tomllib`; the table of codes with each language's name and script; an unknown code or a missing key is an error
> - [ ] `guppi/render.py` — fill `{{documentation_lang}}` and `{{chat_lang}}` in every Render from the `## Render` of `rule-guppi-config`; an unresolved placeholder, key or code is a `RenderError`; no placeholder, no read of the page; the docstring names the placeholders
> - [ ] `tests/test_config.py` — the table, a missing key, an unknown code
> - [ ] `tests/test_render.py` — `-k placeholder`: a filled Render, the page unchanged, an unknown placeholder, key and code with nothing written, a run with no placeholder and no `rule-guppi-config`
> - [ ] `uv run guppi render`: `guppi.toml`
> - [ ] read `estimate-guppi-config-fills-the-languages`

> **ratification:**
> ```
> - decision[case 476.1][create][rule-guppi-config]{ref:rule-harness}{tags:harness,render}
> - decision[case 476.1][create][estimate-guppi-config-fills-the-languages]{ref:rule-guppi-config}{tags:harness,render}
> - decision[case 476.1][update][rule-render-harness]{ref:rule-render-harness}
> - decision[case 476.1][update][rule-harness]{ref:rule-harness}
> ```

### Case 476.2 — The Case schema and the agent files name the languages set in rule-guppi-config

> **given:**
> `rule-case-protocol` — its Render, the headings, the language, the Spec form, the tags and the showing of a round
> **＋** `vault/wiki/case-schema.md` — the schema rendered from `rule-case-protocol`
> **＋** `rule-case-build` — its Render, the language of the Case and of a round
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from `rule-case-build`
> **＋** `rule-ask` — its Render, the language of the aliases
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `rule-guppi-config` — the two languages, in its Render

> **when:**
> The agent reads `vault/wiki/case-schema.md` in a working session, and `case-guppi` or `ask-guppi` starts with its agent file.

> **then:**
> Where these files named English for a Case, the Spec and the vault, they name the language that `rule-guppi-config` sets as `documentation_lang`.
> **＋** Where they named Russian for the chat, the aliases and a translated round, they name the language that `rule-guppi-config` sets as `chat_lang`.
> **＋** `vault/wiki/case-schema.md` asks for the manner of ASD-STE100 Simplified Technical English only when `documentation_lang` is English.
> **－** The Purpose sections of `rule-case-protocol`, `rule-case-build` and `rule-ask` keep their words: they state this project's values.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `in the Spec, in English; in the chat the same heading, the name in Russian, over`
>   - new: `in the Spec, in {{documentation_lang}}; in the chat the same heading, the name in {{chat_lang}}, over`
>   - old:
>     ```
>     `case-guppi` writes the whole Case in English (case 441). A Case it built reaches the person whole in English, in the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that the agent sends (case 452.4). Russian in the chat with the owner for the short text on each Case and sub-case that goes with the file, the name in its heading, a round of questions of `case-guppi`, translated from the answer, and the agent's own text; the ledger lines of `ratification` stand in the chat as the answer holds them, the words the vault will hold (cases 387.1, 441, 452.5). The main agent writes a short-form Case in English in the chat, and the hook writes it as shown (case 441). English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Spec is written from the English answer and the English short form, slugs, field names and ledger lines unchanged (cases 123, 387.1, 441). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`.
>     ```
>   - new:
>     ```
>     `case-guppi` writes the whole Case in {{documentation_lang}} (case 441). A Case it built reaches the person whole in {{documentation_lang}}, in the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that the agent sends (case 452.4). {{chat_lang}} in the chat with the owner for the short text on each Case and sub-case that goes with the file, the name in its heading, a round of questions of `case-guppi`, translated from the answer, and the agent's own text; the ledger lines of `ratification` stand in the chat as the answer holds them, the words the vault will hold (cases 387.1, 441, 452.5). The main agent writes a short-form Case in {{documentation_lang}} in the chat, and the hook writes it as shown (case 441). {{documentation_lang}} in everything that lands in the vault, in the manner of ASD-STE100 Simplified Technical English when that language is English: the Spec is written from the {{documentation_lang}} answer and the {{documentation_lang}} short form, slugs, field names and ledger lines unchanged (cases 123, 387.1, 441, 476.2). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`; the two are set in `rule-guppi-config`, rendered into `guppi.toml`.
>     ```
>   - old: `` the blockquotes in English, the `then` and `tasks` blocks ``
>   - new: `` the blockquotes in {{documentation_lang}}, the `then` and `tasks` blocks ``
>   - old: `with a meaning and a Russian alias`
>   - new: `with a meaning and a {{chat_lang}} alias`
>   - old: `it writes a short text in Russian on what the Case changes`
>   - new: `it writes a short text in {{chat_lang}} on what the Case changes`
>   - old: `which the agent shows translated into Russian line by line`
>   - new: `which the agent shows translated into {{chat_lang}} line by line`
>   - change: `the languages of the Case, the chat and the vault named by the placeholders set in rule-guppi-config; ASD-STE100 only for English (case 476.2)`
> - [ ] update `rule-case-build`
>   - old: `Write it whole in English — its name`
>   - new: `Write it whole in {{documentation_lang}} — its name`
>   - old: `who reads it in English, and the person ratifies it`
>   - new: `who reads it in {{documentation_lang}}, and the person ratifies it`
>   - old: `your recommended answer, in English, with no Case heading`
>   - new: `your recommended answer, in {{documentation_lang}}, with no Case heading`
>   - change: `the language of the Case and of a round named by the placeholder set in rule-guppi-config (case 476.2)`
> - [ ] update `rule-ask`
>   - old: `` the aliases column of `vault/wiki/tags.md` maps Russian words to tags ``
>   - new: `` the aliases column of `vault/wiki/tags.md` maps {{chat_lang}} words to tags ``
>   - change: `the language of the aliases named by the placeholder set in rule-guppi-config (case 476.2)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`

> **ratification:**
> ```
> - decision[case 476.2][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 476.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 476.2][update][rule-ask]{ref:rule-ask}
> ```

### Case 476.3 — The pre-spec finding reads the script of documentation_lang from guppi.toml

> **given:**
> `guppi/config.py` — the script of a language, and the read of `guppi.toml`
> **＋** `guppi/ratified.py` — `untranslated`, the judgment of the finding
> **＋** `guppi/prespec.py` — `check_untranslated`, the text of the finding
> **＋** `tests/test_prespec.py` — the tests of the finding
> **＋** `guppi.toml` — the language of the repository, as the checks read it
> **＋** `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — its Render names the finding
> **＋** `estimate-language-spec-prose-in-english` — its Criterion replaced whole

> **when:**
> `guppi prespec --check <plan>` runs at `/pre-spec`, and reads the plan file and `guppi.toml`.

> **then:**
> A name, `context` or `problem` of a Case of the plan that holds a letter outside the script of the language `guppi.toml` sets as `documentation_lang` gives one finding naming the Case, the part and the language.
> **＋** A short-form Case under `## Deferred` is read the same way.
> **＋** A plan whose names, contexts and problems hold no letter outside that script gives no finding of this check.
> **＋** A `guppi.toml` that is missing, or that names a code the table of `guppi/config.py` does not hold, gives one finding that names `guppi.toml`, and no Case is read by this check.
> **＋** The judgment of a letter's script lives in `guppi/config.py`, and `guppi/ratified.py` imports it.
> **－** The `given`, `when`, `then` and the blocks of a Case are not read by this check: a quotation there keeps its language.
> **－** The plan is compared with no other file: no ratified copy is read.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `` still holding a Cyrillic letter, a short form under `## Deferred` included — `case-guppi` writes English and a short form is shown in English; ``
>   - new: `` still holding a letter outside the script of {{documentation_lang}}, the language `guppi.toml` sets for the repository, a short form under `## Deferred` included — `case-guppi` writes {{documentation_lang}} and a short form is shown in {{documentation_lang}}; ``
>   - change: `the finding reads guppi.toml and looks for a letter outside the script of documentation_lang, not for Cyrillic (case 476.3)`
> - [ ] update `estimate-language-spec-prose-in-english`
>   - set: `{status: pending, purpose: "Pre-spec finds a name, context or problem of a Case of the plan that holds a letter outside the script of the documentation language of guppi.toml, a short form under Deferred included", method: "uv run pytest tests/test_prespec.py -k script"}`
>   - change: `the Criterion replaced whole — a letter outside the script of documentation_lang, read from guppi.toml, not a Cyrillic letter (case 476.3)`
> - [ ] `guppi/config.py` — the script of a language's code, and whether a text holds a letter outside it
> - [ ] `guppi/ratified.py` — `untranslated` takes the language and imports the judgment from `guppi/config.py`; `CYRILLIC` removed
> - [ ] `guppi/prespec.py` — `check_untranslated` reads `guppi.toml` through `guppi/config.py`; the finding names the language; a missing file or an unknown code is one finding that names `guppi.toml`
> - [ ] `tests/test_prespec.py` — the tests `-k cyrillic` renamed `-k script`: `en` with a Cyrillic letter, a plan with none, a short form under `## Deferred`, a missing `guppi.toml`, an unknown code
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-language-spec-prose-in-english`

> **ratification:**
> ```
> - decision[case 476.3][update][rule-prespec]{ref:rule-prespec}
> - decision[case 476.3][update][estimate-language-spec-prose-in-english]{ref:estimate-language-spec-prose-in-english}
> ```

### Case 476.4 — rule-language names the languages set in rule-guppi-config, and its promise leaves the chat

> **given:**
> `rule-language` — its purpose, its Purpose and its Render, on the placeholders
> **＋** `CLAUDE.md` — rendered from `rule-language`
> **＋** `rule-guppi-config` — the two languages, in its Render
> **＋** `vault/wiki/case-schema.md` — the form of a Case, which the rule does not repeat
> **＋** `estimate-language-followed` — its Criterion replaced whole
> **＋** `insight-session-reply-language-follows-the-english-text-read` — the Insight this Case actions
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec of a session
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a built Case

> **when:**
> The render writes `CLAUDE.md` from `rule-language` and the Render of `rule-guppi-config`, and a session writes into the repository.

> **then:**
> `CLAUDE.md` holds the `## Language` section of `rule-language`, with the names of the languages that `rule-guppi-config` sets as `documentation_lang` and `chat_lang` where its Render holds the placeholders.
> **＋** Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the approved Spec in `raw/<date>/<hi HHMM>/spec.md` — is in `documentation_lang`.
> **＋** A Case built by `case-guppi` is in `documentation_lang` whole — its name, `context`, `problem`, `recommend`, `given`, `when`, `then`, `tasks` and `ratification` — in `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and its name, `context` and `problem` are in `documentation_lang` in `raw/<date>/<hi HHMM>/spec.md`.
> **＋** Its `given`, `when`, `then` and `tasks` enter `raw/<date>/<hi HHMM>/spec.md` unchanged.
> **＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language.
> **－** The language of the agent's own text in the chat is not read: a reply in a language other than `chat_lang` is not a failure of this promise.
> **－** The rule speaks of the language, not of the Case form: the form is `vault/wiki/case-schema.md`.

> **tasks:**
> - [ ] update `rule-language`
>   - set: `{purpose: "Keeps the repository in the documentation language and the chat with the owner in the chat language, both set in rule-guppi-config, a built Case whole in the documentation language in the file sent to the person, with slugs, paths and quotations unchanged in either"}`
>   - old: `Keeps the repository in English and the chat with the owner in Russian.`
>   - new: `` Keeps the repository in the documentation language and the chat with the owner in the chat language, `documentation_lang` and `chat_lang` set in `rule-guppi-config` and rendered into `guppi.toml` — English and Russian in this project (case 476.4). ``
>   - sections.Render:
>     ```
>     <!-- rule-language -->
>     ## Language
>
>     {{documentation_lang}} for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. {{chat_lang}} for chat with the owner; a Case is {{documentation_lang}} whole — its name, `context`, `problem` and `recommend` too — in the file the agent sends the person and in the Spec, and the chat holds a short {{chat_lang}} text on each Case and sub-case, its ledger lines in {{documentation_lang}} as the file holds them; a short-form Case is {{documentation_lang}} in the chat, as the Spec holds it. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. Technical terms in {{documentation_lang}} are not transliterated in {{chat_lang}} text. The two languages are set in `rule-guppi-config`, rendered into `guppi.toml`.
>     <!-- /rule-language -->
>     ```
>   - change: `the two languages named by the placeholders set in rule-guppi-config (case 476.4)`
> - [ ] update `estimate-language-followed`
>   - set: `{status: pending, purpose: "The section stands in CLAUDE.md with the languages set in rule-guppi-config, and what a session writes into the repository is in the documentation language, slugs and paths unchanged", method: "one reading by hand in the next session — CLAUDE.md against the Render of rule-guppi-config, and the session's commit, Spec and Case files against the section"}`
>   - change: `the Criterion replaced whole — the languages come from rule-guppi-config, and the language of the agent's text in the chat leaves the promise (case 476.4)`
> - [ ] update `insight-session-reply-language-follows-the-english-text-read`
>   - set: `{status: actioned, addressed_by: decision-case-476.4}`
>   - change: `actioned: the language of the chat leaves the promise of estimate-language-followed; a slip in the chat is fixed on the person's request and gets no guard (case 476.4)`
> - [ ] `uv run guppi render`: `CLAUDE.md`
> - [ ] read `estimate-language-followed` — by hand, in the session after the render

> **ratification:**
> ```
> - decision[case 476.4][update][rule-language]{ref:rule-language}
> - decision[case 476.4][update][estimate-language-followed]{ref:estimate-language-followed}
> - decision[case 476.4][update][insight-session-reply-language-follows-the-english-text-read]{ref:insight-session-reply-language-follows-the-english-text-read}
> ```
