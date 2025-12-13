# Harjoitus 3: Finally-harjoitus ⭐⭐

## Tehtävänanto

Tee yksinkertainen laskin, joka:
1. Kysyy käyttäjältä kaksi lukua
2. Kysyy mitä laskutoimitusta tehdään (+, -, *, /)
3. Tulostaa tuloksen
4. Käsittelee virheet
5. **Tulostaa AINA lopuksi**: "Kiitos laskimen käytöstä!" (käytä `finally`-lohkoa)

## Esimerkkitulostus

**Onnistunut suoritus:**
```
Anna ensimmäinen luku: 10
Anna toinen luku: 5
Valitse toimitus (+, -, *, /): +
Tulos: 15
Kiitos laskimen käytöstä!
```

**Virhe (jako nollalla):**
```
Anna ensimmäinen luku: 10
Anna toinen luku: 0
Valitse toimitus (+, -, *, /): /
Virhe: Et voi jakaa nollalla!
Kiitos laskimen käytöstä!
```

**Virhe (ei numero):**
```
Anna ensimmäinen luku: teksti
Anna toinen luku: 5
Valitse toimitus (+, -, *, /): +
Virhe: Anna molemmat luvut numeroina!
Kiitos laskimen käytöstä!
```

## Vinkkejä

- Käytä `try-except-finally` rakennetta
- `finally`-lohko suoritetaan **aina**, tapahtuipa virhe tai ei
- Käsittele `ValueError` ja `ZeroDivisionError`
- Käytä `if-elif` rakenteita laskutoimituksille

## Aloita tästä

Avaa [harjoitus3.py](harjoitus3.py) ja aloita koodaaminen!
