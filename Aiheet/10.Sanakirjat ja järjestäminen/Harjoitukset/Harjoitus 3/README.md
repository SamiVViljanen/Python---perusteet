# Harjoitus 3: Tuplat ja järjestäminen ⭐⭐

## Tehtävänanto

Luo lista tuplista, jossa jokainen tupla sisältää henkilön nimen ja iän.

**Tee seuraavat asiat:**
1. Luo lista, jossa on 5 tuplaa muodossa `(nimi, ikä)`
2. Tulosta alkuperäinen lista
3. Järjestä lista iän mukaan (nuorin ensin)
4. Tulosta järjestetty lista
5. Järjestä lista nimen mukaan aakkosjärjestyksessä
6. Tulosta aakkostettu lista

## Esimerkkitulostus

```
Alkuperäinen lista:
[('Anna', 25), ('Pekka', 30), ('Liisa', 22), ('Matti', 35), ('Kaisa', 28)]

Järjestetty iän mukaan (nuorin ensin):
[('Liisa', 22), ('Anna', 25), ('Kaisa', 28), ('Pekka', 30), ('Matti', 35)]

Järjestetty nimen mukaan:
[('Anna', 25), ('Kaisa', 28), ('Liisa', 22), ('Matti', 35), ('Pekka', 30)]
```

## Vinkkejä

- Luo lista tuplista: `henkilöt = [("Anna", 25), ("Pekka", 30)]`
- Järjestä iän mukaan: `sorted(henkilöt, key=lambda x: x[1])`
- Järjestä nimen mukaan: `sorted(henkilöt)` tai `sorted(henkilöt, key=lambda x: x[0])`
- Lambda-funktio: `lambda x: x[1]` ottaa tupla ja palauttaa toisen alkion (ikä)

## Aloita tästä

Avaa [harjoitus3.py](harjoitus3.py) ja aloita koodaaminen!
