#!/usr/bin/env python3
"""Veřejné losování pořadí AMA na r/Brno.

K čemu to je
------------
Když o jeden termín AMA projeví zájem víc uskupení, nerozhoduje moderátor —
rozhoduje los. Aby šlo ověřit, že jsme losem nezamíchali, musí být losování
*deterministické*: ze stejného vstupu musí komukoli vyjít stejné pořadí.

Proč zrovna kurz ČNB EUR/CZK
----------------------------
Jako zdroj náhody potřebujeme číslo, které splňuje čtyři podmínky najednou:

* **veřejné** — ČNB ho vyhlašuje každý pracovní den ve 14:30 a nechává
  historii viset na webu, takže si ho kdokoli dohledá i zpětně;
* **nepředvídatelné** — nikdo z nás dopředu neví, jestli vyjde 24,315 nebo
  24,320; tři platné číslice za desetinnou čárkou stačí na to, aby se pořadí
  při každé změně úplně přeházelo;
* **zpětně ověřitelné** — kurz z daného dne se už nemění, takže si výsledek
  losování může kdokoli kdykoli přepočítat;
* **mimo náš dosah** — kurz nastavuje centrální banka, ne moderátoři r/Brno.
  Na rozdíl od neseedovaného generátoru náhody nebo od „hodil jsem kostkou"
  tady není nic, co bychom mohli potichu opakovat, dokud nevyjde, co chceme.

Vstup i výsledek losování zveřejňujeme spolu s rozpisem.

Jak se seed odvozuje
--------------------
Kurz se vezme jako řetězec tak, jak ho ČNB vypsala, a odstraní se desetinná
čárka: ``24,315`` → ``24315``. To celé číslo je seed pro ``random.Random``.
Seznam subjektů se před losováním kanonicky setřídí (``sorted()``), takže
na pořadí argumentů na příkazové řádce nezáleží.

Použití
-------
    ./tools/losovani.py --datum 2026-09-09 --subjekty "A" "B" "C"

Offline ověření třetí stranou (bez volání na ČNB) — kurz se zadá ručně:

    ./tools/losovani.py --kurz 24,315 --subjekty "A" "B" "C"

Skript nemá žádné závislosti mimo standardní knihovnu Pythonu 3.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import random
import sys
import urllib.request

CNB_URL = (
    "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/"
    "kurzy-devizoveho-trhu/denni_kurz.txt?date={datum}"
)
KOD_MENY = "EUR"
TIMEOUT = 30


def sestav_url(datum: _dt.date) -> str:
    """Vrátí URL denního fixingu ČNB pro zadaný den (formát data DD.MM.YYYY)."""
    return CNB_URL.format(datum=datum.strftime("%d.%m.%Y"))


def stahni_fixing(url: str) -> str:
    """Stáhne textový denní kurzovní lístek ČNB."""
    req = urllib.request.Request(url, headers={"User-Agent": "r-brno-losovani/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as odpoved:  # noqa: S310
        return odpoved.read().decode("utf-8-sig")


def najdi_radek_meny(fixing: str, kod: str = KOD_MENY) -> str:
    """Najde v kurzovním lístku řádek dané měny a vrátí ho tak, jak je.

    Lístek má tvar::

        01.09.2026 #169
        země|měna|množství|kód|kurz
        EMU|euro|1|EUR|24,315
        ...
    """
    radky = [r.strip() for r in fixing.splitlines() if r.strip()]
    if len(radky) < 3:
        raise ValueError(
            "Kurzovní lístek ČNB je prázdný nebo neúplný — pro zadaný den "
            "možná nebyl vyhlášen (víkend, svátek)."
        )
    hlavicka = radky[1].split("|")
    try:
        sloupec_kodu = hlavicka.index("kód")
    except ValueError:
        sloupec_kodu = 3
    for radek in radky[2:]:
        pole = radek.split("|")
        if len(pole) > sloupec_kodu and pole[sloupec_kodu].strip() == kod:
            return radek
    raise ValueError(f"V kurzovním lístku ČNB není řádek s kódem {kod}.")


def kurz_z_radku(radek: str) -> str:
    """Vytáhne z řádku lístku hodnotu kurzu jako řetězec (s desetinnou čárkou)."""
    pole = [p.strip() for p in radek.split("|")]
    if len(pole) < 5:
        raise ValueError(f"Nečekaný tvar řádku kurzovního lístku: {radek!r}")
    return pole[4]


def seed_z_kurzu(kurz: str) -> int:
    """Odvodí seed: kurz jako řetězec, pryč s desetinnou čárkou, na celé číslo.

    ``24,315`` → ``24315``
    """
    ocisteny = kurz.strip().replace(",", "").replace(".", "").replace(" ", "")
    if not ocisteny.isdigit():
        raise ValueError(
            f"Kurz {kurz!r} není číslo v očekávaném tvaru (např. 24,315)."
        )
    return int(ocisteny)


def losuj(subjekty: list[str], seed: int) -> tuple[list[str], list[str]]:
    """Vrátí dvojici (kanonicky setříděný vstup, vylosované pořadí)."""
    setridene = sorted(subjekty)
    poradi = list(setridene)
    random.Random(seed).shuffle(poradi)
    return setridene, poradi


def _parsuj_datum(text: str) -> _dt.date:
    for tvar in ("%Y-%m-%d", "%d.%m.%Y"):
        try:
            return _dt.datetime.strptime(text.strip(), tvar).date()
        except ValueError:
            continue
    raise argparse.ArgumentTypeError(
        f"Datum {text!r} nerozumím — použij 2026-09-09 nebo 09.09.2026."
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Veřejné losování pořadí AMA na r/Brno "
            "(seed = kurz ČNB EUR/CZK vyhlášený v den losování)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--datum",
        type=_parsuj_datum,
        help=(
            "Den losování (2026-09-09 nebo 09.09.2026). Podle něj se stáhne "
            "kurz z ČNB. Výchozí: dnešek."
        ),
    )
    parser.add_argument(
        "--kurz",
        help=(
            "Kurz EUR/CZK zadaný ručně (např. 24,315) — pro offline ověření "
            "výsledku bez volání na ČNB."
        ),
    )
    parser.add_argument(
        "--subjekty",
        nargs="+",
        required=True,
        metavar="NÁZEV",
        help=(
            "Losovaná uskupení. Na pořadí argumentů nezáleží — seznam se před "
            "losováním kanonicky setřídí."
        ),
    )
    args = parser.parse_args(argv)

    if len(set(args.subjekty)) != len(args.subjekty):
        parser.error("V seznamu subjektů je duplicita — každý subjekt uveď jednou.")

    datum = args.datum or _dt.date.today()
    url = sestav_url(datum)

    if args.kurz:
        kurz = args.kurz.strip()
        radek = f"(zadáno ručně přepínačem --kurz: {kurz})"
        zdroj = f"{url}   [NESTAHOVÁNO — kurz zadán ručně]"
    else:
        try:
            fixing = stahni_fixing(url)
        except Exception as chyba:  # noqa: BLE001
            print(
                f"CHYBA: kurzovní lístek ČNB se nepodařilo stáhnout: {chyba}",
                file=sys.stderr,
            )
            print("Kurz lze zadat ručně přepínačem --kurz.", file=sys.stderr)
            return 2
        radek = najdi_radek_meny(fixing)
        kurz = kurz_z_radku(radek)
        zdroj = url

    seed = seed_z_kurzu(kurz)
    setridene, poradi = losuj(args.subjekty, seed)

    print("=" * 72)
    print("LOSOVÁNÍ POŘADÍ AMA — r/Brno")
    print("=" * 72)
    print(f"Datum losování   : {datum.strftime('%d.%m.%Y')}")
    print(f"Zdroj náhody     : kurz ČNB {KOD_MENY}/CZK, denní kurzovní lístek")
    print(f"Zdrojová URL     : {zdroj}")
    print(f"Řádek z ČNB      : {radek}")
    print(f"Kurz             : {kurz}")
    print(f"Odvozený seed    : {seed}   (kurz bez desetinné čárky)")
    print()
    print("Kanonicky setříděný vstup (sorted()):")
    for i, subjekt in enumerate(setridene, 1):
        print(f"  {i:>2}. {subjekt}")
    print()
    print("VYLOSOVANÉ POŘADÍ:")
    for i, subjekt in enumerate(poradi, 1):
        print(f"  {i:>2}. {subjekt}")
    print()
    print("Přepočítat: random.Random(seed).shuffle(sorted(subjekty))")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
