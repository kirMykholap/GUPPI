<!-- approved 10:22:55 · session bf4dd2b3 -->

# Spec — 2026-09-21, session 0019

## Case 286 — the `read` line of a superseded Case is not one `generate` ticks

> **context:**
> `generate`, once it applied an `estimate` entry of the yaml, ticks the first unticked line `- [ ] read `<slug>`` — in the Spec beside the yaml first, then in the Specs of the other sessions of `raw/`, oldest first. In the Spec beside the yaml it skips the sections of the Cases ratified after the reading (280); in the other Specs it skips nothing and looks at no Case. When a Case is superseded by another (`{supersedes:case N}`), its yaml entries are marked `superseded_by`: `generate` neither applies them nor ticks their page lines (151, 200.2), and Retro does not count their lines (282). But the `read` line of such a Case is an ordinary line to `tick_read`: in the run of 2106 the reading of `estimate-case-protocol-loaded` landed on 1749:39 (Case 278, superseded by 279.1) and 1749:88 (279.1) stayed open. The Estimate page is right — `passed` on the Criterion of 279.1; the Spec says the opposite: a Criterion that is not there was read, and the signed one was not. The 1749 Spec is in the archive now, `generate` does not read it, and line 88 stays `[ ]` for good. The brief also names 1749:38 as ticked by the librarian of 1749 — in the file it is `[ ]`, as it should be for a superseded Case.
> `rule-page-generation` `draft` (`estimate-generate-rewords` pending); of the eight Estimates of the rule one is touched — `estimate-generate-ticks-the-spec` (`passed` 2106), the other seven not; an `update` with a `ref`, no vault query due.

> **problem:**
> A reading closes the line of a Case whose work stands under another Case. The record in the Spec is wrong, and the line of the superseding Case never closes. Either this is contract — and `tick_read` skips the sections of superseded Cases by the marks of the yaml — or a fact for the reading of the Estimate, and the record stays wrong.

> **given:**
> A yaml entry of kind `estimate` carries `slug`, `status`, `result`, `line` and no `case`; a decision entry carries `case` and `line`, the number of its line in the ledger.
> **＋** A line `{supersedes:case N}` marks every entry of Case N `superseded_by`, in the yaml of any session under `raw/` (130.2, 175); `generate` neither applies them nor ticks their page lines (151, 200.2).
> **＋** The lines of a superseded Case are not counted at Retro — its work stands under the superseding Case (282).
> **＋** The Spec of a session lies beside its `materialize.yaml` — `raw/<date>/<HHMM>/spec.md`; the Specs of the other sessions are the `spec.md` of their folders under `raw/`.
> **＋** A Case heading in the Spec is `## Case N — …` or `### Case N.M — …`; its section runs to the next such heading.
> **＋** A reading line of the Spec is `- [ ] read `<slug>`` with text after it, in any Case.
> **＋** `tests/test_generate.py` fixes the behaviour on a temp vault with a Spec beside the yaml and a second Spec with a yaml of its own in another session folder.
> **－** A Rule-class file entry `generate` does not apply — "applied by hand".

