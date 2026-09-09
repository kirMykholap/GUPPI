---
paths:
  - "probe/*.md"
---

<!-- PROBE-COMMENT-9M3ZR8 -->

# Path-scoped probe rule

PROBE-TEXT-4K7QX2

This file is a temporary measurement, not a rule anybody has to obey. It exists to answer
four questions that the vendor documentation does not:

1. does a path-scoped rule reach the main session when it reads a matching file
2. does it reach a SUBAGENT that reads a matching file - the blocker
3. is an HTML comment in a rules file stripped before the model sees it
4. after `/compact`, does Edit demand a re-read - which would re-trigger this rule

The two strings above are nonces. `PROBE-TEXT-4K7QX2` sits in plain text and answers
questions 1, 2 and 4. `PROBE-COMMENT-9M3ZR8` sits inside an HTML comment and answers
question 3: if a reader can quote it, comments in a rules file are NOT stripped and a
"generated, do not edit" banner would cost context.

Neither string is guessable, so "I can see it" cannot be confused with "I inferred it".

Delete this file when the probes are answered.
