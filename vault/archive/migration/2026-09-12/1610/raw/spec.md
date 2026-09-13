<!-- approved 21:48:20 · session 91c83351 -->

# Spec — 2026-09-12, session K

## Case 85 — `.claude/settings.json` as a MOC and its children

> **context:**
> The Frontier, the Spec and the handoff are the session's own working files under
> `raw/<date>/<HHMM>/`, and the agent writes them many times in one session. Every write
> asks the person for permission. The entries that would stop the question belong in
> `permissions.allow`. But `.claude/settings.json` has one page for the whole file today —
> `rule-hook-registry`, `render_mode: full` — and its Purpose says `defaultMode: plan`
> lives there too, "one file has one source". Permissions, the mode and the hook registry
> are three rules in one file.

> **problem:**
> How to describe `settings.json` so that permissions have their own rule, the mode has
> its own and the hooks have their own, while the file keeps one source.

> **given:**
> The vault, asked through `ask-guppi`: no live or `draft` page is about permission
> settings; the only live text is the `permissions` block inside the Render of
> `rule-hook-registry` (`built`, `full`, `governs: .claude/settings.json`, Estimate
> `estimate-hook-registry-rendered`, `passed`). The slugs `rule-settings`,
> `rule-permissions`, `rule-default-mode`, `estimate-settings`, `estimate-permissions` and
> `estimate-default-mode` are free; `rule-plan-mode` is taken by the phase of the session.
> **＋** `render_full` replaces a `<!-- child -->` line with the child's text wrapped in its
> own markers (`guppi/render.py`, `block()`); a marker line must match `^<!-- name -->$`
> exactly. `render.plan` already refuses two `full` pages on one file and already requires
> a `partial` child to be listed in the owner's `children`.
> **＋** JSON holds no comment, so a child spliced with its markers makes the file
> unparsable. This is the one thing the `rule-claude-md` pattern does not lend to a JSON
> file.
> **＋** A marker must be a whole line, so the comma between two JSON keys belongs to the
> text of the child that precedes the other.
> **＋** `guppi guard` and `guppi lint` read no marker; `pages.py` reads the markers of a
> page, not of a file.
> **＋** `rule-harness` is a MOC whose `children` hold `rule-hook-registry`; the new MOC
> takes that slot.
> **＋** The criterion of `estimate-hook-registry-rendered` is the whole file today: the
> Render reproduced byte for byte, the file parses as JSON, the next session start writes
> its `session-start` line.
> **－** Whether Claude Code reads `settings.json` during a session or only at its start is
> written nowhere in the vault. If only at the start, the questions stop at the next `/hi`.

### Case 85.1 — a render into a file that holds no comment

> **when:**
> `guppi render` writes a file that cannot hold a comment — today `.claude/settings.json`.

> **then:**
> The text of each child replaces its `<!-- child -->` line without the two marker lines.
> **＋** In every other file the splice keeps the markers.
> **－** A `partial` page whose file has no `full` owner still needs its markers in the
> file; a file that holds no comment can have no such page.

```then
update:
  - slug: rule-render-harness
    contract: changed
    estimate_slug: estimate-render-harness-reproduces
    sections:
      How it works: |
        `uv run guppi render` writes every governed file from its Rule page; `--check`
        renders in memory and names the files that differ, for `make lint`; `--sync`, the
        `SessionStart` hook, prints a unified diff for each differing file — the file as it
        is, then the rendered text — and writes it, so the agent's first turn shows what
        the render changed: the pages the librarian updated, or a hand edit that is now
        gone and may deserve a Case. It exits 0 always; `SessionStart` cannot block, and a
        render error goes to stderr. The rendered files are committed at Retro.

        A child of a `full` page lands between its own markers, which stay in the file and
        say who owns the text. A file that cannot hold a comment takes the child's text
        bare: the markers would make it unparsable. The owner is then named by the
        `<!-- child -->` line of the parent's body, and `render --check` compares the whole
        file, so nothing is lost but the label in the file itself (case 85.1).
    change: "a child spliced into a file that cannot hold a comment lands without its markers (case 85.1)"
```

```tasks
- [x] guppi/render.py: in `render_full`, a child of a page governing a file that holds no comment is spliced bare
- [x] tests/test_render.py: a full page with one child over a `.json` file — the output holds the child's text, no marker line, and parses as JSON
- [ ] take the reading of estimate-render-harness-reproduces; write the estimate line
```

### Case 85.2 — `rule-settings`, the MOC over the file

> **when:**
> `guppi render` runs, or someone reads `.claude/settings.json`.

> **then:**
> `rule-settings` is a MOC, `enforcement: render`, `render_mode: full`,
> `governs: .claude/settings.json`; its body is the whole file, with one `<!-- child -->`
> line where a child owns the text.
> **＋** Its `children` are `rule-default-mode`, `rule-permissions`, `rule-hook-registry`,
> and that order is the order of the keys in the file.
> **＋** Its Estimate reads the rendered file: it parses as JSON, `render --check` exits 0,
> and the next session start writes its `session-start` line into the event log.
> **－** The MOC holds no rule of its own about what a hook or a permission may be.

```then
create:
  - slug: rule-settings
    type: rule
    kind: MOC
    purpose: Keeps the three rules that share .claude/settings.json from becoming two copies of one file
    tags: [harness, render]
    enforcement: render
    governs: .claude/settings.json
    render_mode: full
    children: [rule-default-mode, rule-permissions, rule-hook-registry]
    sections:
      Purpose: |
        Keeps the three rules that share `.claude/settings.json` from becoming two copies
        of one file. The permission mode a session opens in, what may be written without a
        question, and which hook fires on which event are three different rules with three
        different criteria, and one file carries all three. This page is the file: its body
        is the whole of `settings.json`, and each `<!-- child -->` line names the page that
        owns that text.

        `parent: rule-harness`: the file belongs to no phase of the session.
      Render: |
        <!-- rule-settings -->
        {
          "permissions": {
        <!-- rule-default-mode -->
        <!-- rule-permissions -->
          },
          "hooks": {
        <!-- rule-hook-registry -->
          }
        }
        <!-- /rule-settings -->
    method: uv run guppi render, then json.load on .claude/settings.json and guppi render --check; the live half at the next session start — the session-start line in raw/<date>/event_log.md came from the rendered file
update:
  - slug: rule-harness
    set: {children: [rule-render-harness, rule-settings, rule-lint, rule-index, rule-governed-files-hook, rule-claude-md]}
    change: "rule-settings takes the slot of rule-hook-registry, which becomes its child (case 85.2)"
```

```tasks
- [ ] rule-settings and the rule-harness update land at the librarian's run; after generate, check `children` is [rule-default-mode, rule-permissions, rule-hook-registry] with no duplicate
- [ ] uv run guppi render: .claude/settings.json is rebuilt from the four pages, json.load parses it, render --check exits 0
- [ ] take the reading of estimate-settings; write the estimate line
```

