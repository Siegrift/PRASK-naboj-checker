### Stackovanie
Na začiatku dňa máme čísla $1$ až $n$ uložené v poradí jedno na druhom, pričom číslo 1 je najvyššie. Následne nastalo niekoľko zmien. Zmena $x_i$ spôsobila, že číslo $x_i$ sme presunuli na vrch kopy. Ako vyzerala kopa čísel na konci.

#### Vstup
Na prvom riadku vstupu sú dve medzerou oddelené čísla $n$ a $m$ ($1 \leq n, m \leq 10^5$) -- počet čísel v kope a počet zmien, ktoré sme spravili.

Na druhom riadku je $m$ medzerou oddelených čísel $x_1, x_2 \dots x_m$. $i$-te číslo popisuje $i$-tu zmenu, počas ktorej sme presunuli číslo $x_i$ na vrch kopy.

#### Výstup
Vypíšte $n$ medzerou oddelených čísel v poradí v akom sa nachádzali na kope po vykonaní všetkých zmien. Prvé číslo na výstupe je najvyššie číslo kopy.

##### Sample in
```
5 6
2 2 1 3 5 2
```

##### Sample out
```
2 5 1 3 4
```
