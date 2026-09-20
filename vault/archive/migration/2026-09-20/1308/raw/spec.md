<!-- approved 16:53:51 · session 04856573 -->

# Spec — 2026-09-20, session 1308

## Case 270 — the tick on a reading is set by the one who applied the reading

> **context:**
> Today `generate`, once it applied a `create`, `update`, `delete` or `defer` entry of `materialize.yaml`, ticks the page line of the Spec of the same session, in the section of the entry's Case (case 226.1). An `estimate` entry — the reading of an Estimate — ticks nothing: the Criterion of `estimate-generate-ticks-the-spec` says the `read` lines are the agent's. The agent writes the `estimate[...]` line into the ledger and must tick the `read` line of `spec.md` in the same reply; two actions of one event, and the second one is forgotten — three lines of the Specs 0958 and 0740 stand unticked with their readings `passed`. The librarian sees it and cannot repair it: the librarian writes only to `wiki/`. An `estimate` entry of the yaml carries no Case number, and a reading often lands in the Spec of another session (line 172 of session 0740 was read in 0958; the readings W1–W3 of this session are lines of the Spec 0958); a reading of the same session as the `create` folds into the `create` entry (`folded`).
> State of the pages: `rule-page-generation` `built`, `estimate-generate-ticks-the-spec` `passed`, its Criterion excludes `estimate`; `rule-case-protocol` `built`, `estimate-case-protocol-loaded` `passed` and names the sentence "Work Mode ticks … readings" in its Then, the same sentence stands in `case-schema.md`; `rule-retro` `built`, `estimate-retro-loads` `passed` and counts every unticked `read` line as debt; `rule-work-mode` `draft` (Slice 3b) untouched; the other six Estimates of `rule-page-generation` untouched; every `update` carries a `ref`, no vault query due.

> **problem:**
> The ledger line and the tick in the Spec are one event held by two agents: one has no right to write into the Spec, the other forgets. Who ticks the `read` line, and what the protocol and Retro say about Work Mode then.

### Case 270.1 — `generate` ticks the reading line

> **given:**
> A yaml entry of kind `estimate` carries `slug`, `status`, `result` and no `case`; a `create` entry with `folded` carries the reading of the same session.
> **＋** The Spec of the unit lies beside the yaml — `raw/<date>/<HHMM>/spec.md`; the Specs of the other sessions are the `spec.md` of their folders under `raw/`.
> **＋** A Case heading in the Spec is `## Case N — …` or `### Case N.M — …`; its section runs to the next such heading.
> **＋** A reading line of the Spec is `- [ ] read `<slug>`` with text after it, in any Case.
> **＋** `tests/test_generate.py` fixes the behaviour on a temp vault with a Spec beside the yaml and a second Spec in another session folder.
> **－** A Rule-class file entry `generate` does not apply — "applied by hand".

> **when:**
> `guppi generate` applied an entry and marked it `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit the first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes.
> **＋** Two entries of one kind and slug in one Case tick two lines, in order.
> **＋** For an `estimate` entry, and for a `create` entry with `folded`, the first unticked line `- [ ] read `<slug>`` becomes `- [x]` — in the Spec beside the yaml first, then in the `spec.md` of the other session folders of `raw/`, oldest first; one line per entry.
> **＋** A `create` entry with `folded` ticks both lines: the page line and the reading line.
> **－** A line not found, a section not found, no Spec — no error and no stderr line; the entry is `applied` all the same.
> **－** `lesson` and Rule-class file entries, and an entry marked `failed`, tick no line; the lines on code, tests, migrations and `by hand` are the agent's.
> **－** A Spec under `vault/archive/` is not read.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: |-
          Once an entry is applied, the script ticks its line in the Spec beside the yaml — `- [ ] <kind> `<slug>`` in the section of the entry's Case — so the Spec's page lines are closed by the one who did the work, and a line not found is no error (case 226.1).
        new: |-
          Once an entry is applied, the script ticks its line in the Spec — a page entry the line `- [ ] <kind> `<slug>`` in the section of the entry's Case of the Spec beside the yaml; an `estimate` entry, or a `create` with a folded reading, the first unticked `- [ ] read `<slug>`` line, in the Spec beside the yaml first and then in the `spec.md` of the other session folders of `raw/`, oldest first — so the Spec's page lines and reading lines are closed by the one who did the work, and a line not found is no error (cases 226.1, 270.1).
    change: generate ticks the read line of the Spec when it applies a reading, in this unit's Spec first and then in the other sessions of raw/ (case 270.1)
  - slug: estimate-generate-ticks-the-spec
    set: {status: pending}
    change: the Criterion replaced whole — an estimate entry and a create with a folded reading tick the read line, across the Specs of raw/ (case 270.1)
```

```tasks
- [x] update `rule-page-generation`: the Purpose sentence on the tick — page lines and reading lines
- [x] update `estimate-generate-ticks-the-spec`: the Criterion replaced whole, `pending`
- [x] `guppi/generate.py`: a `READ_LINE` pattern for `- [ ] read `<slug>``, `tick` on `estimate` entries and on `create` entries with `folded`, the walk of the `spec.md` of the other session folders of `raw/` oldest first, the docstring
- [x] `tests/test_generate.py`: a reading ticked in the same Spec; a reading ticked in another session's Spec; a `create` with `folded` ticks both lines; a `lesson` entry ticks none; nothing found — `applied`, no stderr
- [x] by hand, a one-off: `[x]` on lines 249, 432, 191 of `raw/2026-09-20/0958/spec.md` and line 172 of `raw/2026-09-20/0740/spec.md` (W5)
- [x] read `estimate-generate-ticks-the-spec`: pytest; live — the librarian's run of this session, the `read` lines W1–W3 of the Spec 0958 after it
```

### Case 270.2 — the protocol says who ticks which lines

> **given:**
> `CLAUDE.md` is the Render of `rule-claude-md` with the Case protocol section from `rule-case-protocol`, loaded at session start; `case-schema.md` carries the same sentence on the ticks.
> **＋** `estimate-case-protocol-loaded` is the live reading of that Render; its Criterion is replaced whole.
> **＋** `tests/test_ledger.py` fixes the preview cases.

> **when:**
> A session starts with `CLAUDE.md`.

> **then:**
> The agent states the LEDGER-block rule and the one-Case-at-a-time rule without a read call.
> **＋** The Case protocol says the Spec is `raw/<date>/<hi HHMM>/spec.md` — the `## Deferred` heading, the ticked boxes — and the Frontier `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** A reply with a `LEDGER` block ends in that text; no tool call follows in the same reply — the text before a tool call waits for the next `Stop` of the session, and the last reply of a session has none.
> **＋** A block a tool call did follow the agent does not call lost before the `Stop` of that turn; at the next `Stop` it checks the ledger, and only a line missing there is a lesson.
> **＋** The Case protocol says Work Mode ticks the boxes on code, tests, migrations and `by hand` checks; `generate` ticks the page lines and the `read` lines whose reading stands in the ledger; `render` and `sprint` tick the render and sprint lines (cases 226, 250, 270).
> **－** A reply whose ledger lines sit outside a `LEDGER` block — bare, or in a fence with another tag or none — adds nothing to the session's ledger.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: |-
          Work Mode ticks the boxes on code, tests, migrations and readings in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; `generate`, `render` and `sprint` tick the page, render and sprint lines (cases 226, 250); Retro counts the unticked.
        new: |-
          Work Mode ticks the boxes on code, tests, migrations and `by hand` checks in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; `generate` ticks the page lines and the `read` lines whose reading stands in the ledger, `render` and `sprint` the render and sprint lines (cases 226, 250, 270); Retro counts the unticked.
    change: the tick sentence of the Render — readings ticked by generate, not by Work Mode (case 270.2)
  - slug: estimate-case-protocol-loaded
    set: {status: pending}
    change: the Criterion replaced whole — the tick sentence names generate on the read lines (case 270.2)
  - file: vault/wiki/case-schema.md
    change: the tick sentence of "The Spec is written as each Case is ratified" — Work Mode ticks code, tests, migrations and by-hand checks, generate the page and read lines, render and sprint theirs (cases 226, 250, 270)
```

```tasks
- [x] update `rule-case-protocol`: `replace` of the tick sentence in the Render
- [x] update `estimate-case-protocol-loaded`: the Criterion replaced whole, `pending`
- [x] `vault/wiki/case-schema.md` by hand: the tick sentence in "The Spec is written as each Case is ratified"
- [x] render `CLAUDE.md`
- [x] read `estimate-case-protocol-loaded`: the first turn of the next session, by hand
```

### Case 270.3 — Retro does not count as debt a reading that stands in the ledger

> **given:**
> Retro runs before the librarian; `generate` after it ticks the page lines and the `read` lines whose reading stands in the ledger, `render` and `sprint` the render and sprint lines (cases 226, 250, 270.1).

> **when:**
> The person invokes `/retro`, and the agent counts the unticked `tasks` of the Spec.

> **then:**
> A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the ledger of this session are listed as waiting for the librarian and end in none of the four ways; every other unticked line is debt, as today.
> **－** A `read` line without its line in the ledger is debt: the reading was not done.
> **－** Nothing else in Retro changes.

```then
update:
  - slug: rule-retro
    replace:
      - old: |-
          a `create`, `update` or `defer` line of a page, a `guppi render` line and a `guppi sprint` line listed as waiting for the librarian, who ticks them (cases 226, 250), not as debt;
        new: |-
          a `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the Tail above listed as waiting for the librarian, whose scripts tick them (cases 226, 250, 270), not as debt — a `read` line without its line in the Tail is debt;
    change: a read line whose reading stands in the ledger waits for the librarian, not debt (case 270.3)
  - slug: estimate-retro-loads
    set: {status: pending}
    change: the Criterion replaced whole — the read line with its ledger line waits for the librarian (case 270.3)