### Case 85.3 — `rule-hook-registry` becomes a child

> **when:**
> `guppi render` runs.

> **then:**
> `rule-hook-registry` renders the four event keys only, as a `partial` child of
> `rule-settings`.
> **＋** Its Purpose keeps the hooks and drops `defaultMode`, which is now
> `rule-default-mode`.
> **－** The whole-file clauses — the file parses, the next start still logs — belong to
> `estimate-settings` from now on; this page answers for the hook registrations.

```then
update:
  - slug: rule-hook-registry
    contract: changed
    set: {render_mode: partial, parent: rule-settings}
    sections:
      Purpose: |
        Prevents a hook from being registered by hand, outside a ratified decision. A hook
        Rule names `.claude/settings.json` in `implementation_ref`, but nothing ties the
        file to the pages: a registration added or dropped by hand changes what fires with
        no ledger line behind it. This page is the `"hooks"` key of that file; adding a
        hook is an `update` of this page in the same Case that creates the hook's Rule.

        `parent: rule-settings`: the file is one text of three rules, and the registry is
        one of them (case 85.3). A hook in an agent's own frontmatter is part of that
        agent's Render and is ratified with it; this page holds the registrations only.
      Render: |
        <!-- rule-hook-registry -->
            "SessionStart": [
              { "hooks": [ { "type": "command", "command": "uv run guppi event session-start", "timeout": 30 },
                           { "type": "command", "command": "uv run guppi render --sync", "timeout": 60 } ] }
            ],
            "PreToolUse": [
              { "matcher": "ExitPlanMode",
                "hooks": [ { "type": "command", "command": "uv run guppi pretask", "timeout": 30 } ] },
              { "matcher": "Skill",
                "hooks": [ { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] },
              { "matcher": "Edit|Write|MultiEdit",
                "hooks": [ { "type": "command", "command": "uv run guppi guard", "timeout": 30 } ] }
            ],
            "PostToolUse": [
              { "hooks": [ { "type": "command", "command": "uv run guppi event tool", "timeout": 30 } ] },
              { "matcher": "ExitPlanMode",
                "hooks": [ { "type": "command", "command": "uv run guppi spec", "timeout": 30 } ] }
            ],
            "Stop": [
              { "hooks": [ { "type": "command", "command": "uv run guppi ledger", "timeout": 30 } ] }
            ]
        <!-- /rule-hook-registry -->
    change: "the page renders the hooks key only, as a partial child of rule-settings (case 85.3)"
```

```tasks
- [ ] take the reading of estimate-hook-registry-rendered, pending after the contract change; write the estimate line
```

### Case 85.4 — `rule-default-mode`

> **when:**
> A session starts.

> **then:**
> `.claude/settings.json` carries `"defaultMode": "plan"` from `rule-default-mode`, a Leaf
> child of `rule-settings`, and the session opens in Plan Mode.
> **＋** The page says why: nothing is written before a Case is ratified.
> **－** The page holds no other permission field.

```then
create:
  - slug: rule-default-mode
    type: rule
    kind: Leaf
    purpose: Keeps a session from writing anything before a Case is ratified
    tags: [harness, session]
    enforcement: render
    governs: .claude/settings.json
    render_mode: partial
    sections:
      Purpose: |
        Keeps a session from writing anything before a Case is ratified. Plan Mode is the
        form of the whole model: the agent reads, forms Cases and waits for a sign-off, and
        the harness enforces it rather than the agent's memory. `defaultMode` is one key,
        but it decides what a session may do from its first turn, so it is a rule of its
        own and not a line of the registry (case 85.4).
      Render: |
        <!-- rule-default-mode -->
            "defaultMode": "plan",
        <!-- /rule-default-mode -->
    method: the rendered .claude/settings.json holds permissions.defaultMode as "plan" and parses; the live half at the next session start — the session opens in Plan Mode and an edit outside the plan file is not made without a sign-off
```

```tasks
- [ ] take the reading of estimate-default-mode at the next session start; write the estimate line
```

### Case 85.5 — `rule-permissions`

> **when:**
> The agent writes or edits `frontier.md`, `spec.md` or `handoff.md` under
> `vault/raw/<date>/<HHMM>/`, in Plan Mode or in Work Mode.

> **then:**
> The write happens with no question to the person, allowed by the six entries of the
> Render of `rule-permissions`: `Edit` and `Write` for the three names.
> **＋** Nothing else is allowed: `ledger.md`, `event_log.md`, `materialize.yaml` and every
> file a Rule page governs stay outside the list.
> **－** `deny` and `ask` stay empty.
> **－** If Claude Code reads `settings.json` only at a session start, the effect begins at
> the next start; the reading records which it was.

```then
create:
  - slug: rule-permissions
    type: rule
    kind: Leaf
    purpose: Lets the session write its own working files without asking, and nothing else
    tags: [harness, session]
    enforcement: render
    governs: .claude/settings.json
    render_mode: partial
    sections:
      Purpose: |
        Lets the session write its own working files without asking, and nothing else. The
        Frontier, the Spec and the handoff are the session's own record of itself: `/hi`
        writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the
        Spec, `/handoff` writes the note. A question before each of those writes buys
        nothing — the content is the agent's own, and the person reads it in the reply
        anyway.

        What stays outside the list is the point of the list. `ledger.md` and
        `event_log.md` are written by hooks, `materialize.yaml` by a script, and a harness
        file rendered from a Rule page is refused by `guppi guard`: none of them is the
        agent's to write, so none of them is allowed here. `deny` and `ask` stay empty:
        a refusal that matters has a hook behind it (case 85.5).
      Render: |
        <!-- rule-permissions -->
            "allow": [
              "Edit(vault/raw/**/frontier.md)",
              "Write(vault/raw/**/frontier.md)",
              "Edit(vault/raw/**/spec.md)",
              "Write(vault/raw/**/spec.md)",
              "Edit(vault/raw/**/handoff.md)",
              "Write(vault/raw/**/handoff.md)"
            ]
        <!-- /rule-permissions -->
    method: the six entries in the rendered .claude/settings.json and the JSON case of tests/test_render.py; the live probe — one edit of the session's spec.md in Work Mode and one of frontier.md, each recorded as asked or not asked, and the same at the next session's /hi in Plan Mode
```

```tasks
- [ ] live probe after the render: one edit of raw/2026-09-12/1610/spec.md and one of frontier.md, each recorded as asked or not asked
- [ ] take the reading of estimate-permissions; write the estimate line
```

## Case 86 — the field names of the derived Estimate

