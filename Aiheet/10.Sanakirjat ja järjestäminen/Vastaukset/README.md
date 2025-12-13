# Vastaukset: Sanakirjat ja järjestäminen

Tässä kansiossa on kaikkien harjoitusten mallivastaukset sekä selitykset.

---

## Harjoitus 1: Perus sanakirja ⭐

### Ratkaisu
[harjoitus1.py](harjoitus1.py)

```python
# Luo sanakirja 5 henkilöllä
henkilöt = {
    "Anna": 25,
    "Pekka": 30,
    "Liisa": 28,
    "Matti": 35,
    "Kaisa": 22
}

# Tulosta koko sanakirja
print("Kaikki henkilöt:")
print(henkilöt)

# Hae yhden henkilön ikä
print(f"\nAnnan ikä: {henkilöt['Anna']}")

# Lisää uusi henkilö
print("\nLisätään uusi henkilö...")
henkilöt["Ville"] = 27

# Tulosta päivitetty sanakirja
print("\nPäivitetyt henkilöt:")
print(henkilöt)
```

### Selitys
- **Sanakirjan luominen:** `{avain: arvo, avain: arvo}`
- **Hakeminen:** `henkilöt["Anna"]` palauttaa 25
- **Lisääminen:** `henkilöt["Ville"] = 27` lisää uuden avain-arvo-parin
- **Tulostus:** `print(henkilöt)` tulostaa koko sanakirjan

### Sanakirjan perusoperaatiot

| Operaatio | Syntaksi | Esimerkki |
|-----------|----------|-----------|
| Luo tyhjä | `{}` tai `dict()` | `henkilöt = {}` |
| Luo arvoilla | `{avain: arvo}` | `{"Anna": 25}` |
| Hae arvo | `sanakirja[avain]` | `henkilöt["Anna"]` |
| Lisää/muuta | `sanakirja[avain] = arvo` | `henkilöt["Ville"] = 27` |
| Poista | `del sanakirja[avain]` | `del henkilöt["Anna"]` |
| Tarkista | `avain in sanakirja` | `"Anna" in henkilöt` |

### Turvallinen hakeminen get():lla

```python
henkilöt = {"Anna": 25, "Pekka": 30}

# Normaali haku - aiheuttaa virheen jos avainta ei ole
# print(henkilöt["Ville"])  # KeyError!

# Turvallinen haku - palauttaa None jos ei löydy
print(henkilöt.get("Ville"))  # None

# Turvallinen haku oletusarvolla
print(henkilöt.get("Ville", "Ei tiedossa"))  # Ei tiedossa
```

### Opittavaa
✅ Sanakirja tallentaa avain-arvo-pareja  
✅ Haku avaimella on **nopea** (paljon nopeampi kuin listan läpikäynti)  
✅ Avaimet ovat **yksilöllisiä** (sama avain ei voi esiintyä kahdesti)  
✅ `get()` on turvallisempi kuin `[]` jos avain saattaa puuttua  
💡 Käytä sanakirjaa kun tarvitset nopean haun nimellä/ID:llä!

---

## Harjoitus 2: Sanakirjan läpikäynti ⭐⭐

### Ratkaisu
[harjoitus2.py](harjoitus2.py)

```python
# Luo sanakirja opiskelijoiden pisteistä
pisteet = {
    "Anna": 92,
    "Pekka": 78,
    "Liisa": 45,
    "Matti": 88,
    "Kaisa": 79
}

print("=== OPISKELIJOIDEN TULOKSET ===\n")

# Laske keskiarvo
keskiarvo = sum(pisteet.values()) / len(pisteet)
print(f"Keskiarvo: {keskiarvo:.1f} pistettä\n")

# Etsi paras suoritus
paras_nimi = max(pisteet, key=pisteet.get)
paras_pisteet = pisteet[paras_nimi]
print(f"Paras suoritus: {paras_nimi} ({paras_pisteet} pistettä)\n")

# Käy läpi kaikki opiskelijat
print("Yksittäiset tulokset:")
for nimi, pistemäärä in pisteet.items():
    tila = "Hyväksytty" if pistemäärä >= 50 else "Hylätty"
    print(f"{nimi}: {pistemäärä} pistettä - {tila}")
```

