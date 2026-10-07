## Case 722 — A Case built again leaves no stale part behind

> **context:**
> The check that runs when `case-guppi` stops saves the text of each Case it checks in a store, `<plan>.checked.json`, beside the plan file of the session. It compares a new Case with the other Cases of the session: those of the plan and those that only the store holds. Today a stored entry leaves that comparison only when it has findings, when its top-level Case file is empty, or when a `{supersedes:case N}` mark of the ledger names it. At the pre-spec of session 1804, Case 713 was built as 713.1 and 713.2 and then whole again. The store kept the two sub-cases, and the check refused the showing of Case 719 twice on clashes that only they held (`lesson-case-check-store-keeps-sub-cases-a-rebuild-dropped`, Case 720). `insight-case-check-a-case-id-leaves-only-by-a-supersedes-line` shows the same root on the side of the plan. When a later Case retires each sub-case of a parent, the Spec hook of `rule-spec-write` removes only the sub-cases that the marks name, by `remove_superseded` of `guppi/ratified.py`. So the heading and the story of the parent stay in the plan and in `spec.md` with no sub-case under them. The check of `/pre-spec` that once reported such a parent, `check_ratified` in `lesson-prespec-parent-of-superseded-sub-cases`, is gone: the docstring of `guppi/prespec.py` says the plan is compared with no other file since case 445.2. `retired_whole` of `guppi/prespec.py` already judges a parent retired sub-case by sub-case, for `guppi/onward.py` (case 696.1).
>
> Case 722.1 leaves out of the comparison a stored Case whose top-level file stands, holds text and holds no heading of its id. The entry stays in the store, and the test stands beside the test for a dropped Case of case 701.7. The two leftover entries 713.1 and 713.2 of `adaptive-gathering-dewdrop.checked.json` stay. A Grep of `store_of|read_store\(|STORE_SUFFIX` over `guppi/` printed `guppi/ledger.py`, `guppi/casecheck.py` and `guppi/ratified.py`. Each of them reads the store of the plan file that `plan_path` gives for the current session, so no later session reads that store. Case 722.2 makes the Spec hook remove a parent whose every sub-case with a decision line is retired, by `retired_whole`. Case 722.3 fixes the sentence of the `## Splitting` section of `rule-case-protocol` that says a mark on a sub-case removes that sub-case alone. Case 722.3 carries `{supersedes:case 721}`, since `rule-case-protocol` holds `decision-case-721` in `deferred_by` and the check of `rule-case-check` requires that mark (case 467). Case 722.1 carries `{supersedes:case 720}` for `rule-case-check` for the same reason. `generate` clears a defer only from the pages that the superseding Case names (case 467.3, the docstring of `guppi/generate.py`). So `rule-orchestration` keeps `decision-case-721`, and Frontier item C4 can still take it up with the same mark. `decision-case-721` also held a fault of `rule-case-protocol`: a Frontier line closed again by the superseding Case does not hold for a sprint or backlog item whose Case is taken back. This Case does not fix that fault, so Case 722.3 puts `rule-case-protocol` off again for it. The skill `/pre-spec` calls it a finding when a Case of the plan changes a page that another Case of the plan defers (case 186.2). Here the update and the defer stand in the same sub-case.
>
> Case 722.1 replaces the Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` and sets its `purpose` anew, since the purpose lists what is no other Case. `estimate-case-check-applies-the-pairs-of-the-session-in-order` speaks of the same `other_blocks`. Its Criterion stands: it takes the other Cases from `other_blocks`, its list of what that function leaves out is not closed, and its promise is the order of the pairs. Case 722.2 replaces the Criterion of `estimate-spec-write-removes-a-superseded-case`, whose line on a sub-case mark said the parent stays. Its `purpose` and `method` do not state that line and stand. Case 722.3 changes a Render. `estimate-spec-write-removes-a-superseded-case` checks the behaviour that the changed sentence describes, and `estimate-case-protocol-loaded` checks the render (case 378.5). A Grep of `sub-case alone|removes that sub-case|its parent and its other sub-cases` over `vault/wiki/` printed `case-schema.md`, `rules/rule-case-protocol.md`, `estimates/estimate-spec-write-removes-a-superseded-case.md` and `estimates/estimate-materialize-marks-superseded.md`. The last one stands: it says how `guppi materialize` marks the entries of a superseded sub-case, and a parent with no decision line of its own has no entry. A Grep of `(removes|leaves the Spec|leaves the plan|out of the plan|from the plan)` over `vault/wiki/orchestration.md` and `vault/wiki/rules/rule-orchestration.md` printed the sentence on a Case taken back in both files. It says that the line of the item changes when no part of the Case stays in the plan. That sentence stays true and now also holds when the marks retire each sub-case. The insight and the two lessons are not changed by this Case.
>
> Case 725.2 of this session makes the same check leave out a Case that a `{supersedes:case N}` mark on a decision line of the answer's own file names, under its own Estimate `estimate-case-check-leaves-out-a-case-the-file-supersedes`. So the Criterion that Case 722.1 writes, and the `purpose` it sets, name such a Case only as a Case left out as that Estimate sets, a pointer and no promise of their own, so that one promise is signed in one wording (cases 72.1, 188).
>
> `retired_whole` takes the parent out of the sub-cases it judges and does not read the decision lines of the parent itself, and a parent may hold a decision line of its own, such as the `create` of a rule whose promises are its sub-cases. So Case 722.2 removes a parent only when it also holds no decision line of its own that no mark retires; otherwise its line would stay with no heading in the plan, which `prespec --check` reports. `estimate-prespec-catches-a-superseded-case` says that a `{supersedes:case N.M}` covers Case N.M and its own sub-cases, and that the parent with its other sub-cases stays. Its Criterion stands: it says which Cases a mark covers in the findings of `prespec --check`, and the mark still covers no parent. The Spec hook removes the parent by another judgment, and a parent no longer in the plan gives `prespec --check` no finding, since the parent carries no decision line that stays unretired. The clause that Case 725.2 adds to the Purpose of `rule-case-check` follows the end of the sentence whose start Case 722.1 rewrites, and the two new texts read side by side as one sentence.

> **problem:**
> A part of a Case that a later build or a later Case left behind stays live. The store of the Case-file check keeps a sub-case that a Case built again no longer holds, and it clashes with the Cases that come after it. The Spec hook keeps a parent whose every sub-case is retired, and the schema says that a mark on a sub-case removes that sub-case alone.

> **recommend:**
> - **The two leftover entries of last session**
>   - Recommended: (a) leave them; nothing reads that store any more.
>   - Answer: agreed, (a).
> - **How the check leaves out a sub-case its rebuilt Case no longer holds**
>   - Recommended: (a) leave it out when reading: the check leaves out each stored entry whose top-level Case file stands and holds no section under its id; nothing is deleted.
>   - Answer: agreed, (a).
> - **The pre-spec half of the same pattern**
>   - Recommended: (a) this Case covers the store only.
>   - Answer: (b), a second sub-case for the pre-spec half too. The frame then showed that `/pre-spec` no longer reports such a parent, and the question "Where the pre-spec half is fixed" replaced this one.
> - **What checks that it works**
>   - Recommended: (a) replace the Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` with one more exception line.
>   - Answer: agreed, (a).
> - **Where the pre-spec half is fixed**
>   - Recommended: (a) the Spec hook removes a parent whose every sub-case is retired, by `retired_whole`; the second sub-case changes `rule-spec-write`.
>   - Answer: agreed, (a).
> - **The sentence of the Case schema that the second sub-case makes false**
>   - Recommended: (a) leave the sentence to the waiting item on the defers of Case 713.
>   - Answer: (b), fix the sentence in this Case, in a third sub-case that carries the mark of the put-off decision.
> - **The other fault put off on `rule-case-protocol`**
>   - Recommended: (b) put the page off again for that fault, by a new defer line in this Case.
>   - Answer: (b).
> - **How the new build gets past the check while the first build stands in the plan**
>   - Recommended: (a) the main agent first takes back the first build by a short Case, and the new build is shown after it.
>   - Answer: neither option as such. The person agreed with the main agent's proposal: this Case stays as first ratified, its put-off line included, and Case 723 does not touch the sentence on a Frontier line closed again by the superseding Case.
> - **Change**
>   - Asked: the person dropped the change that built this Case again without the put-off line of Case 722.3.
>   - Taken: the Case went back to its ratified form; the build under the number 724 was emptied.
> - **Change**
>   - Asked: the person had Case 722.1 built again, so that its Criterion also leaves out a Case that a supersedes mark on a decision line of the answer's own file names, as Case 725.2 sets it.
>   - Taken: the exception line of 722.1 on marks now names a mark of the answer's own file beside a mark of the session's ledger; the number and the ledger lines of Case 722 stay.
> - **Change**
>   - Asked: at `/pre-spec`, the person agreed that 722.1 names a Case that a mark of the answer's own file names only as a pointer to `estimate-case-check-leaves-out-a-case-the-file-supersedes`, in its Criterion and its `purpose`, and the findings asked that a parent with a decision line of its own is not removed and that `context` names `estimate-prespec-catches-a-superseded-case`.
>   - Taken: the exception line and the `purpose` of 722.1 point to that Estimate; 722.2 and 722.3 remove a parent only when no line of its own stays unretired, with a new exception line and test; `context` says why the Criterion of `estimate-prespec-catches-a-superseded-case` stands.

