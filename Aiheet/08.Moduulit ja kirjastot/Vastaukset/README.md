# Vastaukset: Moduulit ja kirjastot

Tässä kansiossa on kaikkien harjoitusten mallivastaukset sekä selitykset.

---

## Harjoitus 1: Math-moduulin käyttö ⭐

### Ratkaisu
[harjoitus1.py](harjoitus1.py)

```python
import math

luku = float(input("Anna luku: "))

neliojuuri = math.sqrt(luku)
nelio = math.pow(luku, 2)
ylos = math.ceil(luku)
alas = math.floor(luku)

print(f"Neliöjuuri: {neliojuuri:.3f}")
print(f"Neliö: {nelio}")
print(f"Pyöristys ylös: {ylos}")
print(f"Pyöristys alas: {alas}")
```

### Selitys
- **import math:** Tuo math-moduulin käyttöön
- **math.sqrt():** Laskee neliöjuuren
- **math.pow(luku, 2):** Laskee potenssin (luku²)
- **math.ceil():** Pyöristää ylöspäin seuraavaan kokonaislukuun
- **math.floor():** Pyöristää alaspäin edelliseen kokonaislukuun

### Math-moduulin hyödyllisiä funktioita

| Funktio | Kuvaus | Esimerkki |
|---------|--------|-----------|
| `math.sqrt(x)` | Neliöjuuri | `math.sqrt(16)` → 4.0 |
| `math.pow(x, y)` | Potenssi x^y | `math.pow(2, 3)` → 8.0 |
| `math.ceil(x)` | Pyöristys ylös | `math.ceil(4.1)` → 5 |
| `math.floor(x)` | Pyöristys alas | `math.floor(4.9)` → 4 |
| `math.pi` | Piin arvo | `math.pi` → 3.14159... |
| `math.e` | Neperin luku | `math.e` → 2.71828... |
| `math.sin(x)` | Sini (radiaaneina) | `math.sin(math.pi/2)` → 1.0 |
| `math.cos(x)` | Kosini (radiaaneina) | `math.cos(0)` → 1.0 |

### Vaihtoehtoinen ratkaisu (neliö ilman math.pow)

```python
import math

luku = float(input("Anna luku: "))

neliojuuri = math.sqrt(luku)
nelio = luku ** 2  # Vaihtoehtoisesti ilman math.pow
ylos = math.ceil(luku)
alas = math.floor(luku)

print(f"Neliöjuuri: {neliojuuri:.3f}")
print(f"Neliö: {nelio}")
print(f"Pyöristys ylös: {ylos}")
print(f"Pyöristys alas: {alas}")
```

### Opittavaa
✅ `import moduuli` tuo moduulin käyttöön  
✅ Käytä `moduuli.funktio()` muotoa  
✅ Math-moduuli sisältää matemaattisia funktioita ja vakioita  
💡 Math-moduuli on osa Pythonin standardikirjastoa → ei tarvitse asentaa erikseen!

---

## Harjoitus 2: Random-moduuli ja arvauspeli ⭐⭐

### Ratkaisu
[harjoitus2.py](harjoitus2.py)

```python
import random

oikea_luku = random.randint(1, 20)

while True:
    arvaus = int(input("Arvaa luku 1-20: "))
    
    if arvaus == oikea_luku:
        print(f"Oikein! Luku oli {oikea_luku}.")
        break
    elif arvaus < oikea_luku:
        print("Liian pieni!")
    else:
        print("Liian suuri!")
```

### Selitys
- **random.randint(1, 20):** Luo satunnaisen kokonaisluvun väliltä 1-20 (molemmat mukana)
- **while True:** Ikuinen silmukka joka jatkuu kunnes `break`
- **break:** Lopettaa silmukan kun arvaus on oikein

### Random-moduulin hyödyllisiä funktioita

