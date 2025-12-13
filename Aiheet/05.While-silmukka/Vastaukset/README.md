# Vastaukset: While-silmukka

Tässä kansiossa on kaikkien harjoitusten mallivastaukset sekä selitykset.

---

## Harjoitus 1: Laskuri 1-5 ⭐

### Ratkaisu
[harjoitus1.py](harjoitus1.py)

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### Selitys
- **Laskuri:** Muuttuja `i` toimii laskurina, joka alkaa arvosta 1
- **Ehto:** Silmukka jatkuu niin kauan kuin `i <= 5` (eli 1, 2, 3, 4, 5)
- **Kasvatus:** `i += 1` kasvattaa laskuria joka kierroksella
- **Vaara:** Jos unohdat `i += 1`, syntyy ikuinen silmukka!

### Opittavaa
✅ While-silmukan perusrakenne  
✅ Laskurimuuttujan käyttö  
✅ Ehdon tärkeys (milloin silmukka loppuu)  
⚠️ Muista aina kasvattaa laskuria, muuten tulee ikuinen silmukka!

---

## Harjoitus 2: Salasanan tarkistus ⭐⭐

### Ratkaisu
[harjoitus2.py](harjoitus2.py)

```python
oikea_salasana = "python123"

salasana = input("Anna salasana: ")

while salasana != oikea_salasana:
    salasana = input("Anna salasana: ")

print("Kirjautuminen onnistui!")
```

### Selitys
- **Ensimmäinen kysely:** Salasana kysytään **ennen** silmukkaa
- **Ehto:** `while salasana != oikea_salasana` tarkistaa, onko salasana väärin
- **Toisto:** Jos salasana on väärin, kysytään uudelleen
- **Lopetus:** Kun salasana on oikein, ehto muuttuu epätodeksi → silmukka loppuu

### Yleinen virhe
❌ **VÄÄRIN:**
```python
while salasana != oikea_salasana:
    salasana = input("Anna salasana: ")
```
Jos salasanaa ei kysy ENNEN silmukkaa, `salasana` ei ole määritelty → virhe!

### Vaihtoehtoinen ratkaisu (while True)
```python
while True:
    salasana = input("Anna salasana: ")
    if salasana == oikea_salasana:
        print("Kirjautuminen onnistui!")
        break
```
Tämä on yhtä hyvä! `break` lopettaa silmukan heti kun salasana on oikein.

### Opittavaa
✅ Muuttujan arvo pitää kysyä ENNEN silmukkaa  
✅ While-silmukka käyttäjän syötteen kanssa  
✅ Ehto vertaa käyttäjän syötettä oikeaan arvoon  
💡 Kaksi tapaa: `while ehto` tai `while True + break`

---

## Harjoitus 3: Valikko break-komennolla ⭐⭐

### Ratkaisu
[harjoitus3.py](harjoitus3.py)

```python
while True:
    print("1. Sano hei")
    print("2. Sano moi")
    print("0. Lopeta")
    
    valinta = int(input("Valintasi: "))
    
    if valinta == 1:
        print("Hei!")
    elif valinta == 2:
        print("Moi!")
    elif valinta == 0:
        print("Näkemiin!")
        break
    
    print()
```

### Selitys
- **while True:** Luo ikuisen silmukan (ei ehtoa, aina tosi)
- **break:** Ainut tapa lopettaa `while True` -silmukka
- **Rakenne:** Valikko → syöte → toiminto → (break tai jatka)
- **Tyhjä rivi:** `print()` lisää tyhjän rivin valikkojen väliin

### Opittavaa
✅ `while True` luo ikuisen silmukan  
✅ `break` lopettaa silmukan välittömästi  
✅ Hyvä tapa tehdä valikoita ja menuja  
💡 `while True + break` on usein selkeämpi kuin monimutkainen ehto

### Vaihtoehtoinen ratkaisu (ilman break)
```python
valinta = -1  # Alustus, ei 0

while valinta != 0:
    print("1. Sano hei")
    print("2. Sano moi")
    print("0. Lopeta")
    valinta = int(input("Valintasi: "))
    
    if valinta == 1:
        print("Hei!")
    elif valinta == 2:
        print("Moi!")
    elif valinta == 0:
        print("Näkemiin!")
```
Tämäkin toimii, mutta `while True + break` on selkeämpi!

---

## Harjoitus 4: Arvauspeli ⭐⭐⭐

### Ratkaisu
[harjoitus4.py](harjoitus4.py)

```python
oikea_luku = 7
yritykset = 0

arvaus = int(input("Arvaa luku (1-10): "))
yritykset += 1

while arvaus != oikea_luku:
    if arvaus < oikea_luku:
        print("Liian pieni!")
    else:
        print("Liian suuri!")
    
    arvaus = int(input("Arvaa luku (1-10): "))
    yritykset += 1

print(f"Oikein! Käytit {yritykset} arvausta.")
```

### Selitys
- **Laskuri:** `yritykset` pitää kirjaa arvausten määrästä
- **Ensimmäinen kysely:** Arvaus kysytään ennen silmukkaa
- **Palaute:** `if-else` antaa vihjeen (liian pieni/suuri)
- **Ehto:** Silmukka jatkuu niin kauan kuin `arvaus != oikea_luku`

### Tärkeää
⚠️ Laskuria pitää kasvattaa **kahdessa** paikassa:
1. Ennen silmukkaa (ensimmäinen arvaus)
2. Silmukan lopussa (seuraavat arvaukset)

