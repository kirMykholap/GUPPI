---
title: "A gauge is written by a script that runs the command, and the librarian only reads its errors"
type: decision
status: archived
authority: gauge-writing-mechanism
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md"]
tags: [vault, harness, record-schema]
---

# The ruling, 2026-08-25

The session proposed that the librarian write the number. The owner rejected that and gave the
ground:

> **owner:** «лучше сдлеать скрипт, который будет принимать четкий slug, Страницу что это за
> измерение и сам подставлять значения и ловить ошибку. А агент(бибилиотекарь) - будет запускать
> этот скрипт и видить, что есть ошибка.. нет такой странцы.. окей, пойду поищу.. Вот так мне
> кажется правильно. Агент решает, но механичсекие проверки и работу делает скрипт, что дает нам
> меньше стохастического поведения, понимаешь?»

Then he widened it from a per-line write to a sweep:

> **owner:** «Способ В — команду прогоняет сам скрипт. Мне нравится. То есть мы пишем в measure
> команду, а скрипт сам пишет число... Когда бибилиотекарь заканчивает писать страницы - запускает
> скрипт, который сам проходит все measure, вызывает команду которая там указана и вписывает рядом
> число.»

**The agent decides; the script does the mechanical work.** The librarian names the page and the
subject and runs the script; the script resolves them, refuses what it cannot resolve, runs the
command the region names, and writes the reading beside it.

**A refresh pass walks every measure region**, rather than each line being written where it is
noticed.

# Why the ground is not convenience

**A hand-written line is stochastic and a script's is not**, and the session had produced that exact
failure the same day: it wrote about forty `measure:` destinations in a grammar decided the day
before and never read
([[a-measure-line-names-its-destination-in-brackets-after-the-kind]]). The party writing a line by
hand is the party that does not know the slug.

# It keeps a live prohibition intact rather than overturning it

**A gauge that can be printed is never written by hand**, and that page stays `current`
([[a-measurement-is-testimony-or-a-gauge-and-the-role-decides-where-it-lives]]). **No hand writes
it here**: the region names the command, the script runs it, and the script writes the number. The
two rulings look like a collision and are not one — what the prohibition forbids is a human
transcribing a reading, and this mechanism removes the human from that step.

# Not done

**`scripts/vault-measure.py` does not exist.** No script was written on the day this was decided,
there is no measure region in the corpus for one to walk, and the design that remains open is on a
proposal of its own ([[the-measure-writer-script-and-what-it-refuses-to-do]]).
