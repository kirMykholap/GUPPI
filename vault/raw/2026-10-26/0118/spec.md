<!-- approved 02:41:39 · session 8e24dc1e -->

# Session 0118 — the sprint plugin: the Decision page of a Case replaced by a retired Case

## Case 888 — A Case replaced before its entries applied is written superseded

> **context:**
> When `guppi generate` applies a session, it skips every entry of `materialize.yaml` that carries `superseded_by`, and writes the Decision page of its Case all the same (`apply` of `.guppi/guppi/generate.py`, case 151). `Vault.decision` writes every new page with `status: current`. The earlier page goes `superseded` only later, when the page of the Case that replaced it walks its `supersedes`. Case 883 stopped that walk for a record that itself carries `superseded_by`, a Case that another Case retired. So in a chain where B replaces A, then C retires B and does not name A, the entries of A and of B are skipped, and the page of A stands `current` with no `superseded_by`, though nothing of A applied. The person holds that the skip is right: B replaced A first, so A must not apply after C retires B, and the tags that `mark_superseded` of `.guppi/guppi/materialize.py` writes stay. By the person's choices, `Vault.decision` writes a new page `superseded` when its record carries `superseded_by`, and names in `superseded_by` the slugs the record holds (B in the chain), each by `take_superseded_by`, which writes one History line and one line of `log.md`. Where B stands, B's walk then finds its name already there and writes no second line, so the end state is as today. A page that already stands is skipped as before, so a Case whose entries already applied stays `current` when the Case that replaced it is retired. The cascade then archives the new `superseded` page, as `estimate-generate-cascades` already checks. I read whole `Vault.decision`, `take_superseded_by`, `supersede_children`, `clear_deferred_by`, `Vault.history`, `apply`, `apply_decision` and `archived_by_cascade` of `generate.py`, and `mark_superseded` of `materialize.py`, which writes `decision-case-<by>` into the record of every Case of the family it marks. The rule that governs the choice of the slug is `rule-page-generation`: the script lays the content of `materialize.yaml` into fields and invents nothing. B is in the record, while naming C would need a walk of the chain that no step of the page names. The new condition reads the same key that `Vault.decision` already reads for the two-line body and for the guard of case 883. A Grep `get\("superseded_by"\)` over `.guppi/guppi/generate.py` printed 5 lines: in `superseded_cases`, in `Vault.decision` twice, in `take_superseded_by` and in `apply`. Each is a test of the same key, so the task adds no second judgment. The Criterion of `estimate-generate-writes-the-decision-page` speaks of `status: current` and of what the record of a retired Case changes, so it is replaced whole: its first line names the new status, one `＋` line is added, and the last `－` line says where the earlier page takes the name from. Each other line stays word for word. It already holds more than seven `＋` lines. Its `purpose` and `method` do not state the old promise and stand. `estimate-generate-fails-alone` says that an entry with `superseded_by` leaves no line, and the Decision page of its Case is still written. That stands, since the line it means is the History line of the entry on its target. The new History line is on the Decision page. `estimate-decisions-schema-checked` and `estimate-glossary-terms-defined` stand: the lists of the schema do not change, and the row and its `where` page get the same clause. A Grep `retired that later Case` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/glossary.md`, `vault/wiki/entities/entity-glossary.md` and `vault/wiki/rules/rule-decisions-schema.md`. Each says that a page stays `current` when another Case retired the Case that names it, which the change makes false for a page whose own entries never applied, so the two sources change and their files render again. I read the `## Terms` of `entity-glossary` whole. The pair changes the row `Decision (status)` alone. The rows `ref`, `slug`, `supersedes`, `Decision page`, `deferred_by` and `archived` stand, since none of them says what status a new Decision page takes, and the row `archived` already says that the cascade archives a superseded Decision. A Grep `` status follows the mechanism|makes no decision `superseded` `` over the same paths printed `vault/wiki/rules/rule-page-generation.md` and `.guppi/guppi/materialize.py`, and the docstring of `generate.py` holds the first sentence across a line break. All three change. A Grep `\["superseded_by"\] = |superseded_by=\[` over `.guppi/tests/` printed four lines of `test_generate.py`. I read each test there against the new code. The two tests of the case where a Case is superseded in its own session expect the earlier page `superseded` or `archived`, naming the later Case. The fixture of `other_session` marks only an entry. The tests of case 883 assert only on pages that already stand and on lines that name the retired Case, and the new page of that Case names the Case that retired it. All of them pass on the new code by that reading. The tests that read the live vault, `test_schemas.py` and `test_generate.py` on the lists of `schema.yaml` and `test_guppi_package.py` and `test_ship.py` through `ship.ship`, are not broken by new prose that carries its pointer in a bracket at the end of its sentence. The brief reports at its last reading `uv run --project .guppi guppi test: 1768 passed, 6 skipped, 1 deselected (exit 0)`. No other Case of this session is ratified or shown, and Case 883 of session 2307 is the Case this one extends.

> **problem:**
> A Case that a later Case replaced before its entries applied keeps a Decision page that stands `current` and names no Case that replaced it, when the Case that replaced it is retired in turn, though nothing of it applied.