> **when:**
> `guppi generate` applied an entry and marked it `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit the first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes.
> **＋** Two entries of one kind and slug in one Case tick two lines, in order.
> **＋** For an `estimate` entry, and for a `create` entry with `folded`, the first unticked line `- [ ] read `<slug>`` becomes `- [x]` — in the Spec beside the yaml first, then in the `spec.md` of the other session folders of `raw/`, oldest first; one line per entry.
> **＋** In the Spec beside the yaml, a `read` line in the section of a Case whose first decision entry of the yaml carries a `line` greater than the `line` of the `estimate` entry is not the reading's line — the Case was ratified after it; the search goes on to the next line, then to the other sessions.
> **＋** In any Spec, a `read` line in the section of a Case whose entries in the yaml of that session are marked `superseded_by` is not the reading's line — its work stands under the superseding Case; the search goes on. For the Spec beside the yaml the marks are the run's entries; for the Spec of another session its `materialize.yaml` beside it, read for the marks alone; no yaml beside it — nothing is skipped there.
> **＋** A `create` entry with `folded` ticks both lines: the page line and the reading line; its Case is the reading's Case, the filter of 280 does not apply to it; the filter by `superseded_by` does.
> **－** A line not found, a section not found, no Spec — no error and no stderr line; the entry is `applied` all the same.
> **－** `lesson` and Rule-class file entries, and an entry marked `failed`, tick no line; the lines on code, tests, migrations and `by hand` are the agent's.
> **－** A Spec under `vault/archive/` is not read; the Specs of the other sessions are not filtered by `line`.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "in the Spec beside the yaml first — skipping the section of a Case whose first decision entry stands after the reading in the ledger, a Case ratified after it — and then in the `spec.md` of the other session folders of `raw/`, oldest first — so the Spec's page lines and reading lines are closed by the one who did the work, and a line not found is no error (cases 226.1, 270.1, 280)."
        new: "in the Spec beside the yaml first — skipping the section of a Case whose first decision entry stands after the reading in the ledger, a Case ratified after it — and then in the `spec.md` of the other session folders of `raw/`, oldest first, skipping in every Spec the section of a Case whose entries the yaml beside it marks `superseded_by`, its work standing under the superseding Case — so the Spec's page lines and reading lines are closed by the one who did the work, and a line not found is no error (cases 226.1, 270.1, 280, 286)."
    change: a reading does not tick the read line of a superseded Case, in any Spec of raw/ (case 286)
  - slug: estimate-generate-ticks-the-spec
    set: {status: pending}
    change: the Criterion replaced whole — the read line of a superseded Case is skipped by the marks of the yaml beside the Spec (case 286)
```

```tasks
- [x] update `rule-page-generation`: `replace` in the Purpose — the tick sentence names the superseded Case
- [x] update `estimate-generate-ticks-the-spec`: the Criterion replaced whole, `pending`
- [x] `guppi/generate.py`: `superseded_cases(entries)`; `tick_read` skips them in every Spec — the run's entries for the first, the `materialize.yaml` beside each other Spec; the docstring
- [x] `tests/test_generate.py`: a `read` line under a superseded Case in the Spec beside the yaml — skipped, the next one ticked; in another session's Spec with its yaml — skipped; no yaml beside it — ticked
- [x] by hand, a one-off: `vault/archive/migration/2026-09-20/1749/raw/spec.md` — line 39 back to `[ ]`, line 88 to `[x]`
- [x] read `estimate-generate-ticks-the-spec`: pytest now; live — the first librarian's run whose ledger holds a `{supersedes:case N}` and a reading of a slug with a `read` line under Case N; no date
```

## Case 287 — a `SessionStart compact` hook brings back what `/hi` loaded

> **context:**
> `/hi` brings `sprint.md`, `brief.md`, `case-schema.md` (and the glossary after C4.1) into the first turn through the `@` lines of the skill; `CLAUDE.md` lives in the system prompt. When the client compacts the context, `CLAUDE.md` is read again from disk, but the body of an invoked skill comes back capped at 5,000 tokens — after a compaction the Case schema, the Frontier and the Spec stand in the context only as far as the summary kept them. Two hooks run on `SessionStart`, both without a matcher: `guppi event session-start` (writes `session-start compact`; the `hi` window survives, case 14) and `guppi render --sync`. Nothing brings the session's load back. A hook's stdout over 10,000 characters is saved to a file, so the hook prints paths and the Frontier, not the texts.
> The vault: no page on compaction, `rule-compact-recall` free; the nearest is `rule-internal-context` (`built`), whose `estimate-internal-context-loaded` measures the first turn after `/hi`, not a compaction — not touched; `rule-session-start` (`built`, MOC) takes a fourth child, its `estimate-session-start-context` not touched; `rule-hook-registry` (`built`) — the registration, `estimate-hook-registry-rendered` measures the file against the page, its Criterion unchanged.

> **problem:**
> After a compaction a working session goes on in Plan Mode or Work Mode without the Case schema, without the Frontier and without the exact text of the Spec — the agent works from a summary. A hook is needed that, after `compact`, brings back into the context what `/hi` brought at the start.

