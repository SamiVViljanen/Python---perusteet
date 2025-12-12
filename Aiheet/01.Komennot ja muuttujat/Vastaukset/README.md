# Vastaukset: Komennot ja muuttujat

Tässä kansiossa ovat malliratkaisut harjoitustehtäviin. Vertaa omia ratkaisujasi näihin, mutta muista:

✅ **Ratkaisusi voi olla erilainen ja silti oikein!**  
✅ **Tärkeintä on, että ohjelma toimii oikein**  
✅ **Muuttujien nimet voivat olla erilaiset**

---

## Harjoitus 1: Tervehdys

**Keskeiset oppipisteet:**
- `input()` palauttaa aina merkkijonon
- F-string on kätevä tapa yhdistää tekstiä ja muuttujia
- Vaihtoehtoisesti voit käyttää: `print("Hei", nimi, "! Olet", ika, "vuotta vanha.")`

**Ratkaisu:** [harjoitus1.py](harjoitus1.py)

---

## Harjoitus 2: Lämpötilan muunnos

**Keskeiset oppipisteet:**
- `float()` muuntaa merkkijonon liukuluvuksi
- F-stringissä `:.1f` pyöristää yhteen desimaaliin
- Muista laskujärjestys: kertolasku ennen yhteenlaskua

**Vaihtoehtoinen ratkaisu:**
```python
# Voit myös laskea osissa:
fahrenheit = (celsius * 9 / 5) + 32
# tai
fahrenheit = celsius * 1.8 + 32
```

**Ratkaisu:** [harjoitus2.py](harjoitus2.py)

---

## Harjoitus 3: Ostoslaskuri

**Keskeiset oppipisteet:**
- `:.2f` pyöristää kahteen desimaaliin (rahamuoto)
- Voit tallentaa useita arvoja eri muuttujiin
- ALV lasketaan kertomalla yhteishinnalla (24% = 0.24)

**Vaihtoehtoinen ratkaisu:**
```python
# Voit myös laskea loppusumman suoraan:
loppusumma = yhteishinta * 1.24
```

**Ratkaisu:** [harjoitus3.py](harjoitus3.py)

---

## Harjoitus 4: Sekuntien muunnos

**Keskeiset oppipisteet:**
- `//` kokonaislukujako palauttaa kokonaisluvun
- `%` modulo-operaattori antaa jakojäännöksen
- Eteneminen suuremmasta pienempään: tunnit → minuutit → sekunnit

**Selitys askeleittain:**
```python
# Esimerkki: 3665 sekuntia
tunnit = 3665 // 3600          # 1 (kuinka monta kertaa 3600 mahtuu)
jaannos = 3665 % 3600          # 65 (jäljelle jää)
minuutit = 65 // 60            # 1 (kuinka monta kertaa 60 mahtuu)
sekunnit = 65 % 60             # 5 (lopulliset sekunnit)
```

**Ratkaisu:** [harjoitus4.py](harjoitus4.py)

---

## Harjoitus 5: BMI-laskuri

**Keskeiset oppipisteet:**
- `**` operaattori potenssilaskuun (pituus toiseen)
- Tyypin muunnos: `float()` desimaalilukujen käsittelyyn
- Yksikkömuunnos: cm → m jakamalla sadalla

**Lisätietoa BMI-arvoista:**
- Alle 18.5: Alipaino
- 18.5–24.9: Normaalipaino
- 25.0–29.9: Ylipaino
- 30.0 tai yli: Merkittävä ylipaino

> 🏆 Haaste: Voisitko lisätä ohjelmaan ehtolauseen, joka kertoo käyttäjälle hänen painoluokkansa?

**Ratkaisu:** [harjoitus5.py](harjoitus5.py)

---

## Seuraavat askeleet

Kun hallitset nämä harjoitukset:
1. ✅ Kokeile muuttaa tehtäviä (eri kaavat, yksiköt)
2. ✅ Yhdistele oppeja ja tee omat ohjelmasi
3. ✅ Siirry seuraavaan lukuun: **Ehtolauseet**

Hienoa työtä! 🎉
