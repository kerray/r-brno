#!/usr/bin/env python3
"""Ověří, že citace ve shrnutí AMA sedí slovo od slova s tím, co je na Redditu.

Shrnutí slibuje, že se otázky ani odpovědi hostů **neupravují a nezkracují**.
Tenhle skript ten slib kontroluje strojově: z markdownu shrnutí vytáhne každou
citaci i s ID komentáře, vezme týž komentář ze zdroje a porovná znak po znaku.

Dva zdroje, oba ověřitelné:

1. **Snímek** `runs/<beh>/answers.json` — offline, bez sítě, bez přihlášení.
   Snímek se pořizuje při zveřejnění shrnutí a leží ve stejném repozitáři,
   takže kontrola dá stejný výsledek i za rok:

       ./tools/overit_citace.py wiki/ama/2026-09-02-zelene-brno.md \
           --snimek runs/2026-09-02-zelene-brno/answers.json

2. **Živý Reddit** — porovná shrnutí proti tomu, co ve vlákně stojí teď:

       ./tools/overit_citace.py wiki/ama/2026-09-02-zelene-brno.md --zive

   Veřejné `.json` endpointy Reddit z části adres blokuje (HTTP 403). Když se to
   stane, dá se použít vlastní Reddit aplikace přes proměnné prostředí
   `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USERNAME`,
   `REDDIT_PASSWORD` — účet stačí jakýkoli, číst veřejné komentáře smí každý.

Návratový kód 0 = všechno sedí, 1 = aspoň jedna citace nesedí nebo ji nešlo
načíst.

**Co to NEUMÍ a je dobré to vědět:** když host komentář po zveřejnění shrnutí
edituje, režim `--zive` začne hlásit rozdíl. Reddit předchozí verze nevydává,
takže odlišit „my jsme citovali špatně" od „autor to mezitím změnil" jde jen
podle příznaku `edited` a podle snímku. Proto se snímek pořizuje a commituje.
"""

from __future__ import annotations

import argparse
import base64
import difflib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "r-brno-overeni-citaci/1.1 (+https://github.com/kerray/r-brno)"

ODPOVED = re.compile(
    r"^\*\*Odpověď — \[(?P<autor>/u/[\w-]+)\]\((?P<url>https://www\.reddit\.com/r/\w+/comments/"
    r"(?P<vlakno>\w+)/[^/]*/(?P<id>\w+)/?)\)[^\n]*\*\*$",
    re.M,
)
OTAZKA = re.compile(
    r"^\*Skóre při uzávěrce sběru: \d+ · \[komentář s otázkou ve vlákně\]"
    r"\(https://www\.reddit\.com/r/\w+/comments/(?P<vlakno>\w+)/[^/]*/(?P<id>\w+)/?\)[^\n]*\*$",
    re.M,
)


