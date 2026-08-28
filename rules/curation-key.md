# Psaný klíč pro kuraci povinných 15 otázek

> **STATUS: k připomínkám.** Zveřejněno **před** rozesláním pozvánek, aby byl čas na námitky.
> Pro konkrétní AMA začíná platit ve chvíli, kdy se otevře sběrné vlákno — tehdy se klíč
> i prompt zamrznou a otagují `ama-RRRR-MM-DD-subjekt`.
>
> Prompt `prompts/curation-top15.md` se odvozuje **z tohoto klíče**, ne obráceně — smyslem je mít
> lidsky čitelnou verzi, kterou lze citovat. Když se klíč a prompt rozejdou, platí klíč a prompt se opravuje.

## Krok 0 — vstup

Kuraci předchází **zaslepení**: ve vstupu se jméno hosta nahradí `[HOST]` a jméno uskupení `[SUBJEKT]`.
Nezaslepí to úplně (téma otázky často prozradí, o koho jde), ale sundá to nejsilnější triggery.

Vstupem je **celé sběrné vlákno najednou**, ne po dávkách. Kdyby se dávkovalo, pořadí by záviselo na tom,
ve které dávce otázka skončila.

## Krok 1 — co se do výběru nedostane

- Není to otázka (samotné tvrzení, komentář, vtip). Zůstává ve vlákně.
- Duplicita → sloučí se s původní. **Skóre shluku = max(skóre), NIKDY součet** — sčítání by z počtu účtů
  udělalo násobič hlasů. Členy shluku i jejich jednotlivá skóre zveřejňujeme.
- Osobní útok / doxx (už zachyceno moderací).
- Komentář, který se pokouší oslovit model instrukcí („ignoruj předchozí zadání…"). **Neposlechne se ani
  nemaže** — vyřadí se z výběru a jde do samostatné kolonky ve statistikách.

**Vědomě NEfiltrujeme** otázky „mimo kompetenci města" — je to klasická úniková odpověď a rozhodovat
o kompetenci za hosta není naše práce.

## Krok 2 — složení patnáctky

| Sloty | Klíč | Kdo vybírá |
|---|---|---|
| 10 | nejvýše hlasované otázky, které projdou krokem 1 | mechanicky, hlasy |
| 3 | tematická diverzita — nejvýše hlasovaná otázka z témat, která se do desítky nedostala | model dle klíče |
| 2 | wildcard — málo hlasů, vysoká konkrétnost a doložitelnost | rozhodující moderátor, **viditelně označené** |

**Rozdělení moci nad výběrem: hlasování 10, model 3, jmenovaný člověk 2.**

### Pravidla, která z toho plynou

- **Desítka je nedotknutelná.** Strop „max 3 otázky na jedno téma" se **neuplatňuje na desítku podle hlasů** —
  jinak by model nebo moderátor přebíjeli hlasování. Strop je omezením pro sloty 11–13: diverzitní slot
  nesmí dostat téma, které už má v patnáctce tři otázky.
- **Diverzitní slot dostane vždy nejvýše hlasovanou otázku z daného tématu**, ne „nejlepší" otázku podle
  úsudku modelu. Model rozhoduje o tom, *které téma* chybí, ne o tom, *která otázka* téma zastoupí.
- **Wildcard nesmí být otázka, která by prošla podle hlasů.** Slot má smysl jen pro otázky, které by jinak
  zapadly. Ke každému wildcardu se zveřejní jednou větou důvod.
- **Shoda skóre na hranici (10./11. místo, i uvnitř tématu): rozhoduje dřívější čas komentáře.**
  Je to deterministické a každý si to přepočítá. Když je totožný i čas, rozhoduje nižší `id` komentáře.

### Uzavřený seznam témat

Model přiřadí každé otázce **právě jedno hlavní téma** z tohoto seznamu. Seznam je uzavřený schválně —
volný výběr témat by z „tematické diverzity" udělal nekontrolovatelnou páku.

`doprava` · `bydlení` · `rozpočet a majetek města` · `územní plán a výstavba` · `školství` ·
`sociální a zdravotní` · `kultura a sport` · `bezpečnost` · `životní prostředí` ·
`správa, transparentnost a úřad` · `ostatní`

`ostatní` **nemůže dostat diverzitní slot** — jinak by se jím dal odůvodnit jakýkoli výběr.
Když se do `ostatní` dostane víc než pětina otázek, je to signál, že seznam témat je špatný;
opraví se **mezi AMA**, ne během něj, a se zápisem v `CHANGELOG.md`.

### Když je způsobilých otázek méně než 15

Patnáctka se **nedoplňuje uměle**. Do povinné sady jde všech N způsobilých otázek a v kontrolním výstupu
se uvede „povinných otázek: N (méně než 15, ve sběrném vlákně jich víc nebylo)".
Slotové rozdělení se v takovém případě neuplatňuje a **wildcardy se nepoužijí** — nemá smysl vytahovat
přehlédnutou otázku, když se nic nepřehlédlo.

## Krok 3 — hodnoticí signály

Zvyšuje pořadí: ptá se na konkrétní doložitelné rozhodnutí / hlasování / smlouvu / číslo · odpověditelné
v jednom komentáři · brněnská relevance · tvrzení v otázce je doložené odkazem.

Snižuje pořadí: příliš obecné · už zodpovězeno jinou otázkou v patnáctce.

**Explicitně NESNIŽUJE pořadí to, že je otázka nepříjemná, konfrontační nebo pro hosta trapná.** Tahle věta
musí být doslova i v promptu — model má vestavěnou tendenci k uhlazování.

Otázka s vloženým tvrzením se **nevyřazuje**. Do patnáctky jde v přeformulované podobě
(„je pravda, že X?" + „pokud ano, proč?"), **s poznámkou, že jde o redakční úpravu, a s odkazem na původní
znění**, které zůstává ve vlákně viditelné. Vzory a modelové dvojice: [`wiki/ama/jak-se-ptat.md`](../wiki/ama/jak-se-ptat.md).

## Krok 4 — kontrolní výstup

Ke každé patnáctce se zveřejní: rozdělení slotů (10/3/2), témata a jejich zastoupení, podíl otázek
s doloženým tvrzením, počet sloučených duplicit i s členy shluků, počet vyřazených pokusů o instrukci
modelu, wildcardy a jejich odůvodnění, **počet lidských odchylek od výstupu modelu**, shoda se stínovým
během, jmenovitě rozhodující moderátor. Plus srovnání se všemi předchozími subjekty.

## Co tenhle klíč nepokrývá

- **Nezaručuje stabilitu.** Kurace je jeden běh jazykového modelu; druhý běh nemusí dát totožné pořadí.
  Proto se zveřejňuje vstup, prompt i model id — přepočítat si to může kdokoli.
- **Netvrdí nestrannost.** Tvrdí konzistenci: na všechny subjekty jde stejný postup, stejný prompt,
  stejná verze modelu.