> **recommend:**
> - **Which Case does A's page name as the one that replaced it?**
>   - Recommended: (a) B, the Case the mark on A's record names; nothing is invented and no chain is walked.
>   - Answer: agreed, (a).
> - **Does A's page date that change in its history?**
>   - Recommended: (a) one History line, and one line of the log, at once, as for any page that goes superseded.
>   - Answer: agreed, (a).
> - **How do the texts that define the page status read?**
>   - Recommended: (a) add one clause to both texts for a page whose own entries never applied.
>   - Answer: agreed, (a).

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, whose Purpose changes.
> **＋** `.guppi/guppi/generate.py`: `Vault.decision` and the module docstring.
> **＋** `.guppi/tests/test_generate.py`: the tests of the Decision page.
> **＋** `estimate-generate-writes-the-decision-page`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/materialize.py`: the module docstring on what a `supersedes` mark makes.
> **＋** `rule-decisions-schema`: the field `status` of its Render changes.
> **＋** `vault/wiki/decisions/schema.yaml`: the file rendered from it.
> **＋** `entity-glossary`: the row `Decision (status)` changes.
> **＋** `vault/wiki/glossary.md`: the file rendered from it.
> **＋** `vault/wiki/decisions/decision-case-<N>.md`: the Decision pages that `guppi generate` writes and supersedes.
> **＋** `vault/archive/`: the folder where an archived earlier Decision page may stand.
> **＋** `vault/wiki/log.md`: the feed of page changes that `guppi generate` appends to.

> **when:**
> `uv run --project .guppi guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, or `superseded` for a record that carries `superseded_by`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
> **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded`, unless it stands `archived`, and appends to its `superseded_by`, and does the same to each page in the `children` of the earlier page, at any depth, that stands `current`, a page of an earlier session too. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** An earlier page that stands `archived`, under `vault/archive/` or under `vault/wiki/decisions/`, keeps `status: archived` and its place; it takes the new page into its `superseded_by` with one History line `superseded by decision-case-<N>`, and it removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, as for a page that stands `current`.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`; neither does a page reached only through `children` clear a `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **＋** The new page of a record that carries `superseded_by`, a Case that a later Case superseded before its entries applied, is written `superseded`, takes each slug of the record's `superseded_by` into its own `superseded_by` with one History line `superseded by decision-case-<M>` and one line of `vault/wiki/log.md` per slug, and the cascade of the same run archives it; this holds whether or not another Case retired that later Case in turn.
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
> **－** The Decision pages already written are not rewritten.
> **－** A page whose `superseded_by` already names the new page gets no second History line and no second line in `vault/wiki/log.md`, whether an earlier run put the name there or an earlier step of the same record did, such as a sub-case page reached through the `children` of its parent and named in `supersedes` too.
> **－** A page in `children` that stands `archived` or `superseded` is left as it is.
> **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.
> **－** A record that carries `superseded_by`, a Case that a later Case retired, still gets its page with its `supersedes`, but that `supersedes` changes no other page: no earlier page or page in its `children` changes `status` or takes the record into `superseded_by`, no target loses a `deferred_by`, and no History line and no line of `vault/wiki/log.md` names the retired page for such a change; the page of an earlier Case names the retired Case only when its own record carries it in `superseded_by`.

```then
update:
- slug: rule-page-generation
  replace:
  - old: naming the superseding Decision, and its status follows the mechanism as for any superseded page (case 299.4); a Case whose record carries `superseded_by`, retired by a later Case before its entries applied, still gets its Decision page with its `supersedes`, but that `supersedes` changes no other page and writes no line of History or of `log.md` (as set in case 883);
    new: naming the superseding Decision (case 299.4); a Case whose record carries `superseded_by`, retired by a later Case before its entries applied, gets its Decision page `superseded` at once, naming in `superseded_by` each Decision its record names, with one History line for each, whether or not another Case retired that later Case in turn (as set in case 888); it still lists its own `supersedes`, but that `supersedes` changes no other page and writes no line of History or of `log.md` (as set in case 883);
  change: a Case replaced before its entries applied gets its Decision page superseded at once, naming the Case its record names
- slug: estimate-generate-writes-the-decision-page
  set:
    status: pending
  change: the Criterion replaced whole — the new page of a record with superseded_by is written superseded
- slug: rule-decisions-schema
  replace:
  - old: in `supersedes`, unless another Case retired that later Case before its entries applied, and `archived` the moment
    new: in `supersedes`, unless another Case retired that later Case before its entries applied; a page whose own entries never applied, since a later Case's mark skipped them, is written `superseded` and names that later Case, whether or not another Case then retired it, and `archived` the moment
  change: a Decision page whose own entries never applied is written superseded, naming the Case that replaced it
- slug: entity-glossary
  replace:
  - old: in `supersedes`, unless another Case retired that later Case before its entries applied, `archived` when
    new: in `supersedes`, unless another Case retired that later Case before its entries applied; a page whose own entries never applied, since a later Case's mark skipped them, is written `superseded` and names that later Case, whether or not another Case then retired it, `archived` when
  change: 'the row Decision (status): a page whose own entries never applied is written superseded, naming the Case that replaced it'
```

```tasks
- [ ] update `rule-page-generation`
- [ ] update `estimate-generate-writes-the-decision-page`
- [ ] update `rule-decisions-schema`
- [ ] update `entity-glossary`
- [x] `.guppi/guppi/generate.py`: `Vault.decision` writes a new page `status: superseded` when its record carries `superseded_by`, and takes each slug of it into the page's `superseded_by` by `take_superseded_by` before it saves the page; the module docstring says so where it says that the status of the two-line page follows the mechanism, and in the paragraph of case 883.
- [x] `.guppi/guppi/materialize.py`: the module docstring says that the `{supersedes:case N}` of a Case that a later Case retires still makes `superseded` the earlier Case whose entries it marked before they applied, since that Case's record carries the mark and its new page is written `superseded`.
- [x] `.guppi/tests/test_generate.py`: in a chain where B supersedes A and C supersedes B alone, with no page of A yet, the entries of A are not applied, the page of A ends `superseded` or `archived` with `superseded_by` B alone, one History line and one line of `log.md` `superseded by decision-case-B`, and no name of C; and where B stands, the page of A gets that line once.
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/decisions/schema.yaml`
- [ ] `uv run --project .guppi guppi glossary`
- [ ] read `estimate-generate-writes-the-decision-page`
```

## Case 889 — After /pre-spec the hook sends the agent on while a Case is still out

