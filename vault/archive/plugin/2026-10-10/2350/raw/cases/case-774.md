## Case 774 — The opening-and-close note leaves the current milestone

> **context:**
> The sprint page `entity-sprint-plugin` lists its milestones in order, and `guppi sprint` renders them into `vault/wiki/sprint.md`. A milestone line that names no page is a note: it is never ticked, and it keeps its milestone open until a Case removes it or cuts it into items (`rule-sprint`). The current milestone `The sprint turn and GitHub` opens with the note on the opening and the close of a sprint. That note can end only when `plugin` closes, so the milestone would stay open to the end of the sprint. The person found this odd and asked to decide now what can be decided. The close is already held twice: the last milestone `The plugin` ends with the close line, and the Done-when Estimate `estimate-sprint-plugin-close-steps-run-from-the-line` checks the closing session from that line. The skill `/sprint-close` puts off every other open line of the closing session (`rule-skill-sprint-close`, step 2), so a note moved there would only be put off. The next opening of a sprint comes after `plugin` closes, so none of the five Done-when Estimates of `entity-sprint-plugin` checks an opening. Its one known flaw, the merge step deferred by case 771, is the Frontier item C9 of this session, ratified as Case 775: its sub-case 775.1 creates `estimate-skill-sprint-open-merges-the-closed-sprint-branch`, a check of the text of the skill `/sprint-open` read at the Retro of this session, which targets `rule-skill-sprint-open` and not the sprint page. The person chose to remove the note, and to make the Purpose name only the close, since none of the Done-when Estimates of `entity-sprint-plugin` covers the opening. The pair on the Purpose and the `set` of `purpose` change the one sentence of the page that names the opening. The Done-when sentence of the Purpose already names only the close and stands. The close line of `The plugin` stands as it is, so the Criterion of `estimate-sprint-plugin-close-steps-run-from-the-line`, which quotes that line, stands. The Criterion of `estimate-sprint-renders-the-backlog` states how a note renders and keeps its milestone open, for any sprint page. It checks the render of this change and stands. A Grep `opening and (the )?close of a sprint` over the repository, `vault/raw/` left out, printed `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/entities/entity-sprint-plugin.md` and `vault/wiki/lessons/lesson-hi-brief-line-judged-apart-from-a-broad-milestone-line.md`. `sprint.md` is rendered anew by the task of this Case. The brief is written anew by the librarian's next run. The lesson's trigger records what happened in an earlier session and stays true. The current milestone does not close by this Case: its line on the repository on GitHub keeps it open.

> **problem:**
> The current milestone of `entity-sprint-plugin` holds a note that can end only at the close of the sprint, which is already the last line of the last milestone, so the current milestone cannot close before the sprint does.

> **recommend:**
> - **Where does the opening-and-close note go?**
>   - Recommended: (a) remove the note; the close line of the last milestone and its Done-when check hold the close, and the other Case of this batch holds the known flaw of the opening.
>   - Answer: agreed, (a).
> - **Does the sprint Purpose still name the opening?**
>   - Recommended: (b) change the Purpose and its `purpose` field to name only the close, since nothing in this sprint checks the opening.
>   - Answer: agreed, (b).

> **given:**
> `entity-sprint-plugin`: the sprint page whose milestone note and Purpose change.
> **＋** `vault/wiki/sprint.md`: the file `guppi sprint` writes from the sprint page.
> **＋** `estimate-sprint-plugin-close-steps-run-from-the-line`: the Done-when check of the close, which quotes the close line.
> **＋** `estimate-sprint-renders-the-backlog`: the check of the render of `vault/wiki/sprint.md`.
> **＋** `rule-sprint`: a note leaves its milestone only by a Case.

> **when:**
> `uv run guppi sprint` writes `vault/wiki/sprint.md` from `entity-sprint-plugin`, and someone reads the page or the file.

> **then:**
> The milestone `The sprint turn and GitHub` of `entity-sprint-plugin` holds the line on the repository on GitHub alone.
> **＋** The Purpose of `entity-sprint-plugin` and its `purpose` field say that the close of a sprint works with no fix by hand, and do not name the opening.
> **－** The close line of the milestone `The plugin` stays as it was, as `estimate-sprint-plugin-close-steps-run-from-the-line` quotes it.
> **－** The milestone `The sprint turn and GitHub` does not close by this change: its line on the repository on GitHub keeps it open.

> **tasks:**
> - [ ] update `entity-sprint-plugin`
>   - old: `and the opening and close of a sprint work with no fix by hand.`
>   - new: `and the close of a sprint works with no fix by hand.`
>   - old:
>     ```
>     - the opening and the close of a sprint run with no fix by hand and each flaw found in them is fixed
>     - the repository on GitHub set up so that a pull request from another person is easy to review
>     ```
>   - new:
>     ```
>     - the repository on GitHub set up so that a pull request from another person is easy to review
>     ```
>   - set:
>     ```
>     purpose: "GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand"
>     ```
>   - change: `the note on the opening and the close of a sprint leaves the milestone The sprint turn and GitHub; the Purpose names only the close`
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 774][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```
