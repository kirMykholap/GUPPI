---
title: "A filter sits at the top of a dispatcher and still takes the case number"
type: concept
status: current
authority: filter-placement
basis: code
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# Where the filter goes, and why the placement is the whole of it

**The expensive part happens between the top of a dispatcher and its verdict** — a copy of the whole
vault tree per case, and a full gate run over it. A filter applied at the verdict discards the
answer after paying for it.

**So `--only <pattern>` is decided at the top of the dispatcher**, before the sandbox is built.

# And it must take the case number anyway

**Results are numbered as they are dispatched**, so that two runs of a green suite are
byte-identical and a diff of them is a diff of the suite rather than of the scheduler
([[no-verdict-lives-in-a-variable-in-a-parallel-suite]]).

**A filter that stopped the counter would renumber every case after it**, and a report whose numbers
move between runs cannot be compared to the previous one. `wanted()` therefore consumes the number
even when it refuses the case.

# The floor this leaves, and it is measured rather than assumed

**A filtered run has a floor of about two minutes**: the sandbox is still built, and the cases
written inline run their bodies even when their verdicts are discarded. Measured 2026-08-24 at
2m24s for eight cases and 2m59s for eleven, against a full run of over half an hour.

**Moving the check earlier for those cases means rebuilding fifteen working cases of the archive
section**, which is why the floor stands rather than being repaired
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).