> **context:**
> After `/pre-spec`, the `Stop` hook `uv run --project .guppi guppi onward --plan` sends the agent on where no person is needed, since a reply that carries a `LEDGER` block ends in that text and can call no tool. `plan_onward` of `.guppi/guppi/onward.py` returns no reason when `case_out` finds a Case still out: a file `case-<N>.md` under `cases/` written after the last decision line of Case N. So a batch that the person ratifies in part leaves the Cases still out to no turn. At `/pre-spec` of session 2307 the person ratified Cases 882, 883, 884 and 886, Case 881 had to go back to its `case-guppi`, the hook said nothing, and the session stood until the person asked what came next (`lesson-prespec-loop-stalls-when-one-case-waits-after-a-partial-ratification`, from L55 of `raw/2026-10-17/2307/ledger.md`). The person chose that the hook sends the agent on in that state too, at every reply it sends on today, with a third reason that names each Case still out; the agent sends each one that must change to its `case-guppi`, ends the turn as `orchestration.md` sets it for a Case out while a `case-guppi` has not answered, or opens its reply with `STOP:` when each Case waits only for the person's word. `rule-prespec-onward` is the rule this touches: its Purpose is to keep Plan Mode from stopping where no person is needed, and the chosen option serves it. Two sentences of its Purpose change: the one that sends the agent to the check and the exit gains the condition that no Case is still out, and the third reason is added after the reason of the loop. The Criterion of `estimate-prespec-onward-sends-the-agent-on` lists "no Case is still out" among the conditions of exit 2, and the Criterion of `estimate-prespec-onward-tells-the-loop-from-its-end` says that a Case built again and not yet ratified keeps the hook silent; the change makes both false, so Case 889.1 and Case 889.2 replace each whole, and set anew each `purpose` that states the old promise. Each reason carries the text of `ONLY_THE_PERSON` of `.guppi/guppi/onward.py`, which today asks for `STOP:` for "a Case still out with its case-guppi"; beside the third reason that would tell the agent both `STOP:` and `**Waiting:**` for the same Case (finding F1 of `/pre-spec`), so by the person's choice of the third message that text, and the line of the Criterion of Case 889.1 that states it, keep `STOP:` for a question the person must answer and a Case that waits only for the person's word, and, while a `case-guppi` has not answered, send the agent to the end of the turn that `orchestration.md` sets for a Case out. The reason does not name the `**Waiting:**` line itself, since Case 890.3 sets that a Case sent back after the check refused a showing of a batch is out of the batch and takes no `**Waiting:**` line while its `case-guppi` has not answered; after the person ratifies the other Cases, that Case is still out and this hook names it, and the agent waits for it as `orchestration.md` then sets it. The Criterion of `estimate-prespec-onward-reads-the-decisions-of-the-session` sets when a Case is still out, and that judgment does not change; its line that a Case replaced under a new number does not keep the hook silent stays true, since after the change no Case keeps it silent, so its Criterion stands and the person's choice of two rewritten checks holds. But its tests told a Case out by the silence of the hook and a Case not out by exit 2 alone, which would pass whether the Case is out or not once a Case still out exits 2 too (finding F4 of `/pre-spec`); so the tests of a Case out assert the third reason, and the tests of a Case not out assert the reason of the exit or of the loop, never the third, so that its `method` still tells the two apart. Before `/pre-spec` the hook stays silent on purpose, and this Case does not change that. The Case does not change `rule-orchestration`: the sentences of `orchestration.md` and of `.claude/skills/pre-spec/SKILL.md` that say the hook of `rule-prespec-onward` sends the agent on after the reply that acknowledges the ratification stay true. The item put off on that page by Case 884 stays in `backlog.md`; the item put off by Case 887 is retired by Case 890, whose file carries `{supersedes:case 887}` on the decision lines of Case 890.1 on `rule-case-check` and of Case 890.3 on `rule-orchestration` (finding F2 of `/pre-spec`). A Grep of `rule-prespec-onward|onward --plan` over `vault/wiki/`, `log.md` and `brief.md` left out, printed 21 files; besides the rule page and its three Estimates, the hits of `estimate-orchestration-acknowledging-reply`, `estimate-orchestration-defers-in-one-reply`, `estimate-orchestration-shows-the-frontier-after-a-closed-line` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` say only that the hook sends the agent on after `/pre-spec` or nothing once `spec.md` stands, which stays true; `estimate-prespec-confirms-the-findings-once` says the hook sends the agent to the check and the exit after the one ratification of every Case built again, which stays true; the other hits name the hook as a child, in the registry of hooks, in a Result or a History, or for what it counts as no Case or as ratified (`rule-case-build`, `estimate-case-check-sends-back-a-clash-with-another-case`, `estimate-orchestration-shows-the-built-case`), or as a judgment apart (`estimate-retro-onward-sends-the-agent-to-the-handoff`), which the change leaves true. The same Grep over `.claude/` printed `.claude/settings.json`, `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/case-guppi.md`, none of which the change makes false. A Grep of `case_out|cases_out` over `.guppi/` printed only `.guppi/guppi/onward.py` and `.guppi/tests/test_onward.py`, so the judgment of a Case still out lives in one function, and the ids of the third reason come from that same judgment, with no second copy, as `rule-one-judgment-one-implementation` sets it. The lesson stands in the ledger of session 2307, so no decision line carries `{addresses:...}`.

> **problem:**
> After `/pre-spec`, a batch ratified in part leaves the Cases still out with no turn: the hook that sends the agent on stays silent while any Case is out, so the run stops where no person is needed.

> **recommend:**
> - **How the run goes on after a partial ratification**
>   - Recommended: (a) the hook sends the agent on with a third message.
>   - Answer: agreed, (a).
> - **Which replies get the new message**
>   - Recommended: (a) the same replies as today.
>   - Answer: agreed, (a).
> - **What the new message names**
>   - Recommended: (a) the message names each Case left without a ratification.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) rewrite the two existing checks, in two sub-cases.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the findings of `/pre-spec`: the text that each reason adds asks for `STOP:` for a Case still with its `case-guppi` while the third reason asks for the `**Waiting:**` line; the `context` claimed that the item of Case 887 stays in `backlog.md`; the tests of `estimate-prespec-onward-reads-the-decisions-of-the-session` tell a Case not out by exit 2 alone.
>   - Taken: `ONLY_THE_PERSON` and the line of Case 889.1 keep `STOP:` for a question or a Case that waits only for the person's word and send a `case-guppi` that has not answered to the end of the turn that `orchestration.md` sets for a Case out, which Case 890.3 sets for a Case sent back after a refusal; the `context` says that Case 890 retires the item of Case 887; the tests of a Case not out assert the reason of the exit or of the loop, and that Estimate's Criterion stands, as the `context` says.

### Case 889.1 — A Case still out does not silence the hook

> **given:**
> `estimate-prespec-onward-sends-the-agent-on`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/onward.py`: the hook `guppi onward --plan`.
> **＋** `.guppi/tests/test_onward.py`: the tests of the hook.
> **＋** `rule-prespec-onward`: the rule of the hook.
> **＋** `estimate-prespec-onward-tells-the-loop-from-its-end`: the check of which reason the hook gives.
> **＋** `.guppi/guppi/ledger.py`: the reading of the refusals in the transcript.
> **＋** `.claude/settings.json`: the registry of the `Stop` hooks.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the session, whose presence silences the hook.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose open lines silence the hook.
> **＋** `/pre-spec`: the skill whose `prespec` line the hook waits for.
> **＋** `vault/wiki/orchestration.md`: how the main agent ends a turn while a Case is out.
> **＋** `raw/2026-10-26/0118/cases/case-890.md`: the Case of this session that sets the turn of a Case sent back after a refusal of a showing.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi onward --plan` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session and, after it, a `prespec` line of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block, or a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it; its own refusal is not spent; and the reply does not open with `STOP:`.
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run --project .guppi guppi onward --plan`, and the command of the ledger hook is `uv run --project .guppi guppi ledger`.
> **＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `refusals` of `.guppi/guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply: the one that writes a line again, or an answer with no `LEDGER` block, such as the answer that no Case fixed the cause of the lesson.
> **＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
> **＋** Its reason on stderr sends the agent on with the Cases still out, to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
> **＋** Each reason adds that, when only the person can go on — a question the person must answer, or a Case that waits only for the person's word — the agent opens its reply with `STOP:` and asks the person instead, and that while a `case-guppi` has not answered the agent ends the turn as `vault/wiki/orchestration.md` sets it for a Case out and goes on in the turn that the answer opens.
> **＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript. `.claude/settings.json` registers it on `Stop`, after `uv run --project .guppi guppi onward`.
> **－** A Case still out, as `rule-prespec-onward` judges it, does not keep it silent: it changes only its reason.
> **－** With no `prespec` line of this session after its `hi` in the event log, it exits 0 and prints nothing, and its reason never tells the agent to call `/pre-spec`.
> **－** A reply with no `LEDGER` block after a reply that the ledger hook did not send back gets no reason.
> **－** An error of its own after it has read the payload, when a `prespec` line of this session stands after its `hi`, exits 2 with `onward: not checked: <error>` on stderr and the advice, when no Case is left out, to go on with the loop after the findings of `/pre-spec` or to run the check and exit Plan Mode; the advice does not name a call of `/pre-spec`. It does so at most once a stretch, judged by its own refusal in the stretch alone. Before `/pre-spec`, or when it cannot read the `prespec` line, an error of its own exits 0 and does not send the reply back. An empty payload exits 0.
> **－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
> **－** `uv run --project .guppi guppi onward` without `--plan` keeps its own judgment.

```then
update:
- slug: estimate-prespec-onward-sends-the-agent-on
  set:
    status: pending
    purpose: Whether guppi onward --plan, after /pre-spec, refuses the end of a reply that leaves no Case open in the Frontier and sends the agent on with the Cases still out, to the check and the exit or on with the loop after its findings, once a stretch and once more after each reply the ledger hook sent back, an answer with no LEDGER block included, judged by the refusals in the transcript whatever stop_hook_active says; silent before /pre-spec, on a reply that opens with STOP:, and otherwise
  change: the Criterion replaced whole — a Case still out no longer keeps the hook silent; it changes only its reason
