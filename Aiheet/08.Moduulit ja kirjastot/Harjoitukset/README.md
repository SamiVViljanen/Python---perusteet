# Harjoitukset: Moduulit ja kirjastot

Tee seuraavat harjoitukset järjestyksessä. Jokaista harjoitusta varten on oma alakansio.

---

## Harjoitus 1: Math-moduulin käyttö (⭐ Helppo)

**Tavoite:** Harjoittele sisäänrakennetun `math`-moduulin käyttöä.

**Tehtävä:**
1. Tuo `math`-moduuli
2. Kysy käyttäjältä luku
3. Laske ja tulosta:
   - Neliöjuuri
   - Luvun neliö (käytä `math.pow()`)
   - Luku pyöristettynä ylös (`math.ceil()`)
   - Luku pyöristettynä alas (`math.floor()`)

**Esimerkki:**
```
Anna luku: 4.7
Neliöjuuri: 2.168
Neliö: 22.09
Pyöristys ylös: 5
Pyöristys alas: 4
```

💡 **Vinkki:** `import math` tulee tiedoston alkuun

📝 **Tiedosto:** [Harjoitus 1/](Harjoitus%201/) | [harjoitus1.py](Harjoitus%201/harjoitus1.py)

---

## Harjoitus 2: Random-moduuli ja arvauspeli (⭐⭐ Helppo)

**Tavoite:** Harjoittele `random`-moduulin käyttöä.

**Tehtävä:**
1. Tuo `random`-moduuli
2. Luo satunnainen luku 1-20 väliltä (`random.randint()`)
3. Kysy käyttäjältä arvausta
4. Kerro oliko arvaus oikein, liian pieni vai liian suuri
5. Toista kunnes käyttäjä arvaa oikein

**Esimerkki:**
```
Arvaa luku 1-20: 10
Liian pieni!
Arvaa luku 1-20: 15
Liian suuri!
Arvaa luku 1-20: 13
Oikein! Luku oli 13.
```

💡 **Vinkki:** `random.randint(1, 20)` antaa satunnaisen luvun

📝 **Tiedosto:** [Harjoitus 2/](Harjoitus%202/) | [harjoitus2.py](Harjoitus%202/harjoitus2.py)

---

## Harjoitus 3: Datetime ja ikälaskuri (⭐⭐ Keskitaso)

**Tavoite:** Harjoittele `datetime`-moduulin käyttöä.

**Tehtävä:**
1. Tuo `datetime`-moduuli
2. Kysy käyttäjältä syntymävuosi
3. Hae nykyinen vuosi (`datetime.date.today().year`)
4. Laske ja tulosta ikä
5. Tulosta myös täydellinen päivämäärä ja kellonaika (`datetime.datetime.now()`)

**Esimerkki:**
```
Anna syntymävuosi: 2000
Olet 25-vuotias.
Tänään on: 2025-12-13 14:30:25
```

💡 **Vinkit:**
- `datetime.date.today().year` antaa nykyisen vuoden
- `datetime.datetime.now()` antaa päivämäärän ja kellonajan

📝 **Tiedosto:** [Harjoitus 3/](Harjoitus%203/) | [harjoitus3.py](Harjoitus%203/harjoitus3.py)

---

## Harjoitus 4: Oma moduuli (⭐⭐⭐ Keskitaso)

**Tavoite:** Luo oma moduuli ja käytä sitä.

**Tehtävä:**
1. Luo tiedosto `geometria.py` joka sisältää:
   - Funktio `ympyrän_pinta_ala(säde)` joka palauttaa pinta-alan
   - Funktio `ympyrän_piiri(säde)` joka palauttaa piirin
   - Vakio `PI = 3.14159`
   
2. Luo toinen tiedosto `harjoitus4.py` joka:
   - Tuo `geometria`-moduulin
   - Kysyy käyttäjältä ympyrän säteen
   - Laskee ja tulostaa pinta-alan ja piirin

**Kaavat:**
- Pinta-ala = π × r²
- Piiri = 2 × π × r

**Esimerkki:**
```
Anna ympyrän säde: 5
Pinta-ala: 78.54
Piiri: 31.42
```

💡 **Vinkit:**
- Luo ensin `geometria.py` ja sitten `harjoitus4.py`
- Muista `import geometria`

📝 **Tiedostot:** 
- [Harjoitus 4/geometria.py](Harjoitus%204/geometria.py)
- [Harjoitus 4/harjoitus4.py](Harjoitus%204/harjoitus4.py)

---

## Harjoitus 5: Eri import-muodot (⭐⭐⭐⭐ Haaste)

**Tavoite:** Ymmärrä eri tapoja tuoda moduuleja.

**Tehtävä:**
Luo ohjelma joka käyttää kaikkia import-muotoja:

1. **Muoto 1:** `import math`
   - Laske neliöjuuri luvusta 16

2. **Muoto 2:** `from random import randint, choice`
   - Luo satunnainen luku 1-100
   - Valitse satunnainen väri listasta `["punainen", "sininen", "vihreä"]`

3. **Muoto 3:** `import datetime as dt`
   - Tulosta nykyinen päivämäärä

4. Tulosta kaikki tulokset selkeästi

**Esimerkki:**
```
Neliöjuuri 16:sta: 4.0
Satunnainen luku: 42
Satunnainen väri: sininen
Tänään: 2025-12-13
```

💡 **Vinkit:**
- Kaikki importit tulevat tiedoston alkuun
- Käytä oikeaa syntaksia jokaiselle muodolle
- `choice()` vaatii listan parametrina

📝 **Tiedosto:** [Harjoitus 5/](Harjoitus%205/) | [harjoitus5.py](Harjoitus%205/harjoitus5.py)

---

## Valmis?

Kun olet tehnyt harjoitukset, voit verrata vastauksiasi [Vastaukset](../Vastaukset/)-kansiossa oleviin mallivastauksiin.

💪 Muista: On täysin normaalia, että ratkaisusi näyttää erilaiselta kuin malliratkaisut. Tärkeintä on, että ohjelma toimii oikein!
