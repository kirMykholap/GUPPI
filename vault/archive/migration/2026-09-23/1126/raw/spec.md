<!-- approved 12:49:48 · session 055bb0b2 -->

# Spec — 2026-09-23, session 1126

## Case 363 — `/hi` writes the Frontier in plan mode

> **context:**
> `/hi` writes `frontier.md`, and its lines are closed in the replies of Plan Mode, all inside Claude Code's plan mode, whose text forbids any edit but the plan file. The leave exists already: `rule-permissions` counts the Frontier among the session's own working files, and `settings.json` allows `Write` of `vault/raw/**/frontier.md`; the lesson `lesson-plan-mode-frontier-refused-on-the-client-text` (2026-09-16) recorded the same refusal. Neither the page nor the lesson is in the agent's context at `/hi`, and in this session the refusal came again. The rule must stand in the text of the skill itself.
> `rule-skill-hi` stands `draft`; the Case touches `estimate-hi-writes-frontier`, not `estimate-hi-no-read-calls`; the lesson is of another session, so no `{addresses:…}` mark; no `create`.

> **problem:**
> The text of `/hi` says to write `frontier.md`; Claude Code's plan mode says to write nothing but the plan file. The agent resolves the conflict for plan mode and refuses. The rule must say that plan mode does not stop the write and the closing of the lines of `frontier.md`.

> **given:**
> The system text of Claude Code's plan mode forbids any edit but the plan file.
> **＋** The agent follows the Render of `rule-skill-hi`: it writes `frontier.md` at `/hi` and closes its lines in the replies of Plan Mode.
> **＋** `rule-permissions` counts `frontier.md` among the session's working files; the client may still show its approval prompt (case 237).

> **when:**
> The person types `/hi` with plan mode on, and the agent assembles the Frontier.

> **then:**
> The agent writes `frontier.md` into the session's folder; it does not ask in the chat and does not say that it cannot.
> **＋** In the replies of Plan Mode the agent closes the lines of `frontier.md` the same way.
> **－** The client's approval prompt, if it shows, is the person's; the leave covers `frontier.md` alone.

```then
update:
  - slug: rule-skill-hi
    replace:
      - old: "in Work Mode (case 356.1). Wait"
        new: "in Work Mode (case 356.1). Claude Code's plan mode does not stop this: the agent writes `frontier.md` and closes its lines while plan mode is on — a working file of the session (`rule-permissions`, case 363). Wait"
    change: plan mode does not stop the write of frontier.md or the closing of its lines (case 363)
  - slug: estimate-hi-writes-frontier
    replace:
      - old: "closes `· work` in Work Mode (356.1)."
        new: "closes `· work` in Work Mode (356.1).\n**＋** Claude Code's plan mode is on at `/hi`; the agent writes `frontier.md` and closes its lines all the same, with no refusal in the chat (363)."
    change: the Criterion names the write of frontier.md in plan mode (case 363)
```

```tasks
- [x] update `rule-skill-hi` — one `replace` pair in the Render
- [x] update `estimate-hi-writes-frontier` — one `replace` pair in the Criterion, `pending`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] read `estimate-hi-writes-frontier`
```

## Case 364 — the live pointers at `index.md`, and the Routing Table back on a live text

> **context:**
> Case 318 deleted `vault/wiki/index.md`: each of its `§N` was to be covered by a rule page and every pointer at the file was to go. The reading L63 found two live pointers: the docstring of `guppi/materialize.py:11` ("route computed from `index.md` §5") and the Given of `estimate-case-protocol-case-form`. The same `rg` run again in this session found a third: the Then of `estimate-prespec-reconciles` has `ask-guppi` asked what contradicts "a page, `index.md` or each other", while the Render of `/pre-spec` already says "a page of the vault, a rule of the vault, or each other". And §5, the Routing Table, did not move: `rule-materialize` says "Its route is the Routing Table of this page", and the page holds no table; the version of `index.md` before its removal holds it — decision × `ref` → effect on the target.
> `entity-sprint-migration` stands `draft`; `estimate-sprint-migration-index-dissolved` stands `failed`, its Criterion stands and it is read again after Work Mode; `rule-materialize` stands `built`, and none of its 11 Estimates speaks of the route, so none is touched; `estimate-case-protocol-case-form` (`pending`) is touched by 364.2; `estimate-prespec-reconciles` (`passed`) is touched by 364.3 and goes `pending`; no `create`, so no vault query is due.

> **problem:**
> The Estimate stands `failed` because three live texts send the reader to a file that is gone, and the Routing Table the docstring points at stands on no live page.

> **given:**
> `vault/wiki/index.md` does not exist (case 318).
> **＋** `estimate-sprint-migration-index-dissolved` fails on a live page, a harness file or a docstring of `guppi/` that points at `index.md` or at a `§N` of it.

### Case 364.1 — the Routing Table in the docstring of `guppi/materialize.py`

