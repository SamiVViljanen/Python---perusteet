# Harjoitus 1: Binäärihaku ⭐⭐

## Tehtävänanto

Toteuta binäärihaku-algoritmi, joka etsii luvun järjestetystä listasta.

**Binäärihaun idea:**
1. Tarkista keskimmäinen alkio
2. Jos etsittävä on pienempi, etsi vasemmalta puolelta
3. Jos etsittävä on suurempi, etsi oikealta puolelta
4. Toista kunnes löytyy tai hakualue loppuu

Tee ohjelma, joka:
1. Luo järjestetyn listan: `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]`
2. Toteuttaa binäärihaun funktiolla `binaarihaku(lista, etsittava)`
3. Etsii luvun 13 listasta
4. Etsii luvun 8 listasta (jota ei ole)
5. Tulostaa löydetyn indeksin tai -1 jos ei löydy

## Esimerkkitulostus

```
Lista: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

Etsitään: 13
Löytyi indeksistä: 6

Etsitään: 8
Ei löytynyt (-1)
```

## Vinkit

- Käytä muuttujia: `vasen`, `oikea`, `keski`
- `vasen = 0`, `oikea = len(lista) - 1`
- Keskikohta: `keski = (vasen + oikea) // 2`
- While-silmukka: `while vasen <= oikea:`
- Jos `lista[keski] == etsittava` → palauta `keski`
- Jos `lista[keski] < etsittava` → `vasen = keski + 1`
- Jos `lista[keski] > etsittava` → `oikea = keski - 1`

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus1.py](harjoitus1.py)
