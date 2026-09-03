# Psaný klíč pro shrnutí AMA

> **STATUS: k připomínkám.** Sepsáno po pilotu 2026-09-02, kdy se ukázalo, že pravidlo výběru
> reakcí žilo jen v promptu a nikde jinde.
> Pro konkrétní AMA začíná platit ve chvíli, kdy se otevře sběrné vlákno — tehdy se klíč
> i prompt zamrznou a otagují `ama-RRRR-MM-DD-subjekt`.
>
> Prompt `prompts/summary.md` se odvozuje **z tohoto klíče**, ne obráceně — smyslem je mít
> lidsky čitelnou verzi, kterou lze citovat. Když se klíč a prompt rozejdou, platí klíč a prompt
> se opravuje.

Shrnutí je **dokumentační záruka, ne recenze**: *nemůžeme slíbit dobré odpovědi, můžeme slíbit,
že bude vidět, jaké odpovědi jste dostali.* Vychází **do 48 h** po skončení okna na doplnění,
na wiki (`/r/Brno/wiki/ama/RRRR-MM-DD-subjekt`), ne do postu.

Renderuje ho **skript**, ne model — aby měla každá stránka totožný tvar a šla porovnávat mezi
subjekty. Model plní strukturovaný výstup; sazbu nedělá.

## Krok 1 — co shrnutí obsahuje a v jakém pořadí

Pořadí je závazné. Je to jediné, co drží srovnatelnost napříč subjekty.

| # | Sekce | Co v ní je |
|---|---|---|
| 1 | hlavička | časy živého okna a okna na doplnění, model id, tag zamrzlého promptu |
| 2 | **Odpovídali** | účet, jméno, role, kdo byl garant |
| 3 | **Čísla** | rozpad kategorií: zodpovězeno v okně / doplněno / odmítnuta premisa / bez odpovědi |
| 4 | **Nezodpovězené otázky** | **vypsané jako první, ne schované na konci** |
| 5 | **Otázky a odpovědi** | otázka → odpověď hosta **doslovně** → výrazné reakce |
| 6 | **Moderační statistiky** | viz krok 4 |
| 7 | **Kurace** | model id, tag promptu, sloty, wildcardy a jejich odůvodnění, lidské odchylky, shoda se stínem, rozhodující moderátor jmenovitě, odkaz do `runs/` |

**Nezodpovězené jdou před zodpovězené schválně.** Kdyby byly na konci, dalo by se shrnutí
přečíst jako výčet úspěchů a chybějící odpovědi by zapadly.

**Odpovědi hosta se nezkracují ani neparafrázují.** Ani když jsou dlouhé, ani když míjejí otázku.
Že odpověď míjí otázku, se **nekomentuje** — čtenář má vedle sebe otázku i odpověď.

## Krok 2 — výběr výrazných reakcí