> **context:**
> Case 72.1 ratified that a Leaf `create` carries `method`, the Estimate's `kind` (`QA` by
> default) and its `slug` (only on a collision). In Work Mode the agent saw that `kind` and
> `slug` on the item are already the target page's own fields, chose `estimate_kind` and
> `estimate_slug`, and did not return the fork. The code, the tests and `case-schema.md`
> write the prefixed names; the ratified text of 72.1 does not. Case 81 deferred it here.

> **problem:**
> Either the two names are ratified as they stand, or the form goes back to one where
> `kind` and `slug` are unambiguous. No field the harness reads may carry a name nobody
> signed.

> **given:**
> `guppi/materialize.py` holds `DERIVED_KEYS = ("method", "contract", "estimate_slug",
> "estimate_kind")`; line 497 takes `item.get("estimate_slug") or derived_slug(...)` and
> line 505 `item.get("estimate_kind") or "QA"`. `guppi/pretask.py` prints "estimate <slug>
> exists; name estimate_slug". Both names are pinned in `tests/test_materialize.py` and
> `tests/test_pretask.py`.
> **＋** `case-schema.md` writes both names, in the example block and in the prose, and
> nowhere says why the prefix.
> **＋** Against what `decision-case-81` records: `index.md` §7 and `glossary.md` name no
> item key at all; they describe the derivation without one. The disagreement is between
> the ratified text of 72.1 and `case-schema.md` with the code, and nowhere else.
> **＋** `rule-case-protocol` is a Leaf, `draft`, `deferred_by: [decision-case-81]`; its
> Estimate `estimate-case-protocol-loaded` is `pending` and its Criterion already holds the
> clause of 72.1 — a Leaf `create` carries `method` and no nested `estimate`.
> **－** `_lift_item` puts every key of a create item that it does not skip into the page's
> frontmatter, and `DERIVED_KEYS` keeps these four off the target: without the prefix the
> Estimate's `kind` would overwrite the target page's own.

> **when:**
> The agent writes a `then` block for a `create` whose Estimate is a Research, or whose
> derived slug is taken.
> **＋** A session starts with `CLAUDE.md`, which imports `case-schema.md`.

> **then:**
> The item names them `estimate_kind` and `estimate_slug`.
> **＋** `case-schema.md` says why the prefix: `kind` and `slug` on the item are the target
> page's own fields.
> **－** No other key of a `then` item is renamed; `method` and `contract` stay as they are.

```then
update:
  - slug: rule-case-protocol
    contract: changed
    change: "the two keys of the derived Estimate are ratified as estimate_kind and estimate_slug (case 86)"
  - file: vault/wiki/case-schema.md
    change: "after the sentence on the derived slug and kind, one clause: the two keys carry the estimate_ prefix because `kind` and `slug` on the item are the target page's own fields, and an unprefixed `kind` would overwrite the page's (case 86)"
```

```tasks
- [x] vault/wiki/case-schema.md: the `then`-block section gains the clause on why the prefix, applied by hand as a Rule-class file
- [ ] take the reading of estimate-case-protocol-loaded at the next session start, against the case 86 block; write the estimate line
```

## Case 87 — `source` reaches the page from the ledger line

> **context:**
> `materialize.parse_line` reads the braces of a lesson line into options and returns
> `tags` only. `lesson_entry` then marks every `knowledge` lesson `incomplete: [source]`
> and `generate` writes the page without the field, though the line carried one. Case 82
> deferred it here.

> **problem:**
> The lesson entry's contract (`rule-materialize`, `estimate-materialize-assembles`) names
> `kind`, `root_cause`, Trigger and Root cause, and not `source`; carrying the field is a
> change of that contract. The pages already written without it need a decision of their
> own: a backfill, or debt.

> **given:**
> The lesson branch of `parse_line` returns `record`, `kind`, `slug`, `trigger`,
> `root_cause` and `tags`; the decision branch of the same function already reads
> `options.get("source")` (line 116), so the grammar is there and only the lesson does not
> read it.
> **＋** `lesson_entry` builds `fields: {type, kind, root_cause}` with the sections Trigger
> and Root cause, and calls `incomplete.append("source")` for every `knowledge` lesson
> unconditionally.
> **＋** `lessons/schema.md` requires `source` for `knowledge` — "url or reference" — and
> defines `knowledge` as external material studied once so the source never has to be
> supplied again.
> **＋** Twelve `knowledge` lessons are live and eleven carry no `source`. Five of the
> eleven have a ledger line that carries one:
> `lesson-bash-tool-heredoc-escapes-interpreted`,
> `lesson-frame-read-clauses-omit-candidate-check-and-brief`,
> `lesson-librarian-reads-beyond-the-four-inputs`,
> `lesson-readings-after-librarian-invisible-to-next-hi`,
> `lesson-subagents-parallel-on-one-tree-red-mid-flight`. The other six have no source in
> the line either.
> **＋** `guppi lint` prints exactly eleven findings of class `source`; these are they.
> **＋** `rule-materialize` is a Leaf; its first Estimate is `estimate-materialize-assembles`
> (33 tests, `passed` in session J).
> **－** The librarian set `fields.source` on one entry by hand in the last run because the
> handoff told it to — the conflict of F48. After this change no hand is needed.

> **when:**
> `guppi materialize` reads a `- lesson[...]` ledger line whose braces carry `{source:...}`.

> **then:**
> The entry carries `source` in its `fields`, and `generate` writes it into the page's
> frontmatter.
> **＋** A `knowledge` lesson whose line carries no `source` is still marked
> `incomplete: [source]`; an `error` lesson never is.
> **＋** A one-off run sets `source` on the five live pages whose line carries one and whose
> page lacks it, taking the value from the line.
> **－** The six `knowledge` pages whose lines carry no source keep their lint finding;
> nothing invents one.
> **－** The applied entries of the earlier yamls are not rewritten: they record what the
> parser did that day.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-assembles
    replace:
      - old: "`kind`, `root_cause` and the sections `Trigger` and"
        new: "`kind`, `root_cause`, `source` when the braces of the line carry one, and the sections `Trigger` and"
      - old: "`Root cause` from the line."
        new: "`Root cause` from the line; a `knowledge` lesson whose line carries no `source` is marked `incomplete: [source]`, an `error` lesson never (case 87)."
    change: "the lesson entry carries source from the braces of its line (case 87)"
