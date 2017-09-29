### 3k+1 (Collatz)
Majme číslo k. Ukážeme ho kamarátovi Collatzovi. Ak je **k** párne, Collatz nám vráti **k / 2**, inak nám vráti **3k+1**. Toto číslo prehlásime za nové k. Ukazujeme mu ho až kým nám nevráti **1**. Zaujíma nás koľko krát mu to číslo
musíme ukázať.

#### Vstup
Na prvom riadku vstupu je číslo **n**, počet riadkov na vstupe *(n < 1000)*. Nasleduje **n** riadkov, na každom z nich je číslo **k**, (0 < k <= 100 000).

#### Výstup
Pre každý riadok vstupu vypíšte jedno číslo, počet krokov, kým sa z čísla **k** nestane **1**.

##### Sample in
```
3
8
15
37
```

##### Sample out
```
3
17
21
```
