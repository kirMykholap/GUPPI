<!-- approved 01:36:22 · session e5526707 -->

# Spec — session 1448, 2026-10-06

## Case 692 — A refusal for own text before a round or a Case is cleared by one showing again

> **context:**
> The `Stop` run `uv run guppi casecheck` refuses a reply that shows a round of `case-guppi` when the main agent wrote text in the turn before its last tool call, by `texts_before_last_call` of `guppi/casecheck.py` (case 562). The turn starts at the person's message or a returned answer, by `opens_turn` of `guppi/ledger.py`, and a refusal of a `Stop` hook does not open a turn, so a text written before a tool call stays in the turn after every refusal. Showing the round again cannot remove it, yet the refusal tells the agent to do just that. In this session the main agent wrote a status note before it dispatched `case-guppi` for Case 691; the transcript holds the same refusal three times, quoting that note, and `LIMIT`, three, let the fourth showing through, so the person saw one round four times. The check of the layout of a showing (case 611) calls the same `texts_before_last_call`, and its refusal tells the agent to move that text after the horizontal rule, which a text written before a tool call cannot be. The person chose that the check judges only texts written after the round came back, and after a refusal only what follows it; that the check of a shown Case takes the same fix, applied to the summary of `case-guppi`; and that the limit of three stays. Case 692.1 replaces the Criterion of `estimate-case-check-refuses-text-before-a-round` and Case 692.2 that of `estimate-case-check-refuses-text-outside-the-list`, and sets the `purpose` of each anew, since each names text before the last tool call; their `method` lines name the tests and stand. Case 692.1 also changes the Purpose of `rule-case-check` and its `purpose` field for both sub-cases. The Criterion of `estimate-case-check-judges-a-showing-after-a-refusal` speaks of the count of refusals and of the reasons it counts; the count stays at three and a text before a round or outside a showing is still such a reason, so it stands. The check finds its last refusal by `refusals` of `guppi/ledger.py`, the one judgment of the refusals, which it already calls to count them, so no second test of a refusal record is written; `estimate-ledger-write-lifts`, `estimate-prespec-onward-sends-the-agent-on` and `estimate-retro-onward-sends-the-agent-to-the-handoff`, whose Criteria rest on that one judgment, stand. The bound of the turn does not change, only what is judged inside it, so `estimate-ledger-write-names-the-kind-of-a-user-record`, whose Criterion sets the turn the check reads for a round, stands. Case 692.2 knows a summary by one function, a first line that opens with `**Built:**`, which `summary_findings` of `guppi/casecheck.py` calls too in place of its own test, as `is_round` is shared for a round; the behaviour of that check does not change, so `estimate-case-check-sends-back-a-summary-without-the-case-name` stands. `LEDGER_LINE` of `guppi/casecheck.py` is a copy of `PREFIXES` of `guppi/ledger.py`; Case 692.1 drops it and imports `PREFIXES` (`rule-one-judgment-one-implementation`), and the tests of the check that read the `ratification` of a Case cover it with no promise changed. A Grep `estimate-case-check-refuses-text-before-a-round|estimate-case-check-refuses-text-outside-the-list|texts_before_last_call` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `vault/wiki/log.md`, not read, `guppi/casecheck.py`, which enters through its tasks, `vault/wiki/rules/rule-case-check.md`, whose hits are its `estimates` list and History, and `vault/wiki/estimates/estimate-case-check-refuses-text-outside-the-list.md`, which Case 692.2 changes. A Grep `(nothing before|text of (the main agent's|your) own|before the round|before a round)` over `vault/wiki/` and `.claude/` printed `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-case-check-judges-a-showing-after-a-refusal.md`, `vault/wiki/estimates/estimate-case-check-refuses-text-outside-the-list.md`, `vault/wiki/estimates/estimate-case-check-refuses-text-before-a-round.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/insights/insight-case-form-chat-form-read-by-no-script.md`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-case-check.md`, `vault/wiki/lessons/lesson-orchestration-own-text-before-a-round.md`, `vault/wiki/lessons/lesson-sendmessage-answers-open-a-turn-of-their-own.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md` and `vault/wiki/estimates/estimate-spec-capture-offers-the-fork.md`. The sentence of `rule-orchestration`, its render `orchestration.md` and `estimate-orchestration-shows-the-built-case` that a refused round is shown again with nothing before it stands, and with this Case that showing passes; the hits in `rule-case-protocol`, the insight and `log.md` are History; the two lessons tell what happened in past sessions; the hit in `estimate-spec-capture-offers-the-fork` is about another moment. Case 691 of this session sets what the ledger hook does at the same `Stop`; this Case sets only what `uv run guppi casecheck` judges and leaves the ledger hook as it stands, and it takes on the `LEDGER_LINE` of `guppi/casecheck.py` that Case 691 left to it.

> **problem:**
> The check refuses a round or a Case for a text written before a tool call, which no showing again can remove, so the person sees one round or Case up to four times.

> **recommend:**
> - **Which texts before the round does the check refuse?**
>   - Recommended: (b) only texts written after the round came back, and after a refusal only what follows it.
>   - Answer: agreed, (b).
> - **Does the check of a shown Case get the same fix?**
>   - Recommended: (a) the same fix, in this Case, as a sub-case of its own.
>   - Answer: agreed, (a).
> - **How many refusals before a showing is let through?**
>   - Recommended: (a) keep three.
>   - Answer: agreed, (a).