```

```tasks
- [x] guppi/materialize.py: `parse_line` returns `source` for a lesson record; `lesson_entry` puts it in `fields` and marks `incomplete: [source]` only for a `knowledge` line without one
- [x] tests/test_materialize.py: a knowledge line with a source, a knowledge line without one, an error line with one
- [x] one-off: set `source` on the five live lesson pages whose ledger line carries one, from the line itself
- [ ] take the reading of estimate-materialize-assembles; write the estimate line
```

## Case 88 — the live clauses of the two render Estimates

> **context:**
> Both render readings failed in session J on their wording, not on the code. The live
> half of `estimate-render-harness-reproduces` asks for a `git diff --stat` of the two
> dropped marker lines of `hi/SKILL.md`; the live half of `estimate-claude-md-rendered`
> asks the first render to leave a diff of marker lines only. Both were written in the Plan
> Mode of session I against the tree as it stood; the librarian's run of the same session
> wrote the text of cases 59.2, 59.5, 59.6, 62 and 66 into the Rule pages, and the render
> of session J moved six files and 37 lines. Case 84 deferred the repair here.

> **problem:**
> A live clause that describes one past state of the tree goes stale at the first change of
> a page. Both have to say a standing rule, read against the pages that changed.

> **given:**
> In both pages the stale sentence sits in the prose of `## Criterion`, not in a
> `### case N` block: both Estimates are older than the derived-Criterion scheme of case
> 72. A `{supersedes:case N}` removes a block, so it cannot reach them; only an explicit
> `replace` on the Estimate page can.
> **＋** `estimate-render-harness-reproduces` is `failed`, its target `rule-render-harness`
> (Leaf, `draft`, first Estimate). `estimate-claude-md-rendered` is `pending`, its target
> `rule-claude-md` (MOC, `draft`, one Estimate). Both Rule pages carry
> `deferred_by: [decision-case-84]`.
> **＋** The unit halves of both criteria hold: `tests/test_render.py` is green. Only the
> live half breaks.
> **＋** Case 85.1 of this Spec already sets `estimate-render-harness-reproduces` `pending`
> with a block of its own; the block of 88.1 sits beside it and says another thing — one is
> the bare splice into a file that holds no comment, the other is what a render leaves in
> the tree.
> **＋** This is the class of
> `insight-workflow-contract-change-leaves-its-derived-text-stale` (severity 3): the
> contract moves and the derived text stays. Case 72 closed it for criteria born after it;
> these two are older.
> **－** The reading is taken in this session: Work Mode runs `uv run guppi render` for
> 85.2 anyway.

### Case 88.1 — what a render leaves in the tree

> **when:**
> `uv run guppi render` runs against the live vault.

> **then:**
> `git diff --stat` names only the governed files whose Rule page changed since the last
> render.
> **＋** The diff of each file equals the text of that page's Render; a full render also
> drops the page's outer markers, by design.
> **＋** `uv run guppi render --check` then exits 0.
> **－** The clause names no fixed file and no count of lines: it is read against the pages
> that changed, never against a tree that has passed.

```then
update:
  - slug: rule-render-harness
    contract: changed
    estimate_slug: estimate-render-harness-reproduces
    change: "the live clause of the render reading is a standing rule, read against the pages that changed (case 88.1)"
  - slug: estimate-render-harness-reproduces
    replace:
      - old: |-
          Against the live vault: after `uv run guppi render`, `git diff --stat` shows only the two
          dropped marker lines of `.claude/skills/hi/SKILL.md`; after `rule-claude-md` exists, the
          first render changes `CLAUDE.md` by its marker lines only (case 59.8); and
          `uv run guppi render --check` then exits 0.
        new: |-
          Against the live vault: after `uv run guppi render`, `git diff --stat` names only the
          governed files whose Rule page changed since the last render, each diff equal to the
          text of that page's Render, and `uv run guppi render --check` then exits 0 (case 88.1).
    change: "the stale live clause of cases 18.1 and 59.8 leaves the Criterion prose (case 88.1)"
```

```tasks
- [ ] take the reading of estimate-render-harness-reproduces at this session's render, against the blocks of 85.1 and 88.1; write the estimate line
```

### Case 88.2 — what a render leaves in `CLAUDE.md`

> **when:**
> The first `uv run guppi render` after `rule-claude-md` or `rule-case-protocol` changed.

> **then:**
> `CLAUDE.md` equals the Render of `rule-claude-md` with the text of `rule-case-protocol`
> between its markers.
> **＋** The diff holds the text those two pages gained since the file was last written,
> and nothing else.
> **＋** `guppi render --check` then exits 0, and every session after it loads the same
> text with the two `@` imports expanded.

```then
update:
  - slug: rule-claude-md
    contract: changed
    change: "the live clause of the CLAUDE.md reading is a standing rule, read against the two pages that render it (case 88.2)"
  - slug: estimate-claude-md-rendered
    replace:
      - old: |-
          After `uv run guppi render`, `CLAUDE.md` equals the Render of `rule-claude-md` with
          the text of `rule-case-protocol` between its markers; the first such render leaves
          a `git diff` of marker lines only; `guppi render --check` then exits 0; every
          session after it loads the same text, the two `@` imports expanded.
        new: |-
          After `uv run guppi render`, `CLAUDE.md` equals the Render of `rule-claude-md` with
          the text of `rule-case-protocol` between its markers; the diff of that render holds
          the text those two pages gained since the file was last written, and nothing else;
          `guppi render --check` then exits 0; every session after it loads the same text,
          the two `@` imports expanded (case 88.2).
    change: "the stale live clause of case 59.8 leaves the Criterion prose (case 88.2)"
```

```tasks
- [ ] take the reading of estimate-claude-md-rendered at this session's render; write the estimate line
```

## Case 89 — the render runs in the librarian's phase

> **context:**
> `guppi render` writes files only at a session start, from the `--sync` hook. The
> librarian reaches the renderer through `make lint` alone, whose first step is
> `render --check` — it reports and writes nothing. So its commit holds the pages without
> the files they render into, `make lint` fails at step one on that commit, and the gap
> closes only at the next `/hi`.

> **problem:**
> The files should be written where the pages are made: the error then shows in the same
> run and reaches the brief, and the librarian's commit stops contradicting itself. That
> changes what the commit holds, and it makes the live clause of a reading that passed
> today describe something that can no longer happen.