> **given:**
> `vault/wiki/index.md` does not exist (case 318).
> **＋** On a Leaf rule the mechanism lives in the docstring of its code (`rule-rules-schema`).

> **when:**
> The agent or the librarian looks for the route of a ledger line.

> **then:**
> The docstring of `guppi/materialize.py` holds the Routing Table — decision × `ref` → effect on the target — and names no `index.md`.
> **＋** The Purpose of `rule-materialize` sends the reader to that docstring.
> **－** The code of materialize does not change.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "Its route is the Routing Table of this page."
        new: "Its route is the Routing Table in the docstring of `guppi/materialize.py` (case 364.1)."
    change: the Routing Table lives in the docstring of guppi/materialize.py (case 364.1)
```

```tasks
- [x] update `rule-materialize` — one `replace` pair in Purpose
- [x] `guppi/materialize.py` — the docstring: "computed from `index.md` §5" → "computed by the Routing Table below"; the table — the nine rows of §5 as they stood when the file was removed; the Rule-class map sentence out, in its place "the category from the slug prefix; a slug with no prefix is `unknown` (case 320)"
```

### Case 364.2 — the Given of `estimate-case-protocol-case-form` names no removed file

> **given:**
> `vault/wiki/index.md` does not exist (case 318).
> **＋** The Renders of the six schemas are the `schema.yaml` files; no `schema.md` stands (case 304).

> **when:**
> The Criterion is read for a reading of the Estimate.

> **then:**
> The Given names Render files that exist; neither `index.md` nor `estimates/schema.md` stands in it.

```then
update:
  - slug: estimate-case-protocol-case-form
    replace:
      - old: "`index.md`, `estimates/schema.md` and `schema.yaml` are the Renders of their rule pages (case 304)"
        new: "the six `schema.yaml` are the Renders of their rule pages (case 304)"
    change: the Given names no removed file (case 364.2)
```

```tasks
- [x] update `estimate-case-protocol-case-form` — one `replace` pair inside the Criterion
```

### Case 364.3 — the Then of `estimate-prespec-reconciles` names no `index.md`

> **given:**
> `vault/wiki/index.md` does not exist (case 318).
> **＋** The Render of `rule-prespec` asks `ask-guppi` what contradicts "a page of the vault, a rule of the vault, or each other".

> **when:**
> The Criterion is read for a reading of the Estimate.

> **then:**
> The question on contradictions in the Criterion is the question of the Render.

```then
update:
  - slug: estimate-prespec-reconciles
    replace:
      - old: "which decisions contradict a page, `index.md` or each other"
        new: "which decisions contradict a page of the vault, a rule of the vault, or each other"
    change: the question on contradictions as the Render asks it (case 364.3)
