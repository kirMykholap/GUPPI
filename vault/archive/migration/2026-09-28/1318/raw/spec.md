<!-- approved 19:31:32 · session 14b8fdb1 -->

# Spec — session 1318, 2026-09-28

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

```then
create:
- slug: rule-guppi-config
  type: rule
  ref: rule-harness
  kind: Leaf
  purpose: Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision
  enforcement: render
  governs: guppi.toml
  render_mode: full
  implementation_ref:
  - guppi/config.py
  - tests/test_config.py
  tags:
  - harness
  - render
  sections:
    Purpose: 'Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision. This page''s Render is `guppi.toml`, guppi''s one settings file: a change is an `update` of the Render, and the governed-files hook refuses a hand edit of the file. It sets the language of the repository, `documentation_lang`, and the language of the chat with the owner, `chat_lang`, as codes; `guppi/config.py` holds the table of each code''s name and script. The render reads the codes from this Render and puts the name where another Render writes `{{documentation_lang}}` or `{{chat_lang}}`; the checks, such as the pre-spec finding, read `guppi.toml`. The questions asked at install and the category set stay with `rule-morph` (case 476.1).'
    Render: |-
      <!-- rule-guppi-config -->
      # guppi settings, rendered from vault/wiki/rules/rule-guppi-config.md
      documentation_lang = "en"
      chat_lang = "ru"
      <!-- /rule-guppi-config -->
- slug: estimate-guppi-config-fills-the-languages
  type: estimate
  ref: rule-guppi-config
  kind: QA
  purpose: Whether the render puts the names of the languages set in the Render of rule-guppi-config in place of the placeholders of every Render, and stops with nothing written on a placeholder, key or code it cannot resolve
  method: 'uv run pytest tests/test_config.py and uv run pytest tests/test_render.py -k placeholder; by hand, the first render after the librarian''s run: CLAUDE.md names English and Russian where rule-language holds the placeholders, and guppi.toml holds documentation_lang and chat_lang'
  tags:
  - harness
  - render
update:
- slug: rule-render-harness
  set:
    implementation_ref:
    - guppi/render.py
    - guppi/config.py
    - tests/test_render.py
    - .claude/settings.json
  change: the render fills the language placeholders of a Render from rule-guppi-config; How it works left for the docstring of guppi/render.py (cases 193, 476.1)
- slug: rule-harness
  replace:
  - old: 'Eight more belong here and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1).'
    new: 'Nine more belong here and run in no pipeline: the settings file of guppi, `guppi.toml`, the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1).'
  change: rule-guppi-config, the settings file of guppi, belongs to the harness (case 476.1)
```

```tasks
- [x] create `rule-guppi-config`
- [x] create `estimate-guppi-config-fills-the-languages`
- [x] update `rule-render-harness`
- [x] update `rule-harness`
- [x] one-off migration: `vault/wiki/rules/rule-render-harness.md` — the `## How it works` section removed; what the docstring of `guppi/render.py` does not hold yet moves into it: the `Render:` line of `/hi` (case 115), the librarian's commit of the rendered files (case 89.2), and the sentence of case 139.1 on when Claude Code reads an agent file
- [x] `guppi/config.py` — read `guppi.toml` and the text of a Render with `tomllib`; the table of codes with each language's name and script; an unknown code or a missing key is an error
- [x] `guppi/render.py` — fill `{{documentation_lang}}` and `{{chat_lang}}` in every Render from the `## Render` of `rule-guppi-config`; an unresolved placeholder, key or code is a `RenderError`; no placeholder, no read of the page; the docstring names the placeholders
- [x] `tests/test_config.py` — the table, a missing key, an unknown code
- [x] `tests/test_render.py` — `-k placeholder`: a filled Render, the page unchanged, an unknown placeholder, key and code with nothing written, a run with no placeholder and no `rule-guppi-config`
- [x] `uv run guppi render`: `guppi.toml`
- [x] read `estimate-guppi-config-fills-the-languages`
```

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

```then
update:
- slug: rule-case-protocol
  replace:
  - old: in the Spec, in English; in the chat the same heading, the name in Russian, over
    new: in the Spec, in {{documentation_lang}}; in the chat the same heading, the name in {{chat_lang}}, over
  - old: '`case-guppi` writes the whole Case in English (case 441). A Case it built reaches the person whole in English, in the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that the agent sends (case 452.4). Russian in the chat with the owner for the short text on each Case and sub-case that goes with the file, the name in its heading, a round of questions of `case-guppi`, translated from the answer, and the agent''s own text; the ledger lines of `ratification` stand in the chat as the answer holds them, the words the vault will hold (cases 387.1, 441, 452.5). The main agent writes a short-form Case in English in the chat, and the hook writes it as shown (case 441). English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Spec is written from the English answer and the English short form, slugs, field names and ledger lines unchanged (cases 123, 387.1, 441). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`.'
    new: '`case-guppi` writes the whole Case in {{documentation_lang}} (case 441). A Case it built reaches the person whole in {{documentation_lang}}, in the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that the agent sends (case 452.4). {{chat_lang}} in the chat with the owner for the short text on each Case and sub-case that goes with the file, the name in its heading, a round of questions of `case-guppi`, translated from the answer, and the agent''s own text; the ledger lines of `ratification` stand in the chat as the answer holds them, the words the vault will hold (cases 387.1, 441, 452.5). The main agent writes a short-form Case in {{documentation_lang}} in the chat, and the hook writes it as shown (case 441). {{documentation_lang}} in everything that lands in the vault, in the manner of ASD-STE100 Simplified Technical English when that language is English: the Spec is written from the {{documentation_lang}} answer and the {{documentation_lang}} short form, slugs, field names and ledger lines unchanged (cases 123, 387.1, 441, 476.2). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`; the two are set in `rule-guppi-config`, rendered into `guppi.toml`.'
  - old: the blockquotes in English, the `then` and `tasks` blocks
    new: the blockquotes in {{documentation_lang}}, the `then` and `tasks` blocks
  - old: with a meaning and a Russian alias
    new: with a meaning and a {{chat_lang}} alias
  - old: it writes a short text in Russian on what the Case changes
    new: it writes a short text in {{chat_lang}} on what the Case changes
  - old: which the agent shows translated into Russian line by line
    new: which the agent shows translated into {{chat_lang}} line by line
  change: the languages of the Case, the chat and the vault named by the placeholders set in rule-guppi-config; ASD-STE100 only for English (case 476.2)
- slug: rule-case-build
  replace:
  - old: Write it whole in English — its name
    new: Write it whole in {{documentation_lang}} — its name
  - old: who reads it in English, and the person ratifies it
    new: who reads it in {{documentation_lang}}, and the person ratifies it
  - old: your recommended answer, in English, with no Case heading
    new: your recommended answer, in {{documentation_lang}}, with no Case heading
  change: the language of the Case and of a round named by the placeholder set in rule-guppi-config (case 476.2)