### Case 692.1 — A round is judged by the texts after it came back and after the last refusal

> **given:**
> `guppi/casecheck.py`: the `Stop` run that judges how a round is shown.
> **＋** `guppi/ledger.py`: `refusals`, the one judgment of the refusals, and `PREFIXES`, the openings of a ledger line.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `rule-case-check`: the rule of the check, whose Purpose names the change.
> **＋** `estimate-case-check-refuses-text-before-a-round`: its Criterion is replaced whole.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the count of refusals, which stands.
> **＋** `rule-prespec`: the rule of `/pre-spec`, whose `prespec` line ends the judgment of text before a tool call.
> **＋** `/hi` and `.claude/skills/wait-what/SKILL.md`: where the main agent puts its own questions and re-pitches, with no round.

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that `is_round` of `guppi/casecheck.py`, the one test of a round, finds one; it comes back in the `tool_result` of an `Agent` call, or in the returned answer that opens the turn.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn after the first round of the turn came back and before its last tool call.
> **＋** When the turn holds a refusal of `uv run guppi casecheck`, judged by `refusals` of `guppi/ledger.py`, it judges only the texts after the last such refusal, so a round shown again with nothing before it passes.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** A text the main agent wrote in the turn before the first round came back is not judged.
> **－** Text after the last question and one horizontal rule is not judged.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** With `stop_hook_active` set a round shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** It stores nothing and writes no file.

```then
update:
- slug: estimate-case-check-refuses-text-before-a-round
  set:
    status: pending
    purpose: Whether the Stop run of the Case check refuses a reply that shows a round of case-guppi after a text of the main agent's own written after the round came back, judges only what follows its last refusal in the turn, judges only the first line of the reply after pre-spec, and leaves a turn with no round alone
  change: the Criterion replaced whole — only texts written after the round came back and after the last refusal of the check are judged, so one showing again clears a refusal
- slug: rule-case-check
  replace:
  - old: a round of `case-guppi` from being shown after a text of the main agent's own (case 562), and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` (case 611)
    new: a round of `case-guppi` from being shown after a text of the main agent's own written after the round came back (case 562), and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` or written after the summary of `case-guppi` came back (case 611), each judged only by what follows the last refusal of the check in the turn, so that one showing again clears a refusal (case 692)
  set:
    purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi from being shown after a text of the main agent's own written after the round came back, a Case from being shown with a text of the main agent's own outside the list under its heading and its ratification or written after the summary of case-guppi came back, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built
  change: the check judges a text before a round or a Case only after the round or the summary came back and after its last refusal in the turn
```

```tasks
- [ ] update `estimate-case-check-refuses-text-before-a-round`
- [ ] update `rule-case-check`
- [x] `guppi/casecheck.py`: one function gives the texts the main agent wrote in the turn before its last tool call, after the first text given back that a predicate finds and after the reply that the last refusal of `uv run guppi casecheck` follows, by `refusals` of `guppi/ledger.py`; `round_opening` calls it with `is_round`, in place of `texts_before_last_call`; the module docstring and the docstring of `round_opening` say so.
- [x] `guppi/casecheck.py`: `LEDGER_LINE` goes, and its two readers import `PREFIXES` of `guppi/ledger.py`.
- [x] `tests/test_casecheck.py`: a text before the `Agent` call that brought the round back passes; a text after the round came back and before a later tool call is refused; a round shown again with nothing before it after a refusal of the check passes; a reply that opens with a line of its own after a refusal is refused; a round given back in the returned answer that opens the turn leaves every text of the turn judged.
- [ ] read `estimate-case-check-refuses-text-before-a-round`
```

### Case 692.2 — A shown Case is judged by the texts after its summary came back and after the last refusal

> **given:**
> `guppi/casecheck.py`: the `Stop` run that judges the layout of a showing.
> **＋** `guppi/ledger.py`: `refusals`, the one judgment of the refusals.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `estimate-case-check-refuses-text-outside-the-list`: its Criterion is replaced whole.
> **＋** `estimate-case-check-sends-back-a-summary-without-the-case-name`: the check of a summary, whose test of a summary is shared and which stands.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the count of refusals, which stands.
> **＋** `.claude/settings.json`: registers the `Stop` run of the check.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form, and `uv run guppi casecheck` runs on it, as `.claude/settings.json` registers it.

> **then:**
> `uv run guppi casecheck` exits 2 when a line that is not blank stands in the reply before its first Case heading.
> **＋** It exits 2 when a line stands between a Case heading and the next Case heading or the horizontal rule `---` that is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote, its `> **ratification:**` line and the `>` lines after it.
> **＋** It exits 2 when the main agent wrote text in the turn of the reply after the first summary of `case-guppi` came back and before its last tool call; a summary is a text given back to an `Agent` or `SendMessage` call whose first line that is not blank opens with `**Built:**`, in the `tool_result` of an `Agent` call or in the returned answer that opens the turn.
> **＋** When the turn holds a refusal of `uv run guppi casecheck`, judged by `refusals` of `guppi/ledger.py`, it judges only the texts after the last such refusal, so a Case shown again with no text of its own before its last tool call passes.
> **＋** Its reason on stderr quotes the first such text and tells the agent to show the Case again with nothing of its own before it and its own text after the horizontal rule.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases with the stored answer and the check of how a round opens, and a reply that more than one of them refuse gives each reason.
> **－** A text the main agent wrote in the turn before the first summary came back is not judged, and a turn with no summary judges no text before its last tool call.
> **－** Text after the horizontal rule is not judged.
> **－** A reply with no Case heading that holds a section, the acknowledging reply among them, a fence tagged `DIFF`, and a deferred decision in the short form are not judged.
> **－** With `stop_hook_active` set a Case shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** It stores nothing and writes no file.

```then
update:
- slug: estimate-case-check-refuses-text-outside-the-list
  set:
    status: pending
    purpose: Whether the Stop run of the Case check refuses a reply that shows a Case with a text of the main agent's own before its first Case heading, under a heading outside the list and the ratification, or written after the summary of case-guppi came back and before the last tool call of the turn, judging only what follows its last refusal in the turn
  change: the Criterion replaced whole — only texts written after the summary came back and after the last refusal of the check are judged, so one showing again clears a refusal
