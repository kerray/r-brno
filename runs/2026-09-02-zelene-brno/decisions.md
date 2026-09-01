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

## Poznámka k záznamu (doplněno po zveřejnění)

Ve zveřejněném textu ([`final.md`](final.md)) je u položky 14 uvedeno skóre **(2)**, zatímco
v [`snapshot.json`](snapshot.json) má komentář `p75vfyb` skóre **1**. Rozhodující je snapshot —
je to fotka vlákna při uzávěrce a nesahá se do něj. Na složení povinné sady to nemá vliv:
výběr se nekonal, povinných je všech 14 otázek bez ohledu na pořadí. `final.md` zůstává
doslovným záznamem toho, co bylo zveřejněno, i s tímhle rozdílem — přepisovat zveřejněný text
zpětně by bylo horší než ho nechat a označit.
