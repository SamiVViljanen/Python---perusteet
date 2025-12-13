# Vastaukset: Poikkeukset

Tässä kansiossa on kaikkien harjoitusten mallivastaukset sekä selitykset.

---

## Harjoitus 1: Turvallinen jako ⭐

### Ratkaisu
[harjoitus1.py](harjoitus1.py)

```python
try:
    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))
    tulos = luku1 / luku2
    print(f"Tulos: {tulos}")
except ValueError:
    print("Virhe: Anna molemmat luvut numeroina!")
except ZeroDivisionError:
    print("Virhe: Et voi jakaa nollalla!")
```

### Selitys
- **try-lohko:** Sisältää koodin joka saattaa aiheuttaa virheen
- **ValueError:** Tapahtuu jos `float()` ei voi muuntaa syötettä luvuksi (esim. "teksti")
- **ZeroDivisionError:** Tapahtuu jos yritetään jakaa nollalla
- **Kaksi erillistä except:** Eri virheille eri käsittely ja viesti

### Miksi float() eikä int()?

```python
float(input("..."))  # Hyväksyy: 5, 5.5, 3.14
int(input("..."))    # Hyväksyy vain: 5, 10, 42 (ei desimaaleja)
```

Käytämme `float()` koska jako antaa usein desimaalilukuja.

### Mitä tapahtuu missäkin tilanteessa?

**Tilanne 1: Onnistunut jako**
```
Anna ensimmäinen luku: 10
Anna toinen luku: 2
Tulos: 5.0
```
→ Ei virhettä, ohjelma toimii normaalisti

**Tilanne 2: Ei numero**
```
Anna ensimmäinen luku: teksti
```
→ `float("teksti")` → `ValueError` → Tulostetaan "Virhe: Anna molemmat luvut numeroina!"

**Tilanne 3: Jako nollalla**
```
Anna ensimmäinen luku: 10
Anna toinen luku: 0
```
→ `10 / 0` → `ZeroDivisionError` → Tulostetaan "Virhe: Et voi jakaa nollalla!"

### Vaihtoehtoinen ratkaisu (yksityiskohtaisemmat viestit)

```python
try:
    luku1_str = input("Anna ensimmäinen luku: ")
    luku1 = float(luku1_str)
    
    luku2_str = input("Anna toinen luku: ")
    luku2 = float(luku2_str)
    
    tulos = luku1 / luku2
    print(f"Tulos: {tulos}")
    
except ValueError as e:
    print("Virhe: Anna molemmat luvut numeroina!")
    print(f"Yksityiskohdat: {e}")
except ZeroDivisionError:
    print("Virhe: Et voi jakaa nollalla!")
    print("Yritä uudelleen nollasta poikkeavalla luvulla.")
```

### Opittavaa
✅ `try-except` estää ohjelman kaatumisen  
✅ Eri virheille voi olla eri `except`-lohkot  
✅ Käyttäjäystävälliset virheilmoitukset parantavat käyttökokemusta  
💡 Aina kun käsittelet käyttäjän syötettä, varaudu virheisiin!

---

## Harjoitus 2: Listan käsittely ⭐⭐

### Ratkaisu
[harjoitus2.py](harjoitus2.py)

```python
lista = ["omena", "banaani", "päärynä", "appelsiini", "kiivi"]

print(f"Lista: {lista}")

try:
    indeksi = int(input("Anna indeksi (0-4): "))
    arvo = lista[indeksi]
    print(f"Arvo: {arvo}")
except ValueError:
    print("Virhe: Anna numero!")
except IndexError:
    print("Virhe: Indeksi on liian suuri! Käytä arvoja 0-4.")
```

### Selitys
- **ValueError:** Tapahtuu jos `int()` ei voi muuntaa syötettä luvuksi
- **IndexError:** Tapahtuu jos indeksi on liian suuri tai liian pieni
- **lista[indeksi]:** Hakee listan arvon kyseisestä indeksistä

### Milloin IndexError tapahtuu?

```python
lista = ["a", "b", "c"]  # Indeksit: 0, 1, 2

lista[0]   # OK: "a"
lista[2]   # OK: "c"
lista[3]   # IndexError: list index out of range
lista[10]  # IndexError: list index out of range
lista[-1]  # OK: "c" (viimeinen)
lista[-10] # IndexError: list index out of range
```

### Käytännön esimerkki

