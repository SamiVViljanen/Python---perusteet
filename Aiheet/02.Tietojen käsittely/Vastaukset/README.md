# Vastaukset: Tietojen käsittely

Tässä kansiossa ovat malliratkaisut harjoitustehtäviin. Vertaa omia ratkaisujasi näihin, mutta muista:

✅ **Ratkaisusi voi olla erilainen ja silti oikein!**  
✅ **Tärkeintä on, että ohjelma toimii oikein**  
✅ **Muuttujien nimet voivat olla erilaiset**

---

## Harjoitus 1: Tietotyypin tunnistus

**Keskeiset oppipisteet:**
- `type()` palauttaa muuttujan tietotyypin
- Pythonin perustietotyypit: `str`, `int`, `float`, `bool`
- Tietotyyppi määräytyy automaattisesti arvon mukaan

**Muista:**
- Lainausmerkit → `str`
- Kokonaisluku → `int`
- Desimaaliluku → `float`
- True/False → `bool`

**Ratkaisu:** [harjoitus1.py](harjoitus1.py)

---

## Harjoitus 2: Tyypin muunnokset

**Keskeiset oppipisteet:**
- `input()` palauttaa **aina** merkkijonon
- `int()` muuntaa merkkijonon kokonaisluvuksi
- `float()` muuntaa liukuluvuksi
- Muunnos on välttämätön laskutoimituksille

**Vaihtoehtoinen ratkaisu:**
```python
# Voit yhdistää input ja muunnoksen:
ika = int(input("Anna ikäsi: "))
hinta = float(input("Anna tuotteen hinta: "))
```

**Ratkaisu:** [harjoitus2.py](harjoitus2.py)

---

## Harjoitus 3: Lukujen pyöristäminen

**Keskeiset oppipisteet:**
- `round(x)` pyöristää lähimpään kokonaislukuun
- `round(x, n)` pyöristää n desimaalin tarkkuudella
- `math.ceil()` pyöristää **aina** ylöspäin
- `math.floor()` pyöristää **aina** alaspäin
- Muista importata `import math`!

**Käytännön esimerkki:**
```python
import math

luku = 4.376
print(round(luku))      # 4 (lähin kokonaisluku)
print(round(luku, 2))   # 4.38 (kahteen desimaaliin)
print(math.ceil(luku))  # 5 (ylös)
print(math.floor(luku)) # 4 (alas)
```

**Ratkaisu:** [harjoitus3.py](harjoitus3.py)

---

## Harjoitus 4: Merkkijonojen viipalointi ja indeksointi

**Keskeiset oppipisteet:**
- `split('@')` jakaa merkkijonon listaksi annetun merkin kohdalta
- Indeksointi alkaa 0:sta: `teksti[0]` = ensimmäinen merkki
- Negatiivinen indeksi: `teksti[-1]` = viimeinen merkki
- Kääntäminen: `teksti[::-1]` (step = -1)

**Lisävinkkejä:**
```python
email = "matti@example.com"
osat = email.split('@')  # ['matti', 'example.com']
kayttaja = osat[0]       # 'matti'
domain = osat[1]         # 'example.com'

# Tai suoraan:
kayttaja, domain = email.split('@')
```

**Ratkaisu:** [harjoitus4.py](harjoitus4.py)

---

## Harjoitus 5: Tulosteen muotoilu f-stringillä

**Keskeiset oppipisteet:**
- F-string: `f"Teksti {muuttuja}"`
- Desimaalien muotoilu: `f"{luku:.2f}"` (2 desimaalia)
- Kokonaisluku: `f"{luku:.0f}"` (ei desimaaleja)
- F-stringit ovat selkein tapa yhdistää tekstiä ja muuttujia

**Muotoiluesimerkkejä:**
```python
luku = 63.456789
print(f"{luku}")       # 63.456789 (kaikki desimaalit)
print(f"{luku:.2f}")   # 63.46 (2 desimaalia)
print(f"{luku:.0f}")   # 63 (ei desimaaleja)
print(f"{luku:.4f}")   # 63.4568 (4 desimaalia)
```

**Ratkaisu:** [harjoitus5.py](harjoitus5.py)

---

## Harjoitus 6: Muuttujien roolit yhdistettynä

**Keskeiset oppipisteet:**
- **Gatherer**: Keräilee arvoja (esim. summa)
  - Alustetaan: `summa = 0`
  - Päivitetään: `summa += luku`
  
- **Most-recent holder**: Muistaa viimeisintä/parasta arvoa
  - Alustetaan ensimmäisellä arvolla: `suurin = luku1`
  - Vertaillaan ja päivitetään: `if luku > suurin: suurin = luku`
  
- **Transformation**: Muuntaa arvon toiseen muotoon
  - Esim. `f"{summa:.2f}"` muuntaa numeron muotoilluksi merkkijonoksi

**Vaihtoehtoisempi ratkaisu (ilman ehtolauseita):**
```python
# Huom: Tämä vaatii listojen tuntemusta (käsitellään myöhemmin)
luvut = [luku1, luku2, luku3, luku4, luku5]
suurin = max(luvut)
summa = sum(luvut)
```

> 💡 **Huom:** Tämä tehtävä on tarkoituksella haastavampi ja johdattelee silmukoiden käyttöön. Myöhemmin opimme tekemään tämän `for`-silmukalla!

**Ratkaisu:** [harjoitus6.py](harjoitus6.py)

---

## Seuraavat askeleet

Kun hallitset nämä harjoitukset:
1. ✅ Kokeile eri tyyppisiä syötteitä ja katso mitä tapahtuu
2. ✅ Yhdistele eri muotoilutapoja ja funktioita
3. ✅ Siirry seuraavaan lukuun: **Ehtolauseet**

Hienoa työtä! 🎉


➡️**Seuraavaksi:** [Aihe 03 - Ehtolauseet](../../03.Ehtolauseet/)