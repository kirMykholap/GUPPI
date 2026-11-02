## Case 998 — A missed reader of a changed step counts only when it gets past the approved Spec

> **context:**
> `estimate-case-build-reads-the-readers-of-a-changed-step` checks that `case-guppi` finds every step, skill or place of code that reads the output of a step its Case changes. Its `method` reads the findings of `ask-guppi` at `/pre-spec` and fails on a single reader that `case-guppi` missed, even one that `/pre-spec` caught before the Spec was approved. Its History shows four failures: `raw/2026-10-30/2005/ledger.md#L54`, `raw/2026-10-31/0431/ledger.md#L43`, `raw/2026-11-01/0141/ledger.md#L18` and `raw/2026-11-01/2227/ledger.md#L19`. After each of the first three, a Case added a sentence to `rule-case-build` (948.1, 966 and 985, by the History of that page), and the page was set `pending` again (948.2, 966 and 985, by the History of the Estimate). The last reading counts 4 of 11 findings of `ask-guppi` at the `/pre-spec` of session 2038, such as Case 990, which missed `## The acknowledging reply` of `rule-orchestration` (the Result of the page, and line 19 of that ledger). The person chose to measure only what gets past `/pre-spec`: a reader that both `case-guppi` and `ask-guppi` missed and that comes to light later. The person chose to look for it in the Work Mode and Retro of the session and of the session after it, in one reading taken after that later session. The Case replaces the Criterion whole and sets the `purpose` and `method` anew, since both state the old promise. No line of the old Criterion is carried: each one described the searches `case-guppi` runs before its summary, and those searches stay in the Render of `rule-case-build`, not in this Estimate. It changes only this Estimate: the other Estimates of `rule-case-build` keep their readings, and the Render of `rule-case-build` stands, since the person chose the new measure over a new sentence in the rule. The rule that governs the change is `rule-estimates-schema`: an Estimate is one promise and one way to check it, and a reading by hand names its moment and the place of its evidence. That a `method` waits for a later session only through a part that opens with `after`, or with `by hand, after`, and names its event before a colon is set in `case-schema.md`, the Render of `rule-case-protocol` (case 781), and judged by `waits_for_an_event` of `.guppi/guppi/lint.py`. The Retro rule, `rule-retro`, keeps such an Estimate `pending` at Retro and takes its reading once, whole, after the event; for that reason the person chose one reading over two. `case-guppi` read `.guppi/guppi/lint.py` for the new `method`: `waits_for_an_event` matches its one part, which opens with `by hand, after` and closes its event at the first colon. So `waits_for_another_session` gives `/pre-spec` no finding on it, and `tied_to_a_one_off_moment`, which `check_moment` calls, finds no `first`. `check_unread`, through `waits_for_a_later_moment`, gives no `unread` finding on a `pending` page whose `method` waits for an event. The brief reports the last lint run (`## Flags`, `guppi check`, exit 1) as holding `unread: failed` on this page; that finding leaves once the page is `pending`. The block of the page in `.guppi/links.md` names `rule-case-build`, the target, and `rule-orchestration` and `rule-prespec-onward`, which only its Result names; the Result stays until the next reading, so none of them is made false. A Grep for `readers-of-a-changed-step` over the repository outside `vault/archive/` printed 12 files: `vault/raw/2026-11-02/0039/ledger.md`, `vault/raw/2026-11-02/0039/cases/case-998.md`, `vault/raw/2026-11-02/0039/cases/note-998.md`, `vault/raw/2026-11-02/0039/frontier.md`, `vault/raw/2026-11-01/2227/report.md`, `vault/wiki/brief.md`, `vault/raw/2026-11-01/2227/materialize.yaml`, `vault/wiki/log.md`, `vault/wiki/rules/rule-case-build.md`, `vault/raw/2026-11-01/2227/handoff.md`, `vault/raw/2026-11-01/2227/ledger.md` and `vault/raw/2026-11-01/2227/frontier.md`. Of the live pages, `rule-case-build` lists the slug only in `estimates`, which stands, and no test of `.guppi/tests/` names it. The session's ledger holds no `error` lesson, so the Case carries no `{addresses:...}` mark.