> **given:**
> `SessionStart` fires after a compaction with `source: compact`; the hook's stdout on exit 0 enters the context as text; output over 10,000 characters is saved to a file and the agent gets a preview and the path (Claude Code docs, hooks guide).
> **＋** A `SessionStart` hook cannot block (`lesson-hooks-sessionstart-cannot-block`).
> **＋** The session's window and folder are the ones the ledger hook finds: `session_dir` in `guppi/ledger.py`, the first `hi` of the stamp after its first `session-start`; `compact` does not close the window (case 14).
> **＋** The files `/hi` imports are the `@` lines of `.claude/skills/hi/SKILL.md`, the Render of `rule-internal-context`; the glossary joins them by C4.1.
> **＋** The Spec of a session is `spec.md` in its folder after the approval; before it, the plan file the event log names last under `.claude/plans/`, as `guppi gate` reads it (case 122).
> **＋** `tests/test_recall.py` fixes the behaviour on a temp project with an event log, a skill file and a session folder.

> **when:**
> The client compacted the context of the session — `/compact` or on its own — and `SessionStart` fired with `source: compact`.

> **then:**
> With a `hi` in the session's window, stdout holds: the line `recall: the context was compacted at HH:MM:SS; the session is raw/<date>/<HHMM>/. Read before the next reply:`; then one path per line — the `@` files of the `/hi` skill in their order, the session's `frontier.md` when it exists, the Spec when one exists; then the line `Frontier:` and the text of `frontier.md` as it stands.
> **＋** The list of paths is the `@` lines of the skill file at the moment the hook fires, no copy in the code: a file added to `rule-internal-context` — the glossary by C4.1 — is in the list without a change to the hook.
> **＋** The texts of the files, the Frontier apart, are not printed — the paths only; the output stays under 10,000 characters.
> **－** Without a `hi` in the window — nothing on stdout, exit 0.
> **－** Another `source` — nothing: the matcher keeps the hook from firing, and the code checks `source` itself.
> **－** Exit 0 always; an error prints nothing and blocks nothing; the hook writes no file and no event line — `session-start compact` is already written by `guppi event`.

```then
create:
  - slug: rule-compact-recall
    type: rule
    kind: Leaf
    purpose: Prevents a working session from going on after a compaction without the Case schema, the Frontier and the Spec in its context
    enforcement: hook
    implementation_ref: [guppi/recall.py, guppi/cli.py, tests/test_recall.py, .claude/settings.json]
    tags: [session, hooks, harness]
    sections:
      Purpose: |
        Prevents a working session from going on after a compaction without the Case schema, the Frontier and the Spec in its context. `/hi` loads the session's texts once, through the `@` lines of its skill; a compaction keeps `CLAUDE.md` and a capped part of the skill's body, and the rest survives only in the summary. This hook fires on `SessionStart` with `source: compact` and prints what to read back: the paths of the files `/hi` imports, the session's `frontier.md` and its Spec, and the Frontier's text itself. Paths, not texts: a hook's stdout over 10,000 characters is saved to a file and the agent gets a preview (case 287).
      How it works: |
        `uv run guppi recall`, registered on `SessionStart` with the matcher `compact` (`rule-hook-registry`). Reads the payload from stdin; with a `source` other than `compact` or without a `hi` in the session's window — `session_dir` of `guppi/ledger.py`, the ledger hook's own — it prints nothing, exit 0. Otherwise stdout holds one header line naming the time and the session's folder, then one path per line: the `@` lines of `.claude/skills/hi/SKILL.md` in their order, the folder's `frontier.md` when it exists, the Spec — `spec.md` of the folder, or before the approval the plan file the event log names last under `.claude/plans/`, as `guppi gate` finds it (case 122) — then `Frontier:` and the text of `frontier.md`. The list of files is the skill file's, never a copy in the code. Exit 0 always; the hook writes nothing.
  - slug: estimate-compact-recall-reloads
    type: estimate
    ref: rule-compact-recall
    kind: QA
    purpose: After a compaction of a working session the hook's header, the paths of the /hi files, the Spec and the Frontier's text stand in the context; an ordinary session and another source get nothing
    method: pytest tests/test_recall.py on a temp project; live — the first compaction of a working session, by hand, the hook's text in the context after it
    tags: [session, hooks, harness]
update:
  - slug: rule-session-start
    set: {children: ["[[rule-skill-hi]]", "[[rule-event-log]]", "[[rule-ledger-write]]", "[[rule-compact-recall]]"]}
    change: rule-compact-recall is the fourth child — the hook that brings the session's load back after a compaction (case 287)
  - slug: rule-hook-registry
    change: guppi recall registered on SessionStart with the matcher compact (case 287)
    sections:
      Render: |
        <!-- rule-hook-registry -->
            "SessionStart": [
              { "hooks": [ { "type": "command", "command": "uv run guppi event session-start", "timeout": 30 },
                           { "type": "command", "command": "uv run guppi render --sync", "timeout": 60 } ] },
              { "matcher": "compact",
                "hooks": [ { "type": "command", "command": "uv run guppi recall", "timeout": 30 } ] }
        ],
        "UserPromptSubmit": [
          { "hooks": [ { "type": "command", "command": "uv run guppi event prompt", "timeout": 30 },
                       { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] }
        ],
        "PreToolUse": [

              { "matcher": "ExitPlanMode",
                "hooks": [ { "type": "command", "command": "uv run guppi prespec", "timeout": 30 } ] },
              { "matcher": "Skill",
                "hooks": [ { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] },
              { "matcher": "Edit|Write|MultiEdit",
          "hooks": [ { "type": "command", "command": "uv run guppi guard", "timeout": 30 } ] },
        { "matcher": "Bash",
          "hooks": [ { "type": "command", "command": "uv run guppi bashguard", "timeout": 30 } ] }

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
```

