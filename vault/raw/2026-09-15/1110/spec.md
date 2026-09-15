<!-- approved 14:17:05 · session 4d2f4b79 -->

# Spec — 2026-09-15, session Q (hi 11:10)

## Case 155 — `rule-ask`: two moments of the question instead of "one per Case"

> **context:**
> The description line of the Render of `rule-ask` says "One short question per Case". `CLAUDE.md` (the Render of `rule-case-protocol`) already says otherwise: a question before a `create` without a `ref`, and `/pre-task` asks once for the set. Session P dispatched `ask-guppi` six times, four of them before an `update` with a `ref`, about 355k tokens in subagents; there the page itself and two Greps would have given the `given`. Case 154 deferred the decision to this Plan Mode.

> **problem:**
> Whether the text of `rule-ask` follows the practice: one question before a `create` without a `ref`, one at pre-task, an `update` with a `ref` reads the page itself. The Purpose of `rule-pretask` carries the same phrase, "The per-Case question to `ask-guppi`".

> **given:**
> `rule-ask` (`draft`, `deferred_by: [[decision-case-154]]`, `render`, governs `.claude/agents/ask-guppi.md`): description "… One short question per Case."; its Purpose names the callers — the agent at pre-task, the librarian, the person — and does not say "per Case".
> **＋** `rule-case-protocol` → `CLAUDE.md` line 88: "Before a `create` without a `ref`, ask the vault first … Dispatch the `ask-guppi` agent with one short question." — the `create` moment is ratified there already.
> **＋** `rule-pretask` Purpose, line 20: "The per-Case question to `ask-guppi` asks "does this exist"; this one asks, once, "does this set hold together"."
> **＋** `index.md` §11: "One tool, two moments: pre-task queries by intent before a decision exists; the librarian queries by finished content afterwards" — no conflict, unchanged.
> **＋** An `update` with a `ref`: by this decision itself, the pages were read and `ask-guppi` was not dispatched.
> **－** `estimate-ask-finds` `passed` at 11:1x today (147.2); `contract: same` does not touch it.

> **when:**
> `guppi render` writes `.claude/agents/ask-guppi.md`; someone reads the Purpose of `rule-ask` or of `rule-pretask`.

> **then:**
> The description line of the Render: "Ask the vault what already exists, what is close, what is missing, which rule the proposal touches, which tags fit and whether a slug is free. One question before a `create` without a `ref`, and one at pre-task for the whole set; an `update` with a `ref` reads the page itself."
> **＋** The Purpose of `rule-ask`, after "…so the event log records each call.": "The main agent asks at two moments: before a `create` without a `ref`, and once at pre-task for the set of ratified Cases; the librarian asks by finished content afterwards, as §11 of the map says. An `update` with a `ref` does not ask: the page itself and a Grep give the `given` (case 154)."
> **＋** The Purpose of `rule-pretask`: "The per-Case question to `ask-guppi` asks "does this exist"" → "The question to `ask-guppi` before a `create` without a `ref` asks "does this exist"".
> **＋** `rule-ask` and `rule-pretask` `contract: same`; `decision-case-154` superseded, `rule-ask` loses `deferred_by`.
> **－** `rule-case-protocol`, `CLAUDE.md`, `index.md` §11 do not change: they say this already.
> **－** No line of code, no reading.

```then
update:
  - slug: rule-ask
    contract: same
    replace:
      - old: "description: Ask the vault what already exists, what is close, what is missing, which rule the proposal touches, which tags fit and whether a slug is free. One short question per Case."
        new: "description: Ask the vault what already exists, what is close, what is missing, which rule the proposal touches, which tags fit and whether a slug is free. One question before a `create` without a `ref`, and one at pre-task for the whole set; an `update` with a `ref` reads the page itself."
      - old: "with read-only tools, dispatched through the `Agent` tool, so the event log records each\ncall."
        new: "with read-only tools, dispatched through the `Agent` tool, so the event log records each\ncall. The main agent asks at two moments: before a `create` without a `ref`, and once at\npre-task for the set of ratified Cases; the librarian asks by finished content afterwards, as\n§11 of the map says. An `update` with a `ref` does not ask: the page itself and a Grep give\nthe `given` (case 154)."
    change: "the question has two moments — before a create without a ref, and once at pre-task; an update with a ref reads the page itself; supersedes case 154 (case 155)"
  - slug: rule-pretask
    contract: same
    replace:
      - old: "The per-Case question to `ask-guppi` asks \"does this exist\""
        new: "The question to `ask-guppi` before a `create` without a `ref` asks \"does this exist\""
    change: "the question to ask-guppi is the one before a create without a ref, not one per Case (case 155)"
```