### Selitys
- **sum(pisteet.values()):** Laskee kaikkien arvojen summan
- **len(pisteet):** Laskee avain-arvo-parien määrän
- **max(pisteet, key=pisteet.get):** Etsii avaimen jolla on suurin arvo
- **.items():** Palauttaa avain-arvo-parit tuplina

### Sanakirjan läpikäynti

**Tapa 1: Vain avaimet**
```python
for nimi in pisteet:
    print(nimi)
# Anna
# Pekka
# Liisa
```

**Tapa 2: Vain arvot**
```python
for pistemäärä in pisteet.values():
    print(pistemäärä)
# 92
# 78
# 45
```

**Tapa 3: Avaimet JA arvot (suositellaan!)**
```python
for nimi, pistemäärä in pisteet.items():
    print(f"{nimi}: {pistemäärä}")
# Anna: 92
# Pekka: 78
# Liisa: 45
```

### Hyödyllisiä funktioita sanakirjoille

```python
pisteet = {"Anna": 92, "Pekka": 78, "Liisa": 45}

# Keskiarvo
keskiarvo = sum(pisteet.values()) / len(pisteet)

# Pienin arvo
pienin = min(pisteet.values())

# Suurin arvo
suurin = max(pisteet.values())

# Avain jolla pienin arvo
heikoin = min(pisteet, key=pisteet.get)

# Avain jolla suurin arvo
paras = max(pisteet, key=pisteet.get)

# Kaikki avaimet listana
nimet = list(pisteet.keys())

# Kaikki arvot listana
pisteet_lista = list(pisteet.values())
```

### Vaihtoehtoinen tapa etsiä paras

```python
# Tapa 1: max() funktiolla
paras_nimi = max(pisteet, key=pisteet.get)

# Tapa 2: For-silmukalla
paras_nimi = None
paras_pisteet = -1

for nimi, pistemäärä in pisteet.items():
    if pistemäärä > paras_pisteet:
        paras_pisteet = pistemäärä
        paras_nimi = nimi

print(f"Paras: {paras_nimi} ({paras_pisteet} pistettä)")
```

### Opittavaa
✅ `.values()` antaa kaikki arvot  
✅ `.items()` antaa avain-arvo-parit tuplina  
✅ `max(sanakirja, key=sanakirja.get)` löytää avaimen suurimmalla arvolla  
✅ `sum()`, `min()`, `max()` toimivat arvoilla  
💡 `.items()` on paras tapa käydä läpi sanakirja kun tarvitset molemmat!

---

## Harjoitus 3: Tuplat ja järjestäminen ⭐⭐

### Ratkaisu
[harjoitus3.py](harjoitus3.py)

```python
# Luo lista tuplista
henkilöt = [
    ("Anna", 25),
    ("Pekka", 30),
    ("Liisa", 22),
    ("Matti", 35),
    ("Kaisa", 28)
]

# Tulosta alkuperäinen lista
print("Alkuperäinen lista:")
print(henkilöt)

# Järjestä iän mukaan (nuorin ensin)
iän_mukaan = sorted(henkilöt, key=lambda x: x[1])
print("\nJärjestetty iän mukaan (nuorin ensin):")
print(iän_mukaan)

# Järjestä nimen mukaan
nimen_mukaan = sorted(henkilöt)
print("\nJärjestetty nimen mukaan:")
print(nimen_mukaan)
```

### Selitys
- **Tupla:** Muuttumaton lista, esim. `("Anna", 25)`
- **Lambda:** Pikkufunktio järjestämiseen: `lambda x: x[1]`
- **x[0]** = ensimmäinen alkio (nimi)
- **x[1]** = toinen alkio (ikä)
- **sorted():** Palauttaa uuden järjestetyn listan

### Mikä on tupla?

Tupla on kuin lista, mutta **muuttumaton**:

```python
# Lista - muutettavissa
lista = [1, 2, 3]
lista[0] = 10    # OK
lista.append(4)  # OK

# Tupla - ei muutettavissa
tupla = (1, 2, 3)
# tupla[0] = 10    # TypeError!
# tupla.append(4)  # AttributeError!
```

