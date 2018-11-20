### 3k+1 (Collatz)
Majme číslo $k$. Ukážeme ho kamarátovi Collatzovi. Ak je $k$ párne, Collatz nám vráti $k/2$, inak nám vráti $3k+1$. Toto číslo prehlásime za nové $k$. Ukazujeme mu ho až kým nám nevráti $1$. Koľkokrát sme mu ho museli ukázať?

#### Vstup
Na prvom riadku vstupu je číslo $n$ ($n < 1000$), počet riadkov na vstupe. Nasleduje $n$ riadkov, na každom z nich je číslo $k$ ($0 < k \leq 100\,000$).

#### Výstup
Pre každý riadok vstupu vypíšte jedno číslo -- počet krokov, ktoré musí Collatz spraviť, aby z čísla $k$ vytvoril $1$.

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