```

```tasks
- [ ] update `estimate-prespec-onward-sends-the-agent-on`
- [x] `.guppi/guppi/onward.py`: `plan_onward` no longer returns None when a Case is still out; the module docstring of `guppi onward --plan` drops "no file under cases/ was written after the last decision line" from the conditions of exit 2 and says that a Case still out changes only the reason; the text of `ONLY_THE_PERSON`, which each reason carries, asks for `STOP:` only for a question the person must answer or a Case that waits only for the person's word, and, while a `case-guppi` has not answered, for the end of the turn that `vault/wiki/orchestration.md` sets for a Case out, and the docstring says the same.
- [x] `.guppi/tests/test_onward.py`: the tests that asserted exit 0 because a Case was still out — `test_loop_a_case_built_again_and_not_ratified_keeps_it_silent`, `test_supersede_a_case_file_after_its_last_line_keeps_it_silent`, the case `{supersedes:case 5.1}` of `test_supersede_marks_on_each_sub_case_with_lines_retire_the_parent`, `test_plan_a_case_file_newer_than_its_last_decision_line_is_silent`, `test_plan_a_case_with_no_reply_that_ratified_it_is_out` and `test_plan_a_record_with_no_readable_time_counts_none_of_its_lines` — assert exit 2 with the reason of the Cases still out, and are renamed to say so; a new test has a reply that ratifies one Case of two built again after the `prespec` line and asserts exit 2, and one more asserts exit 2 at the answer with no `LEDGER` block to a reminder of the ledger hook while a Case is still out; the tests that tell a Case not out by the exit code alone — `test_supersede_a_mark_in_ledger_md_sends_it_on`, `test_supersede_a_mark_in_a_reply_of_the_transcript_sends_it_on`, `test_supersede_a_mark_in_the_reply_that_ended_sends_it_on`, the case `{supersedes:case 5.1}{supersedes:case 5.2}` of `test_supersede_marks_on_each_sub_case_with_lines_retire_the_parent`, `test_plan_a_case_file_older_than_its_last_decision_line_is_no_case_out`, `test_plan_a_case_ratified_by_an_earlier_reply_of_the_stretch_is_not_out` and `test_plan_a_case_ratified_before_the_persons_last_message_is_not_out` — assert the reason of the exit or of the loop, never the reason of the Cases still out; a test asserts that `ONLY_THE_PERSON` names `orchestration.md` for a `case-guppi` that has not answered and no longer names a Case still out with its `case-guppi` for `STOP:`.
- [ ] read `estimate-prespec-onward-sends-the-agent-on`
```

### Case 889.2 — The hook names the Cases still out and says what to do

> **given:**
> `estimate-prespec-onward-tells-the-loop-from-its-end`: its Criterion is replaced whole.
> **＋** `rule-prespec-onward`: the rule of the hook, whose Purpose gains the third reason.
> **＋** `.guppi/guppi/onward.py`: the hook `guppi onward --plan` and its judgment of a Case still out.
> **＋** `.guppi/tests/test_onward.py`: the tests of the hook.
> **＋** `rule-one-judgment-one-implementation`: one judgment of a Case still out.
> **＋** `estimate-prespec-onward-sends-the-agent-on`: the check of the text that each reason adds.
> **＋** `/pre-spec`: the skill whose loop after the findings the reasons name.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the case files, also written `cases/`.
> **＋** `cases/`: the same folder, as the lines of `then` name it short.
> **＋** `.guppi/guppi/prespec.py`: the reading of the `prespec` line.
> **＋** `.guppi/guppi/casecheck.py`: the judgment of an empty case file.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi onward --plan` of `.guppi/guppi/onward.py` receives the end of a reply of the main agent that carries a `LEDGER` block, the event log holds a `prespec` line of this session after its `hi`, and every other condition holds under which the hook sends the agent on.