| Funktio | Kuvaus | Esimerkki |
|---------|--------|-----------|
| `random.randint(a, b)` | Satunnainen kokonaisluku väliltä a-b | `random.randint(1, 10)` → esim. 7 |
| `random.random()` | Satunnainen liukuluku väliltä 0-1 | `random.random()` → esim. 0.573 |
| `random.choice(lista)` | Satunnainen alkio listasta | `random.choice([1,2,3])` → esim. 2 |
| `random.shuffle(lista)` | Sekoittaa listan | `random.shuffle(kortit)` |
| `random.uniform(a, b)` | Satunnainen liukuluku väliltä a-b | `random.uniform(1.0, 5.0)` → esim. 3.2 |

### Vaihtoehtoinen ratkaisu (yrityskertojen laskuri)

```python
import random

oikea_luku = random.randint(1, 20)
yritykset = 0

while True:
    arvaus = int(input("Arvaa luku 1-20: "))
    yritykset += 1
    
    if arvaus == oikea_luku:
        print(f"Oikein! Luku oli {oikea_luku}.")
        print(f"Käytit {yritykset} arvausta.")
        break
    elif arvaus < oikea_luku:
        print("Liian pieni!")
    else:
        print("Liian suuri!")
```

### Opittavaa
✅ `random.randint(a, b)` luo satunnaisen kokonaisluvun  
✅ Random-moduuli on hyödyllinen peleissä ja simulaatioissa  
✅ `while True + break` on hyvä tapa tehdä "pelaa kunnes voitat" -silmukoita  
💡 Satunnaisuus on tärkeä osa ohjelmoinnissa (pelit, testaus, data-analyysi)!

---

## Harjoitus 3: Datetime ja ikälaskuri ⭐⭐

### Ratkaisu
[harjoitus3.py](harjoitus3.py)

```python
import datetime

syntymävuosi = int(input("Anna syntymävuosi: "))

nykyinen_vuosi = datetime.date.today().year

ikä = nykyinen_vuosi - syntymävuosi

print(f"Olet {ikä}-vuotias.")

nyt = datetime.datetime.now()
print(f"Tänään on: {nyt}")
```

### Selitys
- **datetime.date.today():** Palauttaa nykyisen päivämäärän
- **.year:** Hakee vuoden päivämäärästä
- **datetime.datetime.now():** Palauttaa nykyisen päivämäärän JA kellonajan

### Datetime-moduulin tärkeimmät osat

**1. date (päivämäärä):**
```python
import datetime

tanaan = datetime.date.today()
print(tanaan)           # 2025-12-13
print(tanaan.year)      # 2025
print(tanaan.month)     # 12
print(tanaan.day)       # 13
```

**2. datetime (päivämäärä + aika):**
```python
import datetime

nyt = datetime.datetime.now()
print(nyt)              # 2025-12-13 14:30:25.123456
print(nyt.hour)         # 14
print(nyt.minute)       # 30
print(nyt.second)       # 25
```

**3. Muotoilu (strftime):**
```python
import datetime

nyt = datetime.datetime.now()

# Muotoile päivämäärä
print(nyt.strftime("%d.%m.%Y"))           # 13.12.2025
print(nyt.strftime("%d/%m/%Y %H:%M"))     # 13/12/2025 14:30
print(nyt.strftime("%A, %d %B %Y"))       # Friday, 13 December 2025
```

### Muotoilukoodit (strftime)

| Koodi | Kuvaus | Esimerkki |
|-------|--------|-----------|
| `%d` | Päivä (01-31) | 13 |
| `%m` | Kuukausi (01-12) | 12 |
| `%Y` | Vuosi (4 numeroa) | 2025 |
| `%H` | Tunti (00-23) | 14 |
| `%M` | Minuutti (00-59) | 30 |
| `%S` | Sekunti (00-59) | 25 |
| `%A` | Viikonpäivä (kokonimi) | Friday |
| `%B` | Kuukausi (kokonimi) | December |

### Vaihtoehtoinen ratkaisu (tarkempi ikälaskuri)

```python
import datetime

syntymavuosi = int(input("Anna syntymävuosi: "))
syntymakuukausi = int(input("Anna syntymäkuukausi (1-12): "))
syntymapaiva = int(input("Anna syntymäpäivä (1-31): "))

tanaan = datetime.date.today()
syntyma = datetime.date(syntymavuosi, syntymakuukausi, syntymapaiva)

ika = tanaan.year - syntyma.year

# Vähennä 1 jos syntymäpäivä ei ole vielä ollut tänä vuonna
if (tanaan.month, tanaan.day) < (syntyma.month, syntyma.day):
    ika -= 1

print(f"Olet {ika}-vuotias.")
```