```tasks
- [ ] nothing in Work Mode: the librarian's run applies the two updates and `guppi render` writes `.claude/agents/ask-guppi.md`; `guppi render --check` exit 0 at its close
```

## Case 156 — `rule-lint`: an Insight is never an orphan

> **context:**
> After sessions O and P `guppi lint` reports 10 `orphan` findings — the ten actioned Insights. An orphan in `rule-lint` is a live entity, rule, estimate or insight that no other live page names in its frontmatter. An Insight is named only by its children, through `insight`; on `actioned` the cascade of 104.2 archives the children and the Insight is left with no live inbound link by construction, while `rule-synthesis` and `index.md` §8 keep it live so a recurrence is caught by its `pattern`. Case 146 deferred the choice: an exemption for an actioned Insight, or Obsidian's notion of an orphan (no inbound link of any kind, body and decision pages included) now that the refs are wikilinks (147).

> **problem:**
> Two ratified norms — the children of an actioned Insight are archived; an actioned Insight stays live — guarantee a third's finding, which catches nothing. Which definition of an orphan lint keeps.

> **given:**
> `rule-lint` (`draft`, `deferred_by: [[decision-case-146]]`, `check`, `estimates: [estimate-lint-catches]` — `passed` at 11:1x today on 149.3): "How it works" lists "orphans" without a definition; the definition lives in the docstring of `guppi/lint.py`: "`orphan` (a live entity, rule, estimate or insight no other live page's frontmatter names; a lesson is a record and an Insight names it or not)"; `check_orphans` (`lint.py:355`) counts as owners only the `LINK_FIELDS` (`parent`, `children`, `estimates`, `target`, `addressed_by`, `insight`) of live pages and excludes `decisions` and `lessons`; the `create`/`update`/`delete`/`defer` lists of a decision page are not ownership.
> **＋** `ask-guppi` (11:14): exists `rule-lint` — the Case carries `{supersedes:case 146}`; near `lesson-obsidian-cli-needs-the-running-app` — the Obsidian option is already rejected by a recorded lesson, `lesson-obsidian-property-links-need-wikilink-form` — the premise of the graph; missing — no page defines "orphan" outside the Context of 146 and `lint.py`; no Insight is about lint; tags `harness`, `workflow` — `rule-lint`'s own.
> **＋** `index.md` §8: an Insight is created on the second lesson; actioned stays live with its `pattern` in its index line; `severity` = the count of children not archived — unchanged.
> **＋** `tests/test_lint.py`: orphan tests on a rule (357) and an estimate (393); "a lesson is never an orphan" (622); no test on an insight.
> **－** Live pages: 10 Insights, all `actioned`, all orphan findings; no other orphan besides the two placeholders of F1.

> **when:**
> `uv run guppi lint` checks orphans.

> **then:**
> An Insight is not an orphan finding, whatever its `status`: its owners are its children, which it names itself in `children`, live or archived; `check_orphans` excludes `insights` beside `decisions` and `lessons`.
> **＋** The text of `rule-lint`: "orphans (a live entity, rule or estimate no other live page names in its frontmatter; a lesson is a record and an Insight names it or not; an Insight owns its children through `children` and is named by no live page once they are archived — neither is one, case 156)"; the docstring of `lint.py` says the same.
> **＋** `rule-lint` `contract: changed`; `estimate-lint-catches` gets a `### case 156` block, `pending`; a test: an Insight nothing names, `status: actioned` — no finding; a rule without an owner — a finding as before.
> **＋** The reading in Work Mode: the test green, live `guppi lint` 84 → 74, no `orphan` on `insights/`.
> **＋** `decision-case-146` superseded, `rule-lint` loses `deferred_by`.
> **－** The definition for entity, rule and estimate does not change; decision pages and bodies do not become ownership — Obsidian's notion is not adopted, the lesson stands.
> **－** The orphans of the Obsidian graph (the placeholders of F1, the hub files) are not this Case.

