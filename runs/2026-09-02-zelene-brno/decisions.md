# Lidské zásahy — AMA Zelené Brno (2026-09-02)

**Lidských odchylek od výstupu modelu: 0.** Ne proto, že by se moderátor s modelem shodl —
model se v tomhle běhu vůbec nepustil, takže nebylo do čeho zasahovat. Nula je tu popis stavu,
ne skóre.

Rozhodující moderátor: **kerray** (`/u/kerray`).

---

## Rozhodnutí 1 — patnáctka se nedoplňovala, wildcardy nepoužity

**Kdy:** 2026-09-01, po uzávěrce sběru (18:00), před sestavením povinné sady.

**Stav vstupu:** ve sběrném vlákně [`1w3ahgu`](https://redd.it/1w3ahgu) bylo **14 kandidátních
otázek od 10 účtů** — viz [`snapshot.json`](snapshot.json) a [`snapshot.md`](snapshot.md).
Tedy **méně než 15 povinných slotů**.

**Rozhodnutí:** do povinné sady jde **všech 14 otázek**. Slotové rozdělení 10/3/2 se neuplatnilo
a **ani jeden ze dvou wildcard slotů nebyl použit**. Kurace se nepouštěla.

**Odůvodnění:** klíč tenhle případ řeší sám — [`rules/curation-key.md`](../../rules/curation-key.md),
oddíl „Když je způsobilých otázek méně než 15": patnáctka se **uměle nedoplňuje**, do povinné sady
jde všech N způsobilých otázek, slotové rozdělení se neuplatní a wildcardy se nepoužijí, protože
nemá smysl vytahovat přehlédnutou otázku, když se nic nepřehlédlo.

**Tohle není odchylka od pravidel, ale jejich uplatnění.** Na tom záleží: pravidlo bylo zveřejněné
**předem**, dřív než bylo známo, kolik otázek přijde. Kdyby vzniklo až po uzávěrce, byla by to
výmluva ušitá na míru výsledku. Takhle je to jen provedení něčeho, co si šlo přečíst dopředu
a co šlo dopředu připomínkovat.

**Odchylka od playbooku to ale je** — ten počítá s rozdělením moci 10 hlasování / 3 model /
2 moderátor. V tomhle běhu vyšlo **14 hlasování / 0 model / 0 moderátor**. Je to odchylka směrem
k **menší** moci moderátora i modelu, ne větší; kdyby vyšla opačně, patřila by sem o to naléhavěji.

**Přiznáno veřejně:** ne jen tady. Je to napsané rovnou v prvním odstavci zveřejněné povinné sady
ve vlákně — viz [`final.md`](final.md), komentář `p78oxkn`.

**Co z prvního běhu neplyne:** nic o kvalitě kuračního klíče ani o chování modelu. Neproběhl výběr,
takže není co měřit. První použitelné srovnání přijde až u subjektu, kde otázek bude víc než slotů.

---

## Rozhodnutí 2 — překlep ve zveřejněném skóre opraven editem

**Kdy:** 2026-09-01 ve 22:13, tedy 35 minut po zveřejnění povinné sady.

**Co se stalo:** ve zveřejněném komentáři `p78oxkn` bylo u položky 14
([`p75vfyb`](https://www.reddit.com/r/Brno/comments/1w3ahgu/-/p75vfyb/)) uvedeno skóre **(2)**,
zatímco [`snapshot.json`](snapshot.json) má u téhož komentáře **1**. Překlep v přepisu, ne rozdíl
v datech — snapshot se nezměnil.

**Rozhodnutí:** komentář **editován týmž účtem** (`/u/ponocny_bot`): skóre opraveno na `(1)`
a pod seznam přidána viditelná poznámka o opravě, která říká, co bylo špatně a že rozhodující je
snapshot. [`final.md`](final.md) nese znění po opravě.

**Odůvodnění:** Reddit označuje editovaný komentář jako editovaný, takže tichá oprava tu ani není
technicky možná — a i kdyby byla, oprava přiznaná v samotném textu je to jediné, co odpovídá tomu,
co si tenhle repozitář o sobě tvrdí. Nechat překlep stát a odkázat lidi do logu by po čtenáři
chtělo práci navíc kvůli naší chybě.

**Na složení povinné sady to nemělo vliv.** Nevybíralo se (viz Rozhodnutí 1), povinných je všech
14 otázek bez ohledu na pořadí i na to číslo. Kdyby se vybíralo, byl by to zásah do výsledku
a patřil by sem s úplně jinou vahou.

**Rozhodující je snapshot.** Do [`snapshot.json`](snapshot.json) se nesáhlo a sahat se nebude —
je to fotka vlákna při uzávěrce a přesně proti ní si má kdokoli výběr přepočítat.

---

## Rozhodnutí 3 — shrnutí pilotu se dělá podle zamrzlého prahu, i když vyjde prázdné

**Kdy:** 2026-09-02, po skončení AMA, při přípravě shrnutí.

**Co se stalo:** prompt zamrzlý na tagu `ama-2026-09-02-zelene-brno` vybírá „výrazné reakce"
prahem *skóre ≥ 50 % nejlepší reakce v podvláknu **a zároveň** ≥ 10 bodů*. V tomhle vlákně je
ten práh **nedosažitelný**. Rozhodující číslo je skóre **čtenářských reakcí na odpovědi hostů**,
protože právě na ně se práh vztahuje: nejvýše hlasovaná taková reakce měla **5 bodů**
(`p7c0o8e`, podvlákno otázky 4). Reakce navíc vznikly jen pod **čtyřmi ze čtrnácti** otázek
(2, 4, 8, 10); pod zbylými deseti není žádná. Prahem ≥ 10 neprojde nic.

Pro pořádek, ať se to nesplete: **skóre samotných otázek je jiné číslo a pro práh nerozhoduje.**
Ve sběrném vlákně měla nejvýše hlasovaná otázka 9 bodů (viz [`snapshot.md`](snapshot.md));
komentář s otázkou 4 v AMA vlákně má bodů 10. Ani jedno z těch čísel do prahu nevstupuje.

**Byly tři možnosti:**

| | Co by to znamenalo |
|---|---|
| 1. Nechat práh a shrnutí vydat | sekce výrazných reakcí vyjde **prázdná** |
| 2. Vyměnit pravidlo a použít ho zpětně | pět reakcí by se objevilo, ale pravidlo by se měnilo po výsledku |
| 3. Vyměnit pravidlo **až od dalšího AMA** | pilot se dokončí podle zamrzlé verze, prázdná sekce zůstane |

**Rozhodnutí: možnost 3.** Shrnutí pilotu se generuje **podle tagu**, s původním prahem, a sekce
výrazných reakcí v něm bude prázdná s vysvětlením. Nové pravidlo (pět nejvýše hlasovaných reakcí
se skóre ≥ 2) platí **od druhého AMA v sérii**.

**Odůvodnění — je v jedné větě a je to celý smysl zamrazování: skóre už známe.** Kdybychom teď
pravidlo vyměnili a použili zpětně, udělali bychom přesně ten úkon, proti kterému je zamrazení
postavené — změnu pravidla poté, co je vidět, jak dopadne. Že by nová verze byla *lepší*, na tom
nic nemění; lepší pravidlo zavedené se znalostí výsledku je pořád pravidlo zavedené se znalostí
výsledku. **Prázdná sekce s vysvětlením je doklad, že mechanismus funguje. Pět zpětně vytažených
reakcí by byl doklad opaku.**

**Navržené znění do shrnutí** místo prázdné sekce (schvaluje kerray):

> **Výrazné reakce:** žádné. Ne proto, že by čtenáři nereagovali — reakce pod odpověďmi hostů
> jsou, jen jich je málo a mají nízké skóre. Práh zamrzlý před tímhle AMA požadoval skóre
> **aspoň 10**; nejvýše hlasovaná čtenářská reakce pod odpovědí hosta měla **5 bodů**, takže ho
> nesplnila ani jedna. Práh jsme **nezměnili zpětně**, protože skóre už bylo vidět a měnit pravidlo podle
> výsledku je přesně to, čemu má zamrazení bránit. Od dalšího AMA platí pevný počet místo prahu:
> pět nejvýše hlasovaných reakcí se skóre aspoň 2. Rozhodnutí i důvod:
> [`runs/2026-09-02-zelene-brno/decisions.md`](https://github.com/kerray/r-brno/blob/main/runs/2026-09-02-zelene-brno/decisions.md).

**Změna pravidla je zapsaná** v [`prompts/summary.md`](../../prompts/summary.md) a v novém psaném
klíči [`rules/summary-key.md`](../../rules/summary-key.md), obojí s poznámkou, od kdy platí.

---

## Rozhodnutí 4 — slib „doplníme původní znění editované odpovědi" se ruší, protože je nesplnitelný

**Kdy:** 2026-09-03, při přípravě shrnutí.

**Co se stalo:** odpověď na povinnou otázku 1
([`p7c59e4`](https://www.reddit.com/r/Brno/comments/1w52826/-/p7c59e4/), /u/Natalie_Vencovska)
byla **editována 2026-09-02 v 11:30:55**, tedy 55 sekund po konci živého okna. Zamrzlý
`prompts/summary.md` u editované odpovědi hosta slibuje **doplnit původní znění**.

**Původní znění nemáme a nejde získat.** Reddit předchozí verze komentářů nevydává — API vrací
jen příznak `edited` a čas úpravy. Vlákno se v průběhu AMA nesnímalo, takže není z čeho čerpat.

**Rozhodnutí:** slib se **neplní tichým vynecháním, ale ruší se a nahrazuje slabším, který splnit
jde**: uvádí se fakt a čas úpravy vždy, původní znění jen tehdy, když ho máme ze snímku. Kde
snímek chybí, shrnutí **napíše, že původní znění nemáme**. Ve shrnutí pilotu je to napsané
u otázky 1, ne schované.

**Odůvodnění:** je to druhý slib bez mechanismu, na který jsme narazili (první je automatické
pouštění zadržených komentářů po 12 hodinách). Nabízet ověřitelnost, která neexistuje, je horší
než ji nenabízet — čtenář si na ni může vsadit. Platí tu totéž, co u zveřejňování kódu: nenabízej
test, který neprojde.

**Zapsáno** v [`prompts/summary.md`](../../prompts/summary.md) a v
[`rules/summary-key.md`](../../rules/summary-key.md), oddíl „Původní znění editované odpovědi
hosta jde uvést jen ze snímku".

**Úkol pro AMA #2:** snímat odpovědi hostů průběžně, aby slib šlo obnovit v silnější podobě.

---

## Poznámka k Rozhodnutí 3 — které skóre se počítá

Původní formulace argumentovala tím, že *nejvýše hlasovaná otázka měla 9 bodů*. Bylo to
zavádějící: práh se vztahuje na **čtenářské reakce pod odpověďmi hostů**, ne na otázky. Rozhodující
číslo je **5 bodů** (`p7c0o8e`, podvlákno otázky 4). Skóre otázek je jiná veličina — ve sběrném
vlákně 9 bodů u nejvýše hlasované otázky, v AMA vlákně 10 bodů u komentáře s otázkou 4 — a do
prahu nevstupuje ani jedno. Text Rozhodnutí 3 je opraven; závěr se nemění.

---

## Co se v tomhle běhu nekonalo

| Krok | Stav |
|---|---|
| zaslepení vstupu (`[HOST]` / `[SUBJEKT]`) → `input.json` | neproběhlo — vstup se modelu nepředával |
| rozhodující běh kurace → `output.json` | neproběhl — nebylo z čeho vybírat |
| stínový běh → `shadow.json` | neproběhl — nemá se s čím porovnávat |
| shoda běhu se stínem → `agreement.md` | nevzniká |
| výběr 2 wildcardů moderátorem | neproběhl (viz Rozhodnutí 1) |

Náklad na API za tenhle běh je **0 Kč** — žádné volání modelu. Viz [`meta.json`](meta.json).

---

## Poznámka k záznamu — časové razítko snapshotu

V [`snapshot.md`](snapshot.md) bylo u řádku „Pořízeno" napsáno `16:23`, protože razítko vzniklo
na stroji běžícím v UTC. Správně je **18:23 CEST**; snapshot je pořízený po uzávěrce (18:00), jen
byl špatně popsaný. Opraven popisek v `snapshot.md` a pole `ama.snapshot_porizen` v
[`meta.json`](meta.json).

Je to **jediná výjimka z pravidla „do snapshotu se nesahá"** a stojí za to říct, kde přesně vede
hranice: neopravil se obsah snapshotu — ani jeden komentář, skóre, id ani pořadí — jen chybně
zapsané časové pásmo u razítka. Kdyby šlo o data, oprava by se nedělala a rozdíl by se popsal tady.
