<!-- approved 03:03:56 · session 7e5f9a7a -->

# Spec — 2026-09-23, session 1859

## Case 383 — the Case schema names the limits of the scripts: a `replace` pair and a sub-case's `given`

> **context:**
> The agent writes a Case by `case-schema.md`, and the scripts apply it. In two places the scripts read the text more narrowly than the schema says, and the schema is silent on it. The first place is a `replace` pair: `generate` looks for `old` inside one `##` section, History excluded, and needs exactly one hit on the page; in session 1355 the anchor of Case 381 opened with the heading `## Milestones` and did not match. The second place is a sub-case's `given`: `materialize` takes it as it stands, and the parent's when it is absent; in session 1853 the sub-cases of 299 wrote "The parent's." and their own lines, a pointer the script does not resolve. Pre-spec caught both, not the schema. The two lessons are the children of `insight-workflow-case-schema-silent-on-what-the-scripts-accept`, `open`, severity 2. Every item is an `update` with a `ref`, so no vault query. No Estimate is touched: the scripts do not change, an `update` of a Render touches no Estimate of the live reading (case 378.5), and the four Estimates of `rule-case-protocol` speak of other things.

> **problem:**
> The agent learns the limits the scripts put on a `replace` pair and on a sub-case's `given` from the check, not from the schema. Should the schema state them beside the form, and the Insight close?

> **given:**
> `rule-case-protocol` — its Render is `case-schema.md`; the Case changes two sentences of it.
> **＋** `vault/wiki/case-schema.md` — the rendered file, loaded by `/hi`.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — the Insight the Case sets `actioned`.
> **＋** `lesson-generate-replace-anchor-stays-in-one-section` — its child on the `replace` pair.
> **＋** `lesson-sub-case-given-the-parents-plus-lines-has-no-form` — its child on a sub-case's `given`.
> **＋** `guppi/generate.py` `replace_hits` — the one matching rule of a pair, which pre-spec uses too.
> **＋** `guppi/materialize.py` — takes a sub-case's `given` as it stands, the parent's when it is absent.

> **when:**
> The agent writes a Case with a `replace` pair, or a sub-case with its own `given`, and reads `case-schema.md` loaded by `/hi`.

> **then:**
> `case-schema.md` says that the `old` of a pair matches inside one `##` section, never in History, a line break matching any whitespace, with exactly one hit on the page.
> **＋** `case-schema.md` says that `materialize` takes a sub-case's `given` as it stands, so a sub-case with the parent's lines and its own writes them all out.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stands `actioned` with `addressed_by: decision-case-383`.
> **＋** Both lessons go to the archive by the cascade.
> **－** `guppi/generate.py` and `guppi/materialize.py` read the text as before.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "and a mapping under `replace` is a shape `generate` rejects)"
        new: "and a mapping under `replace` is a shape `generate` rejects; an `old` matches inside one `##` section of the page — a render block is one section with its headings — never in History, a line break matching any whitespace, and hits the page once: an anchor that crosses a section heading never matches, and one that misses or hits twice fails the entry)"
      - old: "and its own `given` unless it is the parent's word for word;"
        new: "and its own `given` unless it is the parent's word for word — `materialize` takes a sub-case's `given` as it stands, so a sub-case with the parent's lines and more writes them all out, never a pointer to the parent's;"
    change: the Case schema names the limit of a replace pair and of a sub-case's given (case 383)
  - slug: insight-workflow-case-schema-silent-on-what-the-scripts-accept
    set: {status: actioned, addressed_by: decision-case-383}
    change: "actioned: the Case schema names, beside each form, the limit the scripts put on it — a replace pair inside one section, a sub-case's given taken as it stands (case 383)"
```

```tasks
- [x] update `rule-case-protocol` — two `replace` pairs
- [x] update `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — `actioned`, `addressed_by`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Case 384 — the `bashguard` refusal says it is by design

> **context:**
> `rule-bash-guard` refuses a heredoc with a backslash or with a file write and sends the agent to Write. The agent follows it, and at every Retro reports the refusal as a finding. The refusal is the behaviour the hook was made for, so these reports are noise. The message of the hook (`guppi/bashguard.py`, the function `run`) says what to do, but not that the refusal is normal. Case 382 deferred this; this Case takes it up. Three places quote the message: the How it works of `rule-bash-guard`, the Criterion of `estimate-bash-guard`, and the test; the How it works also names the log line `bashguard: <reason>`, while the code writes `bashguard refused: <reason>`. `estimate-bash-guard` stands in the shape before case 193 — a `### case 127` block, `## Context` and `## Method`, no `method` or `purpose` field — so its Criterion is replaced whole and the fields are set in the same `update`; the lines of the old Criterion on the page's creation and on the registration in `settings.json` leave it, being the bookkeeping of case 127 and not the behaviour of the hook. Every item is an `update` with a `ref`, so no vault query.

> **problem:**
> The message of the hook does not say that the refusal is legal and needs no report, so the agent takes it for an event of the session each time.