```tasks
- [x] create `rule-compact-recall`, child of `rule-session-start`
- [x] create `estimate-compact-recall-reloads`, `ref: rule-compact-recall`
- [x] update `rule-session-start`: `children` — the fourth
- [x] update `rule-hook-registry`: the `SessionStart` entry with the matcher `compact`
- [x] `guppi/recall.py`: the hook; `guppi/cli.py`: the `recall` command
- [x] `tests/test_recall.py`: compact with a `hi` — the header, the paths in order, the Frontier's text; a fourth `@` line in the skill file — a fourth path; compact without a `hi` — nothing; another `source` — nothing; no frontier, no Spec — the lines absent; the Spec from the plan file before the approval and from `spec.md` after
- [x] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-compact-recall-reloads`: pytest; live — the first compaction of a working session, by hand; no date
```

## Case 288 — `CLAUDE.md` reviewed: the glossary with `/hi`, the one rule in the schema, the Render cut

> **context:**
> `CLAUDE.md` is the Render of `rule-claude-md` whole, with `rule-language` and `rule-agent-writing` in their markers. It enters the system prompt of every session and of every subagent — the librarian, `ask-guppi`, the subagents of Work Mode. Today it holds: the first paragraph (the description of the project and the one rule — ratification, autonomy over the how, "when unsure: it does", the vault as the only memory), "What is loaded here", the `@` import of the glossary, a paragraph on `index.md` not being imported, "Migration mode" (four items, each a Rule with its Render in the harness by now; "nothing prints it yet" stale since case 125) and "Commands" (`make style` before a commit stands in the Render of `rule-retro`; "no new dependencies" came with the hand-written file in 59.8, never decided on its own). The glossary through `CLAUDE.md` is paid by every subagent; a subagent receives the `CLAUDE.md` hierarchy and not the content of an invoked skill (Claude Code docs, sub-agents). `case-schema.md` opens with a line on how it is loaded and holds the form of a Case; the one rule is not in it.
> The pages: `rule-claude-md` `built` — `estimate-claude-md-rendered` `passed` 1749, touched; `rule-internal-context` `built` — `estimate-internal-context-loaded` `passed` 1749, touched, its How it works says the glossary arrives through `CLAUDE.md`; `rule-case-protocol` `draft` — `estimate-case-protocol-loaded` `passed` 2106, touched, the other three Estimates not, its Purpose says "`CLAUDE.md` keeps the one rule and the glossary". Three `update` with a `ref`, no vault query due. `rule-info` rejected in the chat: the description of a project is no Rule by the glossary's check.

> **problem:**
> The system prompt carries a retelling of rules that live in their own Renders, stale lines and a glossary every subagent pays for, and the one rule stands where no Case is held. What stays in `CLAUDE.md`, where the glossary goes and where the one rule.

### Case 288.1 — the glossary arrives with `/hi`

> **given:**
> The `/hi` skill is the Render of `rule-skill-hi` with its children in markers; `rule-internal-context` is the block of `@` lines Claude Code expands when the skill is invoked.
> **＋** A subagent receives the `CLAUDE.md` hierarchy and not the content of an invoked skill (Claude Code docs, sub-agents).
> **＋** `guppi recall` prints the `@` lines of the skill file after a compaction (287).
> **＋** `guppi render --check` keeps the skill file equal to the page.

> **when:**
> The person invokes `/hi`.

> **then:**
> The text of `sprint.md`, `brief.md`, `case-schema.md` and `glossary.md` is present in the first turn's context, in that order, without a read call.
> **＋** The glossary reaches a session through this block alone; after a compaction its path is in the list of `guppi recall`.
> **－** A subagent — `librarian-guppi`, `ask-guppi`, one of Work Mode — carries no glossary; its prompt names what it needs.

```then
update:
  - slug: rule-internal-context
    change: the glossary is the fourth @ line — it arrives with /hi and reaches no subagent, which pays for CLAUDE.md alone (case 288.1)
    sections:
      Render: |
        <!-- rule-internal-context -->
        @vault/wiki/sprint.md
        @vault/wiki/brief.md
        @vault/wiki/case-schema.md
        @vault/wiki/glossary.md
        <!-- /rule-internal-context -->
      How it works: |
        `case-schema.md` is listed since case 273: the Render of `rule-case-protocol`, it reaches
        a working session here and not through `CLAUDE.md`, so a session without `/hi` carries no
        Case text. `glossary.md` is listed since case 288.1: it left the `@` import of `CLAUDE.md`,
        which every subagent loads and none of them needs. The category schemas are not listed:
        they are read when a page of their category is written. After a compaction `guppi recall`
        prints the paths of these lines back (case 287).
  - slug: estimate-internal-context-loaded
    set: {status: pending}
    change: the Criterion replaced whole — four texts expanded, glossary.md the fourth (case 288.1)
