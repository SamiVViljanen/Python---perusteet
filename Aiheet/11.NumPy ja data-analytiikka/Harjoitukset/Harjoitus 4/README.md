# Harjoitus 4: Datan analysointi ⭐⭐⭐

## Tehtävänanto

Analysoi opiskelijoiden arvosanoja NumPyn avulla.

Sinulla on 5 opiskelijan arvosanat 3 kurssilla (rivit = opiskelijat, sarakkeet = kurssit):

```
arvosanat = [
    [4, 5, 3],  # Opiskelija 1
    [5, 5, 4],  # Opiskelija 2
    [2, 3, 3],  # Opiskelija 3
    [4, 4, 5],  # Opiskelija 4
    [3, 4, 4]   # Opiskelija 5
]
```

Tee ohjelma, joka:
1. Luo NumPy-taulukon arvosanoista
2. Laskee jokaisen opiskelijan keskiarvon (rivien keskiarvot)
3. Laskee jokaisen kurssin keskiarvon (sarakkeiden keskiarvot)
4. Etsii parhaan opiskelijan (paras keskiarvo)
5. Etsii vaikeimman kurssin (alhaisin keskiarvo)
6. Laskee kuinka moni opiskelija sai vähintään yhden 5:n
7. Laskee kokonaiskeskiarvon kaikista arvosanoista

## Esimerkkitulostus

```
Arvosanat:
[[4 5 3]
 [5 5 4]
 [2 3 3]
 [4 4 5]
 [3 4 4]]

Opiskelijoiden keskiarvot: [4.00 4.67 2.67 4.33 3.67]
Kurssien keskiarvot: [3.60 4.20 3.80]

Paras opiskelija: 2 (keskiarvo: 4.67)
Vaikein kurssi: 1 (keskiarvo: 3.60)
Opiskelijoita joilla vähintään yksi 5: 3
Kokonaiskeskiarvo: 3.87
```

## Vinkit

- Rivien keskiarvot: `np.mean(arvosanat, axis=1)`
- Sarakkeiden keskiarvot: `np.mean(arvosanat, axis=0)`
- axis=0 → sarakkeet, axis=1 → rivit
- Suurin arvo: `np.max()` tai `np.argmax()` (indeksi)
- Pienin arvo: `np.min()` tai `np.argmin()` (indeksi)
- Vertailu: `arvosanat == 5` → boolean-taulukko
- Rivillä on 5: `np.any(arvosanat == 5, axis=1)`

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus4.py](harjoitus4.py)
