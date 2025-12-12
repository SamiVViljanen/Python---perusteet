# Komennot ja muuttujat

## Sisällysluettelo
1. [Mikä on muuttuja?](#mikä-on-muuttuja)
2. [Nimeämiskäytännöt](#nimeämiskäytännöt)
3. [Peruskomennot: tulostus ja syöte](#peruskomennot-tulostus-ja-syöte)
4. [Aritmeettiset operaatiot ja muut operaattorit](#aritmeettiset-operaatiot-ja-muut-operaattorit)
5. [Lyhennetyt sijoitukset](#lyhennetyt-sijoitukset)
6. [Tyypin muunnokset](#tyypin-muunnokset)
7. [Kommentit ja selitykset](#kommentit-ja-selitykset)
8. [Yleisiä virheitä ja sudenkuoppia](#yleisiä-virheitä-ja-sudenkuoppia)
9. [Lyhyt käytännön esimerkki](#lyhyt-käytännön-esimerkki)

---

Tämä materiaali on tarkoitettu Pythonin ja ohjelmoinnin täysin aloittelijoille.
Erityisesti opiskelijoille, joille Python on ensimmäinen kosketus ohjelmointiin.

## Mikä on muuttuja?

- Muuttuja on nimi, joka viittaa arvoon. Pythonissa muuttuja luodaan yksinkertaisesti antamalla sille arvo:
```python
luku = 10
nimi = "Maija"
pi = 3.14159
on_tosi = True
```

- Python on tyypiltään dynaamisesti tyypitetty kieli:
  muuttujan tyyppi määräytyy sen arvon mukaan, eikä sitä tarvitse (tai voi) erikseen määritellä.

## Nimeämiskäytännöt

- Käytä selkeitä nimiä ja snake_case-tyyliä:
`opiskelija_nimi`, `laskettu_summa`.

- Vältä Pythonin sisäänrakennettujen nimien ylikirjoittamista (esim. `list`, `str`, `input`).
- Vakiot kirjoitetaan yleensä isoilla kirjaimilla: `PI = 3.14`


## Peruskomennot: tulostus ja syöte

Tulostus:
```python
print("Hei maailma!")
```

Syöte käyttäjältä:
```python
nimi = input("Anna nimesi: ")
print("Hei", nimi)
```

## Aritmeettiset operaatiot ja muut operaattorit

Perusoperaattorit : `+`,`-`, `*`,`/` (liukujako), `//`(kokonaislukujako), `%`(jäännös), `**` (potenssi)

```python
a = 7
b = 2
print(a + b)  # 9
print(a / b)  # 3.5
print(a // b) # 3
print(a % b)  # 1
print(a * b)  # 14
print(a ** b) # 49
```

💡 Kokeile itse:
Muuta muuttujan arvoa ja katso, miten tuloste muuttuu.


## Lyhennetyt sijoitukset

Kätevä tapa päivittää samaa muuttujaa:

```python
x = 5
x += 3  # sama kuin x on yhtäsuuri kuin x + 3, eli x on 8
x *= 2  # x = x * 2 -> x on 16
```

## Tyypin muunnokset
Usein tarvitaan muuntaa merkkijono luvuiksi tai päinvastoin:
```python
s = "123"
n = int(s)    # 123
f = float("3.13")
t = str(42)    # "42"
```

## Kommentit ja selitykset

Yhden rivin kommentti: `# Tämä on kommentti`

Monirivinen teksti dokumentaatiossa on usein docstring.
Docstringejä käytetään erityisesti funktioiden ja moduulien dokumentointiin.

```python
x = 5  # tässä on kommentti

""" tässä on docstring, jota voi käyttää hyödyksi pidempiin kommentointeihin ja selitteisiin """
```

## Yleisiä virheitä ja sudenkuoppia

- Käytä `==' vertailuun ja '=' sijoitukseen (älä sekoita niitä).

- Muuttujan käyttö ennen kuin se on määritelty aiheuttaa virheen (NameError)

- Vältä ylikirjoittamasta sisäänrakennettuja nimiä (esim. älä tee `list = [1, 2]`)

- Muista antaa `input()`-palautus tarvittaessa (esim. `int()`-funktiolla).

## Lyhyt käytännön esimerkki
```python
# Kysy käyttäjän ikä ja kerro syntymävuosi

ika = int(input("Kuinka vanha olet? "))
vuosi = 2025 - ika   # Oletetaan nykyinen vuosi
print(f"Sinä olet syntynyt vuonna {vuosi}.")
```

Odotettu toiminta:
- käyttäjä kirjoittaa esimerkiksi `30`
- Ohjelma tulostaa `Sinä olet syntynyt vuonna 1995.`


## Seuraavaksi
Siirry [Harjoitukset](Harjoitukset/)-kansioon ja tee luvun tehtävät.