```

```tasks
- [x] update `rule-internal-context`: the Render — a fourth `@` line; How it works — the sentence on the glossary
- [x] update `estimate-internal-context-loaded`: the Criterion replaced whole, `pending`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] read `estimate-internal-context-loaded`: the `/hi` of the next session, by hand
```

### Case 288.2 — the one rule opens the Case schema

> **given:**
> `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi`; the hook refuses a hand edit.
> **＋** The one rule stood as the first paragraph of `CLAUDE.md` until this Case (59.8, 272.1).
> **＋** `guppi render --check` keeps the file equal to the page.

> **when:**
> The first `uv run guppi render` after `rule-case-protocol` changed, and the `/hi` of the next session.

> **then:**
> `case-schema.md` opens with the section "The one rule" right under its title: nothing in the vault or the codebase changes without a Decision ratified by the human; the agent has full autonomy over how to implement something once its contract is ratified, and none over the contract itself; when unsure whether something needs ratification, it does; the vault is the only memory — no note outside the repository, what is worth keeping is a `lesson` line or a Case on a Rule page (272.1).
> **＋** The paragraph after it says, as before, that the schema is the Render loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md`, and that a session without `/hi` holds no Case.
> **＋** `render --check` after the render exits 0.
> **－** The other sections of the schema do not change; the description of the project is not in the schema.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "`wiki/case-schema.md` — the Render of `rule-case-protocol`, loaded by `/hi` with `sprint.md` and `brief.md`, so the structure is present from the first turn of a working session rather than read as a file; the map of the vault is [[index]]. A session without `/hi` holds no Case: the ledger hook refuses it."
        new: "## The one rule\n\nNothing in the vault or the codebase changes without a Decision ratified by the human. The agent has full autonomy over *how* to implement something once its contract is ratified, and none over the contract itself. When unsure whether something needs ratification: it does. The vault is the only memory: no note outside the repository — not the harness's memory directory, not a file outside `vault/`; what is worth keeping is a `lesson` line or a Case on a Rule page (case 272.1).\n\n`wiki/case-schema.md` — the Render of `rule-case-protocol`, loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md`, so the structure and the terms are present from the first turn of a working session rather than read as a file; the map of the vault is [[index]]. A session without `/hi` holds no Case: the ledger hook refuses it."
      - old: "keeps the one rule and the glossary."
        new: "keeps the description of the project, the language and the writing rules; the one rule opens this Render, and the glossary comes with it (case 288.2)."
    change: the one rule opens the schema, moved from CLAUDE.md; the opening line names the glossary among the files /hi loads (case 288.2)
  - slug: estimate-case-protocol-loaded
    set: {status: pending}
    change: the Criterion replaced whole — the schema opens with the one rule, the glossary among the files /hi loads (case 288.2)