- slug: rule-ask
  replace:
  - old: the aliases column of `vault/wiki/tags.md` maps Russian words to tags
    new: the aliases column of `vault/wiki/tags.md` maps {{chat_lang}} words to tags
  change: the language of the aliases named by the placeholder set in rule-guppi-config (case 476.2)
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `rule-case-build`
- [x] update `rule-ask`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] `uv run guppi render`: `.claude/agents/ask-guppi.md`
```

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

```then
update:
- slug: rule-prespec
  replace:
  - old: still holding a Cyrillic letter, a short form under `## Deferred` included — `case-guppi` writes English and a short form is shown in English;
    new: still holding a letter outside the script of {{documentation_lang}}, the language `guppi.toml` sets for the repository, a short form under `## Deferred` included — `case-guppi` writes {{documentation_lang}} and a short form is shown in {{documentation_lang}};
  change: the finding reads guppi.toml and looks for a letter outside the script of documentation_lang, not for Cyrillic (case 476.3)
- slug: estimate-language-spec-prose-in-english
  set:
    status: pending
    purpose: Pre-spec finds a name, context or problem of a Case of the plan that holds a letter outside the script of the documentation language of guppi.toml, a short form under Deferred included
    method: uv run pytest tests/test_prespec.py -k script
  change: the Criterion replaced whole — a letter outside the script of documentation_lang, read from guppi.toml, not a Cyrillic letter (case 476.3)
```

```tasks
- [x] update `rule-prespec`
- [x] update `estimate-language-spec-prose-in-english`
- [x] `guppi/config.py` — the script of a language's code, and whether a text holds a letter outside it
- [x] `guppi/ratified.py` — `untranslated` takes the language and imports the judgment from `guppi/config.py`; `CYRILLIC` removed
- [x] `guppi/prespec.py` — `check_untranslated` reads `guppi.toml` through `guppi/config.py`; the finding names the language; a missing file or an unknown code is one finding that names `guppi.toml`
- [x] `tests/test_prespec.py` — the tests `-k cyrillic` renamed `-k script`: `en` with a Cyrillic letter, a plan with none, a short form under `## Deferred`, a missing `guppi.toml`, an unknown code
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-language-spec-prose-in-english`
```

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

```then
update:
- slug: rule-language
  set:
    purpose: Keeps the repository in the documentation language and the chat with the owner in the chat language, both set in rule-guppi-config, a built Case whole in the documentation language in the file sent to the person, with slugs, paths and quotations unchanged in either
  replace:
  - old: Keeps the repository in English and the chat with the owner in Russian.
    new: Keeps the repository in the documentation language and the chat with the owner in the chat language, `documentation_lang` and `chat_lang` set in `rule-guppi-config` and rendered into `guppi.toml` — English and Russian in this project (case 476.4).
  sections:
    Render: |-
      <!-- rule-language -->
      ## Language

      {{documentation_lang}} for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. {{chat_lang}} for chat with the owner; a Case is {{documentation_lang}} whole — its name, `context`, `problem` and `recommend` too — in the file the agent sends the person and in the Spec, and the chat holds a short {{chat_lang}} text on each Case and sub-case, its ledger lines in {{documentation_lang}} as the file holds them; a short-form Case is {{documentation_lang}} in the chat, as the Spec holds it. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. Technical terms in {{documentation_lang}} are not transliterated in {{chat_lang}} text. The two languages are set in `rule-guppi-config`, rendered into `guppi.toml`.
      <!-- /rule-language -->
  change: the two languages named by the placeholders set in rule-guppi-config (case 476.4)
- slug: estimate-language-followed
  set:
    status: pending
    purpose: The section stands in CLAUDE.md with the languages set in rule-guppi-config, and what a session writes into the repository is in the documentation language, slugs and paths unchanged
    method: one reading by hand in the next session — CLAUDE.md against the Render of rule-guppi-config, and the session's commit, Spec and Case files against the section
  change: the Criterion replaced whole — the languages come from rule-guppi-config, and the language of the agent's text in the chat leaves the promise (case 476.4)
- slug: insight-session-reply-language-follows-the-english-text-read
  set:
    status: actioned
    addressed_by: decision-case-476.4
  change: 'actioned: the language of the chat leaves the promise of estimate-language-followed; a slip in the chat is fixed on the person''s request and gets no guard (case 476.4)'
```

```tasks
- [x] update `rule-language`
- [x] update `estimate-language-followed`
- [x] update `insight-session-reply-language-follows-the-english-text-read`
- [x] `uv run guppi render`: `CLAUDE.md`
- [x] read `estimate-language-followed` — by hand, in the session after the render
```

## Case 477 — A plain round, the skill wait-what, and a request for a plain explanation that is no failure

> **context:**
> `estimate-agent-writing-followed` is `failed`. In session 0000 the person asked three times for a plain explanation of a round of `case-guppi`: once on Case 472 and twice on Case 473. The same happened twice on Case 467 and once on Case 476. Case 466.1 had already added a `**Context:**` paragraph to the first round, and the requests went on. The round of 473 was dense because it packed frame facts into the Context and the question bodies: case numbers, slug histories and words like "stamped writer". The main agent's own explanation, which the person understood, was different. It gave the problem in two points and one concrete example ("the hook refused 13 ledger lines, and they were lost"), and it said what each option changes. On 476 a before/after example answered the request. Today no text says who answers such a request. `rule-case-protocol` sends "a question or a change of the person on a shown Case" to `case-guppi`, but the main agent answered the requests itself. The Result of `estimate-case-protocol-shows-the-built-case` records this.
> The person decided in two rounds. A round gets a sentence in `rule-case-build`: the mechanism with an example, a before and after for each option, case numbers only in the `➡️` line, and an unknown term explained. A new Estimate reads that sentence against the text of a round. A request for a plain explanation becomes a legal skill, `wait-what`, taken from github.com/mattpocock/skills with its name kept. The person or the main agent starts it. Such a request is then its normal use, not a complaint, because requests like it can come without end. The main agent explains, and it asks the `case-guppi` of the Case only for a fact of the Case.
> The vault's answer: no page or skill named `wait-what` or `explain` exists in `vault/wiki/`, `vault/archive/` or `.claude/skills/`. Every `create` carries a `ref`. `rule-skill-grill-me` is the pattern for the page of a skill.
> The frame. The sentence of `rule-case-protocol` on a question on a shown Case, and the line of the Criterion of `estimate-case-protocol-shows-the-built-case` that repeats it, would become false for a request for a plain explanation, so 477.3 changes both. `rule-case-build` tells `case-guppi` to answer every message with the Case or a round. A message of the main agent that asks for a fact would break that sentence, so 477.3 adds the answer to such a message. That answer opens with the line `**Fact:**`. Without the mark the main agent would show it as a round, because `rule-case-protocol` reads every answer with no Case heading as a round. So the sentence on a round and the line of the Criterion that repeats it except an answer with this mark. In that Criterion the `when` and three lines are changed on purpose, so the old wording of each is not carried: the line on the answers now excepts a request for a plain explanation, the line on a round now excepts an answer under `**Fact:**`, and the line on the request is new. Every other line is carried unchanged, "Russian" included, since Estimates keep this project's values (Case 476).
> The hook of `rule-case-check` needs no new line. Its How it works already takes as the answer the newest output of `case-guppi` that holds a Case heading. After a built Case, a fact answer makes the hook check and store that Case again and write its file with the same text. Before any Case, it is neither checked nor stored.
> Two Estimates stay untouched. The Criterion of `estimate-case-build-writes-the-case` states the form of a round and the messages that carry the person's words. The round sentence adds to that form, and the fact request is a message of the main agent outside its `when`, so no line of it becomes false. The person chose a separate promise for plainness. `estimate-skill-grill-me-asks-in-rounds` says the form of a round of `case-guppi` "is the promise of `estimate-case-build-writes-the-case`". Once 477.1 puts plainness into `estimate-case-build-writes-a-plain-round`, that line no longer names every promise on a round, but it is still true. It is not updated, because that Estimate is to be read in Work Mode of this session, and an update would push its reading to a later session (case 428.1).
> The Render of `rule-agent-writing` does not change. Case 476.2 of this session changes three phrases of the Render of `rule-case-build` and one phrase in `## Who builds a Case` of `rule-case-protocol` ("which the agent shows translated into Russian line by line"). The anchors of this Case are other text. The Render of `rule-skill-wait-what` holds `{{chat_lang}}`: the render puts in the name of the language that the `## Render` of `rule-guppi-config` (476.1) sets, and both land at the same librarian's run. No reader in code changes.
> Not done: no check counts the requests or reads a round by script. The Case file and the pages get no new sentence on plainness, because no request fell on them. The Render of `rule-agent-writing` stays as it is.