> **given:**
> `rule-bash-guard` — the rule; its How it works quotes the message.
> **＋** `estimate-bash-guard` — the Estimate of the rule; its Criterion quotes the message.
> **＋** `guppi/bashguard.py` — the function `run` prints the message, the module docstring quotes it.
> **＋** `tests/test_bashguard.py` — the tests of the refusals check the message.
> **＋** `raw/<date>/event_log.md` — the day's event log the hook writes the refusal line to.
> **＋** `/dev/null` — the one redirect target that is no file write.
> **＋** `decision-case-382` — the deferred decision the Case takes up.

> **when:**
> The agent calls `Bash`, and `uv run guppi bashguard` on `PreToolUse` reads `tool_input.command` of the payload and finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line.

> **then:**
> A body with a backslash, or a marker line that writes a file (`>` or `>>` not to `/dev/null`, `tee`), exits 2 with the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path>>. Write the script with the Write tool into the scratchpad and run it by path; change a file with Edit. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
> **＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard refused: <reason>` goes to `raw/<date>/event_log.md`.
> **＋** A `<<<` here-string, a heredoc with no backslash and no file write, a command without a heredoc, another tool — exit 0.
> **＋** A payload the hook cannot read — exit 0 with one line on stderr.
> **－** The hook never raises.

```then
update:
  - slug: rule-bash-guard
    replace:
      - old: "tool into the scratchpad and run it by path; change a file with Edit.` — which blocks"
        new: "tool into the scratchpad and run it by path; change a file with Edit. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.` — which blocks"
      - old: "one line `bashguard: <reason>` goes to `vault/raw/<date>/event_log.md`"
        new: "one line `bashguard refused: <reason>` goes to `vault/raw/<date>/event_log.md`"
    change: the refusal message says the refusal is by design and no finding for Retro; the log line named as the code writes it (case 384)
  - slug: estimate-bash-guard
    set:
      status: pending
      purpose: A heredoc with a backslash or a file write is refused before it runs, with a message that sends the agent to Write and says the refusal is no finding
      method: uv run pytest tests/test_bashguard.py; the live reading is the first refusal of a session, its message read on stderr
    change: the Criterion replaced whole — the message says the refusal is by design; recut to the shape of case 193 (case 384)
```

```tasks
- [x] update `rule-bash-guard` — two `replace` pairs, `{supersedes:case 382}`
- [x] update `estimate-bash-guard` — the Criterion replaced whole, `purpose`, `method`, `pending`
- [x] `guppi/bashguard.py` — the new sentence in the message of `run` and in the module docstring
- [x] `tests/test_bashguard.py` — the refusal test checks the new sentence
- [x] read `estimate-bash-guard`
```

## Case 385 — `addressed_by` of an `actioned` Insight takes the later of the two

> **context:**
> At synthesis the librarian hangs a new lesson as a child on an Insight of the same pattern. When the Insight stands `actioned` and the lesson entry carries `addressed_by`, case 284.4 keeps the Insight `actioned` and moves `addressed_by` to the lesson's decision. Case 361 says `addressed_by` is one link, the latest. The rule was written for a lesson of a later session, whose decision is then the latest. Session 1355 went otherwise: Case 378.5 closed `insight-workflow-contract-change-leaves-its-derived-text-stale`, and a lesson of the same session carried the mark of 378.4. The librarian followed 284.4 word for word and moved the field to the earlier 378.4, so the two rules parted. It is a judgment of the librarian, not code: `materialize` only puts `addressed_by` on the lesson entry. The Criterion of `estimate-synthesis-keeps-actioned-by-the-mark` speaks of the move, so it is replaced whole; it stands `pending` already. Every item is an `update` with a `ref`, so no vault query.

> **problem:**
> Where does `addressed_by` of an `actioned` Insight point when the new lesson's decision is earlier than the one in the field: at the latest decision (case 361) or at the lesson's decision (case 284.4)?

> **given:**
> `rule-synthesis` — its Render tells the librarian to move `addressed_by` (case 284.4).
> **＋** `.claude/agents/librarian-guppi.md` — the file `rule-synthesis` renders into.
> **＋** `rule-insights-schema` — its Render says one link, the latest (361), and describes the move of 284.4.
> **＋** `vault/wiki/insights/schema.yaml` — the file `rule-insights-schema` renders into.
> **＋** `estimate-synthesis-keeps-actioned-by-the-mark` — the Estimate of `rule-synthesis`; its Criterion speaks of the move.
> **＋** `insight-workflow-contract-change-leaves-its-derived-text-stale` — the Insight whose field went to the earlier decision.
> **＋** `decision-case-M` — the decision the Insight's `addressed_by` names before the synthesis.

> **when:**
> The librarian, at synthesis, hangs a lesson whose entry carries `addressed_by: decision-case-N` on an existing Insight of the same pattern that stands `actioned` with `addressed_by: decision-case-M`.

> **then:**
> When case N is later than case M — compared number by number, `378.5` after `378.4` — the `update` carries `set: {addressed_by: decision-case-N}`, and `status` stays `actioned`.
> **＋** When case N is not later than M, the `update` carries no `addressed_by`: the field stays `decision-case-M`, and `status` stays `actioned`.
> **＋** Either way the `update` carries `children` plus the lesson; the lesson is `clustered`, the cascade archives it, and the brief reports the pair beside the synthesis.
> **＋** An Insight born from a marked lesson gets, right after its `create`, an `update` with `set: {status: actioned, addressed_by: decision-case-N}` (302.2).
> **＋** A lesson with no `addressed_by` sets an `actioned` Insight `open` with `set: {status: open}`, and a new Insight is born `open`.
> **－** `addressed_by` never names two decisions.

```then
update:
  - slug: rule-synthesis
    replace:
      - old: "the Case of this unit that closed its cause, the pair reported in the brief beside the synthesis (case 284.4)"
        new: "the Case of this unit that closed its cause, and case N is later than the case the Insight's `addressed_by` names — compared number by number, `378.5` after `378.4`; when it is not later, the `update` carries no `addressed_by` and the field stands (case 385); the pair reported in the brief beside the synthesis (case 284.4)"
    change: addressed_by moves to the lesson's decision only when it is the later case (case 385)
  - slug: rule-insights-schema
    replace:
      - old: "Then the Insight stays `actioned`, `addressed_by` moves to that decision, the Lesson becomes a child"
        new: "Then the Insight stays `actioned`, `addressed_by` moves to that decision when its case is later than the one the field names, and stands otherwise — one link, the latest (cases 361, 385) — the Lesson becomes a child"
    change: the move of addressed_by only to a later case (case 385)
  - slug: estimate-synthesis-keeps-actioned-by-the-mark
    set:
      status: pending
      purpose: An Insight stays or is born actioned by the mark — an existing actioned Insight keeps its status and takes the later of the two addressed_by; a new Insight from a marked lesson is set actioned right after its create
    change: the Criterion replaced whole — addressed_by takes the later case (case 385)
  - slug: insight-workflow-contract-change-leaves-its-derived-text-stale
    set: {addressed_by: decision-case-378.5}
    change: addressed_by back to the later case, decision-case-378.5 (case 385)
