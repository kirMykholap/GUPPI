## Case 512 — A number in a round stands only beside a quotation of what it points to

> **context:**
> When a Case needs a choice, `case-guppi` first asks the person a round of questions. Today its instructions say that case numbers, the history of a slug and facts of the frame stay out of the context and the question bodies and stand in the `➡️` line as the source of the recommendation. The last reading of `estimate-case-build-writes-a-plain-round` failed. One first round named "case 193" in its Context, and another round named "Cases 506 and 507" in a Now line. The person looked at the problem more widely than where the number stands. A bare number tells them nothing: to use it they must already know what that Case says, and the agent then argues from it as if they did. In the person's words, translated from the chat: "If the agent refers to some case or historical fact, it is better to give it as a quotation from what it refers to."
> Over four rounds the person decided the following:
> - The rule is for rounds only. The `context` of a Case is read mainly by the agent and becomes history on the Decision page, so it keeps its numbers and details. `problem` and `recommend` work well as they are, so the rule on the story of a Case (`rule-case-protocol`) does not change.
> - A round says things in plain words and uses no number where plain words are enough. A case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in a round only beside a short quotation of the words it points to, as the source of that quotation. This holds in any line, the `➡️` line included.
> - A page name in a code span is not such a reference. It stays where the question is about that page.
> - This Case supersedes Case 511.2, which replaced the Criterion of the same Estimate earlier in this session and kept the old line on case numbers. Signing that Criterion again in a second wording is the fault recorded in `lesson-case-build-signs-one-criterion-twice-in-a-session`. So this Case carries both changes of 511.2. The list lines of the Criterion are carried word for word. The list sentence of `rule-case-build` now only points to the grill-me template and says no list shape of its own. Pre-spec found that the wording of 511.2 said the shape again, which the `then` line "word no shape of their own" forbids, and the person accepted the fix. Case 511.1 stands, and the Frontier line that Case 511 closed stays closed by it. The parent text of Case 511 still says the Case splits into two sub-cases. That is now true only of its record, and the person sees it when 511 is shown again, if ever.
>
> The Criterion is replaced whole. The check of the answer notes four lines of the live Criterion that are not carried word for word. Each is dropped on purpose:
> - "The instructions of `case-guppi` point each question to the question shape…" is carried in the wording of Case 511.2, which adds the lists of the Context.
> - "The shape of a question is read by `estimate-skill-grill-me-asks-in-rounds`, not here" is carried in the wording of Case 511.2, which adds what counts as a list.
> - "Case numbers, the history of a slug and facts of the frame stand in the round only in the `➡️` line…" is replaced by the plain-words line and the quotation line. "Facts of the frame" is dropped because the person named numbers and history. A frame fact said in plain words does the harm the person described no more than any other sentence.
> - "The `context` of a Case keeps its case numbers and frame facts…" is widened to the `context`, `problem` and `recommend` of a Case, as the person chose rounds only.
>
> The `purpose` of the Estimate still says "case numbers only in the recommended answer", and its `method` counts "four parts", so both are set new.
>
> From the frame, these stand:
> - `rule-skill-wait-what` and `estimate-skill-wait-what-re-pitches` say the main agent's re-pitch holds no case number and that "A quoted line keeps its case numbers as written". This agrees with a number that stands beside its quotation.
> - `estimate-skill-grill-me-asks-in-rounds` leaves "the place of its case numbers" to this Estimate. That remains true.
> - `rule-case-protocol` lets the story sections of a Case "name a case number as the source of a claim". This Case leaves that as it is.
> - `estimate-case-build-writes-the-case` does not speak of numbers.
>
> No code reads a round: a search of `guppi/` for case numbers and `➡️` finds nothing. So no reader keeps an old form. The Case creates no page, so no vault query was run. Not done: the story sections of a Case, and a mechanical check of a round, which the person did not choose.

> **problem:**
> A round sends the person to a bare case number, a session id or the history of a page. That tells them nothing unless they already know what it points to, and the agent argues from it as if they did. The instructions allow such numbers in the `➡️` line, and the numbers still slipped into the Context and the Now lines.

> **recommend:**
> Let a number stand in a round only beside a short quotation of the words it points to, and write the rest in plain words. The quotation carries the meaning, and the number beside it only names the source. Supersede Case 511.2 and carry its list change, so that the Criterion is signed once in this session. A round with no number at all was rejected: it hides where a quotation comes from.

> **given:**
> `rule-case-build` — the rule page whose Render holds the round instructions of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from it.
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill whose template sets the question shape and what a list is.
> **＋** `estimate-case-build-writes-a-plain-round` — the promise on a readable round.
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape of a question and of a list.
> **＋** `rule-case-protocol` — the rule on the story sections of a Case, left as it is.
> **＋** `rule-skill-wait-what` — the rule on the main agent's re-pitch, whose quoted lines keep their numbers.

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
> **＋** A list in the `**Context:**` stands one item per line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a list.
> **＋** The instructions of `case-guppi` point each question, and each list of the Context, to `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
> **＋** The round says what it rests on in plain words and uses no number where plain words are enough.
> **＋** A case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in any line of the round, the `➡️` line included, only beside a short quotation of the words it points to, as the source of that quotation.
> **＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
> **－** A page name in a code span is no such reference: it stays where the question is about that page.
> **－** The shape of a question, and what counts as a list, are read by `estimate-skill-grill-me-asks-in-rounds`, not here.
> **－** The `context`, `problem` and `recommend` of a Case keep their numbers as `rule-case-protocol` allows: this promise is about a round only.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old:
>     ```
>     a part with nothing to say left out. Write the round for a person who has not opened the pages
>     ```
>   - new:
>     ```
>     a part with nothing to say left out. A list in the context stands as the grill-me template sets a list. Write the round for a person who has not opened the pages
>     ```
>   - old:
>     ```
>     case numbers, the history of a slug and facts of the frame stay out of the context and the question bodies, and stand in the `➡️` line as the source of the recommendation, and in the `context` of the Case;
>     ```
>   - new:
>     ```
>     say in plain words what the round rests on, and use no number where plain words are enough; a case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in a round, in any line and the `➡️` line too, only beside a short quotation of the words it points to, as the source of that quotation, never alone; a page name in a code span is no such reference and stays where the question is about that page; the `context`, `problem` and `recommend` of the Case keep their numbers;
>     ```
>   - change: `a list in the Context of a first round stands as the grill-me template sets a list; a number in a round stands only beside a quotation of what it points to (case 512, supersedes 511.2)`
> - [ ] update `estimate-case-build-writes-a-plain-round`
>   - set: `{status: pending, purpose: "Whether a round of case-guppi gives the mechanism with a concrete example, a list one item per line, a number only beside a quotation of what it points to, and an unknown term explained", method: "by hand, in a session after the render: one first round and one later round of case-guppi read in the chat against the Criterion"}`
>   - change: `the Criterion replaced whole — a list in the Context one item per line; a number in any line of a round only beside a quotation of what it points to (case 512, supersedes 511.2)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-a-plain-round` — in a later session after the render: one first round and one later round of `case-guppi` read in the chat against the Criterion

> **ratification:**
> ```
> - decision[case 512][update][rule-case-build]{ref:rule-case-build}{supersedes:case 511.2}
> - decision[case 512][update][estimate-case-build-writes-a-plain-round]{ref:rule-case-build}{supersedes:case 511.2}
> ```
