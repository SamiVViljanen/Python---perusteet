# Harjoitukset: Oliot

Tee seuraavat harjoitukset järjestyksessä. Jokaista harjoitusta varten on oma alakansio.

---

## Harjoitus 1: Ensimmäinen luokka (⭐ Helppo)

**Tavoite:** Harjoittele yksinkertaisen luokan määrittämistä.

**Tehtävä:**
1. Luo luokka `Koira` joka ottaa `__init__`-metodissa parametrit:
   - `nimi` (merkkijono)
   - `rotu` (merkkijono)
2. Tallenna parametrit `self.nimi` ja `self.rotu` muuttujiin
3. Luo metodi `hauku()` joka tulostaa: "Hau hau! Minä olen [nimi]."
4. Luo kaksi Koira-oliota ja kutsu niiden `hauku()`-metodeja

**Esimerkki:**
```
Hau hau! Minä olen Musti.
Hau hau! Minä olen Rekku.
```

💡 **Vinkki:** Luokka alkaa `class Koira:` ja metodi `def hauku(self):`

📝 **Tiedosto:** [Harjoitus 1/](Harjoitus%201/) | [harjoitus1.py](Harjoitus%201/harjoitus1.py)

---

## Harjoitus 2: Dataclass (⭐⭐ Helppo)

**Tavoite:** Harjoittele `@dataclass`-dekoraattorin käyttöä.

**Tehtävä:**
1. Tuo `dataclass` kirjastosta: `from dataclasses import dataclass`
2. Luo dataclass `Opiskelija` jolla on attribuutit:
   - `nimi: str`
   - `ikä: int`
   - `opiskelijanumero: str`
3. Luo 2-3 opiskelijaoliota
4. Tulosta oliot (dataclass tekee automaattisesti siistin tulostuksen!)

**Esimerkki:**
```
Opiskelija(nimi='Anna', ikä=22, opiskelijanumero='12345')
Opiskelija(nimi='Matti', ikä=24, opiskelijanumero='67890')
```

💡 **Vinkki:** Dataclass tekee `__init__`:n automaattisesti, ei tarvitse kirjoittaa!

📝 **Tiedosto:** [Harjoitus 2/](Harjoitus%202/) | [harjoitus2.py](Harjoitus%202/harjoitus2.py)

---

## Harjoitus 3: Metodi joka käyttää attribuutteja (⭐⭐ Keskitaso)

**Tavoite:** Harjoittele metodeja jotka käyttävät olion attribuutteja.

**Tehtävä:**
1. Luo luokka `Suorakulmio` joka ottaa `__init__`:ssä:
   - `leveys` (luku)
   - `korkeus` (luku)
2. Luo metodi `laske_pinta_ala()` joka:
   - Palauttaa pinta-alan: `self.leveys * self.korkeus`
3. Luo metodi `laske_piiri()` joka:
   - Palauttaa piirin: `2 * (self.leveys + self.korkeus)`
4. Luo suorakulmio-olio (esim. 5 x 10) ja tulosta pinta-ala ja piiri

**Esimerkki:**
```
Pinta-ala: 50
Piiri: 30
```

💡 **Vinkki:** Metodit voivat käyttää `self.leveys` ja `self.korkeus` attribuutteja!

📝 **Tiedosto:** [Harjoitus 3/](Harjoitus%203/) | [harjoitus3.py](Harjoitus%203/harjoitus3.py)

---

## Harjoitus 4: Luokka laskurilla (⭐⭐⭐ Keskitaso)

**Tavoite:** Harjoittele muuttuvaa tilaa oliossa.

**Tehtävä:**
1. Luo luokka `Laskuri` joka `__init__`:ssä:
   - Alustaa `self.arvo = 0`
2. Luo metodi `kasvata()` joka:
   - Kasvattaa `self.arvo`-muuttujaa yhdellä
3. Luo metodi `vahenna()` joka:
   - Vähentää `self.arvo`-muuttujaa yhdellä
4. Luo metodi `näytä()` joka:
   - Tulostaa nykyisen arvon
5. Testaa: luo laskuri, kasvata 3 kertaa, vähennä kerran, näytä tulos

**Esimerkki:**
```
Laskurin arvo: 2
```

💡 **Vinkki:** Olio "muistaa" arvonsa kutsujen välillä!

📝 **Tiedosto:** [Harjoitus 4/](Harjoitus%204/) | [harjoitus4.py](Harjoitus%204/harjoitus4.py)

---

## Harjoitus 5: Pankkitili-luokka (⭐⭐⭐⭐ Haaste)

**Tavoite:** Yhdistä kaikki oppimasi ja luo käytännöllinen luokka.

**Tehtävä:**
1. Luo luokka `Pankkitili` joka `__init__`:ssä ottaa:
   - `omistaja` (merkkijono)
   - `saldo` (luku, oletusarvo 0)
2. Luo metodi `talleta(summa)` joka:
   - Lisää summan saldoon
   - Tulostaa: "Talletettiin [summa]€. Uusi saldo: [saldo]€"
3. Luo metodi `nosta(summa)` joka:
   - Tarkistaa onko saldoa tarpeeksi
   - Jos on: vähentää summan ja tulostaa uuden saldon
   - Jos ei: tulostaa "Ei tarpeeksi rahaa!"
4. Luo metodi `näytä_saldo()` joka tulostaa saldon

**Esimerkki:**
```
Talletettiin 100€. Uusi saldo: 100€
Talletettiin 50€. Uusi saldo: 150€
Nostettiin 30€. Uusi saldo: 120€
Ei tarpeeksi rahaa!
Tilin saldo: 120€
```

💡 **Vinkit:**
- `if self.saldo >= summa:` tarkistaa saldon riittävyyden
- Muista `self.saldo += summa` ja `self.saldo -= summa`
- Voit antaa oletusarvon: `def __init__(self, omistaja, saldo=0):`

📝 **Tiedosto:** [Harjoitus 5/](Harjoitus%205/) | [harjoitus5.py](Harjoitus%205/harjoitus5.py)

---

## Valmis?

Kun olet tehnyt harjoitukset, voit verrata vastauksiasi [Vastaukset](../Vastaukset/)-kansiossa oleviin mallivastauksiin.

💪 Muista: On täysin normaalia, että ratkaisusi näyttää erilaiselta kuin malliratkaisut. Tärkeintä on, että ohjelma toimii oikein!