### Case 722.1 — The Case-file check leaves out a part its file no longer holds

> **given:**
> `rule-case-check`: the rule of the check of the file of a Case, whose Purpose names what the check leaves out.
> **＋** `estimate-case-check-sends-back-a-clash-with-another-case`: its Criterion is replaced whole.
> **＋** `guppi/casecheck.py`: `other_blocks`, which picks the other Cases of the session.
> **＋** `tests/test_casecheck.py`: the tests of a clash with another Case.
> **＋** `guppi/prespec.py`: `check_same_target`, the judgment of a clash.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case, read for the headings it holds.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session, whose marks retire a Case.
> **＋** `rule-prespec-onward`: the rule whose hook judges a dropped Case by the same function.
> **＋** `estimate-case-check-leaves-out-a-case-the-file-supersedes`: the promise of Case 725.2 on a Case that a mark of the answer's own file names.

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
> **＋** Or `tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.

> **then:**
> The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `guppi/prespec.py`, imported, not copied: each Case of the plan file, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
> **＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
> **＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
> **－** A stored Case that has findings, an entry joined with an agent id, a Case whose number a `{supersedes:case N}` mark of the session's ledger names, and a Case left out as `estimate-case-check-leaves-out-a-case-the-file-supersedes` sets are not compared.
> **－** A stored Case whose top-level file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds nothing but blank space is a dropped Case and is not compared, judged by the one function of `guppi/casecheck.py` that the hook of `rule-prespec-onward` uses too.
> **－** A stored Case whose top-level file `raw/<date>/<hi HHMM>/cases/case-<N>.md` holds text but no heading of its id is a part that a Case built again no longer holds, and is not compared; its entry stays in the store.
> **－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
> **－** Two other Cases that clash with each other give this answer no finding.
> **－** The `Stop` hook `uv run guppi ratified` keeps its check of the Cases it writes, by the same function.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `compares its Cases with the other Cases of the session, ratified or not, a dropped Case whose file is empty aside (case 701.7)`
>   - new: `compares its Cases with the other Cases of the session, ratified or not, a dropped Case whose file is empty and a stored Case that the file of its top-level Case no longer holds aside (cases 701.7, 722.1)`
>   - change: `the check of the file of a Case leaves out a stored Case that the file of its top-level Case no longer holds (case 722.1)`
> - [ ] update `estimate-case-check-sends-back-a-clash-with-another-case`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the check of an answer of case-guppi sends back a Case that sets one field, writes one section or replaces one Criterion that another Case of the session, ratified or only stored, sets, writes or replaces too; a dropped Case, whose file is empty, a stored Case that the file of its top-level Case no longer holds, and a Case left out as estimate-case-check-leaves-out-a-case-the-file-supersedes sets are no such other Case"
>     ```
>   - change: `the Criterion replaced whole — a stored Case that the file of its top-level Case no longer holds is not compared (case 722.1)`
> - [ ] `guppi/casecheck.py`: `other_blocks` leaves out an entry of the store whose top-level Case file stands, holds text and holds no heading of its id; its docstring and the module docstring say so.
> - [ ] `tests/test_casecheck.py`: a `session_clash` test where a stored sub-case whose top-level file holds the Case whole without it gives no clash, and the same entry with its heading in the file gives one.
> - [ ] read `estimate-case-check-sends-back-a-clash-with-another-case`