### Opittavaa
✅ `datetime.date.today()` antaa nykyisen päivämäärän  
✅ `datetime.datetime.now()` antaa päivämäärän JA kellonajan  
✅ `.year`, `.month`, `.day` hakevat yksittäisiä osia  
✅ `strftime()` muotoilee päivämäärän haluamallasi tavalla  
💡 Datetime on tärkeä moduuli kun työskentelet ajojen kanssa!

---

## Harjoitus 4: Oma moduuli ⭐⭐⭐

### Ratkaisu

**geometria.py:**
[geometria.py](geometria.py)

```python
PI = 3.14159

def ympyrän_pinta_ala(säde):
    return PI * säde ** 2

def ympyrän_piiri(säde):
    return 2 * PI * säde
```

**harjoitus4.py:**
[harjoitus4.py](harjoitus4.py)

```python
import geometria

säde = float(input("Anna ympyrän säde: "))

pinta_ala = geometria.ympyrän_pinta_ala(säde)
piiri = geometria.ympyrän_piiri(säde)

print(f"Pinta-ala: {pinta_ala:.2f}")
print(f"Piiri: {piiri:.2f}")
```

### Selitys
- **geometria.py:** Oma moduulitiedosto, sisältää funktioita ja vakioita
- **import geometria:** Tuo oman moduulin käyttöön
- **geometria.funktio():** Kutsuu moduulin funktiota

### Miten oma moduuli toimii?

**1. Luo tiedosto** (esim. `laskut.py`):
```python
# laskut.py
def summa(a, b):
    return a + b

def tulo(a, b):
    return a * b

PI = 3.14159
```

**2. Käytä toisessa tiedostossa:**
```python
# paaohjelma.py
import laskut

print(laskut.summa(5, 3))   # 8
print(laskut.tulo(4, 7))    # 28
print(laskut.PI)            # 3.14159
```

**Tärkeää:**
- Moduulitiedoston tulee olla **samassa kansiossa** tai Python-polulla
- Tiedostonimi **ilman .py-päätettä** on moduulin nimi
- Voit tuoda vain tietyt funktiot: `from laskut import summa`

### Eri tavat tuoda omaa moduulia

**Tapa 1: Tuo koko moduuli**
```python
import geometria

pinta_ala = geometria.ympyrän_pinta_ala(5)
```

**Tapa 2: Tuo vain tietyt funktiot**
```python
from geometria import ympyrän_pinta_ala, PI

pinta_ala = ympyrän_pinta_ala(5)  # Ei tarvitse geometria.-etuliitettä
print(PI)
```

**Tapa 3: Tuo lyhyemmällä nimellä**
```python
import geometria as geo

pinta_ala = geo.ympyrän_pinta_ala(5)
```

### Vaihtoehtoinen geometria.py (math.pi)

```python
import math

PI = math.pi  # Käytä math-moduulin tarkempaa pi-arvoa

def ympyrän_pinta_ala(säde):
    return PI * säde ** 2

def ympyrän_piiri(säde):
    return 2 * PI * säde

def ympyrän_halkaisija(säde):
    return 2 * säde

def ympyrän_sektori(säde, kulma):
    """Laske sektorin pinta-ala (kulma asteina)"""
    return (kulma / 360) * PI * säde ** 2
```

### Opittavaa
✅ Oma moduuli on vain Python-tiedosto samassa kansiossa  
✅ `import moduulinimi` tuo oman moduulin  
✅ Moduulit tekevät koodista uudelleenkäytettävää  
✅ Voit jakaa koodin loogisiin osiin (geometria, laskut, pelilogiikka jne.)  
💡 Isommissa projekteissa moduulit ovat välttämättömiä!

---

## Harjoitus 5: Eri import-muodot ⭐⭐⭐⭐

### Ratkaisu
[harjoitus5.py](harjoitus5.py)

