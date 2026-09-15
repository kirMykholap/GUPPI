<!-- approved 11:40:48 · session 19037d1c -->

# Spec — session N, 2026-09-14, hi 10:29

## Work without a decision

F3, F11, F12 of the Frontier: no Case, no ledger `decision` line; the readings are written as `estimate[...]` lines the moment they exist.

```tasks
- [x] F3: read `estimate-git-context-current` (block 115) at this `/hi`: `Render:` present after `Pull:`, empty on a clean tree
- [x] F3: read `estimate-documentation-completes` (block 100.2) against the librarian's run of session M
- [x] F3: read `estimate-event-log-records` (block 111.1): `- 10:29:12 19037d1c hi` is in the log; the half "a repeated `/hi` adds no line" waits for a second `/hi` of this session
- [x] F3: read `estimate-ledger-write-lifts` (blocks 111.3, 111.6) when the hook writes this session's lines into `raw/2026-09-14/1029/ledger.md` — passed at 10:5x, the lines of 10:32, 10:43, 10:51 in the folder of the stamped `hi`
```

## Case 123 — the language of a Case in the chat and in the Spec

> **context:**
> `## Language` of `CLAUDE.md` (the Render of `rule-claude-md`, lines 71–75) says: English for everything written into the repository; Russian for chat with the owner "and for the plan he reads in order to approve it". `case-schema.md` `## Language` says: Russian in the chat with the owner, English in everything that lands in the vault. In session M Case 115 was discussed in the chat in English and the Spec was written in English. Today Case 122 went the same way.

> **problem:**
> The rule does not say in which language a Case is discussed in the chat. The agent reads "the plan in Russian" as leave to write the Case in English, because the Case is the plan to come. The Spec is English in practice, and that is right: it lands in `raw/` and in the vault.

> **given:**
> `rule-claude-md` (`MOC`, `built`, `render_mode: full`, `governs: CLAUDE.md`, `estimate-claude-md-rendered` `passed`): the `## Language` section is three sentences inside the Render markers, so the change is a `replace` of the three (a `sections` entry would add a second `## Language` outside the Render — pre-task finding 1 of case 132), and `guppi render` carries it into `CLAUDE.md`.
> **＋** `case-schema.md` is a Rule-class file: an `update` with `file` and `change`, applied by hand in Work Mode; its `## Language` (line 29) is one sentence.
> **＋** `rule-case-protocol` is not touched: the form of a Case does not change, only its language.
> **＋** The Spec of session M (`raw/2026-09-14/0747/spec.md`) is already English; the practice of the Spec does not change.
> **－** Ledger lines, slugs, field and section names (`context`, `given`, `then`), paths and quotations from pages stay English in either language.
> **－** The Frontier line F13 closes on this Case.

> **when:**
> The agent writes a Case in the chat, or carries a ratified Case into the Spec, or reads `CLAUDE.md` and `case-schema.md`.

> **then:**
> `## Language` of `rule-claude-md` reads: "English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. Russian for chat with the owner: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. English technical terms are not transliterated into Cyrillic."
> **＋** `## Language` of `case-schema.md` reads: "Short sentences. One idea per sentence. Active voice. A common word over a term. Russian in the chat with the owner: a Case is discussed there in Russian, all its sections. English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Case enters the Spec translated, its slugs, field names and ledger lines unchanged."
> **＋** `CLAUDE.md` after `guppi render` carries the new section; the reading of `estimate-claude-md-rendered` is a Work Mode task.
> **－** `rule-claude-md` is a MOC with no Estimate of its own behaviour; no `contract` is written.

```then
update:
  - slug: rule-claude-md
    replace:
      - old: "English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents. Russian for chat with the owner, and for the plan he reads in order to approve it. English technical terms are not transliterated into Cyrillic."
        new: "English for everything written into the repository: code, identifiers, comments, pages, commit messages, documents — the Spec included. Russian for chat with the owner: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English. Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language. English technical terms are not transliterated into Cyrillic."
    change: a Case is discussed in the chat in Russian and enters the Spec in English; the plan the owner approves is the Spec (case 123)
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "Language: a Case is discussed in the chat in Russian, all its sections, and enters the Spec translated into English, its slugs, field names and ledger lines unchanged (case 123)"
```

```tasks
- [x] `vault/wiki/case-schema.md` `## Language`, by hand (123): the paragraph of the `then` above
- [ ] `uv run guppi render --sync` after the librarian's `generate`, or `make lint` `render --check` at the close: `CLAUDE.md` `## Language` carries the new text
- [ ] read `estimate-claude-md-rendered` against the rendered `CLAUDE.md`
```

## Case 122 — the ledger lines of a reply that ends in a tool call

> **context:**
> Four lessons on one writer: `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (F), `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (I, archived), `lesson-transcript-omits-text-emitted-before-tool-calls` (L) and `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live` (M). The `Stop` hook reads the final text of a turn; a reply that ends in `Skill`, `ExitPlanMode` or any tool call has no `Stop` and its text is not in the transcript. The Insight's Proposal has stood unactioned since session I. (Case 117 as it stands.)

> **problem:**
> The rule "a reply with ledger lines ends in text" lives in the agent's memory only, and the agent broke it with the lesson live. Either the hook reaches those lines — a `PreToolUse` hook on `Skill|ExitPlanMode` that reads the reply under way, if the payload carries it — or the harness makes the agent's rule mechanical: `CLAUDE.md` says it, and `guppi gate` refuses a `Skill` call while the reply holds an unwritten `LEDGER` block. Which of the two is measurable is a Plan Mode of its own. (Case 117 as it stands.)

> **given:**
> Measured in session N at 10:4x: a text emitted before a `Bash` call in the same reply is absent from `~/.claude/projects/…/19037d1c….jsonl` — the assistant records around it are `thinking` and `tool_use` only — and session M's transcript holds no assistant text between the owner's «ратифицирую» (record 650) and the `Skill` call of `/pre-task` (679): the block of 115 and 116 was never persisted. A `PreToolUse` payload carries `tool_name`, `tool_input`, `transcript_path`, no reply text. The question of the Insight's Proposal is settled: absent, not dropped.
> **＋** `rule-ledger-write` (`Leaf`, `draft`, `estimate-ledger-write-lifts` `pending` on blocks 111.3, 111.6): "a reply that ended in a tool call reaches the ledger at the next `Stop` of the session" — true only when the agent repeats the block. `deferred_by: [decision-case-117]`.
> **＋** `guppi gate` (`rule-retro-commit`, `built`) already runs on `PreToolUse` with the matcher `Skill` and refuses `/handoff` on a dirty tree; `.claude/settings.json` needs no change, `rule-hook-registry` is not touched.
> **＋** `guppi pretask --check` already finds "item […] has no decision line" (`pretask.check_lines`, `window_lines`, `session_decisions`, `split_cases`, `then_blocks`); the gate reuses them and reports only that half. `rule-pretask` is not changed: the check at `/pre-task` stays as it is.
> **＋** The plan file is in no payload; the event log holds `tool Write:` / `tool Edit:` lines with the full path (`- 07:52:53 fde37e7c tool Write: C:\Users\kir\.claude\plans\async-sauteeing-moon.md`). The gate takes the last such path of this session's stamp under `.claude/plans/`. Retro's defers go to `spec.md` only, so the gate reads that file too; `/handoff` after a Retro reply with defer lines is refused the same way.
> **＋** `rule-case-protocol` (`Leaf`, `built`, `render` into `CLAUDE.md`, `estimate-case-protocol-loaded` `passed`): the paragraph "Ledger lines are written by the `Stop` hook, from the reply, verbatim" says nothing about where in the reply.
> **－** `estimate[...]` and `lesson[...]` lines have no source but the text; the gate does not see them. The sentence in `CLAUDE.md` covers them; a loss of one is still a Retro finding, as today.
> **－** `ExitPlanMode` is not gated here: `/pre-task` precedes it and is a `Skill` call, so a reply that ratifies and closes Plan Mode at once is refused at the `/pre-task` step.
> **－** Without a `hi`, without a Spec and without a plan path in the log the gate has nothing to check and exits 0; the `/handoff` refusal of `rule-retro-commit` stays as it is.
> **－** The Frontier line F1 closes on this Case.

> **when:**
> The agent calls a skill through the `Skill` tool and `guppi gate` runs.

> **then:**
> The gate reads the `then` items of every Case in the session's `spec.md` and in the plan file the session's event log names last under `.claude/plans/`, and the decision lines of the session's window as `guppi pretask --check` reads them.
> **＋** When an item has no decision line of its Case, the gate exits 2 and writes nothing: `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B). The text before a tool call is never kept: end this reply in text with the LEDGER block, then call /<skill> in the next reply.`
> **＋** Every item with its line, or no source found: exit 0, silent; the `/handoff` check of the dirty tree runs as before.
> **＋** `rule-ledger-write` gains `guppi/gate.py` and `tests/test_gate.py` in `implementation_ref`; its "How it works" says the gate, not the agent's memory, holds the reply back.
> **＋** `rule-case-protocol` says, after the paragraph on the `Stop` hook: "A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call is never kept, and the hook reads nothing." — rendered into `CLAUDE.md`, `contract: same`.
> **＋** `estimate-ledger-write-lifts` gets a `### case 122` block, `pending`; the test seeds a plan with one item and an empty ledger and expects exit 2 with the case named, then the item's line and expects 0, then no plan path and no `spec.md` and expects 0; the live half is read at the first `/pre-task` of this session after its lines are written: the call passes.
> **－** `{supersedes:case 117}`: `decision-case-117` is superseded, `rule-ledger-write` loses `deferred_by`.