```

```tasks
- [x] update `rule-synthesis` — one `replace` pair
- [x] update `rule-insights-schema` — one `replace` pair
- [x] update `estimate-synthesis-keeps-actioned-by-the-mark` — the Criterion replaced whole, `purpose`, `pending`
- [x] update `insight-workflow-contract-change-leaves-its-derived-text-stale` — `addressed_by: decision-case-378.5`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
- [ ] read `estimate-synthesis-keeps-actioned-by-the-mark`
```

## Case 386 — `guppi sprint` puts a blank line after every milestone heading

> **context:**
> `guppi sprint` writes `sprint.md` from the page `entity-sprint-migration`. The current milestone comes out whole; a closed one and a later one as one heading line. After a whole block `render_milestones` puts a blank line; after a collapsed line it puts none, so two collapsed headings stand back to back, as Slice 4 and Slice 5 do now. Markdown reads them anyway, but every other heading of the file stands between blank lines. Only `sprint_id` in `guppi/materialize.py` reads the file by code, and it needs the first `## ` line, so the change does not touch it. `tests/test_sprint.py` fixes the lines back to back: `EXPECTED` and two assertions. The Criterion of `estimate-sprint-renders-the-backlog` describes the layout of the file, so it is replaced whole; the other four Estimates of `rule-sprint` speak of `--check`, the ticks in the Spec and the moves of milestones, and are left alone. The `update` carries a `ref`, so no vault query.

> **problem:**
> The collapsed milestone headings in `sprint.md` stand with no blank line between them, while every other heading of the file is set off by blank lines.

> **given:**
> `guppi/sprint.py` `render_milestones` — writes the milestone lines; the module docstring describes the file.
> **＋** `tests/test_sprint.py` — fixes the render on a temp vault.
> **＋** `estimate-sprint-renders-the-backlog` — the Estimate of `rule-sprint`; its Criterion describes the file.
> **＋** `rule-sprint` — the rule, `governs: vault/wiki/sprint.md`.
> **＋** `entity-sprint-<id>` — the one live sprint page the script reads, `entity-sprint-migration` today.
> **＋** `vault/wiki/sprint.md` — the file the script writes.

> **when:**
> `guppi sprint` runs with a live page `entity-sprint-<id>` and reads its `estimates`, `## Purpose`, `## Milestones`, `## Backlog` and `## Closed`.

> **then:**
> The file: `# Sprint`; `## <id>`; Purpose; `**Done when**`, one line per Estimate; then `## Milestones`: a closed milestone as one line `### [x] <name>`; the current one as the heading `### [ ] <name>` and each item with its status and `deferred_by`; each later one as one line `### [ ] <name> — N items: ` and its items separated by commas — an item with a wikilink as `[[slug]]`, an item without one by its text, no tick and no status; then `## Backlog`, each item a line; then `## Closed` as it is.
> **＋** Every heading of the file stands between blank lines: a blank line follows each `### ` line, collapsed or whole.
> **＋** An item is ticked by the statuses of every page its `[[slug]]` before the first ` — ` names — `[x]` when each is `built`, `passed` or `archived`, the statuses after ` · ` in the order of the slugs; a wikilink after the ` — ` is text; a line with no wikilink before the ` — ` is a note, `- [ ] <text>`, never ticked, keeping its milestone open.
> **＋** A milestone is closed when every item is `[x]`; with no item it is open.
> **－** A slug with no live or archived page: one line on stderr, exit 1, the file not written; `--check` compares this same render.
> **－** The script writes no page of `wiki/`, `entity-sprint-<id>` included.