> **ratification:**
> ```
> - decision[case 722.1][update][rule-case-check]{ref:rule-case-check}{supersedes:case 720}
> - decision[case 722.1][update][estimate-case-check-sends-back-a-clash-with-another-case]{ref:rule-case-check}
> ```

### Case 722.2 — The Spec hook removes a parent whose every sub-case is retired

> **given:**
> `rule-spec-write`: the rule of the `Stop` hook that writes a ratified Case into the Spec and removes a superseded one.
> **＋** `estimate-spec-write-removes-a-superseded-case`: its Criterion is replaced whole.
> **＋** `estimate-spec-write-answers-a-refusal`: the promise of the hook with `stop_hook_active` set.
> **＋** `guppi/ratified.py`: `remove_superseded`, which removes a superseded Case.
> **＋** `tests/test_ratified.py`: the tests of the removal of a superseded Case.
> **＋** `guppi/prespec.py`: `retired_whole`, the judgment of a parent retired sub-case by sub-case.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session, whose marks retire a Case.
> **＋** `raw/<hi date>/<hi HHMM>/spec.md`: the approved Spec of the session.

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds a decision line carrying `{supersedes:case N}`, and it has written the Case of that line in the same run.

> **then:**
> The hook removes the section of Case N — its heading, its sections, its `then` and `tasks` blocks, and the sections of its sub-cases — from the plan file.
> **＋** Once `raw/<hi date>/<hi HHMM>/spec.md` stands, it removes every section of Case N and of its sub-cases from it too.
> **＋** A `{supersedes:case N.M}` removes the section of that sub-case alone while another sub-case of its parent with a decision line is not retired; the parent and those other sub-cases stay.
> **＋** When the marks of the session's `raw/<date>/<hi HHMM>/ledger.md` and of the reply retire each sub-case of a parent that has a decision line, judged by `retired_whole` of `guppi/prespec.py`, imported, not copied, and the parent holds no decision line of its own that no mark retires, the hook removes the section of that parent too.
> **－** A parent with a decision line of its own that no mark retires stays in the plan file and in `raw/<hi date>/<hi HHMM>/spec.md`, though each of its sub-cases is retired.
> **＋** A section of Case N under `## Deferred` is removed the same way.
> **＋** With `stop_hook_active` set, the hook removes as without it, as `estimate-spec-write-answers-a-refusal` sets it.
> **－** A Case N that neither file holds — a Case of an earlier session, a defer taken up — is no refusal, and nothing is removed.
> **－** A line whose own Case the hook refused or did not write removes nothing.