**Miksi käyttää tuplaa?**
- ✅ Nopeampi kuin lista
- ✅ Turvallisempi (ei voi vahingossa muuttaa)
- ✅ Voi käyttää sanakirjan avaimena
- ✅ Sopii kiinteälle datalle (koordinaatit, päivämäärät)

### Lambda-funktiot

Lambda on "pikafunktio" jota ei tarvitse nimetä:

```python
# Normaali funktio
def hae_ikä(henkilö):
    return henkilö[1]

järjestetty = sorted(henkilöt, key=hae_ikä)

# Lambda - lyhyempi!
järjestetty = sorted(henkilöt, key=lambda x: x[1])
```

**Lambda-syntaksi:**
```
lambda parametrit: palautusarvo
```

**Esimerkkejä:**
```python
# Palauta itseisarvo
lambda x: abs(x)

# Palauta tupla toinen alkio
lambda x: x[1]

# Palauta merkkijonon pituus
lambda s: len(s)

# Palauta laskutulos
lambda a, b: a + b
```

### Tupla järjestyy oletuksena ensimmäisen alkion mukaan

```python
koordinaatit = [(5, 2), (1, 8), (3, 4), (1, 2)]

# Järjestetään - ensimmäinen alkio ratkaisee
järjestetty = sorted(koordinaatit)
print(järjestetty)  # [(1, 2), (1, 8), (3, 4), (5, 2)]

# Jos ensimmäinen sama, katsotaan toista:
# (1, 2) < (1, 8) koska 2 < 8
```

### Järjestäminen eri tavoilla

```python
henkilöt = [("Anna", 25), ("Pekka", 30), ("Liisa", 22)]

# Nimen mukaan (oletuksena)
sorted(henkilöt)
# [('Anna', 25), ('Liisa', 22), ('Pekka', 30)]

# Iän mukaan
sorted(henkilöt, key=lambda x: x[1])
# [('Liisa', 22), ('Anna', 25), ('Pekka', 30)]

# Iän mukaan, vanhin ensin
sorted(henkilöt, key=lambda x: x[1], reverse=True)
# [('Pekka', 30), ('Anna', 25), ('Liisa', 22)]

# Nimen pituuden mukaan
sorted(henkilöt, key=lambda x: len(x[0]))
# [('Anna', 25), ('Liisa', 22), ('Pekka', 30)]
```

### Opittavaa
✅ Tupla on muuttumaton lista: `(1, 2, 3)`  
✅ Lambda on lyhyt funktio: `lambda x: x[1]`  
✅ `sorted()` ei muuta alkuperäistä listaa  
✅ `key=` määrittää minkä mukaan järjestetään  
💡 Lambda on kätevä järjestämisessä kun tarvitset yksinkertaisen funktion!

---

## Harjoitus 4: Sanakirjan järjestäminen ⭐⭐⭐

### Ratkaisu
[harjoitus4.py](harjoitus4.py)

```python
# Luo sanakirja tuotteista ja hinnoista
tuotteet = {
    "Maito": 1.50,
    "Leipä": 2.30,
    "Juusto": 4.50,
    "Kahvi": 5.90,
    "Mehu": 2.80,
    "Voi": 3.20
}

# Tulosta alkuperäinen sanakirja
print("Alkuperäinen sanakirja:")
for tuote, hinta in tuotteet.items():
    print(f"{tuote}: {hinta:.2f} €")

# Järjestä hinnan mukaan (halvin ensin)
print("\n=== HALVIN ENSIN ===")
halvin_ensin = sorted(tuotteet.items(), key=lambda x: x[1])
for tuote, hinta in halvin_ensin:
    print(f"{tuote}: {hinta:.2f} €")

# Järjestä hinnan mukaan (kallein ensin)
print("\n=== KALLEIN ENSIN ===")
kallein_ensin = sorted(tuotteet.items(), key=lambda x: x[1], reverse=True)
for tuote, hinta in kallein_ensin:
    print(f"{tuote}: {hinta:.2f} €")

# Järjestä aakkosjärjestyksessä
print("\n=== AAKKOSJÄRJESTYKSESSÄ ===")
aakkosissa = sorted(tuotteet.items())
for tuote, hinta in aakkosissa:
    print(f"{tuote}: {hinta:.2f} €")
```

