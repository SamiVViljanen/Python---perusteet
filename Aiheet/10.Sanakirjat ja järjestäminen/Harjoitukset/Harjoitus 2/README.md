# Harjoitus 2: Sanakirjan läpikäynti ⭐⭐

## Tehtävänanto

Luo sanakirja, jossa on 5 opiskelijan nimet ja heidän pistemääränsä (0-100).

**Tee seuraavat asiat:**
1. Luo sanakirja `pisteet`
2. Laske kaikkien opiskelijoiden pisteiden keskiarvo
3. Etsi ja tulosta kuka sai parhaat pisteet
4. Käy läpi kaikki opiskelijat ja tulosta:
   - Nimi ja pistemäärä
   - "Hyväksytty" jos pisteet >= 50, muuten "Hylätty"

## Esimerkkitulostus

```
=== OPISKELIJOIDEN TULOKSET ===

Keskiarvo: 76.4 pistettä

Paras suoritus: Anna (92 pistettä)

Yksittäiset tulokset:
Anna: 92 pistettä - Hyväksytty
Pekka: 78 pistettä - Hyväksytty
Liisa: 45 pistettä - Hylätty
Matti: 88 pistettä - Hyväksytty
Kaisa: 79 pistettä - Hyväksytty
```

## Vinkkejä

- Keskiarvo: `sum(pisteet.values()) / len(pisteet)`
- Paras: `max(pisteet, key=pisteet.get)` tai käytä for-silmukkaa
- Läpikäynti: `for nimi, pistemäärä in pisteet.items():`

## Aloita tästä

Avaa [harjoitus2.py](harjoitus2.py) ja aloita koodaaminen!
