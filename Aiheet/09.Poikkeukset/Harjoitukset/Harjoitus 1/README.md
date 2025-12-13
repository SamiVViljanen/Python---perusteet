# Harjoitus 1: Turvallinen jako ⭐

## Tehtävänanto

Tee ohjelma, joka kysyy käyttäjältä kaksi lukua ja jakaa ne keskenään.

**Käsittele seuraavat virhetilanteet:**
- Jos käyttäjä ei anna numeroa → ValueError
- Jos käyttäjä yrittää jakaa nollalla → ZeroDivisionError

## Esimerkkitulostus

**Onnistunut suoritus:**
```
Anna ensimmäinen luku: 10
Anna toinen luku: 2
Tulos: 5.0
```

**Virhe 1 (ei numero):**
```
Anna ensimmäinen luku: teksti
Anna toinen luku: 5
Virhe: Anna molemmat luvut numeroina!
```

**Virhe 2 (jako nollalla):**
```
Anna ensimmäinen luku: 10
Anna toinen luku: 0
Virhe: Et voi jakaa nollalla!
```

## Vinkkejä

- Käytä `try-except` rakennetta
- Tarvitset kaksi erillistä `except`-lohkoa: `ValueError` ja `ZeroDivisionError`
- Muista tulostaa selkeät virheilmoitukset käyttäjälle

## Aloita tästä

Avaa [harjoitus1.py](harjoitus1.py) ja aloita koodaaminen!