```

```tasks
- [x] update `estimate-prespec-reconciles` — one `replace` pair inside the Criterion, `pending`
- [ ] read `estimate-prespec-reconciles`
- [x] read `estimate-sprint-migration-index-dissolved`
```

## Case 365 — the retired term "Rule-class" and the `file` route out of the docstrings and test names

> **context:**
> Case 321 retired the term "Rule-class"; case 320 took the `file` route out of the scripts, and `find_item` of `guppi/materialize.py` finds a `then` item by `slug` alone. The texts of the code did not follow: the docstring of `guppi/materialize.py` says the item "of a Rule-class file" is found "by `slug`, or by `file`"; the docstring of `guppi/generate.py` names "a Rule-class file entry" where the code tells any entry with no category (`unknown`) and ticks nothing for it; the docstring of `wikilink` says "a Rule-class slug" for a slug without a category prefix; three test names carry the term (`tests/test_lint.py`, `tests/test_pages.py`, `tests/test_render.py`). The grep of `estimate-sprint-migration-rule-class-files-dissolved` does not catch them: it looks for `RULE_CLASS`, `rule_class_path`, `prose_names` and "applied by hand".
> `rule-page-generation` stands `draft`, `rule-materialize` `built`; only texts change and no behaviour, so no Estimate of either rule is touched; the `method` of `estimate-sprint-migration-rule-class-files-dissolved` is item C4 and does not change here; no `create`.

> **problem:**
> The docstrings and the test names describe a route and a class of files that no longer exist, and give the reader of the code a false model — a `then` item found by `file`.

> **given:**
> The term "Rule-class" is retired (case 321).
> **＋** `find_item` of `guppi/materialize.py` finds a `then` item by `slug` alone; the `file` route is gone (case 320).
> **＋** `guppi generate` ticks nothing for an entry with no category (`unknown`).
> **＋** `guppi/` and `tests/` hold compiled caches, `__pycache__/*.pyc`, those of removed modules among them; git ignores them, and grep reads them.

> **when:**
> A reader opens the docstrings of `guppi/generate.py` or `guppi/materialize.py`, or the test names of `tests/`.

> **then:**
> No docstring of `guppi/` and no test name of `tests/` names "Rule-class"; the sources `*.py` are checked, not the caches.
> **＋** The docstring of `guppi/materialize.py` says a `then` item is found by `slug` alone (case 320).
> **＋** The docstring of `guppi/generate.py` names an entry with no category, and `wikilink` a slug without a category prefix.
> **－** The code does not change; the test with an entry of `category: "file"` in `tests/test_generate.py` stays — it is the shape of an old yaml entry, and the test checks that it ticks nothing.

```then
update:
  - slug: rule-page-generation
    change: the docstrings of guppi/generate.py name an entry with no category, not a Rule-class file (case 365)
  - slug: rule-materialize
    change: the docstring of guppi/materialize.py finds a then item by slug alone, no Rule-class file (case 365)
```

```tasks
- [x] update `rule-page-generation` — `change` alone; the mechanism lives in the docstring
- [x] update `rule-materialize` — `change` alone
- [x] `guppi/materialize.py` — the docstring sentence on the "Rule-class file" and `file` → "The `then` item is found by `slug` alone (case 320)."
- [x] `guppi/generate.py` — the docstring "a Rule-class file entry" → "an entry with no category (`unknown`, case 320)"; `wikilink` "a Rule-class slug" → "a slug without a category prefix"
- [x] `tests/test_lint.py`, `tests/test_pages.py`, `tests/test_render.py` — the three test names without "rule_class": "a slug without a prefix" or "a file of the vault"
- [x] `make test` green; `grep -rni --include='*.py' 'rule.class' guppi/ tests/` empty
```

## Case 366 — the message of an update with no content, as the code prints it

> **context:**
> On an `update` with no content — none of `set`, `sections`, `replace`, `change`, `rename`, `reword` — `guppi generate` changes no page, prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout, leaves the exit code alone and marks the entry `applied`. The words "nothing applied" came with case 320, which took the `file` route out of the scripts. One line of the Criterion of `estimate-generate-fails-alone` still expects the old words "applied by hand", and the reading L58 set the Estimate `failed`. The same reading found that no test of `tests/test_generate.py` asserts the message, which is how the words drifted unseen.
> `estimate-generate-fails-alone` stands `failed`, its target `rule-page-generation` (`draft`); the Purpose of the rule says nothing of an empty `update`, so the rule page does not change; no other Estimate of the rule speaks of this branch; no `create`.

> **problem:**
> The Criterion describes a message the code no longer prints, and no test fixes the message that it prints.

> **given:**
> `guppi generate` applies the entries of a `materialize.yaml` in order; an `update` with none of `set`, `sections`, `replace`, `change`, `rename`, `reword` changes no page (case 320).
> **＋** The tests in `tests/test_generate.py` fix the behaviour.

> **when:**
> `guppi generate` meets an `update` with no content.

> **then:**
> It prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout; the page does not change, the entry is marked `applied`, the exit code stays 0.
> **＋** A test asserts the line, the unchanged page and the `applied` mark.

```then
update:
  - slug: estimate-generate-fails-alone
    replace:
      - old: "prints `an update with no content in the Spec; applied by hand` and is marked applied."
        new: "prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout, changes no page and is marked applied (case 320)."
    change: the message of an update with no content as the code prints it since case 320 (case 366)
```

```tasks
- [x] update `estimate-generate-fails-alone` — one `replace` pair inside the Criterion, `pending`
- [x] `tests/test_generate.py` — an `update` with no content: the line on stdout, exit 0, the page unchanged, `applied` in the yaml
- [ ] read `estimate-generate-fails-alone`
```

## Case 367 — the reading of Slice 3f without `make lint`

> **context:**
> The `method` and the When of `estimate-sprint-migration-rule-class-files-dissolved` ask for `make lint` exit 0 at the close of Slice 3f. `make lint` checks the whole vault, and in this session it gave 100 findings, exit 2: 62 on the legacy Decision pages of Cases 1–28, 31 `unread`, 3 on `rule-spec-box`, 3 `deferred`, 1 `unmigrated` — none on what Slice 3f did, the schemas, the glossary, `index.md`, the `file` route. The exit 0 is the promise of `estimate-sprint-migration-lint-clean`, at the close of the sprint, when the legacy Decision pages go to the archive. So the Estimate of a closed Slice cannot pass before the sprint closes. Apart from that, the grep of the `method` does not catch the word "Rule-class", which Case 365 takes out of the docstrings and test names, and nothing would check it.
> Both Estimates stand `pending`, their target `entity-sprint-migration` (`draft`); `-lint-clean` is not touched; the "Done when" line of `sprint.md` takes the `purpose`, which does not change; no `create`.

> **problem:**
> The Estimate of one Slice waits for a clean lint of the whole sprint, and its grep does not see the term the Slice retired.

> **given:**
> `make lint` checks the whole vault; its exit 0 is the promise of `estimate-sprint-migration-lint-clean` at the close of the sprint.
> **＋** By Case 365 no source `*.py` of `guppi/` and `tests/` names "Rule-class"; the `__pycache__` caches do not count.

> **when:**
> Someone reads `estimate-sprint-migration-rule-class-files-dissolved`.

> **then:**
> The reading runs neither `make lint` nor `guppi lint`; the Estimate passes on the `ls` of the schemas and `index.md`, the grep, `render --check` and `glossary --check`.
> **＋** The case-insensitive grep of `rule.class|applied by hand|prose_names` over the files `*.py` of `guppi/` and `tests/` is empty.
> **－** Every finding of lint, on the pages of Slice 3f too, is `estimate-sprint-migration-lint-clean`'s; lint itself does not change.

```then
update:
  - slug: estimate-sprint-migration-rule-class-files-dissolved
    set:
      method: "one reading by hand: ls vault/wiki/*/schema.md empty and vault/wiki/index.md absent; grep -rniE --include='*.py' 'rule.class|applied by hand|prose_names' guppi/ tests/ empty; uv run guppi render --check and uv run guppi glossary --check exit 0"
    replace:
      - old: "a grep of the `file` route over `guppi/`, `uv run guppi render --check`, `uv run guppi glossary --check`, `make lint`."
        new: "a grep of the `file` route and of the retired term over `guppi/` and `tests/`, `uv run guppi render --check`, `uv run guppi glossary --check`; `make lint` is the reading of `estimate-sprint-migration-lint-clean`."
      - old: "\"Rule-class\" is a retired term in the Case schema and in the glossary."
        new: "\"Rule-class\" is a retired term in the Case schema and in the glossary, and no docstring of `guppi/` and no test name of `tests/` carries it (case 365)."
    change: the reading of the Slice without make lint, the grep widened to the retired term over guppi/ and tests/ (case 367)
