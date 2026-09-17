# The categories — what Entity, Rule and Estimate are (discussion of session 1119, 2026-09-17)

A record of the discussion, not a decision. Deferred by case 230 to the next session; the
person thinks it over and the definitions come back as a Case. Written by the agent from
the chat; the words are the agent's, the objections are the person's.

## Where it started

`entity-sprint-migration` is the first live Entity page (case 209). The vault never said in
one place what an Entity is, why it exists, how it is cut and what it carries. Flag 3 of the
2238 handoff (`sprint.md` at `SessionStart`) opened the question; the person widened it.

## The person's questions

1. Render is a force of a Rule. Can an Entity render? No. Then the sprint page needs a Rule
   that renders it — and the text comes from the Entity page? Settled: `rule-sprint` is
   the Rule (`enforcement: check`, `governs: sprint.md`), the Entity is the data, the file
   is *computed* from the page by `guppi sprint`, not copied from a Render. The link runs
   Rule → file (`governs`) and script → page (the slug prefix); there is no field from the
   Entity to the Rule. The person: the categories and their edges must be explicit, so the
   agent does not do it "somehow".
2. If an Entity describes a file, there are hundreds of files. If not, what is it — its
   exact functions and criteria?
3. The sprint should be an order of milestones, not a flat backlog; the Frontier from the
   current milestone only; a true backlog for "some day". Done: case 229.
4. If an Entity has rules of behaviour, are those Rules? What separates an Estimate of an
   Entity from a Rule of an Entity?
5. Will the agent confuse a Rule bound to an Entity with a standalone Rule? What is needed
   so it does not?
6. Is a MOC Rule a sequence of steps? What is a MOC Entity — nesting only? What does an
   Estimate of a MOC Entity check, and one of a Leaf?
7. If a user wants to keep knowledge in a project (with code or without) — a new category,
   or the existing structure?