**Onnistunut haku:**
```
Lista: ['omena', 'banaani', 'päärynä', 'appelsiini', 'kiivi']
Anna indeksi (0-4): 2
Arvo: päärynä
```

**Virhe 1 (ei numero):**
```
Lista: ['omena', 'banaani', 'päärynä', 'appelsiini', 'kiivi']
Anna indeksi (0-4): kaksi
Virhe: Anna numero!
```

**Virhe 2 (liian suuri indeksi):**
```
Lista: ['omena', 'banaani', 'päärynä', 'appelsiini', 'kiivi']
Anna indeksi (0-4): 10
Virhe: Indeksi on liian suuri! Käytä arvoja 0-4.
```

### Vaihtoehtoinen ratkaisu (negatiiviset indeksit sallittu)

```python
lista = ["omena", "banaani", "päärynä", "appelsiini", "kiivi"]

print(f"Lista: {lista}")
print(f"Listan pituus: {len(lista)}")
print("Vinkki: Voit käyttää myös negatiivisia indeksejä (-1 = viimeinen)")

try:
    indeksi = int(input("Anna indeksi: "))
    arvo = lista[indeksi]
    print(f"Arvo indeksillä {indeksi}: {arvo}")
except ValueError:
    print("Virhe: Anna numero!")
except IndexError:
    print(f"Virhe: Indeksi {indeksi} on liian suuri tai liian pieni!")
    print(f"Käytä arvoja {-len(lista)} - {len(lista)-1}")
```

### Vaihtoehtoinen ratkaisu (kysytään kunnes saadaan kelvollinen)

```python
lista = ["omena", "banaani", "päärynä", "appelsiini", "kiivi"]

print(f"Lista: {lista}")

while True:
    try:
        indeksi = int(input("Anna indeksi (0-4): "))
        arvo = lista[indeksi]
        print(f"Arvo: {arvo}")
        break  # Lopetetaan kun onnistuu
    except ValueError:
        print("Virhe: Anna numero!")
    except IndexError:
        print("Virhe: Indeksi on liian suuri! Käytä arvoja 0-4.")
```

### Opittavaa
✅ `IndexError` tapahtuu kun yrität käyttää indeksiä jota ei ole  
✅ Listan indeksit alkavat 0:sta ja päättyvät `len(lista)-1`:een  
✅ Negatiiviset indeksit käyvät takaa: -1 = viimeinen, -2 = toiseksi viimeinen  
💡 Aina kun käytät indeksejä, varaudu `IndexError`:iin!

---

## Harjoitus 3: Finally-harjoitus ⭐⭐

### Ratkaisu
[harjoitus3.py](harjoitus3.py)

```python
try:
    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))
    toimitus = input("Valitse toimitus (+, -, *, /): ")
    
    if toimitus == "+":
        tulos = luku1 + luku2
    elif toimitus == "-":
        tulos = luku1 - luku2
    elif toimitus == "*":
        tulos = luku1 * luku2
    elif toimitus == "/":
        tulos = luku1 / luku2
    else:
        print("Virheellinen toimitus!")
        tulos = None
    
    if tulos is not None:
        print(f"Tulos: {tulos}")
        
except ValueError:
    print("Virhe: Anna molemmat luvut numeroina!")
except ZeroDivisionError:
    print("Virhe: Et voi jakaa nollalla!")
finally:
    print("Kiitos laskimen käytöstä!")
```

### Selitys
- **try-lohko:** Käsittelee syötteet ja laskennan
- **except ValueError:** Käsittelee virheelliset luvut
- **except ZeroDivisionError:** Käsittelee jaon nollalla
- **finally:** Suoritetaan **AINA**, riippumatta siitä tapahtuuko virhe vai ei

### Miksi finally on hyödyllinen?

`finally` varmistaa että tietty koodi **suoritetaan aina**:
- Tiedostojen sulkeminen
- Yhteyksien sulkeminen
- Loppuviestit käyttäjälle
- Lokitiedot

### Käytännön esimerkit

**Onnistunut lasku:**
```
Anna ensimmäinen luku: 10
Anna toinen luku: 5
Valitse toimitus (+, -, *, /): +
Tulos: 15.0
Kiitos laskimen käytöstä!  ← Finally suoritetaan
```

**Virhe (jako nollalla):**
```
Anna ensimmäinen luku: 10
Anna toinen luku: 0
Valitse toimitus (+, -, *, /): /
Virhe: Et voi jakaa nollalla!
Kiitos laskimen käytöstä!  ← Finally suoritetaan
```