### Selitys
- **.items():** Palauttaa lista tuplista: `[("Maito", 1.50), ("Leipä", 2.30), ...]`
- **lambda x: x[1]:** Ottaa tupla `("Maito", 1.50)` ja palauttaa `1.50` (hinta)
- **lambda x: x[0]:** Ottaa tupla `("Maito", 1.50)` ja palauttaa `"Maito"` (nimi)
- **reverse=True:** Kääntää järjestyksen (laskeva)

### Sanakirjan järjestäminen

Sanakirjaa **ei voi järjestää suoraan**, mutta voit järjestää sen **avain-arvo-parit**:

**1. Järjestä avainten mukaan:**
```python
tuotteet = {"Maito": 1.50, "Leipä": 2.30, "Juusto": 4.50}

# Tapa 1: Järjestä avaimet
for tuote in sorted(tuotteet):
    print(f"{tuote}: {tuotteet[tuote]}")

# Tapa 2: Järjestä .items()
for tuote, hinta in sorted(tuotteet.items()):
    print(f"{tuote}: {hinta}")
```

**2. Järjestä arvojen mukaan:**
```python
# Arvon mukaan (pienin ensin)
järjestetty = sorted(tuotteet.items(), key=lambda x: x[1])

# Arvon mukaan (suurin ensin)
järjestetty = sorted(tuotteet.items(), key=lambda x: x[1], reverse=True)
```

### Mitä .items() palauttaa?

```python
tuotteet = {"Maito": 1.50, "Leipä": 2.30}

# .items() palauttaa dict_items-olion
print(tuotteet.items())
# dict_items([('Maito', 1.50), ('Leipä', 2.30)])

# Voit muuntaa sen listaksi
lista = list(tuotteet.items())
print(lista)
# [('Maito', 1.50), ('Leipä', 2.30)]

# Jokainen alkio on tupla:
for tupla in tuotteet.items():
    print(tupla)
    print(f"Nimi: {tupla[0]}, Hinta: {tupla[1]}")
```

### Luo uusi järjestetty sanakirja

```python
tuotteet = {"Maito": 1.50, "Leipä": 2.30, "Juusto": 4.50}

# Järjestä hinnan mukaan ja luo uusi sanakirja
järjestetty_dict = dict(sorted(tuotteet.items(), key=lambda x: x[1]))
print(järjestetty_dict)
# {'Maito': 1.50, 'Leipä': 2.30, 'Juusto': 4.50}

# HUOM: Python 3.7+ säilyttää sanakirjan järjestyksen!
```

### Monimutkaisempi järjestäminen

```python
# Opiskelijat: pisteet ja ikä
opiskelijat = {
    "Anna": (92, 22),
    "Pekka": (78, 25),
    "Liisa": (92, 21),
    "Matti": (78, 23)
}

# Järjestä ensin pisteiden mukaan, sitten iän mukaan
järjestetty = sorted(
    opiskelijat.items(),
    key=lambda x: (-x[1][0], x[1][1])  # -pisteet (laskeva), ikä (nouseva)
)

for nimi, (pisteet, ikä) in järjestetty:
    print(f"{nimi}: {pisteet} pistettä, {ikä} vuotta")
```

### Opittavaa
✅ `.items()` palauttaa avain-arvo-parit tuplina  
✅ `sorted(..., key=lambda x: x[1])` järjestää arvojen mukaan  
✅ `sorted(..., key=lambda x: x[0])` järjestää avainten mukaan  
✅ `reverse=True` kääntää järjestyksen  
✅ Python 3.7+ säilyttää sanakirjan järjestyksen  
💡 Sanakirja + sorted() on tehokas yhdistelmä!

---

## Harjoitus 5: Sanalaskuri ⭐⭐⭐⭐

### Ratkaisu
[harjoitus5.py](harjoitus5.py)

