### Počítame
Poľská prefixová notácia je zápis aritemtických výrazov, ktorý nepotrebuje zátvorky. Vyznačuje sa tým, že najskôr píšeme operáciu až potom argumenty. Pri vyhodnocovaní takéhoto výrazu vždy nájdeme poslednú operáciu, aplikujeme ju na nasledujúce dve hodnoty a všetky tri slová nahradíme výsledkom. Toto opakujeme, až kým nevyhodnotíme celý výraz.

Ľahšie to možno demonštrovať na príkladoch:

  - `15` vyhodnotíme ako `15`
  - `+ 6 9` vyhodnotíme ako `6 + 9`
  - `+ * 2 3 9` vyhodnotíme ako `(2 * 3) + 9`
  - `+ 6 + 2 7` vyhodnotíme ako `6 + (2 + 7)`
  - `+ * 2 3 + 2 7` vyhodnotíme ako `(2 * 3) + (2 + 7)`
  - `+ * + 1 1 3 9` vyhodnotíme ako `((1 + 1) * 3) + 9`
  - `+ 9 * 3 + 1 1` vyhodnotíme ako `9 + (3 * (1 + 1))`

Pre jednoduchosť sa obmedzíme iba na násobenie (`*`) a sčítanie (`+`).

#### Vstup
Vstup obsahuje jeden riadok na ktorom je výraz v poľskej prefixovej notácii. Jednotlivé prvky tohto zápisu sú oddelené medzerou.

#### Výstup
Vypíšte výslednú hodnotu zadaného výrazu.

##### Sample in
```
* + 1 2 + 3 4
```

##### Sample out
```
21
```