```

```tasks
- [x] update `estimate-sprint-migration-rule-class-files-dissolved` — `set.method`, two `replace` pairs inside the Criterion
- [ ] read `estimate-sprint-migration-rule-class-files-dissolved` — after the tasks of Case 365
```

## Case 368 — the heading of a Case in the chat

> **context:**
> The Case schema (`case-schema.md`, the Render of `rule-case-protocol`) names the eight sections of a Case and their order, but not where a Case begins or under which heading. It names a heading in the chat only for a sub-case (`### Case N.M — name`), for the short form of a defer (`## Case N — name`) and for the acknowledging reply (`## Case N — ratified`). In the Spec the heading `## Case N — name` stands, because the earlier Specs were written so and the scripts find a Case by its heading. In the chat of this session the Cases 363–367 opened straight with `context`, while the sub-cases 364.1–364.3 opened with their heading; the lesson is `lesson-case-protocol-chat-case-without-heading`.
> `rule-case-protocol` stands `draft`; the Case touches `estimate-case-protocol-case-form` (`pending`), whose Then describes the form of a Case in the chat, `estimate-case-protocol-loaded`, the live reading of the Render (case 187), and `estimate-case-protocol-acknowledging-reply`, whose "the reply that carries a Case … stay as today" the heading changes; it does not touch `estimate-case-protocol-ledger-line-form`; no `create`.

> **problem:**
> A full Case in the chat has no named heading; the agent follows the text literally and shows the Case without one, while a sub-case of the same reply has it.

> **given:**
> The agent shows a Case in the form `case-schema.md` gives, the Render of `rule-case-protocol` loaded by `/hi`.
> **＋** The schema names the heading of a sub-case, `### Case N.M — name`, already (Splitting).

> **when:**
> The agent shows a Case in the chat — at its first showing, when shown again after the person's change, and with sub-cases.

> **then:**
> The Case opens with the heading `## Case N — name`, the name in the language of the chat; its sections stand under it.
> **＋** A sub-case stands under its parent with the heading `### Case N.M — name`.
> **＋** In the Spec the same heading stands, the name in English.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "Eight, in this order. Each is one blockquote: the first line `**name:**`, the text on the following quoted lines."
        new: "Eight, in this order, under the heading `## Case N — name` — in the chat at every showing, the name in the language of the chat; in the Spec the same heading in English; a sub-case under `### Case N.M — name` beneath its parent (case 368). Each section is one blockquote: the first line `**name:**`, the text on the following quoted lines."
    change: a Case opens with the heading `## Case N — name` in the chat and in the Spec (case 368)
  - slug: estimate-case-protocol-case-form
    replace:
      - old: "a sub-case questioned or changed is shown again alone (355.2)."
        new: "a sub-case questioned or changed is shown again alone (355.2).\n**＋** The Case opens with the heading `## Case N — name` at every showing, a sub-case with `### Case N.M — name` (368)."
    change: the Criterion names the heading of a Case in the chat (case 368)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "**＋** `render --check` after the render exits 0."
        new: "**＋** The section Sections says a Case opens with the heading `## Case N — name`, in the chat and in the Spec, a sub-case with `### Case N.M — name` (368).\n**＋** `render --check` after the render exits 0."
    change: the Criterion names the heading of a Case in the Render (case 368)
  - slug: estimate-case-protocol-acknowledging-reply
    replace:
      - old: "stay as today; no tool call follows the block in the same reply."
        new: "are not measured here — their form stands in `case-schema.md` (368); no tool call follows the block in the same reply."
    change: the other replies are not measured here, their form stands in the schema (case 368)