> **problem:**
> The rounds of `case-guppi` carry frame facts where the person needs the mechanism and the effect of each option, so the person asks for a plain explanation again and again. Each request fails `estimate-agent-writing-followed`, and no text says who answers the request or in what form.

### Case 477.1 — A round of case-guppi written in plain words

> **given:**
> `rule-case-build` — its Render, the paragraph on a round and its Context
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from `rule-case-build`
> **＋** `estimate-case-build-writes-a-plain-round` — the new promise
> **＋** `estimate-case-build-writes-the-case` — the form of a round, which stands

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
> **＋** Each question body says what each option changes, as a before and after.
> **＋** Case numbers, the history of a slug and facts of the frame stand in the round only in the `➡️` line of a question, as the source of its recommendation.
> **＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
> **－** The `context` of a Case keeps its case numbers and frame facts: the sentence is about a round only.

```then
create:
- slug: estimate-case-build-writes-a-plain-round
  type: estimate
  ref: rule-case-build
  kind: QA
  purpose: Whether a round of case-guppi gives the mechanism with a concrete example, a before and after for each option, case numbers only in the recommended answer, and an unknown term explained
  method: 'by hand, in a session after the render: one round of case-guppi read in the chat against the four parts of the Criterion'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: a part with nothing to say left out. A later round on the item
    new: 'a part with nothing to say left out. Write the round for a person who has not opened the pages: the context gives the mechanism in plain words with one concrete example of where it goes wrong; each question body says what each option changes, as a before and after; case numbers, the history of a slug and facts of the frame stay out of the context and the question bodies, and stand in the `➡️` line as the source of the recommendation, and in the `context` of the Case; a term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it (case 477.1). A later round on the item'
  change: a round of case-guppi gives the mechanism with a concrete example, a before and after for each option, case numbers only in the recommended answer, and an unknown term explained (case 477.1)
```

```tasks
- [x] update `rule-case-build`
- [x] create `estimate-case-build-writes-a-plain-round`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-writes-a-plain-round`
```

### Case 477.2 — The skill wait-what writes the last text again in plain words

> **given:**
> `rule-skill-wait-what` — the new Rule; its Render is the skill
> **＋** `.claude/skills/wait-what/SKILL.md` — the skill, rendered in full from `rule-skill-wait-what`
> **＋** `estimate-skill-wait-what-re-pitches` — the new promise
> **＋** `rule-plan-mode` — the parent of the skills of Plan Mode
> **＋** `vault/wiki/glossary.md` — the terms of the vault
> **＋** `rule-guppi-config` — the code of `chat_lang` that the render puts in (case 476.1)
> **＋** `.claude/agents/case-guppi.md` — the agent that holds the facts of its Case

> **when:**
> The person types `/wait-what` on `UserPromptSubmit`, or the main agent calls the skill on `PreToolUse Skill` when the person asks in words for a plain explanation of its last text, after `uv run guppi render` wrote `.claude/skills/wait-what/SKILL.md` from `rule-skill-wait-what`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/wait-what/SKILL.md` equals the Render of `rule-skill-wait-what`, with the name of the language that the `## Render` of `rule-guppi-config` sets for `chat_lang` in place of its placeholder.
> **＋** The main agent writes its last text again — a round, the short text on a Case or a reply — in the language of `chat_lang`, in short active sentences with one idea each.
> **＋** It opens with a little background, shows how the thing works on one real case, and names the effect of every choice the text offers.
> **＋** It holds no case number and no history of a slug, uses the terms of `vault/wiki/glossary.md`, and explains a term in a few words where it first stands.
> **＋** It takes a fact of a Case that the main agent does not hold from the `case-guppi` of that Case, never from a guess.
> **＋** It ends with the open question asked again.
> **－** No option and no recommendation of the last text changes.
> **－** The skill starts no Case and writes no ledger line.

```then
create:
- slug: rule-skill-wait-what
  type: rule
  ref: rule-plan-mode
  kind: Leaf
  purpose: Prevents a text the person did not understand from being explained again in the same dense words, or changed while it is explained
  enforcement: render
  governs: .claude/skills/wait-what/SKILL.md
  render_mode: full
  tags:
  - harness
  - workflow
  sections:
    Purpose: 'Prevents a text the person did not understand from being explained again in the same dense words, or changed while it is explained. `/wait-what` writes the agent''s last text again — a round of `case-guppi`, the short text on a Case, a reply — in the chat language, in plain words, with a concrete example and the terms of `vault/wiki/glossary.md`. It comes from the skill `wait-what` of github.com/mattpocock/skills and keeps its name. The upstream text asks for ASD-STE100 and `CONTEXT.md`: here they are short active sentences in the chat language and the glossary, since ASD-STE100 is a standard for English only. The main agent may start it too, when the person asks in words, so one text decides what a plain explanation holds. A request for it is its normal use, not a complaint about the agent''s text (case 477.2).'
    Render: |-
      <!-- rule-skill-wait-what -->
      ---
      name: wait-what
      description: "Stop. That last message did not land: re-pitch it. Run it when the person types /wait-what, or asks in words for a plain explanation of the agent's last text."
      ---

      Wait, I don't understand where you've got to here. Re-pitch your last text — a round of questions, the short text on a Case, or a reply — in {{chat_lang}}.

      Give a little context first. Then say the mechanism in plain words, with one concrete example of where it goes wrong. For each option, say what changes, as a before and after. Write short sentences, one idea per sentence, in the active voice.

      Leave out case numbers and the history of a slug. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.

      When you need a fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.

      Change no option and no recommendation. End with the open question, asked again.
      <!-- /rule-skill-wait-what -->
- slug: estimate-skill-wait-what-re-pitches
  type: estimate
  ref: rule-skill-wait-what
  kind: QA
  purpose: Whether the skill wait-what writes the agent's last text again in plain words in the chat language, with the open question asked again and no option changed
  method: uv run guppi render --check; by hand, in a session after the render, one run of the skill read in the chat, on the person's /wait-what or on a request in words
  tags:
  - harness
  - workflow
```

```tasks
- [x] create `rule-skill-wait-what`
- [x] create `estimate-skill-wait-what-re-pitches`
- [x] `uv run guppi render`: `.claude/skills/wait-what/SKILL.md`
- [x] read `estimate-skill-wait-what-re-pitches`
```