```python
# Kysy käyttäjältä lause
lause = input("Anna lause: ")

# Jaa sanoiksi ja muunna pieniksi kirjaimiksi
sanat = lause.lower().split()

# Laske sanat sanakirjaan
sanalaskuri = {}

for sana in sanat:
    # Poista välimerkit
    sana = sana.strip(".,!?;:")
    
    # Älä laske tyhjiä sanoja
    if sana:
        # Lisää tai kasvata lukumäärää
        sanalaskuri[sana] = sanalaskuri.get(sana, 0) + 1

# Järjestä yleisin ensin
järjestetty = sorted(sanalaskuri.items(), key=lambda x: x[1], reverse=True)

# Tulosta tulokset
print("\n=== SANALASKURI ===\n")

if järjestetty:
    yleisin_sana, yleisin_määrä = järjestetty[0]
    print(f"Yleisin sana: {yleisin_sana} ({yleisin_määrä} kertaa)\n")
    
    print("Kaikki sanat (yleisimmästä harvinaisimpaan):")
    for sana, määrä in järjestetty:
        print(f"{sana}: {määrä} kertaa")
    
    print(f"\nYhteensä {len(sanalaskuri)} erilaista sanaa.")
else:
    print("Ei sanoja laskettavaksi.")
```

### Selitys
- **.lower():** Muuntaa merkkijonon pieniksi kirjaimiksi
- **.split():** Jakaa merkkijonon sanoiksi välilyönnin kohdalta
- **.strip(".,!?;:"):** Poistaa välimerkit alusta ja lopusta
- **.get(sana, 0):** Palauttaa arvon tai 0 jos ei löydy
- **sanalaskuri[sana] += 1:** Kasvattaa lukumäärää

### Sanalaskurin logiikka

**Perusidea:**
```python
sanalaskuri = {}

for sana in ["kissa", "koira", "kissa", "kissa", "koira"]:
    if sana in sanalaskuri:
        sanalaskuri[sana] += 1  # Lisää 1
    else:
        sanalaskuri[sana] = 1   # Ensimmäinen kerta

print(sanalaskuri)
# {'kissa': 3, 'koira': 2}
```

**Lyhyempi tapa get():lla:**
```python
sanalaskuri = {}

for sana in ["kissa", "koira", "kissa", "kissa", "koira"]:
    sanalaskuri[sana] = sanalaskuri.get(sana, 0) + 1

print(sanalaskuri)
# {'kissa': 3, 'koira': 2}
```

### Merkkijonon käsittely

```python
lause = "Python on loistava! Python on helppo."

# 1. Muunna pieniksi kirjaimiksi
lause = lause.lower()
# "python on loistava! python on helppo."

# 2. Jaa sanoiksi
sanat = lause.split()
# ['python', 'on', 'loistava!', 'python', 'on', 'helppo.']

# 3. Poista välimerkit jokaisesta sanasta
puhdistetut = []
for sana in sanat:
    puhdas = sana.strip(".,!?;:")
    puhdistetut.append(puhdas)
# ['python', 'on', 'loistava', 'python', 'on', 'helppo']
```

### Välimerkkien poistaminen

```python
sana = "python!"

# strip() poistaa merkit alusta JA lopusta
print(sana.strip("!"))    # "python"

# Esimerkkejä
print("loistava!".strip(".,!?"))   # "loistava"
print("...kissa...".strip("."))    # "kissa"
print("!?hei!?".strip("!?"))       # "hei"

# HUOM: strip() ei poista keskeltä!
print("kis!sa".strip("!"))  # "kis!sa" (! keskellä)
```

### Vaihtoehtoiset tavat laskea sanoja

**Tapa 1: Counter (collections-moduuli)**
```python
from collections import Counter

lause = "python on loistava python on helppo"
sanat = lause.split()

sanalaskuri = Counter(sanat)
print(sanalaskuri)
# Counter({'python': 2, 'on': 2, 'loistava': 1, 'helppo': 1})

# Yleisimmät 3
print(sanalaskuri.most_common(3))
# [('python', 2), ('on', 2), ('loistava', 1)]
```

