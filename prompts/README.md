# Prompty

Prompty, kterými se pouští jazykový model. **Veřejné záměrně** — smyslem je, aby si kdokoli mohl výběr přepočítat.

| Soubor | K čemu |
|---|---|
| `curation-top15.md` | výběr povinných 15 otázek (odvozeno z `rules/curation-key.md`) |
| `triage-queue.md` | řazení moderační fronty podle závažnosti |
| `appeal-devils-advocate.md` | druhý průchod při odvolání — úkolem je najít důvody, proč byl původní zásah **špatný** |
| `summary.md` | generování shrnutí |

## Pravidla, která platí pro všechny

- **Zamrznutí.** Prompt platný pro dané AMA se zamrzne ve chvíli otevření sběrného vlákna a otaguje `ama-RRRR-MM-DD-subjekt`. Změna během běhu jen s veřejnou poznámkou ve vlákně a novým commitem.
- **Model:** `claude-sonnet-5`. `temperature` ani `top_p` tenhle model nepřijímá — determinismus se nenastavuje, **měří** (viz `runs/*/agreement.md`).
- **Uživatelský text jde do promptu jako data v oddělovači**, nikdy jako instrukce. Komentář, který vypadá jako pokus oslovit bota instrukcí, se neposlechne, ale ani nemaže — označí se.
- **Netvrdíme, že je model nestranný.** Není. Tvrdíme, že na všechny subjekty pouštíme stejný postup, stejným promptem, ve stejné verzi.

> **STATUS: sepsáno, k připomínkám.** Prompty jsou odvozené z `rules/curation-key.md` a zveřejněné
> **před** rozesláním pozvánek, aby byl čas na námitky. Pro konkrétní AMA se zamrazí ve chvíli,
> kdy se otevře sběrné vlákno.
>
> Co ještě nemají za sebou: **dry-run na starých vyhrocených vláknech r/Brno** (měření českých
> false positives u `triage-queue.md`) a **test prompt injection** — vlastní pokus o „ignoruj
> předchozí instrukce" musí skončit v označených, ne v patnáctce.