```

```tasks
- [x] update `rule-case-protocol`: `replace` in the Render — the opening paragraph; `replace` in the Purpose — the sentence on `CLAUDE.md`
- [x] update `estimate-case-protocol-loaded`: the Criterion replaced whole, `pending`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-loaded`: the `/hi` of the next session, by hand
```

### Case 288.3 — `CLAUDE.md`: the title, the description, two markers

> **given:**
> `CLAUDE.md` is the Render of `rule-claude-md` whole (`render_mode: full`), the children `rule-language` and `rule-agent-writing` in their markers; the hook refuses a hand edit.
> **＋** Each item of "Migration mode" is a Rule with its own Render: `rule-internal-context`, `rule-ledger-write`, `rule-retro`, `rule-handoff`, `rule-documentation`, `rule-spec-capture`; "`make style` clean before the commit" is in the Render of `rule-retro`.
> **＋** The glossary and the schema arrive with `/hi` (273.3, 288.1); the one rule stands in the schema (288.2).
> **＋** `guppi render --check` keeps the file equal to the page.

> **when:**
> The first `uv run guppi render` after `rule-claude-md` changed, and the start of the next session with `CLAUDE.md`.

> **then:**
> `CLAUDE.md` is: `# GUPPI`; one paragraph — a Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into; the vault is `vault/`, its map `vault/wiki/index.md`, its terms `vault/wiki/glossary.md`; a working session opens with `/hi`; then the text of `rule-language` and `rule-agent-writing` in their markers.
> **＋** `render --check` after the render exits 0; every session and every subagent loads this text.
> **－** No `@` import, no "What is loaded here", no paragraph on `index.md`, no "Migration mode", no "Commands", no one rule and no sentence on memory — the one rule is in the schema; the `children` of `rule-claude-md` are `rule-language` and `rule-agent-writing`.

```then
update:
  - slug: rule-claude-md
    replace:
      - old: "The Render imports [[glossary]] and points at [[index]]; the Case schema is the Render of `rule-case-protocol`, loaded by `/hi` (cases 272, 273.3)."
        new: "The Render holds the description of the project and the two children; the glossary and the Case schema arrive with `/hi`, the one rule opens the schema (cases 272, 273.3, 288.3)."
    change: the Render is the title, the description of the project and the two markers — the import, What is loaded here, the index paragraph, Migration mode and Commands leave; the one rule to the schema (case 288.3)
    sections:
      Render: |
        <!-- rule-claude-md -->
        # GUPPI

        A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. The vault is `vault/`; its map is `vault/wiki/index.md`; its terms are `vault/wiki/glossary.md`. A working session opens with `/hi`.

        <!-- rule-language -->

        <!-- rule-agent-writing -->
        <!-- /rule-claude-md -->
      How it works: |
        Rendered in full into `CLAUDE.md`; each child — `rule-language`, `rule-agent-writing` — splices into its marker line. The file is the system prompt of every session and of every subagent, so it holds what each of them needs and no more: the description of the project and the two standing rules. The glossary and the Case schema arrive with `/hi` through `rule-internal-context`, and the one rule opens the schema (case 288). The section "Migration mode", carried from the hand-written file of 2026-09-12, left with case 288.3, each of its items a Rule with a Render of its own by then; "Commands" left with it — `make style` before a commit is `rule-retro`'s, and "no new dependencies" came with the file in 59.8 and was never decided on its own. `rule-language` and `rule-agent-writing` have this page as their parent since case 272. `rule-case-protocol` was a child from case 66 to case 273, when its Render became `case-schema.md` and its parent `rule-plan-mode`.
  - slug: estimate-claude-md-rendered
    set: {status: pending}
    change: the Criterion replaced whole — the title, the description and the two markers, nothing else (case 288.3)
```