```then
update:
  - slug: rule-ledger-write
    contract: changed
    set: {implementation_ref: [guppi/ledger.py, guppi/gate.py, tests/test_gate.py, .claude/settings.json]}
    replace:
      - old: "So a reply that ended in a tool call (`Skill`, `ExitPlanMode`), which has no `Stop` of its own, reaches the ledger at the next `Stop` of the session, with that time; only the last reply of a session can still be lost, and Retro sees it."
        new: "A reply that ends in a tool call (`Skill`, `ExitPlanMode`) has no `Stop` of its own, and the text before the call is never kept: not in the transcript, not in `last_assistant_message` (measured in sessions L and N). The harness holds the reply back instead of the agent's memory: `guppi gate` on `PreToolUse Skill` reads the `then` items of every Case in the session's `spec.md` and in the plan file the session's event log names last under `.claude/plans/`, and the decision lines of the session's window as `guppi pretask --check` reads them; an item with no decision line of its Case refuses the call with exit 2 — `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B). The text before a tool call is never kept: end this reply in text with the LEDGER block, then call /<skill> in the next reply.` — and every item with its line, or no source found, passes silently (case 122). `estimate[...]` and `lesson[...]` lines have no source but the text; a loss of one is a Retro finding. A block the agent repeats in a later text reaches the ledger at that `Stop`, with that time; only the last reply of a session can still be lost, and Retro sees it."
    change: guppi gate refuses a Skill call while a then item of the session's Spec or plan file has no decision line in the ledger; the text before a tool call is never kept (case 122)
  - slug: rule-case-protocol
    contract: same
    replace:
      - old: "Without `/hi` the hook refuses and says so: tell the person, do not retry."
        new: "Without `/hi` the hook refuses and says so: tell the person, do not retry. A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call is never kept, and the hook reads nothing."
    change: a reply that carries a LEDGER block ends in that text, no tool call after it (case 122)
```

```tasks
- [x] `guppi/gate.py`: `plan_path` — the last `tool Write:` / `tool Edit:` line of this session's stamp in the logs `ledger.session_event_logs` walks whose path lies under `.claude/plans/`; `unwritten_items` — `split_cases` + `then_blocks` over `session_dir/spec.md` and the plan file (each skipped when absent), `window_lines` + `session_decisions` over the window, the "has no decision line" half of `pretask.check_lines`, findings deduplicated; on any: exit 2 with the message of the `then`, the skill named; else the `/handoff` check as before; no `hi`: exit 0
- [x] `tests/test_gate.py`: a plan named in the event log with one `update` item and an empty ledger → exit 2, stderr names the case; the item's decision line in `raw/<date>/<HHMM>/ledger.md` → exit 0; no plan path in the log and no `spec.md` → exit 0; a `spec.md` with a `defer` item and no line → exit 2; `/handoff` on a dirty tree still refused
- [x] `make test`, `make style`
- [x] read `estimate-ledger-write-lifts` block 122: the three cases against the test, the live half at the first `/pre-task` of this session after its lines are written
- [ ] `guppi render --sync` after the librarian's `generate`: `CLAUDE.md` carries the sentence of `rule-case-protocol`
```

## Case 124 — an open Insight as a Case of the next Plan Mode

> **context:**
> Today an Insight is "never a Decision target" (glossary, `insights/schema.md`, `index.md` §8); it reaches the Frontier only as the "Related Insight" of a deferred Case. `insight-session-vault-knowledge-not-loaded` (severity 4, the heredoc trap among its children) and `insight-ledger-hook-reads-only-the-final-text` (severity 3) have Proposals nobody was ever asked to ratify or reject; the same trap returns every session. (Case 119 as it stands.)

> **problem:**
> Lessons pile up, the librarian writes the Insight, and nothing puts it in front of the person as a Case. The owner's design: the librarian surfaces an open Insight in the brief as a Case for the next Plan Mode, where it is ratified into a decision on its Proposal, or rejected, or deferred with a count — the same lifecycle a deferred Case has. (Case 119 as it stands.)

> **given:**
> `rule-brief` (`Leaf`, `built`, `render` into `.claude/agents/librarian-guppi.md`, `estimate-brief-written` `passed`, `deferred_by: [decision-case-119]`): the Deferred item of the Render reads "at most seven items, one per target of a `defer` entry … plus every item of the previous brief's list whose decision no `supersedes` retired. Rank by the `severity` of a related Insight, then by the number of times the item was postponed".
> **＋** `rule-page-generation` (`Leaf`, `built`, `estimate-generate-writes` `passed`): `defer` sets `deferred_by` for `rules` and `entities` only (`generate.py:565-568, 579-580`); `KEY_ORDER["insights"]` has no `deferred_by`; `update` is not bound to a category; the cascade archives the `clustered` children of an `actioned` Insight and recounts `severity` (104.2, 104.3, 110); `derive_insight` builds a lesson's `## Insight` from its field — the model for `## Addressed by`. `clear_deferred_by` on a `supersedes` works through `find`, whatever the category. `index.py` shows `deferred_by` on a line of any category; `lint` treats it as a ref.
> **＋** Rule-class files: `glossary.md` — the `Insight` row ("never a Decision target") and the `deferred_by` row ("On an Entity or Rule"); `index.md` §8 — "An Insight is never the target of a Decision. It reaches you as a `brief.md` candidate in a later session and becomes an ordinary ratified Case there"; `insights/schema.md` — "Created by the librarian, never by a decision", the `addressed_by` row, the `## Addressed by` section ("Script places the decision link here once fixed"), no `deferred_by` row.
> **＋** Ten Insights today, all `open`, severity 2–4; under the cap of 7 with six deferred Cases the first lines go to the Insights of severity 4 and 3.
> **＋** `/hi` assembles the Frontier from the whole brief; a Deferred item is already an item, `rule-skill-hi` is not changed (F4 is its own Case).
> **－** The creation of an Insight stays with the librarian; a Decision neither creates nor deletes one. `severity` is still never written by hand (110.1).
> **－** `rule-synthesis` is not changed: clustering as it was.
> **－** The Frontier line F2 closes on this Case.