```

```tasks
- [x] update `rule-retro`: `replace` of the waiting-for-the-librarian sentence in the Render
- [x] update `estimate-retro-loads`: the Criterion replaced whole, `pending`
- [x] render `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-loads`: the first `/retro` after the render, by hand — this session
```

## Case 271 — the librarian's ban on `spec.md` against Readings due and Next session

> **context:**
> The librarian's frame — the Render of `rule-documentation`, the file `.claude/agents/librarian-guppi.md` — forbids it to read `ledger.md`, `spec.md`, the plan, the Decision pages and the archive: what the scripts do with the yaml is written in the frame itself, and the librarian must not draw judgments from the session. Later the same frame got two sections of the brief that need lines of the Spec: Readings due takes the place of a reading from the unticked `- [ ] read …` line (case 200.3), Next session lists the unticked boxes of the Specs (case 268.1). The ban stayed as it was, and the frame orders one thing and forbids the same. The Criterion of `estimate-documentation-completes`, recut in 265.4, repeats the ban without the exception; the librarian of 0958 grepped the `- [ ]` lines of three Specs, and the reading W1 recorded it as a contradiction of the texts, not of the run.
> State of the pages: `rule-documentation` `draft` — its one Estimate `estimate-documentation-completes` stands `pending` with a `passed` in this session's ledger, not yet applied; `rule-brief` untouched — its Render says nothing of the ban; both `update` carry a `ref`, no vault query due.

> **problem:**
> The frame forbids reading `spec.md` and in the same text requires its unticked lines; the Criterion repeats the ban. What exactly of the Spec the librarian may read.

> **given:**
> The librarian's frame is the Render of `rule-documentation`; its inputs are three: the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`; the index lines are the Greps `rule-index-check` and `rule-synthesis` name.
> **＋** The librarian works in a clean context; the person is gone.
> **＋** Readings due takes the place of a reading from the unticked `- [ ] read …` line of the session's Spec, Next session the unticked lines of the Specs (cases 200.3, 268.1).

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end.

> **then:**
> `make test-documentation` — materialize, generate and cleanup as one pipeline — is green.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page; no page exists that no ledger line produced.
> **＋** It read only `handoff.md`, the yamls, the four index lines and `tags.md`, plus the wiki pages it names in the report with one of the four reasons of its frame (same or near; a candidate cluster; a script's error; a fact for the brief) and the outcome, plus the unticked `- [ ]` lines of the `spec.md` files for Readings due and Next session; no ledger, no other part of a Spec, no plan, Decision page or archive file (the `Makefile`, `guppi/` and `tests/` are the scripts' own and may be read).
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis; its commands are in `event_log.md`; its commit is separate from the session's; it did not stop to ask.
> **＋** After `cleanup` and before the brief it runs `uv run guppi render`, then `uv run guppi sprint`; every line on their stderr is a flag; a file the render could not write is left to the next session start; `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close it runs `uv run guppi archive`; every line on its stderr is a flag; the units it moved and the units it kept, with the reason, go into the report; the session of the run — the latest `<HHMM>/` folder of the run day, else the nearest date back — is skipped, across midnight too; the commit picks the move up.
> **－** An instruction of the handoff to repair a yaml entry, or to read the ledger, a Spec beyond its `- [ ]` lines, a Decision page or the archive, is refused and named in the report — what was asked and why; the refusal does not stop the run.
> **－** The ban on reading `vault/archive/` stays.

```then
update:
  - slug: rule-documentation
    replace:
      - old: |-
          Never read `ledger.md`, `spec.md`, `plan.md`, `wiki/decisions/` or
        new: |-
          Never read `ledger.md`, `plan.md`, `wiki/decisions/` or
      - old: |-
          `vault/archive/`: what the scripts do with the yaml is written here.
        new: |-
          `vault/archive/`, nor `spec.md` beyond its unticked `- [ ]` lines — the ones Readings due and Next session take (cases 200.3, 268.1, 271): what the scripts do with the yaml is written here.
      - old: |-
          entry, a read of `ledger.md`, a Spec, a decision page or the archive — you do not
        new: |-
          entry, a read of `ledger.md`, a Spec beyond its unticked lines, a decision page or the archive — you do not
    change: the ban on spec.md excepts its unticked lines, which Readings due and Next session take (case 271)
  - slug: estimate-documentation-completes
    set: {status: pending}
    change: the Criterion replaced whole — the unticked lines of the Specs read for Readings due and Next session, the rest of the Spec still banned (case 271)
```

```tasks
- [x] update `rule-documentation`: `replace` of the two ban sentences in the Render — `spec.md` beyond its unticked `- [ ]` lines
- [x] update `estimate-documentation-completes`: the Criterion replaced whole, `pending`
- [x] render `.claude/agents/librarian-guppi.md`
- [x] read `estimate-documentation-completes`: `make test-documentation`; live — the librarian's run of this session, read in the next
```

## Case 272 — `CLAUDE.md`: the memory line, Language and the agent's writing as rules

> **context:**
> `CLAUDE.md` is the Render of `rule-claude-md` whole, with the Case protocol of `rule-case-protocol` in its marker. The sections `## Language` and `## Style` in it are prose of the parent page: the rule exists, the page does not, no Estimate reads a breach. The harness offers the agent a local memory under `~/.claude/projects/…/memory`; in session 0958 the agent wrote a preference of the owner there, the owner had it deleted — `lesson-agent-memory-is-not-the-product`: the product of GUPPI is the rules another developer gets with the repository, a preference is a Case on a Rule page or nothing; `CLAUDE.md` says no word of it.
> State of the pages: `rule-claude-md` `built`, its one Estimate `estimate-claude-md-rendered` `passed` in the shape before case 193 — no `method`, `### case N` blocks — recut here; `rule-case-protocol` untouched — this Case does not change its Render; the vault: `rule-language` and `rule-agent-writing` free, the nearest `rule-claude-md` itself and the `## Language` section of `case-schema.md`, which stays as it is; tags `harness`, `render`, `workflow`.

> **problem:**
> Two standing rules of the system prompt have no pages, and the agent is not told that the vault is the only memory. How `CLAUDE.md` splits into rules and where the memory line stands.

### Case 272.1 — `rule-claude-md`: the memory line and the markers

> **given:**
> `CLAUDE.md` is the Render of `rule-claude-md` whole; a `partial` child lands in its marker line `<!-- slug -->`, the markers stay; a child without a marker line is a `render` error.
> **＋** `children` and `parent` are filled by the scripts from the `ref` of the pages created.
> **＋** `tests/test_render.py` fixes the splice of several children into one `full` file.

> **when:**
> The first `uv run guppi render` after `rule-claude-md` or any of its children changed, and a session start with `CLAUDE.md`.

> **then:**
> `CLAUDE.md` equals the Render of `rule-claude-md` with the text of each child between its markers; the diff of that render holds only the text those pages gained since the file was last written; `guppi render --check` then exits 0.
> **＋** The first paragraph of `CLAUDE.md` says: the vault is the only memory; the agent writes no note outside the repository — not the harness's local memory directory, not a file outside `vault/`; what is worth keeping is a `lesson` line or a Case on a Rule page.
> **＋** Every session loads the same text, its `@` imports expanded.
> **－** The sections `## Language` and `## How the agent writes` in the Render of `rule-claude-md` are marker lines only — `<!-- rule-language -->`, `<!-- rule-agent-writing -->`; their text lives on `rule-language` and `rule-agent-writing`.

```then
update:
  - slug: rule-claude-md
    replace:
      - old: |-
          are unsure whether something needs ratification: it does.
        new: |-
          are unsure whether something needs ratification: it does. The vault is the only memory: write no note outside the repository — not the harness's local memory directory, not a file outside `vault/`; what is worth keeping is a `lesson` line or a Case on a Rule page (case 272.1).
      - old: |-
          ## Language

          English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. Russian for chat with the owner: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. English technical terms are not transliterated into Cyrillic.
        new: |-
          <!-- rule-language -->
      - old: |-
          ## Style

          Keep the facts and remove the sales pitch. Name a real source or remove the claim. Short
          sentences, active voice, a common word over a term. Give the answer first. Say what is done
          and what is not done; never leave the not-done implied.
        new: |-
          <!-- rule-agent-writing -->
      - old: |-
          Rendered in full into `CLAUDE.md`; `rule-case-protocol` splices into its marker.
        new: |-
          Rendered in full into `CLAUDE.md`; each child — `rule-case-protocol`, `rule-language`, `rule-agent-writing` — splices into its marker line.
      - old: |-
          `rule-case-protocol` has this page as its parent since case 66 and is its one child; the renderer splices it into the marker.
        new: |-
          `rule-case-protocol` has this page as its parent since case 66, `rule-language` and `rule-agent-writing` since case 272; the renderer splices each into its marker.
    change: the memory sentence in the first paragraph; Language and Style leave the Render for the children rule-language and rule-agent-writing, marker lines in their place (case 272.1)
  - slug: estimate-claude-md-rendered
    set:
      status: pending
      purpose: CLAUDE.md equals the Render of rule-claude-md with each child between its markers, and every session loads that text
      method: uv run guppi render and guppi render --check after the build, plus one reading of CLAUDE.md at the next session start, by hand
    change: the recut to the shape of case 193 — purpose, method, the Criterion replaced whole; three children spliced, the memory sentence (case 272.1)
```

```tasks
- [x] update `rule-claude-md`: the memory sentence in the first paragraph of the Render; `## Language` and `## Style` → marker lines; How it works names three children
- [x] update `estimate-claude-md-rendered`: the recut to the shape of case 193 — `method`, the Criterion replaced whole, `pending`
- [x] render `CLAUDE.md`
- [x] read `estimate-claude-md-rendered`: `uv run guppi render` and `--check` after the build; the next session start, by hand
```

### Case 272.2 — `rule-language`

> **given:**
> The conditions of the parent.
> **＋** `rule-language` is a Leaf, `enforcement: render`, `render_mode: partial`, `governs: CLAUDE.md`, a child of `rule-claude-md`; its Render is the section `## Language` inside the marker `<!-- rule-language -->`.