> **given:**
> `rule-documentation` is the full Render of the librarian agent, its steps numbered: 1
> `materialize`, index check, synthesis, 2 `generate`, 3 `cleanup`, then brief and close.
> Its How it works says "The close commits only `vault/`, apart from the session's own
> commit".
> **＋** `rule-close` is a Leaf, `built`, `partial`; its Render says "Commit only paths
> under `vault/` … never anything outside `vault/`", and its Estimate
> `estimate-close-commits` (`passed`) asks for one commit "touching only vault/ paths".
> **＋** The criterion of `estimate-documentation-completes` asks only that the commit be
> separate from the session's; it holds no vault-only clause, so no prose of it is touched.
> **＋** Every governed file lies under three paths beside the vault: `CLAUDE.md`,
> `.claude/settings.json`, and the files under `.claude/agents/` and `.claude/skills/`. So
> `git add vault CLAUDE.md .claude` covers them and sweeps nothing else.
> **＋** `guppi cleanup` is the last step that changes which pages are live and where they
> lie: it moves every `status: archived` page out of `vault/wiki/`, strips archived slugs
> from `children` and `estimates`, and rewrites the indexes. `render_units` filters by
> `enforcement`, never by `status`, so a render before cleanup would build a file from a
> page this run archived, and a full page whose child was archived would splice the
> archived text or fail on it. The render belongs after cleanup.
> **＋** `run()` builds every output in memory through `plan()` and only then calls
> `write_all`, so a `RenderError` leaves nothing written. A pre-flight `--check` would add
> no protection, and it cannot serve as a gate: it exits 1 whenever a file merely differs,
> which after `generate` is always.
> **＋** `.claude/settings.json` is the only governed file a machine parses. If it does not
> load, every hook goes with it — the ledger, the event log, the guard, the pretask gate,
> the spec capture, `render --sync` — and `defaultMode: plan` with them, silently. Case 85
> makes that file an assembly of four pages with the comma between two keys carried in a
> child's body, and 89.1 removes the person who used to see the diff at a session start.
> **－** The frontmatter of an agent or a skill file is machine-read too. It is short,
> stable and barely part of a Render, so 89.4 does not cover it; that would be its own Case.
> **－** `git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so what a
> pull brings is rendered only at the following start. Closing that needs a render inside
> `/hi` after the pull, and it waits for the pull itself to be decided (sprint, Slice 5).

### Case 89.1 — the step in the pipeline

> **when:**
> The librarian reaches the end of its run.

> **then:**
> After `cleanup` and before the brief it runs `uv run guppi render`, and the governed
> files are written from the pages of that same run.
> **＋** Every line on its stderr is a flag for the brief.
> **＋** `make lint` at the close then passes its `render --check` step.
> **－** A file the render could not write is left to the next session start; the librarian
> does not write it by hand.

```then
update:
  - slug: rule-documentation
    contract: changed
    replace:
      - old: |-
          3. Run `uv run guppi cleanup`. Every line on its stderr is a flag.

          <!-- rule-brief -->
        new: |-
          3. Run `uv run guppi cleanup`. Every line on its stderr is a flag.

          4. Run `uv run guppi render`. The pages are final after cleanup, so the governed
             files are written from them here. Every line on its stderr is a flag; a file it
             could not write is left to the next session start.

          <!-- rule-brief -->
      - old: |-
          brief, so the brief sees the final graph and the lint output. The close commits
          only `vault/`, apart from the session's own commit.
        new: |-
          brief, so the brief sees the final graph and the lint output. The render runs after
          cleanup, since cleanup is the last step that changes which pages are live and where
          they lie, and the close commits the pages together with the files they render into,
          apart from the session's own commit (case 89).
    change: "the pipeline gains a render step after cleanup (case 89.1)"
```

```tasks
- [ ] rule-documentation lands at the librarian's run, and the agent file follows at that same render
- [ ] take the reading of estimate-documentation-completes against the librarian's run of this session; write the estimate line
```

### Case 89.2 — what the librarian's commit holds

> **when:**
> The librarian commits.

> **then:**
> The commit takes `vault/` and the files the render wrote: `git add vault CLAUDE.md
> .claude`.
> **＋** It stays one commit, separate from the session's, with the same message
> convention, and never `--amend`.
> **－** No path outside those three.

```then
update:
  - slug: rule-close
    contract: changed
    replace:
      - old: |-
          Close. Run `make lint` and keep its output for the report. Commit only paths under
          `vault/`: `git add vault && git commit -m "docs(vault): librarian, <date>"`, never
          `--amend`, never anything outside `vault/`.
        new: |-
          Close. Run `make lint` and keep its output for the report. Commit the vault with the
          files the render wrote: `git add vault CLAUDE.md .claude && git commit -m
          "docs(vault): librarian, <date>"`, never `--amend`, never a path outside those three.
    change: "the commit takes the governed files the render wrote, beside vault/ (case 89.2)"
  - slug: estimate-close-commits
    replace:
      - old: |-
          After a live librarian run: git log shows one commit after the Retro commit,
          touching only vault/ paths, with the message convention;
        new: |-
          After a live librarian run: git log shows one commit after the Retro commit,
          touching vault/ and the governed files the render wrote and nothing else, with the
          message convention (case 89.2);
    change: "the vault-only clause of the criterion names the rendered files too (case 89.2)"
