<!-- approved 18:47:27 · session 38204912 -->

# Spec — session 2026-09-24 1303

## Case 390 — The acknowledging reply of a re-ratification carries its LEDGER block again

> **context:**
> Since Case 387.2 the `Stop` hook of `rule-spec-write` writes a Case into the Spec only after a reply whose `LEDGER` block holds that Case's decision lines. When a Case is shown again and ratified again, its lines are the same as the ones already written. The ledger hook skips a line that already stands in any `ledger.md` under `raw/` (`guppi/ledger.py`, docstring). So in session 1859 the agent acknowledged the re-ratification of 384–388 without the block, and with the hook live those texts would not have reached the Spec. The schema does not forbid it: the section `## The acknowledging reply` of `rule-case-protocol` is silent on a re-ratification. The code needs no change: `stop()` in `guppi/ratified.py` takes the lines from the reply itself, not from the ledger, finds the last showing of the Case and replaces its section in the plan and in the ratified copy. Repeating the lines does no harm: the ledger does not write them twice. `rule-case-protocol` stands `draft`. No vault query: every item is an `update` with a `ref`. Read against the Case: `rule-spec-write`, `estimate-spec-write-copies-the-ratified-case` and `guppi/ledger.py`; no contradiction. `estimate-case-protocol-acknowledging-reply` speaks of the form of the acknowledging reply, so its Criterion is replaced whole, written in the model of Case 378: no `Given:` and no `－` line on the bounds of the measurement. `estimate-case-protocol-loaded` is not touched: its Criterion, still in the old model, lists the paragraphs of the Render, and the one pass of Slice 3g rewrites it whole (378.1); it is not read before that. `estimate-spec-write-copies-the-ratified-case` already asks for a reply with the `LEDGER` block and is not touched either.

> **problem:**
> A re-ratified Case can stay out of the Spec: the schema lets the reply that acknowledges a re-ratification go without its `LEDGER` block.

> **given:**
> `rule-case-protocol` — the section `## The acknowledging reply` of its Render.
> **＋** `vault/wiki/case-schema.md` — the Render, written by `uv run guppi render`.
> **＋** `estimate-case-protocol-acknowledging-reply` — the Estimate of the acknowledging reply.
> **＋** `rule-spec-write` — its `Stop` hook writes a Case into the Spec after a reply whose `LEDGER` block holds the Case's decision lines.
> **＋** `rule-ledger-write` — the ledger hook, which appends each line once.

> **when:**
> The person ratifies a Case, or ratifies again a Case shown again after its ratification, and the agent writes the reply that acknowledges it.

> **then:**
> The reply has four parts, in this order: the `LEDGER` block first; the heading `## Case N — ratified` and a paragraph `Changes:` — what changes, in one or two sentences; a paragraph `Notes:` — facts that did not enter the Case, omitted when there are none; the heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last.
> **＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` naming the ids, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: Headings and labels in the language of the chat (case 167, supersedes 157).
    new: 'Headings and labels in the language of the chat (case 167, supersedes 157). The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification: the ledger hook does not append a line it already holds, and the hook of `rule-spec-write` writes a Case into the Spec only after a reply that carries its lines (case 390).'
  change: the acknowledging reply of a re-ratification carries the LEDGER block again (case 390, supersedes 389)
- slug: estimate-case-protocol-acknowledging-reply
  set:
    status: pending
  change: the Criterion replaced whole — the LEDGER block of a re-ratification (case 390)
```

```tasks
- [ ] update `rule-case-protocol` — one sentence at the end of `## The acknowledging reply` in the Render
- [ ] update `estimate-case-protocol-acknowledging-reply` — the Criterion replaced whole by the `when` and `then` of this Case
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-acknowledging-reply` — by hand, the first acknowledging reply of a re-ratification and the ledger after it
- [x] `{supersedes:case 389}` on the ledger line of `rule-case-protocol` — the defer taken up
```

## Case 391 — The frame of a Case is checked by the agent `frame-guppi` before the showing