8. Does the model hold when there is no product code — a person configuring the harness for
   themselves, GUPPI as an assistant (the mechanic's helper)? Is Entity always about code?
9. "Why" and "what for": Rules answer what for, Entities why? Then every lesson could birth
   an Entity ("because of this case"). Worth building?

## Candidate definitions, in the order they fell

**A. Rule = a constraint on the work; Entity behaviour = Entity + Estimates.** (agent)
Fell: "who can violate it" does not separate — a developer can break anything, latency
included.

**B. Functional requirements = Rules of the Entity, non-functional = Estimates of the
Entity.** (person) Fell: the functional / non-functional line is fuzzy (security?), and the
happy path ("adding increments quantity") has no violation.

**C. Rule = any behaviour with a yes/no answer per action; Estimate = a number or a state of
the whole.** (agent) Fell on the person's example: "holds a million users — yes/no" reads
as a Rule. Double reading.

**D. Rule = a requirement with a home in code — a file whose job is this requirement and
nothing else (`implementation_ref`); Estimate on an Entity = a requirement without a home,
emerging from the whole, only measurable.** (agent) The person liked it, and found the
hole: the criterion is *after* building; at planning time it becomes "will there be a
home", and a load test can be claimed as one. Kept as the after-the-fact check, not the
criterion.

**E. Noun — condition — measure.** (agent, from the person's "look from the other end")
Entity = a noun the person named as part of what is built; Rule = a condition on each case
("never", "always", "each", "when X then Y"), refuted by one counterexample written as a
test case, always with a guard (the home is the consequence); Estimate on an Entity = a
measure of the whole ("holds", "fast", "clean", "merged", a statistic), no counterexample,
only a reading. One question: *a condition on each case, or a measure of the whole?*
Claimed consistency: a per-case condition can always be held by a guard (a timeout for
"every request under 200 ms"), a measure never; D and E are one criterion seen before and
after building. Worked through three scenarios (below). The person: the answers did not
convince — the model reads well with product code and badly without it.

**F. What the person put forward last.** The vault is a base of promises with elements
over them — decisions, rules, entities, estimates. Fine for development. For "a helper for
a car mechanic" it is not: the Entity describes nobody knows what — the client, the car,
the case — and the cases themselves are not in the vault at all but in a database. So
GUPPI has no ready structure for that and one must be built: code, a database, harness
rules for such a project. Perhaps the Entity *is* the breakdown case and the harness must
be extended. No universality in sight; Entity always ends up about code.

## The agent's position at the close

- The vault is a base of promises with evidence; that is not about code. The *category
  set* `entity / rule / estimate` is the vocabulary of development and is not universal;
  stretching Entity to "a breakdown case" makes the vault the product's database and the
  harness a specialist of every domain — the panacea, not to be built.
- The mechanic example holds two requests: *build* a helper (product code; the development
  categories fit) and *be* the helper (GUPPI runs the case: `/hi`, a Case with
  `context / problem / recommend`, a hypothesis as `estimate[Research]`, "what to check" as
  `method`, the outcome an `estimate[...][passed|failed]` line, the conclusion a
  `lesson[knowledge]` with `source`, similar cases an Insight, a brief between visits).
  The mechanism fits whole; only the nouns differ — `case-`, `symptom-`, `check-` instead
  of `entity-`, `rule-`.
- So the universality is at the level of the mechanism — ratification, ledger, pages from
  the ledger by schema, lint by schema, lessons → insights, brief — and the missing step is
  **the category set as data of the project**: `materialize` already lifts by
  `schema.yaml` (214.1) and lint checks by it (212); `generate` still holds the categories
  in code (`INITIAL_STATUS`, `REF_FIELDS`). A development project takes the default set; a
  mechanic's project its own, with the same `lesson / insight / decision`. After the
  migration. Written into the sprint's Backlog by case 229.1.
- "Why" per Entity: not to build. The why of a harness rule is stored three times already
  — `## Purpose`, `origin` (the Case), and the lessons behind it through Insight →
  `addressed_by`. An Entity per why is a fourth copy of the Decision page, and every lesson
  would propose a new thing.
- Recommended for now, to be discussed: record the *development* definitions only, short —
  Entity a named thing to be built with `code_ref`, a kind not an instance; Rule a
  condition on each case with a guard; Estimate the evidence, a test on a Rule, a measure
  of the whole on an Entity; the harness a tree of rules without an Entity over it, a
  recorded exception (the sprint is a thing of the harness and an Entity, so "not about the
  harness → Entity" cannot be the criterion). Without `applies_to`, without new `kind`s —
  the product model is early. The person wants to think more before that.

## Pieces that came out along the way (not decided, not lost)

- **MOC Rule = a process**: ordered children and an Estimate on the order
  (`rule-end-of-work` + `estimate-end-of-work-order`). A group of similar rules without an
  order is a tag, not a MOC. `rule-harness` and the other MOC rules stay rules.
- **MOC Entity** = a thing whose parts the person named; its Estimates measure what no
  child owns; a Leaf's measure its own scope. A Leaf with empty `rules` and `estimates` is
  legal — the person said nothing yet. The MOC/Leaf difference is the presence of children;
  §6 cuts a Leaf in Retro when the closing judgment falls apart.
- **The edge Entity ↔ Rule**: `applies_to` on the Rule written in the Case, `rules` on the
  Entity written by `generate` as a backlink (one source, like `parent` / `children`).
  Lint holds `enforcement: code` ⇔ `applies_to`. A rule with `applies_to` leaves the rules
  Grep of `ask-guppi`; the entry for a product question is the entities Grep, then the
  edges `rules` / `estimates`; a duplicate of a product rule is looked for in the `rules`
  of that Entity (precedent: Estimates have no index, reached through `target`, case 193).
- **`kind: test | measurement | reading`** instead of `QA | Research`: `test` only on a
  Rule (at least one), `measurement` only on an Entity (without a bar it is research),
  `reading` on either. Makes the boundary machine-checked. The person's instinct that the
  kinds are wrong; the agent's proposal.
- **A measure begets a rule** (scenario 2): "slow" (a failed measurement, recorded first as
  debt) → "each image ≤ 200 KB" (a condition with a guard). A normal order of work.
- **Pre-task for a product** — the questions before records: the DoD of the root; the
  numbers behind "fast" / "minimum"; what is outside; whether two words are one noun; the
  first milestone.
- **Knowledge of the user**: no new category. Knowledge a rule or a measure leans on —
  `lesson[knowledge]` with `source`, clustered by Insights, checked by the rule that leans
  on it (as today). Knowledge nothing leans on — not a vault page: `vault/notes/` outside
  `wiki/`, unchecked, unread by `ask-guppi`, like `raw/`; the moment a rule leans on a
  note it becomes a `lesson[knowledge]` through a Case. A product's knowledge base is
  product data, `entity-knowledge-base` with `code_ref` outward.
- **Entity = a kind of thing, not an instance**: `entity-lesson` is a page, lesson 7 is
  data. The agent transcribes the nouns the person named and invents none; brownfield code
  without a promise gets no page.

## The three scenarios (agent's answers, which the person did not find convincing)

1. Empty project, a diagnostic helper for a car workshop: `entity-diagnostician` (MOC) with
   a measure "≤ M hypotheses after ≤ K questions on N reference cases" (N, K, M asked);
   children the nouns — complaints, knowledge base (`code_ref` outward), hypotheses,
   questions, checks; rules — "each question removes ≥ 1 hypothesis", "each check names
   the hypotheses it splits", "a hypothesis is in the knowledge base" (to be asked).
2. Existing Telegram mini app, "images on page X load slowly": `entity-miniapp` (root, only
   the pages the person names), `entity-page-x` with `estimate-page-x-images-load-time`
   read `failed` first (the debt recorded before the work); the fix may add a rule with a
   guard ("each image ≤ 200 KB, WebP").
3. A system-design course app: `entity-sd-course` (MOC, no measure named — ask the DoD),
   `entity-lesson` with "each lesson followed by a quiz", "each lesson's dialogue recorded",
   `entity-lesson-request` with "each request yields a lesson draft"; lessons are data.

## Open for the next session

- The person's objection F: is there a universal definition of Entity, or is the
  development set one set among several and the category set the thing to make data?
- Whether to record the development definitions now (short) or wait for the wider model.
- If recorded: `index.md` §1 and §6, `glossary.md`, `entities/schema.md` (Entity a noun,
  a kind not an instance, `rules`, an empty Leaf legal), `rules/schema.md` (`applies_to`,
  `enforcement: code`, MOC = process), `estimates/schema.md` (three kinds),
  `lessons/schema.md` (the knowledge boundary), `vault/notes/`.
