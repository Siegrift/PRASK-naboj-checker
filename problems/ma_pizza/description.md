### Pizza
Máme $n$ pízz, každú na samostatnom tanieri a každá je rozkrájaná na $n$ trojuholníkov. Chceli by sme tieto trojuholníky popresúvať tak, aby na každom taniery bol práve jeden kúsok každej pizze. Jediné čo vieme je presunúť trojuholník z jedného taniera na voľné miesto na inom taniery. To by nám však samozrejme neumožňovalo spraviť žiadnu operáciu (keďže taniere sú na začiatku plné), preto máme ešte jeden malý pomocný tanierik, na ktorý sa zmestí jeden kúsok pizze a na začiatku je prázdny.

Nájdite jedno možné riešenie, ktoré využije najmenší počet presunov.

Taniere aj pizze si očíslujeme číslami $1$ až $n$, pričom platí, že na taniery $i$ je na začiatku pizza $i$. Pomocný tanierik mám číslo $0$.

#### Vstup
Na vstupe je jedno celé číslo $n$ ($1 \leq n \leq 500$) -- počet pízz.

#### Výstup
Vypíšte niekoľko riadkov, každý popisuje jedno presunutie, počet použitých presunutí je najmenší možný. Každý riadok výstupu obsahuje tri celé čísla $t_1$, $t_2$ a $p$ a znamená, že pizzu $p$ presunieme z taniera $t_1$ na tanier $t_2$.

##### Sample in
```
2
```

##### Sample out
```
1 0 1
2 1 2
0 2 1
```