> **when:**
> A session starts with `CLAUDE.md`, and the agent writes — into the repository or into the chat.

> **then:**
> Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the Spec — is English; the chat with the owner is Russian, a Case is discussed in the chat in Russian in all its sections and enters the Spec translated.
> **＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language; English technical terms are not transliterated into Cyrillic.
> **－** The rule speaks of the language, not of the Case form — the form is `case-schema.md`.

```then
create:
  - slug: rule-language
    type: rule
    kind: Leaf
    purpose: Keeps the repository in English and the chat with the owner in Russian, with slugs, paths and quotations unchanged in either
    enforcement: render
    governs: CLAUDE.md
    render_mode: partial
    ref: rule-claude-md
    tags: [harness, render, workflow]
    sections:
      Purpose: |
        Keeps the repository in English and the chat with the owner in Russian. Until case 272 the
        rule was a section of the Render of `rule-claude-md`: a standing condition with no page and
        no Estimate. A Case is discussed in Russian and enters the Spec in English (case 123); the
        manner of the English that lands in the vault — ASD-STE100 Simplified Technical English —
        is the `## Language` section of `case-schema.md`, which this rule does not repeat.
      Render: |
        <!-- rule-language -->
        ## Language

        English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. Russian for chat with the owner: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. English technical terms are not transliterated into Cyrillic.
        <!-- /rule-language -->
  - slug: estimate-language-followed
    type: estimate
    ref: rule-language
    kind: QA
    purpose: The section stands in CLAUDE.md and a session follows it — English in the repository, Russian in the chat, slugs and paths unchanged
    method: one reading by hand in the next session — the section in CLAUDE.md, the session's commit, Spec and chat against it
    tags: [harness, render, workflow]
```

```tasks
- [x] create `rule-language`, `ref: rule-claude-md`
- [x] create `estimate-language-followed`, `ref: rule-language`
- [x] render `CLAUDE.md`
- [x] read `estimate-language-followed`: the next session, by hand — the section in `CLAUDE.md`, the commit, the Spec and the chat of the session
```

### Case 272.3 — `rule-agent-writing`

> **given:**
> The conditions of the parent.
> **＋** `rule-agent-writing` is a Leaf, `enforcement: render`, `render_mode: partial`, `governs: CLAUDE.md`, a child of `rule-claude-md`; its Render is the section `## How the agent writes` inside the marker `<!-- rule-agent-writing -->`.

> **when:**
> A session starts with `CLAUDE.md`, and the agent writes a text — a reply, a page, a commit message, a document.

> **then:**
> The facts stay and the sales pitch goes; a claim names a real source or goes; short sentences, active voice, a common word over a term; the answer first; what is done and what is not done are named, the not-done never implied.
> **－** The rule is about the agent's text, not about code — `make style` holds the style of the code.

```then
create:
  - slug: rule-agent-writing
    type: rule
    kind: Leaf
    purpose: Keeps the agent's text to facts with a source, short active sentences, the answer first and the not-done named
    enforcement: render
    governs: CLAUDE.md
    render_mode: partial
    ref: rule-claude-md
    tags: [harness, render, workflow]
    sections:
      Purpose: |
        Keeps the agent's text — replies, pages, commit messages, documents — to facts with a
        source, short active sentences, the answer first and the not-done named. Until case 272 the
        rule was the section `## Style` of the Render of `rule-claude-md`: a standing condition with
        no page and no Estimate. It is about the agent's prose; the style of the code is `make style`.
      Render: |
        <!-- rule-agent-writing -->
        ## How the agent writes

        Keep the facts and remove the sales pitch. Name a real source or remove the claim. Short
        sentences, active voice, a common word over a term. Give the answer first. Say what is done
        and what is not done; never leave the not-done implied.
        <!-- /rule-agent-writing -->
  - slug: estimate-agent-writing-followed
    type: estimate
    ref: rule-agent-writing
    kind: QA
    purpose: The section stands in CLAUDE.md and one reply of the session holds to it — facts with a source, short sentences, the answer first, the not-done named
    method: one reading by hand in the next session — the section in CLAUDE.md and one reply of the agent against it
    tags: [harness, render, workflow]
