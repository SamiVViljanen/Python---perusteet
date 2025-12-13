# Harjoitus 2: Tilastofunktiot ⭐⭐

## Tehtävänanto

Harjoittele NumPyn tilastofunktioita.

Sinulla on lämpötiladataa viikon ajalta (Celsius):  
`lampotilat = [15.5, 18.2, 16.8, 20.1, 19.5, 17.3, 21.0]`

Tee ohjelma, joka:
1. Luo NumPy-taulukon lämpötiloista
2. Laskee ja tulostaa:
   - Keskiarvon
   - Mediaanin
   - Keskihajonnan
   - Pienimmän ja suurimman arvon
3. Laskee kuinka monta päivää lämpötila oli yli 18 astetta
4. Tulostaa ne lämpötilat, jotka olivat yli 18 astetta

## Esimerkkitulostus

```
Lämpötilat: [15.5 18.2 16.8 20.1 19.5 17.3 21. ]
Keskiarvo: 18.34°C
Mediaani: 18.20°C
Keskihajonta: 1.97°C
Minimi: 15.50°C
Maksimi: 21.00°C
Yli 18°C päiviä: 4
Lämpimät päivät: [18.2 20.1 19.5 21. ]
```

## Vinkit

- Keskiarvo: `np.mean()`
- Mediaani: `np.median()`
- Keskihajonta: `np.std()`
- Minimi/maksimi: `np.min()`, `np.max()`
- Vertailu: `lampotilat > 18` luo boolean-taulukon
- Suodatus: `lampotilat[lampotilat > 18]`
- Lukumäärä: `np.sum(lampotilat > 18)` tai `len(suodatettu)`

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus2.py](harjoitus2.py)
