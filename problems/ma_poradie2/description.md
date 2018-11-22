### Poradie 2
Žaba má permutáciu čísel $1$ až $n$. Ale namiesto toho aby vám prezradil akú permutáciu skrýva vám iba povedal niekoľko informácií o tom, ktoré číslo sa nachádza pred nejakým iným. Nájdite jednu možnú permutáciu, ktorú Žaba môže skrývať.

#### Vstup
Prvý riadok obsahuje dve medzerou oddelené čísla $n$ a $m$ ($1 \leq n,m \leq 10^6$) -- počet čísel permutácie a počet informácií, ktoré vám Žaba poskytol.

Nasleduje $m$ riadkov, každý z nich obsahuje dvojicu čísel $x_i$ a $y_i$ ($1 \leq x_i \neq y_i \leq n$), ktorá hovorí o tom, že číslo $x_i$ sa v permutácii nachádza niekde pred číslo $y_i$. Môžete predpokladať, že Žaba neklame a informácie, ktoré vám poskytne sú konzistentné s aspoň jednou permutáciou čísel $1$ až $n$.

#### Výstup
Na jeden riadok vypíšte medzerou oddelené čísla tvoriace Žabovu permutáciu. Ak existuje viacero možností, vypíšte ľubovoľnú z nich.

##### Sample in
```
5 4
5 2
4 1
2 4
3 1
```

##### Sample out
```
5 2 4 3 1
```