> **then:**
> When a Case is still out, as `rule-prespec-onward` judges it, the hook exits 2 and tells the agent that the Cases it names by id were built again and are not ratified yet: to send each one that must change to its `case-guppi`, as the loop after the findings of `/pre-spec` sets it. What the agent does when only the person can go on, or while a `case-guppi` has not answered, is the text that each reason adds, as `estimate-prespec-onward-sends-the-agent-on` sets it.
> **＋** It names each Case still out by the N of its file `case-<N>.md` under `raw/<date>/<hi HHMM>/cases/`, found by the one function of `.guppi/guppi/onward.py` that judges whether a Case is still out.
> **＋** When no Case is still out and a file under `raw/<date>/<hi HHMM>/cases/` was written after the last `prespec` line of the session, the hook exits 2 and tells the agent that the Cases built again on the findings of `/pre-spec` are ratified, to run `uv run --project .guppi guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
> **＋** When no Case is still out and no file under `cases/` was written after that line, the hook exits 2 and tells the agent to go on with the loop after the findings of `/pre-spec`: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit as above.
> **＋** The hook reads the time of the `prespec` line, on the date of the event log that holds it, through the one function of `.guppi/guppi/prespec.py` that `window` uses to find the line.
> **＋** One function of `.guppi/guppi/casecheck.py` tells whether a file under `raw/<date>/<hi HHMM>/cases/` holds nothing but blank space, both for this judgment and for the judgment whether a Case is still out.
> **－** While a Case is still out, the hook never tells the agent that the Cases built again are ratified, and never sends it on with the loop alone.
> **－** A reply that writes a defer or a lesson after `/pre-spec` and before any Case is built again never gets the message that the Cases built again are ratified.
> **－** An emptied file under `cases/`, the file of a dropped Case, is never taken for a Case built again after the `prespec` line, nor for a Case still out, whatever its time: with no other file written after that line, the agent is sent on with the loop after the findings.

```then
update:
- slug: rule-prespec-onward
  replace:
  - old: With the line, when a file under
    new: With the line and no Case still out, when a file under
  - old: or, when no Case goes back, to run the check and exit (case 686.1).
    new: 'or, when no Case goes back, to run the check and exit (case 686.1). When a Case is still out at a reply it would send on, such as a reply that ratifies only some Cases of a batch, it sends the agent on instead with a reason that names each such Case: to send each one that must change to its `case-guppi`, to end the turn as `orchestration.md` sets it for a Case out while a `case-guppi` has not answered, and to open the reply with `STOP:` and ask the person when each waits only for the person''s word (as set in case 889.2).'
  change: 'a Case still out no longer keeps the hook silent after /pre-spec: a third reason names each such Case and says what to do'
- slug: estimate-prespec-onward-tells-the-loop-from-its-end
  set:
    status: pending
    purpose: Whether guppi onward --plan, after /pre-spec, names each Case still out and sends the agent on with it while one is out, sends the agent to the check and the exit only when no Case is out and a file under cases/ that holds more than blank space was written after the last prespec line of the session, and on with the loop after the findings when none was; the emptied file of a dropped Case counts as none
  change: the Criterion replaced whole — a third reason names each Case still out in place of the silence
```

```tasks
- [ ] update `rule-prespec-onward`
- [ ] update `estimate-prespec-onward-tells-the-loop-from-its-end`
- [x] `.guppi/guppi/onward.py`: one function returns the ids of the Cases still out, by the judgment `case_out` makes today, and `case_out` returns whether that list holds any; `plan_onward` returns a third reason, with the ids of that function and the text of `ONLY_THE_PERSON`, when the list holds any, before it chooses between the reason of the exit and the reason of the loop.
- [x] `.guppi/tests/test_onward.py`: a test asserts that the third reason names each Case still out by id and none that is not out, that it holds `case-guppi`, `orchestration.md` and `STOP:`, and that it holds neither the reason of the exit nor the reason of the loop; a test asserts that the ids come from the function that `case_out` uses.
- [ ] read `estimate-prespec-onward-tells-the-loop-from-its-end`
```

## Case 890 — The check reads a Case built again as its file holds it, and the clean Cases of a batch go first

> **context:**
> The check of the file of a Case judges it with the other Cases of the session. `other_blocks` of `.guppi/guppi/casecheck.py` gives them: each Case of the plan file as last ratified, then each entry of `<plan>.checked.json` under its number alone that the plan file does not hold. A Case built again after its ratification is so taken from the plan file, while `unread_sentences` looks for the words its pairs wrote in a `Read` of its current file `raw/<date>/<hi HHMM>/cases/case-<N>.md`. At `/pre-spec` of session 2307 Case 883 was built again, and the `Stop` check of `rule-case-check` refused the showing of Case 881 three times on 881.24, since the words of the old 883 stood in no file that its `case-guppi` read (`lesson-casecheck-reads-a-sibling-from-the-plan-as-last-ratified`). That refusal held back the reply that showed the five Cases of the loop together, so the one Case with a finding held back the four with none; the person ratified 882, 883, 884 and 886 first and 881 after, and put both matters off by Case 887. The person chose that the check takes such a Case as its file holds it, when its stored entry has no finding, in each judgment that reads `other_blocks`, so that one list of the other Cases stays, as `rule-one-judgment-one-implementation` sets it; and that, when the `Stop` check refuses a showing of a batch for a finding stored with one Case, that Case goes back to its `case-guppi` and leaves the batch and the other Cases are shown for ratification, in every batch before `/pre-spec` and in the loop after its findings. `rule-case-check` and `rule-orchestration` carry `deferred_by` with `decision-case-887`, so Case 890.1 and Case 890.3 carry `{supersedes:case 887}` on the decision lines that name them. `rule-orchestration` also carries `decision-case-884`, for the growing context of `case-guppi`; the person chose to leave that matter out, so no line carries `{supersedes:case 884}`, which would retire the whole of Case 884, and the page stays in `backlog.md` through it. The Frontier line C2 has the source `brief`, so the check of an open `backlog` line does not bear on it. A Grep of `other_blocks` over `.guppi/` printed `.guppi/guppi/casecheck.py` alone, so the change stays in the one function that gives the other Cases; `ratified.py` and `prespec.py` read the plan file by their own `split_cases`, and this Case does not change them. Among the Estimates of `rule-case-check`, the Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` says the other Cases are each Case of the plan file, which the change makes false, so Case 890.2 replaces it whole and rewrites that one line, carrying every other line as it stands; `estimate-case-check-applies-the-pairs-of-the-session-in-order`, `estimate-case-check-notes-a-page-the-cascade-archives`, `estimate-case-check-notes-a-sentence-two-cases-change` and `estimate-case-check-leaves-out-a-case-the-file-supersedes` name the other Cases as `other_blocks` gives them, or the pairs of the other Cases of the session applied before those of the file, or a Case a mark leaves out, and stay true, since they do not say which text of a Case counts; `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read` looks for the part another Case wrote in a read of that Case's file, which stays true and now finds it. A Grep of `for one ratification` over `vault/wiki/` printed 12 files: `orchestration.md`, `log.md`, `rule-orchestration`, `rule-prespec`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-orchestration-marks-each-round-of-a-batch`, `estimate-orchestration-signs-a-batch-together`, `estimate-orchestration-signs-items-taken-together`, `estimate-orchestration-rechecks-a-sibling-after-a-joint-send`, `estimate-prespec-confirms-the-findings-once`, `estimate-orchestration-acknowledging-reply` and `estimate-orchestration-batches-cases-out-at-once`. Each hit outside `log.md` and the History lines says that every Case of a batch, or every Case built again, is shown in one reply for one ratification; that showing still comes first, and the new step only follows its refusal, with the Case sent back out of the batch, so the hits stand; the person chose that the Criterion of `estimate-prespec-gathers-the-answers-after-findings` names the new step, and Case 890.4 replaces it, carrying its other lines but the two on the labelled line and on writing nothing else, which gain the exception of the reply that answers the refusal; since `.claude/skills/pre-spec/SKILL.md` takes the new text only at the librarian's render, Case 890.4 also sets its `method` to read the new Render of `rule-prespec` in the Spec at Retro, as the Estimate of Case 890.3 does for `rule-orchestration`. That reply sends a Case to its `case-guppi` and shows Cases while that answer is out, which step 3 of `rule-prespec`, the `**Waiting:**` step of a batch and the sentence of case 730.1 on Cases out at the same time would forbid; so the pair of Case 890.3 says that the Case sent back leaves the batch and that neither of those holds for it in that reply, a second pair of 890.3 says so after the sentence of case 730.1, and a pair of Case 890.4 makes the same exception at the end of step 3, so that the reply ends as a showing ends and names the Case sent back as still out in the agent's own text. The Criterion of `estimate-orchestration-shows-the-built-case` names the reply that follows a refusal of the `Stop` check for a file not sent or a showing that differs from the checked text; a stored finding is neither, so its Criterion stays true and the new step stands beside it. Case 889 makes the hook of `rule-prespec-onward` send the agent on after `/pre-spec` while a Case is still out, with a reason that names it and, while a `case-guppi` has not answered, sends the agent to the end of the turn that `orchestration.md` sets for a Case out; so the pair of Case 890.3 sets that end: the answer to the refusal ends as a showing, and each later turn while the `case-guppi` of the Case sent back has not answered and no Case shown waits for the person ends with the `**Waiting:**` line that names it. This Case does not change that hook. A Grep of `orchestration\.md` over `.guppi/tests/` printed `.guppi/tests/test_orchestration.py`, which reads only the blocks tagged `showing` and `defer` of the live `orchestration.md`, and this Case leaves both blocks as they are; `.guppi/tests/test_case_schema.py` runs `check_answer` with no store, so it does not reach `other_blocks`. The lesson stands in the ledger of session 2307, so no decision line carries `{addresses:...}`.

