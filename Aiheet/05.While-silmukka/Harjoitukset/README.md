# Harjoitukset: While-silmukka

Tee seuraavat harjoitukset järjestyksessä. Jokaista harjoitusta varten on oma alakansio.

---

## Harjoitus 1: Laskuri 1-5 (⭐ Helppo)

**Tavoite:** Harjoittele yksinkertaista while-silmukkaa laskurilla.

**Tehtävä:**
1. Luo muuttuja `i = 1`
2. Käytä while-silmukkaa tulostamaan luvut 1-5
3. Muista kasvattaa `i`-muuttujaa joka kierroksella!

**Esimerkki:**
```
1
2
3
4
5
```

💡 **Vinkki:** Muista ehto `while i <= 5:` ja kasvata `i += 1`

📝 **Tiedosto:** [Harjoitus 1/](Harjoitus%201/) | [harjoitus1.py](Harjoitus%201/harjoitus1.py)

---

## Harjoitus 2: Salasanan tarkistus (⭐⭐ Helppo)

**Tavoite:** Harjoittele while-silmukkaa käyttäjän syötteen kanssa.

**Tehtävä:**
1. Määritä oikea salasana muuttujaan: `oikea_salasana = "python123"`
2. Kysy käyttäjältä salasanaa niin kauan kunnes se on oikein
3. Kun salasana on oikein, tulosta "Kirjautuminen onnistui!" ja lopeta silmukka

**Esimerkki:**
```
Anna salasana: väärä
Anna salasana: vieläkin väärä
Anna salasana: python123
Kirjautuminen onnistui!
```

💡 **Vinkki:** `while salasana != oikea_salasana:`

📝 **Tiedosto:** [Harjoitus 2/](Harjoitus%202/) | [harjoitus2.py](Harjoitus%202/harjoitus2.py)

---

## Harjoitus 3: Valikko break-komennolla (⭐⭐ Keskitaso)

**Tavoite:** Harjoittele `while True` ja `break`-komentoa.

**Tehtävä:**
1. Luo ikuinen silmukka `while True:`
2. Näytä valikko:
   ```
   1. Sano hei
   2. Sano moi
   0. Lopeta
   ```
3. Jos käyttäjä valitsee 1, tulosta "Hei!"
4. Jos käyttäjä valitsee 2, tulosta "Moi!"
5. Jos käyttäjä valitsee 0, tulosta "Näkemiin!" ja lopeta `break`

**Esimerkki:**
```
1. Sano hei
2. Sano moi
0. Lopeta
Valintasi: 1
Hei!

1. Sano hei
2. Sano moi
0. Lopeta
Valintasi: 2
Moi!

1. Sano hei
2. Sano moi
0. Lopeta
Valintasi: 0
Näkemiin!
```

💡 **Vinkki:** Käytä `break` lopettaaksesi silmukan

📝 **Tiedosto:** [Harjoitus 3/](Harjoitus%203/) | [harjoitus3.py](Harjoitus%203/harjoitus3.py)

---

## Harjoitus 4: Arvauspeli (⭐⭐⭐ Keskitaso)

**Tavoite:** Yhdistä while-silmukka, ehtolauseet ja laskuri.

**Tehtävä:**
1. Määritä oikea luku muuttujaan: `oikea_luku = 7`
2. Luo laskuri arvausten määrälle
3. Kysy käyttäjältä arvausta niin kauan kunnes se on oikein
4. Anna vihjeitä: "Liian pieni!" tai "Liian suuri!"
5. Kun oikein, kerro montako arvausta kului

**Esimerkki:**
```
Arvaa luku (1-10): 5
Liian pieni!
Arvaa luku (1-10): 9
Liian suuri!
Arvaa luku (1-10): 7
Oikein! Käytit 3 arvausta.
```

💡 **Vinkit:**
- Laskuri: `yritykset = 0` ja `yritykset += 1`
- Ehto: `while arvaus != oikea_luku:`

📝 **Tiedosto:** [Harjoitus 4/](Harjoitus%204/) | [harjoitus4.py](Harjoitus%204/harjoitus4.py)

---

## Harjoitus 5: Positiivisten lukujen summa (⭐⭐⭐⭐ Haaste)

**Tavoite:** Harjoittele while-silmukkaa ja gatherer-roolia.

**Tehtävä:**
1. Kysy käyttäjältä lukuja yksi kerrallaan
2. Laske positiivisten lukujen summa
3. Jos käyttäjä syöttää 0 tai negatiivisen luvun, lopeta kysely
4. Tulosta summa ja montako positiivista lukua syötettiin

**Esimerkki:**
```
Anna luku: 5
Anna luku: 10
Anna luku: 3
Anna luku: 7
Anna luku: 0
Syötit 4 positiivista lukua.
Summa: 25
```

💡 **Vinkit:**
- Kaksi laskuria: `summa` ja `maara`
- Ehto: `while luku > 0:` TAI `while True:` + `if luku <= 0: break`
- Muista kysyä ensimmäinen luku ennen silmukkaa!

📝 **Tiedosto:** [Harjoitus 5/](Harjoitus%205/) | [harjoitus5.py](Harjoitus%205/harjoitus5.py)

---

## Valmis?

Kun olet tehnyt harjoitukset, voit verrata vastauksiasi [Vastaukset](../Vastaukset/)-kansiossa oleviin mallivastauksiin.

💪 Muista: On täysin normaalia, että ratkaisusi näyttää erilaiselta kuin malliratkaisut. Tärkeintä on, että ohjelma toimii oikein!
