## Case 538 — The brief of `/carry` keeps Next session from the open lines of the Frontier

> **context:**
> `/carry` ends a planning session whose ratified Spec is left for a later session. It rewrites `vault/wiki/brief.md` in a short shape. Step 1 of `rule-carry-over` (case 451.9) leaves out Readings due and Next session. The root cause of `lesson-carry-short-brief-drops-the-work-list` names the claim behind that step: `make lint` lists the pending Estimates again. But `/hi` builds its Work list and its Ask list from the Next session of the brief alone (`rule-skill-hi`), and it reads neither `make lint` nor the Frontier of the previous session. After the `/carry` of session 2024, the `/hi` of session 0138 had no Work list. The open W lines of the 2024 Frontier and the Readings due of the brief of 1c196e8 stood on no list, and they were restored by hand. Case 531.10 kept the short shape without Next session. The person put the fix off as Case 533, so `rule-carry-over` carries `deferred_by: [[decision-case-533]]` and stands in `backlog.md`. In the round, the person chose two things. First, Next session in the short brief is taken from the open lines of the session's `frontier.md`, and Readings due and Readings at the close stay out. Second, both Criteria that speak of the short brief are replaced whole, one sub-case each. At pre-spec, the person also chose that `Cases` in the brief of `/carry` is always the line "none". `/pre-spec` fails on an open line under `## Cases`, and `/carry` runs only after `ExitPlanMode`, so no such line is open at `/carry`. A deferred decision reaches `/hi` through `backlog.md`, and a sprint item reaches it through `vault/wiki/sprint.md`. No page is created, so no vault query ran. In the frame, the paragraph of the Render of `rule-brief` on the second writer says that Next session is omitted. The last `－` line of `estimate-brief-written` says that the brief of `carry` has no Next session. The change makes both false, so sub-case 538.2 rewrites both. The second line of `estimate-carry-over-writes` still holds, and sub-case 538.1 replaces that Criterion whole with a new line on what the short shape holds. Case 539 of this session removes the move of `generate` that sends a milestone item of the sprint page to the Backlog, and the drop of an emptied milestone. It also changes the words of `rule-brief` on those moves. So, by the person's choice in the round of Case 539, the new Criterion of `estimate-brief-written` no longer says that Flags name those moves. Pre-spec will note on purpose that two old lines of that Criterion are not carried: the line on the moves and the line on the brief of `carry`. Sub-case 538.2 does not touch the text of `rule-brief` on the moves, since Case 539 changes it. The two sub-cases share words about the sections of the brief and the lists of Next session. That is on purpose: each Criterion must read whole without the other, one for the librarian's run and one for `/carry`. The Purpose of `rule-end-of-work` and the Purpose of `rule-backlog` stay true, and `rule-skill-hi` does not change. No code reads the sections of the brief: a Grep of `guppi/` and `tests/` found none. So no reader has to accept an old form. The lesson was written in session 0138, and its fix is ratified in this session, so it gets no mark (case 284.2). `insight-session-vault-knowledge-not-loaded` has `severity: 1`, and of its children only `lesson-carry-short-brief-drops-the-work-list` is live. It stays open, since this Case does not change it. Two things are not done: how `/work` takes up a conserved Spec (Frontier item C4), and the two or three lists of Next session in the brief of the librarian (Frontier item C7).

> **problem:**
> The short brief of `/carry` has no Next session, and `/hi` takes its Work list and its Ask list only from Next session. So the session after a conserved Spec starts with no open work, and the open readings drop out of sight. The frame of the brief and its Estimate still promise that shape.

> **recommend:**
> In step 1 of `rule-carry-over`, the short brief keeps Next session. `Work` and `Ask the person` are taken from the open lines of the session's `frontier.md`, and `Cases` is the line "none". That Frontier already holds the previous brief's Next session, with the lines this session closed removed. Replace the Criterion of `estimate-carry-over-writes` whole. Rewrite the paragraph of `rule-brief` on the second writer, and replace the Criterion of `estimate-brief-written` whole, without the moves that Case 539 removes. `/hi` needs no change. Copying Next session and Readings due from the previous brief was rejected, because it misses the work that this session's Frontier took from other sources. A change to `/hi` so that it reads the previous Frontier was also rejected, because it grows `/hi` beyond the files it loads.

### Case 538.1 — `/carry` writes Next session from the open lines of the Frontier

> **given:**
> `rule-carry-over` — the rule whose Render is the skill `carry`, the second end of a session beside Work Mode, `/retro` and `/handoff`
> **＋** `.claude/skills/carry/SKILL.md` — the rendered skill
> **＋** `estimate-carry-over-writes` — the promise of what `/carry` writes
> **＋** `vault/wiki/brief.md` — the brief `/carry` rewrites
> **＋** `raw/<hi date>/<hi HHMM>/frontier.md` — the Frontier of the session, whose open lines the brief takes
> **＋** `raw/<hi date>/<hi HHMM>/carry.md` — the mark of a conserved Spec, committed with the rest of `vault/raw/`
> **＋** `vault/wiki/backlog.md` — written by `uv run guppi backlog`, shows the conserved Spec and each deferred decision; a sprint item stands on `vault/wiki/sprint.md`
> **＋** `rule-skill-hi` — `/hi` takes its Work list and its Ask list from the Next session of the brief alone, and `/pre-spec` fails on an open line under `## Cases`

> **when:**
> The agent calls the skill `/carry` on `PreToolUse Skill`, after the person answered "conserve" at the fork `ExitPlanMode` prints. The person never types it.

