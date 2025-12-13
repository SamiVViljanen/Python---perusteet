# Harjoitus 4: Else-lohko ⭐⭐⭐

## Tehtävänanto

Kysy käyttäjältä ikää.

**Jos syöte on validi (ei virhettä):**
- Tulosta ikä
- Tulosta onko käyttäjä alaikäinen (alle 18) vai täysi-ikäinen (18+)
- **Käytä `else`-lohkoa** tähän normaalitoimintaan

**Jos syöte on virheellinen:**
- Käsittele `ValueError`

## Esimerkkitulostus

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

## Vinkkejä

- Käytä `try-except-else` rakennetta
- `else`-lohko suoritetaan **vain jos ei tapahdu virhettä**
- Tarkista `else`-lohkossa onko ikä alle 18
- Älä laita normaalitoimintaa `try`-lohkoon, vaan `else`-lohkoon

## Rakenne

```python
try:
    # Vain riskialtis koodi (input ja int-muunnos)
    ...
except ValueError:
    # Virheen käsittely
    ...
else:
    # Normaali toiminta (tulostukset ja tarkistukset)
    ...
```

## Aloita tästä

Avaa [harjoitus4.py](harjoitus4.py) ja aloita koodaaminen!
