# Psaný klíč pro kuraci povinných 15 otázek

> **STATUS: NÁVRH.** Ještě neplatí pro žádné AMA. Zdroj pravdy je zatím playbook; tenhle soubor se z něj dopisuje.
> Prompt `prompts/curation-top15.md` se odvozuje **z tohoto klíče**, ne obráceně — smyslem je mít lidsky čitelnou verzi, kterou lze citovat.

## Krok 1 — co se do výběru nedostane

- Není to otázka (samotné tvrzení, komentář, vtip). Zůstává ve vlákně.
- Duplicita → sloučí se s původní. **Skóre shluku = max(skóre), NIKDY součet** — sčítání by z počtu účtů udělalo násobič hlasů. Členy shluku i jejich skóre zveřejňujeme.
- Osobní útok / doxx (už zachyceno moderací).

**Vědomě NEfiltrujeme** otázky „mimo kompetenci města" — je to klasická úniková odpověď a rozhodovat o kompetenci za hosta není naše práce.

## Krok 2 — složení patnáctky

| Sloty | Klíč | Kdo vybírá |
|---|---|---|
| 10 | nejvýše hlasované otázky, které projdou krokem 1 | mechanicky, hlasy |
| 3 | tematická diverzita — nejvýše hlasovaná otázka z témat, která se do desítky nedostala (max 3 otázky na téma v celé patnáctce) | model dle klíče |
| 2 | wildcard — málo hlasů, vysoká konkrétnost a doložitelnost | rozhodující moderátor, **viditelně označené** |

## Krok 3 — hodnoticí signály

Zvyšuje pořadí: ptá se na konkrétní doložitelné rozhodnutí / hlasování / smlouvu / číslo · odpověditelné v jednom komentáři · brněnská relevance · tvrzení v otázce je doložené odkazem.

Snižuje pořadí: příliš obecné · už zodpovězeno jinou otázkou v patnáctce.

**Explicitně NESNIŽUJE pořadí to, že je otázka nepříjemná, konfrontační nebo pro hosta trapná.** Tahle věta musí být doslova i v promptu — model má vestavěnou tendenci k uhlazování.

## Krok 4 — kontrolní výstup

Ke každé patnáctce se zveřejní: rozdělení slotů (10/3/2), témata a jejich zastoupení, podíl otázek s doloženým tvrzením, počet sloučených duplicit, wildcardy a jejich odůvodnění, **počet lidských odchylek od výstupu modelu**, shoda se stínovým během, jmenovitě rozhodující moderátor.

## Otevřené otázky

- [ ] Uzavřený seznam témat (doprava, bydlení, rozpočet, územní plán, školství, sociální, kultura, bezpečnost, životní prostředí, správa a transparentnost, ostatní?)
- [ ] Rozhodnutí sporu: platí strop „max 3 na téma" i na desítku podle hlasů, nebo jen na sloty 11–15?
- [ ] Pravidlo pro shodu hlasů na 10./11. místě (návrh: dřívější čas)
- [ ] Chování při méně než 15 způsobilých otázkách