```then
update:
  - slug: rule-lint
    contract: changed
    replace:
      - old: "(case 149.3),\norphans, a `built` page with an Estimate"
        new: "(case 149.3),\norphans (a live entity, rule or estimate no other live page names in its frontmatter; a lesson is a record and an Insight names it or not; an Insight owns its children through `children` and is named by no live page once they are archived — neither is one, case 156), a `built` page with an Estimate"
    change: "an Insight is never an orphan: its owners are its children, named in its own children field, live or archived; supersedes case 146 (case 156)"
```

```tasks
- [x] `guppi/lint.py`: `check_orphans` excludes `insights` beside `decisions` and `lessons`; the module docstring says "`orphan` (a live entity, rule or estimate no other live page's frontmatter names; a lesson is a record and an Insight names it or not; an Insight owns its children through `children`, archived or not, and is never one — case 156)"
- [x] `tests/test_lint.py`: an Insight nothing names, `status: actioned` — no `orphan` finding; the rule and estimate orphan tests unchanged
- [x] `make test`, `make style`
- [x] read `estimate-lint-catches` (block 156): the test above; live `uv run guppi lint` 84 → 74 findings, none `orphan` under `insights/`
```

## Case 157 — `rule-case-protocol`: the shape of the reply that acknowledges a ratification

> **context:**
> `rule-case-protocol` (Render → `CLAUDE.md`) says where the `decision[...]` lines are written — "in the reply that acknowledges ratification" — and that this reply ends in the `LEDGER` block. What the rest of that reply looks like the rule does not say; today it went as one block of running text. The owner chose a shape from the variants shown: a heading, "Changes", "Notes", the frontier as a checklist, the block.

> **problem:**
> The shape of the acknowledging reply is ratified nowhere; the agent is not bound to keep it, and keeping it in the agent's memory is a decision without a Case.

> **given:**
> `rule-case-protocol` (`draft`, `render`, `estimates: [estimate-case-protocol-loaded]` — `passed` today on 144.1): the Render, lines 60–65, the paragraph on the Spec ends "Retro counts the unticked."; lines 79–81: "Write the `- decision[...]` lines only in the reply that acknowledges ratification … A reply that carries a `LEDGER` block ends in that text."
> **＋** `rule-skill-hi`: `frontier.md` is `- [ ] F<n> — <title> · <source>`, closed as `[x] … · case N`, `[x] … · work`, `[-] … · defer case N`; the checklist in the reply repeats that form.
> **＋** Language: the chat with the owner is in Russian (`rule-claude-md`, Language) — the headings and labels of the reply are in the language of the chat, the rule describes them in English.
> **＋** An `update` with a `ref`: the page was read, `ask-guppi` not dispatched (155).
> **－** `case-schema.md` does not change: the acknowledging reply is not a section of a Case.

> **when:**
> The owner answers a Case with a ratification; the agent writes the reply that acknowledges it.

> **then:**
> The reply has four parts, in this order: a heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next; the `LEDGER` block, last.
> **＋** The headings and labels are in the language of the chat: "ратифицирован", "Меняется", "Заметки".
> **＋** `rule-case-protocol` `contract: changed`; `estimate-case-protocol-loaded` gets a `### case 157` block, `pending`; read in the next session at the first such reply after the render.
> **－** The replies on readings and lessons keep their shape; the reply that carries a Case (the seven sections) too.
> **－** `CLAUDE.md` changes only through the librarian's render.

```then
update:
  - slug: rule-case-protocol
    contract: changed
    replace:
      - old: "Work Mode ticks the boxes in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; Retro\ncounts the unticked."
        new: "Work Mode ticks the boxes in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; Retro\ncounts the unticked.\n\nThe reply that acknowledges a ratification has four parts, in this order: a heading\n`## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a\nparagraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading\n`## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the\nopen ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question\nwhich item is next; the `LEDGER` block, last. Headings and labels in the language of the chat (case 157)."
    change: "the reply that acknowledges a ratification has four parts: the Case heading with Changes, Notes when any, the Frontier as a checklist, the LEDGER block last (case 157)"