```

```tasks
- [x] create `rule-agent-writing`, `ref: rule-claude-md`
- [x] create `estimate-agent-writing-followed`, `ref: rule-agent-writing`
- [x] render `CLAUDE.md`
- [x] read `estimate-agent-writing-followed`: the next session, by hand — the section in `CLAUDE.md` and one reply of the agent against it
```

## Case 273 — `case-schema.md` as the Render of `rule-case-protocol`, the import moved to `/hi`

> **context:**
> The Case form is described twice: in `case-schema.md`, a Rule-class file edited by hand and imported into `CLAUDE.md`, and in the Render of `rule-case-protocol`, spliced into the same `CLAUDE.md`. Four of the nine paragraphs of the Render repeat the schema word for word — the form, the operands, the story sections, the sub-cases, the writing of the Spec; every change of the form was signed twice (267 changed both). Five paragraphs stand only in the Render — the Frontier, the acknowledging reply, the harness rendered from `rules/`, `ask-guppi` before a `create`, the ledger mechanics — and the schema does not know them. A session without `/hi` carries all that text although no Case is possible without `/hi`: the ledger hook refuses.
> State of the pages: `rule-case-protocol` `built`, `governs: CLAUDE.md`, `partial`, parent `rule-claude-md`; its `estimate-case-protocol-loaded` `pending` from 270.2 — its Criterion is replaced once more here, the sentence of 270.2 inside; the three other Estimates of the rule read the behaviour, not the delivery, and are untouched. `rule-claude-md` `built`, its `estimate-claude-md-rendered` `pending` from 272.1 — replaced a second time here, the text of 272.1 whole. `rule-internal-context` `built`, `estimate-internal-context-loaded` `passed` in the shape before case 193. `rule-plan-mode` a MOC of four children, its Estimates untouched. The Rule-class files `glossary.md` and `index.md` call the schema "imported into CLAUDE.md" — changed by hand. Compaction and subagents are out of scope by the owner's decision.

> **problem:**
> One text in two places, signed twice; a part of the protocol stands only in the system prompt, where nobody reads it as the schema. Where the one text on the Case lives, and when it reaches the session.

### Case 273.1 — `rule-case-protocol` renders `case-schema.md`

> **given:**
> A `full` page writes the whole file named by `governs`, without its outer markers; a child of a `full` page governs the same file as its parent, otherwise `render` errors (case 277).
> **＋** The `children` of a Rule MOC is an ordered list, set explicitly.
> **＋** `tests/test_render.py` fixes a `full` render into a file outside `.claude/`.

> **when:**
> The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

> **then:**
> `vault/wiki/case-schema.md` equals the Render of `rule-case-protocol`; `render --check` exits 0; the file is no longer edited by hand — the hook refuses.
> **＋** The schema holds one text: what stood in it, plus from the old Render — the Frontier `frontier.md` and the closing of its lines, Plan Mode not ending while a line is open; the acknowledging reply of four parts; the harness rendered from `rules/`, never by hand; `ask-guppi` before a `create` without a `ref`, the answer in `context`; the ledger mechanics — the `LEDGER` block, the `Stop` hook, `{tags}`, `{source}`, when each line is written, the refusal without `/hi`, a reply with the block ending in it, a block a tool call followed not lost before `Stop`.
> **＋** The tick sentence in the wording of 270.2; the Language section of the schema on the manner of the English of the vault, the language of the repository and the chat being `rule-language`.
> **＋** At `/hi` the agent states the LEDGER-block rule and the one-Case-at-a-time rule without a read call.
> **－** Nothing of the schema is repeated in `CLAUDE.md`; `rule-case-protocol` is a child of `rule-plan-mode`, the last of its list.

```then
update:
  - slug: rule-case-protocol
    set:
      governs: vault/wiki/case-schema.md
      render_mode: full
      parent: "[[rule-plan-mode]]"
    sections:
      Purpose: |
        Prevents a decision from being acted on before it is ratified, or ratified without its
        content in view. This is instruction, not enforcement — no hook can check "did you
        finish the Frontier" or "did you wait for the sign-off" — so it is written where the
        agent sees it in every working session: `vault/wiki/case-schema.md`, the Render of this
        page, loaded by `/hi` with `sprint.md` and `brief.md` (case 273.1). A session without
        `/hi` holds no Case — the ledger hook refuses — and carries none of this text; `CLAUDE.md`
        keeps the one rule and the glossary. Until case 273 the Render was a section of `CLAUDE.md`
        and the schema a file edited by hand; the two said the same thing twice and were signed
        twice. `parent: rule-plan-mode` is the rule of the phase in which a Case is held (case 188).
      Render: |
        <!-- rule-case-protocol -->
        # Case — schema

        `wiki/case-schema.md` — the Render of `rule-case-protocol`, loaded by `/hi` with `sprint.md` and `brief.md`, so the structure is present from the first turn of a working session rather than read as a file; the map of the vault is [[index]]. A session without `/hi` holds no Case: the ledger hook refuses it.

        A Case is the unit of dialogue, not a vault page. It lives only inside a session. This schema exists because the Case is where content gets ratified: whatever is not in a Case was never signed by anyone.

        **One agent response ≈ one Case.**

        ## Plan Mode and the Frontier

        One reply is one Case, in the eight sections below. That is the form of Plan Mode. The Frontier is `raw/<date>/<hi HHMM>/frontier.md`, written at `/hi`; close its line in the reply that ends the item — `· case N` when ratified, `· work` when it needed no decision, `· defer case N` when deferred. Plan Mode does not end while a line is open; `/pre-spec` checks it. Never move to the next Case until this one is ratified or deferred.

        ## Sections

        Eight, in this order. Each is one blockquote: the first line `**name:**`, the text on the following quoted lines.

        | Section | Required | Content |
        |---|---|---|
        | `context` | yes | What this is about, in plain words. In Work Mode this may shrink to a one-line reference back to an earlier Case; it is never omitted. |
        | `problem` | yes | What requires a decision. |
        | `recommend` | yes | The agent's suggestion. Not carried onto the Decision page. |
        | `given` | yes | The conditions of the behaviour: one per line, and only a condition a line of `then` depends on — the rule that constrains, the test that fixes the behaviour. The state of the pages the Case changes, what conflicts, what sits in `draft`, the vault's answer and which Estimates of the rule the Case touches go to `context` (case 188). |
        | `when` | yes | The action that triggers the behaviour: a hook fires, a script runs, the person invokes a skill. For a change to a document, the moment someone reads it. |
        | `then` | yes | What holds after the action, once the recommendation is accepted. Behaviour only: no Estimate block, no reading, no `supersedes` — those are lines of `tasks` (cases 159, 188). |
        | `tasks` | yes | The work the Case leaves: a checklist, one line per page `update`, file, test, command, one-off migration and reading; no `contract` line, no "block N" line (case 188). In the chat a blockquote with the checklist; in the Spec the block tagged `tasks` — the same lines (case 159). |
        | `ratification` | yes | The human's sign-off, question, or their own alternative. Ends with a preview of the ledger lines in an untagged fence, and the turn ends with a plain question in the chat, never a picker tool. A Case the person changed is shown again: `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and no `recommend` (cases 62, 163). |

        ## Operands

        In `given`, `when` and `then`, the first line stands alone. Every further line starts with a bold operand: **＋** for one more condition or action — "and also", **－** for a limit or an exception — "but not", "does not apply here". One statement per line. `context`, `problem` and `recommend` carry no operand (case 159).

        ## Language

        Short sentences. One idea per sentence. Active voice. A common word over a term. Russian in the chat with the owner: a Case is discussed there in Russian, all its sections. English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Case enters the Spec translated, its slugs, field names and ledger lines unchanged (case 123). The language of the repository and of the chat as a standing rule is `rule-language`, in `CLAUDE.md`.

        The story sections — `context`, `problem`, `recommend` — name the slug of the thing described only; no count of sentences, the shape of each bounds it: `context` opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages, and closes with one sentence of bookkeeping — the state of the pages the Case changes, the vault's answer, the Estimates of the rule the Case touches and the ones it does not; a case number stands in `context` or `problem` only when the Case is about that case; no line numbers and no quotation unless the Case is about one; `problem` says what is wrong, or the question answered, in one paragraph; `recommend` says the choice and why, the rejected option in one sentence (case 267). `given` holds the conditions of the behaviour, one per line, and only a condition a line of `then` depends on: the rule that constrains, the test that fixes the behaviour; no state of pages, no history, no quotation for its own sake (case 188). `then` holds behaviour only; the bookkeeping is `tasks`. Slugs, file names and field values sit in code spans; bold is for section labels and operands only. In the chat one horizontal rule at most, after the Case or its last sub-case, and only when the agent's own text follows. The Spec keeps its form — the blockquotes in English, the `then` and `tasks` blocks — and the scripts read nothing of the chat form (case 159).

        ## `given`, `when` and `then` are the Criterion

        The Case that creates an Estimate writes its Criterion; the Case that changes a promise names the Estimate by slug and replaces its Criterion whole. The scripts copy the Case's `given`, `when` and `then`, verbatim with their operands, as the Estimate's `Criterion` — `Given:`, `When:`, `Then:` — replacing what stood there and setting the page `pending`, unless the item wrote the Criterion under `sections` itself, which then stands, on an `update` as on a `create` (case 204); no `### case N` block, nothing appended, and nothing removed by a `{supersedes:case N}` — the replaced text stays in the Spec of its session and in History. Only a replaced Criterion sets `pending`: an `update` of a rule's `Purpose` touches no Estimate, an `update` of its `Render` touches the Estimate of the live reading of that Render (case 187). One promise per Case or sub-case: a Case that touches two promises is two sub-cases, and pre-spec asks for the split. Nothing is signed twice, and nothing is signed in two wordings (cases 72.1, 188). A `when` on a slash command names the path it covers — the person's typed command on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`, or both; the reading of a `then` that covers both takes both (case 173).

        ## The `then` block lives in the Spec

        Ratifying "create entity-x" without seeing what that page will claim is an empty ratification. The human signs content, not the fact that a decision occurred. The content is a YAML block tagged `then` under the Case in the Spec — the plan the human approves at the end of Plan Mode — not in the chat. A list under each decision type present, one entry per target, `slug` first.

        ```then
        create:
          - slug: entity-cart
            type: entity
            kind: MOC
            purpose: Lets a buyer review an order before paying
            tags: [cart, checkout]
            sections:
              Purpose: |
                Until now items went straight from the catalogue to payment.
          - slug: estimate-cart-renders-in-time
            type: estimate
            ref: entity-cart
            kind: Research
            purpose: Whether the cart renders within 200ms, and what dominates the time if not
            method: measure the render at 10, 50 and 200 line items, against a seeded database
            tags: [cart, performance]
        update:
          - slug: entity-checkout
            set: {tags: [cart, checkout, payment]}
            change: the cart precedes payment
          - slug: estimate-checkout-orders-the-steps
            set: {status: pending}
            change: the Criterion replaced whole — the cart precedes payment
        ```

        A `create` holds the fields the target schema needs a judgment for; prose for a body section goes under `sections`, keyed by the section name. A new promise is an explicit `create` of an Estimate: its own item, `ref` naming the target, its slug written in the Case — `estimate-<target minus its prefix>-<promise>` — with `kind`, `purpose`, `method` and `tags`; its Criterion is the Case's `given`, `when` and `then`, lifted by the scripts, or the text the item writes under `sections: Criterion` (cases 188, 194.1). A `create` of a rule or an entity carries no `method`, `estimate_kind` or `estimate_slug`; nothing is derived from it. A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate. An `update` holds `set` (fields), `sections` (the whole new text of a section), `replace` (a list of `{old, new}` pairs, each `old` replaced by its `new` inside the body; one pair is a list of one, and a mapping under `replace` is a shape `generate` rejects), `change` (one line for History) and, when the page changes its slug, `rename` (the new slug, the same category prefix; the page moves and every link to it in the live pages follows, `origin`, History and Result kept — case 258.1); it carries no `contract`. An `update` of an Estimate carries `slug`, `set: {status: pending}` and `change` — and `set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211); the scripts replace its Criterion with the Case's `given`, `when` and `then`, or keep the text the item wrote under `sections: Criterion` (case 204). One promise per Case or sub-case: two touched promises are two sub-cases, and pre-spec asks for the split. A `delete` holds `impact`, a `defer` a `type` and a `purpose`. A Rule-class file (`index.md`, `glossary.md`, a schema) is an `update` with `file` and `change`, applied by hand in Work Mode; `CLAUDE.md` and this file are not — they are rendered from `rule-claude-md` and `rule-case-protocol` and change by an `update` of one of them (cases 59.8, 273.1). New tags are declared under `new_tags` with a meaning and a Russian alias, under any Case of the Spec (case 61).

        **The Spec is written as each Case is ratified**, into the plan file, in the reply that carries the Case's ledger lines: `context`, `problem`, `given`, `when`, `then`, the `then` block and a block tagged `tasks` — one `- [ ] <what>` per file to change, test to write, command to run, one-off migration, and one per reading of an Estimate the Case creates or sets `pending`, by its slug. `recommend` and `ratification` stay in the chat; code is Work Mode. Work Mode ticks the boxes on code, tests, migrations and `by hand` checks in `raw/<date>/<hi HHMM>/spec.md`, the session's folder (case 73), in the reply that finishes the task; `generate` ticks the page lines and the `read` lines whose reading stands in the ledger, `render` and `sprint` the render and sprint lines (cases 226, 250, 270); Retro counts the unticked (case 59.3).

        Derivable fields — `origin`, `status`, `parent` from `ref`, `children`, `code_ref`, `deferred_by` — are filled mechanically and are not written here. `guppi materialize` reads the blocks, and what is not in a block was signed by nobody.

        **The slug is written in the Case**, and pre-spec checks it. Meaningful, never an index: `entity-cart`, `lesson-hooks-sessionstart-cannot-block`. The page's category comes from its prefix: `rule-`, `entity-`, `estimate-`, `lesson-`, `insight-`. Decision pages are the one exception: `decision-case-<N>`, one per Case, written by the script.

        ## The vault before a `create`

        Before a `create` without a `ref`, ask the vault first: does this exist, what conflicts, what sits in `draft`, which tags fit. Dispatch the `ask-guppi` agent with one short question and put the answer in `context`. An `update` carries a `ref` and reads the page itself.

        ## The short form — deferred decisions

        A deferred decision is its own Case in the short form — `## Case N — name`, then `context`, `problem`, and a `then` block with `defer:` carrying `slug`, `type` and `purpose`; no `recommend`, `given`, `when` or `then` section. It has two moments: the close of Plan Mode, when the person defers the items left open, and Retro, which ratifies no other decision. Either way the agent appends it to `raw/<date>/<hi HHMM>/spec.md` under the `## Deferred` heading before writing its ledger line, one line per target, so `materialize` finds it like any other Case; a defer line without its Case is marked `incomplete`. Two or more pages share one Case only when one context and one problem hold for all of them. A page-less Slice task goes to `sprint.md`, not into a defer. Taking a deferred decision up means building its full Case from its page — `context` and `problem` as they stand, then `recommend`, `given` (the vault asked), `when`, `then` — and writing `{supersedes:case N}` on the line. A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5).

        ## Splitting

        If the human's reply to a Case is a follow-up question, the Case was not atomic. Detect this and propose splitting into sub-cases — recursive dotted ids, `1.1`, `1.1.1`. A sub-case is `### Case N.M — name` under its parent, with its own `when`, `then`, `tasks` and `ratification` (case 159), and its own `given` unless it is the parent's word for word; `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing one there (case 60). Ratifying a parent does not ratify its children.

        A question that only asks you to justify a choice already on the table ("why this approach?") does **not** split the Case. A question whose answer requires a new choice with its own consequences ("how will we handle X?") **does**.

        **Never move to another Case until the current one is ratified or deferred.**

        ## What a Case produces

        | Outcome | Ledger line |
        |---|---|
        | ratified decision | `- decision[case 12][update][rule-x]{ref:rule-x}` or `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` |
        | a measurement taken | `- estimate[slug][passed\|failed] <date, command or place; the result>` (case 199) |
        | something learned | `- lesson[error\|knowledge][slug]{tags:a,b} trigger: <...> root_cause: <...>` |

        The id is `case N` — the word and a space — in the first bracket and in `{supersedes:case N}` alike; `{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1).

        **Decision lines are markup only** — their content already sits ratified in the Spec, so the
        line just names what happens to which page, and the tags a `create` was ratified with.

        **Estimate and lesson lines carry their text inline.** Their content is born in the moment
        and exists nowhere else: a measurement taken after the tests were written, a failure
        understood while still fresh. There is nothing in the Spec to point at.

        An `estimate[...]` line does not replace the `decision[...]` that created the page — the
        decision made it exist, the estimate line fills it.

        Only the **main agent** writes ledger lines. A subagent that takes a measurement returns it; the main agent records it. A subagent that hits a fork stops and returns — it never decides.

        Ledger lines are written by the `Stop` hook, from the reply, verbatim, each with the time of writing. A record is a `- decision[...]`, `- estimate[...]` or `- lesson[...]` line inside a fenced block opened with the `LEDGER` tag; the same line anywhere else — bare, or in a block with another tag or none — is a preview and is never written. A `create` line carries the ratified tags: `{tags:a,b}`. A `knowledge` lesson line carries `{source:...}`, the url or reference the lesson studied — a file of the harness, a probe, a client version; the schema requires it, and a line without it is `incomplete: [source]` in the yaml and a lint finding on the page. An `error` lesson never carries one. Write the `- decision[...]` lines only in the reply that acknowledges ratification; `- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson exists, an `estimate[...]` line opening with the date of the reading and the command or the place it was read (case 199). Without `/hi` the hook refuses and says so: tell the person, do not retry. A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call waits for the next `Stop` of the session, and the last reply of a session has none. A block a tool call did follow is not lost until that `Stop` has passed: check the ledger then, and only a line missing there is a lesson.

        ## The acknowledging reply

        The reply that acknowledges a ratification has four parts, in this order: the `LEDGER` block first; a heading `## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when there are none; a heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last. Headings and labels in the language of the chat (case 167, supersedes 157).

        ## Slug collisions

        Pre-spec checks the slug when the Case is formed. If it is nonetheless taken by generation time — a second decision in the same session claimed it, or a page was created by hand — **the generation script errors rather than renaming.**

        Silently producing `entity-cart-2` would put a name in the vault that nobody ratified, and break the correspondence between a decision and its page. The librarian runs the script, so the librarian sees the error and judges what to do.

        ## The harness

        The harness — hooks, skills, agents, `settings.json`, `CLAUDE.md`, this file — is rendered from `rules/`. A harness file changes through an `update` of its Rule page, never by hand; a hook refuses the edit.

        ## Not schema-governed

        `brief.md`, `sprint.md`, `tags.md` and `log.md` are not pages and have no schema. Lint must not check them against the page template.
        <!-- /rule-case-protocol -->
    change: the page renders vault/wiki/case-schema.md in full, the five paragraphs of the old CLAUDE.md Render folded into the schema, the duplicates gone; parent rule-plan-mode (case 273.1)
  - slug: rule-plan-mode
    set:
      children: ["[[rule-ask]]", "[[rule-prespec-hook]]", "[[rule-prespec]]", "[[rule-spec-capture]]", "[[rule-case-protocol]]"]
    change: rule-case-protocol joins the children, last (case 273.1)
  - slug: estimate-case-protocol-loaded
    set:
      status: pending
      method: one reading at the first /hi of a session, by hand, plus the preview cases of tests/test_ledger.py
    change: the Criterion replaced whole — the schema is the Render of rule-case-protocol, loaded by /hi, and holds the ledger, Frontier and acknowledging-reply paragraphs (case 273.1)
  - file: vault/wiki/glossary.md
    change: the rows Rule-class files and CLAUDE.md, index.md — case-schema.md is the Render of rule-case-protocol, loaded by /hi; CLAUDE.md the Render of rule-claude-md with rule-language and rule-agent-writing, importing the glossary (cases 272, 273)
  - file: vault/wiki/index.md
    change: the §1 line of case-schema.md and the §2 sentence — the Render of rule-case-protocol, loaded by /hi, not imported into CLAUDE.md (case 273.1)