### Case 124.1 — brief: an open Insight in the Deferred list

> **when:**
> The librarian writes `brief.md` by its frame (the Render of `rule-brief`).

> **then:**
> The Deferred item of the Render reads: "Deferred: at most seven items — one per target of a `defer` entry in the yamls the walk named, every item of the previous brief's list whose decision no `supersedes` retired, and every Insight whose `status` is `open`. Rank by `severity` — the Insight's own, or that of the Insight related to a deferred Case — then by the number of briefs the item has stood in: the previous brief's count plus one. An Insight's line carries its slug, its `severity`, its `pattern` and its Proposal in one or two sentences; in Plan Mode it is a Case whose `recommend` starts from that Proposal, and it ends in an `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written the same way, or a `defer` with the Insight as its target."
> **＋** `estimate-brief-written` gets a `### case 124.1` block, `pending`; read against the brief of the next librarian's run: the `open` Insights stand in Deferred by severity, with a count.
> **－** `{supersedes:case 119}`: `decision-case-119` is superseded, `rule-brief` loses `deferred_by`.

```then
update:
  - slug: rule-brief
    contract: changed
    replace:
      - old: "- Deferred: at most seven items, one per target of a `defer` entry in the yamls the walk named, plus every item of the previous brief's list whose decision no `supersedes` retired. Rank by the `severity` of a related Insight, then by the number of times the item was postponed. Take that number from the previous brief and add one."
        new: "- Deferred: at most seven items — one per target of a `defer` entry in the yamls the walk named, every item of the previous brief's list whose decision no `supersedes` retired, and every Insight whose `status` is `open`. Rank by `severity` — the Insight's own, or that of the Insight related to a deferred Case — then by the number of briefs the item has stood in: the previous brief's count plus one. An Insight's line carries its slug, its `severity`, its `pattern` and its Proposal in one or two sentences; in Plan Mode it is a Case whose `recommend` starts from that Proposal, and it ends in an `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written the same way, or a `defer` with the Insight as its target."
    change: every open Insight stands in the Deferred list of the brief, ranked by its severity, with a count of the briefs it stood in, and is a Case of the next Plan Mode (case 124.1)
```

```tasks
- [ ] read `estimate-brief-written` block 124.1 against the brief of the next librarian's run (the `open` Insights in Deferred by severity, with a count)
```

### Case 124.2 — generate: an Insight as the target of `update` and `defer`

> **when:**
> `guppi generate` applies a yaml entry whose target is a page of `insights/`.

> **then:**
> A `defer` with an Insight as its target appends the decision slug to its `deferred_by`, as for a Rule; `KEY_ORDER["insights"]` gains `deferred_by` after `addressed_by`; a `supersedes` removes it through the same `clear_deferred_by`.
> **＋** An `update` with `set: {addressed_by: decision-case-N}` writes the field, and on every write of an Insight page the `## Addressed by` section is derived from the field — `- [[decision-case-N]]` — as a lesson's `## Insight` is from `insight` (114); without the field there is no section.
> **＋** An `update` with `set: {status: actioned}` goes as any `update`; the cascade of the same run archives the `clustered` children (104.2) and recounts `severity`.
> **＋** `estimate-generate-writes` gets a `### case 124.2` block, `pending`; the test: a `defer` on an insight → `deferred_by` written and shown in `insights-index.md`; an `update` with `addressed_by` and `status: actioned` → `## Addressed by` with the link, the children `archived`; a `supersedes` clears `deferred_by`.
> **－** An Insight is neither created nor deleted through the yaml: a `create` or `delete` with an Insight as its target is a `generate` error, as today.

```then
update:
  - slug: rule-page-generation
    contract: changed
    estimate_slug: estimate-generate-writes
    replace:
      - old: "A `defer` with a page appends History `deferred` and the decision slug to its `deferred_by`;"
        new: "A `defer` with a page appends History `deferred` and the decision slug to its `deferred_by` — a Rule, an Entity or an Insight (case 124.2);"
      - old: "History `insight section derived` (case 114);"
        new: "History `insight section derived` (case 114); an insight whose `addressed_by` is set gets `## Addressed by` holding the link the same way, rebuilt from the field on every write, and an `update` that sets `status: actioned` goes as any update, the cascade of the same run archiving the `clustered` children and recounting `severity` (case 124.2);"
    change: a defer marks an Insight deferred_by like a Rule, and the Addressed by section of an Insight is derived from addressed_by (case 124.2)
```

```tasks
- [x] `guppi/generate.py`: `KEY_ORDER["insights"]` gains `deferred_by` after `addressed_by`; `defer` sets `deferred_by` for `insights` too (lines 565-568 and 579-580, the category tuple); `derive_addressed_by(page)` after the model of `derive_insight`, called on every save of an `insights` page (the `save` path that calls `derive_insight` for lessons, and the cascade)
- [x] `tests/test_generate.py`: a `defer` entry on an insight writes `deferred_by` and `insights-index.md` shows it; an `update` with `set: {addressed_by: decision-case-9, status: actioned}` writes `## Addressed by` with `- [[decision-case-9]]` and the cascade archives its `clustered` children; a `supersedes` of that defer clears `deferred_by`; a `create` with an `insight-` slug is an error
- [x] `make test`, `make style`
- [x] read `estimate-generate-writes` block 124.2 against the test
```

### Case 124.3 — glossary, `index.md` §8, `insights/schema.md`

> **when:**
> Someone reads one of the three files.

> **then:**
> `glossary.md`: the `Insight` row reads "Over Lessons sharing a root cause, made by the librarian on the second; surfaces in the brief's Deferred list and is the target of the `update` that actions or rejects it, or of a `defer`; never created or deleted by a Decision; `actioned` reopens" (case 124); the `deferred_by` row reads "On an Entity, Rule or Insight".
> **＋** `index.md` §8: "An Insight is never created or deleted by a Decision. Every `open` Insight stands in the brief's Deferred list, ranked by `severity`, and is a Case of the next Plan Mode: its Proposal is ratified into an `update` of the Insight (`status: actioned`, `addressed_by`) with what it needs, or rejected the same way, or deferred with the Insight as the target (case 124)."
> **＋** `insights/schema.md`: "Created by the librarian, never by a decision" → "Created by the librarian, never by a decision; an `update` actions or rejects it, a `defer` postpones it"; the table gains a `deferred_by` row (no; a list of decision slugs; the `defer` decisions that postponed it, set by `generate`, cleared by a `supersedes`); `## Addressed by` — "Derived by `generate` from `addressed_by`".
> **－** Applied by hand in Work Mode; no Estimate.