```

```tasks
- [ ] nothing in Work Mode: the librarian's run applies the update and `guppi render` writes `CLAUDE.md`; `guppi render --check` exit 0 at its close
- [ ] read `estimate-case-protocol-loaded` (block 157): the next session, at the first reply that acknowledges a ratification after the render — the four parts in order, the block last
```

## Case 158 — `rule-materialize`: the librarian's entry is readable

> **context:**
> Case 142.1 ratified: "An existing entry the script cannot read — not a mapping, or a mapping without `line` and without `derived` — is left as it is, named on stderr, and does not end the run". The librarian's own entries — the synthesis `create` of an Insight, the `update` of a lesson — carry `librarian: synthesis` and neither `line` nor `derived`. By the letter of the rule they are unreadable and are named on stderr every run; the code (`materialize.py:842-850`) takes `librarian` as a third mark of a readable entry and says nothing. The handoff of P recorded this as a caveat "for a later `update`".

> **problem:**
> The text of `rule-materialize` and block 142.1 of `estimate-materialize-assembles` describe a behaviour that does not exist; the code does the right thing, but the text has not signed it.

> **given:**
> `rule-materialize` (`built`, `check`, `estimates: [estimate-materialize-assembles, estimate-materialize-walks-dates]`, both `passed`): line 43, the text of 142.1 with "without `line` and without `derived`"; the docstring of `materialize.py` lines 22–23 says the same; the comment in the code at line 843 says "none of `line`, `derived`, `librarian`".
> **＋** `estimate-materialize-assembles`: block 142.1, line 116, repeats the wording; `passed` (P, 1633 L55).
> **＋** `tests/test_materialize.py:486` fixes the behaviour (`err == ""` for an entry with `librarian` and no `line`); `:1336` — two unreadable entries named.
> **＋** `rule-documentation` describes the marks `librarian`, `synthesis`, `near` — unchanged.
> **＋** An `update` with a `ref`: the pages and the code were read, `ask-guppi` not dispatched.
> **－** Block 142.1 is not removed (a `supersedes` would drop the whole block with its four other conditions); block 158 refines it.

> **when:**
> `guppi materialize` meets an existing entry in `materialize.yaml`.

> **then:**
> The entry is readable when it is a mapping with at least one of `line`, `derived`, `librarian`; the librarian's entry — `librarian: synthesis` (or `merged`), no `line` — is left as it is, with no line on stderr.
> **＋** An unreadable one — not a mapping, or a mapping with none of the three — is left as it is, named on stderr once, and the run goes on, as in 142.1.
> **＋** The text of `rule-materialize` and the docstring of `materialize.py`: "a mapping with none of `line`, `derived`, `librarian`" in place of "without `line` and without `derived`".
> **＋** `rule-materialize` `contract: changed`; `estimate-materialize-assembles` gets a `### case 158` block, `pending`; the reading in Work Mode: tests 486 and 1336 green, the stderr of the run of P empty.
> **－** No line of code beyond the docstring; `walks-dates` untouched.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-assembles
    replace:
      - old: "An existing entry the script cannot read — not a mapping, or a mapping without `line` and without `derived` — is left as it is, named on stderr, and does not end the run (case 142.1)."
        new: "An existing entry the script cannot read — not a mapping, or a mapping with none of `line`, `derived`, `librarian` — is left as it is, named on stderr, and does not end the run (cases 142.1, 158); the librarian's own entries carry `librarian` and no `line`."
    change: "an entry with librarian and no line is readable: the librarian's synthesis entries are left alone without a stderr line; the text of 142.1 made precise (case 158)"
