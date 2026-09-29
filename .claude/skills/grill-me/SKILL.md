---
name: grill-me
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each question should be formatted like so:

    ❓ **Q1** - **<question title>**:

    **Now:** <what holds today, said once for the question; "nothing exists yet" when nothing does>

    - **(a) <option name>**
      - **After:** <what holds with this option>
    - **(b) <option name>**
      - **After:** <what holds with this option>

    ➡️ <your recommended answer, and why>

The body of a question starts on the line after its title. The `**Now:**` line says once what holds today. Each option starts on its own line as a list item with its name in bold, and under it stands one nested `**After:**` item: what holds with this option. An option has nothing else under it: no list of costs, no second item, no other label. A cost, when it matters, is a plain sentence inside the `**After:**` text or in the reasoning after `➡️`. Every question takes this shape, one on a new idea with nothing behind it too. In the language of the chat the labels may stand translated; the shape stays.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), find it yourself, or dispatch a sub-agent when you can dispatch one; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the shared understanding is confirmed: by the user's word, unless the instructions that started the grill name another confirmation.
