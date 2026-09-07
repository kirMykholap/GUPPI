---
title: "PyYAML is declared rather than added, and the no-new-dependencies rule is not opened"
type: decision
status: current
authority: dependency-declaration
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-22
created: 2026-08-22
sources: ["pyproject.toml", "uv.lock", "scripts/vault-authority.sh", "scripts/vault-check.sh"]
tags: [harness, vault, process]
---

# The ruling, 2026-08-22

**`pyyaml>=6.0` is a declared `dev` dependency in `pyproject.toml`.** It was already installed and
already imported by the vault scripts before this date, arriving **only as a transitive extra of
`uvicorn[standard]`** — so the choice was never *add a dependency or not*, but *declare one that is
present, or keep relying on another package's extra*.

**`uv lock` resolved 48 packages and PyYAML still resolves at 6.0.3.** The lock gained two lines: the
package was already in the graph, and what changed is who asks for it.

# The argument the owner accepted

**The harness holding onto another package's extra IS the fragility the no-new-dependencies rule
exists to prevent, not an instance of it.** `uvicorn[standard]` may drop `PyYAML` in any release, or
the web stack may change — and on that day five scripts that parse YAML would break for a reason
none of them names, in a repository where nothing declares the package at all. An undeclared
dependency is a dependency whose removal is silent.

**It is a `dev` dependency and not a runtime one**, because nothing about the product needs YAML.
The vault's scripts, its schemas and its registers are the only readers
([[vault-scripts]], [[the-per-folder-frontmatter-schema]]).

## Rejected: a generated `.tsv` sidecar beside each register

It would let the scripts read a structured file without any parser at all. **It buys the structure by
adding a generated artefact that can go stale**, which is the shape this store has already replaced
once — the generated catalogue became a query for exactly that reason
([[the-page-list-is-a-query-not-a-generated-file]], [[a-copied-list-drifts-and-a-sweep-cannot]]).

## Rejected: leaving five scripts hand-parsing YAML

`vault-check.sh`, `vault-inject.sh`, `vault-catalogue.sh`, `vault-units.sh` and `vault-authority.sh`
each re-derive what a key looks like, what a list looks like, and what a trailing carriage return
does ([[the-yaml-class-is-pinned-to-lf]]). **Five parsers is a maintenance surface that has already
drifted**, and leaving it in place to avoid declaring a package that is installed anyway is paying
the cost twice.

# What this does NOT do, and the boundary is the point

**It does not open the dependency rule.** *Add no new dependencies — neither Python packages nor
npm* stands unchanged, and this decision is not a precedent for the next package: nothing was
installed here, and the ruling turns on the package already being present and already imported.
**A reader who wants a new dependency still has to ask** ([[ask-before-weakening-or-working-around-a-rule]]).

**It closes a hole under the rule rather than making an exception to it.** The rule's subject is what
this repository *depends on*; a package that is depended on and undeclared was outside the rule's
reach while being exactly what the rule is about — a rule that reads the manifest cannot see a
dependency that is not in it ([[no-rule-reads-a-harness-file]]).

**And it does not decide the register format.** Whether `tags.md` and `authority.md` become
machine-readable files is a separate question, still open and still the owner's — the parser being
declared removes one obstacle from that design and answers none of its four open points
([[a-machine-readable-format-for-the-registers]]).

**Nothing has been rewritten to use it.** The five hand-written parsers are all still hand-written;
this decision makes replacing them legal, not done.