```then
update:
  - slug: estimate-sprint-renders-the-backlog
    set: {status: pending}
    change: the Criterion replaced whole — a blank line after every milestone heading (case 386)
```

```tasks
- [x] `guppi/sprint.py` — a blank line after each collapsed heading in `render_milestones`; the sentence in the docstring
- [x] `tests/test_sprint.py` — `EXPECTED` and the two assertions with a blank line between headings
- [x] update `estimate-sprint-renders-the-backlog` — the Criterion replaced whole, `pending`
- [x] `uv run guppi sprint`
- [ ] read `estimate-sprint-renders-the-backlog`
```

## Case 387 — the re-showing by a ratified copy: `given`, `when`, `then` in English, the Spec written by a hook

> **context:**
> Today the agent writes each ratified Case into the plan file itself, in the reply with its ledger lines, and translates the whole Case into English. When a signed Case changes later — the person's change, a finding of pre-spec, a change of the model — the agent shows it again whole: `given`, `when`, `then`, `tasks` and `ratification`, even for a change of one word; in session 1355 a change of the model made three Cases signed again this way. Also, the English the vault receives is the agent's translation, which nobody compares with the signed text, and `when` and `then` become the Criterion of an Estimate word for word. The vault (ask-guppi): no rule covers a Spec written by a hook or a reconciliation; `rule-case-protocol` (`draft`) says the agent writes the Spec and a re-showing is always whole; `rule-language` (`built`) says Russian in all sections; `rule-prespec` (`draft`) checks the plan against the ledger lines, not against a copy; `rule-hook-registry` takes the registration of a hook in the Case that creates its rule; `rule-spec-write` and `rule-spec-reconcile` are free. `estimate-language-followed` is replaced, since it asks for Russian in all sections; `estimate-case-protocol-loaded` and `estimate-hook-registry-rendered` are not touched — an `update` of a Render touches no Estimate of the live reading (case 378.5); `estimate-case-protocol-case-form` speaks of the chat form, not of its language or of who writes the Spec. The re-showing in Work Mode stays as it is: the Spec there is `spec.md`, not the plan file.

> **problem:**
> A small change of a signed Case costs a whole re-showing, and the English the vault receives is a translation nobody compares with what was signed.

### Case 387.1 — the language: `given`, `when`, `then` and `tasks` in English in the chat

> **given:**
> `rule-language` — the Render of its Language section stands in `CLAUDE.md`.
> **＋** `rule-case-protocol` — the Language section of its Render in `vault/wiki/case-schema.md`.
> **＋** `estimate-language-followed` — the Estimate of `rule-language`; its Criterion speaks of the language of the chat.
> **＋** `CLAUDE.md` — loaded in every session.
> **＋** `vault/wiki/case-schema.md` — loaded by `/hi`.

> **when:**
> A session starts with `CLAUDE.md`, and the agent writes into the repository or into the chat.

> **then:**
> Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the approved Spec — is English.
> **＋** The chat with the owner is Russian: the name of a Case, its `context`, `problem` and `recommend`, and the agent's own text.
> **＋** A Case's `given`, `when`, `then` and `tasks` — lines and sub-points — are English in the chat and enter the Spec unchanged.
> **＋** The name, `context` and `problem` are translated into English in the Spec before its approval.
> **＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language; English technical terms are not transliterated into Cyrillic.
> **－** The rule speaks of the language, not of the Case form — the form is `vault/wiki/case-schema.md`.

```then
update:
  - slug: rule-language
    replace:
      - old: "A Case is discussed in Russian and enters the Spec in English (case 123);"
        new: "A Case is discussed in Russian, its `given`, `when`, `then` and `tasks` written in English in the chat (cases 123, 387.1);"
      - old: "Russian for chat with the owner: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English."
        new: "Russian for chat with the owner: the name of a Case, its `context`, `problem` and `recommend` are Russian in the chat and are translated into English in the Spec before its approval; its `given`, `when`, `then` and `tasks` are English in the chat, the words that enter the Spec and the vault unchanged."
    set:
      purpose: Keeps the repository in English and the chat with the owner in Russian, a Case's given, when, then and tasks English in the chat, with slugs, paths and quotations unchanged in either
    change: a Case's given, when, then and tasks are English in the chat (case 387.1)
  - slug: rule-case-protocol
    replace:
      - old: "Russian in the chat with the owner: a Case is discussed there in Russian, all its sections. English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Case enters the Spec translated, its slugs, field names and ledger lines unchanged (case 123)."
        new: "Russian in the chat with the owner for the name of a Case, its `context`, `problem` and `recommend`, and the agent's own text; `given`, `when`, `then` and `tasks` — lines and sub-points — are English in the chat already, the words the vault will hold (case 387.1). English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the name, `context` and `problem` are translated in the Spec before its approval, slugs, field names and ledger lines unchanged (cases 123, 387.1)."
    change: the language of the Case sections in the chat (case 387.1)
  - slug: estimate-language-followed
    set: {status: pending}
    change: the Criterion replaced whole — given, when, then and tasks English in the chat (case 387.1)
```