> **problem:**
> The check of a Case reads another Case built again from the plan as last ratified and looks for its words in its current file, so a sibling built again makes the check fail until it is ratified again; and one Case of a batch with a stored finding holds back the showing of every Case of the batch.

> **recommend:**
> - **Which text of another Case the check uses**
>   - Recommended: (a) the last built text, for every check.
>   - Answer: agreed, (a).
> - **What happens when the check refuses one Case of a batch**
>   - Recommended: (a) the clean Cases are shown at once, and the faulty one goes back.
>   - Answer: agreed, (a).
> - **The other put-off on `rule-orchestration`**
>   - Recommended: (a) it stays out of this Case.
>   - Answer: agreed, (a).
> - **Where the clean Cases go first**
>   - Recommended: (a) in both places, a batch before `/pre-spec` and the loop after its findings.
>   - Answer: agreed, (a).
> - **How the change to the check is checked**
>   - Recommended: (a) a new check, with the clash check reworded.
>   - Answer: agreed, (a).
> - **How the change to the batch is checked**
>   - Recommended: (a) a new check for the batch, and the loop check reworded.
>   - Answer: agreed, (a).

### Case 890.1 — A Case built again counts as its file holds it

> **given:**
> `estimate-case-check-takes-a-case-built-again-from-its-file`: the new check of which text of another Case counts.
> **＋** `rule-case-check`: the rule of the check, whose Purpose gains the sentence.
> **＋** `.guppi/guppi/casecheck.py`: `other_blocks`, the one list of the other Cases of the session.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the check.
> **＋** `<plan>.checked.json`: the store of the checked Cases beside the plan file.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the case files.
> **＋** `rule-one-judgment-one-implementation`: one list of the other Cases for every judgment.

> **when:**
> The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file under `raw/<date>/<hi HHMM>/cases/`, while the plan file of the session holds another Case that `<plan>.checked.json` holds under its number alone with another text, since it was built again after its ratification.

> **then:**
> The hook takes that other Case as `<plan>.checked.json` holds it, in place of its text in the plan file, when its entry holds no finding and the file under `raw/<date>/<hi HHMM>/cases/` of its top-level Case holds its heading.
> **＋** It takes it so in each judgment that reads the other Cases of the session through `other_blocks` of `.guppi/guppi/casecheck.py`: the clash of two Cases, the order of the `replace` and `reword` pairs, the read of the sentence around each pair, and the notes of the cascade.
> **＋** A part of a sentence that a pair of that other Case wrote then counts as read when it stands whole in the outputs of the `Read` calls of the subagent on the file of that Case.
> **＋** The other Cases keep the order of the plan file, and the entries the plan file does not hold come after them, as before.
> **－** An entry with findings, an entry joined with an agent id, and an entry whose top-level file is empty or no longer holds its heading leave the other Case as the plan file holds it.
> **－** The hook writes nothing to the plan file or to `<plan>.checked.json` for this judgment.

```then
create:
- slug: estimate-case-check-takes-a-case-built-again-from-its-file
  ref: rule-case-check
  kind: QA
  purpose: Whether the check of the file of a Case takes another Case of the session that was built again after its ratification as its stored text holds it, in place of the plan file, in every judgment that reads the other Cases, so that the words its pairs wrote are found in a read of its file
  method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k built_again_sibling
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: while the build it replaces stands in the plan (case 725.2).
    new: while the build it replaces stands in the plan (case 725.2). A Case of the plan that was built again after its ratification, whose entry in the store holds no finding and whose top-level file still holds it, is taken as the store holds it, in place of the plan, in each judgment that reads the other Cases, so that the words its pairs wrote are judged, and looked for in a read of its file, as the person will ratify them (as set in case 890.1).
  change: a Case built again after its ratification counts as its stored text holds it, not as the plan holds it
```