```

```tasks
- [x] update `rule-case-protocol` — one `replace` pair in the Render, the Sections paragraph
- [x] update `estimate-case-protocol-case-form` — one `replace` pair inside the Criterion
- [x] update `estimate-case-protocol-loaded` — one `replace` pair inside the Criterion
- [x] update `estimate-case-protocol-acknowledging-reply` — one `replace` pair inside the Criterion
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-case-form`
- [ ] read `estimate-case-protocol-loaded`
- [ ] read `estimate-case-protocol-acknowledging-reply`
```

## Case 369 — "writes nothing else" in `rule-page-generation`

> **context:**
> The Purpose of `rule-page-generation` says the script "lays the content of `materialize.yaml` into schema fields and writes nothing else". The same Purpose then names what `generate` writes beyond the yaml's content: the cascade — `built`, the archive of a superseded decision, the severity of an Insight, the `rules` of an Entity from the `applies_to` of the live rules; the move of a sprint item to the Backlog; the ticks of the Spec; the links a `rename` rewrites and the words a `reword` changes over every live page. All of it is computed by the mechanism, none invented; but "nothing else", read literally, is false, and the pre-spec of session 0034 named it a contradiction.
> `rule-page-generation` stands `draft`; only its Purpose changes, which by case 187 touches no Estimate; none of its nine Estimates quotes the sentence, and none is touched; no `create`.

> **problem:**
> The sentence meant to forbid a field nobody ratified forbids what the same paragraph allows below.

> **given:**
> The Purpose of `rule-page-generation` names the steps `generate` takes beyond laying the yaml's content: the cascade, the move of the sprint, the ticks of the Spec, `rename`, `reword`.

> **when:**
> Someone reads the Purpose of `rule-page-generation`.

> **then:**
> The Purpose says the script lays the content of `materialize.yaml` into schema fields and invents nothing; what it writes beyond that content is computed from the pages, the Specs, the ledgers and the Frontiers of `raw/` and the archive by the steps the page names.
> **－** The bans stand: no section is derived from a ref field, no Estimate from a flag.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "the content of `materialize.yaml` into schema fields and writes nothing else: no section is derived from a ref field"
        new: "the content of `materialize.yaml` into schema fields and invents nothing: what it writes beyond that content is computed from the pages, the Specs, the ledgers and the Frontiers of `raw/` and the archive by the steps this page names — the cascade, the move of the sprint, the ticks of the Spec, the links of a `rename`, the words of a `reword` (case 369); no section is derived from a ref field"
    change: the script invents nothing; what it writes beyond the yaml is computed by the steps the page names (case 369)
