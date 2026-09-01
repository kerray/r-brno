# runs/ — logy jednotlivých běhů

Už prázdné není. První běh je [`2026-09-02-zelene-brno/`](2026-09-02-zelene-brno) — pilotní AMA
se Zeleným Brnem. Soubory kurace v něm chybí schválně: otázek přišlo míň než slotů, takže se
nevybíralo a model se vůbec nepustil.

Adresář zapisuje a commituje **skript, který kuraci pouští** — ne člověk. Když je publikování logu
ruční krok navíc, přestane se do třetího AMA dělat a nikdo si toho nevšimne dřív než při první
stížnosti.

## Jeden běh = jedna složka

Složka se jmenuje **`RRRR-MM-DD-subjekt`**: datum konání AMA a slug uskupení. Je to schválně tentýž
tvar, jakým se taguje zamrzlý prompt (`ama-RRRR-MM-DD-subjekt`), takže log, prompt i vlákno jdou
spárovat bez dohadování.

```
runs/RRRR-MM-DD-subjekt/
  snapshot.json      # syrový sběr z Reddit API po uzávěrce
  snapshot.md        # tentýž snapshot čitelně, tabulkou
  meta.json          # model id (claude-sonnet-5), tag promptu, hash, čas,
                     # kdo rozhodoval, kumulativní náklad API
  input.json         # přesný vstup po zaslepení ([HOST]/[SUBJEKT]) + id komentářů
  output.json        # rozhodující běh kurace: pořadí + u KAŽDÉ otázky pole `reason`
  shadow.json        # stínový běh (bez pravomoci, jen měření)
  agreement.md       # shoda mezi během a stínem, generováno
  decisions.md       # každý lidský zásah do výstupu modelu + odůvodnění
  final.md           # patnáctka tak, jak odešla hostovi
  summary.md         # transparenční čísla po skončení AMA
```

Soubory přibývají postupně, jak běh postupuje — složka s jedním snapshotem je legitimní stav
(znamená „sběr skončil, kurace ještě neproběhla"), ne rozdělaná práce.

A některé soubory v konkrétním běhu **nevzniknou vůbec**. Když je způsobilých otázek méně než 15,
klíč výběr neuplatňuje a model se nepouští — pak `input.json`, `output.json`, `shadow.json`
a `agreement.md` nemají obsah, který by dávaly, a chybí právem. Co se nekonalo a proč, patří
do `decisions.md`; `meta.json` to nese strojově čitelně (`model_invoked: false` a seznam
nevzniklých souborů). **Prázdné soubory na oko se nezakládají** — zmizel by rozdíl mezi
„neproběhlo" a „proběhlo a nic nevyšlo".

| Soubor | Vzniká | Co v něm je |
|---|---|---|
| `snapshot.json` | po uzávěrce sběru | syrová data z Reddit API: každý komentář sběrného vlákna i s `id`, `score`, `author`, `created_utc`, `permalink` a rodičovským postem |
| `snapshot.md` | tamtéž, generováno ze `snapshot.json` | čitelná tabulka otázek podle skóre + počty otázek na autora; verze pro lidi, ne pro stroj |
| `meta.json` | při běhu kurace | model id, tag a hash promptu, čas, jmenovitě rozhodující moderátor, kumulativní náklad API |
| `input.json` | při běhu kurace | to, co model doopravdy dostal — po zaslepení `[HOST]` / `[SUBJEKT]`, s id komentářů |
| `output.json` | při běhu kurace | rozhodující výstup: pořadí, přiřazené téma a **u každé otázky `reason`**; jméno souboru je pevné, odkazuje se na něj [`prompts/curation-top15.md`](../prompts/curation-top15.md) |
| `shadow.json` | při běhu kurace | stínový běh bez pravomoci; existuje jen proto, aby šlo změřit, jak moc je jeden běh nahodilý |
| `agreement.md` | generováno | shoda rozhodujícího běhu se stínovým |
| `decisions.md` | ručně, hned po zásahu | každá lidská odchylka od výstupu modelu i s odůvodněním |
| `final.md` | po uzavření výběru | povinná sada tak, jak odešla hostovi |
| `summary.md` | po skončení AMA | čísla podle [`wiki/ama/moderace.md`](../wiki/ama/moderace.md) — zachycené, odstraněné, opravy, odvolání, rozpad zodpovězeno / odmítnuta premisa / bez odpovědi |

## Snapshot se pořizuje po uzávěrce sběru

Snapshot je **fotka sběrného vlákna ve chvíli, kdy se zavřelo**, a pořizuje se **před** tím, než se
na vstup pustí model. Je to ten podklad, o kterém mluví wiki: nestačí, že si výběr můžete přečíst —
podstatné je, že si ho **můžete přepočítat**. Kdo má snapshot, prompt a model id, spustí si kuraci
sám a porovná pořadí s naším. Bez snapshotu je zveřejněný prompt na nic, protože by chyběl vstup.

Proto se do snapshotu nesahá. Když se vlákno po uzávěrce ještě pohne (dodatečné hlasy, smazaný
komentář), snapshot zůstává tak, jak byl pořízen — a rozdíl patří do `decisions.md`, ne do přepisu
historie.

## Nejdůležitější soubor je `decisions.md`

Ne výstup modelu — **odchylky od něj**. Tam je skutečná moc: model navrhuje, člověk rozhoduje,
a jediné místo, kde se to může tiše zvrtnout, je nezaznamenaný přepis. Proto jde počet odchylek
do shrnutí jako **titulkové číslo**.

Když je log nudný, je to dobrá zpráva. Když je nudný *podezřele* — nula odchylek napříč všemi
subjekty — taky to o něčem vypovídá a je lepší, když si toho všimneme my.

## Co se ověřilo na prvním běhu

**Contest mode skóre moderátorovi neskrývá.** Ve sběrném vlákně běžel contest mode (náhodné pořadí,
skryté skóre), ale ve snapshotu má **každý** komentář `score_hidden: false` a skutečné skóre.
Snapshot jde tedy pořídit **ještě před vypnutím contest módu** — kvůli logu se nemusí nastavení
vlákna měnit dřív, než je potřeba. Pro čtenáře vlákna zůstává skóre skryté; my ho vidíme, protože
jsme moderátoři, a proto ho rovnou zveřejňujeme ve `snapshot.md`.

**U pilotu se výběr vůbec nekonal.** Ve vlákně bylo **14 otázek od 10 účtů**, tedy **méně než
15 povinných slotů**. Klíč na tenhle případ pamatuje ([`rules/curation-key.md`](../rules/curation-key.md),
oddíl „Když je způsobilých otázek méně než 15"): patnáctka se uměle nedoplňuje, do povinné sady jde
všech N způsobilých otázek a slotové rozdělení 10/3/2 se neuplatní. Takže: **všech 14 otázek je
povinných a moderátor nepoužil ani jeden z obou wildcard slotů.** Nemá smysl vytahovat přehlédnutou
otázku, když se nic nepřehlédlo.

Je to odchylka od playbooku, ale **směrem k menší moci moderátora**, ne větší — a je přiznaná
i přímo ve vlákně, ne jen tady. Zaznamenáváme ji proto, že první běh, ve kterém se nevybíralo,
neříká o kuraci nic; nic si z něj o kvalitě klíče nevyvozujte.

## Náklad

`meta.json` vede kumulativní náklad na API a průběžný součet se zveřejňuje. Limit výdajů
neregistrované třetí osoby je **3 000 Kč a týká se i výdajů**, nejen odměn — vlastní útrata
za model se do něj počítá.
