## Case 654 — The synthesis names a page whose text it reads to judge a cause

> **context:**
> At the synthesis the librarian compares the `root_cause` of each new lesson with the index lines of the lessons and the Insights, and groups the lessons that share a cause. `estimate-synthesis-clusters` checks this step. Its reading at the `/hi` of session 0311 (line L1 of `raw/2026-10-05/0311/ledger.md`) failed on one clause, which says every lesson page read at synthesis is named in the report with its outcome. In the librarian run of session 0109, call 13 printed the frontmatter fields of six lesson pages and three Insights: their `status`, `insight`, `children` and `tags`, without `root_cause` or `pattern` and without the text of any section. The librarian used these fields to see which lessons were already grouped and which lessons each Insight holds, and its report named none of the six lesson pages. The frame of the librarian, the Render of `rule-documentation`, names a page in the report only when the librarian opens it to judge a duplicate, a shared root cause or a failed script, and says a page opened for any other need is not named (case 567.1). The `－` clause of `estimate-documentation-completes` says the same of a page read for its field names or any other need. The clause that failed asks for more than the frame does. The person chose to narrow the check: the report names a page whose text is read to judge a shared cause, and a read of frontmatter fields alone is not named. The new Criterion leaves out on purpose the clause that names every lesson page read at synthesis. In its place, a page is named when the librarian opens it to judge a shared root cause, which is the reason the frame gives. A read of the Trigger, Root cause, `root_cause`, Pattern or `pattern` of a page outside the two Greps counts as such an opening, whether the librarian reads the body or the frontmatter. A `－` line stands beside it: a read of only `status`, `insight`, `children` and `tags`, made to learn which lessons are grouped or which lessons an Insight holds, is not named. The pre-spec run found that a first wording judged only by which part of the page was read. Under that wording a read of `root_cause` alone, made to judge a shared cause, went unnamed, although the frame names it. The present wording judges by the reason, as the frame does, and lists the fields that need no name. Every other line is carried word for word. The Render of `rule-synthesis` already asks the librarian to read the Trigger and Root cause of a candidate and name the page with its outcome, so it agrees with the new clause and stands. The frame of `rule-documentation` and the Criterion of `estimate-documentation-completes` stand for the same reason. The Criterion of `estimate-synthesis-keeps-actioned-by-the-mark` is about `addressed_by` and `status` on an Insight, not about reads, so it stands. The Case creates no page, so no vault query is needed. A Grep `estimate-synthesis-clusters` over the repository, with the glob `!**/decisions/** !vault/archive/** !vault/raw/**`, printed 4 files: `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-synthesis.md` and `vault/wiki/insights/insight-librarian-frame-omits-required-reads.md`. The hit in `rule-synthesis` is its `estimates` field, which stands. The hit in the Insight is its Proposal, which names a past reading of the Estimate and stays true. The brief and the log are not read. The page has no `purpose` field, and its `method` names only when the reading is taken, not the old promise, so neither is set anew.

> **problem:**
> The Criterion of `estimate-synthesis-clusters` asks the librarian to name in its report every lesson page it reads at synthesis. The frame of the librarian and `estimate-documentation-completes` say a page read for anything but a judgment is not named. The check fails a run that kept its frame.

> **recommend:**
> - **How the clash between the check and the librarian's instructions is settled**
>   - Recommended: (a) narrow the check: name only a page whose text is read to judge a shared cause, a lesson's Trigger and Root cause or an Insight's Pattern; a read of frontmatter fields alone is not named; only the Criterion of `estimate-synthesis-clusters` changes.
>   - Answer: agreed, (a).

> **given:**
> `estimate-synthesis-clusters`: its Criterion is replaced whole.
> **＋** `rule-synthesis`: the rule the Estimate checks, whose Render asks for the Trigger and Root cause of a candidate.
> **＋** `rule-documentation`: the frame of the librarian, in `.claude/agents/librarian-guppi.md`, which says which reads the report names.
> **＋** `estimate-documentation-completes`: its clause on the reads that need no name stands.
> **＋** `vault/wiki/lessons/` and `vault/wiki/insights/`: the pages the synthesis compares and reads.
> **＋** `vault/archive/`: the archive the synthesis does not need.

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The brief names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, with the number of lines each printed.
> **＋** The brief gives one line for each lesson entry: its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every page the librarian opens at synthesis to judge whether a lesson shares its root cause is named in the report with the outcome: the Insight it joined, or none and why. A read of its Trigger, Root cause, `root_cause`, Pattern or `pattern` outside the two Greps is such an opening.
> **＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
> **－** A read at synthesis of only the fields `status`, `insight`, `children` and `tags` of a page under `vault/wiki/lessons/` or `vault/wiki/insights/`, made to learn which lessons are grouped or which lessons an Insight holds, is not named in the report and fails nothing here.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line until the close of its sprint, and the flag of such a read is the promise of `estimate-documentation-completes`.

> **tasks:**
> - [ ] update `estimate-synthesis-clusters`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a page is named in the report when it is opened to judge a shared cause; a read of only its status, insight, children and tags is not (case 654)`
> - [ ] read `estimate-synthesis-clusters`

> **ratification:**
> ```
> - decision[case 654][update][estimate-synthesis-clusters]{ref:rule-synthesis}
> ```
