# Harjoitukset: Komennot ja muuttujat

Tee seuraavat harjoitukset järjestyksessä.

---

## Harjoitus 1: Tervehdys (⭐ Helppo)

**Tavoite:** Harjoittele `input()`- ja `print()`-funktioiden käyttöä.

**Tehtävä:**
1. Kysy käyttäjältä hänen nimensä
2. Kysy käyttäjältä hänen ikänsä
3. Tulosta tervehdys muodossa: "Hei [nimi]! Olet [ikä] vuotta vanha."

**Esimerkki:**
```
Anna nimesi: Matti
Anna ikäsi: 25
Hei Matti! Olet 25 vuotta vanha.
```

📝 **Tiedosto:** [Harjoitus 1/](Harjoitus%201/) | [harjoitus1.py](Harjoitus%201/harjoitus1.py)

---

## Harjoitus 2: Lämpötilan muunnos (⭐⭐ Helppo)

**Tavoite:** Harjoittele tyypin muunnoksia ja aritmeettisia operaatioita.

**Tehtävä:**
1. Kysy käyttäjältä lämpötila Celsius-asteina
2. Muunna lämpötila Fahrenheit-asteiksi kaavalla: `F = C * 9/5 + 32`
3. Tulosta tulos yhden desimaalin tarkkuudella

**Esimerkki:**
```
Anna lämpötila Celsius-asteina: 25
25.0°C on 77.0°F
```

💡 **Vinkki:** Käytä `float()` ja f-stringiä muotoiluun: `f"{luku:.1f}"`

📝 **Tiedosto:** [Harjoitus 2/](Harjoitus%202/) | [harjoitus2.py](Harjoitus%202/harjoitus2.py)

---

## Harjoitus 3: Ostoslaskuri (⭐⭐ Keskitaso)

**Tavoite:** Harjoittele useamman muuttujan käsittelyä ja laskutoimituksia.

**Tehtävä:**
1. Kysy käyttäjältä kolmen tuotteen hinnat
2. Laske yhteishinta
3. Laske ja näytä 24% ALV erikseen
4. Näytä loppusumma (hinta + ALV)

**Esimerkki:**
```
Anna tuotteen 1 hinta: 10.50
Anna tuotteen 2 hinta: 5.00
Anna tuotteen 3 hinta: 12.30
Yhteishinta (ilman ALV): 27.80€
ALV (24%): 6.67€
Loppusumma: 34.47€
```

💡 **Vinkki:** ALV lasketaan: `yhteishinta * 0.24`

📝 **Tiedosto:** [Harjoitus 3/](Harjoitus%203/) | [harjoitus3.py](Harjoitus%203/harjoitus3.py)

---

## Harjoitus 4: Sekuntien muunnos (⭐⭐⭐ Keskitaso)

**Tavoite:** Harjoittele kokonaisjakolaskua (`//`) ja jakojäännöstä (`%`).

**Tehtävä:**
1. Kysy käyttäjältä sekuntien määrä
2. Muunna sekunnit muotoon: tunnit, minuutit ja sekunnit
3. Tulosta tulos muodossa: "X tuntia, Y minuuttia ja Z sekuntia"

**Esimerkki:**
```
Anna sekuntien määrä: 3665
3665 sekuntia on 1 tuntia, 1 minuuttia ja 5 sekuntia
```

💡 **Vinkit:**
- 1 tunti = 3600 sekuntia
- 1 minuutti = 60 sekuntia
- Käytä `//` ja `%` operaattoreita

📝 **Tiedosto:** [Harjoitus 4/](Harjoitus%204/) | [harjoitus4.py](Harjoitus%204/harjoitus4.py)

---

## Harjoitus 5: BMI-laskuri (⭐⭐⭐ Keskitaso)

**Tavoite:** Yhdistä kaikki opitut taidot: input, tyypin muunnokset, aritmetiikka ja tulostus.

**Tehtävä:**
1. Kysy käyttäjältä paino (kg) ja pituus (cm)
2. Muunna pituus metreiksi
3. Laske BMI kaavalla: `BMI = paino / (pituus_metreissä ** 2)`
4. Tulosta BMI yhden desimaalin tarkkuudella

**Esimerkki:**
```
Anna painosi (kg): 75
Anna pituutesi (cm): 175
BMI-indeksisi on 24.5
```

💡 **Vinkit:**
- Pituus metreiksi: `pituus_cm / 100`
- Käytä `**` potenssilaskuun
- Muotoile tulos: `f"{bmi:.1f}"`

📝 **Tiedosto:** [Harjoitus 5/](Harjoitus%205/) | [harjoitus5.py](Harjoitus%205/harjoitus5.py)

---

## Valmis?

Kun olet tehnyt harjoitukset, voit verrata vastauksiasi [Vastaukset](../Vastaukset/)-kansiossa oleviin mallivastauksiin.

💪 Muista: On täysin normaalia, että ratkaisusi näyttää erilaiselta kuin malliratkaisut. Tärkeintä on, että ohjelma toimii oikein!