> **context:**
> The agent writes a Case from what it has in view: the dialogue, the rule page, the code. The pages the Case changes or runs beside are not read against it before the showing. A contradiction is found only by pre-spec, after the ratification, and its fix costs a showing again. It happened in sessions 1809 (Cases 175 and 164) and 1859 (eight contradictions in Case 387): the two lessons of `insight-workflow-case-written-without-reading-the-pages-it-changes`, `open`, severity 2. If the main agent reads the frame itself, that is 20–25 thousand tokens of Opus per Case, measured in this session from its transcript, and they stay in the context to the end of the session. `ask-guppi` does not fit: it searches by meaning, opens every dispatch with the Grep of the index lines of all rules and runs on Opus; over its 59 past dispatches before a `create` the median input is 205 772 tokens a dispatch. So the frame is read by a separate narrow agent on Sonnet. It gets the draft of the Case in the prompt of the call, not from the chat: `transcript_texts` in `guppi/ledger.py` takes only the text blocks, so the call is not a showing. State: `rule-plan-mode` `built`, its Estimates speak of the vault's answer before a `create` and of naming the Estimates; `rule-case-protocol` `draft`; `rule-ask` `built`, its Purpose is one entry point of the search by meaning, and the new agent does not search. `estimate-plan-mode-verified` is not touched: its Criterion speaks of the answer before a `create`. `estimate-case-protocol-case-form` speaks of what `context` closes with, which 391.2 extends; it is not touched here, since the one pass of Slice 3g rewrites it whole (378.1), and it is not read before that. No vault query: every `create` line of the ledger carries a `ref`. The four new names are free: a grep over the repository found none. Read against the Case: `rule-ask`, `rule-plan-mode`, `estimate-plan-mode-verified`, `estimate-ask-finds`, `rule-rules-schema` (the fields of a rule with `enforcement: render`) and `rule-render-harness`. One contradiction, taken in: an agent written by `guppi render` is available from the next session (case 139.1), so its reading is in the next session.

> **problem:**
> A Case is shown without being read against its frame, and reading the frame in the main agent fills its context. Is a narrow, cheap agent needed that reads the frame before the showing, and a rule for when to call it?

### Case 391.1 — The agent `frame-guppi`

> **given:**
> `rule-frame-check` — the new rule of the agent, a child of `rule-plan-mode`.
> **＋** `.claude/agents/frame-guppi.md` — its Render, written by `uv run guppi render`.
> **＋** `estimate-frame-check-finds-a-contradiction` — its Estimate.
> **＋** `rule-ask` — the search of the vault by meaning, which the new agent does not do.
> **＋** `rule-render-harness` — renders a rule with `governs` into its file, an agent from the next session.
> **＋** `.claude/settings.json` — the hooks registered on each event.

> **when:**
> The main agent dispatches `frame-guppi` with the lines of a Case's `given` and a few lines on what the Case changes.

> **then:**
> The agent reads each page and file the lines name, the part a line names where it names one, and the Criterion of each Estimate a named page lists in `estimates`.
> **＋** For a Case that adds or changes a hook, it also reads the hooks registered on the same event in `.claude/settings.json` and the rule of each.
> **＋** It answers with a `read:` line of the slugs and paths read, then one numbered line per contradiction — the page or file, the sentence, how the change contradicts it, the fix — or the line `none`.
> **＋** An Estimate whose Criterion speaks of the thing the change touches, and which the lines do not name, is a contradiction.
> **＋** It runs on `model: sonnet` with the tools Read, Grep and Glob.
> **－** It does not search the vault by meaning, and does not open the decision pages or the archive.

