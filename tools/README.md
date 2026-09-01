# tools/

Skripty, které rozhodují o něčem, co by jinak rozhodl moderátor. Jsou tady
proto, aby si kdokoli mohl výsledek přepočítat sám a nemusel nám věřit.

## `losovani.py` — veřejné losování pořadí AMA

Když o jeden termín AMA projeví zájem víc uskupení, rozhoduje **veřejné
losování**, ne moderátor. Aby to bylo ověřitelné, je los deterministický: ze
stejného vstupu vyjde komukoli stejné pořadí.

### Jak to funguje

1. **Zdroj náhody** je kurz **ČNB EUR/CZK** vyhlášený v den losování. Bereme ho
   z oficiálního denního kurzovního lístku:
   `https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=DD.MM.YYYY`

   Proč zrovna tohle číslo: je **veřejné** (ČNB ho vyhlašuje každý pracovní den
   ve 14:30 a nechává historii na webu), **nepředvídatelné** (dopředu nikdo
   neví, jestli vyjde 24,315 nebo 24,320), **zpětně ověřitelné** (kurz z daného
   dne se už nezmění) a **mimo dosah pořadatelů** — nastavuje ho centrální
   banka, ne moderátoři r/Brno. Není tedy nic, co bychom mohli potichu
   opakovat, dokud nevyjde, co se nám hodí.

2. **Seed** se z kurzu odvodí průhledně: kurz jako řetězec, pryč s desetinnou
   čárkou → celé číslo. `24,315` → `24315`.

3. **Vstup se kanonicky setřídí** (`sorted()`) ještě před losováním, takže na
   pořadí, v jakém subjekty zadáme na příkazovou řádku, nezáleží.

4. Losuje se `random.Random(seed).shuffle(...)` nad tím setříděným seznamem.

Vstup (datum, kurz, celý řádek z ČNB, seed) i výsledek zveřejňujeme spolu
s rozpisem.

### Spuštění

Skript je čistý Python 3 bez závislostí — stačí systémový `python3`.

```bash
./tools/losovani.py --datum 2026-09-09 --subjekty "Uskupení A" "Uskupení B" "Uskupení C"
```

### Jak si losování přepočítat

Ve zveřejněném záznamu losování najdete **datum** a **kurz**. Obojí si můžete
ověřit přímo u ČNB (odkaz je ve výstupu skriptu) a pak si výsledek spočítat
sami — buď se stažením kurzu:

```bash
./tools/losovani.py --datum 2026-09-09 --subjekty "Uskupení A" "Uskupení B" "Uskupení C"
```

…nebo úplně offline, se zadáním kurzu ručně (žádné volání na ČNB):

```bash
./tools/losovani.py --kurz 24,315 --subjekty "Uskupení A" "Uskupení B" "Uskupení C"
```

Musí vám vyjít stejné pořadí jako nám. Když nevyjde, je to chyba nebo podvod —
a rádi bychom o tom věděli: [issue](https://github.com/kerray/r-brno/issues)
nebo modmail r/Brno.

Přepočítat to jde i bez tohoto skriptu, třemi řádky v čemkoliv, co má stejný
Mersenne Twister jako Python:

```python
import random
poradi = sorted(subjekty)
random.Random(24315).shuffle(poradi)
```

### Ukázka výstupu

```
========================================================================
LOSOVÁNÍ POŘADÍ AMA — r/Brno
========================================================================
Datum losování   : 09.09.2026
Zdroj náhody     : kurz ČNB EUR/CZK, denní kurzovní lístek
Zdrojová URL     : https://www.cnb.cz/.../denni_kurz.txt?date=09.09.2026
Řádek z ČNB      : EMU|euro|1|EUR|24,315
Kurz             : 24,315
Odvozený seed    : 24315   (kurz bez desetinné čárky)

Kanonicky setříděný vstup (sorted()):
   1. Uskupení A
   2. Uskupení B
   3. Uskupení C

VYLOSOVANÉ POŘADÍ:
   1. Uskupení C
   2. Uskupení A
   3. Uskupení B

Přepočítat: random.Random(seed).shuffle(sorted(subjekty))
========================================================================
```

### Poznámky

- ČNB vyhlašuje kurz jen v **pracovní dny**. Pro víkend nebo svátek lístek
  neexistuje a skript to řekne — losujeme tedy v pracovní den.
- Připomínky k metodě jsou nejužitečnější **dřív, než se podle ní losuje**:
  issue nebo pull request.
