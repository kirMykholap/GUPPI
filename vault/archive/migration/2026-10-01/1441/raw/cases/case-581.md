## Case 581 — While answers of case-guppi are out after pre-spec, the main agent ends each waiting turn with one labelled line

> **context:**
> This Case is Case 580 built again under a new id, its content unchanged. Case 580 was first ratified with no sub-cases, then ratified again as 580.1 and 580.2. The plan file kept the old body of 580 beside the two sub-cases. So `guppi prespec --check` found the `replace` of `rule-prespec` and the Criterion of `estimate-prespec-gathers-the-answers-after-findings` signed twice. Per `rule-spec-write`, a decision line that carries `{supersedes:case N}` removes the section of Case N, with its sub-cases, from the plan file and from `spec.md`. So 581.1 carries `{supersedes:case 580}` and `{supersedes:case 580.1}`, and 581.2 carries `{supersedes:case 580.2}`. Each Case superseded has its own block, which retires all three sets of ledger lines. The Frontier line that Case 580 closed is closed again by this Case.
>
> After `/pre-spec` reports findings, the main agent sends each fix to the `case-guppi` that built the Case. It waits until every answer is back, then shows the person one gathered list. Step 2 of the loop in `rule-prespec`, rendered into `.claude/skills/pre-spec/SKILL.md`, forbids any text in the chat while an answer is still out. An answer to `SendMessage` does not come back inside the turn, though. It arrives later as a notice, and that notice opens a turn of its own, as `lesson-sendmessage-answers-open-a-turn-of-their-own` records. Every turn ends with a reply. So the reading of `estimate-prespec-gathers-the-answers-after-findings` in session 1237, ledger line 37, failed: the main agent wrote in the chat twice while answers were out. Once was at the end of the turn that sent the fixes. The other was in the turn opened by the answer for 567, while the answer for 569 was still out. The handoff of that session asked whether the clause should allow one short line per such turn.
>
> The person chose three things. First, one short line closes each turn that sends to a `case-guppi` and each turn an answer opens while another answer is still out. The line names the Cases that have answered and the Cases still out, and holds nothing of an answer and no question. Second, the line opens with a fixed bold label that ends in a colon. Third, only the loop after the findings changes. The label matters because of `uv run guppi casecheck` on `Stop`. After `/pre-spec`, when the turn brought back a round of questions, it refuses a reply whose first line opens neither with `❓ ` nor with a bold label that ends in a colon. The pattern `LABEL_LINE` in `guppi/casecheck.py` accepts any such label. So if one answer brings a round while another answer is still out, a plain waiting line would be refused, and the labelled line passes with no change to the logic of the check. Session 1237 brought back no round in the loop, so this was not seen live.
>
> `/pre-spec` then found that the same check states a false reason for its exemption after `/pre-spec`. It says that the loop after the findings runs in one turn. This Case puts the opposite into the skill. The reason stands in three places:
> - the passage of `rule-case-check` on how a round opens
> - the module docstring of `guppi/casecheck.py` and the docstring of its function `round_opening`
> - the `－` line on the exemption after `/pre-spec` in the Criterion of `estimate-case-check-refuses-text-before-a-round`
>
> The person chose to correct the reason in all three with the behaviour unchanged. That is 581.2. A promise changes only whole, so 581.2 replaces that Criterion whole and sets the Estimate `pending`. Its `purpose` and `method` do not state the reason, so they stand. The change to `guppi/casecheck.py` is to its docstrings only, so the person's choice of no code change still holds for the logic. 581.1 changes `rule-prespec` and replaces the Criterion of `estimate-prespec-gathers-the-answers-after-findings` whole. 581.1 also sets a new `purpose`, because the old one says the agent stays quiet, and a new `method`, so that the reading looks for refusals of `guppi casecheck` in the loop.
>
> The check of the answer noted lines of the old Criteria that are not carried word for word. All of these changes are on purpose:
> - The `when` of 581.1 now also names `.claude/skills/pre-spec/SKILL.md`, rendered from `rule-prespec`. The trigger is the same.
> - In 581.1, the line that the agent writes nothing in the chat while an answer is out is the promise this Case changes. It becomes the two lines on the labelled waiting line and on what that line may hold. Its clause that no answer of one `case-guppi` is passed on alone is kept.
> - In 581.2, only the `－` line on the exemption after `/pre-spec` changes: its reason. Every other line is carried word for word.
>
> Frame. These searches back the claims above:
> - A Grep of `(?i)notification|while an answer|answers? (is|are) (still )?out|write nothing in the chat` over `vault/wiki/`, leaving out `decisions/`, printed `rule-prespec`, `brief.md`, `lesson-sendmessage-answers-open-a-turn-of-their-own` and `estimate-prespec-gathers-the-answers-after-findings`. The `brief.md` hit is not read.
> - A Grep of `(?i)notification|while an answer|write nothing in the chat` over `.claude/` printed only `.claude/skills/pre-spec/SKILL.md`, which the render rewrites.
> - A Grep of `SendMessage` over `vault/wiki/rules/` printed `rule-case-protocol`, `rule-case-check`, `rule-case-build`, `rule-prespec` and `rule-skill-wait-what`. The same Grep over `.claude/` printed `.claude/agents/case-guppi.md`, `.claude/skills/wait-what/SKILL.md` and `.claude/skills/pre-spec/SKILL.md`.
> - A Grep of `(?i)runs in one turn|in one turn` over the repository, leaving out `vault/raw/` and `vault/archive/`, printed these files:
>   - `vault/wiki/where-to-stop.md`
>   - `.claude/skills/work/SKILL.md`
>   - `guppi/casecheck.py`
>   - `rule-case-check`
>   - `log.md`
>   - `rule-work-mode`
>   - `rule-where-to-stop`
>   - `estimate-case-check-refuses-text-before-a-round`
>   - `estimate-work-mode-takes-the-work-readings`
>   - `decision-case-562`
> - A Grep of `(?i)in the chat|SendMessage|loop` over the Estimates `estimate-prespec-*` printed three files: the target, `estimate-prespec-reconciles` and `estimate-prespec-notes-a-long-chain`.
>
> What the hits mean:
> - Of the `SendMessage` hits, the `rule-case-protocol` passage on who builds a Case sets what goes by `SendMessage`, not what the agent writes while it waits. `rule-skill-wait-what` uses `SendMessage` to ask for a fact. `rule-case-build` and its render describe how `case-guppi` is asked again. None of them sets a form for the waiting reply. The `rule-case-check` hit is the passage that 581.2 corrects.
> - Of the one-turn hits, the Work Mode files speak of the run from `/work` to the handoff, another moment. `log.md` is not read, and the Decision page is history.
> - Of the Estimates, `estimate-prespec-reconciles` speaks of sending a finding to its `case-guppi`, and `estimate-prespec-notes-a-long-chain` speaks of a one-line answer to a `note:` line. Neither speaks of what is written while an answer is out, so both stand.
> - `case-schema.md` says the Cases built again in the loop go out together and come back together. That stays true.
>
> The comparison of `guppi casecheck` judges only a reply that shows a Case heading, and the waiting line shows none. That reply also carries no `LEDGER` block, so the hooks that Case 577 changes do not act on it. Case 579 sets the dispatch prompt, which this Case does not touch.
>
> No code reads the changed texts, so no old form is kept. Not done here: waits on a `case-guppi` outside this loop, where no rule sets anything. `insight-prespec-after-findings-loop-unruled` stays open.

