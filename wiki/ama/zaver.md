# AMA série 2026 — ohlédnutí

*Tato stránka je generovaná z [github.com/kerray/r-brno](https://github.com/kerray/r-brno) — změny se dělají tam, přes pull request.*

Před komunálními volbami 9.–10. 10. 2026 proběhlo na r/Brno pět AMA s uskupeními kandidujícími do Zastupitelstva města Brna. Tahle stránka není shrnutí odpovědí — ta jsou u jednotlivých AMA níže. Je to ohlédnutí za tím, jak jsme sérii dělali my: co jsme si naplánovali, co z toho opravdu běželo a kde jsme vlastní pravidla nedodrželi.

Neříká nic o tom, kdo odpověděl lépe. To si přečtěte sami.

## Pět AMA

| Datum | Uskupení | Hostů | Otázek ze sběru | Zodpovězeno z povinných | Shrnutí |
|---|---|---|---|---|---|
| 2. 9. (pilot) | Zelené Brno | 3 | 14 | 14 / 14 | [2026-09-02-zelene-brno](/r/Brno/wiki/ama/2026-09-02-zelene-brno) |
| 18. 9. | Nové Brno | 3 | 13 | 13 / 13 | [2026-09-18-nove-brno](/r/Brno/wiki/ama/2026-09-18-nove-brno) |
| 24. 9. | Přísaha | 3 | 3 | 3 / 3 | [2026-09-24-prisaha](/r/Brno/wiki/ama/2026-09-24-prisaha) |
| 30. 9. | Tu! Piráti a Fakt Brno | 3 | 2 | 2 / 2 | [2026-09-30-pirati](/r/Brno/wiki/ama/2026-09-30-pirati) |
| 6. 10. | Za lužánky | 2 | 6 | 6 / 6 | [2026-10-06-za-luzanky](/r/Brno/wiki/ama/2026-10-06-za-luzanky) |
| **celkem** | | **14** | **38** | **38 / 38** | |

Pořadí je chronologické. Kdo se přihlásil, kdo ne a kdy, je v [rozcestníku](/r/Brno/wiki/ama/index). Co se ve kterém vlákně stalo nad rámec čísel — včetně otázek čtenářů položených přímo ve vlákně, které už povinné nebyly — je v jednotlivých shrnutích.

## Pravidla, která jsme si napsali

Šest týdnů před volbami je každá akce s politiky součástí kampaně. Naší obranou měla být symetrie a přepočitatelnost, a tak jsme ji vybudovali důkladně. Možná až příliš.

V [pozvánce](/r/Brno/wiki/ama/pozvanka) a na stránce [moderace](/r/Brno/wiki/ama/moderace) stojí mimo jiné:

- sběrné vlákno **4 dny** předem, uzávěrka sběru **48 h** předem, povinná sada **24 h** předem,
- **15 povinných otázek**, rozdělených **10 podle hlasů / 3 vybere jazykový model / 2 wildcardy moderátora**, wildcardy viditelně označené,
- prompt pro model **zmrazený na gitovém tagu** ve chvíli otevření sběru, k tomu **stínový běh** bez pravomoci, jen aby šlo změřit, jak je jeden běh nahodilý,
- **contest mode** ve sběrném vlákně a jeho vypnutí při výběru, aby šlo skóre zkontrolovat,
- **veřejné losování** termínů skriptem, jehož zdrojem náhody je kurz ČNB EUR/CZK,
- vyjádření těch, kdo pozvání odmítnou, otištěné doslova, **nejvýše 500 znaků bez odkazů**,
- jména a účty hostů **72 h předem**, garant, ověření z oficiálního kanálu uskupení,
- selektivní uzavření vlákna po oknu na doplnění, s předem zveřejněným zněním důvodu (makro U1),
- snapshot sběrného vlákna při uzávěrce, aby si výběr mohl kdokoli přepočítat.

## Co se z toho opravdu použilo

**Výběr otázek nikdy.** Patnáct otázek se nesešlo ani jednou — nejvíc jich bylo v pilotu (14), pak 13, 3, 2 a 6. Pro tenhle případ měl [klíč pro výběr](https://github.com/kerray/r-brno/blob/main/rules/curation-key.md) předem sepsané pravidlo: patnáctka se uměle nedoplňuje a povinná je každá způsobilá otázka. Takže:

| | |
|---|---|
| Běhů kurace jazykovým modelem | **0** z 5 |
| Náklad na kuraci | **0 Kč** |
| Použitých wildcardů moderátora | **0** |
| Slotové rozdělení 10 / 3 / 2 | **ani jednou uplatněno** |
| Otázek ze sběru přenesených do AMA vlákna | **38 z 38** |

Výsledná moc nad tím, na co hosté povinně odpovídali, tedy připadla ze sta procent čtenářům. S tím se dá žít.

Zmrazený prompt ale neležel ladem zbytečně: zamrzal a tagoval se tak jako tak, protože dopředu nikdo neví, kolik otázek přijde.

## Kde jsme vlastní pravidla nedodrželi

Všechno níže je podrobně, s časy, v sekcích „Přiznané odchylky" jednotlivých shrnutí. Tady jen přehled:

- **Termíny sběru se posouvaly.** V pilotu trval sběr zhruba 32 hodin místo čtyř dnů a povinná sada vyšla 13 hodin předem místo 24. Ani ve čtyřech dalších AMA jsme slíbené „48 h / 24 h předem" nedodrželi — nejtěsněji vyšly otázky deset minut před startem, nejvíc jsme se s uzávěrkou sběru opozdili asi o 23 hodin.
- **V pilotu náš vlastní AutoModerator zadržel garantce všech 12 komentářů**, protože měla dva dny starý účet. Pouštěl je ručně člověk, nejdéle po 8 minutách. Napsali jsme si to varování dopředu do vlastní dokumentace a stejně jsme AMA vlákna z pravidla nevyňali. Od druhého AMA je vyňatá.
- **V jednom sběrném vlákně jsme při výběru zapomněli vypnout contest mode**, takže skóre nešlo v tu chvíli zkontrolovat. Vypnul ho bot až o tři dny později.
- **Jednou se vlákno na dvě minuty „zavřelo" o den dřív**, než mělo — záhlaví hlásilo konec nových otázek a běžel uzavírací běh. Nic nesmazal; po dvou minutách opraveno.
- **Ve dvou AMA se nevytvořil tag zmrazeného promptu** a jednou se nepořídil snímek sběru při uzávěrce. Prompt se tehdy nepoužil, ale slib je slib.
- **V pilotu jsme slíbili zaznamenat původní znění editovaných odpovědí** — a neměli jsme k tomu mechanismus. Slib jsme veřejně zúžili na to, co splnit jde.
- **Slib „v AMA vláknech automatické filtry neběží"** jsme splnili jen napůl. Náš AutoModerator neběžel; Redditův vlastní spam filtr vypnout neumíme (viz níže).

## Kdo to celé odtáhl

**ponocny_bot** — tedy kerrayovy skripty na Windmillu a kerrayova režie. Lidský moderátor je na r/Brno jeden, takže bez automatizace by série neproběhla.

Bot v průběhu série:

- **zakládal sběrná i AMA vlákna**, připínal je, zamykal a na start živého okna odemykal s přesností na pár sekund,
- **přenášel otázky** ze sběrného vlákna do AMA vlákna, v pořadí podle hlasů při uzávěrce,
- **přidával hosty** mezi schválené uživatele a **dával jim flair** `AMA host — …`,
- v živém okně **každých 30 sekund kontroloval frontu moderace** a pouštěl, co tam uvízlo,
- **zavíral vlákna**: po oknu na doplnění selektivně (nové otázky ne, odpovědi uvnitř větví ano), se shrnutím natvrdo,
- pořizoval **snímky vláken**, ze kterých vznikala shrnutí.

Hlídání fronty se ukázalo jako nejdůležitější práce celé série. **Redditův spam filtr zadržel v posledních třech AMA všech 25 komentářů hostů** (5 + 9 + 11). Proč, Reddit neuvádí. V živém okně je bot pouštěl za 3 až 32 sekund. Když nehlídal — mimo živé okno — jedna odpověď čekala na schválení 55 minut a dvě další 13 hodin, a do první verze shrnutí se proto nedostaly; doplnili jsme je dodatkem.

**Shrnutí** psal jazykový model podle veřejného [klíče pro shrnutí](https://github.com/kerray/r-brno/blob/main/rules/summary-key.md). Shrnutí procházela nezávislou recenzí a citace v nich kontroloval [skript](https://github.com/kerray/r-brno/blob/main/tools/overit_citace.py) znak po znaku proti snímku vlákna — u každého AMA s výsledkem, že všechny citace sedí slovo od slova. Ten skript si může pustit kdokoli.

Zdrojový kód bota veřejný není (proč, je na stránce [moderace](/r/Brno/wiki/ama/moderace)). Veřejné jsou prompty, klíče, konfigurace a logy běhů v [`runs/`](https://github.com/kerray/r-brno/tree/main/runs).

## Moderační čísla za celou sérii

| | |
|---|---|
| Odstraněno kategorie A / B / C | **0 / 0 / 0** |
| Odvolání | **0** |
| Falešné „AMA host" flairy | **0** |
| Komentářů odstraněných po uzavření vlákna | **0** |

*(Čísla z moderačních statistik jednotlivých shrnutí a z moderačního logu; shrnutí Nového Brna moderační statistiky neobsahuje, u Tu! Pirátů jsou falešné flairy „nezaznamenané" — stav flairů ve vlákně tehdy nešel ze snímku ověřit.)*

## Dotaz na úřad

Ještě před prvním AMA jsme se písemně zeptali Úřadu pro dohled nad hospodařením politických stran a politických hnutí, jestli formát spadá pod zákon o volebních kampaních. Úřad odpověděl 17. 9. 2026: pořadatelům diskusí v souvislosti s komunálními volbami registrační povinnost třetí osoby nevzniká. Celé znění dotazu i odpovědi je na [dotaz-udhpsh](/r/Brno/wiki/ama/dotaz-udhpsh).

## Děkujeme

- **Všem uskupením, která přišla, a jejich hostům** — za čas, odpovědi a trpělivost s naší byrokracií i s Redditem, který jim komentáře schovával.
- **Všem, kdo se ptali, hlasovali, doptávali se a četli.** Bez otázek by to byla jen pětice prázdných vláken s přesným časováním.
- **Úřadu pro dohled nad hospodařením politických stran a politických hnutí** za věcnou odpověď ještě v průběhu série.

## Co bychom příště udělali jinak

Návrhy, ne sliby — připomínky vítáme v [repozitáři](https://github.com/kerray/r-brno) nebo modmailem:

- pravidla pro výběr ponechat, ale počítat s tím, že se obvykle nepoužijí — a podle toho zjednodušit, co se slibuje dopředu,
- hlídat frontu i mimo živé okno, aspoň do konce okna na doplnění,
- termíny sběru navázat na potvrzení termínu automaticky, ne ručně.

## Souvisí

- [/r/Brno/wiki/ama/index](/r/Brno/wiki/ama/index) — rozcestník série
- [/r/Brno/wiki/ama/pozvanka](/r/Brno/wiki/ama/pozvanka) — pravidla, jak je dostali hosté
- [/r/Brno/wiki/ama/moderace](/r/Brno/wiki/ama/moderace) — jak jsme moderovali
- [/r/Brno/wiki/ama/jak-se-ptat](/r/Brno/wiki/ama/jak-se-ptat) — jak se ptát
- [/r/Brno/wiki/ama/stret-zajmu](/r/Brno/wiki/ama/stret-zajmu) — prohlášení o střetu zájmů
- [/r/Brno/wiki/ama/dotaz-udhpsh](/r/Brno/wiki/ama/dotaz-udhpsh) — dotaz na ÚDHPSH a odpověď
