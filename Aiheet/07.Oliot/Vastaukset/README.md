# Vastaukset: Oliot

Tässä kansiossa on kaikkien harjoitusten mallivastaukset sekä selitykset.

---

## Harjoitus 1: Ensimmäinen luokka ⭐

### Ratkaisu
[harjoitus1.py](harjoitus1.py)

```python
class Koira:
    def __init__(self, nimi, rotu):
        self.nimi = nimi
        self.rotu = rotu
    
    def hauku(self):
        print(f"Hau hau! Minä olen {self.nimi}.")

koira1 = Koira("Musti", "Sekarotuinen")
koira2 = Koira("Rekku", "Labradorinnoutaja")

koira1.hauku()
koira2.hauku()
```

### Selitys
- **class Koira:** Määrittää uuden luokan nimeltä Koira
- **__init__:** Erityinen metodi jota kutsutaan kun olio luodaan (konstruktori)
- **self:** Viittaa luotavaan olioon itseensä
- **self.nimi:** Olion attribuutti (muuttuja joka kuuluu oliolle)
- **def hauku(self):** Metodi (funktio joka kuuluu luokalle)

### Mikä on self?

`self` on viittaus **siihen olioon jota juuri käsitellään**.

```python
koira1 = Koira("Musti", "Sekarotuinen")
# Kun kutsut: koira1.hauku()
# → self viittaa koira1-olioon
# → self.nimi on "Musti"

koira2 = Koira("Rekku", "Labradorinnoutaja")  
# Kun kutsut: koira2.hauku()
# → self viittaa koira2-olioon
# → self.nimi on "Rekku"
```

### Opittavaa
✅ Luokka on "kaava" josta voidaan luoda monta oliota  
✅ `__init__` alustetaan automaattisesti kun olio luodaan  
✅ `self` viittaa aina kyseiseen olioon  
✅ Attribuutit tallennetaan `self.nimi` muotoon  
💡 Jokainen olio on itsenäinen - `koira1.nimi` ≠ `koira2.nimi`

---

## Harjoitus 2: Dataclass ⭐⭐

### Ratkaisu
[harjoitus2.py](harjoitus2.py)

```python
from dataclasses import dataclass

@dataclass
class Opiskelija:
    nimi: str
    ikä: int
    opiskelijanumero: str

opiskelija1 = Opiskelija("Anna", 22, "12345")
opiskelija2 = Opiskelija("Matti", 24, "67890")
opiskelija3 = Opiskelija("Liisa", 21, "11111")

print(opiskelija1)
print(opiskelija2)
print(opiskelija3)
```

### Selitys
- **@dataclass:** Dekoraattori joka luo automaattisesti `__init__`, `__repr__` ja `__eq__` metodit
- **Tyyppimerkinnät:** `nimi: str` kertoo että nimi on merkkijono
- **Ei __init__:iä tarvita:** Dataclass tekee sen automaattisesti!

### Dataclass vs normaali luokka

**Ilman dataclassia:**
```python
class Opiskelija:
    def __init__(self, nimi, ikä, opiskelijanumero):
        self.nimi = nimi
        self.ikä = ikä
        self.opiskelijanumero = opiskelijanumero
    
    def __repr__(self):
        return f"Opiskelija(nimi={self.nimi}, ikä={self.ikä}, opiskelijanumero={self.opiskelijanumero})"
```

**Dataclassilla:**
```python
@dataclass
class Opiskelija:
    nimi: str
    ikä: int
    opiskelijanumero: str
```

Molemmat tekevät saman asian, mutta dataclass on paljon lyhyempi! 🎉

### Milloin käytät dataclassia?

✅ **Käytä dataclassia kun:**
- Luokka sisältää pääasiassa dataa (attribuutteja)
- Ei tarvitse monimutkaista logiikkaa
- Haluat nopean ja helpon tavan luoda "data-säiliö"

❌ **Älä käytä dataclassia kun:**
- Tarvitset monimutkaisen `__init__`:in
- Luokka sisältää paljon logiikkaa ja metodeja
- Tarvitset erityistä käyttäytymistä

### Opittavaa
✅ Dataclass säästää aikaa ja vähentää koodia  
✅ Tyyppimerkinnät auttavat ymmärtämään mitä dataa odotetaan  
✅ Automaattiset metodit (`__repr__`, `__eq__`) tekevät elämästä helpompaa  
💡 Dataclass on täydellinen kun tarvitset vain "data-paketin"!

