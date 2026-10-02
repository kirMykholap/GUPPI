---
type: decision
case: "13"
status: current
create: ["[[rule-case-protocol]]", "[[estimate-case-protocol-loaded]]"]
origin: raw/2026-09-09/ledger.md#case-13
sprint: migration
created: 2026-09-09
tags: [session, workflow, ledger]
---

## When

**context.** Правило, которое агент видит всегда: как ведётся Case, когда он делится,
когда и как пишутся ledger-строки. Инструкция, не enforcement — хука на «закончил ли ты
Frontier» не бывает, поэтому текст стоит там, где агент его не пропустит: в `CLAUDE.md`.
Первый Leaf будущего `rule-plan-mode` (Slice 2), описан в `docs/migration/rule-plan-mode.md`
как ребёнок 1.

**now.** `CLAUDE.md` — bootstrap Slice 0: импортирует glossary и case-schema, несёт секцию
«Migration mode» с пунктом «ledger lines are written by hand … until the ledger hook
exists», который после Case 10 станет ложным. Шесть секций Case уже приходят через
`@vault/wiki/case-schema.md` — повторять их нельзя. Правило «fence — предпросмотр, голая
строка — запись» ратифицировано в Case 10 и ещё нигде не записано для агента. `/ask`
появится в Slice 2; до него «спросить vault» — чтение папок категорий.

**problem.** (а) текст секции; (б) правка «Migration mode» под появившийся хук;
(в) `parent: rule-plan-mode` указывает на страницу, которой нет до Slice 2.

**recommend.**

(а) Секция `## Case protocol` в `CLAUDE.md` между маркерами, ~20 строк, без повтора
case-schema:

```markdown
<!-- rule-case-protocol -->
```

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-13
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
- 2026-10-02 updated: the code fence of When closed: the text was cut off when the page was written; no content change (case 591.11) · [[decision-case-591.11]]
- 2026-10-03 updated: the check of its closed fence taken after the librarian's run of session 1202; the box of Case 591.11 in raw/2026-10-02/1202/spec.md ticked by Work Mode of session 2300 (case 606.2) · [[decision-case-606.2]]