```

```tasks
- [x] `guppi/materialize.py`: the module docstring — "a mapping with none of `line`, `derived`, `librarian`" (cases 142.1, 158)
- [x] `make test`, `make style`
- [x] read `estimate-materialize-assembles` (block 158): `tests/test_materialize.py` 486 (a librarian entry without `line` kept, stderr empty) and 1336 (two unreadable entries named) green; the stderr of `guppi materialize` in the librarian's run of P empty over three units with synthesis entries
```

## Case 159 — `rule-case-protocol`: the shape of a Case in the chat

> **context:**
> A Case is seven sections in blockquotes; the shape is set in `case-schema.md` and in the Render of `rule-case-protocol`, which lands in `CLAUDE.md`. On the first three sections the rule says one phrase — "in plain words"; the operands ＋/－ are defined as "one more condition" and "a limit"; `then` holds both behaviour and bookkeeping — the contract mark, the Estimate block, the reading. The Spec is the same Case in English plus the `then` and `tasks` blocks the scripts read. Today a Case in the chat is hard to read: the story is written in the language of the contract, `then` drowns in bookkeeping, slugs and bold mix.

> **problem:**
> What a Case in the chat should look like to be readable, without changing what the scripts read from the Spec.

> **given:**
> `rule-case-protocol` (`draft`, `render` → `CLAUDE.md`, `estimates: [estimate-case-protocol-loaded]`, `pending` by 157): the paragraph "A Case renders as…" sets the blockquotes, the operands, the sub-cases and the preview in `ratification`; the paragraph "The Spec is written…" the `tasks` block of the Spec.
> **＋** `case-schema.md` (Rule-class, applied by hand): the Sections table of seven rows, the paragraphs Operands, Language, Splitting, "The Spec is written…".
> **＋** `guppi materialize` reads from the Spec the `when`/`then` blockquotes (into the criterion), the `then` block and `problem`; `guppi pretask --check` the `then` block; nothing reads the chat form.
> **＋** Case 157 set the reply that acknowledges a ratification — a separate reply, not a Case.
> **－** The Spec does not change its form: the same blockquotes in English, the `then` and `tasks` blocks; otherwise `materialize` would change.

> **when:**
> The agent writes a Case in the chat — at its first showing, when shown again after the owner's change, and with sub-cases.

> **then:**
> `context`, `problem`, `recommend` are blockquotes without operands, the slug of the thing described only, up to seven sentences each: `context` — what the thing is and how it works today, for a reader who has not opened the pages, no line numbers and no quotation unless the Case is about one; `problem` — what is wrong, or the question answered, one paragraph; `recommend` — the choice and why, the rejected option in one sentence.
> **＋** `given` — one fact per line, only those a line of `then` depends on: the state of the pages changed; the rule that constrains; the vault's answer; the test that fixes the behaviour. The first line bare, then **＋** "and also", **－** "but not / does not apply here". No history, no quotation for its own sake.
> **＋** `then` — behaviour only: **＋** what also holds, **－** what does not happen; no `contract`, Estimate blocks, readings or `supersedes`.
> **＋** A new section `tasks` between `then` and `ratification`: a blockquote with a checklist, one line per page `update` with its `contract`, Estimate block, file, test, command, reading — the same lines that go into the Spec's `tasks` block.
> **＋** Slugs, file names and field values in code spans; bold only for section labels and operands.
> **＋** Sub-cases: the story and the shared `given` on the parent; each `### Case N.M` has its own `when`, `then`, `tasks`, `ratification`.
> **＋** One horizontal rule, after the Case or its last sub-case, and only when the agent's own text follows.
> **－** The Spec as today: `context`, `problem`, `given`, `when`, `then` as blockquotes in English, the `then` and `tasks` blocks; the `tasks` section of the chat is its `tasks` block.
> **－** The acknowledging reply (157) and the short form of a defer do not change.

