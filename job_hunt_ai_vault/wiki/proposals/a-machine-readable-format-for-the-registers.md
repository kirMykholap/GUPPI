---
title: "A machine-readable format for `tags.md` and `authority.md`, and the dependency rule bends for it"
type: proposal
status: current
authority: register-file-format
basis: human
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-a-claim-is-looked-up-before-a-page-is-written/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md", "scripts/vault-authority.sh", "scripts/vault-check.sh", "pyproject.toml"]
decided_by: [[the-register-file-format-discussion-is-deferred-and-the-dependency-rule-is-named-not-lifted]]
tags: [vault, harness, process]
---

# The owner raised it and named the exception, 2026-08-21

> «Правило про лишние зависимости - окей. Но это то, что нам нужно. Нам нужен yaml или json или
> еще что-то для ведения тегов и authority. Запиши, обсудим на следующей сессии.»

**He is aware of the standing rule against new dependencies and is saying this is the case that
earns one.** Nothing is decided: the discussion is next session's, and the design is written down
here because it existed only in that exchange.

# The measurement behind it

**Five hand-written YAML parsers live in `scripts/`** — `vault-check.sh`, `vault-inject.sh`,
`vault-catalogue.sh`, `vault-units.sh`, and the `vault-authority.sh` this session added. Each one
re-derives what a key looks like, what a list looks like, and what a trailing carriage return does
([[the-yaml-class-is-pinned-to-lf]]).

**PyYAML 6.0.3 is already installed and is transitive**, absent from `pyproject.toml`. So the choice
is not *add a dependency or not* but *declare one that is present, or keep writing parsers around
it*.

# What is open, and it is more than the format

- **Which files.** `tags.md` and `authority.md` are the registers a script reads; `index.md`,
  `sprint.md` and `log.md` are prose a human reads and are not obviously in scope.
- **What Obsidian does with the result.** Both registers are opened by the owner in Obsidian today,
  and a `.yaml` or `.json` file is not a note. A format that a script parses and a human cannot read
  moves a cost rather than removing one.
- **Whether the unchecked half survives the move.** The value of these files is the definitions and
  the Russian aliases, and no format checks those
  ([[aliases-carry-the-question-across-languages]]). A structured file makes the *derivable* half
  cheaper, which is the half already audited in both directions
  ([[authority-becomes-the-index-and-is-required-outside-rules]]).
- **What it costs to keep.** Five parsers is a maintenance surface; one dependency is another. This
  is exactly the question the mechanism admission test would be for
  ([[an-admission-test-for-mechanisms]]).

**Recorded as raised, on his instruction, and not acted on.**

# The parser is declared, and the format is still open — 2026-08-22

**One of the two things this page treats as open is settled and it is the smaller one.** PyYAML is a
declared `dev` dependency in `pyproject.toml`, on the owner's ruling of this date
([[pyyaml-is-declared-rather-than-added-and-the-dependency-rule-is-not-opened]]).

**The measurement above is unchanged and its conclusion is confirmed**: the choice was never *add a
dependency or not* — it was *declare one that is present, or keep writing parsers around it* — and
the argument that carried it is that the harness holding onto another package's extra is itself the
fragility the rule guards against. **`uv lock` resolved 48 packages and PyYAML still resolves at
6.0.3.**

**What is still open is everything this page calls open**: which files, what Obsidian does with the
result, whether the unchecked half survives the move, and what it costs to keep. **The title's
second clause is now dated rather than pending** — *the dependency rule bends for it* was the
prospect on 2026-08-21; what happened instead is that the rule was found not to reach a package
already installed, so nothing bent.

**And the five hand-written parsers are all still hand-written.** The declaration makes replacing
them legal, not done, so this proposal is not built and is not retirable
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).
