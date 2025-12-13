# Harjoitus 1: NumPy-taulukon perusteet ⭐

## Tehtävänanto

Tutustu NumPy-taulukoihin ja niiden perusoperaatioihin.

Tee ohjelma, joka:
1. Luo NumPy-taulukon luvuista `[10, 20, 30, 40, 50]`
2. Tulostaa taulukon
3. Tulostaa taulukon ensimmäisen ja viimeisen alkion
4. Kertoo kaikki alkiot kahdella
5. Luo toisen taulukon luvuista `[1, 2, 3, 4, 5]`
6. Laskee taulukoiden summan yhteen (alkio kerrallaan)
7. Tulostaa tuloksen

## Esimerkkitulostus

```
Alkuperäinen taulukko: [10 20 30 40 50]
Ensimmäinen: 10
Viimeinen: 50
Kerrottuna kahdella: [ 20  40  60  80 100]
Toinen taulukko: [1 2 3 4 5]
Summa: [ 11  22  33  44  55]
```

## Vinkit

- Tarvitset: `import numpy as np`
- Luo taulukko: `np.array([...])`
- Indeksointi toimii kuten listoissa: `taulukko[0]`, `taulukko[-1]`
- Aritmetiikka toimii kaikille alkioille: `taulukko * 2`
- Taulukoiden yhteenlasku: `taulukko1 + taulukko2`

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus1.py](harjoitus1.py)
