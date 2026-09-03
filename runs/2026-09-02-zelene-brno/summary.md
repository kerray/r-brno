# Transparenční čísla — AMA Zelené Brno (2026-09-02)

Veřejná verze shrnutí je na **[/r/Brno/wiki/ama/2026-09-02-zelene-brno](https://www.reddit.com/r/Brno/wiki/ama/2026-09-02-zelene-brno)**
(zdroj: [`wiki/ama/2026-09-02-zelene-brno.md`](../../wiki/ama/2026-09-02-zelene-brno.md)).
Tady je totéž v podrobnostech, které by wiki stránku zahltily — hlavně rozpis jednotlivých
moderačních zásahů.

| | |
|---|---|
| Živé okno | 2026-09-02 9:00–11:30 CEST (vlákno odemčeno 9:01:18) |
| Okno na doplnění | do 2026-09-03 11:30; vlákno zamčeno 11:36:25 |
| AMA vlákno | [`1w52826`](https://redd.it/1w52826) |
| Sběrné vlákno | [`1w3ahgu`](https://redd.it/1w3ahgu) |
| Oznamovací vlákno | [`1w390zo`](https://redd.it/1w390zo) |
| Rozhodující moderátor | kerray (`/u/kerray`) |

## Zdroj čísel

- **obsah vlákna** — Reddit API, `get_submission_by_id` + `get_comments` (74 komentářů,
  shoda s `num_comments`), staženo 2026-09-03,
- **moderační zásahy** — `subreddit.mod.log` za období 2026-09-01 00:00 → 2026-09-03 11:40 CEST,
  261 záznamů, z toho 94 v AMA vláknech. Zásah pozná `action == "removecomment"`, původce pole
  `mod` (`AutoModerator` / `ponocny_bot` / člověk), pravidlo pole `details`.

- **snímek citovaných komentářů** — [`answers.json`](answers.json), 28 komentářů (14 povinných
  otázek + 14 odpovědí hostů), pořízen při zveřejnění shrnutí. Slouží ke strojové kontrole, že
  citace ve shrnutí sedí doslova: `./tools/overit_citace.py wiki/ama/2026-09-02-zelene-brno.md
  --snimek runs/2026-09-02-zelene-brno/answers.json`. Ke dni zveřejnění **sedí všech 28 citací**.

**Pozor na výklad dat z vlákna:** `get_comments` vrací viditelný strom, odstraněné komentáře se
v něm typicky vůbec neobjeví. Tvrzení o moderaci proto stojí na mod logu, ne na fetchi vlákna.

## Odpovědi

| | |
|---|---|
| Povinných otázek | 14 |
| `v_okne` | **14** |
| `doplneno` | 0 |
| `odmitnuta_premisa` | 0 |
| `bez_odpovedi` | **0** |

| Host | Přímých odpovědí | Otázky | Komentářů ve vlákně celkem |
|---|---|---|---|
| /u/Natalie_Vencovska | 9 | 1, 2, 3, 4, 6, 8, 10, 11, 13 | 12 |
| /u/zbiejczuk | 5 | 5, 7, 9, 12, 14 | 14 |
| /u/MichalBerg | 0 | — | 4 |

Rozpad přímých odpovědí se shoduje s indexovým komentářem bota `p7bxpzs`.

**Hraniční případ ke kategorii `odmitnuta_premisa`:** otázka 8 se ptá *„Prý jste pro ODSun
nádraží… Je to pravda?"*. Odpověď `p7c9ius` popisuje opačný postoj, ale **nepojmenovává tvrzení,
které odmítá**, takže mechanický klíč naplněný není a kategorie zůstává `v_okne`. Zaznamenáno,
protože je to přesně ten typ případu, na který se klíč ptá v otevřené otázce č. 1
([`rules/summary-key.md`](../../rules/summary-key.md)).

## Výrazné reakce: 0

Zamrzlý práh: skóre ≥ 50 % nejvýše hodnocené reakce v podvláknu **a zároveň** ≥ 10 bodů.

| Otázka | Reakcí čtenářů | Nejvyšší skóre | Nad prahem |
|---|---|---|---|
| 2 | 4 | 3 | 0 |
| 4 | 4 | **5** (`p7c0o8e`) | 0 |
| 8 | 2 | 1 | 0 |
| 10 | 1 | 1 | 0 |
| ostatních 10 otázek | 0 | — | 0 |

Rozhodnutí práh zpětně neměnit: [`decisions.md`](decisions.md), Rozhodnutí 3.

## Moderační zásahy

| Kategorie | Počet |
|---|---|
| A — okamžité odstranění (osobní údaje, výhrůžky, spam) | 0 |
| B — podržení s možností opravy | 0 |
| C — označení pro moderátora | 0 |
| D — nabídka přeformulování | 0 |
| AutoModerator, filtr na stáří účtu | **14** |
| odstranění moderátorem na žádost autora | 1 |
| komentáře odstraněné po uzavření vlákna | 0 |
| zamčené větve | 0 |
| odvolání | 0 |

Kategorie A–D jsou obsahové soudy a nepadl ani jeden. Čtrnáct zásahů AutoModeratoru žádný obsahový
soud není — filtruje se podle stáří účtu.

**`/u/ponocny_bot` neodstranil v AMA vláknech ani jeden komentář.**

### Rozpis: /u/Natalie_Vencovska, 12 z 12 komentářů

Pravidlo `Novy ucet (< 30 dni) - komentar` (v configu `action: filter`; Reddit loguje `filter`
i `remove` shodně jako `removecomment`). „Puštěno" = první schvalovací akce v mod logu.

| # | Komentář | Zachyceno | Puštěno | Kdo pustil | Neviditelný |
|---|---|---|---|---|---|
| 1 | `p7byfse` | 9:11:37 | 9:13:19 | ponocny_bot | 1 m 42 s |
| 2 | `p7bz2kv` | 9:17:05 | 9:18:17 | kerray | 1 m 12 s |
| 3 | `p7c1bqd` | 9:36:54 | 9:39:19 | ponocny_bot | 2 m 25 s |
| 4 | `p7c1pcq` | 9:40:15 | 9:41:22 | ponocny_bot | 1 m 07 s |
| 5 | `p7c4cs0` | 10:03:46 | 10:04:13 | kerray | 0 m 27 s |
| 6 | `p7c59e4` | 10:11:53 | 10:12:22 | kerray | 0 m 29 s |
| 7 | `p7c7gg8` | 10:31:18 | 10:35:13 | kerray | 3 m 55 s |
| 8 | `p7c9ius` | 10:49:35 | 10:51:50 | kerray | 2 m 15 s |
| 9 | `p7cchmc` | 11:15:18 | 11:19:57 | kerray | 4 m 39 s |
| 10 | `p7ce78l` | 11:30:01 | 11:33:49 | kerray | 3 m 48 s |
| 11 | `p7cgo49` | 11:50:33 | 11:52:18 | ponocny_bot | 1 m 45 s |
| 12 | `p7cihel` | 12:05:13 | 12:13:20 | ponocny_bot | 8 m 07 s |

Vše 2026-09-02. Nejméně 27 s, obvykle kolem 2 minut, nejdéle 8 m 07 s; součet ≈ **31 m 51 s**.
Poslední dva zásahy padly už po konci živého okna, v okně na doplnění.

**Pustil to pokaždé člověk.** Pět schválení proběhlo účtem `ponocny_bot`, ale ani jedno
automaticky — automatika na tohle neexistuje. Slíbené automatické puštění po 12 hodinách není
implementované; kdyby se moderátor zrovna nedíval, komentář by čekal dál.

### Rozpis: další dva zasažení týmž pravidlem

| Komentář | Autor | Kde | Zachyceno | Puštěno | Neviditelný |
|---|---|---|---|---|---|
| `p75kukc` | /u/look_butt_dont_touch | sběrné vlákno | 1. 9. 12:56:04 | 13:01:55 | **5 m 51 s** |
| `p7bssdq` | /u/FigureKooky1408 | AMA vlákno | 2. 9. 8:23:50 | 8:26:18 | **2 m 28 s** |

`p75kukc` je otázka, ze které se stala **povinná otázka č. 10**.

### Odstranění moderátorem

| Komentář | Kdy | Kdo odstranil | Proč |
|---|---|---|---|
| `p75bi6p` (vlákno `1w390zo`) | 1. 9. 11:47:33 | kerray | **autor si to vyžádal v textu komentáře** |

Obsah se nezveřejňuje — běžný uživatel, podle klíče jen fakt a čas. Skóre 1, žádné reporty,
žádný removal reason.

### Zamykání

| Kdy | Vlákno | Akce | Kdo |
|---|---|---|---|
| 1. 9. 18:21:41 | `1w3ahgu` | lock (uzávěrka sběru byla 18:00) | kerray |
| 2. 9. 8:38:49 | `1w52826` | lock (bot mezitím vkládal otázky) | kerray |
| 2. 9. 9:01:18 | `1w52826` | **unlock = start živého okna** | kerray |
| 2. 9. 11:38:52 → 11:39:02 | `1w3ahgu` | unlock + lock (10 s, doplnění aktualizace do těla) | ponocny_bot |
| 3. 9. 11:36:25 | `1w52826` | **lock = konec okna na doplnění** | ponocny_bot |

Žádná jednotlivá větev zamčená nebyla.

### Flairy

Za celé období **žádná změna flairu v AMA vláknech** (0 `editflair`). Flair
`AMA host — Zelené Brno` nesou přesně `/u/Natalie_Vencovska`, `/u/zbiejczuk` a `/u/MichalBerg`.

## Kurace

Model se nepustil, wildcardy nepoužity, lidských odchylek 0, náklad 0 Kč.
Podrobně v [`meta.json`](meta.json) a [`decisions.md`](decisions.md), Rozhodnutí 1.

## Co tenhle běh neumí doložit

- **původní znění editované odpovědi** `p7c59e4` — vlákno se průběžně nesnímalo, Reddit předchozí
  verze nevydává; slib byl proto zrušen a nahrazen slabším ([`decisions.md`](decisions.md),
  Rozhodnutí 4),
- **nic o kvalitě kuračního klíče ani o chování modelu** — nevybíralo se,
- **shodu se stínovým během** — stínový běh se nekonal.
