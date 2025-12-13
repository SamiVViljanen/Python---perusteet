# Vastaukset: Ehtolauseet

Tässä kansiossa ovat malliratkaisut harjoitustehtäviin. Vertaa omia ratkaisujasi näihin, mutta muista:

✅ **Ratkaisusi voi olla erilainen ja silti oikein!**  
✅ **Tärkeintä on, että ohjelma toimii oikein**  
✅ **Muuttujien nimet voivat olla erilaiset**

---

## Harjoitus 1: Ikärajan tarkistus

**Keskeiset oppipisteet:**
- `if-else`-rakenne on ehtolauseiden perusrakenne
- Vertailuoperaattori `>=` (suurempi tai yhtä suuri)
- Vain toinen lohko suoritetaan (joko `if` TAI `else`)

**Muista:**
- `if` suoritetaan kun ehto on `True`
- `else` suoritetaan kun ehto on `False`
- Sisennys on tärkeä! (4 välilyöntiä tai 1 tab)

**Ratkaisu:** [harjoitus1.py](harjoitus1.py)

---

## Harjoitus 2: Arvosanan määrittäminen

**Keskeiset oppipisteet:**
- `elif` mahdollistaa useita vaihtoehtoja
- **Järjestys on tärkeä!** Aloita suurimmasta/korkeimmasta
- Ensimmäinen tosi ehto voittaa, loput ohitetaan

**Miksi järjestys on tärkeä?**
```python
# OIKEIN - aloita suurimmasta
if pisteet >= 90:
    print("Kiitettävä")
elif pisteet >= 80:  # Tänne tullaan vain jos < 90
    print("Hyvä")

# VÄÄRIN - kaikki yli 60 menee "Välttäväksi"
if pisteet >= 60:
    print("Välttävä")  # 95 pistettä → "Välttävä"!
elif pisteet >= 90:
    print("Kiitettävä")  # Tänne ei koskaan tulla
```

**Ratkaisu:** [harjoitus2.py](harjoitus2.py)

---

## Harjoitus 3: Parillinen vai pariton?

**Keskeiset oppipisteet:**
- Modulo-operaattori `%` antaa jakojäännöksen
- Parillinen luku: jakojäännös 0, kun jaetaan 2:lla
- Pariton luku: jakojäännös 1, kun jaetaan 2:lla

**Modulo-esimerkkejä:**
```python
print(8 % 2)   # 0 (8 jaettuna 2:lla, ei jäännöstä)
print(7 % 2)   # 1 (7 jaettuna 2:lla, jää 1)
print(10 % 3)  # 1 (10 jaettuna 3:lla = 3 täyttä, jää 1)
print(15 % 4)  # 3 (15 jaettuna 4:lla = 3 täyttä, jää 3)
```

**Vaihtoehtoinen ratkaisu:**
```python
# Voit myös käyttää != vertailua
if luku % 2 != 0:
    print(f"Luku {luku} on pariton")
else:
    print(f"Luku {luku} on parillinen")
```

**Ratkaisu:** [harjoitus3.py](harjoitus3.py)

---

## Harjoitus 4: Lämpötilan luokittelu

**Keskeiset oppipisteet:**
- Useampi `elif` samassa rakenteessa
- Väliarvot: esim. 15-25 tarkoittaa `>= 15 and < 25`
- Kun aloitat suurimmasta, riittää `>=` tarkistus

**Miksi yksinkertainen vertailu riittää?**
```python
# Kun aloitetaan suurimmasta:
if lampotila > 25:        # Yli 25
    # ...
elif lampotila >= 15:     # 15-25 (koska < 25 on jo varmaa!)
    # ...
elif lampotila >= 5:      # 5-14 (koska < 15 on jo varmaa!)
    # ...

# Jos aloitettaisiin pienimmästä, tarvittaisiin AND:
if lampotila < -5:
    # ...
elif lampotila >= -5 and lampotila < 5:  # Monimutkaisempaa!
    # ...
```

**Ratkaisu:** [harjoitus4.py](harjoitus4.py)

---

## Harjoitus 5: Kirjautuminen

**Keskeiset oppipisteet:**
- `and`-operaattori: molemmat ehdot täytyy olla totta
- Voit yhdistää useita vertailuja samaan ehtoon
- Järjestelmällinen lähestyminen: tarkista kaikki yhdistelmät

**Totuustaulukko:**
```
Käyttäjätunnus | Salasana | Tulos
---------------|----------|------------------
Oikein         | Oikein   | Kirjautuminen OK
Oikein         | Väärin   | Salasana väärin
Väärin         | Oikein   | Tunnus väärin
Väärin         | Väärin   | Molemmat väärin
```

**Vaihtoehtoinen ratkaisu (sisäkkäiset if-lauseet):**
```python
if tunnus == oikea_tunnus:
    if salasana == oikea_salasana:
        print("Kirjautuminen onnistui!")
    else:
        print("Salasana on väärin")
else:
    if salasana == oikea_salasana:
        print("Käyttäjätunnus on väärin")
    else:
        print("Sekä käyttäjätunnus että salasana ovat väärin")
```

**Lyhyempi ratkaisu (ei kaikilla viesteillä):**
```python
if tunnus == oikea_tunnus and salasana == oikea_salasana:
    print("Kirjautuminen onnistui!")
else:
    print("Virheellinen käyttäjätunnus tai salasana")
```

**Ratkaisu:** [harjoitus5.py](harjoitus5.py)

---

## Yhteenveto: Ehtolauseiden vinkit

### 1. Sisennys on pakollinen
```python
# OIKEIN
if ehto:
    print("Tämä kuuluu if-lohkoon")
    print("Tämäkin")

# VÄÄRIN - ei sisennystä
if ehto:
print("Virhe!")  # IndentationError
```

### 2. Muista kaksoispisteen (:)
```python
# OIKEIN
if ehto:
    print("OK")

# VÄÄRIN - puuttuu kaksoispisteen
if ehto
    print("Virhe!")  # SyntaxError
```

### 3. Käytä == vertailuun, = sijoitukseen
```python
# OIKEIN
if ika == 18:  # Vertailu
    print("Täsmälleen 18")

# VÄÄRIN
if ika = 18:   # Sijoitus ei toimi if-lauseessa!
    print("Virhe!")
```

### 4. Loogisten operaattoreiden järjestys
- `not` (ensin)
- `and` (sitten)
- `or` (viimeksi)

```python
# Nämä ovat erilaiset:
if not x and y:     # (not x) and y
if not (x and y):   # not (x and y)
```

---

## Seuraavat askeleet

Kun hallitset nämä harjoitukset:
1. ✅ Kokeile eri syötteitä ja reuna-arvoja (0, -1, 100)
2. ✅ Yhdistele ehtolauseita monimutkaisempiin ohjelmiin
3. ✅ Siirry seuraavaan lukuun: **For-silmukat**

Hienoa työtä! 🎉

➡️**Seuraavaksi:** [Aihe 04 - For-silmukka](../../04.For-silmukka/)