**Virhe (ei numero):**
```
Anna ensimmäinen luku: teksti
Anna toinen luku: 5
Valitse toimitus (+, -, *, /): +
Virhe: Anna molemmat luvut numeroina!
Kiitos laskimen käytöstä!  ← Finally suoritetaan
```

**Huomaa:** "Kiitos laskimen käytöstä!" tulostuu **aina**!

### Finally vs normaalikoodin loppu

**Ilman finally:**
```python
try:
    luku = int(input("Anna luku: "))
    print(f"Luku: {luku}")
except ValueError:
    print("Virhe!")

print("Loppu")  # Tulostetaan aina, mutta EI finally-lohkon sisällä
```

**Finally:n kanssa:**
```python
try:
    luku = int(input("Anna luku: "))
    print(f"Luku: {luku}")
except ValueError:
    print("Virhe!")
finally:
    print("Loppu")  # Tulostetaan aina, finally-lohkon sisällä
```

Ero on pieni, mutta `finally` on **selkeämpi** ja **eksplisiittinen**.

### Vaihtoehtoinen ratkaisu (yksinkertaistettu)

```python
try:
    a = float(input("Anna luku 1: "))
    b = float(input("Anna luku 2: "))
    op = input("Toimitus (+, -, *, /): ")
    
    if op == "+":
        print(f"Tulos: {a + b}")
    elif op == "-":
        print(f"Tulos: {a - b}")
    elif op == "*":
        print(f"Tulos: {a * b}")
    elif op == "/":
        print(f"Tulos: {a / b}")
    else:
        print("Tuntematon toimitus!")
        
except ValueError:
    print("Virhe: Anna numerot!")
except ZeroDivisionError:
    print("Virhe: Jako nollalla!")
finally:
    print("Kiitos laskimen käytöstä!")
```

### Opittavaa
✅ `finally` suoritetaan **aina**, tapahtuipa virhe tai ei  
✅ Hyödyllinen resurssien vapauttamiseen ja loppuviesteihin  
✅ Voit yhdistää `try-except-finally` samaan rakenteeseen  
💡 Käytä finally kun tarvitset "siivoustyötä" virheestä riippumatta!

---

## Harjoitus 4: Else-lohko ⭐⭐⭐

### Ratkaisu
[harjoitus4.py](harjoitus4.py)

```python
try:
    ika = int(input("Anna ikäsi: "))
except ValueError:
    print("Virhe: Anna ikä numeroina!")
else:
    print(f"Ikäsi on {ika} vuotta.")
    
    if ika < 18:
        print("Olet alaikäinen.")
    else:
        print("Olet täysi-ikäinen.")
```

### Selitys
- **try-lohko:** Vain riskialtis koodi (input ja muunnos)
- **except-lohko:** Käsittelee virheen jos se tapahtuu
- **else-lohko:** Suoritetaan **vain jos ei tapahdu virhettä**

### Miksi käyttää else-lohkoa?

`else` erottaa **normaalin toiminnan** virheenkäsittelystä:

**Ilman else (huonompi):**
```python
try:
    ika = int(input("Anna ikäsi: "))
    # Kaikki tämä on try:n sisällä - ei hyvä!
    print(f"Ikäsi on {ika} vuotta.")
    if ika < 18:
        print("Olet alaikäinen.")
    else:
        print("Olet täysi-ikäinen.")
except ValueError:
    print("Virhe: Anna ikä numeroina!")
```

**Else:n kanssa (parempi):**
```python
try:
    ika = int(input("Anna ikäsi: "))  # Vain riskialtis koodi
except ValueError:
    print("Virhe: Anna ikä numeroina!")
else:
    # Normaali toiminta (ei try:ssä)
    print(f"Ikäsi on {ika} vuotta.")
    if ika < 18:
        print("Olet alaikäinen.")
    else:
        print("Olet täysi-ikäinen.")
```

### Miksi tämä on parempi?

1. **Selkeämpi:** Erottaa riskialtiin koodin normaalista koodista
2. **Turvallisempi:** Jos `else`-lohkossa tapahtuu virhe, se ei käsitellä `except`:ssä
3. **Helpompi lukea:** Näet heti mikä koodi saattaa aiheuttaa virheen

### Käytännön esimerkit

**Onnistunut (alaikäinen):**
```
Anna ikäsi: 15
Ikäsi on 15 vuotta.
Olet alaikäinen.
```