**Tapa 2: defaultdict**
```python
from collections import defaultdict

sanalaskuri = defaultdict(int)  # Oletusarvo 0

for sana in ["kissa", "koira", "kissa"]:
    sanalaskuri[sana] += 1

print(dict(sanalaskuri))
# {'kissa': 2, 'koira': 1}
```

**Tapa 3: Manuaalinen (kuten harjoituksessa)**
```python
sanalaskuri = {}

for sana in ["kissa", "koira", "kissa"]:
    sanalaskuri[sana] = sanalaskuri.get(sana, 0) + 1
```

### Käytännön sovelluksia

**1. Analysoiti tekstitiedosto:**
```python
with open("teksti.txt", "r", encoding="utf-8") as f:
    teksti = f.read()

sanat = teksti.lower().split()
sanalaskuri = {}

for sana in sanat:
    sana = sana.strip(".,!?;:")
    if sana:
        sanalaskuri[sana] = sanalaskuri.get(sana, 0) + 1

# Top 10
top10 = sorted(sanalaskuri.items(), key=lambda x: x[1], reverse=True)[:10]
for sana, määrä in top10:
    print(f"{sana}: {määrä}")
```

**2. Etsi harvinaiset sanat:**
```python
# Sanat jotka esiintyvät vain kerran
harvinaiset = [sana for sana, määrä in sanalaskuri.items() if määrä == 1]
print(f"Harvinaisia sanoja: {len(harvinaiset)}")
```

**3. Prosenttiosuudet:**
```python
yhteensä = sum(sanalaskuri.values())

for sana, määrä in sorted(sanalaskuri.items(), key=lambda x: x[1], reverse=True):
    prosentti = (määrä / yhteensä) * 100
    print(f"{sana}: {määrä} ({prosentti:.1f}%)")
```

### Opittavaa
✅ Sanakirja on täydellinen sanojen laskemiseen  
✅ `.get(avain, oletusarvo)` välttää KeyErrorin  
✅ `.split()` jakaa merkkijonon sanoiksi  
✅ `.strip()` poistaa merkkejä alusta ja lopusta  
✅ Järjestä ja rajaa tuloksia: `sorted(...)[:10]`  
💡 Sanalaskuri on yleinen data-analytiikan tehtävä!

---

## Yhteenveto: Sanakirjat, tuplat ja järjestäminen

### Sanakirjat

**Luominen:**
```python
tyhjä = {}
henkilöt = {"Anna": 25, "Pekka": 30}
```

**Operaatiot:**
```python
henkilöt["Anna"]              # Hae arvo
henkilöt["Ville"] = 27        # Lisää/muuta
del henkilöt["Anna"]          # Poista
henkilöt.get("Anna", 0)       # Turvallinen haku
"Anna" in henkilöt            # Tarkista onko olemassa
```

**Läpikäynti:**
```python
for avain in sanakirja:                    # Avaimet
for arvo in sanakirja.values():            # Arvot
for avain, arvo in sanakirja.items():      # Molemmat
```

### Tuplat

**Luominen:**
```python
tupla = (1, 2, 3)
koordinaatit = (10, 20)
henkilö = ("Anna", 25, "Helsinki")
```

**Ominaisuudet:**
- ❌ Ei muutettavissa (immutable)
- ✅ Nopeampi kuin lista
- ✅ Voi käyttää sanakirjan avaimena
- ✅ Sopii kiinteälle datalle

**Purkaminen:**
```python
x, y, z = (1, 2, 3)
nimi, ikä = ("Anna", 25)
```

### Järjestäminen

**Perus:**
```python
lista.sort()                  # Muuttaa listan
uusi = sorted(lista)          # Palauttaa uuden
```

**Laskeva:**
```python
lista.sort(reverse=True)
uusi = sorted(lista, reverse=True)
```

**Mukautettu:**
```python
# Pituuden mukaan
sanat.sort(key=len)

# Lambda
tupla_lista.sort(key=lambda x: x[1])

# Sanakirja arvon mukaan
järjestetty = sorted(sanakirja.items(), key=lambda x: x[1])
```