---

## Harjoitus 3: Metodi joka käyttää attribuutteja ⭐⭐

### Ratkaisu
[harjoitus3.py](harjoitus3.py)

```python
class Suorakulmio:
    def __init__(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus
    
    def laske_pinta_ala(self):
        return self.leveys * self.korkeus
    
    def laske_piiri(self):
        return 2 * (self.leveys + self.korkeus)

suorakulmio = Suorakulmio(5, 10)

print(f"Pinta-ala: {suorakulmio.laske_pinta_ala()}")
print(f"Piiri: {suorakulmio.laske_piiri()}")
```

### Selitys
- **Metodit käyttävät attribuutteja:** `self.leveys` ja `self.korkeus`
- **return:** Palauttaa lasketun arvon
- **Metodikutsu:** `suorakulmio.laske_pinta_ala()` kutsuu metodia ja palauttaa tuloksen

### Miksi metodit ovat hyödyllisiä?

**Huono tapa (ilman metodeja):**
```python
class Suorakulmio:
    def __init__(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus

suorakulmio = Suorakulmio(5, 10)
pinta_ala = suorakulmio.leveys * suorakulmio.korkeus  # Lasketaan ulkona
piiri = 2 * (suorakulmio.leveys + suorakulmio.korkeus)  # Lasketaan ulkona
```

**Hyvä tapa (metodit):**
```python
class Suorakulmio:
    def __init__(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus
    
    def laske_pinta_ala(self):
        return self.leveys * self.korkeus
    
    def laske_piiri(self):
        return 2 * (self.leveys + self.korkeus)

suorakulmio = Suorakulmio(5, 10)
pinta_ala = suorakulmio.laske_pinta_ala()  # Selkeä ja uudelleenkäytettävä
piiri = suorakulmio.laske_piiri()
```

Metodit:
- ✅ Pitävät logiikan luokan sisällä
- ✅ Helpottavat uudelleenkäyttöä
- ✅ Tekevät koodista luettavampaa

### Opittavaa
✅ Metodit voivat käyttää olion attribuutteja (`self.leveys`)  
✅ `return` palauttaa arvon metodista  
✅ Logiikka kuuluu metodeihin, ei luokan ulkopuolelle  
💡 Oliot yhdistävät datan ja toiminnan samaan paikkaan!

---

## Harjoitus 4: Luokka laskurilla ⭐⭐⭐

### Ratkaisu
[harjoitus4.py](harjoitus4.py)

```python
class Laskuri:
    def __init__(self):
        self.arvo = 0
    
    def kasvata(self):
        self.arvo += 1
    
    def vahenna(self):
        self.arvo -= 1
    
    def näytä(self):
        print(f"Laskurin arvo: {self.arvo}")

laskuri = Laskuri()

laskuri.kasvata()
laskuri.kasvata()
laskuri.kasvata()

laskuri.vahenna()

laskuri.näytä()
```

### Selitys
- **Muuttuva tila:** Olio "muistaa" arvonsa metodikutsujen välillä
- **self.arvo:** Attribuutti joka säilyy olion elinkaaren ajan
- **Ei parametreja:** `kasvata()` ja `vahenna()` eivät tarvitse parametreja koska ne muokkaavat `self.arvo`

### Miten olio muistaa?

```python
laskuri = Laskuri()  # arvo = 0

laskuri.kasvata()    # arvo = 1
laskuri.kasvata()    # arvo = 2
laskuri.kasvata()    # arvo = 3

laskuri.vahenna()    # arvo = 2

laskuri.näytä()      # Tulostaa: Laskurin arvo: 2
```

Jokainen metodikutsu **muokkaa samaa oliota** → arvo säilyy!

### Vertailu: funktio vs olio

**Funktio (ei muista tilaa):**
```python
arvo = 0

def kasvata():
    global arvo  # Tarvitaan global!
    arvo += 1

def näytä():
    print(f"Arvo: {arvo}")

kasvata()
kasvata()
näytä()  # Arvo: 2
```

**Olio (muistaa tilan):**
```python
class Laskuri:
    def __init__(self):
        self.arvo = 0
    
    def kasvata(self):
        self.arvo += 1  # Ei tarvitse globalia!
    
    def näytä(self):
        print(f"Arvo: {self.arvo}")

laskuri = Laskuri()
laskuri.kasvata()
laskuri.kasvata()
laskuri.näytä()  # Arvo: 2
```

