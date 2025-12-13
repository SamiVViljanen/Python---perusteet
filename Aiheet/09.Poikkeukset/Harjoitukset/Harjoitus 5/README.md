# Harjoitus 5: Useita poikkeuksia ⭐⭐⭐⭐

## Tehtävänanto

Tee funktio `lue_tiedosto(tiedostonimi)`, joka:
1. Yrittää lukea tiedoston sisällön
2. Palauttaa sisällön merkkijonona
3. Käsittelee kaikki mahdolliset virheet

**Käsittele seuraavat virhetilanteet:**
- `FileNotFoundError` - Tiedostoa ei löydy
- `PermissionError` - Ei oikeuksia lukea tiedostoa
- `UnicodeDecodeError` - Tiedoston merkistö on virheellinen
- `Exception` - Muut odottamattomat virheet (yleinen)

**Testaa funktiota:**
- Luo testiksi tiedosto `testi.txt` ja kirjoita siihen jotain
- Kutsu funktiota tiedostolla joka on olemassa
- Kutsu funktiota tiedostolla joka EI ole olemassa

## Esimerkkitulostus

**Onnistunut luku:**
```
Tiedoston sisältö:
Tämä on testitiedosto.
Hienoa, että poikkeukset toimivat!
```

**Tiedostoa ei löydy:**
```
Virhe: Tiedostoa 'ei_ole.txt' ei löydy.
```

**Ei oikeuksia:**
```
Virhe: Ei oikeuksia lukea tiedostoa 'salainen.txt'.
```

## Vinkkejä

- Luo funktio: `def lue_tiedosto(tiedostonimi):`
- Käytä `with open(...)` tiedoston avaamiseen
- Käsittele poikkeukset **järjestyksessä**: erityisimmät ensin, yleinen viimeisenä
- Palauta `None` jos lukeminen epäonnistuu
- Palauta sisältö jos lukeminen onnistuu

## Rakenne

```python
def lue_tiedosto(tiedostonimi):
    try:
        # Yritä lukea tiedosto
        ...
    except FileNotFoundError:
        # Tiedostoa ei löydy
        ...
    except PermissionError:
        # Ei oikeuksia
        ...
    except UnicodeDecodeError:
        # Merkistövirhe
        ...
    except Exception as e:
        # Muut virheet
        ...
```

## Testaaminen

Luo ensin testiksi tiedosto `testi.txt`:
```python
with open("testi.txt", "w", encoding="utf-8") as f:
    f.write("Tämä on testitiedosto.\n")
    f.write("Hienoa, että poikkeukset toimivat!")
```

Sitten testaa funktiota:
```python
sisältö = lue_tiedosto("testi.txt")
if sisältö:
    print(sisältö)

sisältö = lue_tiedosto("ei_ole.txt")  # Pitäisi tulostaa virheilmoitus
```

## Aloita tästä

Avaa [harjoitus5.py](harjoitus5.py) ja aloita koodaaminen!
