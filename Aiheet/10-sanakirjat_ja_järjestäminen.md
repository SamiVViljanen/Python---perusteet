# Sanakirjat ja järjestäminen

## Sisällysluettelo
1. [Mikä on sanakirja?](#mikä-on-sanakirja)
2. [Sanakirjan perustoiminnot](#sanakirjan-perustoiminnot)
3. [Sanakirjan läpikäynti](#sanakirjan-läpikäynti)
4. [Tuplat (Tuples)](#tuplat-tuples)
5. [Listojen järjestäminen](#listojen-järjestäminen)
6. [Tuplien järjestäminen](#tuplien-järjestäminen)
7. [Sanakirjojen järjestäminen](#sanakirjojen-järjestäminen)
8. [Käytännön sovelluksia](#käytännön-sovelluksia)
9. [Yhteenveto](#yhteenveto)

---

Tässä oppaassa opit käyttämään sanakirjoja, tuploja ja järjestämään tietoa eri tavoin.

## Mikä on sanakirja?

**Sanakirja** (dictionary, dict) on tietorakenne, joka tallentaa tietoa **avain-arvo-pareina**. Se on kuin oikea sanakirja: haet sanan (avaimen) ja saat määritelmän (arvon).

### Miksi käyttää sanakirjaa?

```python
# Ilman sanakirjaa - hankalaa!
nimet = ["Anna", "Pekka", "Liisa"]
iät = [25, 30, 28]
# Miten löydän Pekan iän? Täytyy etsiä indeksi...

# Sanakirjan kanssa - helppoa!
henkilöt = {
    "Anna": 25,
    "Pekka": 30,
    "Liisa": 28
}
print(henkilöt["Pekka"])  # 30 - suoraan!
```

### Sanakirjan luominen

```python
# Tyhjä sanakirja
tyhjä = {}
tyhjä2 = dict()

# Sanakirja arvoilla
puhelinluettelo = {
    "Anna": "040-1234567",
    "Pekka": "050-7654321",
    "Liisa": "045-9876543"
}

# Eri tietotyyppejä
opiskelija = {
    "nimi": "Anna Virtanen",
    "ikä": 22,
    "opintopisteet": 45,
    "läsnä": True,
    "kurssit": ["Python", "Matematiikka", "Fysiikka"]
}

# Numeroavaimet
tulokset = {
    1: "kultaa",
    2: "hopeaa",
    3: "pronssia"
}
```

## Sanakirjan perustoiminnot

### Arvojen hakeminen

```python
henkilö = {
    "nimi": "Anna",
    "ikä": 25,
    "kaupunki": "Helsinki"
}

# Hakeminen hakasulkeilla
print(henkilö["nimi"])  # Anna
print(henkilö["ikä"])   # 25

# Jos avain puuttuu, tulee virhe!
# print(henkilö["osoite"])  # KeyError!

# Turvallinen hakeminen get():lla
print(henkilö.get("nimi"))      # Anna
print(henkilö.get("osoite"))    # None (ei virhettä)
print(henkilö.get("osoite", "Ei tiedossa"))  # Oletusarvo
```

### Arvojen lisääminen ja muuttaminen

```python
henkilö = {"nimi": "Anna", "ikä": 25}

# Lisää uusi avain-arvo-pari
henkilö["kaupunki"] = "Helsinki"
print(henkilö)  # {'nimi': 'Anna', 'ikä': 25, 'kaupunki': 'Helsinki'}

# Muuta olemassa olevaa arvoa
henkilö["ikä"] = 26
print(henkilö)  # {'nimi': 'Anna', 'ikä': 26, 'kaupunki': 'Helsinki'}

# Lisää useita kerralla
henkilö.update({"ammatti": "Insinööri", "puhelin": "040-1234567"})
print(henkilö)
```

### Arvojen poistaminen

```python
henkilö = {
    "nimi": "Anna",
    "ikä": 25,
    "kaupunki": "Helsinki",
    "puhelin": "040-1234567"
}

# Poista del:llä
del henkilö["puhelin"]
print(henkilö)  # puhelin poistettu

# Poista pop():lla (palauttaa arvon)
ikä = henkilö.pop("ikä")
print(f"Poistettiin ikä: {ikä}")  # 25
print(henkilö)

# Poista ja anna oletusarvo jos ei löydy
ammatti = henkilö.pop("ammatti", "Ei tiedossa")
print(ammatti)  # Ei tiedossa

# Tyhjennä koko sanakirja
henkilö.clear()
print(henkilö)  # {}
```

### Tarkistaminen

```python
henkilö = {"nimi": "Anna", "ikä": 25}

# Onko avain olemassa?
print("nimi" in henkilö)      # True
print("osoite" in henkilö)    # False
print("Anna" in henkilö)      # False (Anna on arvo, ei avain!)

# Montako alkiota?
print(len(henkilö))  # 2

# Kaikki avaimet
print(henkilö.keys())    # dict_keys(['nimi', 'ikä'])

# Kaikki arvot
print(henkilö.values())  # dict_values(['Anna', 25])

# Kaikki parit
print(henkilö.items())   # dict_items([('nimi', 'Anna'), ('ikä', 25)])
```

## Sanakirjan läpikäynti

### Avainten läpikäynti

```python
pisteet = {
    "Anna": 95,
    "Pekka": 87,
    "Liisa": 92
}

# Tapa 1: Läpikäynti (oletuksena avaimet)
for nimi in pisteet:
    print(nimi)
# Anna
# Pekka
# Liisa

# Tapa 2: Eksplisiittisesti avaimet
for nimi in pisteet.keys():
    print(nimi)
```

### Arvojen läpikäynti

```python
# Läpikäy vain arvot
for pistemäärä in pisteet.values():
    print(pistemäärä)
# 95
# 87
# 92

# Laske keskiarvo
keskiarvo = sum(pisteet.values()) / len(pisteet)
print(f"Keskiarvo: {keskiarvo:.1f}")  # 91.3
```

### Avain-arvo-parien läpikäynti

```python
# Läpikäy avaimet JA arvot
for nimi, pistemäärä in pisteet.items():
    print(f"{nimi} sai {pistemäärä} pistettä")

# Anna sai 95 pistettä
# Pekka sai 87 pistettä
# Liisa sai 92 pistettä
```

### Käytännön esimerkki

```python
# Laske arvosanat
pisteet = {
    "Anna": 95,
    "Pekka": 87,
    "Liisa": 92,
    "Matti": 76,
    "Kaisa": 68
}

print("=== ARVOSANAT ===\n")

for nimi, pistemäärä in pisteet.items():
    if pistemäärä >= 90:
        arvosana = 5
    elif pistemäärä >= 80:
        arvosana = 4
    elif pistemäärä >= 70:
        arvosana = 3
    elif pistemäärä >= 60:
        arvosana = 2
    else:
        arvosana = 1
    
    print(f"{nimi}: {pistemäärä} pistettä → Arvosana {arvosana}")
```

**Tulostus:**
```
=== ARVOSANAT ===

Anna: 95 pistettä → Arvosana 5
Pekka: 87 pistettä → Arvosana 4
Liisa: 92 pistettä → Arvosana 5
Matti: 76 pistettä → Arvosana 3
Kaisa: 68 pistettä → Arvosana 2
```

## Tuplat (Tuples)

**Tupla** on kuin lista, mutta **muuttumaton** (immutable). Kun tupla on luotu, sitä ei voi muuttaa.

### Miksi käyttää tuplaa?

- ✅ Nopeampi kuin lista
- ✅ Turvallisempi (ei voi vahingossa muuttaa)
- ✅ Voi käyttää sanakirjan avaimena
- ✅ Sopii kiinteälle datalle (esim. koordinaatit, päivämäärät)

### Tuplan luominen

```python
# Tyhjä tupla
tyhjä = ()
tyhjä2 = tuple()

# Tupla arvoilla
koordinaatit = (10, 20)
päivämäärä = (2025, 11, 9)
henkilö = ("Anna", 25, "Helsinki")

# Yhden alkion tupla (huomaa pilkku!)
yksi = (5,)    # Oikein
ei_tupla = (5)  # Väärin! Tämä on vain numero sulkeissa

# Ilman sulkeita (toimii myös)
toinen = 1, 2, 3
print(type(toinen))  # <class 'tuple'>
```

### Tupla vs. lista

```python
# Lista - muutettavissa
lista = [1, 2, 3]
lista[0] = 10    # OK
lista.append(4)  # OK
print(lista)     # [10, 2, 3, 4]

# Tupla - ei muutettavissa
tupla = (1, 2, 3)
# tupla[0] = 10    # TypeError!
# tupla.append(4)  # AttributeError!
print(tupla)       # (1, 2, 3)
```

### Tupla-operaatiot

```python
koordinaatit = (10, 20, 30)

# Hakeminen (kuten listassa)
print(koordinaatit[0])   # 10
print(koordinaatit[-1])  # 30

# Ositus (slicing)
print(koordinaatit[0:2])  # (10, 20)

# Pituus
print(len(koordinaatit))  # 3

# Onko alkio tuplassa?
print(10 in koordinaatit)  # True

# Yhdistäminen
tupla1 = (1, 2)
tupla2 = (3, 4)
yhdistetty = tupla1 + tupla2
print(yhdistetty)  # (1, 2, 3, 4)

# Monistus
kolminkertainen = (1, 2) * 3
print(kolminkertainen)  # (1, 2, 1, 2, 1, 2)
```

### Tupla-purkaminen (unpacking)

```python
# Purkaminen muuttujiin
koordinaatit = (10, 20, 30)
x, y, z = koordinaatit
print(f"x={x}, y={y}, z={z}")  # x=10, y=20, z=30

# Funktio, joka palauttaa tupla
def laske_tilastot(luvut):
    return (min(luvut), max(luvut), sum(luvut) / len(luvut))

pienin, suurin, keskiarvo = laske_tilastot([5, 2, 8, 1, 9])
print(f"Pienin: {pienin}, Suurin: {suurin}, Keskiarvo: {keskiarvo}")

# Vaihda muuttujien arvot
a = 5
b = 10
a, b = b, a  # Käyttää tuplaa taustalla!
print(f"a={a}, b={b}")  # a=10, b=5
```

### Tuplat sanakirjan avaimina

```python
# Lista EI voi olla avain (koska muutettavissa)
# sanakirja = {[1, 2]: "arvo"}  # TypeError!

# Tupla voi olla avain!
koordinaatit_kartta = {
    (0, 0): "Lähtöpiste",
    (10, 5): "Kaupunki",
    (20, 15): "Vuori",
    (-5, 3): "Järvi"
}

print(koordinaatit_kartta[(10, 5)])  # Kaupunki

# Käytännön esimerkki: shakkipeli
shakkilauta = {
    ("a", 1): "Valkoinen torni",
    ("e", 1): "Valkoinen kuningas",
    ("e", 8): "Musta kuningas"
}

print(shakkilauta[("e", 1)])  # Valkoinen kuningas
```

## Listojen järjestäminen

### Perusjärjestäminen

```python
# Numerot
numerot = [5, 2, 8, 1, 9, 3]

# sort() - järjestää listan paikan päällä
numerot.sort()
print(numerot)  # [1, 2, 3, 5, 8, 9]

# sorted() - palauttaa uuden järjestetyn listan
alkuperäinen = [5, 2, 8, 1, 9, 3]
järjestetty = sorted(alkuperäinen)
print(alkuperäinen)  # [5, 2, 8, 1, 9, 3] (ei muuttunut)
print(järjestetty)   # [1, 2, 3, 5, 8, 9]

# Merkkijonot (aakkosjärjestyksessä)
nimet = ["Pekka", "Anna", "Liisa", "Matti"]
nimet.sort()
print(nimet)  # ['Anna', 'Liisa', 'Matti', 'Pekka']
```

### Laskeva järjestys

```python
numerot = [5, 2, 8, 1, 9, 3]

# Laskeva järjestys
numerot.sort(reverse=True)
print(numerot)  # [9, 8, 5, 3, 2, 1]

# sorted():n kanssa
laskeva = sorted([5, 2, 8, 1, 9, 3], reverse=True)
print(laskeva)  # [9, 8, 5, 3, 2, 1]
```

### Erikoistapaukset

```python
# Isot ja pienet kirjaimet
nimet = ["anna", "Pekka", "LIISA", "matti"]
nimet.sort()
print(nimet)  # ['LIISA', 'Pekka', 'anna', 'matti']
# Isot kirjaimet ensin!

# Järjestä isoilla/pienillä kirjaimilla välittämättä
nimet.sort(key=str.lower)
print(nimet)  # ['anna', 'LIISA', 'matti', 'Pekka']

# Järjestä pituuden mukaan
sanat = ["banaani", "omena", "päärynä", "viini"]
sanat.sort(key=len)
print(sanat)  # ['omena', 'viini', 'banaani', 'päärynä']

# Järjestä pituuden mukaan, pisin ensin
sanat.sort(key=len, reverse=True)
print(sanat)  # ['päärynä', 'banaani', 'omena', 'viini']
```

## Tuplien järjestäminen

### Perusjärjestäminen

```python
# Tupla järjestyy ensimmäisen alkion mukaan
koordinaatit = [(5, 2), (1, 8), (3, 4), (1, 2)]
järjestetty = sorted(koordinaatit)
print(järjestetty)  # [(1, 2), (1, 8), (3, 4), (5, 2)]
# Jos ensimmäinen sama, katsotaan toista
```

### Järjestäminen tietyn indeksin mukaan

```python
# Opiskelijat: (nimi, ikä, pisteet)
opiskelijat = [
    ("Anna", 22, 95),
    ("Pekka", 25, 87),
    ("Liisa", 21, 92),
    ("Matti", 23, 87)
]

# Järjestä iän mukaan (indeksi 1)
iän_mukaan = sorted(opiskelijat, key=lambda x: x[1])
print("\nJärjestetty iän mukaan:")
for opiskelija in iän_mukaan:
    print(f"{opiskelija[0]}: {opiskelija[1]} vuotta")

# Järjestä pisteiden mukaan (indeksi 2), suurin ensin
pisteiden_mukaan = sorted(opiskelijat, key=lambda x: x[2], reverse=True)
print("\nJärjestetty pisteiden mukaan:")
for opiskelija in pisteiden_mukaan:
    print(f"{opiskelija[0]}: {opiskelija[2]} pistettä")
```

**Tulostus:**
```
Järjestetty iän mukaan:
Liisa: 21 vuotta
Anna: 22 vuotta
Matti: 23 vuotta
Pekka: 25 vuotta

Järjestetty pisteiden mukaan:
Anna: 95 pistettä
Liisa: 92 pistettä
Pekka: 87 pistettä
Matti: 87 pistettä
```

### Lambda-funktiot järjestämisessä

```python
# Lambda on "pikafunktio"
# Muoto: lambda parametrit: palautusarvo

# Esimerkki 1: Järjestä itseisarvon mukaan
numerot = [-5, 2, -8, 1, 9, -3]
järjestetty = sorted(numerot, key=lambda x: abs(x))
print(järjestetty)  # [1, 2, -3, -5, -8, 9]

# Esimerkki 2: Järjestä merkkijonon pituuden mukaan
sanat = ["kissa", "koira", "hevonen", "kana"]
pituuden_mukaan = sorted(sanat, key=lambda s: len(s))
print(pituuden_mukaan)  # ['kana', 'kissa', 'koira', 'hevonen']

# Esimerkki 3: Monimutkaisempi järjestäminen
# Järjestä ensin pisteiden mukaan, sitten nimen mukaan
opiskelijat = [
    ("Pekka", 87),
    ("Anna", 95),
    ("Liisa", 87),
    ("Matti", 92)
]
järjestetty = sorted(opiskelijat, key=lambda x: (-x[1], x[0]))
# Negatiivinen pisteet -> laskeva, nimi -> nouseva
for nimi, pisteet in järjestetty:
    print(f"{nimi}: {pisteet}")
```

## Sanakirjojen järjestäminen

### Järjestäminen avainten mukaan

```python
pisteet = {
    "Pekka": 87,
    "Anna": 95,
    "Liisa": 92,
    "Matti": 76
}

# Järjestä avainten mukaan
järjestetyt_avaimet = sorted(pisteet.keys())
print("Aakkosjärjestyksessä:")
for nimi in järjestetyt_avaimet:
    print(f"{nimi}: {pisteet[nimi]}")

# Lyhyempi tapa
for nimi in sorted(pisteet):
    print(f"{nimi}: {pisteet[nimi]}")
```

### Järjestäminen arvojen mukaan

```python
pisteet = {
    "Pekka": 87,
    "Anna": 95,
    "Liisa": 92,
    "Matti": 76
}

# Järjestä arvojen mukaan (pienin ensin)
järjestetyt = sorted(pisteet.items(), key=lambda x: x[1])
print("\nPisteiden mukaan (pienin ensin):")
for nimi, pistemäärä in järjestetyt:
    print(f"{nimi}: {pistemäärä}")

# Suurin ensin
järjestetyt = sorted(pisteet.items(), key=lambda x: x[1], reverse=True)
print("\nPisteiden mukaan (suurin ensin):")
for nimi, pistemäärä in järjestetyt:
    print(f"{nimi}: {pistemäärä}")
```

### Järjestetty sanakirja

```python
# Luo uusi järjestetty sanakirja
pisteet = {"Pekka": 87, "Anna": 95, "Liisa": 92, "Matti": 76}

# Järjestetty sanakirja arvojen mukaan
järjestetty_dict = dict(sorted(pisteet.items(), key=lambda x: x[1], reverse=True))
print(järjestetty_dict)
# {'Anna': 95, 'Liisa': 92, 'Pekka': 87, 'Matti': 76}

# HUOM: Python 3.7+ säilyttää sanakirjan järjestyksen
```

## Käytännön sovelluksia

### Sovellus 1: Äänestyssovellus

```python
def laske_äänet():
    """Laskee äänestykseen osallistuneiden äänet"""
    äänet = {}
    
    print("=== ÄÄNESTYS ===")
    print("Kirjoita 'lopeta' lopettaaksesi\n")
    
    while True:
        ehdokas = input("Anna ehdokkaan nimi: ").strip()
        
        if ehdokas.lower() == "lopeta":
            break
        
        if not ehdokas:
            continue
        
        # Lisää ääni
        if ehdokas in äänet:
            äänet[ehdokas] += 1
        else:
            äänet[ehdokas] = 1
        
        print(f"✓ Ääni annettu ehdokkaalle {ehdokas}\n")
    
    # Tulosta tulokset
    print("\n" + "=" * 40)
    print("ÄÄNESTYSTULOKSET")
    print("=" * 40)
    
    # Järjestä äänet suurimmasta pienimpään
    järjestetyt = sorted(äänet.items(), key=lambda x: x[1], reverse=True)
    
    yhteensä = sum(äänet.values())
    
    for sijoitus, (ehdokas, äänimäärä) in enumerate(järjestetyt, 1):
        prosentti = (äänimäärä / yhteensä) * 100
        print(f"{sijoitus}. {ehdokas}: {äänimäärä} ääntä ({prosentti:.1f}%)")
    
    print("=" * 40)
    print(f"Ääniä yhteensä: {yhteensä}")
    
    # Voittaja
    if järjestetyt:
        voittaja = järjestetyt[0][0]
        print(f"🏆 Voittaja: {voittaja}")

# Käyttö
laske_äänet()
```

### Sovellus 2: Sanakirjan lukumäärälaskuri

```python
def laske_sanat(teksti):
    """Laskee kuinka monta kertaa kukin sana esiintyy tekstissä"""
    # Muunna pieniksi kirjaimiksi ja jaa sanoiksi
    sanat = teksti.lower().split()
    
    # Laske sanat
    sanalaskuri = {}
    for sana in sanat:
        # Poista välimerkit
        sana = sana.strip(".,!?;:")
        if sana:
            sanalaskuri[sana] = sanalaskuri.get(sana, 0) + 1
    
    return sanalaskuri

# Esimerkki
teksti = """
Python on loistava ohjelmointikieli. Python on helppo oppia.
Monet käyttävät Python-kieltä data-analytiikkaan.
Python on suosittu.
"""

sanalaskuri = laske_sanat(teksti)

# Tulosta yleisimmät sanat
print("=== YLEISIMMÄT SANAT ===\n")
järjestetyt = sorted(sanalaskuri.items(), key=lambda x: x[1], reverse=True)

for sana, määrä in järjestetyt[:10]:  # Top 10
    print(f"{sana}: {määrä} kertaa")
```

**Tulostus:**
```
=== YLEISIMMÄT SANAT ===

python: 4 kertaa
on: 3 kertaa
ohjelmointikieli: 1 kertaa
loistava: 1 kertaa
helppo: 1 kertaa
oppia: 1 kertaa
...
```

### Sovellus 3: Opiskelijatietokanta

```python
def opiskelijatietokanta():
    """Hallinnoi opiskelijoiden tietoja"""
    opiskelijat = {}
    
    while True:
        print("\n=== OPISKELIJATIETOKANTA ===")
        print("1. Lisää opiskelija")
        print("2. Näytä kaikki opiskelijat")
        print("3. Hae opiskelija")
        print("4. Järjestä pisteiden mukaan")
        print("5. Poistu")
        
        valinta = input("\nValitse toiminto (1-5): ").strip()
        
        if valinta == "1":
            nimi = input("Opiskelijan nimi: ").strip()
            try:
                pisteet = int(input("Pisteet: "))
                opiskelijat[nimi] = {
                    "pisteet": pisteet,
                    "päivämäärä": "2025-11-09"
                }
                print(f"✓ {nimi} lisätty!")
            except ValueError:
                print("❌ Virheelliset pisteet!")
        
        elif valinta == "2":
            if not opiskelijat:
                print("Ei opiskelijoita")
            else:
                print("\nKaikki opiskelijat:")
                for nimi, tiedot in opiskelijat.items():
                    print(f"  {nimi}: {tiedot['pisteet']} pistettä")
        
        elif valinta == "3":
            nimi = input("Anna nimi: ").strip()
            if nimi in opiskelijat:
                tiedot = opiskelijat[nimi]
                print(f"\n{nimi}:")
                print(f"  Pisteet: {tiedot['pisteet']}")
                print(f"  Päivämäärä: {tiedot['päivämäärä']}")
            else:
                print("❌ Opiskelijaa ei löydy")
        
        elif valinta == "4":
            if not opiskelijat:
                print("Ei opiskelijoita")
            else:
                järjestetyt = sorted(
                    opiskelijat.items(),
                    key=lambda x: x[1]['pisteet'],
                    reverse=True
                )
                print("\nJärjestetty pisteiden mukaan:")
                for sijoitus, (nimi, tiedot) in enumerate(järjestetyt, 1):
                    print(f"  {sijoitus}. {nimi}: {tiedot['pisteet']} pistettä")
        
        elif valinta == "5":
            print("Näkemiin!")
            break
        
        else:
            print("❌ Virheellinen valinta")

# Käyttö
# opiskelijatietokanta()
```

### Sovellus 4: Koordinaattipisteiden analysointi

```python
def analysoi_koordinaatit(pisteet):
    """Analysoi koordinaattipisteet"""
    if not pisteet:
        print("Ei pisteitä analysoitavaksi")
        return
    
    # Etsi äärimmäiset pisteet
    x_koordinaatit = [p[0] for p in pisteet]
    y_koordinaatit = [p[1] for p in pisteet]
    
    print("=== KOORDINAATTIANALYYSI ===\n")
    print(f"Pisteitä yhteensä: {len(pisteet)}")
    print(f"X-koordinaatit: {min(x_koordinaatit)} - {max(x_koordinaatit)}")
    print(f"Y-koordinaatit: {min(y_koordinaatit)} - {max(y_koordinaatit)}")
    
    # Laske etäisyydet origosta
    etäisyydet = []
    for x, y in pisteet:
        etäisyys = (x**2 + y**2) ** 0.5
        etäisyydet.append(((x, y), etäisyys))
    
    # Järjestä etäisyyden mukaan
    järjestetyt = sorted(etäisyydet, key=lambda x: x[1])
    
    print(f"\nLähin piste origoon: {järjestetyt[0][0]} (etäisyys: {järjestetyt[0][1]:.2f})")
    print(f"Kaukaisin piste origosta: {järjestetyt[-1][0]} (etäisyys: {järjestetyt[-1][1]:.2f})")
    
    # Järjestä x-koordinaatin mukaan
    x_järjestyksessä = sorted(pisteet, key=lambda p: p[0])
    print(f"\nVasen piste: {x_järjestyksessä[0]}")
    print(f"Oikea piste: {x_järjestyksessä[-1]}")
    
    # Järjestä y-koordinaatin mukaan
    y_järjestyksessä = sorted(pisteet, key=lambda p: p[1])
    print(f"Alin piste: {y_järjestyksessä[0]}")
    print(f"Ylin piste: {y_järjestyksessä[-1]}")

# Esimerkki
pisteet = [
    (5, 2),
    (1, 8),
    (3, 4),
    (-2, 6),
    (7, 1),
    (0, 0)
]

analysoi_koordinaatit(pisteet)
```

## Yhteenveto

### Mitä opimme?

**Sanakirjat (dictionaries)**
- Tallentavat tietoa avain-arvo-pareina
- Nopea haku avaimella
- Muutettavissa (mutable)
- Operaatiot: `get()`, `pop()`, `keys()`, `values()`, `items()`

**Tuplat (tuples)**
- Kuin lista, mutta muuttumaton (immutable)
- Nopeampi ja turvallisempi kuin lista
- Voi käyttää sanakirjan avaimena
- Tupla-purkaminen: `x, y, z = (1, 2, 3)`

**Järjestäminen**
- `sort()` - järjestää listan paikan päällä
- `sorted()` - palauttaa uuden järjestetyn listan
- `reverse=True` - laskeva järjestys
- `key=funktio` - mukautettu järjestäminen
- Lambda-funktiot: `lambda x: x[1]`

### Vertailutaulukko

| Rakenne | Muutettava? | Järjestetty? | Avaimet? | Käyttö |
|---------|-------------|--------------|----------|--------|
| **Lista** | ✅ Kyllä | ❌ Ei | Indeksi | Järjestetty kokoelma |
| **Tupla** | ❌ Ei | ❌ Ei | Indeksi | Kiinteä data |
| **Sanakirja** | ✅ Kyllä | ✅ Python 3.7+ | Mikä tahansa | Avain-arvo-parit |

### Kun käyttää mitäkin?

**Lista** 📝
- Tarvitset muutettavan järjestetyn kokoelman
- Käytät indeksejä
- Haluat lisätä/poistaa alkioita

**Tupla** 🔒
- Data ei muutu (esim. koordinaatit, päivämäärät)
- Tarvitset sanakirjan avaimen
- Haluat suojata datan vahingollisilta muutoksilta

**Sanakirja** 🗂️
- Tarvitset nopean haun avaimella
- Data koostuu avain-arvo-pareista
- Mallitat objekteja tai asetuksia

### Järjestämisen muistisäännöt

```python
# Perusjärjestäminen
lista.sort()              # Muuttaa listan
uusi = sorted(lista)      # Luo uuden

# Laskeva järjestys
lista.sort(reverse=True)

# Mukautettu järjestys
lista.sort(key=len)                    # Pituuden mukaan
lista.sort(key=lambda x: x[1])         # Tupla: toinen alkio
dict.items(), key=lambda x: x[1])      # Sanakirja: arvon mukaan
```

### Hyödyllisiä vinkkejä

1. **Käytä `get()` sanakirjan kanssa** - ei aiheuta KeyErroria
2. **Tuplat ovat nopeampia** - käytä kun data ei muutu
3. **Lambda on kätevä** - lyhyet yksiriviset funktiot
4. **enumerate()** - saat indeksin ja arvon: `for i, arvo in enumerate(lista)`
5. **zip()** - yhdistä listoja: `for nimi, ikä in zip(nimet, iät)`

### Harjoitustehtäviä

1. **Puhelinluettelo**: Luo sanakirja, jossa voit lisätä, hakea ja poistaa yhteystietoja

2. **Top 5 -lista**: Kysy käyttäjältä sanoja ja pisteitä, järjestä ja näytä top 5

3. **Koordinaattien järjestäminen**: Luo lista koordinaateista ja järjestä ne etäisyyden mukaan origosta

4. **Sanojen laskuri**: Lue tekstitiedosto ja laske yleisimmät sanat

5. **Opiskelijan keskiarvo**: Tallenna opiskelijan arvosanat sanakirjaan ja laske keskiarvo

Muista: Oikean tietorakenteen valinta tekee koodista selkeämpää ja tehokkaampaa! 🚀