> **tasks:**
> - [ ] update `rule-spec-write`
>   - old: `` removes the section of Case N — with its sub-cases, or `### Case N.M` alone when the line names a sub-case — from the plan file ``
>   - new: `` removes the section of Case N — with its sub-cases, or `### Case N.M` alone when the line names a sub-case, and then its parent too once the marks of the session's ledger and of the reply retire each sub-case of that parent with a decision line, by `retired_whole` of `guppi/prespec.py`, and the parent holds no decision line of its own that no mark retires (case 722.2) — from the plan file ``
>   - change: `the Spec hook removes a parent whose every sub-case with a decision line is retired (case 722.2)`
> - [ ] update `estimate-spec-write-removes-a-superseded-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a parent whose every sub-case is retired leaves the plan and spec.md (case 722.2)`
> - [ ] `guppi/ratified.py`: `remove_superseded` also removes each parent that `retired_whole` of `guppi/prespec.py` finds retired by the marks of the session's ledger and of the reply, when the parent holds no decision line of its own that no mark retires; the module docstring says so.
> - [ ] `tests/test_ratified.py`: `superseded` tests for a mark that retires the last sub-case of a parent, which removes the parent from the plan and from `spec.md`; a mark that leaves a sub-case with a decision line, which keeps the parent; and a parent with a `create` line of its own that no mark retires, which stays when its last sub-case is retired.
> - [ ] read `estimate-spec-write-removes-a-superseded-case`

> **ratification:**
> ```
> - decision[case 722.2][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 722.2][update][estimate-spec-write-removes-a-superseded-case]{ref:rule-spec-write}
> ```

### Case 722.3 — The Case schema says the parent leaves with its last sub-case

> **given:**
> `rule-case-protocol`: the page whose Render changes, put off again for another fault.
> **＋** `vault/wiki/case-schema.md`: the Render, read by `case-guppi`.
> **＋** `rule-spec-write`: the hook whose removal of a superseded Case the sentence describes.

> **when:**
> `case-guppi` reads the section `## Splitting` of `vault/wiki/case-schema.md`, the Render of `rule-case-protocol`.

> **then:**
> The section says that the hook of `rule-spec-write` drops the section of a sub-case its mark names, and the section of the parent as well once no sub-case of that parent with a decision line stays unretired and no line of the parent's own stays unretired.
> **－** The sentence of `vault/wiki/case-schema.md` on a Frontier line closed again by the superseding Case stays as it stands.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `a mark on a sub-case removes that sub-case alone,`
>   - new: `a mark on a sub-case removes that sub-case alone, and the parent with it once a mark retires each sub-case of the parent that has a decision line and the parent holds no decision line of its own that no mark retires (case 722.2),`
>   - change: `the Splitting section says the Spec hook removes a parent whose every sub-case is retired (case 722.3)`
> - [ ] defer `rule-case-protocol`
>   - type: `rule`
>   - purpose: `A Frontier line closed again by the superseding Case does not hold for a sprint or backlog item whose Case is taken back (pre-spec F5 of session 1804); put off again by Case 722.3, which retires decision-case-721 on this page for the sentence on the Spec hook`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`

> **ratification:**
> ```
> - decision[case 722.3][update][rule-case-protocol]{ref:rule-case-protocol}{supersedes:case 721}
> - decision[case 722.3][defer][rule-case-protocol]{ref:rule-case-protocol}
> ```
