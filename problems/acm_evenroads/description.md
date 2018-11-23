### Najkratšia cesta
Na vstupe dostanete neorientovaný ohodnotený graf. Vašou úlohou je nájsť dĺžku najkratšej cesty medzi vrcholmi $1$ a $n$, ktorá prejde po párnom počte ciest.

#### Vstup
Na prvom riadku vstupu sú dve čísla $n$ a $m$ ($1 \leq n,m \leq 10^5$) -- počet vrcholov a hrán v grafe. Vrcholy sú označené číslami $1$ až $n$.

Nasleduje $m$ riadkov, každý popisuje jednu hranu pomocou troch čísel $x_i$, $y_i$ a $w_i$ ($1 \leq x_i \neq y_i \leq n, 1 \leq w_i \leq 10\,000$) -- existuje hrana medzi vrhcolmi $x_i$ a $y_i$, ktorá má dĺžku $w_i$.

#### Výstup
Vypíšte dĺžku najkratšej cesty medzi vrcholmi 1 a $n$, ktorá prejde po párnom počte ciest.

##### Sample in
```
4 4
1 2 2
2 3 1
2 4 10
3 4 6
```

##### Sample out
```
12
```