> **problem:**
> The loop after the findings of `/pre-spec` forbids any text in the chat while an answer of a `case-guppi` is out. But each answer opens a turn of its own, and each turn ends with a reply, so the clause cannot hold and its Estimate failed. The question was what the main agent may write in those turns, how that line gets past the end-of-reply check when an answer brings a round, whether the same allowance covers waits outside the loop, and what to do with the check's stated reason that the loop runs in one turn.

> **recommend:**
> - **What the main agent may write while it waits**
>   - Recommended: (a) one short line in each waiting turn: the turn that sends the fixes and each turn opened by an answer while another is still out end with one line that names the Cases that have answered and those still out, and nothing of what an answer says, and no question.
>   - Answer: (a).
> - **How the waiting line gets past the end-of-reply check**
>   - Recommended: (a) the line opens with a fixed bold label such as `**Waiting:**`, which the check accepts as it stands, with no code change.
>   - Answer: (a).
> - **Waits outside the loop after the findings**
>   - Recommended: (a) only the loop after the findings: only step 2 of `/pre-spec` changes, and waits in ordinary Plan Mode stay as they are.
>   - Answer: (a).
> - **The check's stated reason that the loop runs in one turn**
>   - Recommended: (a) correct the reason everywhere, behaviour unchanged: a second part of the Case rewrites the reason on `rule-case-check` and in the docstrings of `guppi/casecheck.py`, and replaces the promise of the check whole with the same behaviour and the true reason, read again in a later session.
>   - Answer: (a).

### Case 581.1 — The main agent ends each waiting turn of the loop with one labelled line

> **given:**
> `rule-prespec` — the rule of `/pre-spec`, whose Render sets the loop after the findings
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill rendered from that Render
> **＋** `estimate-prespec-gathers-the-answers-after-findings` — the promise of the loop, whose Criterion, `purpose` and `method` this sub-case replaces
> **＋** `.claude/skills/grill-me/SKILL.md` — the question shape of the gathered list
> **＋** `guppi/casecheck.py` — the `Stop` check that judges the first line of a reply whose turn brought back a round
> **＋** `lesson-sendmessage-answers-open-a-turn-of-their-own` — the fact that each answer to `SendMessage` opens a turn of its own

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, and the main agent sends them to the `case-guppi` of those Cases, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case that needs no word of the person to the `case-guppi` of that Case by `SendMessage`, all of them in one message, and holds back a finding whose fix waits for the person's answer.
> **＋** It ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
> **＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of what to answer: its own questions still open and every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to.
> **＋** It sends each answer, with each finding held back for it, to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** It then shows every Case built again in one reply, for one ratification.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop no Case is taken up before the current one is ratified or deferred.
> **－** A question that no answer settles stays in the next list under its number.