### Case 477.3 — The main agent answers a request for a plain explanation, case-guppi gives the facts

> **given:**
> `rule-case-protocol` and `vault/wiki/case-schema.md` — the section Who builds a Case, on what goes to `case-guppi` and what is a round
> **＋** `rule-case-build` and `.claude/agents/case-guppi.md` — the answer of `case-guppi` to a message
> **＋** `.claude/skills/grill-me/SKILL.md` and `.claude/skills/wait-what/SKILL.md` — the form of a round, and the plain explanation
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a shown Case, written by the hook of `rule-case-check`
> **＋** `.claude/agents/ask-guppi.md` — dispatched once, at pre-spec
> **＋** `estimate-case-protocol-shows-the-built-case` — its Criterion replaced whole

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, then its own text after one horizontal rule.
> **＋** A reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`, and so do the person's answers to a round of questions, verbatim and untranslated.
    new: 'A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`, and so do the person''s answers to a round of questions, verbatim and untranslated. A request for a plain explanation — of a round, of the short text on a Case or of a reply, by `/wait-what` or in the person''s words — is not such a question: the main agent answers it itself by the skill `wait-what` (`rule-skill-wait-what`), and asks the `case-guppi` of the Case by `SendMessage` only for a fact of the Case it does not hold; `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading (case 477.3).'
  - old: an answer with no Case heading is a round of questions by the skill `grill-me` (`rule-case-build`),
    new: an answer with no Case heading and no first line `**Fact:**` is a round of questions by the skill `grill-me` (`rule-case-build`),
  change: a request for a plain explanation is answered by the main agent with the skill wait-what; case-guppi is asked only for a fact of its Case and answers under a Fact line, which is not a round (case 477.3)
- slug: rule-case-build
  replace:
  - old: Asked again by a message, answer with the Case whole again, changed as asked, or with a round when the message opens a fork.
    new: Asked again by a message, answer with the Case whole again, changed as asked, or with a round when the message opens a fork. A message that asks you for a fact of the Case, so that the main agent can explain the Case to the person in plain words, you answer with the fact alone, in plain words, under a first line `**Fact:**`, with no Case heading and no round (case 477.3).
  change: case-guppi answers a request of the main agent for a fact of its Case with the fact alone, under a Fact line (case 477.3)
- slug: estimate-case-protocol-shows-the-built-case
  set:
    status: pending
    method: by hand, the Cases of a session at its close, their context against the Agent calls and their showings against the SendUserFile calls of the transcript, and each request for a plain explanation against the Skill and SendMessage calls
  change: the Criterion replaced whole — a request for a plain explanation is answered by the main agent with the skill wait-what, and case-guppi gives only a fact, under a Fact line that is not a round (case 477.3)
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `rule-case-build`
- [x] update `estimate-case-protocol-shows-the-built-case`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-protocol-shows-the-built-case`
```

### Case 477.4 — A request for a plain explanation is no complaint about the agent's text

> **given:**
> `estimate-agent-writing-followed` — its Criterion replaced whole
> **＋** `CLAUDE.md` — the section `## How the agent writes`
> **＋** `rule-agent-writing` — its Render, which does not change
> **＋** `.claude/skills/wait-what/SKILL.md` — the skill that re-pitches a text the person did not follow

> **when:**
> A session starts with `CLAUDE.md` loaded, and the agent writes a text — a reply, a page, a commit message, a document.

> **then:**
> The person raised no complaint in the session that the agent's text broke the section `## How the agent writes` of `CLAUDE.md` — a claim with no real source or wider than the output it rests on, a sales pitch, a long or passive sentence, an answer not given first, a not-done left implied.
> **－** A slip in the agent's text that the agent found and corrected itself, with no complaint of the person, is no fault.
> **－** When the person says they did not follow and wants it said more simply, by `/wait-what` or in words, that is the normal use of `.claude/skills/wait-what/SKILL.md`, not a fault of this rule.
> **－** The code the agent writes is not a text of this rule; `make style` judges the code.

```then
update:
- slug: estimate-agent-writing-followed
  set:
    status: pending
  change: the Criterion replaced whole — a request for a plain explanation, answered by the skill wait-what, is no complaint (case 477.4)
```

```tasks
- [x] update `estimate-agent-writing-followed`
- [ ] read `estimate-agent-writing-followed` — by hand, in the session after the render
```

## Case 478 — The file-route Estimate says which lint findings it covers, and the close of a sprint gets a note

> **context:**
> `make lint` prints one line per finding, in the form `<category>/<slug>: <class>: <what>`. `guppi/lint.py` also prints findings on the `schema.yaml` of a category folder. Those findings are named `<category>/schema`, with the class `schema-description` or `schema.yaml is missing`. The Criterion of `estimate-sprint-migration-file-route-gone` ends with "`make lint` has no finding on a schema". The line can be read two ways. If it means "no finding of the class `schema`", it fails today on 64 findings: 62 on the Decision pages of cases 1–28 and 2 on `rule-spec-box`. If it means "no finding on a `<category>/schema`", it passes. The brief lists 98 lint findings, and none of them is on a schema file. Case 320 wrote the line when the file route was the way to change the schema files by hand. The first reading of 2026-09-22 recorded "no finding on a <category>/schema". The Estimate is `pending`. The main agent ran the grep of its `method` on `guppi/` today and it found no match.
> The person decided in one round. The line means no finding on a `<category>/schema`. The Criterion is replaced whole with that wording, and `purpose` and `method` are reworded to match. The person also asked whether an Estimate like this one goes to the archive once its condition holds. An Estimate has three statuses, `pending`, `passed` and `failed`, and no status for "done". The only way to remove it is a `delete`. The person chose to keep the Estimate live until the sprint closes, so that it still catches a regression. The general rule is that the sprint page and its Estimates go to the archive together at the close of a sprint. It belongs to Slice 5 and is not decided here. It becomes a note in the Slice 5 milestone of `entity-sprint-migration`. Under `rule-sprint`, a note is a line with no wikilink before the ` — `: a task not yet cut into pages, never ticked. At pre-spec, the check of the plan found two parts of the note that the `then` of 478.2 did not state: the condition "once each has passed" and the reason. The person accepted the fix, and the `then` of 478.2 now states both.
> The vault's answer: no `create`, so no vault query ran. The frame. Each line of the old Criterion is carried unchanged, except the lint line, which is changed on purpose, so the check notes it as not carried. 478.1 adds a `－` line that leaves the findings on pages to `estimate-sprint-migration-lint-clean`. That Estimate promises that `make lint` exits 0 at the close of the sprint. It stays true and is not touched. The Purpose of `entity-sprint-migration` says "the `file` route out of the scripts", which stays true. The Criterion of `estimate-sprint-migration-lint-clean` wants each item of `## Milestones` to be "a wikilink to a page or a plain line", and the note is a plain line. Under `rule-sprint`, the note keeps Slice 5 open until a Case cuts it or removes it. Slice 5 already stands open. No reader in code changes.
> Not done: this session cannot read the Estimate, because a Case of this session replaces its Criterion (case 428.1). The brief listed it under Work, and it now moves to a later session. The Estimate is not deleted. No rule on the close of a sprint is written, and no Estimate is archived.