```then
create:
- slug: rule-frame-check
  type: rule
  kind: Leaf
  purpose: Prevents a Case from being shown before the pages of its frame are read against it, without the reading filling the main agent's context
  enforcement: render
  governs: .claude/agents/frame-guppi.md
  render_mode: full
  tags:
  - session
  - workflow
  - harness
  sections:
    Purpose: 'Prevents a Case from being shown before the pages of its frame are read against it, without the reading filling the main agent''s context. The agent `frame-guppi` reads the pages and files a Case''s `given` names, on a cheaper model than the main agent, and returns only the contradictions; the main agent still reads itself the pages it edits by a `replace` pair. It does not search the vault by meaning: that is `rule-ask`.'
    Render: |-
      <!-- rule-frame-check -->
      ---
      name: frame-guppi
      description: Read the frame of a Case against it before the Case is shown. The caller gives the lines of the Case's `given` and a few lines on what the Case changes; the agent reads each page and file named and returns the contradictions, numbered, or none.
      model: sonnet
      tools: Read, Grep, Glob
      ---
      You check the frame of one Case before it is shown to the person. The caller's prompt holds the lines of the Case's `given` — one page, module, file or test per line, with the part it names — and a few lines on what the Case changes, which may be a draft of its `when`, `then` and `tasks`. You decide nothing and propose nothing but the fix of a contradiction.

      Read each page and file the lines name, and only those: a page of the vault is found by a Glob `vault/wiki/**/<slug>.md`; where a line names a section, read that section; for a page with an `estimates` field, read the `## Criterion` of each Estimate it lists. For a Case that adds or changes a hook, read also the hooks registered on the same event in `.claude/settings.json` and the rule page of each. Do not search the vault by meaning — that is `ask-guppi`. Do not open `vault/wiki/decisions/` or `vault/archive/`.

      A contradiction is a sentence of a page or a file that the change would make false or that forbids the change, or an Estimate whose Criterion speaks of the thing the change touches and which the lines do not name.

      Answer with nothing else:
      - read: the slugs and paths read, comma-separated
      - one numbered line per contradiction: `N. <slug or path> — <the sentence, quoted short> — <how the change contradicts it> — <the fix>`
      - or the line `none`
      <!-- /rule-frame-check -->
- slug: estimate-frame-check-finds-a-contradiction
  type: estimate
  kind: QA
  purpose: frame-guppi reads the frame it is given and names a contradiction of it, or none
  method: 'by hand: two live dispatches, one whose lines contradict a sentence of a page they name and one whose lines do not; the tokens of each dispatch from its subagent transcript in the estimate line'
  tags:
  - session
  - workflow
  - harness
  ref: rule-frame-check
```

```tasks
- [ ] create `rule-frame-check` — the rule of the agent
- [ ] create `estimate-frame-check-finds-a-contradiction` — the promise of the agent
- [ ] `uv run guppi render`: `.claude/agents/frame-guppi.md`
- [ ] read `estimate-frame-check-finds-a-contradiction` — by hand, two live dispatches in the next session
```

### Case 391.2 — When the agent calls `frame-guppi`

> **given:**
> `rule-case-protocol` — the section on the vault before a `create` in its Render.
> **＋** `vault/wiki/case-schema.md` — the Render, written by `uv run guppi render`.
> **＋** `rule-frame-check` — the agent `frame-guppi` the sentence names.
> **＋** `estimate-case-protocol-checks-its-frame` — the new Estimate of the check.
> **＋** `insight-workflow-case-written-without-reading-the-pages-it-changes` — the Insight the Case sets `actioned`.

> **when:**
> The agent prepares a Case that changes the behaviour of a rule or of a hook, before its first showing in the chat, and again before a showing after its `given` changed.

> **then:**
> The agent dispatches `frame-guppi` with the lines of the Case's `given` and a few lines on what it changes, in the prompt of the call; nothing of the Case stands in the chat before the answer.
> **＋** Each contradiction the answer names is fixed in the Case before it is shown, or the Case says why it stands.
> **＋** The `context` of the Case gives what was read and what was found, or that nothing was found.
> **＋** Before a showing again, the dispatch carries only the lines of `given` added since the last dispatch and the pages changed since.
> **－** A Case that changes no behaviour of a rule or of a hook dispatches nothing.

```then
create:
- slug: estimate-case-protocol-checks-its-frame
  type: estimate
  kind: QA
  purpose: A Case that changes the behaviour of a rule or a hook is checked by frame-guppi before it is shown
  method: by hand, the Cases of a session at its close, their context against the Agent calls of the event log
  tags:
  - session
  - workflow
  ref: rule-case-protocol
update:
- slug: rule-case-protocol
  replace:
  - old: An `update` carries a `ref` and reads the page itself.
    new: An `update` carries a `ref` and reads the page itself. Before the first showing of a Case that changes the behaviour of a rule or of a hook, the agent dispatches `frame-guppi` ([[rule-frame-check]]) with the lines of the Case's `given` and a few lines on what it changes — in the prompt of the call, not in the chat — and fixes each contradiction it returns before the showing, or says why it stands; before a showing again it sends only the lines of `given` added since and the pages changed since. A Case that changes no behaviour of a rule or a hook dispatches nothing; the pages the agent edits by a `replace` pair it reads itself (case 391.2).
  - old: the vault's answer and why an Estimate of the rule is not touched
    new: the vault's answer, what `frame-guppi` found, and why an Estimate of the rule is not touched
  change: the frame of a Case checked by frame-guppi before the showing (case 391.2)