```then
update:
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "Insight row: surfaces in the brief's Deferred list, the target of the update that actions or rejects it or of a defer, never created or deleted by a Decision; deferred_by row: on an Entity, Rule or Insight (case 124.3)"
  - slug: index
    file: vault/wiki/index.md
    change: "§8 Insight: never created or deleted by a Decision; every open Insight stands in the brief's Deferred list by severity and is a Case of the next Plan Mode — actioned, rejected or deferred (case 124.3)"
  - slug: insights-schema
    file: vault/wiki/insights/schema.md
    change: "an update actions or rejects an Insight, a defer postpones it; a deferred_by row; Addressed by derived by generate from addressed_by (case 124.3)"
```

```tasks
- [x] `vault/wiki/glossary.md`: the `Insight` and `deferred_by` rows, by hand (124.3)
- [x] `vault/wiki/index.md` §8: the Insight paragraph, by hand (124.3)
- [x] `vault/wiki/insights/schema.md`: the "Created by the librarian" sentence, the `deferred_by` row, the `## Addressed by` row, by hand (124.3)
```

## Case 125 — where `/hi` takes the time of its folder from

> **context:**
> Case 111.4 removed the `Recorded:` line from the `/hi` skill: the `hi` is now written by the `UserPromptSubmit` hook (`guppi event prompt`, 111.1) with the session's stamp. Today it worked: `- 10:29:12 19037d1c hi`. But the skill's text still says "`HHMM` the time of the `hi` line above (case 73)" — and there is no line above any more. To name the folder `raw/2026-09-14/1029/` the agent read `event_log.md` through Bash.

> **problem:**
> The skill points at a line nobody prints. The agent either guesses the time or makes a read call — against the purpose of `rule-skill-hi` ("prevents a session from being loaded piecemeal by read-tool calls"). The time of the `hi` needs a source in the context, without a read.

> **given:**
> `rule-event-log` (`Leaf`, `draft`, `estimate-event-log-records` `pending` on block 111.1): "the log gains `- HH:MM:SS <stamp> hi` … a second `/hi` of the same session and any other prompt write nothing (case 111.1)"; `prompt_line` (`event.py:127-136`) returns the line or None, the hook is silent on stdout; `hi_written` already knows whether a `hi` of this session exists.
> **＋** `rule-skill-hi` (`MOC`, `built`, `estimate-hi-no-read-calls` `passed` on 101.3, `estimate-hi-writes-frontier` `passed`): line 41 of the Render — "`HHMM` the time of the `hi` line above (case 73)". The folder and the time come from `ledger.session_dir`; in a `!` substitution of the skill `CLAUDE_SESSION_ID` is empty (111), so a substitution cannot name the session — the hook can, its payload carries `session_id`. A `UserPromptSubmit` hook's stdout on exit 0 is added to the context (Claude Code hooks reference).
> **＋** The order "the `UserPromptSubmit` hook → the expansion of the skill" is not measured; it does not matter here: the line reaches the context with the prompt, before the agent's reply.
> **－** Other prompts: the hook stays silent; exit 0 always, errors on stderr only.
> **－** `estimate-hi-no-read-calls` gets no block: its criterion (no read call) does not change, the way to meet it does; its reading is by 101.3 at the next `/hi`.
> **－** The Frontier line F4 closes on this Case.

> **when:**
> The person submits `/hi` and the `UserPromptSubmit` hook `uv run guppi event prompt` runs.

> **then:**
> Having written the `hi` line, the hook prints on stdout `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/`; when a `hi` of this session already exists it prints `hi: already recorded at HH:MM:SS → raw/<date>/<HHMM>/` and writes nothing; on any other prompt it is silent. The line reaches the session's context.
> **＋** The Render of `rule-skill-hi`: "`HHMM` the time of the `hi` line above (case 73)" → "`HHMM` from the `hi:` line the `UserPromptSubmit` hook put in context (cases 73, 125)".
> **＋** `estimate-event-log-records` gets a `### case 125` block, `pending`; the test: `/hi` → the line written and stdout `hi: … → raw/…/`; a second `/hi` → stdout `already recorded`, no new line in the log; `hello` → stdout empty. The live reading at the next `/hi`: the `hi:` line is in the context and the folder is named without a read call.
> **－** `rule-skill-hi` is a MOC, no `contract` is written; `rule-event-log` is `contract: changed`.

```then
update:
  - slug: rule-event-log
    contract: changed
    replace:
      - old: "a second `/hi` of the same session and any other prompt write nothing (case 111.1)."
        new: "a second `/hi` of the same session and any other prompt write nothing (case 111.1). Having written the line, the hook prints `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/` on stdout, which Claude Code adds to the context; when a `hi` of this session already exists it prints `hi: already recorded at HH:MM:SS → raw/<date>/<HHMM>/`; on any other prompt it is silent. The `/hi` skill takes the time of the session's folder from that line (case 125)."
    change: the prompt hook prints the hi it wrote, or the one already recorded, with the session's folder, into the context (case 125)
  - slug: rule-skill-hi
    replace:
      - old: "`HHMM` the time of the `hi` line above (case 73)"
        new: "`HHMM` from the `hi:` line the `UserPromptSubmit` hook put in context (cases 73, 125)"
    change: the time of the session's folder comes from the hook's hi line in context, not from a line the skill no longer prints (case 125)
```

```tasks
- [x] `guppi/event.py`: `prompt` — after writing the `hi` line print `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/` on stdout; when `hi_written` is true, find that `hi` (its time and date in the logs walked) and print `hi: already recorded at HH:MM:SS → raw/<date>/<HHMM>/`; any other prompt: nothing on stdout; `run` gains a `stdout` parameter like `pretask.run`
- [x] `tests/test_event.py`: `/hi` prints the `hi:` line with the folder; a second `/hi` prints `already recorded` and adds no line; `hello` prints nothing; the folder across midnight is the `hi` date's
- [x] `make test`, `make style`
- [x] read `estimate-event-log-records` block 125 against the test; block 111.1 and the live half of 125 at the next `/hi` (the `hi:` line in context, the folder named without a read call; a repeated `/hi` prints `already recorded` and adds no line)
- [ ] `guppi render --sync` after the librarian's `generate`: `.claude/skills/hi/SKILL.md` carries the new sentence
```

## Case 126 — the ledger of `/retro` on a day without a date-level ledger

> **context:**
> The Render of `rule-retro` (109.1) reads the ledgers of the day with `cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null`. On 2026-09-14 no date-level ledger exists — the first day with the session form of case 103 alone — so `cat` exits 1, the harness reports the substitution failed, and the skill text does not reach the agent; the `retro` event was still recorded. (Case 118 as it stands.)

> **problem:**
> A substitution that names a file which the model of case 103 no longer guarantees fails on every session from now on. The fix is one `|| true` or a glob-only form; it is an `update` of `rule-retro`, which Retro cannot ratify. (Case 118 as it stands.)