```tasks
- [x] update `rule-language` — two `replace` pairs and `purpose`
- [x] update `rule-case-protocol` — one `replace` pair
- [x] update `estimate-language-followed` — the Criterion replaced whole, `pending`
- [x] `uv run guppi render`: `CLAUDE.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-language-followed`
```

### Case 387.2 — a hook writes the ratified Case into the Spec and the ratified copy

> **given:**
> `rule-spec-write` — the new hook rule, a child of `rule-plan-mode`.
> **＋** `estimate-spec-write-copies-the-ratified-case` — its Estimate.
> **＋** `guppi/ratified.py` — the module of the hook; `tests/test_ratified.py` — its tests.
> **＋** `<plan>.ratified.md` — the ratified copy beside the plan file, outside the repository.
> **＋** `rule-case-protocol` — its Render says who writes the Spec and which chat form the scripts read.
> **＋** `rule-hook-registry` — the Render of the `"hooks"` key of `.claude/settings.json`.
> **＋** `guppi/gate.py` `plan_path` — finds the session's plan file by the event log.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads the session's transcript and finds the last earlier reply that shows `## Case N —` whole.

> **then:**
> The hook writes that Case into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `given`, `when` and `then` as they stand in the chat; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points.
> **＋** It writes the same text the same way into the ratified copy `<plan>.ratified.md` beside the plan file.
> **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span or a fenced block under the sub-point.
> **＋** `recommend` and `ratification` are not written.
> **＋** When the last showing of Case N is a `DIFF` block, not the Case whole, the hook writes nothing for it.
> **＋** No plan file in the event log, no showing of Case N, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **－** A Case whose lines are all `defer` is not written by the hook: the agent appends it under `## Deferred`, as before.

```then
create:
  - slug: rule-spec-write
    type: rule
    kind: Leaf
    enforcement: hook
    implementation_ref: [guppi/ratified.py, tests/test_ratified.py, .claude/settings.json]
    purpose: Prevents a ratified Case from entering the Spec in other words than the ones the person signed
    tags: [hooks, harness, workflow, session]
    sections:
      Purpose: |
        Prevents a ratified Case from entering the Spec in other words than the ones the person signed. Until case 387 the agent wrote each Case into the plan file itself, translated from the chat, and nobody compared the two. Now `given`, `when`, `then` and `tasks` are English in the chat, and a hook copies them.
      How it works: |
        `uv run guppi ratified` on `Stop`. After a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`, it reads the session's transcript, finds the last earlier reply that shows `## Case N —` whole, and writes that Case into the plan file named by `gate.plan_path` and into the ratified copy `<plan>.ratified.md` beside it, outside the repository: the heading, `context`, `problem`, `given`, `when` and `then` as they stand, a block tagged `then` built from the sub-points of `tasks`, and a block tagged `tasks` of the task lines without their sub-points; the section of Case N is replaced when it stands, appended otherwise. A last showing that is a `DIFF` block writes nothing. No plan file, no showing, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0. A defer-only Case is the agent's, under `## Deferred`.
  - slug: estimate-spec-write-copies-the-ratified-case
    type: estimate
    ref: rule-spec-write
    kind: QA
    purpose: The ratified Case enters the plan file and its ratified copy in the words of the chat, the then block built from the sub-points
    method: uv run pytest tests/test_ratified.py -k write; the live reading by hand, the plan file and its ratified copy after the first ratification of a session
    tags: [hooks, harness, workflow]
update:
  - slug: rule-case-protocol
    replace:
      - old: "**The Spec is written as each Case is ratified**, into the plan file, in the reply that carries the Case's ledger lines:"
        new: "**The Spec is written as each Case is ratified**, by the `Stop` hook of `rule-spec-write`, after the reply that carries the Case's ledger lines: it copies the Case from the reply that showed it into the plan file and into the ratified copy `<plan>.ratified.md` beside it, outside the repository; the agent creates the plan file with its title line before the first Case of the session (case 387.2). The Case holds"
      - old: "and the scripts read nothing of the chat form (case 159)."
        new: "and the hook of `rule-spec-write` reads the chat form: a task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block, its sub-points its keys — `old` and `new` in pairs, `reword old` and `reword new`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, with as many backticks as the value needs, or a fenced block under the sub-point; a Case off this form is not written, and the hook says why (cases 159, 387.2)."
    change: the Spec is written by the hook of rule-spec-write, which reads the chat form (case 387.2)
  - slug: rule-hook-registry
    replace:
      - old: '"command": "uv run guppi ledger", "timeout": 30 } ] }'
        new: '"command": "uv run guppi ledger", "timeout": 30 }, { "type": "command", "command": "uv run guppi ratified", "timeout": 30 } ] }'
    change: guppi ratified registered on Stop beside guppi ledger (case 387.2)