```then
update:
  - slug: rule-case-protocol
    contract: changed
    replace:
      - old: "One reply is one Case, in the seven sections of `case-schema.md`: context, problem,\nrecommend, given, when, then, ratification."
        new: "One reply is one Case, in the eight sections of `case-schema.md`: context, problem,\nrecommend, given, when, then, tasks, ratification."
      - old: "sections. In `given`, `when` and `then` every line after the first starts with a\nbold operand: **＋** for one more condition or action, **－** for a limit or an\nexception."
        new: "sections. `context`, `problem` and `recommend` carry no operand, name the slug of the thing described only, and run to seven sentences each at most: `context` says what the thing is and how it works today, for a reader who has not opened the pages, with no line numbers and no quotation unless the Case is about one; `problem` says what is wrong, or the question answered, in one paragraph; `recommend` says the choice and why, the rejected option in one sentence. `given` holds one fact per line, and only a fact a line of `then` depends on: the state of the pages the Case changes, the rule that constrains, the vault's answer, the test that fixes the behaviour; no history, no quotation for its own sake. In `given`, `when` and `then` every line after the first starts with a\nbold operand: **＋** for one more condition or action — \"and also\", **－** for a limit or an\nexception — \"but not\", \"does not apply here\". `then` holds behaviour only: no `contract` mark, no Estimate block, no reading, no `supersedes`; those are lines of `tasks`, a section between `then` and `ratification`, a checklist in its blockquote — one line per page `update` with its `contract`, Estimate block, file, test, command and reading — the same lines that go into the Spec's `tasks` block. Slugs, file names and field values sit in code spans; bold is for section labels and operands only. One horizontal rule at most, after the Case or its last sub-case, and only when the agent's own text follows (case 159)."
      - old: "with its own `when`, `then` and\n`ratification`, and its own `given` unless it is the parent's word for word"
        new: "with its own `when`, `then`, `tasks` and\n`ratification`, and its own `given` unless it is the parent's word for word"
      - old: "always `given`, `when`, `then` and `ratification`, and\nno `recommend`"
        new: "always `given`, `when`, `then`, `tasks` and `ratification`, and\nno `recommend`"
    change: "the shape of a Case in the chat: the story sections by explicit rules, given as the facts then depends on, then as behaviour only, a tasks section as the checklist of the Spec, code spans, one rule after the Case (case 159)"
  - file: vault/wiki/case-schema.md
    change: "the Sections table gains `tasks` between `then` and `ratification` — a blockquote checklist in the chat, the `tasks` block in the Spec; Operands: ＋ is \"and also\", － \"but not / does not apply here\", none in context, problem, recommend; Language: the rules of the story sections and the cap of seven sentences, given as the facts then depends on, then as behaviour only, code spans; Splitting: a sub-case has its own tasks (case 159)"
```

```tasks
- [x] `vault/wiki/case-schema.md` by hand: the Sections table row `tasks`; the Operands paragraph; the Language paragraph (the story rules, the cap, `given`, `then`, code spans, the horizontal rule); the Splitting paragraph (`tasks` on a sub-case); the paragraph "One agent response ≈ one Case" unchanged
- [ ] `rule-case-protocol` applied by the librarian; `guppi render` writes `CLAUDE.md`; `guppi render --check` exit 0 at its close
- [ ] read `estimate-case-protocol-loaded` (block 159): the next session, the first Case written after the render — the story sections by the rules, `given` as facts, `then` as behaviour, `tasks` as a checklist, code spans, the rule only after the Case
```

## Case 160 — `decision-case-140`, `lesson-obsidian-property-links-need-wikilink-form`: a wikilink quoted in prose

> **context:**
> Lint reads every `[[…]]` in the body of a page as a link and requires that page to exist. One exception: inside backticks it is a quotation, not a link; Obsidian reads it the same way. When a page quotes the form of a link in plain quotes — `"[[slug]]"` — lint sees a link to a page `slug`, and Obsidian's graph an unresolved link. This happened twice before: Case 130.1 cured the pages of 112.x, Case 140 the pages of 130.x. Now the same quotation stands in the Context of `decision-case-140` itself (the librarian carried it from the chat as it was) and in the `root_cause` of the lesson on property links (written in the ledger line in quotes, the hook wrote it verbatim).

> **problem:**
> Two `ref` findings, the third time on the same thing; the pages or lint.

> **given:**
> `decision-case-140` Context: `"History and log lines end with · [[decision-case-N]] when a decision exists"` without backticks; its own Given carries the same phrase in backticks, no finding.
> **＋** `lesson-obsidian-property-links-need-wikilink-form`: the Root cause section and the `root_cause` field carry `"[[slug]]"`; Obsidian shows `slug` as an unresolved link from the section (checked by the owner), lint raises `ref` from the same place.
> **＋** `guppi lint`: `CODE_SPAN` drops a `[[…]]` inside backticks; Obsidian does the same (checked); `generate.update` applies `replace` to the body and `set` to the fields of a page of any category, with a History line — the precedent of 140 and 144.2.
> **＋** `decisions/schema.md`: "a decision is not edited" — 140 already decided that backticks change nothing signed.
> **－** The ledger line the lesson was born from is not rewritten; the page changes.