```

```tasks
- [x] update `rule-page-generation` — one `replace` pair in Purpose
```

## Case 370 — a `replace` pair in the chat as sub-points under its task

> **context:**
> The `then` block — `replace` pairs, `set` values, `sections` text — lives in the Spec; the chat has none. For the person to sign content and not the fact of a change, the agent shows that content in `tasks`. The schema says of `tasks` only "in the chat a blockquote with the checklist; in the Spec the block tagged `tasks` — the same lines"; it gives no form for a pair in the chat. In this session the pairs first stood inside the task line (363, 364), from Case 367 as sub-points under it; the person named the second form convenient. It stands on the agent's memory, not in the rule.
> `rule-case-protocol` stands `draft`, updated in this session by Case 368 already; the Case touches `estimate-case-protocol-case-form` (`pending`), whose Then describes the form of `tasks` in the chat, and `estimate-case-protocol-loaded`, the live reading of the Render (case 187); the other two Estimates of the rule are not touched; the paragraph on the `then` block says its content is "not in the chat" and changes with the row; no `create`.

> **problem:**
> The content the person signs has no form in the chat; each session chooses one again, and a pair inside a long line is hard to read.

> **given:**
> The chat has no `then` block; it lives in the Spec (case 159).
> **＋** The person signs content, not the fact of a decision; a ratification without the content in view is empty.

> **when:**
> The agent shows in the chat a Case whose item writes content of a page.

> **then:**
> Under the task line stand sub-points: for a `replace` or `reword` pair `old` and `new`, each a sub-point of its own; for a `set`, a `sections` or the fields of a `create` the value as a sub-point of its own.
> **＋** In the Spec the same content stands in the `then` block, and the task line of the `tasks` block stays one line.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "In the chat a blockquote with the checklist; in the Spec the block tagged `tasks` — the same lines (case 159)."
        new: "In the chat a blockquote with the checklist, and under a line whose item writes content that content as sub-points — `old` and `new` of each `replace` or `reword` pair, the value of a `set`, the text of a `sections`, the fields of a `create` — each on its own sub-point (case 370); in the Spec the block tagged `tasks`, the same lines without the sub-points, whose content is the `then` block (case 159)."
      - old: "— the plan the human approves at the end of Plan Mode — not in the chat."
        new: "— the plan the human approves at the end of Plan Mode — not in the chat, where its content stands as sub-points of `tasks` (case 370)."
    change: in the chat the content of an item stands as sub-points under its task line (case 370)
  - slug: estimate-case-protocol-case-form
    replace:
      - old: '**＋** `tasks` carries no `contract` line and no "block N" line.'
        new: '**＋** `tasks` carries no `contract` line and no "block N" line; in the chat the content of an item stands as sub-points under its line — `old` and `new` of a pair, the value of a `set` or a `sections`, the fields of a `create` (370).'
    change: the Criterion names the sub-points of an item's content in the chat (case 370)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "**＋** `render --check` after the render exits 0."
        new: "**＋** The `tasks` row says the content of an item stands in the chat as sub-points under its line, and the paragraph on the `then` block that its content stands there as sub-points of `tasks` (370).\n**＋** `render --check` after the render exits 0."
    change: the Criterion names the sub-points of tasks in the Render (case 370)
```

```tasks
- [x] update `rule-case-protocol` — two `replace` pairs in the Render, the `tasks` row of Sections and the paragraph on the `then` block
- [x] update `estimate-case-protocol-case-form` — one `replace` pair inside the Criterion
- [x] update `estimate-case-protocol-loaded` — one `replace` pair inside the Criterion
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-case-form`
- [ ] read `estimate-case-protocol-loaded`
```

## Case 371 — "needs nothing" in `estimate-prespec-binds-a-sprint-line`

> **context:**
> `guppi prespec --check` reads the Frontier lines; a sprint line closed `· case N` needs an `update` of the sprint page under that Case, and a line `[-] … · sprint` gives no finding. The Criterion of `estimate-prespec-binds-a-sprint-line` says of the second: "needs nothing: the item stays on the page as it is". Since Case 354.1 that is no longer so: an item put off `· sprint` in three sessions in a row goes to the Backlog by `generate`. For `prespec` the line still needs nothing, but "stays on the page as it is" contradicts 354.1; the pre-spec of session 0034 named it a known contradiction.
> `estimate-prespec-binds-a-sprint-line` stands `passed`, its target `rule-prespec`; a pair inside its Criterion sets it `pending`; the move is the promise of `estimate-sprint-moves-a-passed-over-item` (`pending`), not touched; the code does not change; no `create`.

> **problem:**
> A line of the Criterion promises the item stays on the page unchanged, while another script's rule moves it after three sessions.

> **given:**
> `prespec.check_frontier` gives no finding on a line closed `[-] … · sprint`.
> **＋** An item put off `· sprint` in three sessions in a row goes from its milestone to the Backlog by `generate` (case 354.1).

> **when:**
> `guppi prespec --check` reads a Frontier line closed `[-] … · sprint`.

> **then:**
> No finding.
> **＋** The item stays in its milestone until `generate` moves it to the Backlog after three such sessions in a row (354.1).

```then
update:
  - slug: estimate-prespec-binds-a-sprint-line
    replace:
      - old: "**＋** A line closed `[-] … · sprint` needs nothing: the item stays on the page as it is."
        new: "**＋** A line closed `[-] … · sprint` needs nothing from `prespec`: no finding; the item stays in its milestone until `generate` moves it to the Backlog after three such sessions in a row (354.1)."
    change: a sprint line put off needs nothing from prespec; the item stays until generate moves it (case 371)