### Vertailutaulukko

| Tietorakenne | Muuttuva? | Järjestetty? | Haku | Käyttö |
|--------------|-----------|--------------|------|--------|
| **Lista** | ✅ Kyllä | ❌ Ei | O(n) | Järjestetty kokoelma |
| **Tupla** | ❌ Ei | ❌ Ei | O(n) | Kiinteä data |
| **Sanakirja** | ✅ Kyllä | ✅ Py 3.7+ | O(1) | Avain-arvo-parit |

### Yleisiä virheitä

**1. Sanakirjan haku ilman tarkistusta**
```python
# ❌ VÄÄRIN
print(henkilöt["Ville"])  # KeyError jos ei ole!

# ✅ OIKEIN
print(henkilöt.get("Ville", "Ei löydy"))
# tai
if "Ville" in henkilöt:
    print(henkilöt["Ville"])
```

**2. Tupla yhden alkion kanssa**
```python
# ❌ VÄÄRIN
tupla = (5)    # Tämä on vain numero!
print(type(tupla))  # <class 'int'>

# ✅ OIKEIN
tupla = (5,)   # Pilkku tekee siitä tupla!
print(type(tupla))  # <class 'tuple'>
```

**3. Järjestäminen ilman key:tä**
```python
opiskelijat = [("Anna", 25), ("Pekka", 30)]

# ❌ Vain nimen mukaan (oletuksena)
järjestetty = sorted(opiskelijat)

# ✅ Iän mukaan
järjestetty = sorted(opiskelijat, key=lambda x: x[1])
```

**4. .items() unohtaminen**
```python
tuotteet = {"Maito": 1.50, "Leipä": 2.30}

# ❌ Ei toimi!
# for tuote, hinta in tuotteet:  # ValueError!

# ✅ Toimii!
for tuote, hinta in tuotteet.items():
    print(f"{tuote}: {hinta}")
```

---

## Vinkkejä

💡 **Käytä get()** - välttää KeyErrorin: `sanakirja.get(avain, oletusarvo)`  
💡 **Tuplat ovat nopeampia** - käytä kun data ei muutu  
💡 **Lambda on kätevä** - lyhyet funktiot järjestämiseen  
💡 **.items() avain-arvo-pareille** - paras tapa läpikäyntiin  
💡 **Counter-moduuli** - helpottaa sanojen laskemista  
💡 **sorted() ei muuta alkuperäistä** - turvallinen käyttää  

---

## Hyödyllisiä koodipätkiä

**Käännä sanakirja (vaihda avaimet ja arvot):**
```python
alkuperäinen = {"Anna": 25, "Pekka": 30}
käännetty = {ikä: nimi for nimi, ikä in alkuperäinen.items()}
# {25: 'Anna', 30: 'Pekka'}
```

**Yhdistä kaksi sanakirjaa:**
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

yhdistetty = {**dict1, **dict2}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# tai
yhdistetty = dict1 | dict2  # Python 3.9+
```

**Suodata sanakirja:**
```python
pisteet = {"Anna": 92, "Pekka": 78, "Liisa": 45}

# Vain hyväksytyt (>= 50)
hyväksytyt = {nimi: p for nimi, p in pisteet.items() if p >= 50}
# {'Anna': 92, 'Pekka': 78}
```

**Ryhmittele lista:**
```python
nimet = ["Anna", "Anu", "Pekka", "Petra", "Antti"]

# Ryhmittele alkukirjaimen mukaan
ryhmät = {}
for nimi in nimet:
    alkukirjain = nimi[0]
    if alkukirjain not in ryhmät:
        ryhmät[alkukirjain] = []
    ryhmät[alkukirjain].append(nimi)

print(ryhmät)
# {'A': ['Anna', 'Anu', 'Antti'], 'P': ['Pekka', 'Petra']}
```

---

Hienoa työtä! Olet nyt oppinut sanakirjojen, tuplien ja järjestämisen perusteet. 🎉

➡️**Seuraavaksi:** [Aihe 11 - NumPy ja data-analytiikka](../../11.NumPy%20ja%20data-analytiikka/)