```python
# 1. MUOTO 1: import math
import math

# 2. MUOTO 2: from random import randint, choice
from random import randint, choice

# 3. MUOTO 3: import datetime as dt
import datetime as dt

# 4. Laske neliöjuuri 16:sta (käytä math.sqrt)
neliojuuri = math.sqrt(16)

# 5. Luo satunnainen luku 1-100 (käytä randint)
satunnainen_luku = randint(1, 100)

# 6. Valitse satunnainen väri (käytä choice)
varit = ["punainen", "sininen", "vihreä"]
satunnainen_vari = choice(varit)

# 7. Hae tämän päivän päivämäärä (käytä dt.date.today)
tanaan = dt.date.today()

# 8. Tulosta kaikki tulokset
print(f"Neliöjuuri 16:sta: {neliojuuri}")
print(f"Satunnainen luku: {satunnainen_luku}")
print(f"Satunnainen väri: {satunnainen_vari}")
print(f"Tänään: {tanaan}")
```

### Selitys eri import-muodoista

**1. import moduuli**
```python
import math

# Käyttö: moduuli.funktio()
math.sqrt(16)
```
✅ Selkeä mistä funktio tulee  
✅ Ei nimiavaruuksien yhteentörmäyksiä  
⚠️ Pitää kirjoittaa `moduuli.` joka kerta

**2. from moduuli import funktio**
```python
from random import randint, choice

# Käyttö: funktio() suoraan
randint(1, 100)
choice(lista)
```
✅ Lyhyempi syntaksi  
✅ Tuo vain tarvittavat funktiot  
⚠️ Ei selvää mistä funktio tulee (jos ei ole tuttu)

**3. import moduuli as lyhenne**
```python
import datetime as dt

# Käyttö: lyhenne.funktio()
dt.date.today()
```
✅ Lyhyempi kirjoittaa  
✅ Yleisesti käytetyt lyhenteet (np, pd, plt)  
⚠️ Pitää muistaa mikä lyhenne on

**4. from moduuli import * (EI SUOSITELLA!)**
```python
from math import *

# Käyttö: funktio() suoraan
sqrt(16)
pi
```
❌ Ei selvää mistä funktio tulee  
❌ Voi ylikirjoittaa omia funktioita  
❌ Epäselvä koodi

### Milloin käytät mitäkin muotoa?

| Muoto | Käyttö | Esimerkki |
|-------|--------|-----------|
| `import moduuli` | Yleisin, suositellaan | `import math` |
| `from moduuli import x` | Kun tarvitset vain muutaman funktion | `from math import sqrt, pi` |
| `import moduuli as x` | Pitkät moduulinimet, vakiintuneet lyhenteet | `import numpy as np` |
| `from moduuli import *` | **Älä käytä!** | ❌ |

### Vakiintuneet lyhenteet (konventiot)

```python
import numpy as np           # NumPy
import pandas as pd          # Pandas
import matplotlib.pyplot as plt  # Matplotlib
import seaborn as sns        # Seaborn
```

Nämä ovat niin yleisiä että kaikki ohjelmoijat tunnistavat ne!

### Nimiavaruuksien yhteentörmäys -esimerkki

**Ongelma:**
```python
from math import *
from statistics import *

# Molemmat moduulit voivat sisältää saman funktion!
# Jälkimmäinen ylikirjoittaa ensimmäisen
```

**Ratkaisu:**
```python
import math
import statistics

math.sqrt(16)
statistics.mean([1, 2, 3])
```

### Opittavaa
✅ On useita tapoja tuoda moduuleja  
✅ `import moduuli` on turvallisin ja selkein  
✅ `from moduuli import funktio` sopii pienille määrille  
✅ `as lyhenne` on hyödyllinen pitkille nimille  
✅ Vältä `from moduuli import *`  
💡 Valitse import-muoto tilanteen mukaan!

---

## Yhteenveto: Import-muodot

### Perusmuodot

```python
# 1. Tuo koko moduuli
import math
print(math.sqrt(16))

# 2. Tuo tietyt funktiot
from random import randint, choice
print(randint(1, 10))

# 3. Tuo lyhyemmällä nimellä
import datetime as dt
print(dt.date.today())

# 4. EI SUOSITELLA
from math import *  # Tuo kaiken
print(sqrt(16))  # Ei selvää mistä sqrt tulee
```

