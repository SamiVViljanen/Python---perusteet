# Moduulit ja kirjastot

## Sisällysluettelo
1. [Mikä on moduuli ja kirjasto?](#mikä-on-moduuli-ja-kirjasto)
2. [Sisäänrakennettujen moduulien käyttö](#sisäänrakennettujen-moduulien-käyttö)
3. [Eri tapoja tuoda moduuleja](#eri-tapoja-tuoda-moduuleja)
4. [Omien moduulien luominen](#omien-moduulien-luominen)
5. [Nimiavaruuksien yhteentörmäykset](#nimiavaruuksien-yhteentörmäykset)
6. [Hyviä käytäntöjä](#hyviä-käytäntöjä)
7. [Yhteenveto](#yhteenveto)

---

Tässä oppaassa opit, mitä Pythonin moduulit ja kirjastot ovat, miten niitä käytetään ja miten voit luoda omia moduuleja.

## Mikä on moduuli ja kirjasto?

**Moduuli** on yksinkertaisesti Python-tiedosto, joka sisältää funktioita, luokkia ja muuttujia. Moduulit auttavat organisoimaan koodia ja välttämään toistoa.

**Kirjasto** (library) on laajempi kokoelma moduuleja, jotka toimivat yhdessä. Esimerkiksi `numpy` on kirjasto, joka sisältää useita moduuleja tieteelliseen laskentaan.

**Miksi käytämme moduuleja?**
- Vältetään saman koodin kirjoittaminen uudelleen
- Koodi on paremmin organisoitu
- Voidaan käyttää muiden kirjoittamia valmiita työkaluja
- Projekti pysyy selkeämpänä ja helpommin ylläpidettävänä

## Sisäänrakennettujen moduulien käyttö

Python sisältää paljon valmiita moduuleja, joita voit käyttää heti. Tässä kolme yleisintä:

### math-moduuli

`math`-moduuli sisältää matemaattisia funktioita ja vakioita:

```python
import math

# Neliöjuuri
print(math.sqrt(16))  # 4.0

# Piin arvo
print(math.pi)  # 3.141592653589793

# Pyöristys ylös/alas
print(math.ceil(4.3))   # 5
print(math.floor(4.7))  # 4

# Potenssi
print(math.pow(2, 3))  # 8.0
```

### random-moduuli

`random`-moduuli tuottaa satunnaislukuja ja tekee satunnaisia valintoja:

```python
import random

# Satunnainen kokonaisluku väliltä 1-10
print(random.randint(1, 10))  # esim. 7

# Satunnainen liukuluku väliltä 0-1
print(random.random())  # esim. 0.573241

# Satunnainen valinta listasta
hedelmät = ["omena", "banaani", "appelsiini"]
print(random.choice(hedelmät))  # esim. "banaani"

# Sekoita lista
kortit = [1, 2, 3, 4, 5]
random.shuffle(kortit)
print(kortit)  # esim. [3, 1, 5, 2, 4]
```

### datetime-moduuli

`datetime`-moduuli käsittelee päivämääriä ja aikoja:

```python
import datetime

# Nykyinen päivämäärä ja aika
nyt = datetime.datetime.now()
print(nyt)  # esim. 2025-11-09 14:30:25.123456

# Vain päivämäärä
tänään = datetime.date.today()
print(tänään)  # esim. 2025-11-09

# Päivämäärän osat
print(f"Vuosi: {tänään.year}")     # 2025
print(f"Kuukausi: {tänään.month}") # 11
print(f"Päivä: {tänään.day}")      # 9

# Päivämäärän muotoilu
muotoiltu = nyt.strftime("%d.%m.%Y %H:%M")
print(muotoiltu)  # esim. 09.11.2025 14:30
```

## Eri tapoja tuoda moduuleja

Pythonissa on useita tapoja tuoda (import) moduuleja. Jokainen tapa sopii eri tilanteisiin.

### 1. import moduuli

Perusmuoto - tuo koko moduulin:

```python
import math

tulos = math.sqrt(25)
print(tulos)  # 5.0
```

**Huom:** Käytettävä muotoa `moduuli.funktio()`

### 2. from moduuli import funktio

Tuo vain tietyn funktion tai vakion:

```python
from math import sqrt, pi

print(sqrt(25))  # 5.0
print(pi)        # 3.141592653589793
```

**Huom:** Nyt voit käyttää funktiota suoraan ilman `math.`-etuliitettä.

### 3. from moduuli import *

Tuo kaikki moduulin sisältö:

```python
from math import *

print(sqrt(25))  # 5.0
print(pi)        # 3.141592653589793
print(cos(0))    # 1.0
```

**Varoitus:** Tätä tapaa **ei suositella**, koska se voi aiheuttaa nimiavaruuksien yhteentörmäyksiä!

### 4. import moduuli as lyhenne

Anna moduulille lyhyempi nimi:

```python
import datetime as dt

nyt = dt.datetime.now()
print(nyt)
```

Tämä on hyödyllistä, kun moduulin nimi on pitkä tai kun haluat käyttää yleisiä lyhenteitä (esim. `numpy as np`, `pandas as pd`).

## Omien moduulien luominen

Voit luoda omat moduulit - se on helppoa!

### Esimerkki: Luo moduuli `laskut.py`

```python
# laskut.py

def summa(a, b):
    """Laskee kahden luvun summan"""
    return a + b

def tulo(a, b):
    """Laskee kahden luvun tulon"""
    return a * b

def neliö(x):
    """Laskee luvun neliön"""
    return x ** 2

# Vakio
PI = 3.14159
```

### Käytä omaa moduulia toisessa tiedostossa

```python
# pääohjelma.py

import laskut

print(laskut.summa(5, 3))    # 8
print(laskut.tulo(4, 7))     # 28
print(laskut.neliö(5))       # 25
print(laskut.PI)             # 3.14159
```

### Tai tuo vain tietyt funktiot

```python
# pääohjelma.py

from laskut import summa, neliö

print(summa(10, 20))  # 30
print(neliö(6))       # 36
```

**Tärkeää:** 
- Moduulitiedoston tulee olla samassa kansiossa tai Python-polulla
- Tiedostonimi ilman `.py`-päätettä on moduulin nimi

## Nimiavaruuksien yhteentörmäykset

**Nimiavaruus** (namespace) tarkoittaa aluetta, jossa nimet (muuttujat, funktiot) ovat määriteltyjä.

### Mitä on yhteentörmäys?

Yhteentörmäys tapahtuu, kun kaksi eri asiaa saa saman nimen:

```python
from math import *

# Oma funktio nimeltä sqrt
def sqrt(x):
    return "Oma funktio"

print(sqrt(16))  # Mikä sqrt käytetään?
```

Nyt `math`-moduulin `sqrt`-funktio **ylikirjoitetaan** omalla funktiolla! Tämä voi aiheuttaa odottamattomia virheitä.

### Kuinka välttää yhteentörmäykset?

**1. Käytä `import moduuli` -muotoa:**

```python
import math

def sqrt(x):
    return "Oma funktio"

print(math.sqrt(16))  # 4.0 (math-moduulin funktio)
print(sqrt(16))       # "Oma funktio" (oma funktio)
```

**2. Tuo vain tarvitsemasi funktiot:**

```python
from math import pi, cos

# Ei konfliktia sqrt:n kanssa
def sqrt(x):
    return "Oma funktio"

print(sqrt(16))  # "Oma funktio"
print(pi)        # 3.141592653589793
```

**3. Vältä `from moduuli import *` -muotoa:**

Tämä tuo kaiken, jolloin et tiedä, mitkä nimet ovat käytössä.

### Esimerkki ongelmasta

```python
from math import *
from random import *

# Molemmat moduulit voivat sisältää samoja nimiä
# Jälkimmäinen ylikirjoittaa ensimmäisen!
```

## Hyviä käytäntöjä

1. **Käytä `import moduuli` -muotoa yleisesti:**
   ```python
   import math
   import random
   ```

2. **Tuo vain tarvitsemasi funktiot:**
   ```python
   from datetime import datetime, timedelta
   ```

3. **Älä käytä `import *` -muotoa:**
   - Tekee koodista epäselvää
   - Voi aiheuttaa nimiavaruuksien yhteentörmäyksiä

4. **Käytä yleisiä lyhenteitä:**
   ```python
   import datetime as dt
   import numpy as np     # jos käytät NumPy-kirjastoa
   import pandas as pd    # jos käytät Pandas-kirjastoa
   ```

5. **Järjestä importit:**
   ```python
   # Ensin sisäänrakennetut moduulit
   import math
   import random
   
   # Sitten ulkoiset kirjastot
   import numpy as np
   
   # Lopuksi omat moduulit
   import laskut
   ```

6. **Dokumentoi omat moduulit:**
   ```python
   # laskut.py
   """
   Tämä moduuli sisältää yksinkertaisia laskutoimituksia.
   """
   
   def summa(a, b):
       """Laskee kahden luvun summan"""
       return a + b
   ```

## Yhteenveto

### Mitä opimme?

- **Moduuli** on Python-tiedosto, joka sisältää funktioita ja muuttujia
- **Kirjasto** on laajempi kokoelma moduuleja
- Python sisältää paljon valmiita moduuleja: `math`, `random`, `datetime` jne.
- Voit **luoda omia moduuleja** tallentamalla koodin `.py`-tiedostoon
- On **eri tapoja tuoda** moduuleja: `import`, `from...import`, `import...as`
- **Nimiavaruuksien yhteentörmäykset** voivat aiheuttaa ongelmia
- Vältä `from moduuli import *` -muotoa

### Ero import-muodoissa

| Muoto | Käyttö | Suositus |
|-------|--------|----------|
| `import math` | `math.sqrt(25)` | ✅ Suositellaan |
| `from math import sqrt` | `sqrt(25)` | ✅ OK pienelle määrälle |
| `from math import *` | `sqrt(25)` | ❌ Vältä |
| `import math as m` | `m.sqrt(25)` | ✅ OK, varsinkin pitkille nimille |

### Muista

Moduulit tekevät ohjelmistasi:
- **Järjestelmällisemmän** - koodi on loogisesti jaettu
- **Uudelleenkäytettävämmän** - voit käyttää samaa koodia monessa projektissa
- **Helpomman ylläpitää** - muutokset on helppo tehdä yhteen paikkaan

Jos tarvitset samaa koodia useassa paikassa, luo siitä moduuli!
