# AMA s brněnskými politiky — rozcestník

Série AMA („Ask Me Anything") s lidmi, kteří kandidují do Zastupitelstva města Brna, před komunálními volbami 9.–10. 10. 2026.

**Je to pilot.** Formát tohoto typu se tu ještě nedělal.

## Stránky

| Stránka | Co v ní je |
|---|---|
| [/r/brno/wiki/ama/moderace](/r/brno/wiki/ama/moderace) | Jak moderujeme AMA vlákna — kategorie zásahů, odvolání, který model to jede a podle čeho |
| [/r/brno/wiki/ama/jak-se-ptat](/r/brno/wiki/ama/jak-se-ptat) | Jak formulovat otázku, aby nešla obejít — vzory a modelové dvojice |
| [/r/brno/wiki/ama/pozvanka](/r/brno/wiki/ama/pozvanka) | Text pozvánky pro kandidující uskupení, doslova a v plném znění |
| [/r/brno/wiki/ama/dotaz-udhpsh](/r/brno/wiki/ama/dotaz-udhpsh) | Dotaz na Úřad pro dohled nad hospodařením politických stran — znění, datum, stav |

Shrnutí jednotlivých AMA přibývají jako `ama/RRRR-MM-DD-subjekt`.

## Kde se to dělá

Všechna pravidla, prompty i logy běhů jsou veřejné v [github.com/kerray/r-brno](https://github.com/kerray/r-brno):

- `wiki/ama/` — tyto stránky
- `rules/curation-key.md` — psaný klíč pro výběr povinných 15 otázek
- `rules/removal-reasons.md` — přesná znění, která dostanete při moderačním zásahu
- `prompts/` — prompty, kterými se pouští jazykový model (`claude-sonnet-5`)
- `runs/` — logy jednotlivých běhů (vstup, výstup, lidské odchylky, náklad)

Prompt platný pro dané AMA se **zamrzne ve chvíli otevření sběrného vlákna** a otaguje. Od té chvíle se nemění jinak než veřejně.

## Připomínky

Připomínky k pravidlům i k promptům jsou vítané — nejlépe jako issue nebo pull request v repozitáři, nebo modmailem. Nejužitečnější jsou **dřív, než pravidlo poběží naostro**.
