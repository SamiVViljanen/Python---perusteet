# Ehtolauseet (Conditional Statements)

## Sisällysluettelo
1. [Ehdollinen suoritus](#ehdollinen-suoritus)
2. [If-lause](#if-lause)
3. [Elif ja Else](#elif-ja-else)
4. [Loogiset lausekkeet](#loogiset-lausekkeet)
5. [Vertailuoperaattorit](#vertailuoperaattorit)
6. [Loogiset operaattorit](#loogiset-operaattorit)
7. [Sisennyksen merkitys](#sisennyksen-merkitys)
8. [Käyttäjän syötteisiin perustuvat ohjelmat](#käyttäjän-syötteisiin-perustuvat-ohjelmat)
9. [Käytännön esimerkkejä](#käytännön-esimerkkejä)

---

## Ehdollinen suoritus

**Ehdollinen suoritus** tarkoittaa, että ohjelma tekee päätöksiä ja suorittaa eri koodia eri tilanteissa. Tämä on ohjelmalogiikan perusta!

### Miksi ehtolauseita tarvitaan?

```python
# Ilman ehtolauseita - kaikki suoritetaan aina
print("Tervetuloa!")
print("Olet täysi-ikäinen")  # Tulostuu aina, vaikka ei olisi

# Ehtolauseiden kanssa - ohjelma tekee päätöksiä
ika = 15
if ika >= 18:
    print("Olet täysi-ikäinen")  # Tulostuu vain jos ehto on tosi
else:
    print("Olet alaikäinen")
```

---

## If-lause

`if`-lause on perusehtolause. Se suorittaa koodin vain, jos ehto on **tosi** (True).

### Perussyntaksi

```python
if ehto:
    # Tämä koodi suoritetaan, jos ehto on tosi
    print("Ehto toteutui!")
```

### Yksinkertaiset esimerkit

```python
# Esimerkki 1: Lämpötilan tarkistus
lampotila = 25

if lampotila > 20:
    print("Ulkona on lämmintä!")

# Esimerkki 2: Ikäraja
ika = 18

if ika >= 18:
    print("Saat äänestää!")

# Esimerkki 3: Salasanan tarkistus
salasana = "salainen123"

if salasana == "salainen123":
    print("Kirjautuminen onnistui!")
```

### Usean rivin koodia

```python
pisteet = 85

if pisteet >= 50:
    print("Läpäisit kokeen!")
    print("Onneksi olkoon!")
    pisteet += 5  # Bonuspisteet
    print(f"Uudet pisteesi: {pisteet}")
```

---

## Elif ja Else

### Else - vaihtoehtoinen toiminta

`else` suoritetaan, kun `if`-ehto on **epätosi** (False).

```python
ika = 15

if ika >= 18:
    print("Olet täysi-ikäinen")
else:
    print("Olet alaikäinen")  # Tämä tulostuu
```

### Elif - useita vaihtoehtoja

`elif` (else if) mahdollistaa useiden ehtojen testaamisen.

```python
pisteet = 75

if pisteet >= 90:
    print("Arvosana: Kiitettävä")
elif pisteet >= 80:
    print("Arvosana: Hyvä")
elif pisteet >= 70:
    print("Arvosana: Tyydyttävä")  # Tämä tulostuu
elif pisteet >= 50:
    print("Arvosana: Välttävä")
else:
    print("Arvosana: Hylätty")
```

### Täydellinen esimerkki

```python
lämpötila = 18

if lämpötila > 25:
    print("🌞 Helteinen päivä!")
    print("Muista juoda vettä")
elif lämpötila > 15:
    print("☀️ Mukava sää")  # Tämä tulostuu
    print("Hyvä päivä kävelylle")
elif lämpötila > 5:
    print("🌤️ Viileää")
    print("Ota takki mukaan")
else:
    print("❄️ Kylmää!")
    print("Pukeudu lämpimästi")
```

**HUOM:** Vain **yksi** lohko suoritetaan! Ensimmäinen tosi ehto voittaa.

---

## Loogiset lausekkeet

Loogiset lausekkeet palauttavat **True** (tosi) tai **False** (epätosi).

```python
# Yksinkertaisia totuusarvoja
print(5 > 3)      # True
print(10 < 5)     # False
print(7 == 7)     # True
print(8 != 8)     # False

# Käyttö if-lauseissa
ika = 20
if ika >= 18:     # 20 >= 18 → True
    print("Täysi-ikäinen")
```

---

## Vertailuoperaattorit

Vertailuoperaattorit vertaavat kahta arvoa.

| Operaattori | Merkitys | Esimerkki | Tulos |
|------------|----------|-----------|-------|
| `==` | Yhtä suuri kuin | `5 == 5` | `True` |
| `!=` | Eri suuri kuin | `5 != 3` | `True` |
| `>` | Suurempi kuin | `7 > 3` | `True` |
| `<` | Pienempi kuin | `3 < 7` | `True` |
| `>=` | Suurempi tai yhtä suuri | `5 >= 5` | `True` |
| `<=` | Pienempi tai yhtä suuri | `4 <= 5` | `True` |

### Esimerkkejä

```python
# Lukujen vertailu
x = 10
y = 20

print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x > y)    # False
print(x <= 10)  # True
print(y >= 20)  # True

# Merkkijonojen vertailu
nimi1 = "Anna"
nimi2 = "Pekka"

print(nimi1 == "Anna")   # True
print(nimi1 != nimi2)    # True

# HUOM: Merkkijonot vertaillaan aakkosjärjestyksessä
print("Anna" < "Pekka")  # True (A tulee ennen P:tä)
```

### Yleisiä virheitä

```python
# VÄÄRIN: Yksi =-merkki on sijoitus, ei vertailu!
x = 5
if x = 5:  # SyntaxError!
    print("Virhe!")

# OIKEIN: Kaksi =-merkkiä on vertailu
if x == 5:
    print("Oikein!")

# VÄÄRIN: Ei voi käyttää matemaattista merkintää
if 10 < x < 20:  # Toimii Pythonissa, mutta...
    print("x on välillä 10-20")

# SELVEMPI tapa:
if x > 10 and x < 20:
    print("x on välillä 10-20")
```

---

## Loogiset operaattorit

Loogiset operaattorit yhdistävät useita ehtoja.

### 1. AND (ja)

Molemmat ehdot täytyy olla tosia.

```python
ika = 25
ajokortti = True

if ika >= 18 and ajokortti:
    print("Voit vuokrata auton!")  # Tulostuu

# Totuustaulu AND:lle
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
```

### 2. OR (tai)

Vähintään yhden ehdon täytyy olla tosi.

```python
viikonloppu = True
loma = False

if viikonloppu or loma:
    print("Ei tarvitse mennä töihin!")  # Tulostuu

# Totuustaulu OR:lle
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

### 3. NOT (ei)

Kääntää totuusarvon päinvastaiseksi.

```python
saastaa = False

if not saastaa:
    print("Voit mennä ulos!")  # Tulostuu

# NOT-operaattorin käyttö
print(not True)   # False
print(not False)  # True

# Käytännön esimerkki
kirjautunut = False
if not kirjautunut:
    print("Ole hyvä ja kirjaudu sisään")
```

### Yhdistelmät

```python
ika = 22
opiskelija = True
tyossakayvä = False

# AND ja OR yhdessä
if (ika >= 18 and ika <= 65) and (opiskelija or tyossakayvä):
    print("Olet työikäinen ja joko opiskelija tai töissä")

# Monimutkaisempi esimerkki
lämpötila = 22
sade = False
tuuli = 5  # m/s

if lämpötila > 15 and not sade and tuuli < 10:
    print("Täydellinen päivä piknikille!")
```

### Suoritusjärjestys

Suoritusjärjestys (prioriteetti):
1. `not` (korkein)
2. `and`
3. `or` (matalin)

```python
# Ilman sulkeita
if True or False and False:
    print("Tämä tulostuu")  # and suoritetaan ensin

# Sulkeilla voi muuttaa järjestystä
if (True or False) and False:
    print("Tämä ei tulostu")
```

---

## Sisennyksen merkitys

Python käyttää **sisennystä** (indentation) määrittämään koodilohkot. Tämä on ainutlaatuista Pythonissa!

### Oikea sisennys

```python
# OIKEIN: 4 välilyöntiä (tai 1 tab)
if True:
    print("Tämä kuuluu if-lohkoon")
    print("Tämäkin kuuluu if-lohkoon")
print("Tämä ei kuulu if-lohkoon")

# OIKEIN: Sisäkkäiset ehdot
ika = 20
ajokortti = True

if ika >= 18:
    print("Olet täysi-ikäinen")
    if ajokortti:
        print("Voit ajaa autoa")
    print("Tämä tulostuu aina kun ika >= 18")
```

### Väärä sisennys

```python
# VÄÄRIN: Ei sisennystä
if True:
print("Virhe!")  # IndentationError

# VÄÄRIN: Epäjohdonmukainen sisennys
if True:
    print("2 välilyöntiä")
      print("4 välilyöntiä")  # IndentationError

# VÄÄRIN: Sekaisin tabit ja välilyönnit
if True:
    print("Välilyöntejä")
	print("Tabi")  # IndentationError (näyttää samalta mutta ei ole!)
```

### Hyvät käytännöt

```python
# ✅ SUOSITUS: Käytä 4 välilyöntiä
if ika >= 18:
    print("Täysi-ikäinen")
    pisteet = 100
    if pisteet > 50:
        print("Läpäisit!")

# ✅ Tyhjät rivit eivät tarvitse sisennystä
if True:
    print("Ensimmäinen rivi")

    print("Tyhjän rivin jälkeen")

# ✅ Kommentit seuraavat samaa sisennystä
if ika >= 18:
    # Tarkistetaan ajokortti
    if ajokortti:
        print("Voit ajaa")
```

**VINKKI:** Useimmat editorit (kuten VS Code) hoitavat sisennyksen automaattisesti!

---

## Käyttäjän syötteisiin perustuvat ohjelmat

Ohjelmien pitää usein tehdä päätöksiä käyttäjän syötteiden perusteella.

### Perusteet

```python
# Yksinkertainen esimerkki
nimi = input("Mikä on nimesi? ")

if nimi == "Admin":
    print("Tervetuloa, järjestelmänvalvoja!")
else:
    print(f"Tervetuloa, {nimi}!")
```

### Numeeristen syötteiden käsittely

```python
# MUISTA: input() palauttaa aina merkkijonon!
ika_str = input("Mikä on ikäsi? ")
ika = int(ika_str)  # Muunna kokonaisluvuksi

if ika >= 18:
    print("Olet täysi-ikäinen")
else:
    vuosia_jaljella = 18 - ika
    print(f"Sinulla on vielä {vuosia_jaljella} vuotta täysi-ikäisyyteen")
```

### Virheenkäsittely

```python
# Perusversio ilman virheenkäsittelyä
try:
    ika = int(input("Anna ikäsi: "))
    
    if ika < 0:
        print("Ikä ei voi olla negatiivinen!")
    elif ika > 150:
        print("Epärealistinen ikä!")
    elif ika >= 18:
        print("Olet täysi-ikäinen")
    else:
        print("Olet alaikäinen")
        
except ValueError:
    print("Virhe: Anna numero!")
```

### Merkkijonojen käsittely

```python
# Isot/pienet kirjaimet - käytä .lower() tai .upper()
vastaus = input("Haluatko jatkaa? (kyllä/ei): ").lower()

if vastaus == "kyllä" or vastaus == "k":
    print("Jatketaan...")
elif vastaus == "ei" or vastaus == "e":
    print("Lopetetaan")
else:
    print("En ymmärtänyt vastaustasi")

# Tyhjien merkkien poisto
nimi = input("Anna nimesi: ").strip()

if nimi == "":
    print("Et antanut nimeä!")
else:
    print(f"Hei, {nimi}!")
```

### Useamman syötteen käsittely

```python
print("=== ELOKUVALIPUN HINTA ===")

ika = int(input("Mikä on ikäsi? "))
opiskelija = input("Oletko opiskelija? (kyllä/ei): ").lower()

hinta = 12.00  # Perushinta

if ika < 12:
    hinta = 7.00
    print("Lasten lippu")
elif ika >= 65:
    hinta = 8.00
    print("Eläkeläisen lippu")
elif opiskelija == "kyllä":
    hinta = 9.00
    print("Opiskelijalippu")
else:
    print("Normaali lippu")

print(f"Lipun hinta: {hinta:.2f}€")
```

---

## Käytännön esimerkkejä

### Esimerkki 1: Yksinkertainen kirjautuminen

```python
print("=== KIRJAUTUMINEN ===")

kayttajatunnus = input("Käyttäjätunnus: ").strip()
salasana = input("Salasana: ")

# Oikeat tunnukset (oikeassa ohjelmassa ei näin!)
OIKEA_TUNNUS = "admin"
OIKEA_SALASANA = "salasana123"

if kayttajatunnus == OIKEA_TUNNUS and salasana == OIKEA_SALASANA:
    print("✓ Kirjautuminen onnistui!")
    print("Tervetuloa järjestelmään")
else:
    print("✗ Väärä käyttäjätunnus tai salasana")
    
    if kayttajatunnus != OIKEA_TUNNUS:
        print("Vihje: Tarkista käyttäjätunnus")
    if salasana != OIKEA_SALASANA:
        print("Vihje: Tarkista salasana")
```

### Esimerkki 2: BMI-laskuri päätöksenteolla

```python
print("=== BMI-LASKURI ===")

paino = float(input("Anna painosi (kg): "))
pituus = float(input("Anna pituutesi (m): "))

# Laske BMI
bmi = paino / (pituus ** 2)

print(f"\nBMI-indeksisi on: {bmi:.1f}")

# Tulkitse tulos
if bmi < 18.5:
    print("Luokitus: Alipaino")
    print("💡 Vinkki: Syö monipuolisesti ja ravitsevasti")
elif bmi < 25:
    print("Luokitus: Normaalipaino")
    print("✓ Hyvä! Pidä huolta terveellisistä elämäntavoista")
elif bmi < 30:
    print("Luokitus: Ylipaino")
    print("💡 Vinkki: Lisää liikuntaa ja kiinnitä huomiota ruokavalioon")
else:
    print("Luokitus: Merkittävä ylipaino")
    print("💡 Suositus: Keskustele terveydenhuollon ammattilaisen kanssa")
```

### Esimerkki 3: Yksinkertainen peli

```python
import random

print("=== ARVAA NUMERO ===")
print("Arvaa numero väliltä 1-10")

# Tietokone arpoo numeron
oikea_numero = random.randint(1, 10)

# Käyttäjä arvaa
arvaus = int(input("Anna arvauksesi: "))

if arvaus == oikea_numero:
    print("🎉 Oikein! Arvasit numeron!")
elif arvaus < oikea_numero:
    print("📈 Liian pieni! Oikea numero oli", oikea_numero)
else:
    print("📉 Liian suuri! Oikea numero oli", oikea_numero)
```

### Esimerkki 4: Arvosanamuunnin

```python
print("=== ARVOSANAMUUNNIN ===")

pisteet = int(input("Anna pisteesi (0-100): "))

# Tarkista, että pisteet ovat oikean välillä
if pisteet < 0 or pisteet > 100:
    print("Virhe: Pisteiden täytyy olla välillä 0-100")
else:
    # Määritä arvosana
    if pisteet >= 90:
        arvosana = 5
        selite = "Kiitettävä"
    elif pisteet >= 80:
        arvosana = 4
        selite = "Hyvä"
    elif pisteet >= 70:
        arvosana = 3
        selite = "Tyydyttävä"
    elif pisteet >= 60:
        arvosana = 2
        selite = "Välttävä"
    elif pisteet >= 50:
        arvosana = 1
        selite = "Heikko"
    else:
        arvosana = 0
        selite = "Hylätty"
    
    print(f"\nPisteet: {pisteet}")
    print(f"Arvosana: {arvosana} - {selite}")
    
    # Lisäpalaute
    if arvosana >= 4:
        print("🌟 Erinomaista työtä!")
    elif arvosana >= 2:
        print("👍 Hyvä suoritus!")
    elif arvosana == 1:
        print("📚 Läpäisit, mutta harjoittele lisää")
    else:
        print("💪 Yritä uudelleen!")
```

### Esimerkki 5: Kaupan alennuslaskuri

```python
print("=== KAUPAN ALENNUSLASKURI ===")

ostokset = float(input("Ostoksen summa (€): "))
asiakaskortti = input("Onko sinulla asiakaskortti? (kyllä/ei): ").lower()
viikonpaiva = input("Mikä viikonpäivä tänään on? ").lower()

alennus_prosentti = 0

# Asiakaskortin perusalennus
if asiakaskortti == "kyllä":
    alennus_prosentti = 5
    print("✓ Asiakaskorttialennus: 5%")

# Lisäalennukset
if viikonpaiva == "tiistai":
    alennus_prosentti += 10
    print("✓ Tiistaialennus: 10%")

# Suurten ostosten alennus
if ostokset > 100:
    alennus_prosentti += 5
    print("✓ Suuralennus (yli 100€): 5%")

# Laske lopullinen hinta
if alennus_prosentti > 0:
    alennus_euroina = ostokset * (alennus_prosentti / 100)
    loppusumma = ostokset - alennus_euroina
    
    print(f"\n{'=' * 30}")
    print(f"Alkuperäinen hinta: {ostokset:.2f}€")
    print(f"Alennukset yhteensä: {alennus_prosentti}%")
    print(f"Säästit: {alennus_euroina:.2f}€")
    print(f"{'=' * 30}")
    print(f"MAKSETTAVA: {loppusumma:.2f}€")
else:
    print(f"\nMaksettava: {ostokset:.2f}€")
    print("Ei alennuksia tällä kertaa")
```

---

## Yhteenveto

### Tärkeimmät oppipisteet:

1. **If-lause**: Suorittaa koodin vain, jos ehto on tosi
   ```python
   if ehto:
       # koodi
   ```

2. **Elif-lause**: Testaa vaihtoehtoisen ehdon
   ```python
   if ehto1:
       # koodi1
   elif ehto2:
       # koodi2
   ```

3. **Else-lause**: Suoritetaan, jos mikään ehto ei toteudu
   ```python
   if ehto:
       # koodi1
   else:
       # koodi2
   ```

4. **Vertailuoperaattorit**: `==`, `!=`, `>`, `<`, `>=`, `<=`

5. **Loogiset operaattorit**: `and`, `or`, `not`

6. **Sisennys**: 4 välilyöntiä määrittää koodilohkon

7. **Input-käsittely**: Muista muuntaa tietotyypit ja käsitellä virheet

### Muistisäännöt:

- ✅ Käytä `==` vertailuun, ei `=`
- ✅ Muista kaksoispiste `:` ehdon perässä
- ✅ Sisennä koodi 4 välilyönnillä
- ✅ Käytä `.lower()` merkkijonojen vertailussa
- ✅ Muunna `input()` oikeaan tietotyyppiin

## Seuraavaksi
Siirry [Harjoitukset](Harjoitukset/)-kansioon ja tee luvun tehtävät.