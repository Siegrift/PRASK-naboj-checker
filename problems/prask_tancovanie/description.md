### Poradie
Žaba má permutáciu čísel $1$ až $n$. Ale namiesto toho aby vám prezradil akú permutáciu skrýva, vám iba o $n-1$ číslach povedal, ktoré číslo je v permutácii priamo pred ním. Zistite akú permutáciu Žaba skrýva.

#### Vstup
Prvý riadok obsahuje číslo $n$ ($1 \leq n \leq 10^6$) -- počet čísel permutácie.

Nasleduje $n-1$ riadkov, každý z nich obsahuje dvojicu čísel $x_i$ a $y_i$ ($1 \leq x_i, y_i \leq n$), ktorá hovorí o tom, že pred číslom $x_i$ sa v permutácii nachádza číslo $y_i$. Môžete predpokladať, že všetky $x_i$ sú navzájom rôzne.

#### Výstup
Na jeden riadok vypíšte medzerou oddelené čísla tvoriace Žabovu permutáciu.

##### Sample in
```
5
5 2
4 3
2 4
3 1
```

##### Sample out
```
1 3 4 2 5
```