```tasks
- [x] update `rule-claude-md`: the Render whole; How it works whole; `replace` in the Purpose — the sentence on the import
- [x] update `estimate-claude-md-rendered`: the Criterion replaced whole, `pending`
- [x] `uv run guppi render`: `CLAUDE.md`
- [x] read `estimate-claude-md-rendered`: `render --check` after the build; the start of the next session, by hand
```

## Case 290 — the tails of pre-spec: the pages 287 and 288 left at odds with themselves

> **context:**
> 288.1 and 288.3 take the glossary out of `CLAUDE.md`, but `glossary.md` itself says in its header "Rule-class; imported into `CLAUDE.md`", and its row "`CLAUDE.md`, `case-schema.md`, `index.md`" that `@path` expands it inline. It is a Rule-class file, changed only by an `update` with `file`, by hand. 287 gives `rule-session-start` a fourth child, but the page's How it works says "Children 2–3 are hooks. They run in every session" and "the registration of children 2–3". 286 and 288.1 replaced the Criterion of two Estimates, and their `purpose` — "in the Spec beside its yaml", "sprint.md, brief.md and case-schema.md" — stayed from the old promise; the Purpose of `rule-case-protocol`, one line above the replace of 288.2, still says "loaded by `/hi` with `sprint.md` and `brief.md`".
> Three pages and two Estimates; no Criterion is touched: a `purpose` is the index line, not the promise; the Purpose of a rule touches no Estimate (187). Updates with a `ref`; the vault asked at pre-spec.

> **problem:**
> After this session's render four texts contradict what is ratified: the glossary names its old path, the page of the session start counts its children, two index lines and a Purpose describe the previous promise.

### Case 290.1 — `glossary.md` says where it comes from

> **given:**
> `glossary.md` is a Rule-class file: it changes only by a ratified `update` with `file`, by hand (§1).
> **＋** The glossary arrives with `/hi` as the fourth `@` line (288.1); `CLAUDE.md` is the title, the description and two markers (288.3).

> **when:**
> Someone reads `glossary.md` — in the first turn after `/hi`, or as a file.

> **then:**
> The header says "Rule-class; loaded by `/hi` with the Case schema"; the row "`CLAUDE.md`, `case-schema.md`, `index.md`" says `CLAUDE.md` is the Render of `rule-claude-md` — the description of the project, `rule-language` and `rule-agent-writing` in their markers; the schema and the glossary arrive with `/hi` (288); the map is read a section at a time.
> **－** The other rows do not change.

```then
update:
  - slug: glossary
    file: vault/wiki/glossary.md
    change: the header and the CLAUDE.md row say the glossary and the schema arrive with /hi, and what CLAUDE.md holds since 288.3 (case 290.1)
```

```tasks
- [x] update `glossary`, by hand: the header line — "Rule-class; loaded by `/hi` with the Case schema." — and the row `CLAUDE.md`, `case-schema.md`, `index.md`
```

### Case 290.2 — `rule-session-start` counts four children

> **given:**
> `rule-compact-recall` is the fourth child of `rule-session-start`, the hook on `SessionStart compact` in a working session (287).
> **＋** `rule-session-start` renders nothing; a change of its How it works touches no Estimate.

> **when:**
> Someone reads the page `rule-session-start`.

> **then:**
> How it works says: children 2–4 are hooks; 2 and 3 run in every session, 4 only after a compaction and only with a `hi` in the window; the registration of children 2–4 is in `rule-hook-registry`.
> **－** The other sections do not change.