```

```tasks
- [x] update `rule-case-protocol`: `governs: vault/wiki/case-schema.md`, `render_mode: full`, `parent: rule-plan-mode`; the Purpose; the Render — the schema with the folded paragraphs
- [x] update `rule-plan-mode`: `children` + `rule-case-protocol`
- [x] update `estimate-case-protocol-loaded`: the Criterion replaced whole — loaded by `/hi`, `method`, `pending`
- [x] `vault/wiki/glossary.md` by hand: the rows Rule-class files and `CLAUDE.md`, `index.md`
- [x] `vault/wiki/index.md` by hand: the §1 line of `case-schema.md`, the §2 sentence "imported into CLAUDE.md" → "loaded by /hi"
- [x] render `vault/wiki/case-schema.md` — the first write of the file by the renderer, a one-off migration: the diff against the hand-written file read before the commit
- [x] `tests/test_render.py`: a `full` page into a file outside `.claude/`
- [x] read `estimate-case-protocol-loaded`: the first turn after the `/hi` of the next session, by hand; `tests/test_ledger.py`
```

### Case 273.2 — `/hi` expands the schema

> **given:**
> The `/hi` SKILL is the Render of `rule-skill-hi` with its children in markers; `rule-internal-context` is the block of `@` lines Claude Code expands when the skill is invoked.
> **＋** `tests/test_render.py` fixes the text of the block.

> **when:**
> The person invokes `/hi`.

> **then:**
> The text of `sprint.md`, `brief.md` and `case-schema.md` is present in the first turn's context, in that order, without a read call.
> **－** The glossary is not in the list — it arrives through `CLAUDE.md`.

```then
update:
  - slug: rule-internal-context
    replace:
      - old: |-
          @vault/wiki/brief.md
          <!-- /rule-internal-context -->
        new: |-
          @vault/wiki/brief.md
          @vault/wiki/case-schema.md
          <!-- /rule-internal-context -->
      - old: |-
          The glossary, `case-schema.md` and the category schemas are not listed here: they arrive
          through `@import` in `CLAUDE.md`, and re-reading them would duplicate context that is
          already present.
        new: |-
          `case-schema.md` is listed since case 273: the Render of `rule-case-protocol`, it reaches
          a working session here and not through `CLAUDE.md`, so a session without `/hi` carries no
          Case text. The glossary and the category schemas are not listed: the glossary arrives
          through `@import` in `CLAUDE.md`, the schemas are read when a page of their category is
          written.
    change: case-schema.md joins the imports of /hi; the glossary stays with CLAUDE.md (case 273.2)
  - slug: estimate-internal-context-loaded
    set:
      status: pending
      purpose: The text of sprint.md, brief.md and case-schema.md is present in the first turn's context after /hi, without a read call
      method: one reading at the /hi of a session, by hand
    change: the recut to the shape of case 193 — purpose, method, the Criterion replaced whole; three texts expanded, case-schema.md the third (case 273.2)
```

```tasks
- [x] update `rule-internal-context`: `@vault/wiki/case-schema.md` in the Render; How it works — the glossary through `CLAUDE.md`, the schema here
- [x] update `estimate-internal-context-loaded`: the recut to the shape of case 193 — `method`, the Criterion replaced whole, `pending`
- [x] render `.claude/skills/hi/SKILL.md`
- [x] read `estimate-internal-context-loaded`: the `/hi` of the next session, by hand
```

### Case 273.3 — `CLAUDE.md` without the protocol

> **given:**
> The conditions of 272.1.

> **when:**
> The first `uv run guppi render` after `rule-claude-md` or any of its children changed, and a session start with `CLAUDE.md`.

> **then:**
> `CLAUDE.md` equals the Render of `rule-claude-md` with the text of each child — `rule-language`, `rule-agent-writing` — between its markers; the diff of that render holds only the text those pages gained since the file was last written; `guppi render --check` then exits 0.
> **＋** The first paragraph says the vault is the only memory (272.1); "What is loaded here" names one import, `glossary.md`, and says the Case schema arrives at `/hi`; `index.md` is not imported.
> **＋** Every session loads the same text, its `@` import expanded.
> **－** `CLAUDE.md` holds no `rule-case-protocol` marker, no import of `case-schema.md` and no line on the Case form; the `children` of `rule-claude-md` are `rule-language` and `rule-agent-writing`.

```then
update:
  - slug: rule-claude-md
    set:
      children: ["[[rule-language]]", "[[rule-agent-writing]]"]
    replace:
      - old: |-
          Now the file is the Render of this page, whole, with the Case protocol
          spliced from `rule-case-protocol`; a change to it is an `update` of one of the two. The Render imports [[glossary]] and [[case-schema]] and points at [[index]].
        new: |-
          Now the file is the Render of this page, whole, with `rule-language` and `rule-agent-writing` spliced into their markers; a change to it is an `update` of one of the three. The Render imports [[glossary]] and points at [[index]]; the Case schema is the Render of `rule-case-protocol`, loaded by `/hi` (cases 272, 273.3).
      - old: |-
          The glossary and the Case schema arrive through the imports below, so the terms and the shape
          of a Case are present from the first turn without a read.

          @vault/wiki/glossary.md

          @vault/wiki/case-schema.md
        new: |-
          The glossary arrives through the import below, so the terms are present from the first turn
          without a read. The shape of a Case — `vault/wiki/case-schema.md`, the Render of
          `rule-case-protocol` — arrives with `/hi`, which opens a working session; a session without
          `/hi` holds no Case.

          @vault/wiki/glossary.md
      - old: |-
          <!-- rule-case-protocol -->

          <!-- rule-language -->
        new: |-
          <!-- rule-language -->
      - old: |-
          Rendered in full into `CLAUDE.md`; each child — `rule-case-protocol`, `rule-language`, `rule-agent-writing` — splices into its marker line.
        new: |-
          Rendered in full into `CLAUDE.md`; each child — `rule-language`, `rule-agent-writing` — splices into its marker line.
      - old: |-
          `rule-case-protocol` has this page as its parent since case 66, `rule-language` and `rule-agent-writing` since case 272; the renderer splices each into its marker.
        new: |-
          `rule-language` and `rule-agent-writing` have this page as their parent since case 272; the renderer splices each into its marker. `rule-case-protocol` was a child from case 66 to case 273, when its Render became `case-schema.md` and its parent `rule-plan-mode`.
    change: the Case protocol leaves CLAUDE.md — no marker, no import of the schema; the glossary stays; children rule-language and rule-agent-writing (case 273.3)
  - slug: estimate-claude-md-rendered
    set: {status: pending}
    change: the Criterion replaced whole — the text of 272.1 plus no protocol in CLAUDE.md, one import (case 273.3)
