# For-silmukka (For Loop)

## Sisällysluettelo
1. [Miksi käytetään for-silmukkaa?](#miksi-käytetään-for-silmukkaa)
2. [Mitä tässä tapahtuu?](#mitä-tässä-tapahtuu)
3. [Esimerkkejä for-silmukan käytöstä](#esimerkkejä-for-silmukan-käytöstä)
4. [Break ja continue](#break-ja-continue)
5. [Miksi for-silmukka on hyödyllinen?](#miksi-for-silmukka-on-hyödyllinen)
6. [For vs while](#for-vs-while)
7. [Yhteenveto](#yhteenveto)

---

## Miksi käytetään for-silmukkaa?

Pythonissa **for-silmukka** (for-loop) on tapa **toistaa sama koodi monta kertaa** helposti ja selkeästi.
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

## Mitä tässä tapahtuu?

- For aloittaa silmukan ("toista seuraava lohko")
- i on muuttuja, joka saa eri arvon joka kierroksella
- range(5) tuottaa luvut 0,1,2,3 ja 4
- print("Hei maailma!") suoritetaan jokaisella kierroksella


## Esimerkkejä for-silmukan käytöstä

### Listan läpikäynti
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

### Merkkijonon läpikäynti
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

### Indexin käyttö enumerate():lla
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

### Range() eri tavoilla

```Python
range(5)        # -> 0, 1, 2, 3, 5 (oletuksena alkaa 0:sta)
range(1, 6)     # -> 1, 2, 3, 4, 5 (alkaen 1:stä, päättyen 5:een)
range(0, 10, 2) # -> 0, 2, 4, 6, 8 (joka toinen luku)
```


## Break ja continue

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


## Miksi for-silmukka on hyödyllinen?

- Toistaa saman toiminnon monta kertaa ilman turhaa koodin kopiointia
- Tekee koodista siistin ja helposti luettavan
- Toimii erityisen hyvin listojen, merkkijonojen ja muiden kokoelmien kanssa
- Vähentää virheiden määrää (ei unohdu yksittäisiä vaiheita)


## For vs while

- **FOR-loop** käytetään, kun **tiedetään montako kierrosta** tehdään, tai kun käydään läpi jokin kokoelma (lista, merkkijono).

- **WHILE-loop** käytetään, kun **toistetaan kunnes jokin ehto täytyy** (esim. kunnes käyttäjä lopettaa)

## Yhteenveto

For-silmukka on ohjelmoinnin **perustyökalu**, joka auttaa:
- toistamaan toimintoja automaattisesti
- käsittelemään useita arvoja helposti
- kirjoittamaan selkeämpää ja tehokkaampaa koodia


### Muista

Jos sinun täytyy tehdä jotain "monta kertaa" for-loop on usein paras ratkaisu!

## Seuraavaksi
Siirry [Harjoitukset](Harjoitukset/)-kansioon ja tee luvun tehtävät.