**Onnistunut (täysi-ikäinen):**
```
Anna ikäsi: 25
Ikäsi on 25 vuotta.
Olet täysi-ikäinen.
```

**Virhe:**
```
Anna ikäsi: kaksi
Virhe: Anna ikä numeroina!
```

### Try-Except-Else-Finally yhdessä

Voit käyttää kaikkia neljää samassa rakenteessa:

```python
try:
    ika = int(input("Anna ikäsi: "))
except ValueError:
    print("Virhe: Anna ikä numeroina!")
else:
    print(f"Ikäsi on {ika} vuotta.")
    if ika < 18:
        print("Olet alaikäinen.")
    else:
        print("Olet täysi-ikäinen.")
finally:
    print("Kiitos!")
```

**Suoritusjärjestys:**
1. **try** → Yritetään
2. Jos virhe → **except** → **finally**
3. Jos ei virhettä → **else** → **finally**
4. **finally** suoritetaan **aina**!

### Vaihtoehtoinen ratkaisu (lisätarkistukset)

```python
try:
    ika = int(input("Anna ikäsi: "))
except ValueError:
    print("Virhe: Anna ikä numeroina!")
else:
    # Tarkistetaan onko ikä realistinen
    if ika < 0:
        print("Virhe: Ikä ei voi olla negatiivinen!")
    elif ika > 150:
        print("Virhe: Epärealistinen ikä!")
    else:
        print(f"Ikäsi on {ika} vuotta.")
        
        if ika < 18:
            print("Olet alaikäinen.")
        elif ika < 65:
            print("Olet työikäinen aikuinen.")
        else:
            print("Olet eläkeikäinen.")
```

### Opittavaa
✅ `else`-lohko suoritetaan **vain jos ei tapahdu virhettä**  
✅ Erottaa normaalin toiminnan virheenkäsittelystä  
✅ Tekee koodista selkeämmän ja turvallisemman  
💡 Käytä else kun haluat tehdä jotain vain onnistuneen try:n jälkeen!

---

## Harjoitus 5: Useita poikkeuksia ⭐⭐⭐⭐

### Ratkaisu
[harjoitus5.py](harjoitus5.py)

```python
def lue_tiedosto(tiedostonimi):
    """
    Lukee tiedoston sisällön ja palauttaa sen merkkijonona.
    Palauttaa None jos lukeminen epäonnistuu.
    """
    try:
        with open(tiedostonimi, "r", encoding="utf-8") as f:
            sisältö = f.read()
            return sisältö
    except FileNotFoundError:
        print(f"Virhe: Tiedostoa '{tiedostonimi}' ei löydy.")
        return None
    except PermissionError:
        print(f"Virhe: Ei oikeuksia lukea tiedostoa '{tiedostonimi}'.")
        return None
    except UnicodeDecodeError:
        print(f"Virhe: Tiedoston '{tiedostonimi}' merkistö on virheellinen.")
        return None
    except Exception as e:
        print(f"Odottamaton virhe: {e}")
        return None


# Luo testiksi tiedosto
with open("testi.txt", "w", encoding="utf-8") as f:
    f.write("Tämä on testitiedosto.\n")
    f.write("Hienoa, että poikkeukset toimivat!")

# Testaa funktiota
print("=== Testi 1: Tiedosto löytyy ===")
sisältö = lue_tiedosto("testi.txt")
if sisältö:
    print("Tiedoston sisältö:")
    print(sisältö)

print("\n=== Testi 2: Tiedostoa ei löydy ===")
sisältö = lue_tiedosto("ei_ole.txt")

print("\n=== Testi 3: Tyhjä tiedostonimi ===")
sisältö = lue_tiedosto("")
```

### Selitys
- **FileNotFoundError:** Tiedostoa ei löydy
- **PermissionError:** Ei oikeuksia lukea/kirjoittaa
- **UnicodeDecodeError:** Tiedoston merkistökoodaus on virheellinen
- **Exception:** Kaikkien muiden virheiden käsittely (yleinen)

### Miksi käsitellä useita poikkeuksia?

Tiedostojen käsittelyssä voi tapahtua **monenlaisia virheitä**:
- Tiedostoa ei ole olemassa
- Tiedosto on lukittu
- Ei oikeuksia
- Merkistöongelmat
- Levy täynnä
- jne.

### Poikkeusten järjestys on tärkeä!

**OIKEIN (erityiset ensin, yleinen viimeinen):**
```python
try:
    ...
except FileNotFoundError:      # Erityinen
    ...
except PermissionError:        # Erityinen
except UnicodeDecodeError:     # Erityinen
except Exception:              # Yleinen (viimeisenä!)
    ...
```