```

```tasks
- [x] create `rule-spec-write`
- [x] create `estimate-spec-write-copies-the-ratified-case`
- [x] update `rule-case-protocol` — two `replace` pairs
- [x] update `rule-hook-registry` — one `replace` pair
- [x] `guppi/ratified.py` — the `Stop` writer: find the showing, read the sub-points, write the plan file and the ratified copy
- [x] `guppi/cli.py` — the command `ratified`
- [x] `tests/test_ratified.py` — the write, the section replaced, a `DIFF` and a defer skipped, exit 2 without a plan file
- [x] `uv run guppi render`: `.claude/settings.json`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-spec-write-copies-the-ratified-case`
```

### Case 387.3 — the reconciliation on an edit of a ratified Case

> **given:**
> `rule-spec-reconcile` — the new hook rule, a child of `rule-plan-mode`.
> **＋** `estimate-spec-reconcile-shows-a-changed-case` — its Estimate.
> **＋** `guppi/ratified.py` — one comparison function for the edit hook, `Stop` and pre-spec; `tests/test_ratified.py` — its tests.
> **＋** `<plan>.ratified.md` — the ratified copy 387.2 writes.
> **＋** `rule-case-protocol` — the `ratification` row of its Render says when a Case is shown again.
> **＋** `rule-hook-registry` — the Render of the `"hooks"` key.

> **when:**
> The agent edits the plan file with `Edit`, `Write` or `MultiEdit`, and `uv run guppi ratified --edit` on `PostToolUse` compares each Case of the ratified copy with its section in the plan file; then the `Stop` hook `uv run guppi ratified`, after the write of 387.2 in the same run, reads the first reply after the edit.

> **then:**
> The compared parts are the ids of the Case and its sub-cases, `given`, `when`, `then`, the `then` block and the `tasks` block, byte for byte once the line ends are made the same; the name, `context` and `problem` are not compared.
> **＋** A Case whose compared parts differ: `additionalContext` names the parts and tells the agent to show the Case whole for ratification; the hook marks Case N as waiting for its showing.
> **＋** A Case whose name, `context` or `problem` alone differ: no message and no mark.
> **＋** At `Stop`, a marked Case that the reply does not show whole: exit 2 with the reason; the mark is cleared either way, so a later reply — an answer to a question of the person — is not refused; on the re-fire (`stop_hook_active`) exit 0.
> **－** An edit of another file, or of the plan file outside a ratified Case — its title, `## Deferred` — is not compared.
> **－** A Case not yet in the ratified copy is not compared.

```then
create:
  - slug: rule-spec-reconcile
    type: rule
    kind: Leaf
    enforcement: hook
    implementation_ref: [guppi/ratified.py, tests/test_ratified.py, .claude/settings.json]
    purpose: Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again
    tags: [hooks, harness, workflow, session]
    sections:
      Purpose: |
        Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again. The prose of a Case — its name, `context` and `problem` — is Russian in the ratified copy and English in the approved Spec, so it is not compared; everything the scripts apply is.
      How it works: |
        `uv run guppi ratified --edit` on `PostToolUse` of `Edit`, `Write` and `MultiEdit` on the plan file: it compares each Case of the ratified copy `<plan>.ratified.md` with its section in the plan — the ids, `given`, `when`, `then`, the `then` block and the `tasks` block — and, for a Case whose parts differ, returns them in `additionalContext` with the order to show the Case whole, and marks the Case as waiting for its showing; a change of the name, `context` or `problem` alone gets no message and no mark. `uv run guppi ratified` on `Stop`, after its write, exits 2 when a marked Case is not shown whole in the reply, and clears the mark either way; on the re-fire (`stop_hook_active`) exit 0. The comparison is one function of `guppi/ratified.py`; `guppi prespec --check` imports it.
  - slug: estimate-spec-reconcile-shows-a-changed-case
    type: estimate
    ref: rule-spec-reconcile
    kind: QA
    purpose: An edit of a ratified Case that changes what the scripts apply is shown whole in the first reply after it
    method: uv run pytest tests/test_ratified.py -k reconcile; the live reading by hand, the first edit of a ratified Case in a session
    tags: [hooks, harness, workflow]
update:
  - slug: rule-case-protocol
    replace:
      - old: "is shown again: `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and no `recommend` (cases 62, 163); until it is ratified again, nothing of the change is written or acted on; the translation of a Case into the Spec is no change (case 373)."
        new: "is shown again. A Case not yet ratified is shown again whole. A ratified Case is, in Plan Mode, changed in the plan file first, and `rule-spec-reconcile` compares it with the ratified copy: when its `given`, `when`, `then`, `then` block or `tasks` changed, it is shown again — `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and no `recommend` (cases 62, 163); until it is ratified again, nothing of the change is acted on. When only its name, `context` or `problem` changed, the reply shows the change as a `DIFF` of the edit and asks for no ratification; the translation of the name, `context` and `problem` before the approval is no change and is not shown (cases 373, 387.3). In Work Mode a changed Case is shown again whole."
    change: a ratified Case is shown whole again when what the scripts apply changed, as a DIFF when only its prose changed (case 387.3)
  - slug: rule-hook-registry
    replace:
      - old: '"command": "uv run guppi spec", "timeout": 30 } ] }'
        new: '"command": "uv run guppi spec", "timeout": 30 } ] }, { "matcher": "Edit|Write|MultiEdit", "hooks": [ { "type": "command", "command": "uv run guppi ratified --edit", "timeout": 30 } ] }'
    change: guppi ratified --edit registered on PostToolUse of Edit, Write and MultiEdit (case 387.3)