> **when:**
> The librarian applies the two updates; then `guppi lint` checks the bodies.

> **then:**
> In the Context of `decision-case-140` the phrase stands in backticks; in the Root cause section and the `root_cause` field of the lesson, `` `[[slug]]` `` in place of `"[[slug]]"`.
> **＋** The two `ref` findings go; two unresolved links leave the Obsidian graph.
> **－** No other page is touched; lint does not change.

```then
update:
  - slug: decision-case-140
    replace:
      - old: ": \"History and log lines end with · [[decision-case-N]] when a decision exists\" — without backticks"
        new: ": `\"History and log lines end with · [[decision-case-N]] when a decision exists\"` — without backticks"
    change: "the quoted wikilink of the Context in backticks: lint and Obsidian read a quotation, not a link (case 160)"
  - slug: lesson-obsidian-property-links-need-wikilink-form
    set:
      root_cause: "Obsidian reads a property value as a link only in the form `[[slug]]` (quoted in YAML, or it parses as a nested list); a bare slug is text; a property link is seen by the graph, backlinks, unresolved and Bases, and resolves in any folder, the archive included"
    replace:
      - old: "in the form \"[[slug]]\" (quoted in YAML"
        new: "in the form `[[slug]]` (quoted in YAML"
    change: "the quoted wikilink of the root cause in backticks: lint and Obsidian read a quotation, not a link (case 160)"
```

```tasks
- [ ] nothing in Work Mode: the librarian's run applies the two updates
- [ ] after the librarian's run: `guppi lint` raises no `ref` on `decision-case-140` and on the lesson (the next session's `/hi`)
```

## Case 161 — `rule-materialize`: the `then` item of a Rule-class file is found by `file`

> **context:**
> A change of a Rule-class file — `index.md`, `glossary.md`, `case-schema.md`, any `schema.md` — is written in the Spec as `case-schema.md` says: an `update` with the keys `file` and `change`, no `slug`. The ledger line carries a slug — `case-schema`, `index`. `materialize` looks for the `then` item of a ledger line by `slug` only; it finds none and marks the entry `incomplete: [then]`, though the item is there and the path of the file is derived from the slug anyway. So were the 13 entries of the run of P marked, and the entry of 133 in the run of O; the brief lists them under Flags each time as "the same class". The test of this case seeds an item with `slug` and `file` together — so it is green while a Spec written by the schema is red.

> **problem:**
> Every session that touches a Rule-class file leaves false `incomplete` marks in the yaml, and the brief lists them; the code or the shape of the item in the Spec has to change.

> **given:**
> `materialize.py` `find_item` compares `item["slug"]` with the slug of the line; `rule_class_path(slug)` gives the path for `index`, `glossary`, `case-schema`, `<category>-schema[-yaml]`; the branch "an item with `file`" after `find_item` is unreachable for an item without `slug`.
> **＋** `case-schema.md`: "A Rule-class file … is an `update` with `file` and `change`"; the Spec of this session (Case 159) is written that way.
> **＋** `tests/test_materialize.py:303` seeds `slug: glossary` with `file` — passes; no test seeds an item without `slug`.
> **＋** `rule-materialize` (`built`, `estimates: [estimate-materialize-assembles]`, `pending` by 158): "a Rule-class file is `file` with its `path`"; how the item is found the text does not say.
> **－** `generate` does not change: it skips a `file` entry with the line "applied by hand" as today.

> **when:**
> `guppi materialize` lifts a line `decision[case N][update][<rule-class slug>]` and looks for its item in the `then` block of the Spec.

> **then:**
> The item is found when its `slug` equals the slug of the line, or its `file` equals `rule_class_path(slug)`; `change` is lifted, `incomplete` is empty, `category: file`, `path` from `file`.
> **＋** An item with both keys is found as before.
> **－** A Rule-class slug with no item in `then` stays `incomplete: [then]`.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-assembles
    replace:
      - old: "a Rule-class file is `file` with its `path`"
        new: "a Rule-class file is `file` with its `path`; its `then` item is found by `slug`, or by `file` equal to the path the slug maps to, since the schema writes such an item with `file` and `change` alone (case 161)"
    change: "the then item of a Rule-class file is found by file as well as by slug; no false incomplete on a file entry (case 161)"
```

