# PRASK-naboj-checker

Vytvori odovzdavatko na informaticky naboj. Ucastnici vedia copy-pastnut svoj output do odovzdavatka
a ten im vypluje heslo, ktore vedia odniest opravovatelom...  
_(Pozor: output sa matchuje uplne, cize zalezi aj na prazdnych riadkoch resp newline za poslednym riadkom),
nezalezi vsak na type konca riadku_

Cela appka funguje offline a (uz) funguje aj multiplatformovo... Ak chcete appku preniest na ine pocitace
skopirujte subory `index.html`, `style.css`, `words.js`, `main.js` a `sha256.js`...

## Vytvorenie a spustenie stranky

v subore `main.js` najdete premennu problem list, do nej treba ulozit vygenerovane (zahashovane)
data o ulohach. Stranku potom staci spustit otvorenim `index.html` v prehliadaci.

## Vytvorenie dat

V adresari `problems` najdete mnoho suborov a podadresarov. Kazdy podadresar obsahuje jednu ulohu.
Kazda uloha sa sklada zo 4 casti (vstupny subor, zadanie, generator, solver)... V adresari `template`
najdete maketu...

Popis ostatnych suborov:

- **order.txt** - mena adresarov uloh, v poradi v akom maju byt v odovzdavatku...
  Sem treba napisat vsetky ulohy ktore sa maju vygenerovat.
- **generate-pdf.py** - vygeneruje pdf so zadaniami uloh v `order.txt` (potrebujete `pandoc`)
- **generate.py** - vygeneruje vstupy a vystuy pre kazdu ulohu, a vypluje
  zahashovane spravne vysledky uloh (**tento vystup treba nakopirovat do premennej `problemList` v `main.js`**)
- **test_all.py** - otestuje vsetky ulohy
- **hashToJs.py** - zahashuje ulohy do formatu aky ocakava `main.js`. Jednotlivym uloham v `order.txt`
  zodpovedaju jednotlive slova v premennej `corr`.

## Ak nieco nefunguje

Ak nieco nefunguje tak je to pravdepodobne moja chyba :D. Mozete mi dat vediet a skusim sa nato pozriet...