> **problem:**
> One line of the Criterion of `estimate-sprint-migration-file-route-gone` has two readings: one passes today and one fails. A reader cannot tell which reading the promise means. No page says what happens to the Estimates of a sprint when it closes.

### Case 478.1 — The lint line of the file-route Estimate names the findings on a category schema

> **given:**
> `estimate-sprint-migration-file-route-gone` — the promise that the file route is gone; its Criterion replaced whole
> **＋** `guppi/` — the scripts the file route left
> **＋** `guppi/generate.py` — applies or fails the entry of each kind, and ticks the line of an applied entry
> **＋** `guppi/materialize.py` — `category_of` gives the entry of a slug with no prefix `category: unknown`
> **＋** `guppi/prespec.py` — `check_governed` refuses an `update` item that carries `file`
> **＋** `guppi/lint.py` — reports a finding on the `schema.yaml` of a category folder as `<category>/schema`
> **＋** `estimate-sprint-migration-lint-clean` — the promise of `make lint` at the close of the sprint, which stands
> **＋** `vault/wiki/sprint.md` — shows the `purpose` of the Estimate

> **when:**
> `generate` applies a `materialize.yaml` that holds an entry lifted from a ledger line whose slug has no category prefix.
> **＋** `make test` and `make lint` run on the tree.

> **then:**
> No file under `guppi/` holds `RULE_CLASS`, `rule_class`, `applied by hand` or `prose_names`.
> **＋** An `update` item that carries `file` is a `pre-spec` finding: `check_governed` refuses any such item, not only one on a governed path.
> **＋** The entry of a ledger line whose slug has no category prefix lands `category: unknown`.
> **＋** `generate` fails a `create` of that entry, and a `defer` of it with no page, with `category 'unknown' is not a vault folder`.
> **＋** `generate` applies an `update` of that entry to the page of that slug in any folder, and ticks its line.
> **＋** `generate` applies a `delete` of that entry with the stdout line `outside the vault, nothing to archive`, and ticks its line.
> **＋** `make test` is green, and `make lint` prints no finding on a `<category>/schema`, the `schema.yaml` of a category folder.
> **－** `generate` prints "applied by hand" for no entry.
> **－** A `make lint` finding on a page, a missing field or section of a Decision page or a rule page included, is outside this promise: `estimate-sprint-migration-lint-clean` holds it.

```then
update:
- slug: estimate-sprint-migration-file-route-gone
  set:
    status: pending
    purpose: The file route is out of the scripts — no RULE_CLASS, rule_class, applied by hand or prose_names in guppi/; an update item with file is a pre-spec finding; a slug without a prefix lands category unknown; tests green and no lint finding on the schema.yaml of a category folder
    method: rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/ empty; uv run pytest tests/test_generate.py -k unknown — the update applied in any folder, the create and the page-less defer failed, the delete outside the vault; make test; make lint — no line on a <category>/schema
  change: the Criterion replaced whole — the lint line names the findings on a <category>/schema, and a finding on a page is left to estimate-sprint-migration-lint-clean; purpose and method reworded to match (case 478.1)
```

```tasks
- [x] update `estimate-sprint-migration-file-route-gone`
- [x] `uv run guppi sprint`
- [x] read `estimate-sprint-migration-file-route-gone`
```

### Case 478.2 — A note in Slice 5: the sprint page and its Estimates go to the archive together at the close

> **given:**
> `entity-sprint-migration` — the Slice 5 milestone, the closing of the sprint
> **＋** `rule-sprint` — a line with no wikilink before the ` — ` is a note, never ticked
> **＋** `vault/wiki/sprint.md` — rendered from the sprint page by `uv run guppi sprint`

> **when:**
> Someone reads the Slice 5 milestone of `entity-sprint-migration`, or `vault/wiki/sprint.md` after `uv run guppi sprint`.

> **then:**
> Slice 5 holds a note: at the close of a sprint, once each Estimate the sprint page lists has passed, the sprint page and those Estimates go to the archive together.
> **＋** The note gives its reason: a done-condition of a sprint has nothing left to guard after the close.
> **＋** The note is never ticked, and it keeps Slice 5 open until a Case cuts it into pages or removes it.
> **－** No Estimate goes to the archive, and no status changes: the note decides nothing.

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: '- [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239'
    new: |-
      - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
      - the close of a sprint — `entity-sprint-<id>` and the Estimates it lists go to the archive together once each has passed: a done-condition of a sprint has nothing left to guard after the close; not yet decided (case 478.2)
  change: 'a note in Slice 5: the sprint page and its Estimates go to the archive together at the close of a sprint, once each has passed (case 478.2)'