### Vaihtoehtoinen ratkaisu (while True)
```python
oikea_luku = 7
yritykset = 0

while True:
    arvaus = int(input("Arvaa luku (1-10): "))
    yritykset += 1
    
    if arvaus == oikea_luku:
        print(f"Oikein! Käytit {yritykset} arvausta.")
        break
    elif arvaus < oikea_luku:
        print("Liian pieni!")
    else:
        print("Liian suuri!")
```
Tässä laskuria kasvatetaan vain **yhdessä** paikassa → vähemmän virheitä!

### Opittavaa
✅ Laskurin käyttö (gatherer-rooli)  
✅ While-silmukka + ehtolauseet yhdessä  
✅ Palaute käyttäjälle silmukan sisällä  
💡 `while True + break` voi olla selkeämpi kuin `while ehto`

---

## Harjoitus 5: Positiivisten lukujen summa ⭐⭐⭐⭐

### Ratkaisu
[harjoitus5.py](harjoitus5.py)

```python
summa = 0
maara = 0

luku = int(input("Anna luku: "))

while luku > 0:
    summa += luku
    maara += 1
    luku = int(input("Anna luku: "))

print(f"Syötit {maara} positiivista lukua.")
print(f"Summa: {summa}")
```

### Selitys
- **Kaksi laskuria:**
  - `summa` = kaikkien lukujen summa (gatherer)
  - `maara` = montako lukua syötettiin (counter)
- **Ensimmäinen kysely:** Luku kysytään ennen silmukkaa
- **Ehto:** `while luku > 0` jatkaa niin kauan kuin luku on positiivinen
- **Lopetus:** Kun käyttäjä syöttää 0 tai negatiivisen, silmukka loppuu

### Gatherer-rooli
```python
summa += luku  # Sama kuin: summa = summa + luku
```
- Aluksi `summa = 0`
- Jos käyttäjä syöttää 5: `summa = 0 + 5 = 5`
- Jos käyttäjä syöttää 10: `summa = 5 + 10 = 15`
- Jos käyttäjä syöttää 3: `summa = 15 + 3 = 18`

### Vaihtoehtoinen ratkaisu (while True)
```python
summa = 0
maara = 0

while True:
    luku = int(input("Anna luku: "))
    
    if luku <= 0:
        break
    
    summa += luku
    maara += 1

print(f"Syötit {maara} positiivista lukua.")
print(f"Summa: {summa}")
```
Tässä tarkistus on **ennen** laskurien kasvattamista → 0 tai negatiivinen ei lisätä summaan.

### Opittavaa
✅ Kaksi laskuria samassa silmukassa  
✅ Gatherer-rooli: `summa += luku`  
✅ Counter-rooli: `maara += 1`  
✅ While-silmukan ehto päättää milloin lopetetaan  
💡 Tämä on yleinen kaava: kerää dataa kunnes tulee lopetusarvo

---

## Yhteenveto: While vs For

### Milloin käytät while-silmukkaa?
✅ Kun **et tiedä** montako kierrosta tarvitaan  
✅ Kun lopetusehto riippuu **käyttäjän syötteestä**  
✅ Kun haluat **ikuisen silmukan** (`while True`)  
✅ Kun haluat **tarkastaa ehdon** joka kierroksen alussa

**Esimerkit:**
- Salasanan kysely (kunnes oikein)
- Pelin pääsilmukka (kunnes pelaaja lopettaa)
- Datan lukeminen (kunnes tiedosto loppuu)

### Milloin käytät for-silmukkaa?
✅ Kun **tiedät** montako kierrosta tarvitaan  
✅ Kun käyt läpi **listan, merkkijonon tai range():n**  
✅ Kun haluat **iteroida tietyn määrän**

**Esimerkit:**
- Tulosta luvut 1-10
- Käy läpi lista
- Toista 5 kertaa

---

## Yleisiä virheitä

### 1. Ikuinen silmukka (ei kasvata laskuria)
❌ **VÄÄRIN:**
```python
i = 1
while i <= 5:
    print(i)
    # Unohti i += 1 → ikuinen silmukka!
```

### 2. Muuttujaa ei määritelty ennen silmukkaa
❌ **VÄÄRIN:**
```python
while salasana != "python":  # NameError: salasana ei ole määritelty
    salasana = input("Anna salasana: ")
```

✅ **OIKEIN:**
```python
salasana = input("Anna salasana: ")  # Kysy ensin!
while salasana != "python":
    salasana = input("Anna salasana: ")
```

### 3. Laskuri vain yhdessä paikassa
❌ **VÄÄRIN:**
```python
arvaus = int(input("Arvaa: "))
# Ei kasvateta yrityksiä!

while arvaus != 7:
    arvaus = int(input("Arvaa: "))
    yritykset += 1  # Kasvatetaan vain täällä

print(f"Käytit {yritykset} arvausta")  # Puuttuu ensimmäinen!
```

✅ **OIKEIN:**
```python
arvaus = int(input("Arvaa: "))
yritykset = 1  # Ensimmäinen arvaus lasketaan!

while arvaus != 7:
    arvaus = int(input("Arvaa: "))
    yritykset += 1
```

---

## Vinkkejä

💡 **Testi-input:** Kun testaat, syötä erilaisia arvoja (oikein, väärin, rajatapaukset)  
💡 **Print-debuggaus:** Tulosta muuttujien arvot silmukan sisällä, jos jotain menee pieleen  
💡 **Pieni askel:** Testaa ensin yksinkertainen silmukka, lisää sitten ehtolauseet  
💡 **Kommentit:** Kirjoita kommentit ENNEN koodia – auttaa suunnittelussa!

---

Hienoa työtä! Olet nyt oppinut while-silmukoiden perusteet. 🎉

**Seuraavaksi:** Aihe 06 - Funktioiden määrittäminen
