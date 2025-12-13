# Vastaukset: For-silmukka

Tässä kansiossa ovat malliratkaisut harjoitustehtäviin. Vertaa omia ratkaisujasi näihin, mutta muista:

✅ **Ratkaisusi voi olla erilainen ja silti oikein!**  
✅ **Tärkeintä on, että ohjelma toimii oikein**  
✅ **Muuttujien nimet voivat olla erilaiset**

---

## Harjoitus 1: Tulosta numerot 1-10

**Keskeiset oppipisteet:**
- `range(1, 11)` tuottaa luvut 1-10 (huom: 11 ei sisälly!)
- For-silmukka käy läpi kaikki arvot automaattisesti
- Muuttuja `i` saa uuden arvon joka kierroksella

**Range-funktion perusteet:**
```python
range(5)        # 0, 1, 2, 3, 4 (oletuksena alkaa 0:sta)
range(1, 6)     # 1, 2, 3, 4, 5 (alusta 1, loppuun 6, ei sisälly)
range(1, 11)    # 1, 2, 3, ..., 10
```

**Ratkaisu:** [harjoitus1.py](harjoitus1.py)

---

## Harjoitus 2: Parilliset luvut

**Keskeiset oppipisteet:**
- `range()` ottaa kolme parametria: `range(start, stop, step)`
- `step=2` tarkoittaa että otetaan joka toinen arvo
- Tämä on tehokkaampi kuin tarkistaa joka luvun parillisuutta

**Step-parametrin käyttö:**
```python
range(0, 21, 2)   # 0, 2, 4, 6, ..., 20 (joka toinen)
range(1, 10, 2)   # 1, 3, 5, 7, 9 (parittomat)
range(10, 0, -1)  # 10, 9, 8, ..., 1 (takaperin)
range(0, 10, 3)   # 0, 3, 6, 9 (joka kolmas)
```

**Vaihtoehtoinen ratkaisu (ilman step-parametria):**
```python
for i in range(11):  # 0-10
    if i % 2 == 0:
        print(i * 2)  # 0, 2, 4, 6, ..., 20
```

**Ratkaisu:** [harjoitus2.py](harjoitus2.py)

---

## Harjoitus 3: Listan läpikäynti

**Keskeiset oppipisteet:**
- `enumerate()` palauttaa sekä indeksin että alkion
- Indeksointi alkaa 0:sta, joten lisää 1 näyttääksesi "1. omena"
- Voit purkaa tuple:n suoraan for-lauseessa

**Enumerate-esimerkkejä:**
```python
hedelmät = ["omena", "banaani", "appelsiini"]

# Enumerate antaa (indeksi, arvo) -parit
for i, hedelmä in enumerate(hedelmät):
    print(i, hedelmä)
# 0 omena
# 1 banaani
# 2 appelsiini

# Aloita indeksointi 1:stä
for i, hedelmä in enumerate(hedelmät, start=1):
    print(f"{i}. {hedelmä}")
# 1. omena
# 2. banaani
# 3. appelsiini
```

**Vaihtoehtoinen ratkaisu (ilman enumerate):**
```python
hedelmät = ["omena", "banaani", "appelsiini", "päärynä"]
for i in range(len(hedelmät)):
    print(f"{i + 1}. {hedelmät[i]}")
```

**Ratkaisu:** [harjoitus3.py](harjoitus3.py)

---

## Harjoitus 4: Summan laskeminen

**Keskeiset oppipisteet:**
- **Gatherer-rooli**: muuttuja joka keräilee arvoja
- Alusta ennen silmukkaa: `summa = 0`
- Päivitä silmukassa: `summa += i`

**Gatherer-malli:**
```python
# 1. Alusta keräilijä
summa = 0

# 2. Käy läpi arvot
for i in range(1, 101):
    # 3. Päivitä keräilijää
    summa += i  # sama kuin: summa = summa + i

# 4. Käytä lopullista arvoa
print(summa)
```

**Matemaattinen fakta:**
- Lukujen 1-100 summa = 5050
- Kaava: n * (n + 1) / 2, missä n = 100
- 100 * 101 / 2 = 5050

**Pythonin valmis funktio:**
```python
print(sum(range(1, 101)))  # 5050
```

**Ratkaisu:** [harjoitus4.py](harjoitus4.py)

---

## Harjoitus 5: Kertotaulu

