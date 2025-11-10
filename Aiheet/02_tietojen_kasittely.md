# Tietojen käsittely Pythonissa

## Sisällysluettelo
1. [Perustietotyypit](#perustietotyypit)
2. [Tietotyyppien muunnokset](#tietotyyppien-muunnokset)
3. [Lukujen pyöristäminen](#lukujen-pyöristäminen)
4. [Merkkijonojen käsittely](#merkkijonojen-käsittely)
5. [Tulosteen muotoilu](#tulosteen-muotoilu)
6. [Muuttujien roolit](#muuttujien-roolit)

---

## Perustietotyypit

Python käyttää useita perustietotyyppejä datan tallentamiseen ja käsittelyyn.

### 1. Merkkijonot (String - str)
Merkkijonot sisältävät tekstiä ja ne merkitään lainausmerkeillä.

```python
# Erilaisia merkkijonoja
nimi = "Matti"
sukunimi = 'Meikäläinen'
lause = "Python on helppoa!"
monirivinen = """Tämä on
monirivinen
merkkijono"""

print(type(nimi))  # <class 'str'>
```

### 2. Kokonaisluvut (Integer - int)
Kokonaisluvut ovat lukuja ilman desimaaleja.

```python
ika = 25
vuosi = 2025
lampotila = -15
iso_luku = 1_000_000  # Alaviiva helpottaa lukemista

print(type(ika))  # <class 'int'>
```

### 3. Liukuluvut (Float)
Liukuluvut sisältävät desimaaleja.

```python
hinta = 19.99
pii = 3.14159
lampotila_celsius = 23.5
tieteellinen = 1.5e-4  # 0.00015

print(type(hinta))  # <class 'float'>
```

---

## Tietotyyppien muunnokset

Usein tarvitaan muunnoksia eri tietotyyppien välillä.

### String → Integer/Float

```python
# Merkkijonosta kokonaisluvuksi
ika_str = "25"
ika_int = int(ika_str)
print(ika_int + 5)  # 30

# Merkkijonosta liukuluvuksi
hinta_str = "19.99"
hinta_float = float(hinta_str)
print(hinta_float * 2)  # 39.98
```

### Integer/Float → String

```python
# Luvusta merkkijonoksi
ika = 25
ika_teksti = str(ika)
print("Ikä: " + ika_teksti)  # Ikä: 25

hinta = 19.99
hinta_teksti = str(hinta)
print("Hinta: " + hinta_teksti + "€")  # Hinta: 19.99€
```

### Integer ↔ Float

```python
# Kokonaisluvusta liukuluvuksi
luku = 10
liukuluku = float(luku)
print(liukuluku)  # 10.0

# Liukuluvusta kokonaisluvuksi (katkaisee desimaalit)
desimaaliluku = 9.99
kokonaisluku = int(desimaaliluku)
print(kokonaisluku)  # 9
```

### Käytännön esimerkki

```python
# Käyttäjän syöte on aina merkkijono
nimi = input("Anna nimesi: ")
ika = input("Anna ikäsi: ")

# Muunnetaan ikä luvuksi laskutoimituksia varten
ika_vuosina = int(ika)
ika_kuukausina = ika_vuosina * 12

print(f"{nimi}, olet {ika_kuukausina} kuukautta vanha!")
```

---

## Lukujen pyöristäminen

### round() -funktio

```python
# Perus pyöristäminen
luku = 3.14159
pyoristetty = round(luku)
print(pyoristetty)  # 3

# Pyöristäminen tiettyyn desimaaliin
pii = 3.14159265359
print(round(pii, 2))   # 3.14
print(round(pii, 4))   # 3.1416

# Käytännön esimerkki: hintalaskuri
hinta_per_kilo = 12.50
paino = 0.374  # kg
kokonaishinta = hinta_per_kilo * paino
print(f"Hinta: {round(kokonaishinta, 2)}€")  # Hinta: 4.68€
```

### Muita pyöristysmenetelmiä

```python
import math

luku = 3.7

# Pyöristys ylöspäin
print(math.ceil(luku))   # 4

# Pyöristys alaspäin
print(math.floor(luku))  # 3

# Katkaiseminen (poistaa desimaalit)
print(int(luku))         # 3
```

---

## Merkkijonojen käsittely

### Indeksointi

Merkkijonon merkkejä voi käsitellä yksitellen indeksien avulla.

```python
sana = "Python"

# Indeksointi alkaa nollasta
print(sana[0])   # P
print(sana[1])   # y
print(sana[5])   # n

# Negatiiviset indeksit alkavat lopusta
print(sana[-1])  # n
print(sana[-2])  # o
print(sana[-6])  # P
```

**Visualisointi:**
```
 P   y   t   h   o   n
 0   1   2   3   4   5    (positiiviset indeksit)
-6  -5  -4  -3  -2  -1    (negatiiviset indeksit)
```

### Viipalointi (Slicing)

Viipaloinnilla voi poimia osan merkkijonosta.

```python
teksti = "Python ohjelmointi"

# Perussyntaksi: [alku:loppu]
print(teksti[0:6])    # Python
print(teksti[7:18])   # ohjelmointi

# Alusta loppuun
print(teksti[:6])     # Python (alusta indeksiin 6)
print(teksti[7:])     # ohjelmointi (indeksistä 7 loppuun)

# Askel-parametri: [alku:loppu:askel]
print(teksti[::2])    # Pto hemoni (joka toinen merkki)
print(teksti[::-1])   # itniomlehjo nohtyP (käänteinen)
```

### Käytännön esimerkkejä

```python
# Henkilötunnuksen käsittely
hetu = "010195-1234"
paiva = hetu[0:2]       # 01
kuukausi = hetu[2:4]    # 01
vuosi = hetu[4:6]       # 95
print(f"Syntymäaika: {paiva}.{kuukausi}.{vuosi}")

# Sähköpostin tarkistus
email = "matti@example.com"
kayttaja = email[:email.index("@")]  # matti
domain = email[email.index("@")+1:]  # example.com
print(f"Käyttäjä: {kayttaja}, Palvelin: {domain}")
```

---

## Tulosteen muotoilu

### print() -funktion peruskäyttö

```python
# Perus tulostus
print("Terve maailma!")

# Usean arvon tulostus
nimi = "Anna"
ika = 30
print("Nimi:", nimi, "Ikä:", ika)

# Erotinmerkin muuttaminen
print("omena", "banaani", "kirsikka", sep=", ")  # omena, banaani, kirsikka

# Rivinvaihdon muuttaminen
print("Ensimmäinen rivi", end=" ")
print("Sama rivi")  # Ensimmäinen rivi Sama rivi
```

### F-stringit (suositeltu tapa!)

F-stringit ovat modernin Pythonin paras tapa muotoilla tulostetta.

```python
nimi = "Matti"
ika = 25
pituus = 1.82

# Perus f-string
print(f"Nimi: {nimi}, Ikä: {ika}")

# Laskutoimitukset f-stringissä
print(f"{nimi} on {ika * 12} kuukautta vanha")

# Desimaalien määrä
hinta = 19.99567
print(f"Hinta: {hinta:.2f}€")  # Hinta: 19.99€

# Leveys ja tasaus
print(f"{'Nimi':<10} {'Ikä':>5}")  # Vasen tasaus / Oikea tasaus
print(f"{nimi:<10} {ika:>5}")

# Prosenttiluvut
osuus = 0.847
print(f"Onnistumisprosentti: {osuus:.1%}")  # Onnistumisprosentti: 84.7%
```

### .format() -metodi

```python
# Vanha tapa, toimii edelleen
nimi = "Liisa"
ika = 28

print("Nimi: {}, Ikä: {}".format(nimi, ika))
print("Nimi: {0}, Ikä: {1}, Nimi: {0}".format(nimi, ika))

# Nimetyt parametrit
print("Hei {nimi}, olet {ika} vuotta vanha".format(nimi=nimi, ika=ika))
```

### %-muotoilu (vanha tyyli)

```python
# Vanhempi tapa, käytetään harvemmin
nimi = "Pekka"
ika = 35

print("Nimi: %s, Ikä: %d" % (nimi, ika))
print("Hinta: %.2f€" % 19.99567)
```

### Merkkijonomenetelmät

```python
teksti = "python ohjelmointi"

# Isoiksi/pieniksi kirjaimiksi
print(teksti.upper())       # PYTHON OHJELMOINTI
print(teksti.lower())       # python ohjelmointi
print(teksti.capitalize())  # Python ohjelmointi
print(teksti.title())       # Python Ohjelmointi

# Välilyöntien käsittely
teksti2 = "  liikaa välilyöntejä  "
print(teksti2.strip())      # "liikaa välilyöntejä"
print(teksti2.lstrip())     # "liikaa välilyöntejä  "
print(teksti2.rstrip())     # "  liikaa välilyöntejä"

# Korvaaminen
print(teksti.replace("python", "Python"))  # Python ohjelmointi

# Tarkistukset
print("python" in teksti)   # True
print(teksti.startswith("p"))  # True
print(teksti.endswith("i"))    # True
```

---

## Muuttujien roolit

Muuttujilla on erilaisia rooleja ohjelman logiikassa.

### 1. Kiintoarvo (Constant)

Arvo, joka ei muutu ohjelman suorituksen aikana.

```python
# Nimeämiskäytäntö: ISOT_KIRJAIMET
ALV_PROSENTTI = 24
PI = 3.14159
MAX_YRITYKSET = 3

hinta_ilman_alvia = 100
kokonaishinta = hinta_ilman_alvia * (1 + ALV_PROSENTTI / 100)
print(f"Hinta ALV:llä: {kokonaishinta:.2f}€")
```

### 2. Stepper (Askeltaja)

Muuttuja, joka etenee säännöllisesti (esim. silmukassa).

```python
# Askeltaja for-silmukassa
for i in range(1, 6):  # i on askeltaja
    print(f"Kierros: {i}")

# Manuaalinen askeltaja
laskuri = 0
while laskuri < 5:
    print(f"Laskuri: {laskuri}")
    laskuri += 1  # Askeltaa yhdellä
```

### 3. Most-recent holder (Viimeisin arvo)

Säilyttää viimeisimmän arvon (esim. silmukassa).

```python
# Käyttäjän syötteet
viimeisin_syote = ""
while viimeisin_syote != "lopeta":
    viimeisin_syote = input("Anna komento (lopeta lopettaa): ")
    print(f"Annoit: {viimeisin_syote}")

# Suurin/pienin arvo
numerot = [45, 23, 67, 12, 89]
suurin = numerot[0]
for numero in numerot:
    if numero > suurin:
        suurin = numero  # Päivittyy aina uudella suurimmalla
print(f"Suurin luku: {suurin}")
```

### 4. Gatherer (Kerääjä/Akumulaattori)

Kerää tai laskee yhteen arvoja.

```python
# Summan kerääminen
summa = 0  # Aloitusarvo
numerot = [10, 20, 30, 40, 50]
for numero in numerot:
    summa += numero  # Kerää summaa
print(f"Yhteensä: {summa}")  # 150

# Merkkijonon kerääminen
tulos = ""  # Tyhjä alku
sanat = ["Hei", "maailma", "Python", "on", "kivaa"]
for sana in sanat:
    tulos += sana + " "  # Kerää sanoja
print(tulos.strip())  # Hei maailma Python on kivaa

# Listan kerääminen
parilliset = []
for i in range(1, 11):
    if i % 2 == 0:
        parilliset.append(i)
print(parilliset)  # [2, 4, 6, 8, 10]
```

### 5. Transformation (Muunnos)

Muuttuja, joka muuttuu laskutoimituksen tai muunnoksen kautta.

```python
# Yksinkertainen muunnos
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Hinnan muunnos
hinta_euroina = 100
vaihtokurssi = 1.08
hinta_dollareina = hinta_euroina * vaihtokurssi
print(f"{hinta_euroina}€ = ${hinta_dollareina:.2f}")

# Merkkijonon muunnos
nimi = "matti meikäläinen"
nimi_muotoiltu = nimi.title()  # Muunnos
print(nimi_muotoiltu)  # Matti Meikäläinen
```

### 6. Temporary (Väliaikainen)

Lyhytaikainen arvo laskutoimituksissa.

```python
# Kahden muuttujan vaihto
a = 5
b = 10
temp = a  # Väliaikainen tallennuspaikka
a = b
b = temp
print(f"a = {a}, b = {b}")  # a = 10, b = 5

# Keskiarvon laskenta
luvut = [10, 20, 30, 40, 50]
summa = sum(luvut)  # Väliaikainen arvo
keskiarvo = summa / len(luvut)
print(f"Keskiarvo: {keskiarvo}")
```

---

## Kattava käytännön esimerkki

Tässä on laaja esimerkki, joka yhdistää kaikki opitut asiat:

```python
# Kaupan kassajärjestelmä

# Kiintoarvot
ALV_PROSENTTI = 24
ALENNUS_RAJA = 100
ALENNUS_PROSENTTI = 10

print("=" * 40)
print("TERVETULOA KAUPPAAN".center(40))
print("=" * 40)

# Käyttäjän tiedot
nimi = input("Anna nimesi: ").strip().title()
asiakasnumero = input("Anna asiakasnumerosi: ").strip()

print(f"\nTervetuloa, {nimi}!")
print(f"Asiakasnumero: {asiakasnumero[:4]}****")  # Viipalointi

# Ostoskori (gatherer)
yhteishinta = 0.0
tuotteet = []

# Ostoslista
print("\nAnna ostetut tuotteet (tyhjä lopettaa):")
while True:
    tuote = input("Tuotteen nimi: ").strip()
    if tuote == "":
        break
    
    # Muunnokset ja tarkistukset
    try:
        hinta_str = input("Hinta (€): ")
        hinta = float(hinta_str)
        
        maara_str = input("Määrä: ")
        maara = int(maara_str)
        
        # Laskenta
        rivi_hinta = hinta * maara
        yhteishinta += rivi_hinta  # Gatherer
        
        tuotteet.append({
            'nimi': tuote.title(),
            'hinta': hinta,
            'maara': maara,
            'yhteensa': rivi_hinta
        })
        
        print(f"✓ Lisätty: {tuote.title()} - {rivi_hinta:.2f}€\n")
        
    except ValueError:
        print("Virheellinen syöte! Yritä uudelleen.\n")

# Tulostetaan kuitti
print("\n" + "=" * 40)
print("KUITTI".center(40))
print("=" * 40)

# Most-recent holder ja muotoilu
for i, tuote in enumerate(tuotteet, 1):  # Stepper
    print(f"{i}. {tuote['nimi']:<20} {tuote['maara']} kpl")
    print(f"   {tuote['hinta']:.2f}€ × {tuote['maara']} = {tuote['yhteensa']:.2f}€")

print("-" * 40)

# Alennuksen laskenta
alennus = 0.0
if yhteishinta >= ALENNUS_RAJA:
    alennus = yhteishinta * (ALENNUS_PROSENTTI / 100)
    print(f"Alennus ({ALENNUS_PROSENTTI}%): -{alennus:.2f}€")

# Loppusumma
vahennyksen_jalkeen = yhteishinta - alennus
alv_maara = vahennyksen_jalkeen * (ALV_PROSENTTI / 100)
loppusumma = vahennyksen_jalkeen

print(f"Välisumma: {yhteishinta:.2f}€")
print(f"Sis. ALV {ALV_PROSENTTI}%: {alv_maara:.2f}€")
print("=" * 40)
print(f"YHTEENSÄ: {loppusumma:.2f}€".rjust(40))
print("=" * 40)

# Maksutapa
maksettu_str = input("\nMaksettu määrä (€): ")
maksettu = float(maksettu_str)

if maksettu >= loppusumma:
    vaihtoraha = maksettu - loppusumma
    print(f"\n✓ Maksu hyväksytty!")
    print(f"Vaihtorahaa: {vaihtoraha:.2f}€")
else:
    puuttuu = loppusumma - maksettu
    print(f"\n✗ Maksu ei riitä! Puuttuu vielä {puuttuu:.2f}€")

print(f"\nKiitos, {nimi}! Tervetuloa uudelleen!")
print("=" * 40)
```

---

## Yhteenveto

### Tärkeimmät oppipisteet:

1. **Tietotyypit**: `str`, `int`, `float` - valitse oikea tyyppi tarkoitukseen
2. **Muunnokset**: `int()`, `float()`, `str()` - muista muuntaa ennen laskutoimituksia
3. **Pyöristäminen**: `round()` - erittäin tärkeä rahalaskuissa
4. **Indeksointi**: `[0]`, `[-1]` - merkkejä voi käsitellä kuten listoja
5. **Viipalointi**: `[alku:loppu:askel]` - tehokas tapa käsitellä merkkijonoja
6. **F-stringit**: `f"{muuttuja}"` - moderni ja selkeä muotoilutapa
7. **Muuttujien roolit**: Ymmärrä, miksi muuttuja on olemassa - helpottaa koodin lukemista


Onnea ohjelmointiin! 🐍