> **problem:**
> The Estimate has failed four times on readers that `/pre-spec` caught before the Spec was approved. Each failure added one more sentence to `rule-case-build`. The check does not measure whether a missed reader actually gets through: it fails on any miss by `case-guppi` alone, however the next check handles it.

> **recommend:**
> - **Where and when a miss is looked for**
>   - Recommended: (a) at the Retro of the same session.
>   - Answer: (b) at Retro, and again after the next session.
> - **What the Criterion promises**
>   - Recommended: (a) replace the Criterion whole with the outcome.
>   - Answer: (a).
> - **Which Estimates change**
>   - Recommended: (a) this Estimate only.
>   - Answer: (a), after the main agent explained the question in plain words.
> - **One reading or two**
>   - Recommended: (a) one reading, after the next session, covering both sessions.
>   - Answer: (a).

> **given:**
> `estimate-case-build-reads-the-readers-of-a-changed-step`: the Estimate whose Criterion, `purpose` and `method` are replaced.
> **＋** `rule-case-build`: the target of the Estimate, the rule of `.claude/agents/case-guppi.md`.
> **＋** `rule-prespec`: the rule of `/pre-spec`, whose findings come before the approval.
> **＋** `rule-estimates-schema`: the rule of one promise, one way to check it, and the field `method`.
> **＋** `rule-case-protocol`: the rule of a `method` part that waits for an event it names.
> **＋** `rule-retro`: the rule of Retro, which keeps a reading that waits for an event `pending`.
> **＋** `.guppi/guppi/`: the harness code, whose functions may do a step a Case changes.

> **when:**
> The person approves the Spec of a session whose Cases `case-guppi` built, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, and checked by `/pre-spec`, and a Case of that Spec changes what a step of a skill, an agent, a hook or a function of `.guppi/guppi/` writes, copies or shows, or adds a path on which a step does so.

> **then:**
> Each step, skill or place of code that reads that output or does the same step, and that the change makes false, stands in a Case of the approved Spec, or the `context` of a Case names it and says why it stands.
> **＋** A reader that a finding of `/pre-spec` named and that a Case built again took in counts as found.
> **＋** No such reader comes to light in the Work Mode or the Retro of that session or of the session after it, by a Case built again, a task added by hand, a red test or check, or an `error` lesson.
> **－** A text in a History line, in `log.md` or in `brief.md` is not such a reader.

> **tasks:**
> - [ ] update `estimate-case-build-reads-the-readers-of-a-changed-step`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether no step, skill or place of code that reads the output of a step a Case changes, or does the same step, and that the change makes false, gets past the approved Spec unnamed by both case-guppi and /pre-spec and comes to light in the Work Mode or Retro of that session or of the session after it"
>     method: "by hand, after the Retro of the session that follows a session whose approved Spec holds a Case of case-guppi that changes what a step writes, copies or shows or adds a path on which a step does so: the Work Mode and Retro of both sessions, read in their ledgers and in the transcripts of their main agents under ~/.claude/projects/, for a step, a skill or a place of code that reads the output of the changed step or does the same step, that the change makes false and that no Case and no context of the approved Spec named, such as a Case built again in Work Mode, a task added by hand, a red test or check or an error lesson for it, the count and the transcripts in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — a missed reader of a changed step counts only when it gets past the approved Spec and comes to light in that session or the session after it; pending again after the failed reading of session 2227`
> - [ ] read `estimate-case-build-reads-the-readers-of-a-changed-step`

> **ratification:**
> ```
> - decision[case 998][update][estimate-case-build-reads-the-readers-of-a-changed-step]{ref:rule-case-build}
> ```