- slug: insight-workflow-case-written-without-reading-the-pages-it-changes
  set:
    status: actioned
    addressed_by: decision-case-391.2
  change: 'actioned: the frame of a Case is checked by frame-guppi before the showing (case 391.2)'
```

```tasks
- [ ] update `rule-case-protocol` — one sentence after the vault query, and the close of `context` in the Language section, in its Render
- [ ] create `estimate-case-protocol-checks-its-frame` — the promise of the check
- [ ] update `insight-workflow-case-written-without-reading-the-pages-it-changes` — `actioned`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-checks-its-frame` — by hand, at the close of the first session with `frame-guppi`
```

## Case 392 — The size of the context after each reply, and a warning past 400 000

> **context:**
> Today the person does not see how full the context window is. In VS Code the indicator in the prompt box shows only past 50%, and `/context` is typed by hand. A hook gets only `transcript_path`, not the size of the context: the answer of the Claude Code documentation (`hooks-guide.md`), brought by the agent `claude-code-guide`. The size can be counted from the transcript: every reply of the model carries `usage` there, and the sum of input, cache read, cache creation and output is the size of the context; the measurement of this session was taken that way. The stdout of a `UserPromptSubmit` hook reaches only the agent: the person did not see the line `hi: 13:03:25 …` after `/hi`. For the person there is the `systemMessage` of a `Stop` hook; the documentation says it is shown to the user, and is silent on `Stop` in VS Code. So the first reading is live: if the line is not seen, Case 392.1 is shown again with the fallback, the line written by the agent, about 20 tokens a reply. By Case 391.2 this Case calls for `frame-guppi`, which exists only from the next session; the agent read the frame itself: the Render of `rule-hook-registry`, the `Stop` and `UserPromptSubmit` keys of `.claude/settings.json` (`guppi ledger`, `guppi ratified`, `guppi event prompt`, `guppi gate`), `rule-bash-guard` as the pattern of a hook rule, and the docstring of `guppi/ledger.py`. Two findings. First, `guppi ratified` may exit 2, and then `Stop` fires again with `stop_hook_active`, so the new hook stays silent on the re-fire, or the line comes out twice. Second, the ledger hook takes the final reply from `last_assistant_message`, since at `Stop` the transcript may not hold the last call yet; so the number is the last call the transcript holds, and may lag one call. Both went into `then`. `rule-hook-registry` stands `built`; its `estimate-hook-registry-rendered` still holds a block of the old model that counts the commands of `UserPromptSubmit`, so 392.4 replaces its Criterion with the live reading of 378.5. `rule-context-size` goes under `rule-harness`, whose Purpose counts the rules outside its pipeline; 392.3 brings that count and `estimate-harness-pipeline` up to date. A rule whose hook only prints has a precedent in `rule-compact-recall`. No vault query: every `create` line of the ledger carries a `ref`. The names `rule-context-size`, `guppi/context.py` and the two Estimate slugs are free: a grep found none.

> **problem:**
> The person sees in the chat neither the size of the context nor its growth over a reply, and nothing stops a session that has grown too large. Are a line after each reply and a warning past 400 000 tokens needed?

### Case 392.1 — A line with the size of the context after each reply

> **given:**
> `rule-context-size` — the new hook rule, a child of `rule-harness`.
> **＋** `estimate-context-size-shown-after-each-reply` — its Estimate.
> **＋** `guppi/context.py` — the count from the transcript; `guppi/cli.py` — the command `guppi context`.
> **＋** `tests/test_context.py` — its tests, on a transcript written by the test.
> **＋** `guppi/ledger.py` — the predicate of a main-agent record, taken out of `transcript_texts` and imported by `guppi/context.py`.
> **＋** `rule-hook-registry` — the `"Stop"` key of its Render.
> **＋** `.claude/settings.json` — the rendered hooks, where `guppi ratified` may exit 2 and fire `Stop` again.

> **when:**
> The `Stop` hook `uv run guppi context` runs after a reply of the main agent and reads the transcript at `transcript_path`.

> **then:**
> The hook prints JSON with a `systemMessage` of one line that opens with `context: <N> tokens (<+D> since the last reply)`.
> **＋** N is the sum of the input, cache read, cache creation and output tokens of the last main-agent API call the transcript holds; D is N less the same sum at the last main-agent call before the person's last prompt.
> **＋** The records of a subagent (`isSidechain`) are not counted.
> **＋** On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, the hook prints nothing.
> **－** The hook never blocks: it exits 0 in every case.

