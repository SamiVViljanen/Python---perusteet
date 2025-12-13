# Harjoitukset: For-silmukka

Tee seuraavat harjoitukset järjestyksessä. Jokaista harjoitusta varten on oma alakansio.

---

## Harjoitus 1: Tulosta numerot 1-10 (⭐ Helppo)

**Tavoite:** Harjoittele `range()`-funktion käyttöä for-silmukassa.

**Tehtävä:**
1. Käytä for-silmukkaa tulostamaan numerot 1-10
2. Jokainen numero omalle rivilleen

**Esimerkki:**
```
1
2
3
4
5
6
7
8
9
10
```

💡 **Vinkki:** `range(1, 11)` tuottaa luvut 1-10

📝 **Tiedosto:** [Harjoitus 1/](Harjoitus%201/) | [harjoitus1.py](Harjoitus%201/harjoitus1.py)

---

## Harjoitus 2: Parilliset luvut (⭐⭐ Helppo)

**Tavoite:** Harjoittele `range()`-funktion askellusta (step).

**Tehtävä:**
1. Tulosta kaikki parilliset luvut väliltä 0-20
2. Käytä range()-funktion kolmatta parametria (askellus)

**Esimerkki:**
```
0
2
4
6
8
10
12
14
16
18
20
```

💡 **Vinkki:** `range(0, 21, 2)` tuottaa joka toisen luvun

📝 **Tiedosto:** [Harjoitus 2/](Harjoitus%202/) | [harjoitus2.py](Harjoitus%202/harjoitus2.py)

---

## Harjoitus 3: Listan läpikäynti (⭐⭐ Keskitaso)

**Tavoite:** Harjoittele listan läpikäyntiä for-silmukalla.

**Tehtävä:**
1. Luo lista: `hedelmät = ["omena", "banaani", "appelsiini", "päärynä"]`
2. Käy lista läpi for-silmukalla
3. Tulosta jokainen hedelmä numeroidusti muodossa: "1. omena"

**Esimerkki:**
```
1. omena
2. banaani
3. appelsiini
4. päärynä
```

💡 **Vinkit:**
- Voit käyttää `enumerate()` saadaksesi indeksin
- Muista että indeksointi alkaa 0:sta, joten lisää 1

📝 **Tiedosto:** [Harjoitus 3/](Harjoitus%203/) | [harjoitus3.py](Harjoitus%203/harjoitus3.py)

---

## Harjoitus 4: Summan laskeminen (⭐⭐⭐ Keskitaso)

**Tavoite:** Harjoittele muuttujan päivittämistä silmukassa (gatherer-rooli).

**Tehtävä:**
1. Laske ja tulosta kaikkien lukujen summa väliltä 1-100
2. Käytä for-silmukkaa ja summa-muuttujaa

**Esimerkki:**
```
Lukujen 1-100 summa on: 5050
```

💡 **Vinkit:**
- Alusta summa: `summa = 0`
- Päivitä silmukassa: `summa += i`

📝 **Tiedosto:** [Harjoitus 4/](Harjoitus%204/) | [harjoitus4.py](Harjoitus%204/harjoitus4.py)

---

## Harjoitus 5: Kertotaulu (⭐⭐⭐ Keskitaso)

**Tavoite:** Harjoittele for-silmukkaa käytännön laskuissa.

**Tehtävä:**
1. Kysy käyttäjältä luku (1-10)
2. Tulosta kyseisen luvun kertotaulu 1-10

**Esimerkki:**
```
Minkä luvun kertotaulu? 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

💡 **Vinkki:** Käytä f-stringiä muotoiluun: `f"{luku} x {i} = {luku * i}"`

📝 **Tiedosto:** [Harjoitus 5/](Harjoitus%205/) | [harjoitus5.py](Harjoitus%205/harjoitus5.py)

---

## Harjoitus 6: FizzBuzz (⭐⭐⭐⭐ Haaste)

**Tavoite:** Yhdistä for-silmukka ja ehtolauseet (klassinen ohjelmointihaaste!).

**Tehtävä:**
1. Tulosta luvut 1-30
2. **MUTTA:**
   - Jos luku on jaollinen 3:lla, tulosta "Fizz"
   - Jos luku on jaollinen 5:llä, tulosta "Buzz"
   - Jos luku on jaollinen molemmilla (3 JA 5), tulosta "FizzBuzz"
   - Muuten tulosta luku normaalisti

**Esimerkki:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
...
```

💡 **Vinkit:**
- Tarkista ENSIN jaollisuus molemmilla (15)
- Sitten jaollisuus 3:lla
- Sitten jaollisuus 5:llä
- Käytä modulo-operaattoria: `luku % 3 == 0`

📝 **Tiedosto:** [Harjoitus 6/](Harjoitus%206/) | [harjoitus6.py](Harjoitus%206/harjoitus6.py)

---

## Valmis?

Kun olet tehnyt harjoitukset, voit verrata vastauksiasi [Vastaukset](../Vastaukset/)-kansiossa oleviin mallivastauksiin.

💪 Muista: On täysin normaalia, että ratkaisusi näyttää erilaiselta kuin malliratkaisut. Tärkeintä on, että ohjelma toimii oikein!