Oliot ovat paljon selkeämpiä kun tarvitaan **tilaa** (state)!

### Opittavaa
✅ Oliot muistavat tilansa metodikutsujen välillä  
✅ `self.arvo` säilyy olion elinkaaren ajan  
✅ Ei tarvitse `global`-muuttujia  
💡 Oliot ovat täydellisiä kun haluat "muistavan" rakenteen!

---

## Harjoitus 5: Pankkitili-luokka ⭐⭐⭐⭐

### Ratkaisu
[harjoitus5.py](harjoitus5.py)

```python
class Pankkitili:
    def __init__(self, omistaja, saldo=0):
        self.omistaja = omistaja
        self.saldo = saldo
    
    def talleta(self, summa):
        self.saldo += summa
        print(f"Talletettiin {summa}€. Uusi saldo: {self.saldo}€")
    
    def nosta(self, summa):
        if self.saldo >= summa:
            self.saldo -= summa
            print(f"Nostettiin {summa}€. Uusi saldo: {self.saldo}€")
        else:
            print("Ei tarpeeksi rahaa!")
    
    def näytä_saldo(self):
        print(f"Tilin saldo: {self.saldo}€")

tili = Pankkitili("Matti Meikäläinen")

tili.talleta(100)
tili.talleta(50)
tili.nosta(30)
tili.nosta(200)  # Epäonnistuu
tili.näytä_saldo()
```

### Selitys
- **Oletusarvo:** `saldo=0` antaa oletusarvon jos sitä ei anneta
- **Parametrit metodissa:** `talleta(summa)` ja `nosta(summa)` ottavat summan parametrina
- **Ehto:** `if self.saldo >= summa` tarkistaa onko rahaa tarpeeksi
- **Tila muuttuu:** Jokainen talletus/nosto muuttaa `self.saldo`

### Oletusarvo parametrissa

```python
def __init__(self, omistaja, saldo=0):
```

Tämä tarkoittaa:
```python
tili1 = Pankkitili("Matti")           # saldo = 0 (oletusarvo)
tili2 = Pankkitili("Anna", 500)       # saldo = 500 (annettu arvo)
```

### Metodit parametreilla

```python
def talleta(self, summa):
    self.saldo += summa
```

`self` on **aina ensimmäinen parametri**, mutta sitä ei anneta kutsussa:
```python
tili.talleta(100)  # self = tili, summa = 100
```

Python antaa `self`:n automaattisesti!

### Ehto metodissa

```python
def nosta(self, summa):
    if self.saldo >= summa:
        self.saldo -= summa
        print(f"Nostettiin {summa}€. Uusi saldo: {self.saldo}€")
    else:
        print("Ei tarpeeksi rahaa!")
```

Tämä estää saldon menemisen negatiiviseksi!

### Käytännön esimerkki

```python
tili = Pankkitili("Matti", 100)  # Alkusaldo 100€

tili.talleta(50)   # saldo = 150€
tili.nosta(30)     # saldo = 120€
tili.nosta(200)    # Ei onnistu! saldo pysyy 120€
```

### Vaihtoehtoinen ratkaisu (lisäominaisuuksia)

```python
class Pankkitili:
    def __init__(self, omistaja, saldo=0):
        self.omistaja = omistaja
        self.saldo = saldo
        self.tapahtumat = []  # Lista tapahtumista
    
    def talleta(self, summa):
        self.saldo += summa
        self.tapahtumat.append(f"Talletus: +{summa}€")
        print(f"Talletettiin {summa}€. Uusi saldo: {self.saldo}€")
    
    def nosta(self, summa):
        if self.saldo >= summa:
            self.saldo -= summa
            self.tapahtumat.append(f"Nosto: -{summa}€")
            print(f"Nostettiin {summa}€. Uusi saldo: {self.saldo}€")
        else:
            print("Ei tarpeeksi rahaa!")
    
    def näytä_tapahtumat(self):
        print("Tapahtumat:")
        for tapahtuma in self.tapahtumat:
            print(f"  - {tapahtuma}")
```

Nyt voit myös nähdä tapahtumahistorian! 📊

### Opittavaa
✅ Oletusarvot parametreissa: `saldo=0`  
✅ Metodit voivat ottaa parametreja: `talleta(summa)`  
✅ Ehdot metodien sisällä: `if self.saldo >= summa`  
✅ Tila muuttuu ajan myötä: `self.saldo += summa`  
💡 Luokka mallintaa "asian" jolla on tila ja käyttäytyminen!