```then
create:
- slug: rule-context-size
  type: rule
  kind: Leaf
  purpose: Prevents a session from running on while the person cannot see how full the context window is
  enforcement: hook
  implementation_ref:
  - guppi/context.py
  - tests/test_context.py
  - .claude/settings.json
  tags:
  - hooks
  - harness
  - session
  sections:
    Purpose: Prevents a session from running on while the person cannot see how full the context window is. In the VS Code extension the context indicator shows only past half of the window, and `/context` is typed by hand; no hook payload carries the size, only `transcript_path`. The size is counted from the transcript, where every API call of the model carries its `usage`.
    How it works: '`uv run guppi context` on `Stop`. It reads the transcript at `transcript_path`, skips the records of a subagent (`isSidechain`), and takes N, the sum of the input, cache read, cache creation and output tokens of the last main-agent call the transcript holds — at `Stop` the last call may not be there yet, so N may lag one call — and D, N less the same sum at the last call before the person''s last prompt. It prints JSON with a `systemMessage`: `context: <N> tokens (<+D> since the last reply)`. On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call carrying `usage`, it prints nothing; it exits 0 always.'
- slug: estimate-context-size-shown-after-each-reply
  type: estimate
  kind: QA
  purpose: After each reply the person sees the size of the context and its change since the last reply
  method: uv run pytest tests/test_context.py; the live reading by hand, the line after the replies of a session in the VS Code chat
  tags:
  - hooks
  - harness
  - session
  ref: rule-context-size
update:
- slug: rule-hook-registry
  replace:
  - old: '"command": "uv run guppi ratified", "timeout": 30 } ] }'
    new: '"command": "uv run guppi ratified", "timeout": 30 }, { "type": "command", "command": "uv run guppi context", "timeout": 30 } ] }'
  change: the Stop hook guppi context registered (case 392.1)
```

```tasks
- [ ] create `rule-context-size` — the hook rule
- [ ] create `estimate-context-size-shown-after-each-reply` — the promise of the line
- [ ] update `rule-hook-registry` — the `Stop` hook `guppi context`, after `guppi ratified`
- [x] `guppi/ledger.py` — the predicate of a main-agent record out of `transcript_texts`, imported by `guppi/context.py`
- [x] `guppi/context.py` — the count of N and D, and the `Stop` output
- [x] `guppi/cli.py` — the command `guppi context`
- [x] `tests/test_context.py` — N and D on a written transcript, a sidechain record skipped, the re-fire silent, no `usage` silent
- [ ] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-context-size-shown-after-each-reply` — `uv run pytest tests/test_context.py`, then by hand in the VS Code chat in the next session
```

### Case 392.2 — A warning past 400 000 tokens

> **given:**
> `rule-context-size` — the rule 392.1 creates.
> **＋** `estimate-context-size-warns-past-the-limit` — its Estimate.
> **＋** `guppi/context.py` — the same count of N; `tests/test_context.py` — its tests.
> **＋** `rule-hook-registry` — the `"UserPromptSubmit"` key of its Render.
> **＋** `.claude/settings.json` — the rendered hooks, where `guppi event prompt` also prints to the agent's context.

> **when:**
> The person sends a prompt and the `UserPromptSubmit` hook `uv run guppi context --prompt` reads the transcript; after the reply the `Stop` hook `uv run guppi context` runs.

> **then:**
> At N of 400 000 or more, the `UserPromptSubmit` hook prints to the agent's context: `context: <N> tokens, past 400 000` and the order to tell the person to close the session with /retro, then /handoff, before the next Case.
> **＋** The agent opens its reply with that recommendation.
> **＋** At N of 400 000 or more, the line of the `Stop` hook ends with `— past 400 000: close the session`.
> **－** Below 400 000 the `UserPromptSubmit` hook prints nothing.

```then
create:
- slug: estimate-context-size-warns-past-the-limit
  type: estimate
  kind: QA
  purpose: Past 400 000 tokens of context the agent tells the person to close the session
  method: uv run pytest tests/test_context.py -k limit; the live reading by hand at the first prompt past 400 000 tokens
  tags:
  - hooks
  - harness
  - session
  ref: rule-context-size