**Keskeiset oppipisteet:**
- For-silmukka sopii erinomaisesti toistoihin käytännön laskuissa
- F-string tekee tulosteen muotoilusta helppoa
- Voit laskea ja tallentaa arvon muuttujaan ennen tulostusta

**Kertotaulun rakenne:**
```python
luku = 5
for i in range(1, 11):
    tulos = luku * i
    print(f"{luku} x {i} = {tulos}")
```

**Kompaktimpi versio:**
```python
luku = 5
for i in range(1, 11):
    print(f"{luku} x {i} = {luku * i}")
```

**Bonushaaste: Tulosta kaikki kertotaulut 1-10:**
```python
for luku in range(1, 11):
    print(f"\nKertotaulu {luku}:")
    for i in range(1, 11):
        print(f"{luku} x {i} = {luku * i}")
```

**Ratkaisu:** [harjoitus5.py](harjoitus5.py)

---

## Harjoitus 6: FizzBuzz

**Keskeiset oppipisteet:**
- Klassinen ohjelmointitehtävä (usein käytetty haastatteluissa!)
- **Järjestys on kriittinen**: tarkista ensin molemmat ehdot
- Yhdistää for-silmukan ja ehtolauseet

**Miksi järjestys on tärkeä?**
```python
# OIKEIN - tarkista ensin molemmat
if i % 3 == 0 and i % 5 == 0:  # 15, 30, 45, ...
    print("FizzBuzz")
elif i % 3 == 0:                # 3, 6, 9, 12, ... (ei 15!)
    print("Fizz")
elif i % 5 == 0:                # 5, 10, 20, ... (ei 15!)
    print("Buzz")

# VÄÄRIN - luku 15 menee "Fizz":ksi!
if i % 3 == 0:       # 15 täyttää tämän ehdon ensimmäisenä!
    print("Fizz")    # 15 → "Fizz" ❌
elif i % 5 == 0:
    print("Buzz")
```

**Vaihtoehtoiset ratkaisut:**

**Ratkaisu 1: Käytä modulo 15**
```python
for i in range(1, 31):
    if i % 15 == 0:      # Sama kuin: i % 3 == 0 and i % 5 == 0
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

**Ratkaisu 2: Rakenna merkkijono**
```python
for i in range(1, 31):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output if output else i)
```

**Miksi FizzBuzz on tärkeä?**
- Testaa peruslogiikan ymmärrystä
- Opettaa ehtojen järjestyksen merkityksen
- Yhdistää useita käsitteitä

**Ratkaisu:** [harjoitus6.py](harjoitus6.py)

---

## Yhteenveto: For-silmukan vinkit

### 1. Range-funktion muodot
```python
range(stop)              # 0 ... stop-1
range(start, stop)       # start ... stop-1
range(start, stop, step) # start ... stop-1, askeleella step
```

### 2. Listan läpikäynti
```python
# Pelkkä alkio
for hedelmä in hedelmät:
    print(hedelmä)

# Alkio + indeksi
for i, hedelmä in enumerate(hedelmät):
    print(i, hedelmä)

# Indeksin kautta
for i in range(len(hedelmät)):
    print(hedelmät[i])
```

### 3. Yleisiä kuvioita

**Gatherer (keräilijä):**
```python
summa = 0
for i in range(1, 11):
    summa += i
```

**Transformation (muunnos):**
```python
for i in range(5):
    print(i * 2)  # Muunna arvo ennen käyttöä
```

**Filter (suodatin):**
```python
for i in range(10):
    if i % 2 == 0:  # Suodata vain tietyt arvot
        print(i)
```

### 4. Break ja Continue
```python
# Break - lopeta silmukka
for i in range(10):
    if i == 5:
        break  # Pysähtyy kun i=5
    print(i)   # 0, 1, 2, 3, 4

# Continue - ohita loppuosa
for i in range(5):
    if i == 2:
        continue  # Ohita i=2
    print(i)      # 0, 1, 3, 4
```

---

## Seuraavat askeleet

Kun hallitset nämä harjoitukset:
1. ✅ Kokeile sisäkkäisiä for-silmukoita (nested loops)
2. ✅ Yhdistele for-silmukoita listojen kanssa
3. ✅ Siirry seuraavaan lukuun: **While-silmukat**

Hienoa työtä! 🎉


➡️**Seuraavaksi:** [Aihe 05 - While-silmukka](../../05.While-silmukka/)