```

```tasks
- [x] update `entity-sprint-migration`
- [x] `uv run guppi sprint`
```

## Case 479 — Work Mode gets the skill /work: the fork asks for it, it writes a baseline and the marks of an expected red, and Retro reads both

> **context:**
> Some Cases change a check in code and also the page that the check reads. The new code runs as soon as it is written, but the page changes only at the librarian's run. Between those two moments `make lint` is red, and that is expected. Today one sentence of `rule-retro` (case 473.1) turns such a red into a note for the handoff. It does this by the agent's own judgment at `/retro`. Nothing marks the red at the moment it is caused. Nothing records which reds stood before the work either, so at Retro the agent cannot tell a red this session caused from a red it found. `rule-work-mode` should hold that part, but it is a `draft` with only a Purpose ("Prevents implementation starting before the plan, branch and baseline exist"). It has no text that a session loads, and 20 Cases defer it. After `ExitPlanMode` the hook `guppi spec` tells the agent to ask in words: Work Mode or `/carry`. `/carry` is a skill, and Work Mode is none.
> The person decided in two rounds. `rule-work-mode` is taken up with a minimum. It holds the Render of a new skill, `/work`. The skill stops on `main`. Before the first change it writes a baseline, the result of `make test` and `make lint`, into `raw/<date>/<hi HHMM>/work.md`. It runs the tasks in order and ticks each box. When a task changes a check that reads a page or a governed file the same Spec updates, it writes a line under `## Expected red` of the same file, naming the check and the page or file. The agent calls `/work` when the person picks it at the fork, and the person may type it to resume. The fork is asked by `AskUserQuestion` with the two options `/work` and `/carry`. Retro reads `work.md`. A red on a page or file that a mark names ends as a note for the handoff. A red line that the baseline already holds is not charged to the session, whatever the marks name. Any other red is debt. In a session with no `work.md`, the sentence of 473.1 stands as it is. `work.md` joins the allow list of `rule-permissions`.
> The person then changed 479.2. The skill takes the branch and the baseline through `!` substitutions that run when it loads. `insight-hi-skill-substitution-checked-by-a-model-call` records that a model call checks such a command before it runs, and that the substitution comes back empty when that call fails. In this session the permission classifier failed to answer several times. With an empty substitution, `## Baseline` would be empty, and Retro would charge every red to the session. So when a substitution is empty, the agent runs that command itself before it goes on. The Insight stays in the backlog as it is.
> At pre-spec the person accepted three fixes. First, a red counts as expected only on the page or file a mark names. Before this fix, one mark on `make lint` would have excused an unrelated new finding. Second, a line the Baseline holds is not debt under any mark. Before this fix, 479.3 and 479.4 contradicted each other. Third, the text of `rule-retro` keeps 473.1 for a session with no `work.md`.
> The vault's answer: every `create` carries a `ref`, so no vault query ran. A Glob of `vault/**/` finds no page for `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` or `estimate-retro-red-in-the-baseline-is-not-charged`. 479.2 names `rule-work-mode`, so it carries one `{supersedes:case N}` block for each of the 20 Cases in its `deferred_by`. The Backlog entry of `rule-work-mode` in `entity-sprint-migration` still names the sentence of `insight-workflow-code-live-before-the-page-it-reads` and case 238. Case 473 placed that sentence in `rule-retro` and 473.2 retired 238, so 479.2 rewrites the entry to the part of Work Mode that is left. `vault/wiki/sprint.md` does not show the Backlog, so no sprint render follows.
> The frame. The rule "never a picker tool" of `vault/wiki/case-schema.md` (case 355.1) is about the ratification of a Case. The fork is the end of a session, not a Case, so the rule stays true, and 479.1 says so in a `－` line. The Render of `rule-carry-over` says it runs "when the person answered the fork with 'conserve'". The `/carry` option is described as conserving the Spec, so that sentence and `estimate-carry-over-writes` stay true. The Criterion of `estimate-session-phases-in-order` lists the marks of a session and does not list `work.md`. A new mark of Work Mode makes no line of it false, so it is not touched. `estimate-guppi-tests-green` still wants `make test` with no failed test on the branch. A test that was red in the baseline stays red there, and 479.4 says so. `estimate-retro-loads` and `estimate-retro-report-holds-each-fact-once` promise the readings and the form of the report. They make no promise about the first read call of Retro, which 479.3 changes, so neither is touched. The glossary row for Work Mode describes the planned model with subagents and stays.
> The replaced Criteria carry their old lines word for word, except these lines, which change on purpose. In 479.1, the line on the stdout named "Work Mode on the Spec or `/carry`". It becomes the stdout line and the line on `AskUserQuestion` with `/work` and `/carry`. In 479.3, the line on the frontier item now requires a mark on the page or file. The line on a red test keeps "fixed or reverted into a patch" and loses "the handoff still needs green", because 479.4 lets the commit wait for no test that was red in the baseline. That exception follows from the person's answer that a baseline red is not charged. In 479.5, `when` adds `work.md`. The line on the allow list names the entries with `work.md` added and no count. The line "Nothing else under `wiki/` is allowed." is dropped, because the carried line on `deny` and `ask` says the same.
> Timing. `guppi/spec.py` runs from the working tree at once. `.claude/skills/work/SKILL.md`, the Retro text and the allow list land at the librarian's render. So an `ExitPlanMode` later in this session would offer `/work` before the skill exists, and the agent would then run Work Mode as it does today. No reader refuses anything, so nothing is lost and no old form is kept.
> Not done: subagents in Work Mode (`rule-subagent-guppi`), the test of each Estimate written first, the Spec box (`rule-spec-box`), and the full Work Mode model the person plans. No script compares a red with `work.md`. The agent reads the file by hand at Retro. 19 of the 20 superseded Decisions, cases 183 to 322, also defer `rule-subagent-guppi`. `generate` clears a defer only from the pages the superseding Case names, so those defers stay on `rule-subagent-guppi` and point at superseded Decisions. The person chose to leave them: the Case that takes up `rule-subagent-guppi` retires them.

> **problem:**
> Work Mode has no text a session loads. It takes no baseline and checks no branch, and it marks nothing when it causes an expected red. So Retro judges each red on its own: an expected red and a red that stood before the work cannot be told apart from a red the session caused. The fork after `ExitPlanMode` also names Work Mode as plain words while `/carry` is a skill.

### Case 479.1 — The fork after ExitPlanMode asks by AskUserQuestion: /work or /carry

> **given:**
> `guppi/spec.py` — `fork_line` and the docstring, the line the hook prints after the Spec is written
> **＋** `tests/test_spec.py` — the tests of the printed fork
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec, which the hook writes
> **＋** `/hi` — opens the session; without its `hi` line the hook writes no Spec
> **＋** `rule-spec-capture` — its Purpose, on the fork
> **＋** `.claude/skills/work/SKILL.md` and `.claude/skills/carry/SKILL.md` — the two skills of the fork
> **＋** `vault/wiki/case-schema.md` — a Case ends with a plain question, never a picker tool
> **＋** `estimate-spec-capture-appends` — the writing of the Spec, which stands
> **＋** `estimate-spec-capture-offers-the-fork` — its Criterion replaced whole

> **when:**
> `guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec, or found it already there.

> **then:**
> The stdout of the hook is one JSON object, `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, that holds the fork line with the session folder and the Spec file.
> **＋** For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
> **＋** The agent sees this line in the `ExitPlanMode` result.
> **＋** The fork line tells the agent to ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (the Spec conserved for a later session), and to start nothing until the person answers.
> **＋** On the answer, the agent calls `.claude/skills/work/SKILL.md` or `.claude/skills/carry/SKILL.md`, the skill of the option picked.
> **－** A `PostToolUse` hook blocks nothing: the tool has run.
> **－** Without a Spec, nothing, as before.
> **－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.
> **－** A Case is still ratified by the person's reply in the chat, never by a picker tool, as `vault/wiki/case-schema.md` says: the picker is for the end of the session only.
> **－** The writing of the Spec does not change: that is the promise of `estimate-spec-capture-appends`.

```then
update:
- slug: rule-spec-capture
  replace:
  - old: into the context — Work Mode, or `/carry` to conserve the Spec — naming the session folder and the Spec file; it blocks nothing, the agent asks and the person chooses (case 190.5).
    new: 'into the context — `/work`, Work Mode on the Spec, or `/carry` to conserve it — naming the session folder and the Spec file; it blocks nothing: the agent asks the person by `AskUserQuestion` with the two options, the person picks, and the agent calls the skill picked (cases 190.5, 479.1).'
  change: the fork is asked by AskUserQuestion with the two options /work and /carry, and the agent calls the skill picked (case 479.1)
- slug: estimate-spec-capture-offers-the-fork
  set:
    status: pending
    purpose: 'The hook prints the fork after the Spec is written: the agent asks by AskUserQuestion with the options /work and /carry, and calls the skill picked'
    method: 'uv run pytest tests/test_spec.py -k fork; by hand, the first ExitPlanMode of a session after the render: the fork asked by AskUserQuestion with /work and /carry, and the skill picked called'
  change: the Criterion replaced whole — the fork is asked by AskUserQuestion with /work and /carry, and the skill picked is called (case 479.1)
```

```tasks
- [x] update `rule-spec-capture`
- [x] update `estimate-spec-capture-offers-the-fork`
- [x] `guppi/spec.py` — `fork_line`: ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (conserve it for a later session, the brief rewritten, `carry.md` as the mark, a commit), start nothing until answered, then call the skill picked; the module docstring names `/work`
- [x] `tests/test_spec.py` — `-k fork`: the line holds `AskUserQuestion`, `/work` and `/carry`, the session folder and the Spec file; the fork printed again when the plan was already there; no fork without a Spec
- [x] read `estimate-spec-capture-offers-the-fork` — by hand, at the first `ExitPlanMode` of a session after the render
```

### Case 479.2 — rule-work-mode holds the skill /work: branch, baseline, tasks in order, the mark of an expected red

