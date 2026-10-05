## Case 673 — A decision line that gains a mark stands beside the first

> **context:**
> When the person ratifies a Case again in its session, the reply that acknowledges it carries all of its decision lines again (case 390). The ledger hook skips a line it already holds word for word. A line that gained a mark is new text, so the ledger keeps both lines. In session 1831, lines L16, L17 and L20 of Cases 669.6, 669.7 and 669.10 were written again as L41, L42 and L43, each with `{supersedes:case …}` marks added. `guppi generate` applied the first line of each pair and printed for the second that it repeats the first, with nothing applied. The marks still retired 659, 630, 617 and 622, since `materialize` puts the marks of every line of a Case into the record of that Case, and `generate` writes the Decision page from that record before it judges a repeat. The log of the vault shows the four pages superseded and archived, and the brief says that the three pages changed once. Nothing went wrong. The handoff of 1831 noted that no check catches the pair, and the brief made it a Frontier item.
> The Purpose of `rule-page-generation` already says that a Case approved again in its session, with its lines written again and a mark added, changes each page once (cases 514, 522). The main agent does not load that page. It loads `vault/wiki/orchestration.md`, whose paragraph on the acknowledging reply says only that the ledger hook does not append a line it already holds. The person chose one sentence there, and no new check. The sentence changes no behaviour, so no Estimate is created or replaced. `estimate-generate-fails-alone` checks the repeat that changes no page, and `estimate-materialize-marks-superseded` checks that the record of a Case lists every Case its lines name; their Criteria state what the sentence says, so they stand. `estimate-generate-writes-the-decision-page` checks that a `supersedes` sets the earlier page `superseded`, which is how the mark retires the earlier decision. `estimate-ledger-write-lifts` checks that a body already in the ledger is not written again, which is why a marked line, a new body, is written. Their Criteria stay true, so they stand. `estimate-orchestration-acknowledging-reply` says that the ledger hook does not append a repeated decision line a second time; a line with a mark added is not a repeat of the first line's text, so that line stays true and the Criterion stands. `estimate-orchestration-loaded` promises that the file equals the Render, that it holds what the main agent alone does, and that `CLAUDE.md`, `case-schema.md` and `ratification.md` repeat no paragraph of it. The new sentence keeps all three true, so its Criterion stands (case 378.5).
> A Grep of `with a mark added|re-ratification` over `vault/wiki/rules/` printed `rule-spec-write.md`, `rule-page-generation.md`, `rule-orchestration.md`, `rule-case-protocol.md` and `rule-prespec-onward.md`. The hits in `rule-spec-write.md`, `rule-case-protocol.md` and `rule-prespec-onward.md` are History lines. The hit in `rule-page-generation.md` is the sentence above, which stays true. The hit in `rule-orchestration.md` is the paragraph this Case extends. A Grep of `ratified again|re-ratification|mark added` over `.claude/` printed nothing, so no harness file sets a form for these lines. Case 672 of this session changes another paragraph of `rule-orchestration`, the one on who ticks which box, and renders the same file; the two new texts do not touch the same sentence and do not contradict each other. The near backlog item `rule-ledger-write` carries the defer of decision 442, on a lesson line with no mark; this Case does not take it up, and it stands. The Frontier line of this item has the source `brief`, so no supersede mark is due.

> **problem:**
> A Case ratified again with a mark added to a decision line leaves two lines for one decision in the ledger. The rule of `generate` says that this is expected and harmless, but the main agent does not read that rule. So the handoff reports the pair as a gap, and the pair comes back as a Frontier item.

> **recommend:**
> - **Whether anything changes for a ledger line written again with a mark added**
>   - Recommended: (a) one sentence in the orchestration file the main agent loads: the marked line stands beside the first, the page changes once, and the mark still retires the older decision; no new check.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: its Render says what the reply that acknowledges a re-ratification carries.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-page-generation`: the rule of `generate`, whose repeat changes a page once.

> **when:**
> The main agent reads `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, after the person ratified again a Case whose decision line gained a mark.

> **then:**
> The file says that the ledger keeps the marked line beside the first line of the same Case, kind and target.
> **＋** The file says that `guppi generate` of `rule-page-generation` changes the target page once and takes the marked line for a repeat.
> **＋** The file says that the mark still retires the earlier decision.
> **－** No check reports the two lines.
> **－** Case 673 does not change `rule-page-generation`.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `writes a Case into the Spec only after a reply that carries its lines (case 390).`
>   - new: `` writes a Case into the Spec only after a reply that carries its lines (case 390). A decision line that gained a mark, such as `{supersedes:case N}`, is new text: the ledger keeps it beside the first line, `generate` changes the page once and takes the marked line for a repeat, and the mark still retires the earlier decision, since the record of a Case takes the marks of all its lines (`rule-page-generation`, case 673). ``
>   - change: `a decision line that gains a mark at a re-ratification stands beside the first; the page changes once and the mark still applies (case 673)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`

> **ratification:**
> ```
> - decision[case 673][update][rule-orchestration]{ref:rule-orchestration}
> ```
