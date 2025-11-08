# MIKSI KÄYTETÄÄN FOR-LOOP (FOR-SILMUKKA)?

Pythonissa **for-silmukka**(for-loop) on tapa **toistaa sama koodi monta kertaa** helposti ja selkeästi.
Sen avulla voidaan käydä läpi esimerkiksi lista, merkkijono tai mikä tahansa joukko asioita - ilman että tarvitsee kirjoittaa sama koodi moneen kertaan.

Esimerkiksi:
``` python
for i in range(5):
  print("Hei maailma!")
```
Tämä tulostaa tekstin "**Hei maailma!** viisi kertaa:

```
Hei maailma!
Hei maailma!
Hei maailma!
Hei maailma!
Hei maailma!
```

# MITÄ TÄSSÄ TAPAHTUU?

- For aloittaa silmukan ("toista seuraava lohko")
- i on muuttuja, joka saa eri arvon joka kierroksella
- range(5) tuottaa luvut 0,1,2,3 ja 4
- print("Hei maailma!") suoritetaan jokaisella kierroksella


# ESIMERKKEJÄ FOR-LOOPIN KÄYTÖSTÄ

## _LISTAN LÄPIKÄYNTI_
``` Python
hedelmät = ["omena", "banaani", "appelsiini"]

for hedelmä in hedelmät:
print(hedelmä)
```
Tulostaa:
```
omena
banaani
appelsiini
```
Tässä silmukka käy siis listan läpi **alkion kerrallaan** ja suorittaa print-komennon jokaiselle.

## _MERKKIJONON LÄPIKÄYNTI_
```Python
sana = "Python"
for kirjain in sana:
  print(kirjain)
```
Tulostaa:
```
p
y
t
h
o
n
```

## _INDEXIN KÄYTTÖ ENUMERATE():LLA_
```Python
hedelmät = ["omena", "banaani", "appelsiini"]
for index, hedelmä in enumerate(hedelmät):
  print(f"{index}: {hedelmä}")
```
Tulostaa:
```
0: omena
1: banaani
2: appelsiini
```

enumerate() on hyödyllinen, kun tarvitset sekä alkion, että sen sijainnin(index).

## _RANGE() ERI TAVOILLA_

```Python
range(5)        # -> 0, 1, 2, 3, 5 (oletuksena alkaa 0:sta)
range(1, 6)     # -> 1, 2, 3, 4, 5 (alkaen 1:stä, päättyen 5:een)
range(0, 10, 2) # -> 0, 2, 4, 6, 8 (joka toinen luku)
```


** _BREAK JA CONTINUE_**
**break** - lopettaa silmukan kesken:
```Python
for i in range(10):
  if i == 5:
    break      # Pysähtyy kun i on 5
  print(i)     # Tulostaa: 0, 1, 2, 3, 4
  ```

**continue** - ohittaa loppuosan ja siirtyy seuraavaan kierrokseen:
```Python
for i in range(5):
  if i == 2:
    continue  # ohittaa luvun 2
  print(i)    # tulostaa 0, 1, 3, 4
```


# MIKSI FOR-LOOP ON HYÖDYLLINEN?

- Toistaa saman toiminnon monta kertaa ilman turhaa koodin kopiointia
- Tekee koodista siistin ja helposti luettavan
- Toimii erityisen hyvin listojen, merkkijonojen ja muiden kokoelmien kanssa
- Vähentää virheiden määrää (ei unohdu yksittäisiä vaiheita)


# FOR vs WHILE

- **FOR-loop** käytetään, kun **tiedetään montako kierrosta** tehdään, tai kun käydään läpi jokin kokoelma (lista, merkkijono).

- **WHILE-loop** käytetään, kun **toistetaan kunnes jokin ehto täytyy** (esim. kunnes käyttäjä lopettaa)

# YHTEENVETO

For-silmukka on ohjelmoinnin **perustyökalu**, joka auttaa:
- toistamaan toimintoja automaattisesti
- käsittelemään useita arvoja helposti
- kirjoittamaan selkeämpää ja tehokkaampaa koodia


## MUISTA

Jos sinun täytyy tehdä jotain "monta kertaa" for-loop on usein paras ratkaisu!