```tasks
- [ ] create `estimate-case-check-takes-a-case-built-again-from-its-file`
- [ ] update `rule-case-check`
- [x] `.guppi/guppi/casecheck.py`: in `other_blocks`, for each Case of the plan, the entry of the store under the same id with no findings and a text, whose top-level file is not `dropped` and is not `left_by_its_file`, gives its `then` block in place of the plan's, in the plan's order; the docstring of `other_blocks` and the passage of the module docstring that says "each Case of the plan file, then each entry of the store under the number alone that the plan does not hold" say so.
- [x] `.guppi/tests/test_casecheck.py`: tests named `built_again_sibling`: a Case of the plan built again in the store with a pair that writes a new sentence, and an answer whose pair matches in that sentence with a `Read` of the page and of the file of that Case, gives no finding that the sentence was not read; an old text that only the plan's version wrote gives the answer a finding of `check_pairs`; an entry with findings, and an entry whose file no longer holds its heading, leave the plan's text; the first two fail on the code before the change.
- [ ] read `estimate-case-check-takes-a-case-built-again-from-its-file`
```

### Case 890.2 — The clash check names the text of a Case built again

> **given:**
> `estimate-case-check-sends-back-a-clash-with-another-case`: its Criterion is replaced whole.
> **＋** `estimate-case-check-takes-a-case-built-again-from-its-file`: which text of a Case built again counts.
> **＋** `estimate-case-check-leaves-out-a-case-the-file-supersedes`: the Cases a mark of the file leaves out.
> **＋** `.guppi/guppi/casecheck.py`: the hook and `other_blocks`.
> **＋** `.guppi/guppi/prespec.py`: `check_same_target`, the judgment of a clash.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the clash.
> **＋** `<plan>.checked.json`: the store of the checked Cases beside the plan file.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a top-level Case.
> **＋** `uv run --project .guppi guppi ratified`: the `Stop` hook that writes the Cases into the plan file.
> **＋** `rule-prespec-onward`: the hook that judges a dropped Case by the same function.

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
> **＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.

> **then:**
> The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `.guppi/guppi/prespec.py`, imported, not copied: each Case of the plan file, as `estimate-case-check-takes-a-case-built-again-from-its-file` sets it for a Case built again after its ratification, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
> **＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
> **＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
> **－** A stored Case that has findings, an entry joined with an agent id, a Case whose number a `{supersedes:case N}` mark of the session's ledger names, and a Case left out as `estimate-case-check-leaves-out-a-case-the-file-supersedes` sets are not compared.
> **－** A stored Case whose top-level file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds nothing but blank space is a dropped Case and is not compared, judged by the one function of `.guppi/guppi/casecheck.py` that the hook of `rule-prespec-onward` uses too.
> **－** A stored Case whose top-level file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds text but no heading of its id is a part that a Case built again no longer holds, and is not compared; its entry stays in the store.
> **－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
> **－** Two other Cases that clash with each other give this answer no finding.
> **－** The `Stop` hook `uv run --project .guppi guppi ratified` keeps its check of the Cases it writes, by the same function.

```then
update:
- slug: estimate-case-check-sends-back-a-clash-with-another-case
  set:
    status: pending
  change: the Criterion replaced whole — a Case of the plan built again after its ratification is compared as its stored text holds it
```

```tasks
- [ ] update `estimate-case-check-sends-back-a-clash-with-another-case`
- [x] `.guppi/tests/test_casecheck.py`: a test named `session_clash` has a Case of the plan that sets a field to one value and its entry built again in the store that sets another, and asserts that an answer clashes with the stored value and not with the plan's; it fails on the code before the change.
- [ ] read `estimate-case-check-sends-back-a-clash-with-another-case`
```

### Case 890.3 — The clean Cases of a batch are shown while the faulty one goes back

> **given:**
> `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`: the new check of the showing after a refusal.
> **＋** `rule-orchestration`: the rule of the main agent, whose Render gains the sentence.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-case-check`: the `Stop` check that refuses a showing of a Case with a stored finding.
> **＋** `<plan>.checked.json`: the store that holds the findings of each Case.
> **＋** `rule-prespec`: the loop after the findings of `/pre-spec`.
> **＋** `case-guppi`: the agent that builds each Case.
> **＋** `raw/2026-10-26/0118/cases/case-889.md`: the Case whose hook names the Case sent back after `/pre-spec` and points to `orchestration.md` for the end of the turn.

> **when:**
> In Plan Mode, the `Stop` check of `rule-case-check` refuses a reply of the main agent that shows the Cases of a batch, for a finding that `<plan>.checked.json` holds with one of them, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent sends the Case whose finding the refusal names, with its top-level Case and each sub-case of that file, back to its `case-guppi` by `SendMessage` with the finding, and that Case leaves the batch.
> **＋** In its answer to the refusal it shows the other Cases of the batch, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification, and the person ratifies them at once or names the ids.
> **＋** The Case sent back is shown when its `case-guppi` answers, as a Case the person questions or changes is shown again: alone when no other Case of the session is out, and otherwise in a batch with the Cases still out.
> **＋** The answer to the refusal ends as a showing ends, its own text after the horizontal rule naming the Case sent back as still out; the Case sent back is out of the batch, so neither the `**Waiting:**` line of a batch nor the joining of Cases out at the same time holds for it in that answer.
> **＋** Each later turn that ends while its `case-guppi` has not answered, and while no Case shown waits for the person's word, ends with one line under the bold label `**Waiting:**`, translated, that names the Case sent back, and nothing else.
> **＋** This holds in every batch before `/pre-spec` and in the loop after the findings of `/pre-spec` that `rule-prespec` sets.
> **－** A refusal for a file not sent, or for a showing that differs from the stored text, sends no Case back: the main agent sends the file and shows the Cases as `vault/wiki/orchestration.md` sets it.
> **－** The main agent puts before the person no Case that the check refused for a stored finding.

```then
create:
- slug: estimate-orchestration-shows-the-clean-cases-of-a-batch-first
  ref: rule-orchestration
  kind: QA
  purpose: Whether, when the Stop check of rule-case-check refuses the showing of a batch for a finding stored with one of its Cases, the main agent sends that Case back to its case-guppi, out of the batch, and shows the other Cases for ratification, before /pre-spec and in the loop after its findings
  method: 'by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