> **given:**
> `rule-retro` (`Leaf`, `draft`, `estimate-retro-loads` `failed` on 109.1, `deferred_by: [decision-case-118]`): line 40 of the Render is the substitution above; the text "the ledger lines of today grouped by Case".
> **＋** `guppi tail` (`rule-ledger-tail`, `built`, `estimate-ledger-tail` `passed`): prints every record line under `vault/raw/` that no entry of a `materialize.yaml` covers, as `<date>/<HHMM> L<n>: <line>`; exit 0 always; a ledger that cannot be read is a line on stderr and the walk goes on. At Retro, before the librarian, the tail is this session's lines whole.
> **＋** The glob form `cat vault/raw/$(date +%F)/*/ledger.md` loses a session across midnight and fails on a day without any ledger; `|| true` hides the failure and does not fix the date.
> **－** `rule-ledger-tail` is not changed: the command and its contract stay, a second caller is added.
> **－** The Frontier line F5 closes on this Case.

> **when:**
> The person invokes `/retro`.

> **then:**
> The Render of `rule-retro`: the line `Ledger of today: !`cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null`` → `Ledger: !`uv run guppi tail`` — the unmaterialized lines, this session's in its folder; the phrase "the ledger lines of today grouped by Case" → "the lines of the Tail above grouped by Case, this session's folder first".
> **＋** `estimate-retro-loads` gets a `### case 126` block, `pending`; read at the first `/retro` after the render — the next session's, since the skill is rendered by the librarian after this session's Retro: the skill loaded, `Ledger:` carries the lines of the session's folder, no substitution failed.
> **－** `{supersedes:case 118}`: `decision-case-118` is superseded, `rule-retro` loses `deferred_by`.

```then
update:
  - slug: rule-retro
    contract: changed
    replace:
      - old: "Ledger of today: !`cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null`"
        new: "Ledger: !`uv run guppi tail`"
      - old: "the ledger lines of today grouped by Case"
        new: "the lines of the Tail above grouped by Case, this session's folder first"
    change: the Retro ledger is the unmaterialized tail printed by guppi tail, not a cat over a date-level file the model of case 103 no longer has (case 126)
```

```tasks
- [ ] `guppi render --sync` after the librarian's `generate`: `.claude/skills/retro/SKILL.md` carries `Ledger: !`uv run guppi tail``
- [ ] read `estimate-retro-loads` block 126 at the first `/retro` after the render (the next session's): the skill loaded, `Ledger:` holds the lines of the session's folder, no failed substitution
```

## Case 127 — a `PreToolUse Bash` hook against the heredoc trap

> **context:**
> `lesson-bash-tool-heredoc-escapes-interpreted` (H), `lesson-heredoc-trap-hit-twice-with-its-lesson-live` (L), `lesson-heredoc-trap-hit-a-third-time-in-work-mode` (M): a heredoc passed to the Bash tool has its backslash escapes interpreted, and the agent reaches for a heredoc first every session, with the lesson live. The Insight's Proposal — pages of a phase carry its traps — is Case 119's; the trap itself has a mechanical fix. (Case 120 as it stands.)

> **problem:**
> A lesson the agent has to remember is not a rule. A `PreToolUse Bash` hook that refuses a command whose heredoc body carries a backslash escape — or refuses a heredoc that writes a file at all, pointing at Write and Edit — makes the trap impossible instead of remembered. (Case 120 as it stands.)

> **given:**
> `rule-bash-guard` is a placeholder (`draft`, `deferred_by: [decision-case-120]`, no `kind`, `estimates` or `tags`: 4 `schema` and 1 `orphan` lint findings). `generate` fills a placeholder on a `create` and keeps its `deferred_by` (`generate.py:400`); a `supersedes` clears it. The slug is taken by the placeholder itself — that is the target.
> **＋** `rule-harness` (`MOC`): children `rule-render-harness, rule-settings, rule-lint, rule-index, rule-governed-files-hook, rule-claude-md`; `rule-governed-files-hook` (`guppi/guard.py`) is the model: `PreToolUse` on `Edit|Write|MultiEdit`, a line in the event log before the refusal, exit 2 with the reason, never raises, exit 0 on an unreadable payload.
> **＋** `rule-hook-registry` (`Leaf`, `built`, `estimate-hook-registry-rendered`): the Render's `PreToolUse` holds three matchers; a new matcher `Bash` is `contract: same`, as 111.2 was: the Estimate checks that the render reproduces the file, not which hooks it holds.
> **＋** Today's case: `cat >> plan.md <<'EOF'` with the body of a Case failed with "unexpected EOF while looking for matching quote" — the second face of the same trap, a file written by a heredoc; Edit worked.
> **－** Tags `hooks`, `harness`; no new tag.
> **－** Not refused: a `<<<` here-string; a heredoc without a backslash whose output goes to a pipe or the screen; `python - <<'EOF'` with a clean body.
> **－** The Frontier line F6 closes on this Case.

> **when:**
> The agent calls the `Bash` tool and the hook `uv run guppi bashguard` runs on `PreToolUse`.

> **then:**
> The hook reads `tool_input.command`, finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line. A body with a backslash, or a marker line that redirects into a file (`>` / `>>` not to `/dev/null`, `tee`) — exit 2, the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path>>. Write the script with the Write tool into the scratchpad and run it by path; change a file with Edit.`
> **＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard: <reason>` goes to `raw/<date>/event_log.md` (case 91).
> **＋** Any other tool, a command without a heredoc, a heredoc without a backslash and without a file write, an unreadable payload — exit 0, the last with a line on stderr; the hook never raises.
> **＋** `rule-bash-guard` is a `Leaf`, `enforcement: hook`, `implementation_ref: [guppi/bashguard.py, tests/test_bashguard.py, .claude/settings.json]`, `parent: rule-harness`, `tags: [hooks, harness]`; `estimate-bash-guard` (`QA`), `pending`: the test on `python - <<'EOF'` with `\n` in the body → 2; `cat > f <<EOF` → 2; a heredoc with a clean body into a pipe → 0; a command without a heredoc → 0; an unreadable payload → 0; the live reading is the first refusal in Work Mode or, without one, the test.
> **＋** `rule-hook-registry`: in `PreToolUse` after the matcher `Edit|Write|MultiEdit` — `{ "matcher": "Bash", "hooks": [ { "type": "command", "command": "uv run guppi bashguard", "timeout": 30 } ] }`; `contract: same`; `rule-harness` gets `rule-bash-guard` as its seventh child through the `ref`.
> **－** `{supersedes:case 120}`: `decision-case-120` is superseded, `rule-bash-guard` loses `deferred_by`.

