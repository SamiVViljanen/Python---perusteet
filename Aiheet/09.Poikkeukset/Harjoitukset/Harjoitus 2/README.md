# Harjoitus 2: Listan käsittely ⭐⭐

## Tehtävänanto

Luo lista, jossa on 5 arvoa (esim. hedelmät, nimet tai numerot).

Pyydä käyttäjää syöttämään indeksi (0-4) ja tulosta kyseisen indeksin arvo.

**Käsittele seuraavat virhetilanteet:**
- Jos käyttäjä ei anna numeroa → ValueError
- Jos indeksi on liian suuri tai liian pieni → IndexError

## Esimerkkitulostus

**Onnistunut suoritus:**
```
Lista: ['omena', 'banaani', 'päärynä', 'appelsiini', 'kiivi']
Anna indeksi (0-4): 2
Arvo: päärynä
```

**Virhe 1 (ei numero):**
```
Lista: ['omena', 'banaani', 'päärynä', 'appelsiini', 'kiivi']
Anna indeksi (0-4): teksti
Virhe: Anna numero!
```

**Virhe 2 (indeksi liian suuri):**
```
Lista: ['omena', 'banaani', 'päärynä', 'appelsiini', 'kiivi']
Anna indeksi (0-4): 10
Virhe: Indeksi on liian suuri! Käytä arvoja 0-4.
```

## Vinkkejä

- Luo ensin lista: `lista = ["omena", "banaani", ...]`
- Tulosta lista käyttäjälle
- Käytä `int(input(...))` indeksin lukemiseen
- Käsittele `ValueError` ja `IndexError`
- `IndexError` voi tapahtua myös negatiivisilla indekseillä (-10)

## Aloita tästä

Avaa [harjoitus2.py](harjoitus2.py) ja aloita koodaaminen!