**VÄÄRIN (yleinen ensin):**
```python
try:
    ...
except Exception:              # Tämä käsittelee KAIKKI!
    ...
except FileNotFoundError:      # Tätä ei koskaan saavuteta!
    ...
```

### With-lause vs manuaalinen sulkeminen

**With-lause (suositellaan):**
```python
with open("data.txt", "r") as f:
    sisältö = f.read()
# Tiedosto suljetaan automaattisesti
```

**Manuaalinen (vanha tapa):**
```python
f = open("data.txt", "r")
try:
    sisältö = f.read()
finally:
    f.close()  # Täytyy muistaa sulkea!
```

`with` on **parempi** koska se sulkee tiedoston automaattisesti!

### Käytännön esimerkit

**Testi 1 (onnistuu):**
```
=== Testi 1: Tiedosto löytyy ===
Tiedoston sisältö:
Tämä on testitiedosto.
Hienoa, että poikkeukset toimivat!
```

**Testi 2 (ei löydy):**
```
=== Testi 2: Tiedostoa ei löydy ===
Virhe: Tiedostoa 'ei_ole.txt' ei löydy.
```

**Testi 3 (tyhjä nimi):**
```
=== Testi 3: Tyhjä tiedostonimi ===
Virhe: Tiedostoa '' ei löydy.
```

### Vaihtoehtoinen ratkaisu (yksityiskohtaisempi)

```python
def lue_tiedosto(tiedostonimi):
    """
    Lukee tiedoston sisällön yksityiskohtaisella virheiden käsittelyllä.
    """
    # Tarkista onko tiedostonimi tyhjä
    if not tiedostonimi:
        print("Virhe: Tiedostonimi ei voi olla tyhjä!")
        return None
    
    try:
        print(f"Yritetään lukea tiedostoa '{tiedostonimi}'...")
        
        with open(tiedostonimi, "r", encoding="utf-8") as f:
            sisältö = f.read()
            
        print(f"✓ Luettiin {len(sisältö)} merkkiä")
        return sisältö
        
    except FileNotFoundError:
        print(f"❌ Tiedostoa '{tiedostonimi}' ei löydy")
        print("💡 Tarkista tiedostonimi ja polku")
        return None
        
    except PermissionError:
        print(f"❌ Ei oikeuksia lukea '{tiedostonimi}'")
        print("💡 Tarkista tiedoston käyttöoikeudet")
        return None
        
    except UnicodeDecodeError as e:
        print(f"❌ Merkistövirhe tiedostossa '{tiedostonimi}'")
        print(f"💡 Yritä eri merkistökoodausta (esim. 'latin-1')")
        print(f"   Virhe: {e}")
        return None
        
    except Exception as e:
        print(f"❌ Odottamaton virhe:")
        print(f"   Tyyppi: {type(e).__name__}")
        print(f"   Viesti: {e}")
        return None
    
    finally:
        print("Tiedostonlukuyritys valmis\n")
```

### Kaikkien virheiden kerääminen (Exception as e)

```python
except Exception as e:
    print(f"Virhe: {e}")
```

`e` sisältää virheen tiedot:
- `str(e)` → Virheilmoitus merkkijonona
- `type(e).__name__` → Virheen tyyppi (esim. "FileNotFoundError")
- `e.args` → Virheen argumentit

### Opittavaa
✅ Eri virheille voi olla eri käsittelyt  
✅ Erityiset poikkeukset ensin, yleinen (Exception) viimeiseksi  
✅ `with open()` sulkee tiedoston automaattisesti  
✅ `except Exception as e` käsittelee kaikki muut virheet  
✅ Palauta `None` jos toiminto epäonnistuu  
💡 Tiedostojen käsittelyssä virheiden käsittely on erityisen tärkeää!

---

## Yhteenveto: Try-Except-Else-Finally

### Täysi rakenne

```python
try:
    # Koodi, joka saattaa aiheuttaa virheen
    luku = int(input("Anna luku: "))
    
except ValueError:
    # Käsitellään ValueError
    print("Virhe: Anna numero!")
    
except ZeroDivisionError:
    # Käsitellään ZeroDivisionError
    print("Virhe: Jako nollalla!")
    
except Exception as e:
    # Käsitellään kaikki muut virheet
    print(f"Odottamaton virhe: {e}")
    
else:
    # Suoritetaan vain jos EI tapahdu virhettä
    print(f"Luku on: {luku}")
    
finally:
    # Suoritetaan AINA
    print("Valmis!")
```