> **given:**
> `rule-work-mode` — the Rule of Work Mode, taken up; its Render is the skill
> **＋** `.claude/skills/work/SKILL.md` — the skill, rendered in full from `rule-work-mode`; its `!` substitutions run when it loads
> **＋** `raw/<date>/<hi HHMM>/work.md` — the baseline and the marks of an expected red, written by the skill
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec, its tasks and boxes
> **＋** `git branch --show-current`, `make test` and `make lint` — the commands of the branch check and of the baseline
> **＋** `vault/wiki/` — the pages, which only the librarian's run writes
> **＋** `entity-sprint-migration` — its Backlog entry on `rule-work-mode`
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — the new promise

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task.
> **＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.

```then
create:
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  type: estimate
  ref: rule-work-mode
  kind: QA
  purpose: Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec in order with their ticks, and marks an expected red under Expected red
  method: 'uv run guppi render --check; by hand, in a session after the render, the first /work the agent calls at the fork and the first /work the person types: the branch, work.md, the ticks of spec.md and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent''s own run of its command, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-work-mode
  set:
    kind: Leaf
    enforcement: render
    governs: .claude/skills/work/SKILL.md
    render_mode: full
    tags:
    - session
    - workflow
    - harness
    - render
  sections:
    Purpose: 'Prevents implementation starting before the plan, branch and baseline exist. Work Mode runs the approved Spec of the session. Its skill `/work` starts after `ExitPlanMode`: the agent calls it when the person picks `/work` at the fork, and the person types it to resume a session that stopped in the middle. It stops on `main`. Before the first change it writes the baseline, the result of `make test` and `make lint`, into `raw/<date>/<hi HHMM>/work.md`, so that Retro charges to the session only a red the baseline does not hold. A substitution of the skill can come back empty when the model call that checks it fails, so the agent then runs the command itself. It runs the tasks in the order of the Spec and ticks each box. A task that changes a check that reads a page or a governed file the same Spec updates writes a mark of an expected red into the same file, naming the check and the page or file, and Retro reads it. Subagents in Work Mode, the test of each Estimate written first and the rest of the model are not decided yet (case 479.2).'
    Render: |-
      <!-- rule-work-mode -->
      ---
      name: work
      description: Work Mode on the approved Spec — check the branch, write the baseline, run the tasks in order and tick each box. The agent calls it when the person picks /work at the fork ExitPlanMode prints; the person types it to resume.
      ---


      Branch: !`git branch --show-current`

      Tests: !`make test`

      Lint: !`make lint`

      A line above can come back empty when the check of its command fails. When Branch is empty, run `git branch --show-current` yourself before anything else. When Tests or Lint is empty, run `make test` and `make lint` yourself before the first change, and use their result for the Baseline.

      Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. If the branch is `main`, stop and say so: Work Mode does not start on `main`. Write and change nothing until the person moves to another branch and `/work` runs again.

      Otherwise, before the first change, write `vault/raw/<date>/<hi HHMM>/work.md` with two sections. `## Baseline`: the exit code of `make test` and of `make lint`, then each failing test and each lint finding line as printed. `## Expected red`: empty for now. When `work.md` already stands, because the person typed `/work` to resume, keep its Baseline as it is: the baseline is taken once, before the first change.

      Run the tasks of the Spec in the order the Spec holds them. Tick each box of code, a test, a migration or a `by hand` check in `spec.md` in the reply that finishes the task. The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here.

      When a task changes a check — `make lint` or one of its steps, or a hook of the working tree — that reads a page or a governed file this Spec updates, add one line under `## Expected red` in the same reply: the check, and the page or file it waits for. That check is red or refuses on that page or file until the librarian's run, and `/retro` ends that red as a note for the handoff.

      Work Mode ends with `/retro`.
      <!-- /rule-work-mode -->
  change: 'taken up: the skill /work — the branch, the baseline in work.md with the agent''s own run when a substitution is empty, the tasks in order with their ticks, the mark of an expected red; every defer retired (case 479.2)'
- slug: entity-sprint-migration
  replace:
  - old: '- [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; the sentence of [[insight-workflow-code-live-before-the-page-it-reads]] on a check that reads a page the same Spec changes; cases 183, 206, 238'
    new: '- [[rule-work-mode]] — the rest of Work Mode past the skill `/work` of case 479.2: the test of each Estimate written first and turned green, and the full model the person plans; cases 183, 206'
  change: the Backlog entry of rule-work-mode names what is left past the skill /work; the sentence on a red check stands in rule-retro (case 479.2)
```

```tasks
- [x] update `rule-work-mode`
- [x] create `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [x] update `entity-sprint-migration`
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — by hand, in a session after the render
```

### Case 479.3 — Retro ends a red on a page or file that Expected red names as a note for the handoff

> **given:**
> `rule-retro` — its Render: the opening of the frontier, and the sentence on a check red before the librarian's run
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `raw/<date>/<hi HHMM>/work.md` — its `## Expected red` and `## Baseline`, written by `/work`
> **＋** `make lint` — the checks of the vault, run by the librarian after the render
> **＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — its Criterion replaced whole

> **when:**
> The person invokes `/retro` in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

> **then:**
> When it opens the frontier, the agent reads `raw/<date>/<hi HHMM>/work.md` if it stands, and makes no other read call.
> **＋** A red or a refusal of a check on a page or file that a line of `## Expected red` of `work.md` names with that check is an item of the frontier, and it ends as a note for the handoff that names the check and the page or file it waits for.
> **－** The red is not debt: the agent does not fix it or revert it into a patch.
> **＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
> **＋** A red or a refusal on a page or file that no line of `## Expected red` names is debt, even when another line names the same check, unless `## Baseline` of `work.md` holds its line.
> **－** In a session with no `work.md`, a red or a refusal of such a check ends as a note for the handoff by the agent's judgment, as it did before `/work`.
> **－** A red test is never an expected red, even when `## Expected red` names it: it is fixed or reverted into a patch by the rule for red tests.

```then
update:
- slug: rule-retro
  replace:
  - old: Open with the frontier, in one message and with no read call.
    new: Open with the frontier, in one message and with no read call but the Read of `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3).
  - old: 'such a red is an item of the frontier that ends as a note for the handoff, naming the check and the page or file it waits for, and it is not debt. A red test is not such a check: it is fixed or reverted as above (case 473.1).'
    new: '`/work` marks such a red under `## Expected red` of `work.md` when the task that changes the check runs, one line naming the check and the page or file it waits for. A red or a refusal of that check on a page or file a line names is an item of the frontier that ends as a note for the handoff, naming the check and the page or file it waits for, and it is not debt; a red or a refusal on a page or file no line names is debt, even when another line names the same check, unless `## Baseline` holds its line. In a session with no `work.md`, such a red ends as a note for the handoff by your judgment, as before. A red test is never an expected red: it is fixed or reverted as above (cases 473.1, 479.3).'
  change: Retro reads work.md, and a red on a page or file that its Expected red names ends as a note for the handoff; any other such red is debt unless the Baseline holds it; with no work.md the judgment of case 473.1 stands (case 479.3)
