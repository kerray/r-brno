# runs/ — logy jednotlivých běhů

Prázdné, dokud neproběhne první AMA.

Adresář zapisuje a commituje **skript, který kuraci pouští** — ne člověk. Když je publikování logu
ruční krok navíc, přestane se do třetího AMA dělat a nikdo si toho nevšimne dřív než při první
stížnosti.

## Tvar jednoho běhu

```
runs/RRRR-MM-DD-subjekt/
  meta.json          # model id (claude-sonnet-5), tag promptu, hash, čas,
                     # kdo rozhodoval, kumulativní náklad API
  input.json         # přesný vstup po zaslepení ([HOST]/[SUBJEKT]) + id komentářů
  output.json        # rozhodující běh: pořadí + u KAŽDÉ otázky pole `reason`
  shadow.json        # stínový běh (bez pravomoci, jen měření)
  agreement.md       # shoda mezi během a stínem, generováno
  decisions.md       # každý lidský zásah do výstupu modelu + odůvodnění
  final.md           # patnáctka tak, jak odešla hostovi
```

## Nejdůležitější soubor je `decisions.md`

Ne výstup modelu — **odchylky od něj**. Tam je skutečná moc: model navrhuje, člověk rozhoduje,
a jediné místo, kde se to může tiše zvrtnout, je nezaznamenaný přepis. Proto jde počet odchylek
do shrnutí jako **titulkové číslo**.

Když je log nudný, je to dobrá zpráva. Když je nudný *podezřele* — nula odchylek napříč všemi
subjekty — taky to o něčem vypovídá a je lepší, když si toho všimneme my.

## Náklad

`meta.json` vede kumulativní náklad na API a průběžný součet se zveřejňuje. Limit výdajů
neregistrované třetí osoby je **3 000 Kč a týká se i výdajů**, nejen odměn — vlastní útrata
za model se do něj počítá.