update:
- slug: rule-orchestration
  replace:
  - old: or in a new batch with each Case it asks to change (case 598.1).
    new: or in a new batch with each Case it asks to change (case 598.1). When the `Stop` check of `rule-case-check` refuses a reply that shows the Cases of a batch, or of the loop after the findings of `/pre-spec`, for a finding stored with one of them, the agent sends that Case, with each Case of its file, back to its `case-guppi` by `SendMessage` with the finding, that Case leaves the batch, and the agent's answer to the refusal shows the other Cases for one ratification and ends as a showing ends, its own text after the horizontal rule naming the Case sent back as still out, since neither the `**Waiting:**` line of a batch nor the sentence below on Cases out at the same time holds for a Case out of the batch; each later turn that ends while its `case-guppi` has not answered, and while no Case shown waits for the person's word, ends with one line under the bold label `**Waiting:**`, translated, that names it, and nothing else; the Case sent back is shown when its `case-guppi` answers, as a Case the person questions or changes is shown again, and a refusal for a file not sent or for a showing that differs from the stored text sends no Case back (as set in case 890.3).
  - old: and every Case of the batch is shown in one reply (case 730.1).
    new: 'and every Case of the batch is shown in one reply (case 730.1). A Case sent back for a finding stored with it, while the other Cases are shown, is no such route: it is out of the batch, as the sentence above on a refusal sets it (as set in case 890.3).'
  change: a Case of a batch with a stored finding goes back to its case-guppi and the other Cases are shown for ratification
```

```tasks
- [ ] create `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`
- [ ] update `rule-orchestration`
- [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`
```

### Case 890.4 — The loop after the findings shows the clean Cases first

> **given:**
> `estimate-prespec-gathers-the-answers-after-findings`: its Criterion is replaced whole.
> **＋** `rule-prespec`: the skill `/pre-spec`, whose step 7 gains the sentence.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the file rendered from `rule-prespec`.
> **＋** `vault/wiki/orchestration.md`: the showing of a Case and of a batch.
> **＋** `estimate-orchestration-shows-the-clean-cases-of-a-batch-first`: the check of the showing after a refusal.
> **＋** `rule-case-check`: the `Stop` check that refuses a showing of a Case with a stored finding.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a question.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose items the labels name.
> **＋** `uv run --project .guppi guppi casecheck`: the command of the check.

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
> **＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
> **＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
> **＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out, but for the reply that answers a refusal of the showing of the Cases built again, which ends as `estimate-orchestration-shows-the-clean-cases-of-a-batch-first` sets it.
> **＋** That line holds nothing of what an answer says and no question, and but for that reply the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** In that list the `**Context:**` label of each first round on an item names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`; a horizontal rule stands before the first round of the list and one between the last question of one Case and the round of the next, and no heading or other line of the main agent's own but such a rule marks where a round begins.
> **＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **＋** After a refusal of that reply by `rule-case-check`, step 7 of `.claude/skills/pre-spec/SKILL.md` sends the main agent to the step of `vault/wiki/orchestration.md` that `estimate-orchestration-shows-the-clean-cases-of-a-batch-first` checks.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run --project .guppi guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
> **－** A question that no answer settles stays in the next list under its number.

```then
update:
- slug: rule-prespec
  replace:
  - old: 7. Show every Case built again in one reply, what step 6 found closed and not closed standing in your own text after the horizontal rule, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
    new: 7. Show every Case built again in one reply, what step 6 found closed and not closed standing in your own text after the horizontal rule, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification. When the check of `rule-case-check` refuses that reply for a finding stored with one of those Cases, send that Case back to its `case-guppi` with the finding and show the others for ratification, as `vault/wiki/orchestration.md` sets it for a batch, and end that reply as the exception of step 3 sets it (as set in case 890.4).
  - old: and the label lets the reply pass the check of `rule-case-check` (case 581.1).
    new: 'and the label lets the reply pass the check of `rule-case-check` (case 581.1). The one exception is the reply of step 7 that answers a refusal of the check for a finding stored with one Case built again: it sends that Case back to its `case-guppi`, shows the other Cases, and ends as a showing ends, your own text after the horizontal rule naming the Case sent back as still out (as set in case 890.4).'
  change: step 7 sends a Case built again with a stored finding back and shows the others for ratification; step 3 makes that reply its one exception
- slug: estimate-prespec-gathers-the-answers-after-findings
  set:
    status: pending
    method: 'by hand at Retro of the session that changes it: the new Render of rule-prespec in the Spec, read against the Criterion, recorded in the estimate line'
    purpose: Whether after the findings of pre-spec the main agent sends nothing to a case-guppi until the person has answered every question of the report, then sends each case-guppi its findings with the answers in one message, ends each waiting turn with one labelled line and writes nothing else while answers are out, gathers every round into one numbered list, and shows the Cases built again in one reply, a Case whose stored finding the check refuses sent back and the others shown, as estimate-orchestration-shows-the-clean-cases-of-a-batch-first sets it
  change: the Criterion replaced whole — after a refusal for a stored finding, step 7 sends that Case back and shows the others
```

```tasks
- [ ] update `rule-prespec`
- [ ] update `estimate-prespec-gathers-the-answers-after-findings`
- [ ] `uv run --project .guppi guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-gathers-the-answers-after-findings`
```

## Deferred

## Case 891 — Two failed readings left open at the close of Plan Mode put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 0118. `estimate-clean-branch-ships-neutral-texts` failed on sentences true only in the repository of GUPPI, and its next reading still fails on the `.gitignore` method of `estimate-sprint-close-moves-old-event-logs`. `estimate-spec-write-writes-a-defer` failed, because its by-hand part waits for a short-form defer the person asks for; Case 885 put it off before.

> **problem:**
> No Case of this session rewrites the texts that keep the clean version from being neutral, or sets when the by-hand part of the defer reading is taken.

```then
defer:
  - slug: estimate-clean-branch-ships-neutral-texts
    type: estimate
    purpose: "The clean version of GUPPI ships no sentence true only in the repository of GUPPI; put off at the close of Plan Mode of session 0118"
  - slug: estimate-spec-write-writes-a-defer
    type: estimate
    purpose: "The Stop hook writes a deferred Case into the Spec as the reply showed it; put off at the close of Plan Mode of session 0118"
```
