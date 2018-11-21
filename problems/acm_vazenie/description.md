### Váženie

Na váženie na trhoch v King's Landingu sa používajú rovnoramenné váhy a sada $n$ závaží, ktoré sú očíslované od 1 po $n$ a majú postupne výhy $1, 3, 9 \dots 3^{n-1}$ (teda závažie s číslo $i$ má váhu $3^{i-1}$). Na ľavej miske váh je predmet s hmotnosťou $k$. Ktoré závažia musíte umiestniť na ľavú a pravú misku váh aby ste ich vyvážili?

#### Vstup
Vstup obsahuje dve medzerou oddelené čísla $n$ ($1 \leq n \leq 40$) a $k$ ($1 \leq k \leq 10^{18}$) -- počet závaži a váha predmetu.

#### Výstup
Ak neexistuje rozloženie závaží, ktoré by váhu vyvážilo na jediný riadok výstupu vypíšte `-1`.

Ak také rozloženie existuje vypíšte dva riadky. Na prvom riadku sú medzerami oddelené čísla závaží, ktoré je treba dať na ľavú misku váh. Na druhom riadku sú medzerami oddelné čísla závaží, ktoré je treba dať na pravú misku váh.

##### Sample in
```
6 47
```

##### Sample out
```
1 3 4
2 5
```