```

```tasks
- [x] create `rule-spec-reconcile`
- [x] create `estimate-spec-reconcile-shows-a-changed-case`
- [x] update `rule-case-protocol` — one `replace` pair
- [x] update `rule-hook-registry` — one `replace` pair
- [x] `guppi/ratified.py` — the comparison function, `--edit` with the mark, and the check at `Stop` after the write
- [x] `tests/test_ratified.py` — blocks changed → show whole and the mark; prose only → silence; `Stop` without the showing → exit 2 and the mark cleared; the next reply → 0; the re-fire → 0
- [x] `uv run guppi render`: `.claude/settings.json`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-spec-reconcile-shows-a-changed-case`
```

### Case 387.4 — pre-spec checks the plan against the ratified copy and finds untranslated prose

> **given:**
> `rule-prespec` — its Render is `.claude/skills/pre-spec/SKILL.md`.
> **＋** `estimate-prespec-checks-the-ratified-copy` — the new Estimate of `rule-prespec`.
> **＋** `guppi/prespec.py` — `--check`; `tests/test_prespec.py` — its tests.
> **＋** `guppi/ratified.py` — the comparison function `--check` imports.
> **＋** `<plan>.ratified.md` — the ratified copy beside the plan file.

> **when:**
> `guppi prespec --check <plan>` runs at `/pre-spec`, after the agent translated the names, `context` and `problem` of the plan, and reads the plan and its ratified copy `<plan>.ratified.md`.

> **then:**
> A Case of the plan whose ids, `given`, `when`, `then`, `then` block or `tasks` differ from its section in the ratified copy: one finding naming the Case and the parts.
> **＋** A Case of the plan with no section in the copy, and a section of the copy with no Case in the plan: one finding each.
> **＋** A name, `context` or `problem` that still holds a Cyrillic letter: one finding.
> **－** The section of a Case a `{supersedes:case N}` of the session's window names is no finding: that Case left the plan (case 299.1).
> **－** A Case under `## Deferred` is not compared.

```then
create:
  - slug: estimate-prespec-checks-the-ratified-copy
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: Pre-spec finds a Case of the plan that differs from its ratified copy in what the scripts apply, or whose prose is still Russian
    method: uv run pytest tests/test_prespec.py -k ratified
    tags: [session, workflow, harness]
update:
  - slug: rule-prespec
    replace:
      - old: "It also prints a line opening with `note:`"
        new: "It also prints one line for every Case of the plan whose ids, `given`, `when`, `then`, `then` block or `tasks` differ from its section in the ratified copy `<plan>.ratified.md` beside the plan file, for every Case of the plan with no section there and every section there with no Case in the plan — a Case a `{supersedes:case N}` of the window names excepted, and the Cases under `## Deferred` not compared — and for every name, `context` or `problem` still holding a Cyrillic letter: translate them before you run it (case 387.4). It also prints a line opening with `note:`"
    change: pre-spec checks the plan against its ratified copy and finds untranslated prose (case 387.4)
```

```tasks
- [x] update `rule-prespec` — one `replace` pair
- [x] create `estimate-prespec-checks-the-ratified-copy`
- [x] `guppi/prespec.py` — the findings on the copy and on Cyrillic, the comparison from `guppi/ratified.py`; the line in the docstring
- [x] `tests/test_prespec.py` — a difference, a missing section, Cyrillic, a supersede
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-checks-the-ratified-copy`
```

## Case 388 — pre-spec: ask-guppi reads the plan itself, the agent answers with one report

> **context:**
> The agent writes bookkeeping facts into a `context` — a page's status, a count, a case number, "no page holds this" — from memory or from a narrow search, and they can be wrong. Both live lessons of the Insight `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` are about a `context`: Case 363 and Case 378. Ask-guppi found both at pre-spec, though it was not told to read the `context`. The text rule of `rule-agent-writing` (case 359) does not hold the facts in memory. Case 380 deferred the Insight; this Case takes it up. Also, before dispatching ask-guppi the agent writes a list of the decisions (cases 198, 203.2): a copy of the plan written by hand, while ask-guppi can read the plan and the pages itself; only the slugs of the deferred decisions are needed, for case 186.2. At the pre-spec of this session the agent, on its own, answered the findings with one report — each finding numbered, the fix it proposed or why it was known, and two decisions for the person — before it showed the changed Cases; the person found the step right and asked for it to be written; the skill does not hold it. The translation step 387.4 adds belongs to this Criterion too. The Criterion of `estimate-prespec-reconciles` describes the steps of the skill and is replaced whole. Every item is an `update` with a `ref`.