> **then:**
> The skill reads the tree. When the tree holds changes outside the session folder and `vault/wiki/brief.md`, the skill stops and says that work was done and the ordinary exit applies.
> **＋** Otherwise it rewrites `vault/wiki/brief.md` in the short shape, with no Deferred list.
> **＋** The short shape holds Where things stand, Flags and Next session, with no Readings due and no Readings at the close.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, a list with no item the line "none": `Cases` is always the line "none", since a deferred decision reaches `/hi` through `vault/wiki/backlog.md` and a sprint item through `vault/wiki/sprint.md`; `Work` holds each open `W` line of `raw/<hi date>/<hi HHMM>/frontier.md`, and `Ask the person` each open `A` line with its Estimate by slug, the mark `needs the person` and its question.
> **＋** It puts `carry.md` into the session folder: one line, a flag for `materialize` and `guppi backlog`, not a document. The session that finishes the work deletes it.
> **＋** It runs `uv run guppi backlog`, and `vault/wiki/backlog.md` then shows the conserved Spec with its targets.
> **＋** It runs `make style` and commits `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`.
> **－** No open `W` or `A` line of `frontier.md` is left out of Next session, so the next `/hi` takes each one into its Frontier.
> **－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`, and it writes no decision. It writes no page of `vault/wiki/`.
> **－** The work stays sequential, session after session: one conserved Spec, no parallel work.
> **－** `.claude/skills/carry/SKILL.md` equals the Render of the page and is not edited by hand.

> **tasks:**
> - [ ] update `rule-carry-over` — step 1 of the Render keeps Next session: `Work` and `Ask the person` from the open lines of `frontier.md`, `Cases` the line "none"
>   - old: `` no Readings due, no Next session, no Readings at the close, no Deferred list — the conserved Spec and its targets stand in `backlog.md` (case 451.9); Flags say what the vault does not know about this session. ``
>   - new: `` no Readings due, no Readings at the close, no Deferred list — the conserved Spec and its targets stand in `backlog.md` (case 451.9); Flags say what the vault does not know about this session; Next session keeps its three lists, one line per item, a list with no item the line "none": `Cases` always the line "none" — a deferred decision reaches `/hi` through `backlog.md`, a sprint item through the sprint page; `Work` each open `W` line of `vault/raw/<hi date>/<hi HHMM>/frontier.md`; `Ask the person` each open `A` line of it, with its Estimate by slug, the mark `needs the person` and its question. `/hi` takes its Work list from Next session alone, so a line left out is lost to the next session (case 538.1). ``
>   - change: `the short brief of /carry keeps Next session: Work and Ask the person from the open lines of the session's frontier.md, Cases the line none (case 538.1)`
> - [ ] update `estimate-carry-over-writes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the short brief keeps Next session: Work and Ask the person from the open lines of frontier.md, Cases the line none`
> - [ ] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
> - [ ] read `estimate-carry-over-writes` at the first `/carry` after the render, and at the `/hi` after it

> **ratification:**
> ```
> - decision[case 538.1][update][rule-carry-over]{ref:rule-carry-over}{supersedes:case 533}
> - decision[case 538.1][update][estimate-carry-over-writes]{ref:estimate-carry-over-writes}
> ```

### Case 538.2 — the frame of the brief says that the brief of `carry` keeps Next session

> **given:**
> `estimate-brief-written` — the promise of the frame of the brief
> **＋** `rule-brief` — the frame of the brief; its Render is spliced into the frame of the librarian
> **＋** `.claude/agents/librarian-guppi.md` — the rendered frame of the librarian
> **＋** `vault/wiki/brief.md` — the brief that the librarian and `/carry` write
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the handoff the librarian reads
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose open lines the brief of `carry` takes
> **＋** `vault/wiki/backlog.md` — holds the deferred items the brief does not list; a sprint item stands on `vault/wiki/sprint.md`
> **＋** `rule-carry-over` — the second writer of the brief

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
> **＋** Where things stand, Readings due, Flags and Readings at the close are as before.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
> **＋** An item stands in one list only. A list with no item is the line "none".
> **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
> **－** The brief states no decision: the sort by kind is not a judgment of the work.

> **tasks:**
> - [ ] update `rule-brief` — the paragraph on the second writer says that the brief of `carry` keeps Next session: `Work` and `Ask the person` from the open lines of `frontier.md`, `Cases` the line "none"
>   - old: `` Readings due, Next session and Readings at the close are omitted; so is the Deferred list — the conserved Spec and its targets stand in `backlog.md`; Flags say what the vault does not know about this session (cases 190.4, 451.8). ``
>   - new: `` Readings due and Readings at the close are omitted; so is the Deferred list — the conserved Spec and its targets stand in `backlog.md`; Flags say what the vault does not know about this session; Next session keeps its three lists — `Work` the open `W` lines of the session's `frontier.md`, `Ask the person` its open `A` lines, `Cases` always the line "none", since a deferred decision reaches `/hi` through `backlog.md` and a sprint item through the sprint page — because `/hi` takes its Work list from Next session alone (cases 190.4, 451.8, 538.2). ``
>   - change: `the brief of carry keeps Next session: Work and Ask the person from the open lines of the session's frontier.md, Cases the line none (case 538.2)`
> - [ ] update `estimate-brief-written`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the brief of carry keeps Next session, Work and Ask the person from the open lines of frontier.md and Cases the line none; Flags no longer name the moves of generate that case 539 removes`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-brief-written` at the librarian's run after the render

> **ratification:**
> ```
> - decision[case 538.2][update][rule-brief]{ref:rule-brief}
> - decision[case 538.2][update][estimate-brief-written]{ref:estimate-brief-written}
> ```
