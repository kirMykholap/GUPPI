## Case 602 — the synthesis gives one line per lesson

> **context:**
> At the end of a session, the synthesis step of `librarian-guppi` compares the root cause of each new lesson with the index lines of the live lessons and Insights. It adds a lesson to an Insight when the cause is the same. The frame (`rule-synthesis`) says that a lesson without a pair stays `new` and that this needs no flag. The frame names a page in the report only when the librarian opened that page to decide. The Criterion of `estimate-synthesis-clusters` asks for more: the report must name the comparisons made against the lines of both Greps, and the outcome of each lesson read, "or none and why". The reading at the /hi of session 2300 failed on this gap. The yaml of session 2049 held two lesson entries. The brief gave a reason against the Insights for `lesson-prespec-onward-re-ratification-out-after-its-stretch` and none for `lesson-case-check-question-line-without-colon-unseen`, although the librarian followed its frame. The person chose to change the frame, not to narrow the Criterion. The person also chose to replace the Criterion whole so that it states the same promise, and to make the line of an unpaired lesson say "none" with a short reason. The new Criterion changes two lines of the old one on purpose. The line on the Greps now names the brief and the number of lines each Grep printed, in place of the loose "comparisons made against their lines". The line on an unpaired lesson now adds that its line in the brief is no flag. The other lines are carried as they stand. The synthesis is reported in the brief: the frame already says that a pair goes "in the brief beside the synthesis". The answer of `rule-close` holds at most twenty lines and nothing else, so the new line goes into the brief. Pre-spec found two weak points, and both stand. First, the Render of `rule-brief` sets five sections of the brief and takes Where things stand from the handoff and the counts of the yaml. The new sentence of `rule-synthesis` names no section, so it makes no sentence of `rule-brief` false. The brief of session 2049 already carries the index check and the synthesis as lines of Where things stand, under the same frame. Naming that section here would add a source that `rule-brief` does not list. Second, `estimate-brief-carries-the-run-facts` has the Readings due line of a `pending` Estimate whose `method` names the librarian's run end with the facts its `method` and Criterion name, and that line compares nothing and carries no passed or failed. `estimate-synthesis-clusters` is such an Estimate, so its Readings due line may repeat the lines of each lesson. That repeat is a copy of facts the run left, not a second judgment. The "none and why" of a lesson is the comparison of root causes that the synthesis makes as its own step. It is not a comparison of the facts with the Criterion of the Estimate, and it is not a verdict. So that Criterion stays true, and this Case does not touch it. A Grep `Where things stand|synthesis|index check` over `vault/wiki/estimates/estimate-brief-*.md` printed hits only in `estimate-brief-written.md`, on the order of the sections of the brief, and none of them speaks of the synthesis line, so `estimate-brief-written` stands. A Grep `without a pair` over the repository, outside `vault/raw/` and `vault/archive/`, printed seven files: `.claude/agents/librarian-guppi.md`, `rule-synthesis.md`, `estimate-synthesis-clusters.md` and `decision-case-487.1` to `decision-case-487.4`. The Decision pages are history and were not read. The rendered file follows by the render. The `method` of the Estimate names a reading of the yaml and the report after a live run with at least two lesson entries. That method states no part of the old promise, so it stands. The page carries no `purpose` field. `estimate-synthesis-keeps-actioned-by-the-mark` speaks of the `addressed_by` mark, not of the report of each lesson, so it is not touched. `estimate-documentation-completes` names a page opened at the synthesis in the report, and this Case keeps that. The new lesson about a question line without its colon has a different cause from the pattern of `insight-prespec-main-agent-question-off-the-grill-me-shape`. This Case clusters no lesson by hand. A Grep `librarian|synthesis` over the case file of Case 601 printed no match, so that Case does not touch this item.

> **problem:**
> The frame of the synthesis lets a lesson that joins nothing go with no word in the report. The Criterion of its Estimate asks for the comparison and the reason for each lesson. Each live reading after a run with an unpaired lesson can fail while the librarian does what its frame says.

> **recommend:**
> - **Does the check of this step get new wording?**
>   - Recommended: (a) replace the wording of the check, so that it says plainly that the report gives one line per new lesson, with the result against both searches
>   - Answer: agreed with the recommendation, (a)
> - **What does the line say for a lesson that joins nothing?**
>   - Recommended: (a) "none" and a short reason — one line per new lesson in the synthesis of the brief: its slug and the lesson or Insight it joined, or none with a few words on why no line of either search shares its cause
>   - Answer: agreed with the recommendation, (a)

> **given:**
> `rule-synthesis` — the frame of the synthesis, rendered into the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the frame of the librarian, which the render writes
> **＋** `estimate-synthesis-clusters` — the promise of the synthesis, its Criterion replaced
> **＋** `vault/wiki/brief.md` — where the librarian reports the synthesis
> **＋** `materialize.yaml` — the lesson entries the synthesis reads and the entries it adds
> **＋** `vault/wiki/lessons/` and `vault/wiki/insights/` — the index lines of the two Greps
> **＋** `vault/archive/` — the archive, whose read the synthesis does not need
> **＋** `estimate-documentation-completes` — the promise that holds the flag of a read outside the frame

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The brief names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, with the number of lines each printed.
> **＋** The brief gives one line for each lesson entry: its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
> **＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line, and the flag of such a read is the promise of `estimate-documentation-completes`.

> **tasks:**
> - [ ] update `rule-synthesis`
>   - old: `` One lesson without a pair stays `new`; that needs no flag. ``
>   - new: `` Write the synthesis into the brief: the two Greps with the number of lines each printed, then one line for each `lesson` entry — its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause (case 602). One lesson without a pair stays `new`; its line in the brief is no flag. ``
>   - change: `the synthesis gives one line per lesson entry in the brief, a lesson that joins nothing with the reason (case 602)`
> - [ ] update `estimate-synthesis-clusters`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the brief gives one line per lesson entry with its outcome against both Greps, or none and why (case 602)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-synthesis-clusters` — by hand, the yaml and the brief after the first live librarian run after the render whose yaml holds at least two lesson entries

> **ratification:**
> ```
> - decision[case 602][update][rule-synthesis]{ref:rule-synthesis}
> - decision[case 602][update][estimate-synthesis-clusters]{ref:rule-synthesis}
> ```