```

```tasks
- [x] update `rule-claude-md`: the protocol marker and the schema import removed, the paragraph "What is loaded here", the Purpose, How it works; `children` set
- [x] update `estimate-claude-md-rendered`: the Criterion replaced whole — the text of 272.1 plus the absence of the protocol, `pending`
- [x] render `CLAUDE.md`
- [x] read `estimate-claude-md-rendered`: `render` and `--check` after the build; the next session start, by hand
```

## Case 274 — `reword`: the rename of a word without a page

> **context:**
> `rename` of 258.1 renames a page and replaces its slug as a whole word on every live page but History and Result, in one item. A word without a page — the name of a skill, a command — has no such path: 261 renamed `pre-task` to `pre-spec` on the pages it named, and the word stayed in the Purpose of `rule-index-check`, `rule-brief`, `rule-ask`, in the Backlog of `entity-sprint-migration`, in `index.md`, `entities/schema.md`, `estimates/schema.md`; no Estimate holds it in a Criterion — History, Result and the slug of an archived Insight only. To replace a word across the vault today is one `update` per page, or the whole Criterion, which `lesson-estimate-update-must-carry-its-criterion-whole` is about.
> State of the pages: `rule-page-generation` `built`, seven Estimates, none on `reword` — a new promise, a `create`; `rule-prespec` `built`, the owner of `/pre-spec`, its Estimates untouched; three Purposes and the Backlog change by the mechanism, the Rule-class files by hand.

> **problem:**
> How to rename a name that has no page in one decision, so that the script neither searches nor guesses, and the person sees and signs every replacement.

### Case 274.1 — `generate` applies `reword`

> **given:**
> An `update` item of a Rule page carries `reword` — a list of `{old, new}` pairs; the page is the owner: the `new` of every pair stands in its Purpose, Render, `governs` or `implementation_ref`, compared without regard to case.
> **＋** A whole word is the boundary of `rename` 258.1: `(?<![\w-])old(?![\w-])`; the slug of a page is renamed by `rename`, not by `reword`.
> **＋** `tests/test_generate.py` fixes the behaviour on a temp vault with three pages and an archive.

> **when:**
> `guppi generate` applies an `update` entry with `reword`.

> **then:**
> Every pair is replaced as a whole word on every live page of `wiki/rules/`, `wiki/entities/` and `wiki/estimates/`, in every section but History and Result and in the fields `purpose` and `method`; one History line per page touched — `reworded: old → new · [[decision-case-N]]`; stdout one line per page with the count.
> **＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
> **－** A pair with no hit on any live page, or with a `new` absent from the owner's text, fails the entry with the reason; nothing is applied.
> **－** `wiki/decisions/` (the journal, without History), `wiki/lessons/` and `wiki/insights/` (records of the past), the archive, `raw/`, the Rule-class files, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes (case 277).

```then
update:
  - slug: rule-page-generation
    replace:
      - old: |-
          a taken or foreign slug fails the entry (case 258.1).
        new: |-
          a taken or foreign slug fails the entry (case 258.1). An `update` whose item carries `reword` — a list of `{old, new}` pairs — replaces each pair as a whole word in every section but History and Result, and in `purpose` and `method`, of every live page of `wiki/`, one History line per page touched; the page is the owner, and a `new` absent from its own text, or a pair with no hit, fails the entry; a slug goes through `rename`, not `reword` (case 274.1).
    change: reword on an update item — pairs replaced as whole words across the live pages, the owner check, failed on no hit (case 274.1)
create:
  - slug: estimate-generate-rewords
    type: estimate
    ref: rule-page-generation
    kind: QA
    purpose: An update item with reword replaces its pairs as whole words on every live page but History and Result, one History line each, and fails on a pair with no hit or a new the owner does not carry
    method: pytest tests/test_generate.py on a temp vault with three pages and an archive; the live reading the librarian's run that applies the first reword
    tags: [harness, workflow, ledger]
```

```tasks
- [x] update `rule-page-generation`: the Purpose sentence on `reword`
- [x] create `estimate-generate-rewords`, `ref: rule-page-generation`
- [x] `guppi/generate.py`: `reword` on an `update` entry — the owner check without regard to case, the walk of the live pages of `rules/`, `entities/` and `estimates/` by the `reword` of 258.1 with a pair in place of a slug, the History line, the stdout line, `failed` on no hit, `reword` alone counted as content; the docstring
- [x] `tests/test_generate.py`: a pair changes three pages and writes History; History and Result untouched; a decision page, a lesson and an insight untouched; a pair with no hit — `failed`; a `new` the owner lacks — `failed`; the archive untouched
- [ ] read `estimate-generate-rewords`: pytest now; live — the first `reword` applied, in a later session (case 277.4)
```

### Case 274.2 — the first use: `pre-task` → `pre-spec`

Superseded by 277.4 at pre-spec: the word means the vault query before a `create` in most of its places, not the check of the set; the sweep goes by `replace` per page. The tasks below are void.

> **given:**
> The conditions of the parent.
> **＋** The grep of the live `wiki/` gives the variants: `pre-task` (the Purpose of `rule-brief` and `rule-ask`, the Backlog of `entity-sprint-migration`, `index.md` four times, `entities/schema.md` twice, `estimates/schema.md` once), `Pre-task` (the Purpose of `rule-index-check`); `pretask` only in History, Result and the slug `insight-pretask-…`.

> **when:**
> The librarian's run applies the item of `rule-prespec` with `reword`, and the person reads `index.md` and the schemas.

> **then:**
> `pre-task` and `Pre-task` stand on no live page and in no Rule-class file outside History and Result; `pre-spec` and `Pre-spec` in their place.
> **－** History, Result, `log.md` and the slugs of archived pages stay as they are.

```then
update:
  - slug: rule-prespec
    reword:
      - {old: pre-task, new: pre-spec}
      - {old: Pre-task, new: Pre-spec}
    change: the word pre-task renamed to pre-spec on every live page by reword (case 274.2)
  - file: vault/wiki/index.md
    change: pre-task → pre-spec in the four places — the slug prefix guard twice, the deferred placeholder, the ask-guppi moments (case 274.2)
  - file: vault/wiki/entities/schema.md
    change: pre-task → pre-spec in the tags row and the slug paragraph (case 274.2)
  - file: vault/wiki/estimates/schema.md
    change: pre-task → pre-spec in the tags row (case 274.2)