> **tasks:**
> - [ ] update `rule-prespec` — step 2 of the loop allows one labelled line per waiting turn
>   - old:
>     ````
>     2. Wait for every `case-guppi` you sent to answer. Write nothing in the chat while an answer is still out, and pass on no answer of one `case-guppi` alone.
>     ````
>   - new:
>     ````
>     2. Wait for every `case-guppi` you sent to answer, and pass on no answer of one `case-guppi` alone. An answer to `SendMessage` comes back as a notice that opens a turn of its own, and each turn ends with a reply: end each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer is still out, with one line that opens with a bold label ending in a colon — `**Waiting:**`, translated — and names the Cases that have answered and the Cases still out. Write nothing else in the chat while an answer is out: nothing of what an answer says, and no question; a round that came back waits for the list of step 3, and the label lets the reply pass the check of `rule-case-check` (case 581.1).
>     ````
>   - change: `step 2 of the loop after the findings: each waiting turn ends with one line under a bold label naming the Cases answered and still out, and nothing else is written (case 581.1)`
> - [ ] update `estimate-prespec-gathers-the-answers-after-findings`
>   - set: `{status: pending, purpose: "Whether after the findings of pre-spec the main agent sends the fixes to their case-guppi at once, ends each waiting turn with one labelled line naming the Cases answered and still out and writes nothing else while answers are out, gathers every question into one numbered list, and shows the Cases built again in one reply", method: "by hand at the /pre-spec of a later session after the render whose report sends findings to two or more case-guppi, the replies between the report and the showing again, the SendMessage calls and any refusal of guppi casecheck read in the transcript"}`
>   - change: `the Criterion replaced whole — one labelled line per waiting turn instead of no text while answers are out (case 581.1)`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-gathers-the-answers-after-findings` — by hand at the `/pre-spec` of a later session after the render whose report sends findings to two or more `case-guppi`

> **ratification:**
> ```
> - decision[case 581.1][update][rule-prespec]{ref:rule-prespec}{supersedes:case 580}{supersedes:case 580.1}
> - decision[case 581.1][update][estimate-prespec-gathers-the-answers-after-findings]{ref:rule-prespec}
> ```

### Case 581.2 — The Case check states the true reason for its exemption after pre-spec

> **given:**
> `rule-case-check` — the rule of the Case check, whose passage on how a round opens gives the reason for the exemption after `/pre-spec`
> **＋** `guppi/casecheck.py` — the check, whose module docstring and the docstring of `round_opening` give the same reason
> **＋** `tests/test_casecheck.py` — the tests of how a round opens, unchanged and run again
> **＋** `estimate-case-check-refuses-text-before-a-round` — the promise of the check, whose Criterion this sub-case replaces
> **＋** `rule-prespec` — the loop after the findings, where each answer of a `case-guppi` comes back in a turn of its own
> **＋** `.claude/skills/grill-me/SKILL.md` — the question line that marks a round
> **＋** `/hi` — the command that opens the session and writes its `hi` line in the event log
> **＋** `.claude/skills/wait-what/SKILL.md` — the re-pitch, a turn the check does not judge

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the person's last prompt, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that holds a question line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, no Case heading and no first line `**Fact:**`.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn before its last tool call.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** Text after the last question and one horizontal rule is not judged.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** On the re-fire (`stop_hook_active`) it exits 0, so the round shown again after a refusal is not judged again.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] update `rule-case-check` — the reason for the exemption after `/pre-spec` no longer says the loop runs in one turn
>   - old:
>     ````
>     after `/pre-spec` that text is not judged, since the loop after its findings runs in one turn.
>     ````
>   - new:
>     ````
>     after `/pre-spec` that text is not judged, since in the loop after its findings each answer of a `case-guppi` comes back in a turn of its own and the text the main agent writes there is set by `rule-prespec` (case 581.2).
>     ````
>   - change: `the reason for the exemption after /pre-spec: each answer of the loop comes back in a turn of its own, and rule-prespec sets the text written there (case 581.2)`
> - [ ] update `estimate-case-check-refuses-text-before-a-round`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the same behaviour, with the true reason for the exemption after /pre-spec (case 581.2)`
> - [ ] `guppi/casecheck.py` — reword the reason in the module docstring and in the docstring of `round_opening` as the new text of `rule-case-check` gives it; no line of logic changes
> - [ ] `uv run pytest tests/test_casecheck.py -k round` — passes unchanged
> - [ ] read `estimate-case-check-refuses-text-before-a-round` — `uv run pytest tests/test_casecheck.py -k round` and by hand in a later session, the first rounds of `case-guppi` shown before and after `/pre-spec`

> **ratification:**
> ```
> - decision[case 581.2][update][rule-case-check]{ref:rule-case-check}{supersedes:case 580.2}
> - decision[case 581.2][update][estimate-case-check-refuses-text-before-a-round]{ref:rule-case-check}
> ```