```then
update:
  - slug: rule-session-start
    replace:
      - old: "Children 2–3 are hooks. They run in **every** session, ordinary ones included, and that is"
        new: "Children 2–4 are hooks. Children 2–3 run in **every** session, ordinary ones included, and that is"
      - old: "The hook registry that records the registration of children 2–3 is not a step of the session; it lives under `rule-harness` with the other tools."
        new: "Child 4, `rule-compact-recall`, runs only after a compaction, and prints only with a `hi` in the window (case 287). The hook registry that records the registration of children 2–4 is not a step of the session; it lives under `rule-harness` with the other tools."
    change: How it works counts four children — the fourth fires after a compaction only (case 290.2)
```

```tasks
- [x] update `rule-session-start`: `replace` in How it works — the two sentences on children 2–3
```

### Case 290.3 — the index lines and the Purpose by the new promise

> **given:**
> The `purpose` of an Estimate is the line the index is built from, not the Criterion; `set.purpose` changes no promise.
> **＋** An `update` of a rule's Purpose touches no Estimate (187).
> **＋** The Criterion of `estimate-generate-ticks-the-spec` is 286's, of `estimate-internal-context-loaded` 288.1's, both `pending`.

> **when:**
> Someone reads the index line of an Estimate, or the Purpose of `rule-case-protocol`.

> **then:**
> The `purpose` of `estimate-generate-ticks-the-spec`: generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading across the Specs of raw/ — never a line of a later or a superseded Case. The `purpose` of `estimate-internal-context-loaded`: the text of sprint.md, brief.md, case-schema.md and glossary.md is present in the first turn's context after /hi, without a read call. The Purpose of `rule-case-protocol`: "loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md` (cases 273.1, 288.1)".
> **－** The Criterion and the `status` do not change.

```then
update:
  - slug: estimate-generate-ticks-the-spec
    set: {purpose: "generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading across the Specs of raw/ — never a line of a later or a superseded Case"}
    change: the purpose by the Criterion of 286 (case 290.3)
  - slug: estimate-internal-context-loaded
    set: {purpose: "The text of sprint.md, brief.md, case-schema.md and glossary.md is present in the first turn's context after /hi, without a read call"}
    change: the purpose by the Criterion of 288.1 (case 290.3)
  - slug: rule-case-protocol
    replace:
      - old: "page, loaded by `/hi` with `sprint.md` and `brief.md` (case 273.1). A session without"
        new: "page, loaded by `/hi` with `sprint.md`, `brief.md` and `glossary.md` (cases 273.1, 288.1). A session without"
    change: the Purpose names the glossary among the files /hi loads (case 290.3)
```

```tasks
- [x] update `estimate-generate-ticks-the-spec`: `set: {purpose}`
- [x] update `estimate-internal-context-loaded`: `set: {purpose}`
- [x] update `rule-case-protocol`: `replace` in the Purpose — the sentence on the files `/hi` loads
```

## Deferred

## Case 289 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b is the current milestone of the sprint: `rule-work-mode` — Work Mode, the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`; `rule-subagent-guppi` — what a subagent may do and the fork that comes back as a Case. Both are `draft` placeholders, deferred fourteen times, the last by 285. This session took the `read` line of a superseded Case (286), the `SessionStart compact` hook (287) and the review of `CLAUDE.md` — the glossary with `/hi`, the one rule in the schema, the Render cut (288) — ahead of it.

> **problem:**
> The person closes this Plan Mode with three Cases and goes to pre-spec; Slice 3b waits for the next session, the fifteenth defer. Two lines of this session bear on it: a subagent loads `CLAUDE.md` and not the glossary (288.1), and `guppi recall` brings the session's load back after a compaction (287) — the rule of Work Mode is written with both.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes on code, tests, migrations and by-hand checks in spec.md (the readings are generate's since case 270, the render and sprint lines in the form of case 279.1), the test of each Estimate written first and turned green, the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes; the first item of the next session
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; a subagent loads CLAUDE.md and no glossary (case 288.1); with rule-work-mode, the first item of the next session
```