```

```tasks
- [ ] update `estimate-case-check-refuses-text-outside-the-list`
- [x] `guppi/casecheck.py`: one function tells a summary of `case-guppi`, a text whose first line that is not blank opens with `**Built:**`, and `summary_findings` calls it in place of its own test; `showing_layout` calls the function of Case 692.1 with it, in place of `texts_before_last_call`, which goes; its reason tells the agent to show the Case again with nothing of its own before it and its own text after the horizontal rule; the module docstring and the docstring of `showing_layout` say so.
- [x] `tests/test_casecheck.py`: a text before the call that brought the summary back passes; a text after the summary came back and before the sending is refused; a Case shown again with nothing of its own before the last tool call after a refusal of the check passes; a turn with no summary judges no text before its last tool call.
- [ ] read `estimate-case-check-refuses-text-outside-the-list`
```

## Case 693 — The read rule for the saved transcripts covers their folder itself

> **context:**
> The allow list of `.claude/settings.json`, rendered from `rule-permissions`, lets every agent read this project's saved transcripts without a prompt through one rule, `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`, added by case 656 so that `case-guppi` can search them. In this session the person saw the client ask for permission at a Grep of a subagent, and confirmed that the prompt named the transcripts folder. The transcript of the subagent `case-guppi` of this session, `agent-a31d1300c6c7c12ad.jsonl`, shows two Greps there: one whose path was the folder itself, sent at 21:19:46 and answered at 21:20:10, and one whose path was a file under it, answered after 3 seconds; the Greps of the subagent of Case 691 over `vault/wiki/rules/` and the repository root whose times were read, in its transcript `agent-aa462e55a2a73f942.jsonl`, were answered in under a second, so the hook `guppi grepguard`, which adds the Decision-page filter to a Grep over the wiki and decides no permission, did not cause the wait. A likely cause, not proven, is that a rule ending in `/**` names what lies inside the folder and not the folder itself; the Purpose of `rule-permissions` already says that Claude Code applies a `Read` rule to Grep and Glob best-effort. The person chose a second read rule that names the folder itself, beside the present one, and nothing else on the allow list. The folder name follows where this repository sits on the person's disk, `C:\PROJECTS\GUPPI`; on another install both rules match nothing. The person chose to leave that not done here: it waits for `rule-morph`, the draft rule of the initiation at install, deferred by case 239, whose `purpose` named only the category set; at pre-spec the person chose that this Case widens that `purpose` to the name of the transcripts folder in the read rules, and the Purpose of `rule-permissions` points there. The defer of `rule-morph` stands, since this Case does not take it up; `rule-guppi-config` already says that the questions asked at install stay with `rule-morph` and stays true; `vault/wiki/backlog.md` is rendered from the pages by `guppi backlog` and follows the new `purpose` at its next run. A Grep `rule-morph` over `vault/wiki/` printed `vault/wiki/brief.md` and `vault/wiki/log.md`, not read, `vault/wiki/backlog.md`, `vault/wiki/entities/entity-sprint-migration.md`, whose line names the category set as case 239 set it and stays true, and `vault/wiki/rules/rule-guppi-config.md`. The Criterion of `estimate-permissions` speaks of a search under the folder and leaves the folder itself unclear, so this Case replaces it whole and sets its `method` anew. A file rendered from a Rule page changes at the librarian's render after the session (case 690.2), so no search of this session runs under the new rule: at pre-spec the person chose that the live probe is the person's word in a session after the librarian's render, and the Estimate stays `pending` until then. `estimate-orchestration-says-when-a-rendered-change-lands` checks that the reply that acknowledges such a Case says so; its Criterion speaks of that reply, which this Case does not change, so it stands. A Grep `permissionDecision|allow list|without asking|permission prompt` over `vault/wiki/rules/` and `.claude/` printed only `vault/wiki/rules/rule-permissions.md`, so no other rule sets whether a tool call asks. A Grep `c--PROJECTS-GUPPI|saved transcript` over `.claude/`, `vault/wiki/`, `guppi/` and `tests/` printed `.claude/settings.json`, `vault/wiki/log.md`, not read, `vault/wiki/lessons/lesson-transcript-keeps-the-text-before-a-tool-call.md`, whose hit is its `source` field and stands, `vault/wiki/rules/rule-permissions.md` and `vault/wiki/estimates/estimate-permissions.md`; no frame text and no test names the folder, so no test changes. Case 691 of this session changes `rule-ledger-write` and the ledger hook, and touches neither page of this Case.

> **problem:**
> A search whose path is the saved transcripts folder itself still makes the client ask for permission, though the allow list was meant to let every search there run without a prompt.

> **recommend:**
> - **Which search asked for permission**
>   - Recommended: (a) the records folder if the prompt named the `.claude\projects` path, otherwise (c), treat the records folder as the cause.
>   - Answer: (a), the records folder.
> - **How a search of the records folder stops asking**
>   - Recommended: (a) a second read rule for the folder itself, beside the present one.
>   - Answer: agreed, (a); with the note that these allow rules name the person's own folders and system, so another install of guppi would need its own.
> - **The allow rule on another person's machine**
>   - Recommended: (a) the rule for this machine now; `context` and the Purpose of `rule-permissions` say that another install needs its own folder name, which waits for `rule-morph`.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) replace the Criterion of `estimate-permissions` so it names the folder itself and everything inside it, checked by the person's word in Work Mode of this session after the render.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, the live probe of `estimate-permissions` cannot run in Work Mode of this session, since a rendered file changes at the librarian's render after the session; the person chose that the probe runs in a session after the librarian's render, the Estimate staying `pending` until then.
>   - Taken: the `method` of `estimate-permissions` names a session after the librarian's render and the person's word there.
> - **Change**
>   - Asked: at pre-spec, the `purpose` of `rule-morph` names only the category set, not the questions of the install; the person chose that this Case widens it to the name of the transcripts folder in the allow list.
>   - Taken: an `update` of `rule-morph` widens its `purpose` and its Purpose, and the new text of `rule-permissions` says that its initiation at install sets the folder name.

> **given:**
> `rule-permissions`: the rule of the allow list, whose Render is the allow list of `.claude/settings.json`.
> **＋** `estimate-permissions`: the check of the allow list, whose Criterion is replaced whole.
> **＋** `.claude/settings.json`: the rendered settings, whose allow list names the working files of the session under `vault/raw/**` and `vault/wiki/brief.md`.
> **＋** `tests/test_render.py`: its JSON case fixes the shape of the rendered block.
> **＋** `rule-morph`: the draft rule of the initiation at install, whose `purpose` is widened.
> **＋** `.claude/agents/case-guppi.md`: the agent file of `case-guppi`, which sets its permission mode.
> **＋** `rule-spec-reconcile`: its guard keeps the writes of `case-guppi` inside `cases/`.
> **＋** `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`: the read rules for `~/.claude/projects/c--PROJECTS-GUPPI`, the folder of this project's saved transcripts, and for what lies inside it.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
> **＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder `~/.claude/projects/c--PROJECTS-GUPPI` itself as its path, or a path under it.

> **then:**
> The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
> **＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
> **＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
> **＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
> **＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
> **＋** `case-guppi` writes the file of its Case in the mode `permissionMode: acceptEdits` of `.claude/agents/case-guppi.md`, with no prompt in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/`.
> **＋** A Read, Grep or Glob whose path is `~/.claude/projects/c--PROJECTS-GUPPI` itself or a path under it runs with no prompt, in Plan Mode too.
> **－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI`.

```then
update:
- slug: rule-permissions
  replace:
  - old: '"Read(~/.claude/projects/c--PROJECTS-GUPPI/**)"'
    new: |-
      "Read(~/.claude/projects/c--PROJECTS-GUPPI)",
            "Read(~/.claude/projects/c--PROJECTS-GUPPI/**)"
  - old: and whether a search there still asks is the person's word (case 656).
    new: 'and whether a search there still asks is the person''s word (case 656). A Grep whose path was that folder itself asked all the same in session 1448, so a second rule names the folder itself beside the rule for what lies inside it (case 693). The folder name follows where this repository sits on the person''s disk: another install needs its own name in both rules, and that is not done here; it waits for [[rule-morph]], whose initiation at install sets the folder name (case 693).'
  change: the folder of the saved transcripts itself joins the allow list for reading, beside what lies inside it; another install needs its own folder name, left to rule-morph
- slug: estimate-permissions
  set:
    status: pending
    method: the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of work.md in Work Mode, recorded in the estimate line; the live probe of the transcripts is the person's word on the client's prompt, in a session after the librarian's render, at a Grep of a subagent whose path is the folder ~/.claude/projects/c--PROJECTS-GUPPI itself and at one whose path is a file under it, recorded in the estimate line — never the agent's, which cannot see the prompt; the Estimate stays pending until the person gives that word
  change: the Criterion replaced whole — the allow list also names the folder of the saved transcripts itself, and a search with that folder as its path runs with no prompt
- slug: rule-morph
  replace:
  - old: so a changed set rewrites no rule;
    new: so a changed set rewrites no rule; it also sets the name of this project's folder of saved transcripts under ~/.claude/projects in the read rules of the allow list of [[rule-permissions]], which name the folder of one machine until then (case 693);
  set:
    purpose: 'The initiation at install: the person sets the category set of the project — the development set entity, rule, estimate by default — and the harness holds it as data, so a changed set rewrites no rule; it also sets the name of this project''s folder of saved transcripts under ~/.claude/projects in the read rules of the allow list of rule-permissions, which name the folder of one machine until then (case 693); the categories discussion of session 1119, raw/2026-09-17/1119/categories-discussion.md; Slice 5'
  change: the initiation at install also sets the name of the transcripts folder in the read rules of rule-permissions
```

```tasks
- [ ] update `rule-permissions`
- [ ] update `estimate-permissions`
- [ ] update `rule-morph`
- [ ] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-permissions`
```

## Case 694 — The ledger hook asks about a lesson's mark without naming Cases

> **context:**
> The `Stop` hook `uv run guppi ledger` asks the agent whether a Case of the session fixed the cause of a lesson that no mark links to a Case. It asks at two moments. First, it holds once a lesson line written after decision lines of the session (case 682.1, `held_message`). Second, it reminds the agent after the write when fresh decision lines follow a lesson that has no mark (case 685.1, `reminder_message`). Both messages list the Cases through one function, `named_cases` of `guppi/ledger.py`. The hold lists every Case whose decision lines stand before the lesson. The reminder lists every Case of the fresh decision lines after it. The hook cannot judge which Case is related to a lesson. The ledger of session 0104 holds two Retro lessons, at lines 47 and 48, after decision lines of nineteen Cases, 685.1 to 690.3; the brief records that the hold named all nineteen, once for each lesson. In this session the ledger holds `lesson-hooks-a-mod-draws-nothing-in-the-mobile-code-tab` at line 1, before the decision lines of Cases 691, 692.1, 692.2 and 693. By `reminder_message`, the reminder after their write names those four Cases, and none of them touches the lesson's subject. The person chose to change both messages, to name no Case and to ask only whether a Case of this session fixed the cause, and to keep the timing: the hold still asks once, and the reminder still comes once a stretch. A stretch ends at the person's next message, and the hook judges whether a line was told by its text (`untold`). With no Case list, the reminder's line is the same for one lesson at every ratification, so a second ratification inside one stretch no longer reminds again for other Cases; the person's answer kept the reminder at once for each message the person sends. Case 694.1 replaces the Criterion of `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, and Case 694.2 that of `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`. Each Criterion promises which Cases its stderr line names. The two lines of each old Criterion that the new one does not carry are its stderr line with the list of Cases and its line on which Cases are named; both are replaced by design, and every other line is carried word for word. The then lines of the two sub-cases share many words because the hold and the reminder are two messages of one hook, checked by two Estimates. Each sub-case states its own message, so the likeness stands. The `purpose` and `method` of both Estimates state no list of Cases, so they stand. The Purpose of `rule-ledger-write` says that the hook asks whether a Case of the session closed the cause and reminds the agent; it names no list, so it stands, and this Case does not touch that page, which Case 691 of this session changes. Case 691 and Case 692 change other functions of `guppi/ledger.py`; this Case changes only the two stderr lines and their docstrings. A Grep `has no mark|held —|fix its cause` over `guppi/`, `tests/`, `.claude/` and `vault/wiki/` printed `guppi/ledger.py`, `guppi/ratified.py`, `tests/test_ledger.py`, `tests/test_onward.py`, `vault/wiki/estimates/estimate-ledger-write-asks-for-the-mark-of-a-lesson.md` and `vault/wiki/estimates/estimate-ledger-write-reminds-of-the-mark-on-a-decision-line.md`. The hit in `guppi/ratified.py` is a docstring about the text a Case file held, not about a lesson, so it stands. The hit in `tests/test_onward.py` is a sample refusal of the ledger hook in a test of `guppi/onward.py`. By its docstring, that hook acts on any line the ledger hook sent back, not on its words, so the sample stands. `orchestration.md` sets what the reply after the reminder holds and names no Case of the message, so it stands.

> **problem:**
> The question about a lesson's mark lists every candidate Case, nineteen at the end of a session, though the hook cannot tell which of them relates to the lesson. The list is noise, and it suggests a link where there is none.

> **recommend:**
> - **Which question does the change cover?**
>   - Recommended: (a) both the hold and the reminder, one sub-case per Estimate, through the one shared function.
>   - Answer: agreed, (a).
> - **Which Cases should the question name?**
>   - Recommended: (a) name no Case; the message asks whether a Case of this session fixed the cause of the lesson, and the rest of the message stays.
>   - Answer: agreed, (a).
> - **Should the reminder come again at later ratifications?**
>   - Recommended: (a) keep the timing as it is; only the wording changes.
>   - Answer: agreed, (a).

### Case 694.1 — The hold of an unmarked lesson names no Case

> **given:**
> `guppi/ledger.py`: the ledger hook, whose `held_message` gives the stderr line of the hold.
> **＋** `tests/test_ledger.py`: the tests of the ledger hook.
> **＋** `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: its Criterion is replaced whole.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: the reminder after the write, which Case 694.2 sets.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

> **then:**
> At the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
> **＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did a Case of this session fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged."
> **＋** The stderr line names no Case, however many decision lines stand before the lesson line.
> **＋** The line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript.
> **＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
> **－** An unmarked line never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
> **－** The hook holds no lesson line that precedes every decision line of the session, no line it refuses for its prefix or cannot parse, and no line that the ledger of some session already holds.
> **－** The hook never holds a decision line for its `{addresses:...}`: it writes it, and the reminder after the write is `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`.
> **－** A session with no `hi` gets no question. The flag `stop_hook_active` changes nothing here, but when it is set and the transcript is unreadable, the hook lets the line land as it stands.

```then
update:
- slug: estimate-ledger-write-asks-for-the-mark-of-a-lesson
  set:
    status: pending
  change: the Criterion replaced whole — the question of the hold names no Case
```

```tasks
- [ ] update `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
- [x] `guppi/ledger.py`: `held_message` takes the slug alone and asks whether a Case of this session fixed the cause; `named_cases` goes once no caller is left; the module docstring and the docstring of `held_message` say that the stderr line names no Case.
- [x] `tests/test_ledger.py`: the held line's stderr line names no Case with decision lines of several Cases before it; the test of the Cases named in first-seen order goes; the other tests of the hold build the message from the slug alone.
- [ ] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
```

### Case 694.2 — The reminder of an unmarked lesson names no Case

> **given:**
> `guppi/ledger.py`: the ledger hook, whose `reminder_message` gives the stderr line of the reminder.
> **＋** `guppi/materialize.py`: its `unlinked_lessons` judges which lessons no mark links to a Case.
> **＋** `tests/test_ledger.py`: the tests of the ledger hook.
> **＋** `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`: its Criterion is replaced whole.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` writes fresh decision lines of the reply just finished, and a `lesson[<slug>]` line stands before them, in the session's ledger or among the lines the same `Stop` writes, with no `{addressed_by:...}` and no decision line after it that carries `{addresses:<slug>}`.

> **then:**
> The hook writes every line of the `Stop` as it would without the reminder, and holds back no line for the mark.
> **＋** After the write, for each such lesson the hook exits 2 and prints: "ledger: lesson[<slug>] has no mark — did a Case of this session fix its cause? Then write the decision line of the Case or sub-case that fixed it again with {addresses:<slug>} added, alone in a LEDGER block; otherwise go on without it."
> **＋** The stderr line names no Case, however many fresh decision lines follow the lesson.
> **＋** The stderr line is printed only when it does not already stand in a refusal of the hook since the person's last message.
> **＋** A decision line written again with `{addresses:<slug>}` lands beside the first line, the hook reminds of that lesson no more, and `guppi materialize` gives the lesson entry `addressed_by`.
> **＋** The hook judges which lessons no mark links to a Case by one function of `guppi/materialize.py`, over the ledger lines in their order.
> **－** A lesson that carries `{addressed_by:...}`, that a decision line after it marks, or that stands after every fresh decision line brings no reminder; nor does a fresh lesson line that the same `Stop` holds back or refuses.
> **－** A `defer` line, and a decision line from an earlier text of the transcript, bring no reminder.
> **－** A session with no `hi` gets no reminder. With `stop_hook_active` set and a transcript the hook cannot read, the lines land and the hook prints nothing.

```then
update:
- slug: estimate-ledger-write-reminds-of-the-mark-on-a-decision-line
  set:
    status: pending
  change: the Criterion replaced whole — the reminder names no Case
```

```tasks
- [ ] update `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
- [x] `guppi/ledger.py`: `reminder_message` takes the slug alone and asks whether a Case of this session fixed the cause; `unaddressed` still finds the lessons that fresh decision lines follow; the module docstring and the docstrings of `unaddressed` and `reminder_message` say that the stderr line names no Case and is told once a stretch.
- [x] `tests/test_ledger.py`: the reminder names no Case with fresh decision lines of several Cases after the lesson; the tests of the Cases named in first-seen order and of a reminder told again for other Cases in one stretch go; the other tests of the reminder build the message from the slug alone.
- [ ] read `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`
```

## Case 695 — The ledger hook refuses aloud a line of a LEDGER block that is no record

> **context:**
> The `Stop` hook `uv run guppi ledger` takes from a block tagged `LEDGER` only the lines that open with `- decision[`, `- estimate[` or `- lesson[`, by `ledger_lines` of `guppi/ledger.py`, and skips every other line of the block without a word. In session 0104 a reading line of Retro was written as `- estimate-` with no `[`; it was lost unseen and written again as line 49 of that session's ledger, which holds it. The lesson `lesson-ledger-block-written-with-a-placeholder-line` records an earlier stub line of a block that the hook skipped the same way. The person chose that every non-blank line of a `LEDGER` block that is no record line is refused aloud, with its own stderr line, told only when it stands in the reply just finished, as a line the grammar cannot read is told (case 552.2), and checked by a new Estimate: Case 695.1. The hook judges such lines also when the reply holds no fresh record line, since it returns early today when it has none. This Case replaces Case 691, which was ratified whole and is built again with sub-cases after the findings of `/pre-spec` and the person's answer to a further round; its decision lines carry `{supersedes:case 691}`.
>
> `ledger_lines` itself does not change: a Grep `\bledger_lines\(` over `guppi/` printed `guppi/ledger.py`, `guppi/onward.py` and `guppi/ratified.py`, and the two other hooks read the record lines through it as before; the new judgment lives beside it and reads `PREFIXES` of the same module. A Grep `LEDGER_LINE = ` over `guppi/` printed `guppi/casecheck.py`, which holds `LEDGER_LINE`, a second copy of `PREFIXES` for the `ratification` of a Case file; by the finding of `/pre-spec`, Case 692 of this session, which changes `guppi/casecheck.py`, imports `PREFIXES` from `guppi/ledger.py` and drops `LEDGER_LINE`, so this Case does not touch that module. This Case sets only what the ledger hook does with a line at `Stop` and how Retro answers its refusal, not the form of a reply that shows a round or a Case, which Case 692 sets. A Grep `LEDGER.{0,200}(skipped|dropped|ignored|silently)` over `vault/wiki/`, `.claude/` and `guppi/` printed `vault/wiki/brief.md`, not read, `vault/wiki/lessons/lesson-ledger-block-written-with-a-placeholder-line.md` and `vault/wiki/lessons/lesson-ledger-ratification-with-a-new-item-lost-its-block.md`; both lessons tell what happened in a past session and stay true. The sentence of `rule-ratification` that a record is such a line inside a `LEDGER` block, and a line elsewhere a preview, stays true. The Criterion of `estimate-ledger-write-lifts` speaks only of record lines that land, and that of `estimate-ledger-write-refuses-a-line-it-cannot-read` only of lines that open with the bracket, so both stand.
>
> `rule-orchestration` sets a line written again only for the reminder of a lesson with no mark (case 685.1) and for a held decision line (case 688.7), which this Case does not touch; the general sentence that the answer to a refusal of the ledger hook writes the refused lines again stands only in the Render of `rule-retro`, for the answer after the reply that ends Retro. There a refused note written again would be refused again, while the new stderr line asks to leave it out; the person chose that Retro leaves such a line out and goes on to `/handoff` when nothing is left to write: Case 695.2, which changes the Render of `rule-retro`, replaces the Criterion of `estimate-retro-runs-on-to-the-handoff` and sets its `purpose` anew, since it names the refused line written again; its `method`, a run read by hand, names no such promise and stands. A Grep `refused lines? (written )?again|writes the refused|lines written again` over `vault/wiki/`, `.claude/` and `guppi/` printed `vault/wiki/log.md`, not read, `vault/wiki/rules/rule-page-generation.md`, `vault/wiki/rules/rule-retro-onward.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/estimates/estimate-retro-onward-sends-the-agent-to-the-handoff.md`, `vault/wiki/estimates/estimate-retro-runs-on-to-the-handoff.md`, `.claude/skills/retro/SKILL.md`, `guppi/generate.py` and `guppi/onward.py`. The hit in `rule-page-generation` and in `guppi/generate.py` is about decision lines written again with a mark, another thing; the hit in `rule-retro` at its History stays. The Purpose of `rule-retro-onward` says the agent answers a refusal with a reply that writes the refused lines again and must end, which Case 695.2 corrects. The Criterion of `estimate-retro-onward-sends-the-agent-to-the-handoff` and the docstrings of `guppi/onward.py` say the hook sends the agent on again at the end of the next reply, which writes the refused lines again; the hook's judgment does not change, and an answer that writes no line and calls `/handoff` leaves `handoff.md` standing at its `Stop`, where that Criterion already has the hook exit 0, so they stand.

> **problem:**
> A line of a `LEDGER` block whose opening is broken is no record, and the hook drops it with no message, so a reading or a lesson can be lost while the agent believes it was written.

> **recommend:**
> - **Which lines in a LEDGER block are refused aloud**
>   - Recommended: (b) every non-blank line inside a `LEDGER` block that does not open with `- decision[`, `- estimate[` or `- lesson[`; blank lines and blocks with another tag or none stay as now.
>   - Answer: agreed, (b).
> - **Which replies the hook tells about**
>   - Recommended: (a) as for a line the grammar cannot read: told only when it stands in the reply just finished, a line of an earlier text skipped silently.
>   - Answer: agreed, (a).
> - **The message and the check that proves it**
>   - Recommended: (b) its own stderr line, which names the three openings, and a new Estimate on `rule-ledger-write`; the passed Estimate stays as it is.
>   - Answer: agreed, (b).
> - **What the reply after Retro does with a refused line that is no record**
>   - Recommended: (a) the Retro rule and `estimate-retro-runs-on-to-the-handoff` change: a refused record line is written again, a refused line that is no record is left out, and with nothing left the agent goes on to commit and call `/handoff`.
>   - Answer: agreed, (a).

### Case 695.1 — The ledger hook refuses aloud a line of a LEDGER block that is no record

> **given:**
> `guppi/ledger.py`: the ledger hook, which reads the lines of `LEDGER` blocks.
> **＋** `tests/test_ledger.py`: the tests of the ledger hook.
> **＋** `rule-ledger-write`: the rule of the ledger hook, whose Purpose names the new refusal.
> **＋** `estimate-ledger-write-refuses-a-line-that-is-no-record`: the new check of the refusal.
> **＋** `rule-ratification`: the form of a ledger line.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py`, in a session with a `hi`, finds in a `LEDGER` block of a text of the main agent a non-blank line that does not open with `- decision[`, `- estimate[` or `- lesson[`.

> **then:**
> The line is not written to the ledger.
> **＋** The record lines of the same `Stop` are written and judged as before.
> **＋** When the line stands in the reply just finished, the hook exits 2 with one stderr line per such line: "ledger: line not written — a LEDGER block holds only lines that open with - decision[, - estimate[ or - lesson[: <line>. Write it again with that opening, or leave it out."
> **＋** A reply whose `LEDGER` block holds no record line gets the same stderr line for each such line.
> **＋** Each stderr line is told once until the person's next message; a repeat of the same line stays silent.
> **－** A line from an earlier text of the transcript is skipped at every later `Stop` without a word.
> **－** A blank line, and a line in a block with another tag or with none, is not refused.
> **－** Without a `hi` the hook judges no such line.

```then
create:
- slug: estimate-ledger-write-refuses-a-line-that-is-no-record
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook refuses aloud a non-blank line of a LEDGER block that does not open with a record prefix, and says why only for the reply just finished
  method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: '`{addresses:<lesson slug>}` (case 685.1).'
    new: '`{addresses:<lesson slug>}` (case 685.1). It refuses aloud a line of a `LEDGER` block that is no record — a non-blank line that does not open with `- decision[`, `- estimate[` or `- lesson[`, which it skipped without a word before — so a record with a broken opening is not lost unseen (case 695.1).'
  change: the hook refuses aloud a non-blank line of a LEDGER block that is no record line
```

```tasks
- [ ] update `rule-ledger-write`
- [ ] create `estimate-ledger-write-refuses-a-line-that-is-no-record`
- [x] `guppi/ledger.py`: one function beside `ledger_lines`, judged by its `PREFIXES` and the fence functions of `guppi/materialize.py`, gives the non-blank lines of `LEDGER` blocks that are no record; the hook judges them after the `hi` check, also when no fresh record line stands, and prints the stderr line through `untold`; the docstring gains a paragraph.
- [x] `tests/test_ledger.py`: a near-miss line and a note in the reply just finished are refused aloud, a block with only such a line too; a line of an earlier text is silent; the record lines beside it land; a blank line and a line of an untagged block pass; a repeat already told is silent.
- [ ] read `estimate-ledger-write-refuses-a-line-that-is-no-record`
```

### Case 695.2 — Retro leaves out a refused line that is no record

> **given:**
> `rule-retro`: the rule of `/retro`, whose Render `.claude/skills/retro/SKILL.md` changes.
> **＋** `estimate-retro-runs-on-to-the-handoff`: its Criterion is replaced whole.
> **＋** `rule-retro-onward`: the hook that sends the agent on to `/handoff`, whose Purpose names the change.
> **＋** `rule-ledger-write`: the ledger hook, whose refusal the answer meets.
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/work.md` and `raw/<date>/<hi HHMM>/handoff.md`: the files of the session that Retro reads and writes.
> **＋** `vault/wiki/where-to-stop.md`: the conditions of a stop.
> **＋** `rule-ratification`: the form of a ledger line.

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

> **then:**
> Retro asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read —, takes the readings whose moment has come, and decides which lessons to write.
> **＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
> **＋** The agent commits the work when `make style` is clean and `make test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
> **＋** One reply ends Retro: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block with every reading and lesson of `/work` and Retro; it asks the person nothing.
> **－** That reply shows the person no report: no heading, no list and no other paragraph stands before or after the block, since `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro.
> **＋** When the ledger hook refuses a line of that reply, the agent answers with a reply that holds only a `LEDGER` block with each refused record line written again; a refused line of the block that is no record, one that does not open with `- decision[`, `- estimate[` or `- lesson[`, is left out. No other `LEDGER` block follows the reply that ends Retro.
> **＋** When no refused line is left to write, that answer holds no `LEDGER` block, and in it the agent commits the session folder and calls `/handoff`.
> **＋** After that reply, or after the reply that answers a refusal of the ledger hook, in the same turn, the agent commits the session folder and calls `/handoff`.
> **－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`, with a reply that opens with `STOP:` and asks the person instead. The answer to a refusal of the ledger hook is no stop.
> **－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

```then
update:
- slug: rule-retro
  replace:
  - old: that reply holds only a `LEDGER` block with the refused lines written again, and the hook of `rule-retro-onward` then sends you on again (case 596).
    new: that reply holds only a `LEDGER` block with the refused record lines written again, and the hook of `rule-retro-onward` then sends you on again (case 596). A refused line of the block that is no record — one that does not open with `- decision[`, `- estimate[` or `- lesson[` — is left out; when no line is left to write, that reply holds no `LEDGER` block, and in it you commit the session folder and call `/handoff` (case 695.2).
  change: the answer to a refusal of the ledger hook after Retro leaves out a refused line that is no record, and goes on to /handoff when nothing is left to write
- slug: rule-retro-onward
  replace:
  - old: the agent answers that refusal with a reply that writes the refused lines again, a reply that must end,
    new: the agent answers that refusal with a reply that writes the refused record lines again, a reply that must end — or, when only lines that are no record were refused, with a reply that writes none and calls `/handoff` itself (case 695.2) —,
  change: the answer to a refusal of the ledger hook may write no line and call /handoff itself when only lines that are no record were refused
- slug: estimate-retro-runs-on-to-the-handoff
  set:
    status: pending
    purpose: Whether /retro reviews the session with no report and no approval, writes every reading and lesson of the turn in one reply and each refused record line of a refusal of the ledger hook again in one reply that holds only them, a refused line that is no record left out, commits on green and calls /handoff in the same turn, writes no defer, and stops only on a condition of vault/wiki/where-to-stop.md
  change: the Criterion replaced whole — a refused line that is no record is left out of the answer to a refusal of the ledger hook, and with nothing left the answer calls /handoff
```

```tasks
- [ ] update `rule-retro`
- [ ] update `rule-retro-onward`
- [ ] update `estimate-retro-runs-on-to-the-handoff`
- [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-runs-on-to-the-handoff`
```
