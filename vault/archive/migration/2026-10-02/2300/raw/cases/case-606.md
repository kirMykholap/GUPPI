## Case 606 — A Case writes no `by hand` box that waits for the librarian's run

> **context:**
> Work Mode ticks each code, test, migration and `by hand` box of its own session's Spec in the reply that finishes the task. Retro counts what stays unticked. The librarian carries every unticked box of the Specs into the Work list of the brief. Case 591.11 wrote a `by hand` box whose check can only run after the librarian's run of its own session: `make lint` prints no `fence` line on `decision-case-13`. That moment comes after Work Mode and Retro have ended, so no one could tick the box in session 1202. Retro of that session did not count it, and the librarian carried it into the brief. Twice a later session took the check and closed its Work line `· work` without ticking the box: W41 of the Frontier of session 1834, and W49 of the Frontier of session 2049. Nothing told either one to tick it. The librarian carried the box each time, and it is open again as W41 of this session's Frontier. The cause is the box itself. The check it asks for already has two homes: the reading of an Estimate, whose `read` line `generate` ticks from the ledger in every `spec.md` under `vault/raw/`, and the `make lint` of the librarian's run, which the brief reports. Case 591.11 itself named `estimate-sprint-migration-lint-clean` as the Estimate of a clean lint. Case 606.1 adds one sentence to the `tasks` form in `case-schema.md`, the Render of `rule-case-protocol`. The sentence bars such a box and says where such a check goes. Case 606.2 closes, once, the one box of this kind open today. The two can fail apart and need different fixes, so they are two sub-cases. Case 606.2 changes no text of a page. Its decision line is an `update` of `decision-case-13` with `change` alone, which writes one History line on that page, the form `case-schema.md` sets for a Case that names a page whose text does not change. This Case replaces Case 603 and its sub-cases 603.1 and 603.2, with the same content. Case 603 was first ratified whole, then split into 603.1 and 603.2 and ratified again. The Spec hook kept the old body of the parent under its heading beside the sub-cases, the fault that `insight-spec-write-parent-body-kept-on-re-ratification` records. The old body then wrote the Criterion of `estimate-case-protocol-case-form` a second time, so one promise stood in two wordings, and the main agent may not edit the plan file. As case 581 did for Case 580, this Case is built again under a new id. Its decision lines supersede 603, 603.1 and 603.2, so the Spec hook removes their text, and the Frontier line C4 closes again under this Case. The person asked whether the librarian needs new instructions. It does not: it ticks no box by hand, `generate` ticks the `read` lines, and the `make lint` of its run is already in the brief, so `rule-brief` stands. `orchestration.md` says that Work Mode ticks the boxes of `raw/<date>/<hi HHMM>/spec.md`, the Spec of its own session. That sentence stays true. The one-off is a task of this session's Spec, which Work Mode ticks there. What the task does is tick one box in the Spec of session 1202, by this ratification, once. No rule names who ticks a box of an earlier Spec, and after Case 606.1 no new Case writes a box that needs one. The Case creates no page, so no vault query was run. In the frame, a Grep of `unticked` over `.claude/`, `vault/wiki/rules/` and `vault/wiki/estimates/` printed 16 files: `rule-brief`, `rule-documentation`, `rule-glossary`, `.claude/agents/librarian-guppi.md`, `rule-materialize`, `rule-page-generation`, `rule-orchestration`, `.claude/skills/retro/SKILL.md`, `rule-retro`, `rule-sprint`, `estimate-brief-written`, `estimate-generate-ticks-the-spec`, `estimate-documentation-completes`, `estimate-glossary-ticks-the-spec`, `estimate-render-harness-ticks-the-spec` and `estimate-sprint-ticks-the-spec`. Each hit, read around its line, says who ticks which line or what the librarian reads and carries. None says which boxes a Case may write. A Grep of `librarian's run` over `vault/wiki/rules/*.md` and `.claude/**/*.md` printed 12 files: `.claude/skills/work/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/agents/librarian-guppi.md`, `.claude/agents/case-guppi.md`, `rule-retro`, `rule-estimates-schema`, `rule-case-build`, `rule-skill-hi`, `rule-work-mode`, `rule-documentation` and `rule-brief`. None lets a Case write a box that waits for that run. `rule-retro` already says that the librarian's `make lint` is the reading of a check that waits for it, which this Case agrees with. A Grep of the `old` anchor over `vault/wiki/` outside `decisions/` printed `vault/wiki/case-schema.md` and `rules/rule-case-protocol.md`; the pair hits the page once. A Grep of `decision-case-13`` over the `frontier.md` files of `vault/raw/2026-10-02/` printed the lines of sessions 1834, 2049 and 2300. Case 606.1 replaces whole the Criterion of `estimate-case-protocol-case-form`, which reads the `tasks` of the Cases of a session by hand, and writes it under `sections`: the lines case 544.11 left stand, and one line is added on the `by hand` box. Its `purpose` and `method` do not state the old promise and stand. `estimate-case-protocol-loaded` checks that the file is rendered and loaded, so it stands. `estimate-case-build-writes-the-case` speaks of the chat form of `case-schema.md` as a whole, so it stands. Case 606.2 is checked by `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its Criterion has Work Mode run each task of the session's Spec in order and tick each `by hand` box in the reply that finishes the task. It stands, because the one-off is one more such task, and Retro counts it as debt when it stays unticked. Cases 601 and 602 of this session change neither `rule-case-protocol` nor the writing of `tasks`.

> **problem:**
> A Case can write a `by hand` box whose check only runs after Work Mode and Retro of its own session have ended. Nobody ticks such a box, and the brief carries it from session to session. The question was whether to tick it later or stop writing it. The person chose to fix the cause and to close the box open today by a Work Mode task.

> **recommend:**
> - **Which boxes does the closer tick?**
>   - Recommended: (a) every box Work Mode ticks — code, a test, a migration or a `by hand` check — in an earlier session's Spec, ticked by whoever closes its Work line.
>   - Answer: not answered; replaced by **Fix the cause, or tick the box later?**
> - **Where is the rule written?**
>   - Recommended: (a) one sentence in the ticking paragraph of `orchestration.md`, which applies at `/hi`, in Work Mode and at Retro.
>   - Answer: not answered; replaced by **Fix the cause, or tick the box later?**
> - **The box open today**
>   - Recommended: (a) a Work Mode task of this Case: run `make lint`, tick the box in `raw/2026-10-02/1202/spec.md` when no `fence` line on `decision-case-13` appears, and close its Work line. Whatever the answer on the cause, the tick then rests on a ratified decision.
>   - Answer: (a).
> - **How is the new rule checked?**
>   - Recommended: (a) rewrite the Criterion of `estimate-case-protocol-case-form` whole, adding a line that `tasks` holds no `by hand` box whose moment comes after Work Mode of its session, read by hand at the close of a later session. A hook that matches words would miss other phrasings.
>   - Answer: (a). The first round asked this question about the ticking rule, and it went unanswered there.
> - **Fix the cause, or tick the box later?**
>   - Recommended: (a) fix the cause. A Case writes no `by hand` box whose moment comes after Work Mode of its session. Such a check is the reading of an Estimate or the `make lint` of the librarian's run, and the box open today is closed once.
>   - Answer: (a). The person asked why such a box stays unticked at all and said the earlier direction was wrong.
> - **Where is the new rule written?**
>   - Recommended: (a) one sentence in the `tasks` part of `case-schema.md`, the Render of `rule-case-protocol`, which `case-guppi` reads whole.
>   - Answer: (a).
> - **What does the second sub-case record in the ledger?**
>   - Recommended: (a) an `update` of `decision-case-13` with `change` alone, which writes one History line on that page saying that the check of its fence has been run and the box ticked; nothing else on the page changes.
>   - Answer: not answered in a round; the person ratified Case 603, which was built on (a), with its sub-cases.

### Case 606.1 — The form of `tasks` bars a `by hand` box that waits for the librarian's run

> **given:**
> `rule-case-protocol` — the form of a Case, rendered into `vault/wiki/case-schema.md`, which `case-guppi` reads whole
> **＋** `estimate-case-protocol-case-form` — the promise on the form of a built Case, its Criterion replaced whole
> **＋** `rule-brief` — the brief of the librarian, which carries the unticked boxes of the Specs under Work; unchanged

> **when:**
> `case-guppi` writes the `tasks` of a Case, following `vault/wiki/case-schema.md` as rendered from `rule-case-protocol`.

> **then:**
> A `by hand` box in `tasks` is a check that Work Mode of the Case's own session takes.
> **＋** A check whose moment comes after that Work Mode — the librarian's run of the session or a later session — is no box. It is the reading of an Estimate, through the `read` line of an Estimate the Case creates or sets `pending` or through an Estimate its `context` names, or it is left to the `make lint` of the librarian's run, which the brief reports.
> **－** `rule-brief` still carries the unticked boxes of the Specs under Work of the brief.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `` one per reading of an Estimate the Case creates or sets `pending`, by its slug. ``
>   - new: `` one per reading of an Estimate the Case creates or sets `pending`, by its slug. A `by hand` box is a check that Work Mode of the Case's own session takes; a check whose moment comes after that Work Mode — the librarian's run of the session or a later session — is no box: it is the reading of an Estimate, through the `read` line of one the Case creates or sets `pending` or through one its `context` names, or it is left to the `make lint` of the librarian's run, which the brief reports (case 606.1). ``
>   - change: `a Case writes no by hand box whose moment comes after Work Mode of its session; such a check is the reading of an Estimate or the make lint of the librarian's run (case 606.1)`
> - [ ] update `estimate-case-protocol-case-form`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     The hook of `rule-case-check` writes a Case that `case-guppi` built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the main agent sends that file to the person, at its first showing or again.
>
>     Then:
>     The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
>     **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
>     **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
>     **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
>     **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
>     **＋** `tasks` holds no `by hand` box whose moment comes after Work Mode of the Case's own session — the librarian's run of that session or a later session; such a check stands as the reading of an Estimate or is left to the `make lint` of the librarian's run.
>     **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
>     **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-orchestration-shows-the-built-case`, and the reply ends with a plain question.
>     **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
>     **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.
>     ```
>   - change: `the Criterion replaced whole — tasks hold no by hand box whose moment comes after Work Mode of the Case's session; the other lines as case 544.11 left them (case 606.1)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-case-form` — by hand, the Cases of a later session at its close

