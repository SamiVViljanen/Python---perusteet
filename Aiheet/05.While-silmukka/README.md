# While-silmukka (While Loop)

## Sisällysluettelo
1. [Miksi käytetään while-silmukkaa?](#miksi-käytetään-while-silmukkaa)
2. [Mitä tässä tapahtuu?](#mitä-tässä-tapahtuu)
3. [Esimerkkejä while-silmukan käytöstä](#esimerkkejä-while-silmukan-käytöstä)
4. [Break ja continue while-silmukassa](#break-ja-continue-while-silmukassa)
5. [While vs for](#while-vs-for)
6. [Miksi while-silmukka on hyödyllinen?](#miksi-while-silmukka-on-hyödyllinen)
7. [Yhteenveto](#yhteenveto)

---

## Miksi käytetään while-silmukkaa?	

Pythonissa while-silmukka (while-loop) on toinen tapa toistaa koodia useita kertoja.
Sitä käytetään erityisesti silloin, kun ei vielä tiedetä montako kertaa toistoja tarvitaan, vaan halutaan toistaa jotain niin kauan kuin ehto on tosi (True).

ESIMERKKI:

```Python
i = 0
while i < 5:
  print("Hei maailma!")
  i += 1
```

Tämä tulostaa tekstin "**Hei maailma!**" viisi kertaa:

```
Hei maailma!
Hei maailma!
Hei maailma!
Hei maailma!
Hei maailma!
```

Silmukka jatkuu niin kauan, kun muuttuja i on pienempi kuin 5.

## Mitä tässä tapahtuu?

-	while aloittaa silmukan, joka jatkuu niin kauan kuin ehto on tosi

-	i < 5 on ehto, jota tarkistetaan jokaisella kierroksella

-	i += 1 kasvattaa muuttujan arvoa, jotta silmukka lopulta loppuu

⚠️⚠️⚠️ Jos ehtoa ei koskaan todeta epätodeksi, syntyy ikuinen silmukka (infinite loop)
 
## Esimerkkejä while-silmukan käytöstä

### Toistaminen kunnes ehto täyttyy
```Python
luku = 0
while luku < 10:
  print(luku)
  luku += 2
```
Tulostaa:
```
0
2
4
6
8
```

### Käyttäjän syötteen tarkistus

```Python
salasana = ""
while salasana != "python":
  salasana = input("Anna salasana: ")

print("Tervetuloa!")
```

Ohjelma pyytää salasanaa niin kauan, kunnes käyttäjä syöttää oikean vastauksen.


### While True – ikuinen silmukka valikkojen kanssa

```Python
while True:
  print("\n1. Jatka")
  print("0. Lopeta")
  valinta = input("Valintasi: ")

  if valinta == "0":
      print("Ohjelma lopetetaan!")
      break
  print("Jatketaan...")
```
 
Tämä on yleisin tapa käyttää while-silmukkaa valikkojen ja vuorovaikutteisten ohjelmien kanssa.

Silmukka jatkuu loputtomiin, kunnes break – komento suoritetaan.


## Break ja continue while-silmukassa

### Break – lopettaa silmukan kesken

```Python
while True:
  vastaus = input("Lopetetaanko? (k/e): ")
  if vastaus == "k":
      break
```

➡️ Silmukka päättyy heti, kun käyttäjä vastaa "k"


### Continue – ohittaa loppuosan ja siirtyy seuraavaan kierrokseen

```Python
i = 0
while i < 5:
  i += 1
  if i == 3:
      continue
  print(i)
```
➡️ Tulostaa luvut 1, 2, 4 ja 5 (luku 3 ohitetaan)

```Python
1
2
4
5
```


## While vs for

| FOR-silmukka | WHILE-silmukka |
|--------------|----------------|
| Käytetään, kun tiedetään montako kertaa toistetaan tai käydään läpi lista | Käytetään, kun ei tiedetä toistojen määrää etukäteen |
| Esim. `for i in range(5):` | Esim. `while i < 5:` |
| Käy läpi kokoelman (lista, merkkijono…) | Toistaa, kunnes ehto muuttuu epätodeksi |
| Helppo ja turvallinen | Joustava, mutta voi jäädä helposti ikuiseen silmukkaan |

## Miksi while-silmukka on hyödyllinen?

-	Sopii tilanteisiin, joissa ei tiedetä toistojen määrää

-	Antaa täyden hallinnan toiston ehdoista ja loppumisesta

-	Hyödyllinen erityisesti käyttäjän syötteiden käsittelyssä

- Tekee ohjelmista vuorovaikutteisempia ja joustavampia


## Yhteenveto

While-silmukka on toistorakenne, joka jatkuu niin kauan kuin ehto on tosi. Se antaa ohjelmoijalle mahdollisuuden hallita ohjelman kulkua tarkasti.


💡Muista: käytä for-silmukkaa, kun tiedät toistojen määrän – ja while-silmukkaa, kun toisto riippuu ehdosta!

Onnea ohjelmointii! 🐍