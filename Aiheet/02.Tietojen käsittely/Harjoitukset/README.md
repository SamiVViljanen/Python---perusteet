# Harjoitukset: Tietojen käsittely

Tee seuraavat harjoitukset järjestyksessä. Jokaista harjoitusta varten on oma tiedosto.

---

## Harjoitus 1: Tietotyypin tunnistus (⭐ Helppo)

**Tavoite:** Harjoittele Pythonin perustietotyyppejä ja `type()`-funktiota.

**Tehtävä:**
1. Luo muuttujia seuraaville arvoille: "Python", 42, 3.14, True
2. Tulosta jokaisen muuttujan tyyppi `type()`-funktion avulla

**Esimerkki:**
```python
Python
42
3.14
True
```

**Tulostuksen tulisi näyttää:**
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

💡 **Vinkki:** `type()` palauttaa muuttujan tietotyypin.

📝 **Tiedosto:** [Harjoitus 1/](Harjoitus%201/) | [harjoitus1.py](Harjoitus%201/harjoitus1.py)

---

## Harjoitus 2: Tyypin muunnokset (⭐⭐ Helppo)

**Tavoite:** Harjoittele tietotyyppien muunnoksia `int()`, `float()` ja `str()`.

**Tehtävä:**
1. Kysy käyttäjältä ikä ja tallenna merkkijonona
2. Muunna ikä kokonaisluvuksi ja tulosta ikä kuukausina (ikä * 12)
3. Kysy käyttäjältä tuotteen hinta merkkijonona
4. Muunna liukuluvuksi ja kerro 2 (esim. oston määrä)
5. Tulosta tulokset

**Esimerkki:**
```
Anna ikäsi: 25
Olet 300 kuukautta vanha!
Anna tuotteen hinta: 19.99
Kahden tuotteen hinta: 39.98€
```

💡 **Vinkki:** `input()` palauttaa aina merkkijonon, joten muunnokset ovat välttämättömiä.

📝 **Tiedosto:** [Harjoitus 2/](Harjoitus%202/) |  [harjoitus2.py](Harjoitus%202/harjoitus2.py)

---

## Harjoitus 3: Lukujen pyöristäminen (⭐⭐ Keskitaso)

**Tavoite:** Harjoittele `round()`-funktiota ja `math.ceil()`/`math.floor()`.

**Tehtävä:**
1. Kysy käyttäjältä tuotteen hinta (float)
2. Pyöristä hinta lähimpään kokonaislukuun ja tulosta
3. Pyöristä hinta ylöspäin ja alaspäin
4. Pyöristä hinta kahden desimaalin tarkkuudella

**Esimerkki:**
```
Anna tuotteen hinta: 4.376
Pyöristetty: 4
Ylös: 5
Alas: 4
Kahden desimaalin tarkkuudella: 4.38
```

💡 **Vinkit:**
- `round(luku)` pyöristää lähimpään kokonaislukuun
- `round(luku, 2)` pyöristää kahteen desimaaliin
- `math.ceil()` pyöristää ylös, `math.floor()` pyöristää alas

📝 **Tiedosto:** [Harjoitus 3/](Harjoitus%203/) | [harjoitus3.py](Harjoitus%203/harjoitus3.py)

---

## Harjoitus 4: Merkkijonojen viipalointi ja indeksointi (⭐⭐⭐ Keskitaso)

**Tavoite:** Harjoittele merkkijonojen indeksointia ja viipalointia.

**Tehtävä:**
1. Kysy käyttäjältä sähköpostiosoite
2. Tulosta käyttäjätunnus (ennen @) ja domain (jälkeen @)
3. Tulosta merkkijonon ensimmäinen ja viimeinen merkki
4. Tulosta merkkijono käänteisenä

**Esimerkki:**
```
Anna sähköpostiosoitteesi: matti@example.com
Käyttäjä: matti
Domain: example.com
Ensimmäinen merkki: m
Viimeinen merkki: m
Käänteinen: moc.elpmaxe@ittam
```

💡 **Vinkit:**
- `split('@')` jakaa merkkijonon osiin
- `teksti[0]` antaa ensimmäisen merkin
- `teksti[-1]` antaa viimeisen merkin
- `teksti[::-1]` kääntää merkkijonon

📝 **Tiedosto:** [Harjoitus 4/](Harjoitus%204/) | [harjoitus4.py](Harjoitus%204/harjoitus4.py)

---

## Harjoitus 5: Tulosteen muotoilu f-stringillä (⭐⭐⭐ Keskitaso)

**Tavoite:** Harjoittele f-stringejä ja muotoilua.

**Tehtävä:**
1. Kysy käyttäjältä nimi, ikä ja paino
2. Tulosta lause muodossa: `Nimi: [nimi], Ikä: [ikä] vuotta, Paino: [paino] kg`
3. Tulosta lisäksi ikä kuukausina ja paino pyöristettynä kahteen desimaaliin
4. Käytä f-stringejä ja muotoilua

**Esimerkki:**
```
Anna nimesi: Anna
Anna ikäsi: 30
Anna painosi (kg): 63.456
Nimi: Anna, Ikä: 30 vuotta, Paino: 63.456 kg
Ikä kuukausina: 360
Paino pyöristettynä: 63.46 kg
```

💡 **Vinkit:**
- F-string: `f"Teksti {muuttuja}"`
- Muotoilu: `f"{luku:.2f}"` kahden desimaalin tarkkuudella
- `f"{luku:.0f}"` kokonaisluvuksi

📝 **Tiedosto:** [Harjoitus 5/](Harjoitus%205/) | [harjoitus5.py](Harjoitus%205/harjoitus5.py)

---

## Harjoitus 6: Muuttujien roolit yhdistettynä (⭐⭐⭐⭐ Haaste)

**Tavoite:** Käytä `gatherer`, `transformation` ja `most_recent_holder` muuttujia.

**Tehtävä:**
1. Kysy käyttäjältä viisi lukua yksi kerrallaan
2. Tallenna suurin luku (most-recent holder)
3. Laske lukujen summa (gatherer)
4. Muunna summa desimaaliksi kahden desimaalin tarkkuudella (transformation)
5. Tulosta tulokset

**Esimerkki:**
```
Anna luku 1: 10
Anna luku 2: 5
Anna luku 3: 20
Anna luku 4: 7
Anna luku 5: 3
Suurin luku: 20
Summa: 45.00
```

💡 **Vinkit:**
- Gatherer: `summa = 0`, sitten `summa += luku`
- Most-recent holder: `suurin = luku1`, sitten vertaa `if luku > suurin:`
- Transformation: `f"{summa:.2f}"`

📝 **Tiedosto:** [Harjoitus 6/](Harjoitus%206/) | [harjoitus6.py](Harjoitus%206/harjoitus6.py)

---

## Valmis?

Kun olet tehnyt harjoitukset, voit verrata vastauksiasi [Vastaukset](../Vastaukset/)-kansiossa oleviin mallivastauksiin.

💪 Muista: On täysin normaalia, että ratkaisusi näyttää erilaiselta kuin malliratkaisut. Tärkeintä on, että ohjelma toimii oikein!