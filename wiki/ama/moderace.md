# Jak moderujeme AMA vlákna

*Tato stránka je generovaná z [github.com/kerray/r-brno](https://github.com/kerray/r-brno) — změny se dělají tam, přes pull request. Historie je veřejná.*

## Zásady
1. **O politickém obsahu nikdy nerozhoduje stroj sám.** Bot ani filtr
   nemažou názory. Co bot zachytí, posoudí člověk — a **když to
   nestihne do 12 hodin, komentář se automaticky pustí.** Nedostatek
   naší kapacity nesmí být tichým mazáním. (Výjimka: osobní údaje
   a výhrůžky, kategorie A.)
2. **Držení není mazání.** Zachycený komentář čeká ve frontě;
   většinu schválíme, nebo vám pomůžeme ho opravit.
3. **Moderujeme formu, ne rétoriku.** Nadávka a osobní útok jsou
   důvod k zásahu. Vložený předpoklad, podsouvání motivu nebo
   slova do úst **nikdy nejsou důvod k odstranění** — na to nemáme
   mandát a byl by to nástroj, jak hosta chránit před nepříjemnými
   otázkami. Řešíme je jen tam, kde vybíráme: v kuraci sběrného
   vlákna, a vždy s viditelným originálem.
4. **Vše logujeme a čísla zveřejníme** (viz níže).

## Čtyři kategorie zásahů
**A. Okamžité odstranění (bez diskuze):** osobní údaje třetích osob,
výhrůžky, spam. Jediná kategorie, kde automatika koná sama.

**B. Podržení s možností opravy:** vulgarita nebo osobní útok
obalený kolem jinak legitimní otázky. Dostanete od nás zprávu
s konkrétním důvodem ("odstraňte nadávku ve druhé větě"). Komentář
upravíte, odpovíte "hotovo" (nebo bot úpravu sám zaznamená) a
moderátor ho schválí. Otázka se neztrácí, jen se zbaví balastu.

**C. Označení pro moderátora:** podezření na koordinaci (čerstvé
účty, shodné formulace, časové shluky), hraniční obsah, ironie,
kterou si stroj neumí přebrat. Bot pouze upozorní tým, sám nedělá nic.

**D. Nabídka přeformulování (jen ve sběrném vlákně, žádný zásah):**
otázka obsahuje tvrzení, které se tváří jako fakt („proč jste
rozkradli X"). Komentář zůstává, kde je, nikdo ho neskrývá. Dostanete
zprávu s návrhem, jak otázku rozdělit na „je pravda, že X?" + „proč?".
Návrh dostanete **veřejnou odpovědí ve vlákně, ne soukromou zprávou**
(hromadné automatické PM jsou nejrychlejší cesta k vyřazení bota za spam
a jde to snadno vyprovokovat). Přijmout nemusíte — do povinné patnáctky
ale vybíráme otázky, které se ptají. Tohle je jediná kategorie, kde se bavíme o formulaci, a
jediná, kde z odmítnutí naší nabídky **neplyne vůbec nic**.

## Co bot je a co dělá
Používáme vlastního asistenčního bota postaveného na jazykovém
modelu. Jeho úkoly: seskupování duplicitních otázek ve sběrném
vlákně, řazení fronty pro moderátory podle závažnosti, upozornění
na vzorce koordinovaného chování a po skončení roztřídění
zodpovězeno/nezodpovězeno pro shrnutí (včetně toho, kdo z hostů
na co odpověděl). **Nemá oprávnění nic smazat.**

## Odvolání
Nesouhlasíte se zásahem → modmail, odpovíme do 24 hodin.

Postup: odvolání spustí **druhý průchod s promptem, jehož úkolem je najít
důvody, proč byl původní zásah špatný** — ne ho potvrdit. Konečné
rozhodnutí dělá člověk. Pokud je zrovna moderátorů víc, rozhoduje jiný
než ten, kdo zasáhl; pokud je jen jeden, rozhoduje on a je to takhle
napsané — nebudeme předstírat „rozhodl modtým", když je modtým jeden
člověk. Kdo je rozhodující moderátor u kterého AMA, najdete ve wiki.

**Všechna odvolání a jejich výsledky zveřejňujeme.** Když nemáme druhý
pár očí uvnitř, kontrolou je tenhle sub. Prompt, podle kterého se
rozhoduje, si můžete přečíst a připomínkovat dřív, než ho na vás
použijeme.

## Transparentnost po každém AMA
Zveřejníme: počet komentářů, počet zachycených, počet skutečně
odstraněných (podle kategorie), počet oprav dle bodu B, počet
nabídnutých a přijatých přeformulování dle bodu D, počet
zamčených větví i s důvodem, počet
odvolání a jejich výsledek. U povinné patnáctky rozpad
**zodpovězeno / odmítnuta premisa / bez odpovědi**.
```