> **problem:**
> Is the text rule enough against facts wider than their check, or is a check due — and where?

> **given:**
> `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — the Insight the Case sets `actioned`.
> **＋** `lesson-case-context-claim-wider-than-its-search` — its live child.
> **＋** `lesson-case-context-bookkeeping-written-from-memory` — its live child.
> **＋** `rule-prespec` — its Render is `.claude/skills/pre-spec/SKILL.md`, which dispatches `ask-guppi`.
> **＋** `estimate-prespec-reconciles` — the Estimate of the steps of that skill.
> **＋** `rule-agent-writing` — the text rule in `CLAUDE.md`: a claim no wider than its check.

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved.

> **then:**
> The agent translates the name, `context` and `problem` of every Case of the plan into English, then runs `guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; it fixes the plan, the frontier or the line for every finding until the command prints no finding.
> **＋** `ask-guppi` is dispatched once with the absolute path of the plan file and the instruction to read every Case outside `## Deferred` — `context`, `when`, `then`, the `then` block — and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
> **＋** Three questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out.
> **＋** The agent answers the findings with one report before any Case is shown again: each finding numbered, with the fix it proposes or why it is already known, and the decisions it needs from the person.
> **＋** Then the changed Cases are shown again in one reply; a wrong fact of a `context` is fixed in the plan as a change of prose.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call; then Plan Mode exits again.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

```then
update:
  - slug: rule-prespec
    replace:
      - old: "List every decision ratified in this Plan Mode, one line each: slug — decision type — `purpose` for a `create`, an `update` and a `delete`, a `defer` by its slug and the word `defer` alone (case 198); for an `update` of a rule or an entity, add the page's `estimates` and which of them the Case names by slug — `ask-guppi` is asked whether an Estimate the Case does not name speaks of the thing the Case changes; one that does is a finding (case 203.2). Dispatch the `ask-guppi` agent once with that list, the absolute path of the plan file, the instruction to read for every Case there outside the `## Deferred` heading its `when` and `then` sections and its `then` block — `replace` old and new, `set`, `sections` — before judging a page, so that a finding can name a wrong wording or a wrong place, and two questions: which of these contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes. A deferred decision enters the list by its slug and the word `defer` alone, without its `purpose`, and its body is not read: the session that takes the defer up judges it with its own pre-spec."
        new: "Dispatch the `ask-guppi` agent once with the absolute path of the plan file and the instruction to read for every Case there outside the `## Deferred` heading its `context`, its `when` and `then` sections and its `then` block — `replace` old and new, `set`, `sections` — and, for an `update` of a rule or an entity, the page's `estimates`, before judging a page, so that a finding can name a wrong wording or a wrong place, and of a Case under `## Deferred` only the slugs of its `defer` items; the agent writes no list of the decisions — the plan is the list (case 388). Three questions: which of these contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes — one that does is a finding (case 203.2); which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out (case 388). Answer the findings with one report before any Case is shown again: each finding numbered, with the fix you propose or why it is already known, and the decisions you need from the person; then show the changed Cases again in one reply (case 388). A wrong fact of a `context` is fixed in the plan as a change of prose. The body of a Case under `## Deferred` is not read: the session that takes the defer up judges it with its own pre-spec."
    change: ask-guppi reads the plan and the context itself; the agent answers the findings with one report before any Case is shown again (case 388)
  - slug: estimate-prespec-reconciles
    set: {status: pending}
    change: the Criterion replaced whole — the translation, ask-guppi reading the plan and the context, the report before the re-showing (case 388)
  - slug: insight-workflow-fact-signed-from-a-check-that-does-not-cover-it
    set: {status: actioned, addressed_by: decision-case-388}
    change: "actioned: a fact of a context is checked by ask-guppi at pre-spec; the text rule of rule-agent-writing stays (case 388)"
```

```tasks
- [x] update `rule-prespec` — one `replace` pair
- [x] update `estimate-prespec-reconciles` — the Criterion replaced whole, `pending`
- [x] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — `actioned`, `addressed_by`, `{supersedes:case 380}`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-reconciles`
```

## Deferred

## Case 389 — the acknowledging reply of a re-ratification carries its LEDGER block again

> **context:**
> By Case 387.2 the `Stop` hook of `rule-spec-write` writes a Case into the Spec only after a reply whose `LEDGER` block holds that Case's decision lines. At the re-ratification of Cases 384–388 in session 1859 the agent wrote no `LEDGER` block: the lines were the same, and the ledger hook skips a line it already holds. With the hook live, that re-ratification would not have reached the Spec. The Case schema does not say that the acknowledging reply of a re-ratification carries the `LEDGER` block again.

> **problem:**
> A re-ratified Case can stay out of the Spec, because the schema lets the acknowledging reply of a re-ratification go without its `LEDGER` block.

```then
defer:
  - slug: rule-case-protocol
    type: rule
    purpose: The acknowledging reply of a re-ratification carries the LEDGER block with the Case's lines again, so the hook of rule-spec-write writes it
```