update:
- slug: rule-context-size
  replace:
  - old: it prints nothing; it exits 0 always.
    new: 'it prints nothing; it exits 0 always. At N of 400 000 or more the line ends with `— past 400 000: close the session`, and `uv run guppi context --prompt` on `UserPromptSubmit` prints to the agent''s context the size and the order to tell the person to close the session with /retro, then /handoff, before the next Case; below the limit it prints nothing.'
  change: the warning past 400 000 tokens (case 392.2)
- slug: rule-hook-registry
  replace:
  - old: '"uv run guppi event prompt", "timeout": 30 },'
    new: '"uv run guppi event prompt", "timeout": 30 }, { "type": "command", "command": "uv run guppi context --prompt", "timeout": 30 },'
  change: the UserPromptSubmit hook guppi context --prompt registered (case 392.2)
```

```tasks
- [ ] update `rule-context-size` — the limit in How it works
- [ ] create `estimate-context-size-warns-past-the-limit` — the promise of the warning
- [ ] update `rule-hook-registry` — the `UserPromptSubmit` hook `guppi context --prompt`, after `guppi event prompt`
- [x] `guppi/context.py` — the limit, the `--prompt` output and the ending of the `Stop` line
- [x] `tests/test_context.py` — below and at the limit, on both hooks
- [ ] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-context-size-warns-past-the-limit` — `uv run pytest tests/test_context.py -k limit`, then by hand at the first prompt past 400 000 tokens
```

### Case 392.3 — The Purpose of `rule-harness` names the seven rules outside the pipeline

> **given:**
> `rule-harness` — its Purpose, which names the rules that belong to it.
> **＋** `estimate-harness-pipeline` — the Estimate that reads that Purpose.
> **＋** `rule-context-size` — the child 392.1 adds.
> **＋** `rule-sprint` — its check runs in `make lint`.

> **when:**
> `make lint` and `make test-harness` run, and someone reads the Purpose of `rule-harness`.

> **then:**
> The Purpose says: three rules belong to no phase of the session — the renderer, the page `settings.json` is assembled from, lint — and with them the check of `rule-sprint` runs in `make lint`, in this order: the harness files against their pages, the sprint file against its page, the glossary file against its page, then the pages.
> **＋** The Purpose names seven more rules that belong to it and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, and the hook that shows the size of the context.
> **＋** `make test-harness` is green; the first three steps of `make lint` — `render`, `sprint` and `glossary --check` — exit 0 with no output on the committed tree; the fourth, `guppi lint`, is read by its own Estimates.

```then
update:
- slug: rule-harness
  replace:
  - old: 'Five more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, and the pinned clock of the tests (cases 59.6, 59.8, 127, 145.1).'
    new: 'Seven more belong here and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, and the hook that shows the size of the context (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3).'
  change: the Purpose names the seven rules outside the pipeline (case 392.3)
- slug: estimate-harness-pipeline
  set:
    status: pending
  change: the Criterion replaced whole — seven rules outside the pipeline, no Given (case 392.3)
```

```tasks
- [ ] update `rule-harness` — the rules outside the pipeline in its Purpose
- [ ] update `estimate-harness-pipeline` — the Criterion replaced whole by the `when` and `then` of this Case
- [ ] read `estimate-harness-pipeline` — `make test-harness`, the first three steps of `make lint`, and the Purpose by hand
```

### Case 392.4 — The Criterion of `estimate-hook-registry-rendered` as the live reading of the Render

> **given:**
> `estimate-hook-registry-rendered` — the Estimate of the render of the hooks.
> **＋** `rule-hook-registry` — its target, the `"hooks"` key of `.claude/settings.json`.
> **＋** `.claude/settings.json` — the rendered file.
> **＋** `tests/test_render.py` — the JSON case of the render.

> **when:**
> `uv run guppi render` writes `.claude/settings.json`.

> **then:**
> The `"hooks"` key of `.claude/settings.json` equals the Render of `rule-hook-registry` byte for byte, and every hook the harness runs is registered by one of its lines.
> **＋** `uv run guppi render --check` exits 0 after the render.

```then
update:
- slug: estimate-hook-registry-rendered
  set:
    status: pending
    method: the JSON case of tests/test_render.py; uv run guppi render --check after the render
  change: the Criterion replaced whole — the live reading of the Render, no count of commands (case 392.4)
```