### Suoritusjärjestys

**Jos virhe tapahtuu:**
1. `try` → Virhe!
2. `except` (sopiva) → Käsitellään virhe
3. `finally` → Suoritetaan aina
4. (`else` ohitetaan!)

**Jos virhe EI tapahdu:**
1. `try` → Onnistuu
2. (`except` ohitetaan!)
3. `else` → Suoritetaan
4. `finally` → Suoritetaan aina

### Milloin käytät mitäkin?

| Lohko | Käyttö | Suoritetaan |
|-------|--------|-------------|
| `try` | Riskialtis koodi | Aina yritetään |
| `except` | Virheen käsittely | Jos virhe tapahtuu |
| `else` | Normaali toiminta | Jos **ei** tapahdu virhettä |
| `finally` | Siivous, resurssien vapautus | **Aina** |

---

## Yleisiä virheitä

### 1. Liian laaja except

❌ **VÄLTÄ:**
```python
try:
    koodi
except:  # Käsittelee KAIKKI virheet, myös Ctrl+C!
    print("Virhe")
```

✅ **PAREMPI:**
```python
try:
    koodi
except ValueError:  # Vain tietty virhe
    print("Virhe")
```

### 2. Väärä järjestys

❌ **VÄÄRIN:**
```python
try:
    koodi
except Exception:     # Tämä käsittelee kaikki
    print("Yleinen")
except ValueError:    # Tätä ei koskaan saavuteta!
    print("ValueError")
```

✅ **OIKEIN:**
```python
try:
    koodi
except ValueError:    # Erityinen ensin
    print("ValueError")
except Exception:     # Yleinen viimeiseksi
    print("Yleinen")
```

### 3. Liikaa koodia try:ssä

❌ **VÄLTÄ:**
```python
try:
    luku = int(input("Anna luku: "))
    tulos = luku * 2
    print(tulos)
    lista = [1, 2, 3]
    # ...paljon lisää
except ValueError:
    print("Virhe")
```

✅ **PAREMPI:**
```python
try:
    luku = int(input("Anna luku: "))  # Vain riskialtis
except ValueError:
    print("Virhe")
else:
    tulos = luku * 2  # Muu koodi else:ssä
    print(tulos)
    lista = [1, 2, 3]
```

### 4. Virheiden piilottaminen

❌ **VAARALLISTA:**
```python
try:
    tärkeä_funktio()
except:
    pass  # Ei tehdä mitään - virhe katoaa!
```

✅ **PAREMPI:**
```python
try:
    tärkeä_funktio()
except Exception as e:
    print(f"Virhe: {e}")
    # tai lokitiedostoon
```

---

## Vinkkejä

💡 **Ole spesifi:** Käsittele tietyt virheet, ei kaikkia  
💡 **Pidä try pieni:** Vain riskialtis koodi try-lohkoon  
💡 **Käytä else:** Erottaa normaalin koodin virheenkäsittelystä  
💡 **Käytä finally:** Resurssien vapauttamiseen  
💡 **Anna ohjeita:** Kerro käyttäjälle mitä tehdä virheen sattuessa  
💡 **Testaa virheet:** Kokeile ohjelmaa virheellisillä syötteillä  
💡 **Älä piilota virheitä:** Lokita tai ilmoita virheistä

---

## Tärkeimmät poikkeukset

| Poikkeus | Syy | Esimerkki |
|----------|-----|-----------|
| `ValueError` | Väärä arvo | `int("abc")` |
| `ZeroDivisionError` | Jako nollalla | `10 / 0` |
| `TypeError` | Väärä tyyppi | `"5" + 5` |
| `IndexError` | Indeksi liian suuri | `lista[100]` |
| `KeyError` | Avainta ei löydy | `sanakirja["ei_ole"]` |
| `FileNotFoundError` | Tiedostoa ei löydy | `open("ei_ole.txt")` |
| `PermissionError` | Ei oikeuksia | `open("/root/file")` |
| `UnicodeDecodeError` | Merkistövirhe | `bytes.decode()` |

---

Hienoa työtä! Olet nyt oppinut virheiden käsittelyn perusteet. 🎉

➡️**Seuraavaksi:** [Aihe 10 - Sanakirjat ja järjestäminen](../../10.Sanakirjat%20ja%20järjestäminen/)