**Platí od druhého AMA v sérii.** Pilot 2026-09-02 se dokončuje podle verze zamrzlé na svém
tagu (viz „Změny uprostřed série" níže).

- do shrnutí jde **pět nejvýše hlasovaných reakcí** na odpověď hosta, se skóre **alespoň 2**,
- **shoda skóre: rozhoduje dřívější čas komentáře**,
- vyhovuje-li jich **míň než pět, uvede se kolik** („zobrazeny 3 reakce"),
- vyhovuje-li jich **víc, uřízne se na pět a přizná se to** („zobrazeno 5 z 9"),
- **nevybírají se podle obsahu** ani podle toho, jestli jsou k hostovi vlídné.

**Proč pevný počet, a ne bodový práh.** Do 2026-09-02 tu stál absolutní práh (≥ 50 % skóre
nejlepší reakce **a zároveň** ≥ 10 bodů). Data z pilotu ukázala, že je nedosažitelný: nejvýše
hlasovaná *otázka* měla 9 bodů. Práh by nevybral nic a shrnutí by vycházela prázdná; jediná
oprava by byla práh v polovině série snížit, což je **nejtišší možný způsob, jak shrnutí
vychýlit**. Pevný počet **nemá co driftovat**, je **srovnatelný napříč subjekty** (u AMA s devíti
body i se čtyřiceti dostanete pět reakcí) a **nedá se doladit**, až bude vidět, jak odpovědi
dopadly. Minimum 2 body je jen pojistka proti komentáři, kterého si nikdo nevšiml.

## Krok 3 — kategorie odpovědí

Přísně mechanické, **žádné hodnocení kvality**:

| Kategorie | Kdy |
|---|---|
| `v_okne` | host odpověděl během živého okna |
| `doplneno` | host odpověděl až v okně na doplnění (+24 h) — uvádí se čas |
| `odmitnuta_premisa` | host **výslovně řekl, které tvrzení v otázce odmítá a proč** |
| `bez_odpovedi` | žádná reakce hosta na tuhle otázku |

Rozhoduje **čas a obsah, ne kvalita**. Vyhýbavá, ale existující odpověď je `v_okne`,
ne `bez_odpovedi`.

**`odmitnuta_premisa` není hodnocení, jestli je odmítnutí oprávněné.** To neposuzujeme —
plyne to z pozvánky (§7) i z [`wiki/ama/jak-se-ptat.md`](../wiki/ama/jak-se-ptat.md). Host má
právo premisu odmítnout místo odpovědi; podmínkou je, že řekne **kterou a proč**. Když u 9 z 15
otázek odmítne premisu, obrázek si udělá čtenář sám a shrnutí to nekomentuje.

> ⚠ **OTEVŘENÉ — není nikde rozhodnuto, nedoplňovat bez rozhodnutí.**
> Kdo a jak kategorii `odmitnuta_premisa` přiděluje: navrhuje ji model a potvrzuje člověk, nebo
> je čistě mechanická? Musí host použít nějaké výslovné označení, nebo se pozná z textu? Co
> když premisu odmítne **a zároveň odpoví**? A co když jen napíše „to není pravda", aniž řekne
> kterou premisu odmítá — je to `odmitnuta_premisa`, nebo `v_okne`?

## Krok 4 — co se uvádí povinně, i když je to nepříjemné

Tohle je jádro celého klíče. Čísla, která se špatně vysvětlují, se uvádějí **taky**, jinak by
shrnutí bylo reklamou.

- **moderační zásahy**: počet komentářů, zachycených, skutečně odstraněných **po kategoriích
  (A/B/C)**, oprav dle B, nabídnutých a přijatých přeformulování dle D, zamčených větví
  **i s důvodem**, odvolání a jejich výsledek,
- **zásahy AutoModeratoru se počítají taky** — filtrace kvůli stáří účtu, karmě nebo doméně je
  moderační zásah jako každý jiný, i když ho neudělal člověk (u pilotu jich bylo přes dvanáct
  a nespočítaly se nikde),
- **počet komentářů odstraněných po uzavření vlákna** (nové otázky napsané po termínu — viz
  [`wiki/ama/moderace.md`](../wiki/ama/moderace.md)),
- **počet lidských odchylek od návrhu modelu** — a je to **titulkové číslo**, ne poznámka pod
  čarou. Tam je skutečná moc: model navrhuje, člověk rozhoduje, a jediné místo, kde se to může
  tiše zvrtnout, je nezaznamenaný přepis,
- **přiznané odchylky od playbooku**: kde se běh odchýlil od vlastních pravidel, i když ku
  prospěchu hosta nebo čtenářů. Odchylka směrem k menší moci moderátora se uvádí stejně jako
  opačná,
- odkaz do `runs/RRRR-MM-DD-subjekt/`, kde je vstup, výstup a `decisions.md`.

Když je log nudný, je to dobrá zpráva. Když je nudný *podezřele* — nula odchylek napříč všemi
subjekty — je to taky informace.

## Krok 5 — co se do shrnutí nedostane

- **hodnocení, jestli host odpověděl dobře**, a jakýkoli názor na politické postoje kohokoli,
- **obsah smazaných komentářů běžných uživatelů** — jen fakt, že reakce byla smazána, a její
  skóre. U hostů je to jinak: jejich pozdější úprava nebo smazání se ve shrnutí uvádí, protože
  jednají ve veřejné politické roli,
- **obnovené znění obsahu odstraněného kvůli osobním údajům** — žádné screenshoty ani přepisy;
  do logu jde jen permalink, čas a report ID. Shrnutí nesmí být cestou, jak si přečíst to, co
  jsme odstranili právě proto, aby to nikdo nečetl,
- obsah komentářů odstraněných v kategorii A obecně.

## Změny uprostřed série

Klíč **zamrzá spolu s promptem** ve chvíli otevření sběrného vlákna a otaguje se
`ama-RRRR-MM-DD-subjekt`. Od té chvíle se pro dané AMA nemění.

**Změna pravidla poté, co jsou vidět výsledky, je odchylka** — patří do
`runs/RRRR-MM-DD-subjekt/decisions.md` s odůvodněním, a nová verze platí **od dalšího AMA**, ne
zpětně. Přesně to se stalo s prahem pro výrazné reakce; viz
[`runs/2026-09-02-zelene-brno/decisions.md`](../runs/2026-09-02-zelene-brno/decisions.md),
Rozhodnutí 3.

## Co tenhle klíč nepokrývá

- **Nezaručuje stabilitu.** Shrnutí je jeden běh jazykového modelu; druhý běh nemusí dát
  totožné formulace. Proto se zveřejňuje vstup, prompt i model id.
- **Netvrdí nestrannost.** Tvrdí konzistenci: na všechny subjekty jde stejný postup, stejný
  prompt, stejná verze modelu.
- **Neřeší otázky, které jsou v textu označené jako OTEVŘENÉ.** Dokud se o nich nerozhodne,
  nejsou pravidlem — a nikdo je nemá vyplňovat úsudkem za běhu.

## Otevřené otázky — soupis

Nejsou to pravidla. Jsou to místa, kde zatím nic rozhodnuto není, a **do rozhodnutí se nemají
vyplňovat úsudkem**.

| # | Co je otevřené | Kde to chybí |
|---|---|---|
| 1 | mechanika `odmitnuta_premisa` — kdo ji přiděluje, podle čeho, co při současné odpovědi | krok 3 |
| 2 | **co se počítá jako „reakce"** — jen přímé odpovědi na komentář hosta, nebo celé podvlákno pod ním? | krok 2 |
| 3 | **reakce na doplněné odpovědi** (okno +24 h) — vybírají se stejně jako u odpovědí v živém okně? | krok 2 |
| 4 | **odkud se berou AutoModí zásahy** do statistik a jak se odliší od zásahů bota a člověka | krok 4 |
| 5 | **pořadí otázek** v sekci „Otázky a odpovědi" — pořadí zveřejněné patnáctky, nebo podle skóre? | krok 1 |