```tasks
- [x] `guppi/materialize.py`: `find_item` — a second pass over the items of the kind: an item whose `file` equals `rule_class_path(slug)` matches; the docstring says so
- [x] `tests/test_materialize.py`: a Spec item with `file` and `change` and no `slug` — the entry has no `incomplete`, `change` lifted, `category: file`, `path` from `file`; the test of line 303 unchanged
- [x] `make test`, `make style`
- [x] read `estimate-materialize-assembles` (blocks 158 and 161): the tests above; the librarian's run of this session — 0 `incomplete: [then]` on the `file` entry of Case 159
```

## Case 163 — `index`, `glossary`, `case-schema`: eight sections everywhere

> **context:**
> Case 159 added the section `tasks` — eight sections now — and named the places to change: the Render of `rule-case-protocol` and the table with the paragraphs of `case-schema.md`. The word "seven" stands in four more places: §2 of the map, the Case row of the glossary, the first sentence of the Sections part of `case-schema.md`, and the `ratification` row of the same table, which lists the sections of a second showing.

> **problem:**
> After the librarian's run `CLAUDE.md` says "eight" while the map, the glossary and the schema itself say "seven".

> **given:**
> `index.md` §2, line 130: "Seven sections: `context`, `problem`, `recommend`, `given`, `when`, `then`, `ratification`".
> **＋** `glossary.md` line 69, the Case row: the seven sections by name.
> **＋** `case-schema.md` line 11: "Seven, in this order."; the `ratification` row of the table: "always `given`, `when`, `then`, `ratification`, and no `recommend`".
> **－** The History line of `rule-case-protocol` and `log.md` say "seven" as history — untouched.

> **when:**
> Someone reads §2 of the map, the Case row of the glossary or the Sections part of the schema.

> **then:**
> All three say "eight" and list `tasks` between `then` and `ratification`; the `ratification` row of the schema reads "always `given`, `when`, `then`, `tasks` and `ratification`".
> **－** Nothing else in these files changes.

```then
update:
  - file: vault/wiki/index.md
    change: "§2: 'Seven sections: … `then`, `ratification`' → 'Eight sections: … `then`, `tasks`, `ratification`' (case 163)"
  - file: vault/wiki/glossary.md
    change: "the Case row lists eight sections, `tasks` between `then` and `ratification` (case 163)"
  - file: vault/wiki/case-schema.md
    change: "'Seven, in this order.' → 'Eight, in this order.'; the `ratification` row: 'always `given`, `when`, `then`, `tasks` and `ratification`' (case 163)"
```

```tasks
- [x] `vault/wiki/index.md` §2 by hand: "Eight sections: …, `then`, `tasks`, `ratification`"
- [x] `vault/wiki/glossary.md` the Case row by hand: eight by name
- [x] `vault/wiki/case-schema.md` by hand: "Eight, in this order."; the `ratification` row with `tasks`
- [x] `make lint` (`render --check` is not touched: the files are not rendered)
```

## Deferred

## Case 162 — Slice 3b: Work Mode, deferred once more

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since case 29, then 64, 78, 93, 107, 116, 129, 141, 152, without `kind`, `estimates` or `tags`; the two lint orphans and 8 `schema` findings. Case 152 (session P) deferred Slice 3b for the eleventh time.

> **problem:**
> The owner opened session Q on the readings due and the three deferred items of the brief, then on the shape of the Case and of the acknowledging reply — Cases 155–161 — and left Slice 3b for a session of its own. The two pages stay placeholders one more session; the postponement count goes to 12.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: The rule of Work Mode — the Spec as tasks with code, the ticked boxes, what a subagent may do, and the fork that comes back as a Case; the Plan Mode of a session of its own
  - slug: rule-subagent-guppi
    type: rule
    purpose: Governs Work Mode's subagents — they execute the Spec's tasks, never decide, and return a fork as a Case; the Plan Mode of a session of its own
```