```then
create:
  - slug: rule-bash-guard
    type: rule
    kind: Leaf
    purpose: Prevents a heredoc from carrying a backslash escape or writing a file through the Bash tool
    enforcement: hook
    implementation_ref: [guppi/bashguard.py, tests/test_bashguard.py, .claude/settings.json]
    tags: [hooks, harness]
    sections:
      Purpose: |
        Prevents a heredoc from carrying a backslash escape or writing a file through the Bash
        tool. On this Windows machine the tool's shell layer interprets backslash escapes inside a
        heredoc body before the interpreter reads it, whatever the quoting of the marker; three
        sessions (H, L, M) broke edit scripts that way with the lesson live, and a heredoc that
        writes a file fails on quotes in its body. A lesson the agent has to remember is not a
        rule; a `PreToolUse` hook cannot be skipped.
      How it works: |
        `uv run guppi bashguard` on `PreToolUse` of `Bash`. It reads `tool_input.command`, finds
        every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing
        line. A body with a backslash, or a marker line that redirects into a file (`>` or `>>`
        not to `/dev/null`, `tee`), exits 2 with the reason on stderr — `bashguard: heredoc
        refused — <a backslash in its body | it writes <path>>. Write the script with the Write
        tool into the scratchpad and run it by path; change a file with Edit.` — which blocks
        the call; one line `bashguard: <reason>` goes to `vault/raw/<date>/event_log.md` before
        that (case 91). A `<<<` here-string, a heredoc without a backslash whose output goes to a
        pipe or the screen, a command without a heredoc, any other tool, or a payload the hook
        cannot read: exit 0, the last with one line on stderr. The hook never raises (case 127).
    method: pytest in `tests/test_bashguard.py` with piped payloads — a `python - <<'EOF'` body with `\n` → 2, `cat > f <<EOF` → 2, a clean heredoc into a pipe → 0, no heredoc → 0, an unreadable payload → 0; the live reading is the first refusal of a Work Mode, written into the estimate line, or the test alone when none occurs
update:
  - slug: rule-hook-registry
    contract: same
    replace:
      - old: |
          { "matcher": "Edit|Write|MultiEdit",
            "hooks": [ { "type": "command", "command": "uv run guppi guard", "timeout": 30 } ] }
        new: |
          { "matcher": "Edit|Write|MultiEdit",
            "hooks": [ { "type": "command", "command": "uv run guppi guard", "timeout": 30 } ] },
          { "matcher": "Bash",
            "hooks": [ { "type": "command", "command": "uv run guppi bashguard", "timeout": 30 } ] }
    change: a PreToolUse hook on Bash, guppi bashguard, against the heredoc trap (case 127)
```

```tasks
- [x] `guppi/bashguard.py`: `heredocs(command)` — every `<<`/`<<-` marker (quoted or not) with its body up to the closing line and the marker line itself; `refusal(command)` — the first body with a backslash, or a marker line redirecting into a file (`>`/`>>` to a path other than `/dev/null`, or `tee`), as the reason string or None; `run` after `guard.run`: read the payload, `Bash` only, log the line, exit 2 with the message, else 0
- [x] `guppi/cli.py`: the `bashguard` subcommand
- [x] `tests/test_bashguard.py`: the five cases of the `method`, plus `<<-` with a tab-indented closing marker, a quoted marker, and `2>/dev/null` on the marker line not counted as a file write
- [x] `make test`, `make style`
- [x] read `estimate-bash-guard` against the test; the live half at the first refusal in Work Mode, if one occurs
- [ ] `guppi render --sync` after the librarian's `generate`: `.claude/settings.json` carries the `Bash` matcher and parses as JSON
```

## Case 128 — the pre-task dispatch carries `when`, `then` and the `then` blocks, not a summary

> **context:**
> At pre-task of session M the dispatch to `ask-guppi` carried one summary line per decision; four of its ten findings answered things the plan's `then` blocks already did (`lesson-pretask-dispatch-summarized-the-plan-and-ask-guppi-judged-the-summary`). `rule-ask` says "one short question"; `rule-pretask` says "dispatch the agent once with that list". (Case 121 as it stands.)

> **problem:**
> The agent judged pages against a paraphrase and could not see the planned wording. The information it lacked must be in the dispatch: the `then` blocks — `replace` pairs, `set`, `sections` — or the path of the plan file, since the agent has Read. (Case 121 as it stands.)