```

```tasks
- [x] update `estimate-prespec-binds-a-sprint-line` — one `replace` pair inside the Criterion, `pending`
- [ ] read `estimate-prespec-binds-a-sprint-line`
```

## Case 372 — render as the guard of a rule on the agent's own conduct

> **context:**
> The rules schema (`rule-rules-schema`, its Render `vault/wiki/rules/schema.yaml`) asks of a Rule a guard that refuses a case; Enforcement says "A constraint that no hook, check or render can detect is not a Rule at all", and the same schema counts "a render that refuses drift" as a guard. The rules on the agent's own conduct — `rule-one-judgment-one-implementation`, created by Case 360, `rule-agent-writing`, `rule-language`, `rule-atomicity` — stand on the text in a file the agent reads, `CLAUDE.md` or `case-schema.md`; the render refuses the drift of that text, not a case in substance, and the Estimate of 360 says "No script refuses a second copy". The pre-spec of session 0034 named this a known contradiction.
> `rule-rules-schema` stands `draft`; the Case touches `estimate-rules-schema-checked` (`pending`), whose Then promises the prose of Enforcement verbatim with one added sentence after 240.2; the four rules of the class do not change; no `create`.

> **problem:**
> The rules schema does not admit a Rule without a guard that refuses the case, while four rules on the agent's conduct stand on the text in the context alone; either the schema is wrong or these pages are not Rules.

> **given:**
> A Rule is a condition one case can break, with a guard that refuses that case; in the harness a render that refuses the drift of a text is such a guard (`rule-rules-schema`).
> **＋** A render puts a rule's text into a file the agent reads — `CLAUDE.md` in every context, `case-schema.md` in a working session; `render --check` and a hook keep it there.

> **when:**
> Someone judges whether a condition on the agent's own conduct is a Rule — at the `create` of a rule, for one.

> **then:**
> A condition on the agent's own conduct is a Rule with `enforcement: render`; its guard is the text in the file the agent reads when it acts, the render refusing the drift of that text.
> **＋** Its Estimate reads the render, and the agent's conduct by hand where it names that.
> **－** No script refuses a case in substance; a constraint on an Entity with no hook, check or render is still not a Rule.

```then
update:
  - slug: rule-rules-schema
    replace:
      - old: "A constraint that no hook, check or render can detect is not a Rule at all. It is a sentence in an Entity's `How it works`."
        new: "A constraint that no hook, check or render can detect is not a Rule at all. It is a sentence in an Entity's `How it works`. The one exception is the agent's own conduct — how it writes, splits and implements — which no script can judge in substance: its `render` rule puts the text into a file the agent reads when it acts — `CLAUDE.md` in every context, `case-schema.md` in a working session —, `render --check` and the governed-files hook refuse its drift, and its Estimate reads the render, and what the agent did by hand where it names that; the text in the context is the guard (case 372)."
    change: the guard of a rule on the agent's own conduct is its text in the context (case 372)
  - slug: estimate-rules-schema-checked
    replace:
      - old: "and one sentence on the edge Rule → Entity after the paragraph of case 240.2"
        new: "and one sentence on the edge Rule → Entity after the paragraph of case 240.2, and one on the guard of the agent's own conduct in Enforcement (372)"
    change: the Criterion names the sentence on the guard of the agent's own conduct (case 372)
```

```tasks
- [x] update `rule-rules-schema` — one `replace` pair in the Render, the Enforcement paragraph
- [x] update `estimate-rules-schema-checked` — one `replace` pair inside the Criterion
- [x] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
- [ ] `uv run pytest tests/test_schemas.py -k rules` green
- [ ] read `estimate-rules-schema-checked`
```

## Case 373 — a Case the agent finds changed after its ratification

> **context:**
> The Case schema asks that a Case the person changed be shown again — `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`. It says nothing of the case where the agent itself, after ratification, finds a gap, an error or a wider scope in the signed text; the agent reads the rule as one on the person's changes alone, repairs the text itself — in the Spec or in the files — and names the repair after the fact. It happened twice: in session 1308 the grep of tasks 277.3 found a sixth file, the agent edited it and backfilled the ledger (`lesson-work-mode-check-widened-the-list-and-the-agent-acted`); in session 0034 the agent added a `problem` to Case 359 and removed a sentence from the `context` of Case 361 in the Spec without a showing (`lesson-spec-text-repaired-after-ratification-without-a-showing`). The librarian clustered both into `insight-workflow-ratified-content-changed-on-the-agents-own-finding` (`open`, severity 2), whose proposal is an update of `rule-case-protocol`.
> `rule-case-protocol` stands `draft`, changed in this session by Cases 368 and 370 already; the Case touches `estimate-case-protocol-case-form` (`pending`), whose When speaks of a showing again, and `estimate-case-protocol-loaded`, the live reading of the Render (case 187); the other two Estimates of the rule are not touched; the Insight goes `actioned`; both lessons are of other sessions, so no `{addresses:…}` mark (case 284.2); no `create`.

> **problem:**
> The rule of the showing again does not name a change the agent found itself, and signed text changes without a signature.

> **given:**
> The person signs content; a text changed after the signature is signed by nobody.
> **＋** A Case the person changed is shown again: `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks`, `ratification`, no `recommend` (cases 62, 163).

> **when:**
> After ratification the agent finds a gap, an error or a wider scope in the text of a Case — in the Spec, at pre-spec or in Work Mode.

> **then:**
> The agent stops and shows the changed Case again, in the form of a showing again.
> **＋** Until the Case is ratified again, the agent writes nothing of the change — not in the Spec, not in the files, not in the ledger — and acts on nothing of it.
> **－** The translation of a Case into English in the Spec is no change when the meaning stays.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "A Case the person changed is shown again: `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and no `recommend` (cases 62, 163)."
        new: "A Case the person changed, or one whose text or scope the agent finds wrong or too narrow after its ratification — in the Spec, at pre-spec or in Work Mode — is shown again: `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and no `recommend` (cases 62, 163); until it is ratified again, nothing of the change is written or acted on; the translation of a Case into the Spec is no change (case 373)."
    change: a Case the agent finds changed after ratification is shown again before anything of the change is written (case 373)
  - slug: estimate-case-protocol-case-form
    replace:
      - old: "The agent writes a Case in the chat — at its first showing, when shown again after the owner's change, and with sub-cases."
        new: "The agent writes a Case in the chat — at its first showing, when shown again after the owner's change or after its own finding in ratified text (373), and with sub-cases."
    change: the When names the showing again after the agent's own finding (case 373)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "**＋** `render --check` after the render exits 0."
        new: "**＋** The `ratification` row says a Case the agent finds changed after its ratification is shown again, and nothing of the change is written or acted on until it is ratified again (373).\n**＋** `render --check` after the render exits 0."
    change: the Criterion names the showing again after the agent's own finding in the Render (case 373)
  - slug: insight-workflow-ratified-content-changed-on-the-agents-own-finding
    set: {status: actioned, addressed_by: decision-case-373}
    change: actioned by the update of rule-case-protocol (case 373)