> **ratification:**
> ```
> - decision[case 606.1][update][rule-case-protocol]{ref:rule-case-protocol}{supersedes:case 603}{supersedes:case 603.1}
> - decision[case 606.1][update][estimate-case-protocol-case-form]{ref:rule-case-protocol}{supersedes:case 603}{supersedes:case 603.1}
> ```

### Case 606.2 — The box of Case 591.11 is ticked once

> **given:**
> `raw/2026-10-02/1202/spec.md` — the Spec whose `by hand` box of Case 591.11 stands unticked
> **＋** `raw/2026-10-02/2300/frontier.md` — the Frontier of this session, whose Work line carries that box
> **＋** `make lint` — the check that box names
> **＋** `decision-case-13` — the Decision page whose `fence` finding that box names; it gains a History line alone
> **＋** `rule-orchestration` — who ticks the boxes of a Spec; unchanged
> **＋** `rule-skill-hi` — a Work line closes `· work` where its work is done; unchanged
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — Work Mode runs and ticks each task of the session's Spec; its Criterion stands

> **when:**
> Work Mode of session 2300 runs the one-off task of Case 606.2.

> **then:**
> Work Mode runs `make lint`. When it prints no `fence` line on `decision-case-13`, Work Mode ticks the `by hand` box of Case 591.11 in `raw/2026-10-02/1202/spec.md` and closes its line of `raw/2026-10-02/2300/frontier.md` as `· work`.
> **－** When `make lint` prints a `fence` line on `decision-case-13`, the box stays unticked and its line of `raw/2026-10-02/2300/frontier.md` stays open.
> **－** `rule-orchestration` still sets who ticks the boxes of a Spec: the tick in `raw/2026-10-02/1202/spec.md` is a one-off of this sub-case and sets no rule.
> **－** The text of `decision-case-13` does not change; only its History gains a line.

> **tasks:**
> - [ ] update `decision-case-13`
>   - change: `the check of its closed fence taken after the librarian's run of session 1202; the box of Case 591.11 in raw/2026-10-02/1202/spec.md ticked by Work Mode of session 2300 (case 606.2)`
> - [ ] one-off, by hand: `make lint` prints no `fence` line on `decision-case-13`; then tick the box of Case 591.11 in `vault/raw/2026-10-02/1202/spec.md` and close its line of `vault/raw/2026-10-02/2300/frontier.md` as `· work`

> **ratification:**
> ```
> - decision[case 606.2][update][decision-case-13]{ref:decision-case-13}{supersedes:case 603.2}
> ```