> **given:**
> `rule-pretask` (`Leaf`, `built`, `render` into `.claude/skills/pre-task/SKILL.md`, `estimate-pretask-reconciles` `passed`, `deferred_by: [decision-case-121]`): the Render's paragraph — "List every decision ratified in this Plan Mode, one line each: slug — decision type — purpose; … Dispatch the `ask-guppi` agent once with that list and the question: which of these contradict a page of the vault, a rule of `index.md`, or each other".
> **＋** `ask-guppi` (`rule-ask`): tools Read, Grep, Glob; reads the indexes, opens a page by slug. The plan file lies outside the repository (`~/.claude/plans/<name>.md`), but Read takes an absolute path; the agent knows it — it writes the file.
> **＋** The `when` + `then` sections are the criterion of the Case (what reaches the Estimate); the `then` block is the page text. The first says which event the change is bound to, the second in which words; `ask-guppi` needs both to name a wrong wording and a wrong place alike (the owner's addition).
> **＋** The lesson `lesson-pretask-dispatch-…` is `new`, without an Insight; this is its fix.
> **－** `rule-ask` is not changed: one question per Case, one dispatch per pre-task, as before.
> **－** The Frontier line F8 closes on this Case.

> **when:**
> The person invokes `/pre-task` and the agent assembles the dispatch for `ask-guppi`.

> **then:**
> The Render of `rule-pretask`: "Dispatch the `ask-guppi` agent once with that list and the question" → "Dispatch the `ask-guppi` agent once with that list, the absolute path of the plan file, the instruction to read for every Case there its `when` and `then` sections and its `then` block — `replace` old and new, `set`, `sections` — before judging a page, so that a finding can name a wrong wording or a wrong place, and the question".
> **＋** `estimate-pretask-reconciles` gets a `### case 128` block, `pending`; read at this session's `/pre-task`: the dispatch carries the path and the instruction on `when`, `then` and the blocks, and no finding answers what the plan already does.
> **－** `{supersedes:case 121}`: `decision-case-121` is superseded, `rule-pretask` loses `deferred_by`.

```then
update:
  - slug: rule-pretask
    contract: changed
    replace:
      - old: "Dispatch the `ask-guppi` agent once with that list and the question"
        new: "Dispatch the `ask-guppi` agent once with that list, the absolute path of the plan file, the instruction to read for every Case there its `when` and `then` sections and its `then` block — `replace` old and new, `set`, `sections` — before judging a page, so that a finding can name a wrong wording or a wrong place, and the question"
    change: the pre-task dispatch carries the plan file's path and the instruction to read every Case's when, then and then block, not a summary (case 128)
```

```tasks
- [x] at this session's `/pre-task`: dispatch `ask-guppi` with the list, the absolute path of the plan file and the instruction of the `then` above — the skill file still carries the old text until the render, so the agent applies the ratified wording by hand this once
- [x] read `estimate-pretask-reconciles` block 128 at this session's `/pre-task`: no finding answers what a `then` block already does
- [ ] `guppi render --sync` after the librarian's `generate`: `.claude/skills/pre-task/SKILL.md` carries the new sentence
```

## Case 130 — the literal `decision-case-N` and the failed entry 112.6

> **context:**
> Entry 112.6 of `raw/2026-09-14/0747/materialize.yaml` is `failed`: the `replace` on `rule-page-generation` did not find its `old`. The reason: the text "History and log lines end with · [[decision-case-N]] when a decision exists" stands only in the History line of 2026-09-11 (line 95), and `generate.replace` skips History (`generate.py:519`); line 44 of the body is already in backticks, and lint does not count it (`CODE_SPAN`, `lint.py:57`). Seven `ref` findings of lint: the History line of `rule-page-generation` and the Given of `decision-case-112.1`–`112.6`, which quote the same line without backticks. The librarian repairs no yaml (rule-documentation); `archive` keeps `0747`: "1 entries not applied".

> **problem:**
> The literal has to be quoted where `replace` does not reach — in History and in six decision pages; and the failed entry has to leave the count, or session M never moves into the archive. `mark_superseded` (`materialize.py:654`) marks `superseded_by` on the entries of its own yaml only.

> **given:**
> `rule-page-generation` (`Leaf`, `built`, `estimate-generate-writes` `passed`; already an `update` by 124.2 in this session — a second entry on one page in ledger order, allowed): History is "appended by hook, never by an agent" — the hand edit of line 95 is ratified here as a one-off migration; the decision pages 112.1–112.6 quote the line in their Given without backticks, the same migration by hand; `decision-case-112.6` goes `superseded` by the cascade and into the archive.
> **＋** `rule-materialize` (`Leaf`, `built`, `estimate-materialize-assembles`, `estimate-materialize-walks-dates` `passed`): "a later `supersedes` adds `superseded_by` to the earlier entry and changes nothing else" — today within one yaml only; `units_with(project_dir, "materialize.yaml")` already lists every yaml; `archive.kept_reason` takes `superseded_by` as done.
> **＋** `rule-lint` is not changed: a code span is no ref already, a History ref is a ref, as designed (72.6).
> **－** Entry 112.6 stays in the yaml as it is, with `failed` and `superseded_by`; `generate` skips `applied` entries only (`generate.py:815`), so the librarian's run of this session retries it, fails it once more — exit 1, a flag — and `archive` then moves `0747` on the `superseded_by` mark (pre-task finding 6 of case 132).
> **－** The Frontier line F9 closes on this Case.

### Case 130.1 — quote the literal by hand

> **when:**
> Work Mode of this session runs the migration task; then `guppi lint`.

> **then:**
> In `rule-page-generation` the History line of 2026-09-11 reads "…History and log lines end with `· [[decision-case-N]]` when a decision exists…"; in the Given of `decision-case-112.1`–`112.6` the same quotation is in backticks. `guppi lint` finds no `ref` to `decision-case-N`: the 7 findings are gone.
> **＋** An `update` of `rule-page-generation`, `contract: same`, `change` only; `generate` appends the History line.
> **－** `{supersedes:case 112.6}`: `decision-case-112.6` is superseded.

```then
update:
  - slug: rule-page-generation
    contract: same
    change: the literal decision-case-N of the History line of 2026-09-11 and of the Given of decision-case-112.1–112.6 quoted by hand, a one-off migration; entry 112.6 superseded (case 130.1)
```

```tasks
- [x] one-off migration, by hand (130.1): wrap `· [[decision-case-N]]` in backticks in the History line of 2026-09-11 of `vault/wiki/rules/rule-page-generation.md` and in the Given line "`rule-page-generation`, History line of 2026-09-11: …" of `vault/wiki/decisions/decision-case-112.1.md` … `112.6.md`; `guppi lint` shows the 7 `ref` findings gone
```

### Case 130.2 — a `supersedes` reaches another unit's yaml

> **when:**
> `guppi materialize` assembles the entry of a line with `{supersedes:case N}`.

> **then:**
> The entries of Case N (decision kinds) are marked `superseded_by` in the yaml of the unit that holds them — its own or any other under `raw/` — and in the `decisions` list of that unit; a foreign yaml is written with that mark only.
> **＋** `estimate-materialize-assembles` gets a `### case 130.2` block, `pending`; the test: the yaml of unit A with an entry of case 5 without `applied`, the ledger of unit B with a line carrying `{supersedes:case 5}` → after `materialize` of unit B the entry in A carries `superseded_by`, the rest of A unchanged; `archive.kept_reason(A)` is None. The live reading at the librarian's run: 112.6 marked, `0747` moved.
> **－** An entry that no yaml holds: as today, nothing.

```then
update:
  - slug: rule-materialize
    contract: changed
    estimate_slug: estimate-materialize-assembles
    replace:
      - old: "a later `supersedes` adds `superseded_by` to the earlier entry and changes nothing else"
        new: "a later `supersedes` adds `superseded_by` to the entries of the earlier Case in whichever unit's yaml holds them — this one or any other under `raw/` — and to that unit's `decisions` list, and changes nothing else; a foreign yaml is written with that mark only (case 130.2)"
    change: a supersedes marks the earlier Case's entries in the yaml of any unit under raw/, so a failed entry superseded from a later session no longer keeps its unit out of the archive (case 130.2)
```

```tasks
- [x] `guppi/materialize.py`: `mark_superseded` — when no entry of case N is in this unit's `entries`, walk `units_with(project_dir, "materialize.yaml")`, load each, mark the entries and the `decisions` of case N, and save that yaml with the mark only; the signature gains `project_dir` (or a helper `mark_superseded_elsewhere`)
- [x] `tests/test_materialize.py`: unit A's yaml with an unapplied entry of case 5, unit B's ledger with `{supersedes:case 5}` → A's entry carries `superseded_by`, A otherwise unchanged; `archive.kept_reason(A)` is None; a case no yaml holds changes nothing
- [x] `make test`, `make style`
- [x] read `estimate-materialize-assembles` block 130.2 against the test; the live half at the librarian's run (112.6 marked, `raw/2026-09-14/0747` moved) is the next session's reading
```

## Case 131 — the History line `updated: the` on `rule-page-generation`

> **context:**
> The `change` of the 114 entry in session M's Spec is the single word "the" (a truncated phrase); `generate` wrote `- 2026-09-14 updated: the · [[decision-case-114]]` into the History of `rule-page-generation` and into `log.md`. The `replace` of 114 applied; only History and `log.md` carry the fragment (brief, Flags).

> **problem:**
> History is the record of what each Case did; the line "updated: the" says nothing. `replace` does not reach History (130), and "appended by hook, never by an agent" is the rule a one-off migration is the only way out of.

> **given:**
> `rule-page-generation` (`Leaf`, `built`): already an `update` by 124.2 and 130.1 in this session — a third entry on one page in ledger order, allowed; line 118 of History is `- 2026-09-14 updated: the · [[decision-case-114]]`.
> **＋** The `change` of 114 in `raw/2026-09-14/0747/spec.md` is not edited: the Spec is the record of what was signed.
> **－** `log.md` is not a page and has no schema; it stays as it is.
> **－** The Frontier line F10 closes on this Case; the rest of F10 is `work` and Slice 5.

> **when:**
> Work Mode of this session runs the migration task.

> **then:**
> The History line of 114 on `rule-page-generation` reads `- 2026-09-14 updated: the cascade derives the ## Insight section of every clustered lesson from its insight field (case 114) · [[decision-case-114]]`.
> **＋** An `update` of `rule-page-generation`, `contract: same`, `change` only; `generate` appends its own History line.

```then
update:
  - slug: rule-page-generation
    contract: same
    change: "the History line of case 114, `updated: the`, completed by hand to name the derived ## Insight section — a one-off migration (case 131)"
```

```tasks
- [x] one-off migration, by hand (131): in `vault/wiki/rules/rule-page-generation.md` replace the History line `- 2026-09-14 updated: the · [[decision-case-114]]` with `- 2026-09-14 updated: the cascade derives the ## Insight section of every clustered lesson from its insight field (case 114) · [[decision-case-114]]`
```

## Work without a decision, continued

F10's live readings, no Case: the readings are written as `estimate[...]` lines the moment they exist.

```tasks
- [x] F10: read `estimate-spec-capture-appends` at the approval of this plan (`raw/2026-09-14/1029/spec.md` appended by `guppi spec`)
- [x] F10: read `estimate-plan-mode-verified` at the approval of this plan (`guppi pretask` held `ExitPlanMode` until `/pre-task` ran)
- [ ] F10: read `estimate-handoff-dispatches` at `/handoff`
```

## Case 132 — pre-task findings: four block amendments and six pages left false

> **context:**
> `ask-guppi` read the plan whole (the dispatch of case 128). Its findings: (1) `sections: Language` in 123 — `## Language` lies inside the Render markers of `rule-claude-md`; `split_sections` gives it to the Render block, a `sections` entry would add a second section and `CLAUDE.md` would not change. (2) The `old` of 124.2, "a `defer` marks its target `deferred_by`", came from the docstring of `generate.py`; the page has no such phrase; the whole 124.2 entry would fail. (3) `sections: Addressed by` in 124.2 is an Insight section, not a Rule one; the Rule page would gain a stray section. (4) 122 leaves `rule-retro-commit` false: "Any other skill or tool: exit 0". (5) 122 and 125 give the event log a second job while `rule-event-log` says "Its one governance job is to carry the `hi` mark". (6) 130.1 said "`generate` takes it no more" — wrong: `generate` skips `applied` only; 112.6 fails once more in the librarian's run (a flag), then `archive` moves `0747` on `superseded_by`. (7) `rule-harness` Purpose: "Two more belong here and run in no pipeline" — three after 127. (8) `rule-retro` Purpose: "a line of today's ledger" — 109.1 promised "this session's", the page did not change. (9) `rule-brief` Purpose: "every deferred item lives on as a draft page" — an Insight in Deferred is no draft page. (10) `rule-ledger-tail` names `/hi` alone; 126 adds `/retro`.

> **problem:**
> Four amendments touch blocks already signed; they cannot change silently. Six pages need new `update` entries, all `contract: same`: no contract changes, the text that became false does.

> **given:**
> Every `old` text below was checked on its page (`rule-retro-commit` 28, `rule-event-log` 22–23, `rule-harness` 20–22, `rule-retro` 24, `rule-brief` 21–22, `rule-ledger-tail` 19, `rule-claude-md` 73–75, `rule-page-generation` 44 and 51).
> **＋** `rule-retro-commit`: `estimate-retro-commit-gates` says "another skill or another tool, exit 0 whatever the tree" — on the tree that stays true; the refusal of 122 is on another ground; `contract: same`.
> **＋** `rule-event-log`, `rule-retro`, `rule-brief` already get an `update` in this session (125, 126, 124.1) — a second entry on a page in ledger order, allowed; `rule-page-generation` gets a block amendment, not a new entry.
> **－** No new Estimate block: no `when` or `then` changes.

> **when:**
> `generate` applies the entries of this Case; the librarian reads `materialize.yaml`.

> **then:**
> The blocks of 123, 124.2 and 130.1 in the Spec are amended as the context says, before Plan Mode ends: 123 a `replace` of the three sentences; 124.2 the `old` of line 51 and the `## Addressed by` text as a second `replace` into `How it works`; 130.1 the `－` line stating the retry.
> **＋** `rule-retro-commit`: "Any other skill or tool: exit 0." → "Any other tool: exit 0; any other skill: exit 0 on the tree — the same hook refuses any skill while a `then` item of the session's Spec has no ledger line (`rule-ledger-write`, case 122)."
> **＋** `rule-event-log`: "Its one governance job is to carry the `hi` mark that tells the ledger hook a working session is open." → "Its governance jobs: to carry the `hi` mark that tells the ledger hook a working session is open, and to name the session's plan file by its `tool Write:` and `tool Edit:` lines for `guppi gate` (case 122)."
> **＋** `rule-harness`: "Two more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, and the page `CLAUDE.md` is rendered from (cases 59.6, 59.8)." → "Three more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, and the page `CLAUDE.md` is rendered from (cases 59.6, 59.8, 127)."
> **＋** `rule-retro`: "work a line of today's ledger ratified" → "work a line of this session's ledger ratified".
> **＋** `rule-brief`: "every deferred item lives on as a draft page and pre-task finds it there" → "every deferred item lives on as a page — a draft placeholder, or the open Insight itself — and pre-task finds it there".
> **＋** `rule-ledger-tail`: "Shows at `/hi` every ledger line that no vault page holds yet." → "Shows at `/hi`, and at `/retro` since case 126, every ledger line that no vault page holds yet."
> **－** Finding 6 is no page: the `－` line of 130.1 is corrected; the librarian's flag is expected.

```then
update:
  - slug: rule-retro-commit
    contract: same
    replace:
      - old: "Any other skill or tool: exit 0."
        new: "Any other tool: exit 0; any other skill: exit 0 on the tree — the same hook refuses any skill while a `then` item of the session's Spec has no ledger line (`rule-ledger-write`, case 122)."
    change: the gate's second refusal, on an unwritten ledger line, named beside the tree check (case 132)
  - slug: rule-event-log
    contract: same
    replace:
      - old: "Its one governance job is to carry the `hi` mark that tells the ledger hook a working session is open."
        new: "Its governance jobs: to carry the `hi` mark that tells the ledger hook a working session is open, and to name the session's plan file by its `tool Write:` and `tool Edit:` lines for `guppi gate` (case 122)."
    change: the event log's second governance job, the plan path for guppi gate, named (case 132)
  - slug: rule-harness
    replace:
      - old: "Two more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, and the page `CLAUDE.md` is rendered from (cases 59.6, 59.8)."
        new: "Three more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, and the page `CLAUDE.md` is rendered from (cases 59.6, 59.8, 127)."
    change: the bash guard hook counted among the children outside the pipeline (case 132)
  - slug: rule-retro
    contract: same
    replace:
      - old: "work a line of today's ledger ratified"
        new: "work a line of this session's ledger ratified"
    change: the scope rule names this session's ledger, as 109.1 promised (case 132)
  - slug: rule-brief
    contract: same
    replace:
      - old: "every deferred item lives on as a draft page and pre-task finds it there"
        new: "every deferred item lives on as a page — a draft placeholder, or the open Insight itself — and pre-task finds it there"
    change: an open Insight in Deferred is a live page, not a draft placeholder (case 132)
  - slug: rule-ledger-tail
    contract: same
    replace:
      - old: "Shows at `/hi` every ledger line that no vault page holds yet."
        new: "Shows at `/hi`, and at `/retro` since case 126, every ledger line that no vault page holds yet."
    change: the second caller of guppi tail, the retro skill, named (case 132)
```

```tasks
- [x] the blocks of 123, 124.2 and 130.1 amended in the plan file before Plan Mode ends (132)
- [ ] nothing else in Work Mode; the librarian's `generate` applies the six replaces
```

## Deferred

## Case 129 — Slice 3b: Work Mode, a session of its own

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders since case 29, then 64, 78, 93, 107, 116, without `kind`, `estimates` or `tags`; two of the three lint orphans. The draft in `docs/migration/` still has to be reconciled with case 59.3 — no separate `plan.md`, the `tasks` blocks of the Spec — and with the fork clause. Case 101.1 gives a placeholder a way to be filled.

> **problem:**
> The phase the harness spends most of its time in is the one phase with no ratified rule. It needs a Plan Mode of its own; the owner set it apart on 2026-09-14 (session N) as the next session's whole agenda, and this session closes the rest of the Frontier (Cases 122–128).

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: The rule of Work Mode — the Spec as tasks with code, the ticked boxes, what a subagent may do, and the fork that comes back as a Case; the Plan Mode of the next session
  - slug: rule-subagent-guppi
    type: rule
    purpose: Governs Work Mode's subagents — they execute the Spec's tasks, never decide, and return a fork as a Case; the Plan Mode of the next session
```