```

```tasks
- [ ] take the reading of estimate-close-commits against the librarian's commit of this session; write the estimate line
```

### Case 89.3 — what `--sync` reports from now on

> **when:**
> A session starts.

> **then:**
> After a librarian run that rendered, the hook prints nothing, writes nothing, and
> `render --check` exits 0.
> **＋** When a governed file and its page have parted — a hand edit, or a change that
> arrived from outside the session — the diff of that file is in the agent's first turn and
> the page's text is written back.
> **－** The Estimate goes `pending` and is read at the next session start.

```then
update:
  - slug: estimate-render-sync-reports
    set: {status: pending}
    replace:
      - old: |-
          Unit: `guppi render --sync` against a temp vault prints a unified diff for a governed
          file that differs and writes the rendered text; prints and writes nothing for an
          identical one; on a render error prints to stderr, writes nothing, exits 0. Live: at
          the first session start after this one, the diff of the pages the librarian changed
          is in the agent's first turn, the files match their pages, `render --check` exits 0;
          the reading records whether the `CLAUDE.md` loaded by that session is the text the
          hook wrote (a marker sentence added by the librarian's run), or the text before it.
        new: |-
          Unit: `guppi render --sync` against a temp vault prints a unified diff for a governed
          file that differs and writes the rendered text; prints and writes nothing for an
          identical one; on a render error prints to stderr, writes nothing, exits 0. Live: at
          a session start after a librarian run that rendered, the hook prints nothing and
          writes nothing and `render --check` exits 0; at a session start after a governed file
          and its page have parted, the diff of that file is in the agent's first turn and the
          page's text is written back (case 89.3).
    change: "the live clause is read against a tree the librarian already rendered (case 89.3)"
```

```tasks
- [ ] take the reading of estimate-render-sync-reports at the next session start; write the estimate line
```

### Case 89.4 — the render writes no broken JSON

> **when:**
> `guppi render` has built its texts and is about to write, and a target's name ends in
> `.json`.

> **then:**
> Each such text goes through `json.loads` before anything is written.
> **＋** If one of them does not parse, nothing at all is written: the file and the page
> that owns it go to stderr, `render` exits 1 and `--sync` exits 0 with the same line.
> **＋** If all of them parse, the run writes as before.
> **－** No other file type is checked: markdown has no grammar to break.

```then
update:
  - slug: rule-render-harness
    contract: changed
    estimate_slug: estimate-render-harness-reproduces
    replace:
      - old: "The rendered files are committed at Retro."
        new: "A governed file whose name ends in `.json` is parsed before anything is written: when one of them does not parse, the run writes nothing and names the file and its page on stderr (case 89.4). The rendered files are committed by the librarian, in its own commit (case 89.2)."
    change: "a json target is parsed before the write, and one failure stops the whole write (case 89.4)"
```

```tasks
- [x] guppi/render.py: every `.json` output is parsed before `write_all`; one failure writes nothing, names the file and its page, exits 1 and 0 for --sync
- [x] tests/test_render.py: a full page whose JSON output does not parse — nothing written, the file and the page named, both exit codes
- [ ] take the reading of estimate-render-harness-reproduces, against the blocks of 85.1, 88.1 and 89.4; write the estimate line
```

## Case 90 — the Estimate is named, not guessed

> **context:**
> Today's reading of `estimate-documentation-completes` failed on one clause: the librarian
> edited yaml entries by hand. There were three, and the handoff asked for all of them. Two
> were needed because of a defect of `materialize`: the derived entry takes the first
> Estimate of the page, and `None` when the page has none. The third is gone with case 87.

> **problem:**
> Two things. A script guesses which Estimate a Case changes instead of asking. And an
> instruction of the handoff that the librarian's own Rule forbids reaches it with the
> authority of the person's session, and is carried out.

> **given:**
> `derived_entries`, the `update` branch: `"slug": estimates[0] if estimates else None`. The
> `create` branch beside it already reads `item.get("estimate_slug")`, and `DERIVED_KEYS`
> already keeps that key off the target page — on an `update` it is simply not read.
> **＋** Both of the librarian's repairs are of this class: case 73.10 had `slug: null`
> (`rule-claude-md` had an empty `estimates` list when materialize ran) and case 73.3 had
> `estimate-hi-no-read-calls` where the Case changed `estimate-hi-writes-frontier`, because
> the first of `rule-skill-hi`'s two Estimates is not the one that moved.
> **＋** Four pages carry two Estimates: `rule-materialize`, `rule-page-generation`,
> `rule-render-harness`, `rule-skill-hi`. Three contracts of this session hit two of them —
> case 87 on `rule-materialize`, 88.1 and 89.4 on `rule-render-harness` — and each time the
> first of the list was the right one by chance, not by guarantee.
> **＋** `pretask --check` already carries the four form findings of case 72.5: a Leaf
> `create` without `method`, a Leaf `update` without `contract`, two contracts in one Case,
> a colliding derived slug. This is the fifth of that family.
> **＋** The criterion of `estimate-documentation-completes` says the librarian edits the
> yaml only as the index check and the synthesis say; case 44 put yaml repairs in the
> forbidden set by name. The librarian takes the handoff as its first input and as its list
> of instructions, and nothing checks the handoff against that criterion.
> **－** The repairs were useful in themselves: without them two pages would be wrong. After
> 90.1 and 90.2 they are not needed; until then the price of a refusal is a wrong entry that
> the next Plan Mode fixes, instead of a hand nobody signed.

### Case 90.1 — the Estimate is named

> **when:**
> `guppi materialize` meets an `update` whose item carries `contract: changed`.

> **then:**
> When the item carries `estimate_slug`, the derived entry goes to that Estimate.
> **＋** When it does not, and the page carries exactly one Estimate, it goes to that one.
> **＋** When the page carries none or more than one and the item names none, the entry goes
> without a slug and is marked `incomplete: [estimate]`.
> **－** The `create` branch does not change: it reads `estimate_slug` already.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-assembles
    replace:
      - old: "An `update` of a Leaf whose item carries `contract: changed` yields an `update` entry of the target's Estimate:"
        new: "An `update` of a Leaf whose item carries `contract: changed` yields an `update` entry of the Estimate the item's `estimate_slug` names, or of the page's one Estimate when it carries exactly one; when it carries none or more than one and the item names none, the entry goes without a slug and is marked `incomplete: [estimate]` rather than guessing (case 90.1):"
    change: "the derived update names its Estimate instead of taking the first of the page's list (case 90.1)"
```

```tasks
- [x] guppi/materialize.py: the `update` branch of `derived_entries` reads `estimate_slug`, falls back to a page's single Estimate, and marks `incomplete: [estimate]` otherwise
- [x] tests/test_materialize.py: an item that names the slug, a page with one Estimate, a page with two and no slug, a page with none and no slug
- [x] read what `generate` does with an entry that has no slug; if it writes instead of reporting, raise it as a finding at Retro, do not fix it here
- [x] take the reading of estimate-materialize-assembles, against the blocks of 87 and 90.1; write the estimate line
```

### Case 90.2 — pre-task asks for the name in Plan Mode

> **when:**
> `guppi pretask --check` runs against the plan of this Plan Mode.

> **then:**
> It prints one line for every `update` with `contract: changed` whose page carries no
> Estimate or more than one while the item names no `estimate_slug`.
> **＋** The line names the Case, the page and the page's Estimates, so the person can see
> the choice.
> **－** A page with exactly one Estimate is no finding.

```then
update:
  - slug: rule-pretask
    contract: changed
    replace:
      - old: "and for every derived Estimate slug that names an existing page while the item has no `slug`;"
        new: "for every derived Estimate slug that names an existing page while the item has no `slug`, and for every `update` with `contract: changed` whose page carries no Estimate or more than one while the item names no `estimate_slug` (case 90.2);"
    change: "a fifth form finding: the Estimate of a contract change is named when the page's list does not name it alone (case 90.2)"
```

```tasks
- [x] guppi/pretask.py: the fifth form finding, with the Case, the page and its estimates on the line
- [x] tests/test_pretask.py: a page with two Estimates and no `estimate_slug`, a page with none, a page with one, an item that names the slug
- [x] take the reading of estimate-pretask-reconciles; write the estimate line
```

### Case 90.3 — an instruction of the handoff against the Rule

> **when:**
> The handoff tells the librarian to do what the criterion of `rule-documentation` forbids
> — repair an entry of the yaml, or read `ledger.md`, a Spec, a decision page or the
> archive.

> **then:**
> The librarian does not do it.
> **＋** It names the instruction in the report: what was asked, and why it was refused.
> **－** The handoff itself is checked by nothing: it is written from memory, and the
> refusal is the librarian's work, not its author's.
> **－** A refusal does not stop the run: the librarian asks no questions, the person is
> gone.

```then
update:
  - slug: rule-documentation
    contract: changed
    replace:
      - old: |-
          say; an entry a script rejects stays as it is and is a flag in the report, never a
          repair.
        new: |-
          say; an entry a script rejects stays as it is and is a flag in the report, never a
          repair. An instruction of the handoff that this frame forbids — a repair of an
          entry, a read of `ledger.md`, a Spec, a decision page or the archive — you do not
          carry out: name it in the report, what was asked and why it was refused, and go on
          (case 90.3).
    change: "an instruction of the handoff that the frame forbids is refused and named in the report (case 90.3)"
```

```tasks
- [ ] take the reading of estimate-documentation-completes, against the blocks of 89.1 and 90.3; write the estimate line
```

## Case 91 — a refusal of the guard leaves a line in the event log

> **context:**
> A `PreToolUse` hook that blocks a tool leaves no `PostToolUse`, so the call reaches the
> event log never. The fact is `lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event`
> (`knowledge`, with the live probe of session J as its source). The live clause of
> `estimate-governed-files-hook-refuses` asks for the call in the event log, and the reading
> failed on it: two of its three clauses hold. Case 83 deferred the choice here.

> **problem:**
> Either the guard writes the line itself, or the clause leaves the criterion. A refusal is
> the one event of a session the log cannot see.

> **given:**
> The guard exits 2 with the rule's slug and the file on stderr, and writes nothing.
> **＋** `guppi/event.py` holds `format_line(name, payload, words, session, now)`,
> `log_path(project_dir, now)` and `append(path, line)`; `guard.py` already imports
> `project_root` and `read_payload` from it. A log line reads
> `- 15:57:15 d08a5ca5 tool Read: …`.
> **＋** The live clause already asks for the line, so no prose of the Estimate changes: it
> takes the `### case 91` block and goes from `failed` to `pending`.
> **＋** The reading is taken in this session: one refused `Edit` on any governed file.
> **－** Cases 85 and 89 change the world around the guard — what `settings.json` holds and
> when the render runs — but not the guard itself. This is the only change of its code in
> the session.

> **when:**
> `guppi guard` refuses an `Edit`, `Write` or `MultiEdit` of a governed file.

> **then:**
> Before it exits 2 it appends one line to `vault/raw/<date>/event_log.md`.
> **＋** The line carries the time, the session, the tool, the path and the slug of the rule
> that governs the file.
> **－** A call the hook lets through writes nothing: `PostToolUse` logs it as before.
> **－** A log the hook cannot write does not change the refusal: the exit stays 2 and the
> reason still goes to stderr.

```then
update:
  - slug: rule-governed-files-hook
    contract: changed
    replace:
      - old: |-
          `file_path` is a governed path exits 2 with the rule's slug and the file, which
          blocks the tool.
        new: |-
          `file_path` is a governed path exits 2 with the rule's slug and the file, which
          blocks the tool, and one line goes to `vault/raw/<date>/event_log.md` before that:
          a blocked call has no `PostToolUse`, so a refusal the hook does not write is
          nowhere (case 91).
    change: "the hook writes its own event line on a refusal (case 91)"
```

```tasks
- [x] guppi/guard.py: one event line before the exit 2, through `format_line`, `log_path` and `append` of `guppi/event.py`
- [x] tests/test_guard.py: a refusal writes the line with the tool, the path and the rule; a passed call writes none; a log that cannot be written leaves the exit at 2
- [x] live probe: one refused `Edit` on a governed file, then the line in `raw/2026-09-12/event_log.md`
- [x] take the reading of estimate-governed-files-hook-refuses; write the estimate line
```

## Case 92 — two texts that parted from the ratified practice

> **context:**
> The librarian raised two facts for this Plan Mode that ask for no new work, only for a
> signature under what already stands. First: §4 of `index.md` says `ref` is omitted on
> `update` and `delete`, while its own example two lines above carries `{ref:rule-x}` on an
> `update`, and every line of the last four sessions carries it. Second: the Work Mode of
> session J changed two mentions of the Spec in `case-schema.md` to the session folder,
> beyond what the `change` lines of case 73 named literally.

> **problem:**
> In both the text and the practice have parted, and neither side is signed. Either the
> text follows the practice, or the practice goes back to the text.

> **given:**
> `index.md` line 181 is the example
> `- decision[case 12][update][rule-x]{ref:rule-x}{source:external_id}{tags:a,b}`; line 185
> says "`ref` — the parent, for a `create` that adds a child. Omitted for update/delete:
> `slug` already identifies the target". Two lines of one section contradict each other.
> **＋** The Render of `rule-case-protocol`, and so `CLAUDE.md`, already says "A record is a
> `- decision[case 12][update][rule-x]{ref:rule-x}`": the ratified text is on the side of
> the practice, and only §4 disagrees.
> **＋** `materialize.parse_line` reads `options.get("ref")` for a decision line of any
> kind; a `ref` on an `update` overrides nothing and breaks nothing.
> **＋** `case-schema.md` names the session folder in two places, line 60 (Work Mode ticks
> the boxes of the Spec) and line 68 (the short form is appended to the Spec). Both say what
> case 73 decided.
> **－** Both files are Rule-class: applied by hand in Work Mode, no Estimate, no reading
> born here.

> **when:**
> Someone reads §4 of `index.md` or `case-schema.md`.

> **then:**
> §4 says `ref` stands on every decision line: on a `create` it is the parent, on an
> `update` or a `delete` it repeats the target's `slug`.
> **＋** `case-schema.md` names the session folder in both places, signed by case 92.
> **－** The form of the lines does not change: no ledger of an earlier session is rewritten.

```then
update:
  - file: vault/wiki/index.md
    change: "§4: `ref` stands on every decision line — the parent on a create, the target's own slug on an update or a delete, as the example of the section and the Render of rule-case-protocol already show (case 92)"
  - file: vault/wiki/case-schema.md
    change: "the two mentions of the Spec that name the session folder beyond the change lines of case 73 are ratified as they stand (case 92)"
```

```tasks
- [x] vault/wiki/index.md §4: the `ref` bullet, applied by hand as a Rule-class file
- [x] vault/wiki/case-schema.md: read the two session-folder mentions against case 73 and leave them as they stand, applied by hand as a Rule-class file
```

## Case 99 — the texts this session's Cases make false

> **context:**
> Four wordings in the vault say what cases 85, 86 and 90 stop being true. It is the class
> case 88 repaired on the two render Estimates: the contract moves and the derived text
> stays. Here it moves in this session, so the repair belongs in it and not one session
> later.

> **problem:**
> Left standing, the next readings fail on the words and not on the code — exactly how two
> render readings failed today.

> **given:**
> `estimate-hook-registry-rendered` (`passed`) asks the render to leave
> `.claude/settings.json` "byte-identical to the ratified Render body" of that page. After
> 85.3 the page renders the `"hooks"` key alone, and the clause is false by construction;
> 85.3 appends a block and does not touch the prose.
> **＋** `rule-pretask` (line 37) and `rule-materialize` (line 47) name the item's key
> `slug` where the code reads `estimate_slug`. Case 86 ratifies the prefixed names; the two
> texts are left from the earlier wording. `estimate-pretask-reconciles` does not carry the
> phrase — checked.
> **＋** The Purpose of `rule-harness` names its four children "the renderer, the hook
> registry, lint and the indexes". After 85.2 the hook registry is a child of
> `rule-settings`, which takes that slot.
> **＋** `estimate-harness-pipeline` reads the steps of `make lint`, not the children list,
> so the slot swap leaves it alone — checked.
> **－** No contract moves here: all four bring the words to what is already signed. Hence
> `contract: same` on the two Leaf pages and no new criterion block.
> **－** The anchor of the `rule-pretask` pair is the text 90.2 leaves behind, so it matches
> only after that entry applies.

> **when:**
> Someone reads the criterion of `estimate-hook-registry-rendered`, the body of
> `rule-pretask` or `rule-materialize`, or the Purpose of `rule-harness`.

> **then:**
> The criterion of `estimate-hook-registry-rendered` speaks of the `"hooks"` key, and of
> `estimate-settings` for the whole file.
> **＋** Both rules name the key `estimate_slug`.
> **＋** The Purpose of `rule-harness` names the page `.claude/settings.json` is assembled
> from, in place of the hook registry.
> **－** Nothing else in these pages changes.

```then
update:
  - slug: estimate-hook-registry-rendered
    replace:
      - old: |-
          `uv run guppi render` leaves `.claude/settings.json` byte-identical to the ratified Render
          body (`git diff` empty after the two hook additions of cases 20 and 24.1 are applied by
          hand once), the file parses as JSON, and the next session start still writes a
          `session-start` line into `event_log.md`.
        new: |-
          `uv run guppi render` writes the `"hooks"` key of `.claude/settings.json` from the Render
          of `rule-hook-registry`, byte for byte, and every registration the harness runs is one of
          its lines (case 85.3). That the assembled file parses and that the next session start
          still writes its `session-start` line into `event_log.md` belong to `estimate-settings`,
          which reads the whole file (case 99).
    change: "the criterion covers the hooks key; the whole-file clauses move to estimate-settings (case 99)"
  - slug: rule-pretask
    contract: same
    replace:
      - old: "that names an existing page while the item has no `slug`,"
        new: "that names an existing page while the item has no `estimate_slug`,"
    change: "the item's key is named estimate_slug, as case 86 ratified (case 99)"
  - slug: rule-materialize
    contract: same
    replace:
      - old: "or the item's `slug`,"
        new: "or the item's `estimate_slug`,"
    change: "the item's key is named estimate_slug, as case 86 ratified (case 99)"
  - slug: rule-harness
    replace:
      - old: |-
          them. Four rules belong to no phase of the session: the renderer, the hook
          registry, lint and the indexes.
        new: |-
          them. Four rules belong to no phase of the session: the renderer, the page
          `.claude/settings.json` is assembled from, lint and the indexes.
    change: "rule-settings takes the slot of the hook registry in the Purpose too (case 99)"
```

```tasks
- [ ] the four replaces land at the librarian's run; no file of the harness changes here
```

## Deferred

## Case 93 — Slice 3b: Work Mode

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since case 29, now
> 78, without `kind`, `estimates` or `tags`; two of lint's three orphans. The draft in
> `docs/migration/` still has to be reconciled with case 59.3 — no separate `plan.md`, the
> `tasks` blocks of the Spec — and with the fork clause.

> **problem:**
> The phase the harness spends most of its time in is the one phase with no ratified rule.
> It needs a Plan Mode of its own, not a corner of this one.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: The rule of Work Mode — the Spec as tasks with code, the ticked boxes, what a subagent may do
  - slug: rule-subagent-guppi
    type: rule
    purpose: The rule of the transcribing subagent — it never decides, and a fork comes back as a Case
```

## Case 94 — the archive in `ask-guppi`

> **context:**
> The search agent reads the four live indexes and never `vault/archived/`, which holds 22
> pages. A `create` whose slug was archived comes back as free.

> **problem:**
> A named slug has to be checked against the archive, and the answer has to say which of
> the two it found.

```then
defer:
  - slug: rule-ask
    type: rule
    purpose: The archive is part of the vault the agent answers from, and a named slug is checked against it
```

## Case 95 — Slice 3c: the lifecycle of `raw/`

> **context:**
> `decided_by` on the pages born of a Case, `origin` as a pointer into the ledger, the
> `raw/<date>/` of a fully applied date archived by run stamp with its paths rewritten, a
> fresh ledger as the tail `/hi` prints, lint on both fields, the pages migrated by script.
> Deferred four times, last as case 79.

> **problem:**
> `raw/` grows without end and nothing says when a date is done with. The slice needs its
> own Plan Mode.

```then
defer:
  - slug: rule-ledger-tail
    type: rule
    purpose: The lifecycle of raw/ — an applied date archived by run stamp, the fresh ledger the tail prints, decided_by and origin under lint
```

## Case 96 — the `## Insight` section nothing writes

> **context:**
> Eighteen `clustered` lessons carry no `## Insight` section, five of them from the last
> run. The synthesis sets the `insight` field in the frontmatter, and nothing writes the
> section `lessons/schema.md` requires. They are 18 of lint's 128 schema findings.

> **problem:**
> Either the synthesis entry carries the section, or the schema stops asking for it. Both
> are a change of what a synthesis entry holds.

```then
defer:
  - slug: rule-synthesis
    type: rule
    purpose: A synthesis entry carries the ## Insight section of the lesson it clusters, or the schema stops requiring one
```

## Case 97 — an Insight whose evidence was withdrawn

> **context:**
> `insight-ledger-hook-reads-only-the-final-text` stands on one live child: case 70
> archived the second of its two members, `generate` recounted its severity to 1, and the
> archived slug stays in `children`. Its Proposal was already the behaviour of case 55.2,
> and the new lesson says the hook dropped nothing.

> **problem:**
> What becomes of an Insight whose evidence is withdrawn is a decision, not a librarian's
> judgment, and no rule says it.

```then
defer:
  - slug: rule-synthesis
    type: rule
    purpose: What becomes of an Insight when its children are archived — the count, the status, and who decides
```

## Case 98 — the render after a pull

> **context:**
> `git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so a change the
> pull brings is rendered only at the following session start. Case 89 puts the render in
> the librarian's phase and leaves this half open.

> **problem:**
> The render has to run once more after the pull, inside `/hi`. It waits for the pull
> itself, which has no upstream to pull from yet (sprint, Slice 5).

```then
defer:
  - slug: rule-skill-hi
    type: rule
    purpose: A render inside /hi after the pull, so what arrives from outside the session reaches its files in the same session
```