---

## Yhteenveto: Olioiden keskeiset käsitteet

### 1. Luokka (Class)
"Kaava" tai "muotti" josta luodaan olioita.

```python
class Auto:  # Luokka
    pass
```

### 2. Olio (Object/Instance)
Luokasta luotu yksittäinen "kappale".

```python
auto1 = Auto()  # Olio
auto2 = Auto()  # Toinen olio
```

### 3. __init__ (Konstruktori)
Metodi jota kutsutaan kun olio luodaan.

```python
class Auto:
    def __init__(self, merkki):
        self.merkki = merkki
```

### 4. self
Viittaus siihen olioon jota käsitellään.

```python
class Auto:
    def __init__(self, merkki):
        self.merkki = merkki  # self = tämä olio
```

### 5. Attribuutit
Olion muuttujat (data).

```python
class Auto:
    def __init__(self, merkki):
        self.merkki = merkki  # Attribuutti
```

### 6. Metodit
Olion funktiot (toiminta).

```python
class Auto:
    def aja(self):  # Metodi
        print("Auto ajaa!")
```

### 7. Dataclass
Helppokäyttöinen tapa luoda data-luokkia.

```python
@dataclass
class Auto:
    merkki: str
    vuosi: int
```

---

## Yleisiä virheitä

### 1. Unohdetaan self
❌ **VÄÄRIN:**
```python
class Koira:
    def __init__(nimi):  # self puuttuu!
        nimi = nimi
```

✅ **OIKEIN:**
```python
class Koira:
    def __init__(self, nimi):  # self mukana
        self.nimi = nimi
```

### 2. Unohdetaan self.attribuutti
❌ **VÄÄRIN:**
```python
class Koira:
    def __init__(self, nimi):
        nimi = nimi  # Ei tallennu olioon!
    
    def hauku(self):
        print(f"Hau! {nimi}")  # NameError!
```

✅ **OIKEIN:**
```python
class Koira:
    def __init__(self, nimi):
        self.nimi = nimi  # Tallennetaan olioon
    
    def hauku(self):
        print(f"Hau! {self.nimi}")  # Toimii!
```

### 3. Annetaan self kutsussa
❌ **VÄÄRIN:**
```python
koira = Koira()
koira.hauku(koira)  # self annetaan automaattisesti!
```

✅ **OIKEIN:**
```python
koira = Koira()
koira.hauku()  # Python antaa self:n automaattisesti
```

### 4. Käytetään luokkaa olion sijaan
❌ **VÄÄRIN:**
```python
class Laskuri:
    def __init__(self):
        self.arvo = 0

Laskuri.kasvata()  # TypeError! Laskuri on luokka, ei olio
```

✅ **OIKEIN:**
```python
class Laskuri:
    def __init__(self):
        self.arvo = 0
    
    def kasvata(self):
        self.arvo += 1

laskuri = Laskuri()  # Luo olio
laskuri.kasvata()    # Kutsu olion metodia
```

---

## Vinkkejä

💡 **Luokkien nimet:** CamelCase (esim. `Pankkitili`, `SähköPosti`)  
💡 **Metodien/attribuuttien nimet:** snake_case (esim. `laske_summa`, `näytä_saldo`)  
💡 **Yksi vastuu:** Yksi luokka tekee yhden asian hyvin  
💡 **Testaa pienissä osissa:** Testaa jokainen metodi erikseen  
💡 **Käytä dataclassia:** Jos luokka on vain data-säiliö

---

## Milloin käytät olioita?

✅ **Käytä olioita kun:**
- Haluat mallintaa "asian" jolla on tila ja käyttäytyminen
- Tarvitset useita samankaltaisia "kappaleita" (esim. useita koiria, tilejä)
- Haluat yhdistää datan ja toiminnan samaan paikkaan
- Ohjelma on monimutkainen ja tarvitsee rakennetta

❌ **Älä käytä olioita kun:**
- Riittää yksinkertainen funktio
- Ei tarvita tilaa (state)
- Ohjelma on hyvin pieni ja yksinkertainen

---

Hienoa työtä! Olet nyt oppinut olioiden perusteet. 🎉

➡️**Seuraavaksi:** [Aihe 08 - Moduulit ja kirjastot](../../08.Moduulit%20ja%20kirjastot/)