```tasks
- [ ] update `estimate-hook-registry-rendered` — the Criterion replaced whole, the page recut with a `method`
- [ ] read `estimate-hook-registry-rendered` — `uv run pytest tests/test_render.py` and `uv run guppi render --check` after the render
```

## Case 393 — The Case schema: the outer span of a value that opens or closes with a backtick is padded by one space

> **context:**
> The value of a sub-point in the chat is one code span or a fenced block under the sub-point. The schema says: as many backticks as the value needs. But when the value itself opens or closes with a backtick, the outer span needs one space on each side, or its backticks run into those of the value. CommonMark reads it so, `code_value` in `guppi/ratified.py` reads it so, and its docstring says so. The schema is silent, and after the ratification of Case 392.1 the agent wrote such a value without the spaces. The hook of `rule-spec-write` refused it, and the Case was shown and ratified again: the lesson `lesson-spec-write-sub-point-opening-with-a-code-span-unpadded`. The code does not change. A test of the form is added, since `tests/test_ratified.py` has none: a grep for double backticks finds only a value with no backtick at its edge. `rule-case-protocol` stands `draft`. No Estimate is touched: the Criterion of `estimate-spec-write-copies-the-ratified-case` ("each value one code span") stays true, since a padded value is one span, and the new test pins the reading that Estimate already promises, so the Case signs no line of it again; `estimate-case-protocol-loaded`, still in the old model, is left to the one pass of Slice 3g (378.1). The Case changes no behaviour of a rule or a hook, so it calls no `frame-guppi` (391.2). No vault query: the item is an `update` with a `ref`. The lesson gets `{addresses:…}` on the ratification line, since it already stands in this session's ledger. Read against the Case: the Language paragraph of `rule-case-protocol`, where the anchor stands once, `code_value` and `tests/test_ratified.py`.

> **problem:**
> The schema does not say how to write a value that opens or closes with a backtick, and the agent learns it from the refusal of the hook; the ratified Case then does not reach the Spec.

> **given:**
> `rule-case-protocol` — the Language section of its Render, on the form of a sub-point value.
> **＋** `vault/wiki/case-schema.md` — the Render, written by `uv run guppi render`.
> **＋** `guppi/ratified.py` — `code_value`, which reads the value of a sub-point.
> **＋** `tests/test_ratified.py` — its tests.
> **＋** `rule-spec-write` — its `Stop` hook refuses a value that is not one code span.

> **when:**
> The agent writes in the chat a sub-point whose value opens or closes with a backtick, and after the ratification the `Stop` hook of `rule-spec-write` reads it.

> **then:**
> `case-schema.md` says that such a value takes an outer span padded by one space on each side.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: with as many backticks as the value needs, or a fenced block under the sub-point
    new: with as many backticks as the value needs — a value that opens or closes with a backtick takes its outer span padded by one space on each side, as CommonMark reads it — or a fenced block under the sub-point
  change: the outer span of a value that opens or closes with a backtick is padded by one space (case 393)
```

```tasks
- [ ] update `rule-case-protocol` — the form of a value in the Language section of its Render
- [x] `tests/test_ratified.py` — a value that opens and closes with a code span, padded, is read whole; the same value unpadded is refused
- [x] `uv run pytest tests/test_ratified.py`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Deferred

## Case 394 — A sub-point value unpadded at a closing backtick is misread, not refused

> **context:**
> The hook of `rule-spec-write` reads the value of a sub-point with `code_value` in `guppi/ratified.py`, as CommonMark reads a code span. A value that opens with a code span and ends in text, written without the padding spaces, is refused: that is the failure of Case 392.1 in session 1303. A value that opens and closes with a code span, written without them — three backticks on each side — is not refused: CommonMark and `code_value` read it as one span whose edge backticks are eaten, and the hook writes the value without them. The test of Case 393 checks the refusal on the first shape only; the task line of 393 says the same value unpadded is refused, which does not hold for the second shape.

> **problem:**
> A value unpadded at both edges enters the Spec with its edge backticks lost, and nothing says so. Should the hook refuse a span whose content opens or closes with a backtick of its own, beyond what CommonMark reads?

```then
defer:
  - slug: rule-spec-write
    type: rule
    purpose: A sub-point value whose outer span is unpadded and whose content opens and closes with a code span is read with its edge backticks eaten, not refused
```