```

```tasks
- [ ] update `rule-prespec`: `reword` — `pre-task → pre-spec`, `Pre-task → Pre-spec`
- [ ] `vault/wiki/index.md` by hand: four places
- [ ] `vault/wiki/entities/schema.md`, `vault/wiki/estimates/schema.md` by hand: three places
- [x] `guppi sprint` → `sprint.md`
- [ ] `grep -rn "pre-task" vault/wiki` after the run: History, Result and `log.md` only
```

### Case 274.3 — `materialize` carries `reword`

> **given:**
> A unit `raw/<date>/<HHMM>/` holds `ledger.md` and `spec.md`; a Case in the Spec has a heading, the sections `given`, `when`, `then` and a `then` block.
> **＋** `guppi generate` applies the `sections` of an `update` entry as whole replacements, `replace` and `reword` as pairs, and writes every field of a `create` entry's `fields` into the frontmatter.
> **＋** The `schema.yaml` of each category lists the fields of its page: `required` and `optional` (case 214).
> **＋** The tests in `tests/test_materialize.py` fix the behaviour; the live reading is the librarian's run.

> **when:**
> `guppi materialize` lifts a record line of a ledger against its Spec.

> **then:**
> One entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `origin`, `line`, `text`, `decision`; from the `then` block — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented (case 258.3).
> **＋** `reword` is a list of `{old, new}` pairs, carried as written; a mapping or a scalar under `reword` is `incomplete: [reword]` (case 274.3).
> **＋** Only the keys the category's `schema.yaml` names as fields reach `fields` of a `create` entry, and of a `defer` entry but for `type` and `purpose` — the defer's own keys, which reach `fields` whatever the target's category, for the placeholder page and for the `## Deferred` of the Decision page; the structural keys of the item go where they go — `ref` to the entry, `sections`, `tags`, `file`; a key that is neither is marked `unknown: [key]` on the entry, printed by `--show`, never written to the page, and the entry applies; `incomplete` is counted by `REQUIRED` as before, and a `defer` without `purpose` is `incomplete: [purpose]` (cases 214.1, 266).
> **＋** An Estimate has its own line and its own entry; the `ref` of the line is the Estimate itself.
> **＋** An `update` entry for an Estimate carries `sections.Criterion` — the text the item wrote under `sections: Criterion` itself, else the `given`, `when` and `then` of its Case verbatim with their operands as `Given:`, `When:`, `Then:` — replacing what stood there, and `set: {status: pending}` unless the item set a status itself; the `given` of a sub-case is its parent's when it has none of its own.
> **＋** A `create` entry for an Estimate keeps `kind`, `purpose`, `method`, `tags` as fields; its Criterion the same way: the written text when there is one, else the Case's; `## Context` and `## Method` are not written.
> **＋** One decision entry per Case: `decision`, `case_text`, `targets`; a sub-case inherits `context`, `problem`, `recommend`, `given`, never `when`.
> **＋** An `estimate` line for a page of the same ledger is folded into its `create`; for an earlier page it is an `estimate` entry. The `new_tags` of any Case reach the yaml once. An existing yaml is extended, never rewritten.
> **－** An `update` entry carries no `contract`, and no Estimate is derived from it; a `create` carries no `method`, `estimate_kind` or `estimate_slug`; neither `criterion_block`, `case_removed` nor `remove_criterion` is derived.
> **－** The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule's item are ignored: they reach neither the page, nor `incomplete`, nor `unknown`.
> **－** A line the grammar does not parse goes under `unparsed`; the run goes on.

```then
update:
  - slug: rule-materialize
    replace:
      - old: |-
          touches two promises (case 204). A unit
        new: |-
          touches two promises (case 204). An `update` item's `reword` — a list of `{old, new}` pairs — is carried to the entry as written, for `generate` to apply; a mapping or a scalar under it is `incomplete: [reword]` (case 274.3). A unit
    change: reword carried from the then block to the entry as a list of pairs (case 274.3)
  - slug: estimate-materialize-assembles
    set: {status: pending}
    change: the Criterion replaced whole — reword among the keys carried from the then block, a list of pairs or incomplete (case 274.3)
```

```tasks
- [x] update `rule-materialize`: the Purpose sentence on `reword`
- [x] update `estimate-materialize-assembles`: the Criterion replaced whole — `reword` in the key line and its form, `pending`
- [x] `guppi/materialize.py`: `reword` among the structural keys of an item, `incomplete: [reword]` on a shape other than a list; the docstring
- [x] `tests/test_materialize.py`: `reword` reaches the entry; a mapping in place of the list — `incomplete`
- [x] read `estimate-materialize-assembles`: pytest; live — the librarian's run of this session
```

## Case 275 — the bare `[[decision-case-N]]` in a lesson's Trigger

> **context:**
> The lesson `lesson-spec-change-text-quotes-a-wikilink-bare` was born from a ledger line of session 0958; its Trigger quotes the `change` of Case 262 — "the two placeholders `[[decision-case-N]]` of the Criterion in code spans" — in quotes, the placeholder bare, without a code span. The page took the text as it was, lint reads the body of a lesson like any other and raises `ref: body names decision-case-N, which no live or archived page carries` — the class the lesson is about, the fifth time. The librarian does not repair it: a lesson page changes by an `update` only.
> State of the pages: the lesson `new`, tags `workflow, harness, librarian`; no Estimate touched — a lesson has none; `rule-lint` untouched — the finding is right.

> **problem:**
> The lesson on bare placeholders carries a bare placeholder itself and stands as a lint finding. Repair the page, or keep the finding.

> **given:**
> Lint reads the body of a lesson; a `[[slug]]` outside a code span is a `ref` that no live or archived page carries.
> **＋** `pre-spec` reads the strings of the `then` blocks and does not read a `[[slug]]` inside backticks (264.2).

> **when:**
> The librarian's run applies the `update`, and `make lint` runs after it.

> **then:**
> The Trigger of the lesson is the same text with `[[decision-case-N]]` in a code span; `make lint` raises no `ref` on this lesson.
> **－** `root_cause`, `kind`, `status`, the tags and the History of the lesson do not change; no other page is touched.

```then
update:
  - slug: lesson-spec-change-text-quotes-a-wikilink-bare
    sections:
      Trigger: |
        the `change` of Case 262 on `estimate-generate-renames` — "the two placeholders `[[decision-case-N]]` of the Criterion in code spans" — went into the page's History as written, and lint raised the same `ref: body names decision-case-N` the Case had just cured in the Criterion; the fourth time on this class (130.1, 140, 160)
    change: the placeholder of the Trigger in a code span — the lesson no longer carries the bare link it is about (case 275)
```

```tasks
- [x] update `lesson-spec-change-text-quotes-a-wikilink-bare`: `sections: Trigger` — the placeholder in a code span
- [x] `make lint` after the librarian's run: no `ref` finding on the lesson
```

## Case 277 — the findings of pre-spec

> **context:**
> The check of the set against the vault found four kinds of gap. Pages that say the schema is imported into `CLAUDE.md` or that the ledger instruction lives in `CLAUDE.md`, beyond the ones already named: the Purpose of `rule-ledger-write`, two Estimates of `rule-case-protocol` (`case-form`, `ledger-line-form`), `rules/schema.md` — which also says `render` applies to harness rules only, while 273.1 renders a file of the vault. The librarian's ban on the Spec without the exception of 271 stands in the `purpose` of `rule-materialize` and in `index.md` §10. And 274.2: the word `pre-task` in the live texts means, in most places, not the check of the set (`/pre-spec`) but the vault query before a `create` — the glossary still calls that moment "Pre-task"; a `reword` pair `pre-task → pre-spec` would give `rule-ask` "at pre-spec and at pre-spec" and a false meaning in `index.md`, `rule-index-check`, `rule-brief`. And the `reword` of 274.1 as written walks every live page — the Decision pages (the journal, without History), the lessons and Insights (records of the past) — which the Case did not say.
> State of the pages: `rule-materialize`, `rule-ledger-write` `built` — the Purpose changes, no Estimate touched; `estimate-case-protocol-case-form`, `estimate-case-protocol-ledger-line-form` `passed` — the Criterion replaced; 274.2 replaced whole (`supersedes`), 274.1 kept with its scope made explicit; the Rule-class files `index.md`, `glossary.md`, `rules/schema.md`, `entities/schema.md`, `estimates/schema.md` by hand.

> **problem:**
> The set of six Cases contradicts seven pages and one Rule-class file, and the first use of `reword` would have changed the meaning of the word in five places. What is repaired in this Spec, and how.

### Case 277.1 — `rule-materialize`: the ban and the keys

> **given:**
> 271: the librarian reads the unticked `- [ ]` lines of the Specs; 274.3: `reword` is a key of an item.

> **when:**
> Someone reads `rule-materialize` or its index line.

> **then:**
> `purpose` and the Purpose say: the librarian does not read the ledger, nor the Spec beyond its unticked lines; the list of the item's keys is `set`, `sections`, `replace`, `reword`, `change`, `rename`.
> **－** The Estimates of the rule do not change.

```then
update:
  - slug: rule-materialize
    set:
      purpose: Prevents the librarian from reading the ledger and the Spec beyond its unticked lines, or from routing a decision by guesswork
    replace:
      - old: |-
          Prevents the librarian from reading the ledger and the Spec itself, or from routing
        new: |-
          Prevents the librarian from reading the ledger and the Spec beyond its unticked lines (case 271), or from routing
      - old: |-
          `set`, `sections`, `replace`, `change`, and `rename` when the item carries it (case 258.2).
        new: |-
          `set`, `sections`, `replace`, `change`, and `rename` or `reword` when the item carries it (cases 258.2, 274.3).
    change: the ban on the Spec excepts its unticked lines; reword in the list of the item's keys (case 277.1)
```

```tasks
- [x] update `rule-materialize`: `set.purpose`; `replace` of the Spec sentence and of the key list
```

### Case 277.2 — `rule-ledger-write`: where the instruction lives

> **given:**
> 273: the instruction to write ledger lines is in `case-schema.md`, loaded by `/hi`; without `/hi` the hook refuses.

> **when:**
> Someone reads the Purpose of `rule-ledger-write`.

> **then:**
> The Purpose says: the instruction lives in the Case schema, which `/hi` loads; a session without `/hi` writes no line, and the hook would not take one.
> **－** The Render and the Estimates of the rule do not change.

```then
update:
  - slug: rule-ledger-write
    replace:
      - old: |-
          `- lesson[...]` lines lives in `CLAUDE.md`, so the agent produces them in *any* session —
          including one with no sprint, no branch context and no brief. Without this hook's check the
        new: |-
          `- lesson[...]` lines lives in `case-schema.md`, the Render of `rule-case-protocol` that `/hi` loads (case 273), so a session without `/hi` produces none — and would produce them in *any* session
          if the instruction stood in `CLAUDE.md` again, including one with no sprint, no branch context and no brief. Without this hook's check the
    change: the ledger instruction lives in the Case schema loaded by /hi, not in CLAUDE.md (case 277.2)
```

```tasks
- [x] update `rule-ledger-write`: `replace` of the sentence on `CLAUDE.md`
```

### Case 277.3 — the Rule-class files: the carrier, the ban, the names

> **given:**
> A Rule-class file is an `update` with `file` and `change`, by hand in Work Mode.
> **＋** `pre-task` in §3 of `index.md`, in `rule-index-check`, `rule-brief` and the glossary means the vault query before a `create`; in the schemas the check of the slug for collisions, which is pre-spec.

