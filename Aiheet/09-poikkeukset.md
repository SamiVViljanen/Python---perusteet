# Poikkeukset ja virheiden käsittely (Exceptions)

## Sisällysluettelo
1. [Mitä ovat virheet ja poikkeukset?](#mitä-ovat-virheet-ja-poikkeukset)
2. [Yleisimmät poikkeustyypit](#yleisimmät-poikkeustyypit)
3. [Try-Except-rakenne](#try-except-rakenne)
4. [Finally-lohko](#finally-lohko)
5. [Else-lohko try-rakenteessa](#else-lohko-try-rakenteessa)
6. [Useiden poikkeusten käsittely](#useiden-poikkeusten-käsittely)
7. [Poikkeuksen tietojen käyttö](#poikkeuksen-tietojen-käyttö)
8. [Käytännön sovelluksia](#käytännön-sovelluksia)
9. [Hyvät käytännöt](#hyvät-käytännöt)
10. [Yhteenveto](#yhteenveto)

---

Tässä oppaassa opit, mitä virheet ja poikkeukset ovat, miten niitä käsitellään ja miten teet ohjelmia, jotka toimivat luotettavasti myös virhetilanteissa.

## Mitä ovat virheet ja poikkeukset?

**Virhe** (error) tai **poikkeus** (exception) on tilanne, jossa ohjelma kohtaa ongelman eikä voi jatkaa normaalisti.

### Kaksi päätyyppiä:

**1. Syntaksivirheet** - koodi on kirjoitettu väärin:
```python
# VÄÄRIN: Puuttuva kaksoispiste
if x > 5
    print("Suuri")  # SyntaxError

# VÄÄRIN: Virheellinen sisennys
if True:
print("Virhe")  # IndentationError
```
Syntaksivirheet **täytyy korjata** ennen kuin ohjelma toimii.

**2. Ajonaikaiset virheet** (runtime errors) - koodi on oikein, mutta jotain menee pieleen suorituksen aikana:
```python
# Koodi näyttää oikealta, mutta...
luku = int("abc")  # ValueError: ei voi muuntaa tekstiä luvuksi

tulos = 10 / 0  # ZeroDivisionError: ei voi jakaa nollalla

lista = [1, 2, 3]
print(lista[10])  # IndexError: indeksi liian suuri
```

### Miksi virheiden käsittely on tärkeää?

Ilman virheiden käsittelyä ohjelma **kaatuu** ja käyttäjä näkee pelottavan virheviestin:

```python
# Ilman virheiden käsittelyä
ika = int(input("Anna ikäsi: "))  # Jos käyttäjä kirjoittaa "kaksi"
# Traceback (most recent call last):
#   File "ohjelma.py", line 1, in <module>
#     ika = int(input("Anna ikäsi: "))
# ValueError: invalid literal for int() with base 10: 'kaksi'
# OHJELMA KAATUU! ❌
```

Virheiden käsittelyn kanssa ohjelma **jatkaa toimintaa** ja antaa käyttäjäystävällisen viestin:

```python
# Virheiden käsittelyn kanssa
try:
    ika = int(input("Anna ikäsi: "))
except ValueError:
    print("Virhe: Anna ikä numeroina, esim. 25")
    # OHJELMA JATKAA! ✅
```

## Yleisimmät poikkeustyypit

Pythonissa on kymmeniä erilaisia poikkeuksia. Tässä yleisimmät:

### ValueError
Arvo on väärää tyyppiä tai muotoa:
```python
# Esimerkki 1: Virheellinen muunnos
luku = int("teksti")  # ValueError

# Esimerkki 2: Virheellinen desimaaliluku
numero = float("1.2.3")  # ValueError
```

### ZeroDivisionError
Yritys jakaa nollalla:
```python
tulos = 10 / 0  # ZeroDivisionError
keskiarvo = summa / 0  # ZeroDivisionError
```

### TypeError
Väärä tietotyyppi operaatiossa:
```python
# Ei voi yhdistellä merkkijonoa ja lukua
tulos = "Ikä: " + 25  # TypeError

# Ei voi kertoa merkkijonoa liukuluvulla
teksti = "Hei" * 2.5  # TypeError
```

### IndexError
Yritys käyttää indeksiä, jota ei ole olemassa:
```python
lista = [1, 2, 3]
print(lista[10])  # IndexError: list index out of range

# Tyhjä lista
tyhjä = []
print(tyhjä[0])  # IndexError
```

### KeyError
Yritetään hakea sanakirjasta avainta, jota ei ole:
```python
henkilö = {"nimi": "Anna", "ikä": 25}
print(henkilö["osoite"])  # KeyError: 'osoite'
```

### NameError
Muuttuja tai funktio ei ole määritelty:
```python
print(muuttuja)  # NameError: name 'muuttuja' is not defined

funktio()  # NameError: name 'funktio' is not defined
```

### FileNotFoundError
Tiedostoa ei löydy:
```python
with open("ei_ole_olemassa.txt", "r") as f:
    sisältö = f.read()  # FileNotFoundError
```

### AttributeError
Objektilla ei ole pyydettyä attribuuttia tai metodia:
```python
luku = 5
luku.append(10)  # AttributeError: 'int' object has no attribute 'append'
```

## Try-Except-rakenne

`try-except` on Pythonin tapa käsitellä virheitä.

### Perussyntaksi

```python
try:
    # Koodi, joka saattaa aiheuttaa virheen
    luku = int(input("Anna luku: "))
except:
    # Mitä tehdään, jos virhe tapahtuu
    print("Virhe tapahtui!")
```

### Toimintaperiaate

1. Python **yrittää** suorittaa `try`-lohkon koodin
2. Jos virhe tapahtuu, Python **hyppää** `except`-lohkoon
3. Ohjelma **jatkaa normaalisti** except-lohkon jälkeen

```python
print("Ohjelma alkaa")

try:
    tulos = 10 / 0  # Tämä aiheuttaa virheen
    print("Tämä ei tulostu")  # Tätä ei suoriteta
except:
    print("Virhe tapahtui!")  # Tämä suoritetaan

print("Ohjelma jatkuu")  # Tämä suoritetaan
```

**Tulostus:**
```
Ohjelma alkaa
Virhe tapahtui!
Ohjelma jatkuu
```

### Tietyn poikkeuksen käsittely

On parempi käsitellä **tietty** poikkeus kuin kaikki:

```python
try:
    ika = int(input("Anna ikäsi: "))
    print(f"Olet {ika} vuotta vanha")
except ValueError:
    print("Virhe: Anna ikä numeroina!")
```

**Miksi tämä on parempi?**
- Vain `ValueError` käsitellään
- Muut virheet (esim. `KeyboardInterrupt`) toimivat normaalisti
- Koodi on selkeämpi

### Käytännön esimerkki: Turvallinen luvun syöttö

```python
print("=== LASKURI ===")

try:
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))
    tulos = luku1 + luku2
    print(f"Summa: {tulos}")
except ValueError:
    print("Virhe: Molempien täytyy olla numeroita!")

print("Kiitos ohjelman käytöstä!")
```

**Ilman virhettä:**
```
=== LASKURI ===
Anna ensimmäinen luku: 5
Anna toinen luku: 3
Summa: 8
Kiitos ohjelman käytöstä!
```

**Virheen kanssa:**
```
=== LASKURI ===
Anna ensimmäinen luku: 5
Anna toinen luku: kaksi
Virhe: Molempien täytyy olla numeroita!
Kiitos ohjelman käytöstä!
```

## Finally-lohko

`finally`-lohko suoritetaan **aina**, riippumatta siitä tapahtuuko virhe vai ei.

### Syntaksi

```python
try:
    # Kokeile tätä
    koodi
except:
    # Jos virhe tapahtuu
    virheenkäsittely
finally:
    # Suoritetaan AINA
    siivous
```

### Milloin käyttää finally?

`finally` on hyödyllinen, kun täytyy:
- Sulkea tiedostoja
- Sulkea tietokantayhteyksiä
- Vapauttaa resursseja
- Kirjata lokitiedot

### Esimerkki 1: Yksinkertainen

```python
try:
    luku = int(input("Anna luku: "))
    tulos = 100 / luku
    print(f"Tulos: {tulos}")
except ValueError:
    print("Virhe: Anna numero!")
except ZeroDivisionError:
    print("Virhe: Et voi jakaa nollalla!")
finally:
    print("Laskin suljetaan...")
```

**Tulostus (onnistunut):**
```
Anna luku: 5
Tulos: 20.0
Laskin suljetaan...
```

**Tulostus (virhe):**
```
Anna luku: teksti
Virhe: Anna numero!
Laskin suljetaan...
```

### Esimerkki 2: Tiedoston käsittely

```python
tiedosto = None

try:
    print("Avataan tiedosto...")
    tiedosto = open("data.txt", "r")
    sisältö = tiedosto.read()
    print(sisältö)
except FileNotFoundError:
    print("Virhe: Tiedostoa ei löydy!")
except PermissionError:
    print("Virhe: Ei oikeuksia lukea tiedostoa!")
finally:
    # Suljetaan tiedosto aina
    if tiedosto is not None:
        tiedosto.close()
        print("Tiedosto suljettu")
```

### Esimerkki 3: Finally suoritetaan aina

```python
def jaa_luvut(a, b):
    try:
        print("Yritetään jakaa...")
        tulos = a / b
        return tulos
    except ZeroDivisionError:
        print("Virhe: Jakaja ei voi olla nolla!")
        return None
    finally:
        print("Finally-lohko suoritetaan")  # Tämä tulostuu AINA

print(jaa_luvut(10, 2))
# Yritetään jakaa...
# Finally-lohko suoritetaan
# 5.0

print(jaa_luvut(10, 0))
# Yritetään jakaa...
# Virhe: Jakaja ei voi olla nolla!
# Finally-lohko suoritetaan
# None
```

## Else-lohko try-rakenteessa

`else`-lohko suoritetaan, jos **ei tapahdu virhettä**.

### Syntaksi

```python
try:
    # Kokeile tätä
    koodi
except:
    # Jos virhe tapahtuu
    virheenkäsittely
else:
    # Jos EI tapahdu virhettä
    onnistuminen
finally:
    # Suoritetaan aina
    siivous
```

### Esimerkki

```python
try:
    luku = int(input("Anna luku: "))
except ValueError:
    print("Virhe: Anna numero!")
else:
    # Tämä suoritetaan vain, jos ei tapahdu virhettä
    print(f"Sait luvun: {luku}")
    print(f"Luvun neliö on: {luku ** 2}")
finally:
    print("Kiitos!")
```

**Onnistunut syöttö:**
```
Anna luku: 5
Sait luvun: 5
Luvun neliö on: 25
Kiitos!
```

**Virheellinen syöttö:**
```
Anna luku: teksti
Virhe: Anna numero!
Kiitos!
```

### Milloin käyttää else?

`else` on hyödyllinen, kun haluat:
- Erottaa normaalin toiminnan virheenkäsittelystä
- Suorittaa koodia vain, jos kaikki meni hyvin
- Tehdä koodista selkeämmän

```python
# Ilman else - epäselvää
try:
    tiedosto = open("data.txt", "r")
    sisältö = tiedosto.read()  # Onko tämä try:n vai normaalin koodin osa?
    print(sisältö)
    tiedosto.close()
except FileNotFoundError:
    print("Tiedostoa ei löydy")

# Else:n kanssa - selkeämpää
try:
    tiedosto = open("data.txt", "r")
except FileNotFoundError:
    print("Tiedostoa ei löydy")
else:
    # Nämä suoritetaan vain, jos tiedosto avautui
    sisältö = tiedosto.read()
    print(sisältö)
    tiedosto.close()
```

## Useiden poikkeusten käsittely

Voit käsitellä useita eri poikkeuksia samassa `try-except`-rakenteessa.

### Tapa 1: Erilliset except-lohkot

```python
try:
    luku = int(input("Anna luku: "))
    tulos = 100 / luku
    print(f"100 / {luku} = {tulos}")
except ValueError:
    print("Virhe: Anna numero!")
except ZeroDivisionError:
    print("Virhe: Et voi jakaa nollalla!")
```

### Tapa 2: Sama käsittely usealle poikkeukselle

```python
try:
    # Koodi
    ...
except (ValueError, TypeError, ZeroDivisionError):
    print("Tapahtui jokin näistä virheistä!")
```

### Tapa 3: Yleinen poikkeus lopussa

```python
try:
    luku = int(input("Anna luku: "))
    tulos = 100 / luku
    lista = [1, 2, 3]
    print(lista[luku])
except ValueError:
    print("Virhe: Anna numero!")
except ZeroDivisionError:
    print("Virhe: Et voi jakaa nollalla!")
except IndexError:
    print("Virhe: Luku on liian suuri listalle!")
except Exception as e:
    # Kaikkien muiden virheiden käsittely
    print(f"Odottamaton virhe: {e}")
```

**TÄRKEÄÄ:** Erityiset poikkeukset **ensin**, yleiset **lopussa**!

### Käytännön esimerkki: Tiedoston lukeminen

```python
def lue_tiedosto(tiedostonimi):
    try:
        with open(tiedostonimi, "r", encoding="utf-8") as f:
            sisältö = f.read()
            return sisältö
    except FileNotFoundError:
        print(f"Virhe: Tiedostoa '{tiedostonimi}' ei löydy")
        return None
    except PermissionError:
        print(f"Virhe: Ei oikeuksia lukea tiedostoa '{tiedostonimi}'")
        return None
    except UnicodeDecodeError:
        print(f"Virhe: Tiedoston merkistö on virheellinen")
        return None
    except Exception as e:
        print(f"Odottamaton virhe: {e}")
        return None

# Käyttö
sisältö = lue_tiedosto("data.txt")
if sisältö:
    print(sisältö)
```

## Poikkeuksen tietojen käyttö

Voit tallentaa poikkeuksen muuttujaan ja käyttää sen tietoja.

### Syntaksi

```python
try:
    koodi
except PoikkeustyyppiException as e:
    # 'e' sisältää virheen tiedot
    print(f"Virhe: {e}")
```

### Esimerkki 1: Virheviestin tulostus

```python
try:
    luku = int("abc")
except ValueError as e:
    print(f"Tapahtui virhe: {e}")
    # Tulostaa: Tapahtui virhe: invalid literal for int() with base 10: 'abc'
```

### Esimerkki 2: Yksityiskohtainen virheilmoitus

```python
try:
    with open("ei_ole.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print("=" * 40)
    print("VIRHE: Tiedostoa ei löydy")
    print("=" * 40)
    print(f"Yksityiskohdat: {e}")
    print(f"Tiedosto: {e.filename}")
    print("=" * 40)
```

**Tulostus:**
```
========================================
VIRHE: Tiedostoa ei löydy
========================================
Yksityiskohdat: [Errno 2] No such file or directory: 'ei_ole.txt'
Tiedosto: ei_ole.txt
========================================
```

### Esimerkki 3: Virhelokin kirjoitus

```python
import datetime

def tallenna_virhe_lokiin(virhe):
    with open("virhe_loki.txt", "a", encoding="utf-8") as f:
        aika = datetime.datetime.now()
        f.write(f"[{aika}] {virhe}\n")

try:
    tulos = 10 / 0
except ZeroDivisionError as e:
    print("Ohjelma kohtasi virheen")
    tallenna_virhe_lokiin(f"ZeroDivisionError: {e}")
    print("Virhe tallennettu lokiin")
```

## Käytännön sovelluksia

### Sovellus 1: Turvallinen numeroiden syöttö

```python
def kysy_luku(viesti, min_arvo=None, max_arvo=None):
    """
    Kysyy käyttäjältä lukua, kunnes saadaan kelvollinen arvo.
    Ohjelma ei kaadu virheellisestä syötteestä.
    """
    while True:
        try:
            luku = int(input(viesti))
            
            # Tarkista rajat
            if min_arvo is not None and luku < min_arvo:
                print(f"Luvun täytyy olla vähintään {min_arvo}")
                continue
            
            if max_arvo is not None and luku > max_arvo:
                print(f"Luvun täytyy olla enintään {max_arvo}")
                continue
            
            return luku
            
        except ValueError:
            print("Virhe: Anna numero!")

# Käyttö
ika = kysy_luku("Anna ikäsi: ", min_arvo=0, max_arvo=150)
print(f"Ikäsi on {ika} vuotta")
```

**Esimerkki käytöstä:**
```
Anna ikäsi: teksti
Virhe: Anna numero!
Anna ikäsi: -5
Luvun täytyy olla vähintään 0
Anna ikäsi: 200
Luvun täytyy olla enintään 150
Anna ikäsi: 25
Ikäsi on 25 vuotta
```

### Sovellus 2: Turvallinen laskutoimitus

```python
print("=== YKSINKERTAINEN LASKIN ===")
print("Lasku päättyy kun kirjoitat 'lopeta'")
print()

while True:
    try:
        # Kysy syöte
        syöte = input("Anna lasku (esim. 5 + 3) tai 'lopeta': ").strip()
        
        # Lopetus
        if syöte.lower() == "lopeta":
            print("Kiitos käytöstä!")
            break
        
        # Laske tulos
        # VAROITUS: eval() on turvaton oikeissa ohjelmissa!
        # Käytetään vain oppimistarkoituksessa
        tulos = eval(syöte)
        print(f"Tulos: {tulos}")
        print()
        
    except ZeroDivisionError:
        print("❌ Virhe: Et voi jakaa nollalla!")
        print()
    except (ValueError, SyntaxError, NameError):
        print("❌ Virhe: Virheellinen laskutoimitus!")
        print("💡 Vinkki: Käytä muotoa: luku operaattori luku")
        print("   Esim: 5 + 3, 10 - 2, 6 * 4, 8 / 2")
        print()
    except Exception as e:
        print(f"❌ Odottamaton virhe: {e}")
        print()
```

### Sovellus 3: Tiedoston käsittely

```python
def kopioi_tiedosto(lähde, kohde):
    """
    Kopioi tiedoston sisällön toiseen tiedostoon.
    Käsittelee virheet ja ilmoittaa käyttäjälle.
    """
    lähde_tiedosto = None
    kohde_tiedosto = None
    
    try:
        print(f"Kopioidaan '{lähde}' -> '{kohde}'...")
        
        # Avaa lähdetiedosto lukemista varten
        lähde_tiedosto = open(lähde, "r", encoding="utf-8")
        
        # Avaa kohdetiedosto kirjoitusta varten
        kohde_tiedosto = open(kohde, "w", encoding="utf-8")
        
        # Kopioi sisältö
        sisältö = lähde_tiedosto.read()
        kohde_tiedosto.write(sisältö)
        
        print("✓ Kopiointi onnistui!")
        return True
        
    except FileNotFoundError:
        print(f"❌ Virhe: Tiedostoa '{lähde}' ei löydy")
        return False
        
    except PermissionError as e:
        print(f"❌ Virhe: Ei oikeuksia tiedostoon")
        print(f"   Yksityiskohdat: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Odottamaton virhe: {e}")
        return False
        
    finally:
        # Suljetaan tiedostot aina
        if lähde_tiedosto is not None:
            lähde_tiedosto.close()
        if kohde_tiedosto is not None:
            kohde_tiedosto.close()
        print("Tiedostot suljettu")

# Käyttö
kopioi_tiedosto("alkuperainen.txt", "kopio.txt")
```

### Sovellus 4: Käyttäjätietojen validointi

```python
def rekisteröi_käyttäjä():
    """
    Rekisteröi uusi käyttäjä validoimalla syötteet.
    Ohjelma ei kaadu virheellisistä syötteistä.
    """
    print("=== KÄYTTÄJÄN REKISTERÖINTI ===\n")
    
    # Käyttäjätunnus
    while True:
        käyttäjätunnus = input("Käyttäjätunnus (3-20 merkkiä): ").strip()
        
        if len(käyttäjätunnus) < 3:
            print("❌ Liian lyhyt! Vähintään 3 merkkiä.\n")
            continue
        if len(käyttäjätunnus) > 20:
            print("❌ Liian pitkä! Enintään 20 merkkiä.\n")
            continue
        if not käyttäjätunnus.isalnum():
            print("❌ Vain kirjaimia ja numeroita!\n")
            continue
        break
    
    # Ikä
    while True:
        try:
            ikä = int(input("Ikä: "))
            if ikä < 13:
                print("❌ Täytyy olla vähintään 13-vuotias!\n")
                continue
            if ikä > 120:
                print("❌ Epärealistinen ikä!\n")
                continue
            break
        except ValueError:
            print("❌ Anna ikä numeroina!\n")
    
    # Sähköposti
    while True:
        email = input("Sähköposti: ").strip().lower()
        
        if "@" not in email or "." not in email:
            print("❌ Virheellinen sähköpostiosoite!\n")
            continue
        break
    
    # Rekisteröinti onnistui
    print("\n" + "=" * 40)
    print("✓ REKISTERÖINTI ONNISTUI!")
    print("=" * 40)
    print(f"Käyttäjätunnus: {käyttäjätunnus}")
    print(f"Ikä: {ikä}")
    print(f"Sähköposti: {email}")
    print("=" * 40)
    
    return {
        "käyttäjätunnus": käyttäjätunnus,
        "ikä": ikä,
        "email": email
    }

# Käyttö
käyttäjä = rekisteröi_käyttäjä()
```

### Sovellus 5: JSON-datan käsittely

```python
import json

def lataa_asetukset(tiedosto="asetukset.json"):
    """
    Lataa asetukset JSON-tiedostosta.
    Jos tiedostoa ei ole tai se on virheellinen, palautetaan oletukset.
    """
    oletusasetukset = {
        "kieli": "suomi",
        "teema": "vaalea",
        "äänenvoimakkuus": 50
    }
    
    try:
        with open(tiedosto, "r", encoding="utf-8") as f:
            asetukset = json.load(f)
            print(f"✓ Asetukset ladattu tiedostosta '{tiedosto}'")
            return asetukset
            
    except FileNotFoundError:
        print(f"⚠ Tiedostoa '{tiedosto}' ei löydy")
        print("→ Käytetään oletusasetuksia")
        return oletusasetukset
        
    except json.JSONDecodeError as e:
        print(f"❌ Virheellinen JSON-muoto:")
        print(f"   Rivi {e.lineno}, sarake {e.colno}")
        print(f"   {e.msg}")
        print("→ Käytetään oletusasetuksia")
        return oletusasetukset
        
    except Exception as e:
        print(f"❌ Odottamaton virhe: {e}")
        print("→ Käytetään oletusasetuksia")
        return oletusasetukset

def tallenna_asetukset(asetukset, tiedosto="asetukset.json"):
    """
    Tallentaa asetukset JSON-tiedostoon.
    """
    try:
        with open(tiedosto, "w", encoding="utf-8") as f:
            json.dump(asetukset, f, indent=2, ensure_ascii=False)
            print(f"✓ Asetukset tallennettu tiedostoon '{tiedosto}'")
            return True
            
    except PermissionError:
        print(f"❌ Ei oikeuksia kirjoittaa tiedostoon '{tiedosto}'")
        return False
        
    except Exception as e:
        print(f"❌ Virhe tallennettaessa: {e}")
        return False

# Käyttö
asetukset = lataa_asetukset()
print(f"\nNykyiset asetukset: {asetukset}")

# Muokkaa ja tallenna
asetukset["teema"] = "tumma"
tallenna_asetukset(asetukset)
```

## Hyvät käytännöt

### 1. Käsittele vain tarvittavat poikkeukset

```python
# ❌ VÄLTÄ: Liian laaja
try:
    koodi
except:  # Käsittelee KAIKKI virheet, myös Ctrl+C
    print("Virhe")

# ✅ PAREMPI: Tietty poikkeus
try:
    luku = int(input("Anna luku: "))
except ValueError:
    print("Virhe: Anna numero!")
```

### 2. Pidä try-lohko pienenä

```python
# ❌ VÄLTÄ: Liikaa koodia try-lohkossa
try:
    luku = int(input("Anna luku: "))
    tulos = luku * 2
    print(f"Tulos: {tulos}")
    lista = [1, 2, 3]
    print(lista[0])
    # ...paljon lisää koodia
except ValueError:
    print("Virhe")

# ✅ PAREMPI: Vain riskialtis koodi try:ssä
try:
    luku = int(input("Anna luku: "))
except ValueError:
    print("Virhe: Anna numero!")
else:
    tulos = luku * 2
    print(f"Tulos: {tulos}")
    lista = [1, 2, 3]
    print(lista[0])
```

### 3. Anna selkeitä virheilmoituksia

```python
# ❌ VÄLTÄ: Epäselvä viesti
try:
    luku = int(input("Anna luku: "))
except ValueError:
    print("Virhe")

# ✅ PAREMPI: Selkeä ja ohjaava viesti
try:
    luku = int(input("Anna luku: "))
except ValueError:
    print("❌ Virhe: Syötä numero, esim. 42")
    print("💡 Vinkki: Älä käytä kirjaimia tai erikoismerkkejä")
```

### 4. Käytä finally-lohkoa resurssien vapauttamiseen

```python
# ✅ HYVÄ: Finally varmistaa sulkemisen
tiedosto = None
try:
    tiedosto = open("data.txt", "r")
    sisältö = tiedosto.read()
except FileNotFoundError:
    print("Tiedostoa ei löydy")
finally:
    if tiedosto is not None:
        tiedosto.close()

# ✅ VIELÄ PAREMPI: with-lause hoitaa sulkemisen automaattisesti
try:
    with open("data.txt", "r") as tiedosto:
        sisältö = tiedosto.read()
except FileNotFoundError:
    print("Tiedostoa ei löydy")
```

### 5. Älä piilota virheitä

```python
# ❌ VÄLTÄ: Virhe piilotetaan
try:
    tärkeä_toiminto()
except:
    pass  # Ei tehdä mitään - VAARALLISTA!

# ✅ PAREMPI: Ilmoita virheestä
try:
    tärkeä_toiminto()
except Exception as e:
    print(f"Virhe: {e}")
    # tai lokitiedostoon:
    # logging.error(f"Virhe: {e}")
```

### 6. Dokumentoi poikkeukset funktioissa

```python
def jaa_luvut(a, b):
    """
    Jakaa luvun a luvulla b.
    
    Args:
        a: Jaettava (float tai int)
        b: Jakaja (float tai int)
    
    Returns:
        Jakolaskun tulos (float)
    
    Raises:
        ZeroDivisionError: Jos b on 0
        TypeError: Jos a tai b ei ole numero
    """
    if b == 0:
        raise ZeroDivisionError("Jakaja ei voi olla nolla")
    return a / b
```

### 7. Käytä erityisiä poikkeuksia yleiset jälkeen

```python
# ❌ VÄÄRIN: Yleinen ensin
try:
    koodi
except Exception:  # Tämä käsittelee KAIKKI
    print("Yleinen virhe")
except ValueError:  # Tätä ei koskaan saavuteta!
    print("ValueError")

# ✅ OIKEIN: Erityiset ensin
try:
    koodi
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except Exception:  # Viimeisenä
    print("Muu virhe")
```

## Yhteenveto

### Mitä opimme?

1. **Virheet ja poikkeukset** tapahtuvat, kun ohjelma kohtaa ongelman
2. **try-except** käsittelee virheet ilman että ohjelma kaatuu
3. **finally** suoritetaan aina (hyödyllinen siivouksessa)
4. **else** suoritetaan, jos ei tapahdu virhettä
5. **Useita poikkeuksia** voi käsitellä samassa rakenteessa
6. **Poikkeuksen tiedot** voi tallentaa ja käyttää

### Try-Except-rakenne yhteenveto

```python
try:
    # Koodi, joka saattaa aiheuttaa virheen
    luku = int(input("Anna luku: "))
    tulos = 100 / luku
    
except ValueError:
    # Käsitellään muunnosvirhe
    print("Anna numero!")
    
except ZeroDivisionError:
    # Käsitellään jakovirhe
    print("Et voi jakaa nollalla!")
    
except Exception as e:
    # Kaikki muut virheet
    print(f"Virhe: {e}")
    
else:
    # Suoritetaan jos EI tapahdu virhettä
    print(f"Tulos: {tulos}")
    
finally:
    # Suoritetaan AINA
    print("Valmis!")
```

### Yleisimmät poikkeukset

| Poikkeus | Syy | Esimerkki |
|----------|-----|-----------|
| `ValueError` | Väärä arvo | `int("abc")` |
| `ZeroDivisionError` | Jako nollalla | `10 / 0` |
| `TypeError` | Väärä tyyppi | `"5" + 5` |
| `IndexError` | Indeksi liian suuri | `lista[100]` |
| `KeyError` | Avainta ei löydy | `sanakirja["ei_ole"]` |
| `FileNotFoundError` | Tiedostoa ei löydy | `open("ei_ole.txt")` |
| `NameError` | Muuttuja ei määritelty | `print(x)` |

### Virheiden käsittelyn hyödyt

✅ **Ohjelma ei kaadu** - toimii myös virhetilanteissa
✅ **Parempi käyttäjäkokemus** - selkeät virheilmoitukset
✅ **Helpompi debuggaus** - tiedät missä ja miksi virhe tapahtui
✅ **Luotettavampi ohjelma** - käsittelee odottamattomat tilanteet

### Muistilista

1. **Ennalta ehkäise** - Tarkista arvot ennen käyttöä kun mahdollista
2. **Käsittele virheet** - Käytä try-except kun virhe on mahdollinen
3. **Ole spesifi** - Käsittele tietyt poikkeukset, ei kaikkia
4. **Anna ohjeita** - Kerro käyttäjälle mitä tehdä
5. **Vapauta resurssit** - Käytä finally tai with-lausetta
6. **Älä piilota** - Lokita tai ilmoita virheistä
7. **Testaa virheet** - Kokeile ohjelmaa virheellisillä syötteillä

### Harjoitustehtäviä

1. **Turvallinen yhteenlasku**: Tee ohjelma, joka kysyy kaksi lukua ja laskee summan. Käsittele tilanteet, joissa syöte ei ole numero.

2. **Tiedoston lukija**: Tee funktio, joka lukee tekstit tiedostosta. Käsittele tilanteet, joissa tiedostoa ei löydy tai sitä ei voi lukea.

3. **Lista-indeksin hakija**: Tee ohjelma, joka kysyy listan indeksin ja tulostaa sen arvon. Käsittele tilanteet, joissa indeksi on liian suuri.

4. **Sanakirjan haku**: Luo sanakirja ja hae siitä arvoja. Käsittele tilanne, jossa avainta ei löydy.

5. **Laskin finally:llä**: Tee laskin, joka tulostaa "Laskin suljetaan" aina lopussa, tapahtuipa virhe tai ei.

Muista: Hyvä ohjelma **epäonnistuu elegantisti** - se kertoo käyttäjälle mitä tapahtui ja miten jatkaa!

🚀 Onnea ohjelmointiin!