def normalizuj(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    radky = [r.rstrip() for r in text.split("\n")]
    while radky and not radky[0]:
        radky.pop(0)
    while radky and not radky[-1]:
        radky.pop()
    return "\n".join(radky)


def odcituj(blok: str) -> str:
    out = []
    for radek in blok.split("\n"):
        if radek.startswith("> "):
            out.append(radek[2:])
        elif radek.strip() in (">", ""):
            out.append("")
        else:
            out.append(radek)
    return normalizuj("\n".join(out))


def blok_citace(text: str, od: int) -> str:
    """Souvislý blok '>' řádků, který za pozicí `od` následuje."""
    sebrano, zacalo = [], False
    for radek in text[od:].split("\n"):
        if radek.startswith(">"):
            zacalo = True
            sebrano.append(radek)
        elif zacalo and radek.strip() == "":
            sebrano.append("")
        elif zacalo:
            break
    return odcituj("\n".join(sebrano))


def vnitrni_citace(body: str) -> str:
    """Z komentáře bota s povinnou otázkou vytáhne samotné znění otázky."""
    return blok_citace(body, 0)


class Zdroj:
    def nacti(self, vlakno: str, cid: str) -> dict:  # pragma: no cover
        raise NotImplementedError


class ZeSnimku(Zdroj):
    def __init__(self, cesta: str):
        self.data = json.load(open(cesta, encoding="utf-8"))["komentare"]
        self.popis = f"snímek {cesta} (pořízen {json.load(open(cesta, encoding='utf-8')).get('porizeno_utc')})"

    def nacti(self, vlakno: str, cid: str) -> dict:
        if cid not in self.data:
            raise LookupError(f"komentář {cid} ve snímku není")
        return self.data[cid]


class ZeRedditu(Zdroj):
    def __init__(self, pauza: float):
        self.pauza = pauza
        self.token = self._token()
        self.popis = "živý Reddit " + ("(přihlášeno vlastní aplikací)" if self.token else "(veřejné .json)")

    @staticmethod
    def _token():
        cid, secret = os.environ.get("REDDIT_CLIENT_ID"), os.environ.get("REDDIT_CLIENT_SECRET")
        user, heslo = os.environ.get("REDDIT_USERNAME"), os.environ.get("REDDIT_PASSWORD")
        if not (cid and secret and user and heslo):
            return None
        data = urllib.parse.urlencode(
            {"grant_type": "password", "username": user, "password": heslo}
        ).encode()
        basic = base64.b64encode(f"{cid}:{secret}".encode()).decode()
        req = urllib.request.Request(
            "https://www.reddit.com/api/v1/access_token",
            data=data,
            headers={"Authorization": f"Basic {basic}", "User-Agent": UA},
        )
        with urllib.request.urlopen(req, timeout=30) as odpoved:
            return json.load(odpoved)["access_token"]

    def nacti(self, vlakno: str, cid: str) -> dict:
        if self.token:
            url = f"https://oauth.reddit.com/api/info?id=t1_{cid}&raw_json=1"
            hlavicky = {"Authorization": f"Bearer {self.token}", "User-Agent": UA}
        else:
            url = f"https://www.reddit.com/comments/{vlakno}/_/{cid}.json?raw_json=1"
            hlavicky = {"User-Agent": UA}
        req = urllib.request.Request(url, headers=hlavicky)
        with urllib.request.urlopen(req, timeout=30) as odpoved:
            data = json.load(odpoved)
        time.sleep(self.pauza)
        listingy = data if isinstance(data, list) else [data]
        for listing in listingy:
            for dite in listing.get("data", {}).get("children", []):
                if dite.get("kind") == "t1" and dite["data"].get("id") == cid:
                    return dite["data"]
        raise LookupError(f"komentář {cid} nenalezen")


def porovnej(nazev, cid, nase, data, ocekavany_autor, vnitrni):
    skutecny = vnitrni_citace(data.get("body", "")) if vnitrni else normalizuj(data.get("body", ""))
    autor = "/u/" + str(data.get("author"))
    edited = data.get("edited")
    znacka = "" if not edited else "  (Reddit hlásí edited)"

    if ocekavany_autor and autor != ocekavany_autor:
        print(f"  {nazev} {cid}  NESEDÍ AUTOR: shrnutí {ocekavany_autor}, zdroj {autor}")
        return False
    if nase == skutecny:
        print(f"  {nazev} {cid}  OK{znacka}")
        return True
    print(f"  {nazev} {cid}  NESEDÍ{znacka}")
    for radek in difflib.unified_diff(
        skutecny.split("\n"), nase.split("\n"),
        fromfile=f"zdroj/{cid}", tofile=f"shrnuti/{cid}", lineterm="",
    ):
        print("      " + radek)
    return False


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("soubor", help="markdown shrnutí")
    ap.add_argument("--snimek", help="runs/<beh>/answers.json — offline zdroj")
    ap.add_argument("--zive", action="store_true", help="porovnat proti živému Redditu")
    ap.add_argument("--pauza", type=float, default=1.5, help="prodleva mezi dotazy (s)")
    args = ap.parse_args()

    if bool(args.snimek) == bool(args.zive):
        ap.error("zvol právě jeden zdroj: --snimek CESTA, nebo --zive")

    zdroj = ZeSnimku(args.snimek) if args.snimek else ZeRedditu(args.pauza)
    text = open(args.soubor, encoding="utf-8").read()

    otazky = [(m, blok_citace(text, m.end()), None, True) for m in OTAZKA.finditer(text)]
    odpovedi = [(m, blok_citace(text, m.end()), m.group("autor"), False) for m in ODPOVED.finditer(text)]
    if not otazky and not odpovedi:
        print("CHYBA: v souboru není ani jedna citace v očekávaném tvaru.")
        return 1

    print("=" * 72)
    print("OVĚŘENÍ CITACÍ VE SHRNUTÍ AMA")
    print("=" * 72)
    print(f"Soubor : {args.soubor}")
    print(f"Zdroj  : {zdroj.popis}")
    print(f"Citací : {len(otazky)} otázek + {len(odpovedi)} odpovědí")
    print()

    chyb = 0
    for nazev, polozky in (("otázka ", otazky), ("odpověď", odpovedi)):
        for m, nase, autor, vnitrni in polozky:
            cid = m.group("id")
            try:
                data = zdroj.nacti(m.group("vlakno"), cid)
            except (urllib.error.URLError, LookupError, json.JSONDecodeError) as chyba:
                print(f"  {nazev} {cid}  NELZE NAČÍST: {chyba}")
                chyb += 1
                continue
            if not porovnej(nazev, cid, nase, data, autor, vnitrni):
                chyb += 1

    celkem = len(otazky) + len(odpovedi)
    print()
    print("=" * 72)
    if chyb:
        print(f"VÝSLEDEK: {celkem - chyb} z {celkem} citací sedí, {chyb} NESEDÍ.")
    else:
        print(f"VÝSLEDEK: všech {celkem} citací sedí slovo od slova.")
    print("=" * 72)
    return 1 if chyb else 0


if __name__ == "__main__":
    sys.exit(main())