- slug: estimate-retro-red-check-of-an-updated-page-is-a-handoff-note
  set:
    status: pending
    purpose: Whether Retro reads work.md and ends a red or a refusal on a page or file that a line of its Expected red names as a note for the handoff, not as debt, while a red on a page or file no line names is debt unless the Baseline holds it, a session with no work.md keeps the judgment of case 473.1, and a red test is never an expected red
    method: one reading by hand at the first /retro after the render in a session whose work.md names a check under Expected red, recorded in the estimate line
  change: the Criterion replaced whole — the red is expected when a line of Expected red of work.md names its check and its page or file, not by the agent's judgment; with no work.md the judgment stands (case 479.3)
```

```tasks
- [x] update `rule-retro`
- [x] update `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — by hand, at the first such `/retro` after the render
```

### Case 479.4 — Retro does not charge a red that the baseline already holds

> **given:**
> `rule-retro` — its Render: the paragraph on red tests, and the commit
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `raw/<date>/<hi HHMM>/work.md` — its `## Baseline` and `## Expected red`, written by `/work`
> **＋** `make test`, `make style` and `make lint` — the checks of the baseline and of the commit
> **＋** `estimate-guppi-tests-green` — `make test` with no failed test on the branch, which stands
> **＋** `estimate-retro-red-in-the-baseline-is-not-charged` — the new promise

> **when:**
> The person invokes `/retro` in a session whose `raw/<date>/<hi HHMM>/work.md` holds a `## Baseline`, and a test fails in the `make test` of Retro, or a lint finding stood in Work Mode.

> **then:**
> Retro counts each failing test and each lint finding line that `## Baseline` holds as red before the work, whatever `## Expected red` names, and writes it in the handoff as a note.
> **＋** It is not debt: nothing is fixed or reverted into a patch for it, and it gets no `lesson[error]` line.
> **＋** The commit of Retro needs `make style` clean and `make test` green, except for the failing tests that `## Baseline` holds.
> **＋** A failing test that `## Baseline` does not hold is fixed or reverted into a patch, as before.
> **－** Without `work.md` there is no baseline, and no red is excused as red before the work.
> **－** `estimate-guppi-tests-green` still wants `make test` with no failed test on the branch: a red test of the baseline stays red there.

```then
create:
- slug: estimate-retro-red-in-the-baseline-is-not-charged
  type: estimate
  ref: rule-retro
  kind: QA
  purpose: Whether Retro ends a failing test or a lint finding that the Baseline of work.md already holds as a note for the handoff, not debt, whatever Expected red names, and commits with make test green but for those tests
  method: one reading by hand at the first /retro after the render in a session whose work.md Baseline holds a failing test or a lint finding line, recorded in the estimate line
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-retro
  replace:
  - old: cause says why Retro was reached with a regression; the handoff still needs green.
    new: 'cause says why Retro was reached with a regression; the handoff still needs green. A failing test or a lint finding line that `## Baseline` of `work.md` already holds was red before the work, whatever `## Expected red` names: it is an item of the frontier that ends as a note for the handoff, named as red before the work; it is not debt, nothing is fixed or reverted for it, and no lesson is written for it (case 479.4).'
  - old: commit (`make style` clean, `make test` green), then call `/handoff`.
    new: commit (`make style` clean, `make test` green but for the tests that `## Baseline` of `work.md` holds), then call `/handoff`.
  change: a red that the Baseline of work.md holds is a note for the handoff under any Expected red, not debt, and the commit does not wait for it (case 479.4)
```

```tasks
- [x] update `rule-retro`
- [x] create `estimate-retro-red-in-the-baseline-is-not-charged`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-red-in-the-baseline-is-not-charged` — by hand, at the first such `/retro` after the render
```

### Case 479.5 — work.md joins the working files the session writes without asking

> **given:**
> `rule-permissions` — its Purpose and its Render, the allow list
> **＋** `.claude/settings.json` — rendered in part from `rule-permissions`
> **＋** `tests/test_render.py` — the JSON case, which fixes the shape of the block
> **＋** `raw/<date>/<hi HHMM>/work.md` — the new working file of the session
> **＋** `frontier.md`, `spec.md`, `handoff.md` and `carry.md` under `vault/raw/**`, and `vault/wiki/brief.md` — the working files already allowed
> **＋** `estimate-permissions` — its Criterion replaced whole

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, and Edit and Write for `vault/wiki/brief.md`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit outside the plan file, allow list or not.
> **＋** A prompt in Plan Mode, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed.

```then
update:
- slug: rule-permissions
  replace:
  - old: 'The Frontier, the Spec, the handoff, the carry mark and the brief of `/carry` are the session''s own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec,'
    new: 'The Frontier, the Spec, the work file, the handoff, the carry mark and the brief of `/carry` are the session''s own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec and writes `work.md` (case 479.5),'
  - old: '"Write(vault/raw/**/handoff.md)",'
    new: |-
      "Write(vault/raw/**/handoff.md)",
            "Edit(vault/raw/**/work.md)",
            "Write(vault/raw/**/work.md)",
  change: work.md, the baseline and the marks of an expected red, joins the allow list (case 479.5)
- slug: estimate-permissions
  set:
    status: pending
    method: the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of work.md in Work Mode, recorded in the estimate line — never the agent's, which cannot see the prompt
  change: the Criterion replaced whole — Edit and Write for work.md join the allow list (case 479.5)
```

```tasks
- [x] update `rule-permissions`
- [x] update `estimate-permissions`
- [x] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-permissions` — by hand, in a session after the render
```

## Deferred

## Case 480 — case-guppi checks its own sub-cases against each other before it answers

> **context:**
> At the pre-spec of session 1318 the check of `ask-guppi` found contradictions inside single Cases, between sibling sub-cases built by one `case-guppi`: 479.3 and 479.4 judged the same red in `rule-retro` two ways, and the sub-cases of 476 said two different things about what the render reads. Each sentence was written for its own sub-case, and no one compared the finished texts on one page before the Case was shown. They were caught only at pre-spec, and the four Cases were ratified again.

> **problem:**
> A Case whose sub-cases change one page reaches the person with texts that contradict each other, and the fault is found only at pre-spec, at the cost of a second ratification.

```then
defer:
  - slug: rule-case-build-checks-its-sub-cases
    type: rule
    purpose: Before it answers, case-guppi reads the finished new texts of all its sub-cases that change one page side by side, and fixes a contradiction between them before the Case is shown
```

## Case 481 — The pre-spec language finding counts the Latin slugs of a code span in a documentation language of another script

> **context:**
> Case 476.3 made the pre-spec finding look for a letter outside the script of `documentation_lang` in the name, `context` and `problem` of a Case. The `context` and `problem` of every Case hold slugs and paths in code spans, and they are Latin. For `en` this changes nothing. For a documentation language of another script, such as `ru`, each of those slugs is a letter outside the script, so the finding would stand on almost every Case. Work Mode of session 1318 found this while writing the tests of 476.3; the name after the heading's dash is judged alone, which the fix of that session covers, but the code spans are not.

> **problem:**
> The finding cannot tell a word written in the wrong language from a slug or path in a code span, so for a documentation language that is not written in Latin script it reports every Case.

```then
defer:
  - slug: rule-prespec-script-skips-code-spans
    type: rule
    purpose: The pre-spec language finding judges the prose of a name, context or problem without its code spans, so a Latin slug in a code span is no letter outside the script of the documentation language
```
