# Harjoitukset: Funktioiden määrittäminen

Tee seuraavat harjoitukset järjestyksessä. Jokaista harjoitusta varten on oma alakansio.

---

## Harjoitus 1: Ensimmäinen funktio (⭐ Helppo)

**Tavoite:** Harjoittele funktion määrittämistä ja kutsumista.

**Tehtävä:**
1. Määritä funktio nimeltä `tervehdi()` joka ei ota parametreja
2. Funktio tulostaa: "Hei! Tervetuloa Python-ohjelmoinnin maailmaan!"
3. Kutsu funktiota 3 kertaa

**Esimerkki:**
```
Hei! Tervetuloa Python-ohjelmoinnin maailmaan!
Hei! Tervetuloa Python-ohjelmoinnin maailmaan!
Hei! Tervetuloa Python-ohjelmoinnin maailmaan!
```

💡 **Vinkki:** Funktion rakenne on `def funktio_nimi():`

📝 **Tiedosto:** [Harjoitus 1/](Harjoitus%201/) | [harjoitus1.py](Harjoitus%201/harjoitus1.py)

---

## Harjoitus 2: Funktio yhdellä parametrilla (⭐⭐ Helppo)

**Tavoite:** Harjoittele funktion parametreja.

**Tehtävä:**
1. Määritä funktio `tervehdi_nimella(nimi)` joka ottaa yhden parametrin
2. Funktio tulostaa: "Hei, [nimi]! Kiva nähdä."
3. Kutsu funktiota kolmella eri nimellä (esim. "Anna", "Matti", "Liisa")

**Esimerkki:**
```
Hei, Anna! Kiva nähdä.
Hei, Matti! Kiva nähdä.
Hei, Liisa! Kiva nähdä.
```

💡 **Vinkki:** Parametri otetaan vastaan suluissa: `def funktio(parametri):`

📝 **Tiedosto:** [Harjoitus 2/](Harjoitus%202/) | [harjoitus2.py](Harjoitus%202/harjoitus2.py)

---

## Harjoitus 3: Funktio return-arvolla (⭐⭐ Keskitaso)

**Tavoite:** Harjoittele return-avainsanaa ja palautusarvoja.

**Tehtävä:**
1. Määritä funktio `nelio(luku)` joka ottaa yhden luvun parametrina
2. Funktio **palauttaa** luvun neliön (luku * luku)
3. Kutsu funktiota luvuilla 3, 5 ja 10
4. Tulosta jokainen tulos

**Esimerkki:**
```
9
25
100
```

💡 **Vinkki:** Käytä `return` palauttaaksesi arvon: `return luku * luku`

📝 **Tiedosto:** [Harjoitus 3/](Harjoitus%203/) | [harjoitus3.py](Harjoitus%203/harjoitus3.py)

---

## Harjoitus 4: Funktio usealla parametrilla (⭐⭐⭐ Keskitaso)

**Tavoite:** Harjoittele useita parametreja ja return-arvoa.

**Tehtävä:**
1. Määritä funktio `laske_summa(a, b, c)` joka ottaa kolme lukua
2. Funktio palauttaa lukujen summan
3. Määritä toinen funktio `laske_keskiarvo(a, b, c)` joka:
   - Kutsuu `laske_summa()`-funktiota
   - Palauttaa keskiarvon (summa / 3)
4. Testaa molempia funktioita luvuilla 10, 20, 30

**Esimerkki:**
```
Summa: 60
Keskiarvo: 20.0
```

💡 **Vinkit:**
- Funktio voi kutsua toista funktiota!
- `keskiarvo = laske_summa(a, b, c) / 3`

📝 **Tiedosto:** [Harjoitus 4/](Harjoitus%204/) | [harjoitus4.py](Harjoitus%204/harjoitus4.py)

---

## Harjoitus 5: Main-funktio ja ohjelmarakenne (⭐⭐⭐⭐ Haaste)

**Tavoite:** Harjoittele main()-funktion käyttöä ja ohjelmarakennetta.

**Tehtävä:**
1. Määritä funktio `celsius_fahrenheit(celsius)` joka:
   - Ottaa lämpötilan Celsius-asteina
   - Palauttaa lämpötilan Fahrenheit-asteina
   - Kaava: `fahrenheit = celsius * 9/5 + 32`

2. Määritä funktio `fahrenheit_celsius(fahrenheit)` joka:
   - Ottaa lämpötilan Fahrenheit-asteina
   - Palauttaa lämpötilan Celsius-asteina
   - Kaava: `celsius = (fahrenheit - 32) * 5/9`

3. Määritä `main()`-funktio joka:
   - Kysyy käyttäjältä lämpötilan Celsius-asteina
   - Muuntaa sen Fahrenheitiksi ja tulostaa tuloksen
   - Kysyy käyttäjältä lämpötilan Fahrenheit-asteina
   - Muuntaa sen Celsiuksiksi ja tulostaa tuloksen

4. Kutsu main-funktiota rivillä `if __name__ == "__main__":`

**Esimerkki:**
```
Anna lämpötila Celsiuksina: 25
25.0°C on 77.0°F

Anna lämpötila Fahrenheitina: 68
68.0°F on 20.0°C
```

💡 **Vinkit:**
- Tee yksi funktio kerrallaan ja testaa!
- main()-funktiossa kutsut molempia muuntofunktioita
- Muista `if __name__ == "__main__":` -rakenne

📝 **Tiedosto:** [Harjoitus 5/](Harjoitus%205/) | [harjoitus5.py](Harjoitus%205/harjoitus5.py)

---

## Valmis?

Kun olet tehnyt harjoitukset, voit verrata vastauksiasi [Vastaukset](../Vastaukset/)-kansiossa oleviin mallivastauksiin.

💪 Muista: On täysin normaalia, että ratkaisusi näyttää erilaiselta kuin malliratkaisut. Tärkeintä on, että ohjelma toimii oikein!