### Hyvät käytännöt

**1. Importit tiedoston alkuun:**
```python
import math
import random
from datetime import datetime

# Sitten muu koodi...
```

**2. Järjestä importit:**
```python
# Ensin sisäänrakennetut
import math
import random

# Sitten ulkoiset kirjastot
import numpy as np

# Lopuksi omat moduulit
import geometria
```

**3. Käytä selkeitä nimiä:**
```python
# Hyvä
import datetime as dt

# Huono
import datetime as d  # Liian lyhyt, epäselvä
```

**4. Vältä import * -muotoa:**
```python
# Hyvä
from math import sqrt, pi

# Huono
from math import *
```

---

## Yleisiä virheitä

### 1. Unohdetaan import
❌ **VÄÄRIN:**
```python
print(math.sqrt(16))  # NameError: name 'math' is not defined
```

✅ **OIKEIN:**
```python
import math
print(math.sqrt(16))
```

### 2. Väärä syntaksi
❌ **VÄÄRIN:**
```python
import math
print(sqrt(16))  # NameError: name 'sqrt' is not defined
```

✅ **OIKEIN:**
```python
import math
print(math.sqrt(16))  # Tarvitaan math.-etuliite
```

TAI

```python
from math import sqrt
print(sqrt(16))  # Nyt sqrt on suoraan käytettävissä
```

### 3. Moduuli ei löydy
❌ **VÄÄRIN:**
```python
import geometria  # ModuleNotFoundError: No module named 'geometria'
```

✅ **OIKEIN:**
- Varmista että `geometria.py` on samassa kansiossa
- Tiedostonimi on oikein (isot/pienet kirjaimet!)
- Ei kirjoitusvirheitä

### 4. Ylikirjoitus
❌ **VÄÄRIN:**
```python
from math import sqrt

def sqrt(x):  # Ylikirjoittaa math.sqrt():n!
    return "Oma funktio"

print(sqrt(16))  # "Oma funktio" (EI 4.0!)
```

✅ **OIKEIN:**
```python
import math

def oma_sqrt(x):  # Eri nimi!
    return "Oma funktio"

print(math.sqrt(16))  # 4.0
print(oma_sqrt(16))   # "Oma funktio"
```

---

## Vinkkejä

💡 **Tutustu dokumentaatioon:** Pythonin virallinen dokumentaatio kertoo kaikki moduulin funktiot  
💡 **Kokeile interaktiivisesti:** Avaa Python-tulkki ja kokeile funktioita  
💡 **Käytä `help()`:** `help(math)` näyttää math-moduulin dokumentaation  
💡 **Lue muiden koodia:** Katso miten ammattilaiset käyttävät moduuleja  
💡 **Luo omia moduuleja:** Järjestä koodi loogisiin osiin

---

## Hyödyllisiä sisäänrakennettuja moduuleja

| Moduuli | Käyttötarkoitus | Esimerkkifunktioita |
|---------|-----------------|---------------------|
| `math` | Matematiikka | `sqrt`, `pow`, `sin`, `cos`, `pi` |
| `random` | Satunnaisuus | `randint`, `choice`, `shuffle` |
| `datetime` | Päivämäärät ja ajat | `date.today`, `datetime.now` |
| `os` | Käyttöjärjestelmä | `listdir`, `mkdir`, `remove` |
| `sys` | Järjestelmätiedot | `argv`, `exit`, `version` |
| `json` | JSON-tiedot | `dump`, `load`, `dumps`, `loads` |
| `re` | Säännölliset lausekkeet | `search`, `match`, `findall` |
| `time` | Aika ja viiveet | `sleep`, `time` |
| `collections` | Tietorakenteet | `Counter`, `defaultdict` |
| `itertools` | Iteraattorit | `combinations`, `permutations` |

---

Hienoa työtä! Olet nyt oppinut moduulien perusteet. 🎉

➡️**Seuraavaksi:** [Aihe 09 - Poikkeukset](../../09.Poikkeukset/)