```

```tasks
- [x] update `rule-case-protocol` — one `replace` pair in the Render, the `ratification` row of Sections
- [x] update `estimate-case-protocol-case-form` — one `replace` pair inside the Criterion
- [x] update `estimate-case-protocol-loaded` — one `replace` pair inside the Criterion
- [x] update `insight-workflow-ratified-content-changed-on-the-agents-own-finding` — `actioned`, `addressed_by`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-case-form`
- [ ] read `estimate-case-protocol-loaded`
```

## Case 374 — the `method` of `estimate-atomicity-rendered` without `make lint`

> **context:**
> The `method` of `estimate-atomicity-rendered` reads "make lint — render --check exit 0; the text between the markers of case-schema.md read by hand after the librarian's render". Its Then asks only that `render --check` exits 0 after the render and that the hook refuses a hand edit; it does not ask the whole `make lint` to exit 0. The "make lint —" at the head of the `method` reads two ways: the brief rendered it as "`make lint`, `render --check` exit 0", and the agent read it the same way. The one who reads the Estimate may ask for a clean lint and fail it on 100 findings that are not the rule's.
> `estimate-atomicity-rendered` stands `pending`, its target `rule-atomicity`; only the `method` field changes, not the Criterion, which by case 296 leaves the Criterion and the status as they stand; no `create`.

> **problem:**
> The wording of the `method` allows the reading "the whole `make lint`, exit 0", and so ties the Estimate of a rule to the lint of the whole sprint, which its Criterion does not ask.

> **given:**
> The Then of `estimate-atomicity-rendered` asks exit 0 of `render --check`, not of the whole `make lint`.
> **＋** The exit 0 of the whole `make lint` is the promise of `estimate-sprint-migration-lint-clean` (case 367).

> **when:**
> Someone reads `estimate-atomicity-rendered` by its `method`.

> **then:**
> The reading runs `uv run guppi render --check` and reads the text between the markers of `case-schema.md`; it does not run `make lint`.

```then
update:
  - slug: estimate-atomicity-rendered
    set:
      method: "uv run guppi render --check exit 0; the text between the markers of case-schema.md read by hand after the librarian's render"
    change: the method names render --check, not make lint (case 374)
```

```tasks
- [x] update `estimate-atomicity-rendered` — `set.method`
- [x] read `estimate-atomicity-rendered`
```

## Deferred

## Case 375 — the report of `/retro`: one list of ratifications, one list of what is not done

> **context:**
> The Render of `rule-retro` asks the Retro to open with the frontier — what was ratified, the lines of the Tail grouped by Case, one line per Case, and the unticked boxes of the Spec per Case — and to close with three lists: every ratification of the session, what got done, what did not. In session 1126 the report followed it and the person found two defects: the ratifications stand twice, once at the opening by the Tail and once in the closing list; and the unticked boxes of the Spec stand apart from "what did not get done", though they are part of it.
> `rule-retro` is not changed in this session; a Retro ratifies no `create`, `update` or `delete`.

> **problem:**
> The report of `/retro` names the same ratifications twice and splits what is not done into two places, so the person reads more and finds the open work in two lists.

```then
defer:
  - slug: rule-retro
    type: rule
    purpose: The report of /retro holds each fact once — the ratifications in one list, the person proposing to drop the opening list by the Tail and keep the closing one; and the unticked boxes of the Spec, those waiting for the librarian and those that are debt, inside the list of what is not done rather than a list of their own
```