> **when:**
> Someone reads `index.md`, `glossary.md`, `rules/schema.md`, `entities/schema.md` or `estimates/schema.md`.

> **then:**
> `index.md`: §10 — the librarian does not read `spec.md` beyond its unticked lines; §5 — the Rule-class map without `case-schema`; §3 lines 159, 403, 415 — "the vault query before a `create`" in place of `pre-task`.
> **＋** `glossary.md`: row 70 — "Plan Mode, the vault query, `/pre-spec`"; rows 86, 88 as 273.1 says.
> **＋** `rules/schema.md`: `render` may govern a Rule-class file of the vault — `case-schema.md` through `rule-case-protocol`; the example of `rule-internal-context` without "through `CLAUDE.md`".
> **＋** `entities/schema.md`, `estimates/schema.md`: "chosen at the vault query before the Case", "checked by pre-spec for collisions".
> **－** The word `pre-task` stays in no Rule-class file.

```then
update:
  - file: vault/wiki/index.md
    change: §10 the librarian's Reads except the unticked lines of spec.md (case 271); §5 line 242 the Rule-class map without case-schema (case 273.1); §3 lines 159, 403, 415 pre-task → the vault query before a create (case 277.3)
  - file: vault/wiki/glossary.md
    change: row 70 Plan Mode, the vault query, /pre-spec — pre-task is no name any more (case 277.3)
  - file: vault/wiki/rules/schema.md
    change: lines 19 and 64 — render may govern a Rule-class file of the vault, case-schema.md through rule-case-protocol (case 273.1); line 157 the example without "through @import in CLAUDE.md" (case 273.2)
  - file: vault/wiki/entities/schema.md
    change: the tags row "chosen at the vault query before the Case"; the slug paragraph "checked by pre-spec for collisions" (case 277.3)
  - file: vault/wiki/estimates/schema.md
    change: the tags row "chosen at the vault query before the Case" (case 277.3)
  - file: vault/wiki/decisions/schema.md
    change: the example Context "Pre-task found no cart page" → "The vault query before the Case found no cart page" — found in Work Mode by the grep the Case asks for (case 277.3)
```

```tasks
- [x] `vault/wiki/index.md` by hand: §10, §5 line 242, §3 lines 159, 403, 415 — with the places of 273.1
- [x] `vault/wiki/glossary.md` by hand: row 70 — with rows 86, 88 of 273.1
- [x] `vault/wiki/rules/schema.md` by hand: lines 19, 64, 157
- [x] `vault/wiki/entities/schema.md`, `vault/wiki/estimates/schema.md` by hand: three places
- [x] `vault/wiki/decisions/schema.md` by hand: the example Context, found by the grep
- [x] `grep -rn "pre-task" vault/wiki/*.md vault/wiki/*/schema.md` after: nothing
```

### Case 277.4 — the sweep of `pre-task` by meaning, in place of 274.2

> **given:**
> `rename` of 258.1 and `reword` of 274.1 change a word, not a meaning; here the meaning differs by place.
> **＋** The live pages with the word: `rule-ask`, `rule-index-check`, `rule-brief` (Purpose), `entity-sprint-migration` (Backlog, Closed); the Decision pages, lessons and Insights are records and are not touched.

> **when:**
> The librarian's run applies the `replace` of each page, and `guppi sprint` redraws `sprint.md`.

> **then:**
> `rule-ask`: "at the vault query before a `create` and at pre-spec"; `rule-index-check`: "The vault query before the Case asked …"; `rule-brief`: "the vault query before a `create` finds it there"; `entity-sprint-migration`: the Backlog line "the vault-query questions before a product's records", the Closed line "pre-spec (then `/pre-task`)" stands as history — unchanged.
> **－** History, Result, the Decision pages, lessons, Insights and `log.md` stay as they are; `rule-prespec` is not touched; no `reword` is applied in this Spec — its live reading waits for the first rename.

```then
update:
  - slug: rule-ask
    replace:
      - old: |-
          the agent at
          pre-task and at pre-spec, the librarian, the person
        new: |-
          the agent at
          the vault query before a `create` and at pre-spec, the librarian, the person
    change: pre-task → the vault query before a create, the first of the two moments (case 277.4, supersedes 274.2)
  - slug: rule-index-check
    replace:
      - old: |-
          Pre-task asked the vault
          before the Case;
        new: |-
          The vault query before the Case asked
          once;
    change: Pre-task → the vault query before the Case (case 277.4)
  - slug: rule-brief
    replace:
      - old: |-
          and pre-task finds it there.
        new: |-
          and the vault query before a `create` finds it there.
    change: pre-task → the vault query before a create (case 277.4)
  - slug: entity-sprint-migration
    replace:
      - old: |-
          the pre-task questions before a product's records (session 1119)
        new: |-
          the vault-query questions before a product's records (session 1119)
    change: the Backlog line — pre-task → the vault query (case 277.4)
```

```tasks
- [x] update `rule-ask`, `rule-index-check`, `rule-brief`: `replace` in the Purpose
- [x] update `entity-sprint-migration`: `replace` of the Backlog line
- [x] `guppi sprint` → `sprint.md`
- [x] `grep -rn "pre-task" vault/wiki/rules vault/wiki/entities vault/wiki/estimates` after: History and Result only
```

### Case 277.5 — `estimate-case-protocol-case-form`: the carrier

> **given:**
> `index.md`, `estimates/schema.md` and `schema.yaml` are Rule-class files: an `update` with `file` and `change`, applied by hand in Work Mode; `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi` (case 273).
> **＋** An `update` of the Render of `rule-case-protocol` touches the Estimate of the live reading of that Render (187).
> **＋** The reading of `estimate-case-protocol-case-form` is the Cases of this session at its close, by hand.

> **when:**
> The agent writes a Case in the chat — at its first showing, when shown again after the owner's change, and with sub-cases.

> **then:**
> `given` holds the conditions of the behaviour; the state of the pages the Case changes goes to `context`.
> **＋** `context` opens with the mechanism in plain words — what the thing does today and where it goes wrong — and closes with one sentence of bookkeeping: the state of the pages, the vault's answer, the Estimates of the rule the Case touches and the ones it does not; a case number stands in `context` or `problem` only when the Case is about that case; no count of sentences — the shape of each story section bounds it (case 267).
> **＋** `given`, `when` and `then` together are the Criterion of the Estimate, copied whole and replacing what stood there.
> **＋** An item that writes `sections: Criterion` itself signs that text, on a `create` and on an `update` alike; the Case's `given`, `when`, `then` are the Criterion of the one Estimate that writes none; that is how one Case touches two Estimates.
> **＋** The Case names by slug the Estimate it changes.
> **＋** `tasks` carries no `contract` line and no "block N" line.
> **－** A `create` carries no `method`, `estimate_kind` or `estimate_slug`: a new promise is an explicit `create` of an Estimate with its own slug.
> **－** The eight sections of the chat form do not change.

```then
update:
  - slug: estimate-case-protocol-case-form
    set: {status: pending}
    change: the Criterion replaced whole — case-schema.md the Render of rule-case-protocol loaded by /hi, not a Rule-class file by hand; CLAUDE.md no longer the carrier (case 277.5)
```

```tasks
- [x] update `estimate-case-protocol-case-form`: the Criterion replaced whole, `pending`
- [x] read `estimate-case-protocol-case-form`: the Cases of this session at its close, by hand
```

### Case 277.6 — `estimate-case-protocol-ledger-line-form`: two documents

> **given:**
> The table of the lines and the paragraph of the ledger mechanics are in `case-schema.md` (273.1); §4 of `index.md` is the second copy of the line's form.

> **when:**
> `/hi` loads the schema; someone reads `case-schema.md` or `index.md` §4; the main agent writes a `- lesson[knowledge][...]` line.

> **then:**
> The table of `case-schema.md` and §4 of the map show `- decision[case 12][update][rule-x]{ref:rule-x}` and `- decision[case 12][create][rule-y]{ref:rule-x}{tags:a,b}` and say: the id is `case N` with the word and a space, in `{supersedes:case N}` too.
> **＋** The ledger paragraph of the schema carries the sentence on `{source:...}` on a `knowledge` lesson line, `incomplete: [source]` without it, an `error` lesson never carrying one.
> **－** The estimate and lesson rows of the table do not change; `rule-ledger-write` does not change — the hook writes verbatim and checks nothing.

```then
update:
  - slug: estimate-case-protocol-ledger-line-form
    set:
      status: pending
      method: one reading by hand of `case-schema.md` and `index.md` §4 after the render, at a session start
    change: the Criterion replaced whole — the table and the ledger paragraph are one document since 273.1, two documents read, not three (case 277.6)
```

```tasks
- [x] update `estimate-case-protocol-ledger-line-form`: the Criterion replaced whole, `method` — two documents, `pending`
- [x] read `estimate-case-protocol-ledger-line-form`: `case-schema.md` and `index.md` §4 after the render, by hand
```

## Deferred

## Case 276 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b is the current milestone of the sprint: `rule-work-mode` — Work Mode, the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`; `rule-subagent-guppi` — what a subagent may do and the fork that comes back as a Case. Both are `draft` placeholders, deferred eleven times, the last by 269. This session took the tick on a reading (270), the librarian's ban on the Spec (271), `CLAUDE.md` as rules (272), the schema as a Render loaded by `/hi` (273), `reword` (274) and a lesson's Trigger (275) ahead of it.

> **problem:**
> The person closes this Plan Mode with six Cases and goes to pre-spec; Slice 3b waits for the next session, the twelfth defer. One line of 270.2 bears on it: Work Mode ticks code, tests, migrations and `by hand` checks, the readings are `generate`'s — the rule is written with that.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes on code, tests, migrations and by-hand checks in spec.md (the readings are generate's since case 270), the test of each Estimate written first and turned green, the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes; the first item of the next session
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; with rule-work-mode, the first item of the next session
```
