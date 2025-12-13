# Harjoitukset: Ehtolauseet

Tee seuraavat harjoitukset järjestyksessä. Jokaista harjoitusta varten on oma alakansio.

---

## Harjoitus 1: Ikärajan tarkistus (⭐ Helppo)

**Tavoite:** Harjoittele yksinkertaista `if-else`-rakennetta.

**Tehtävä:**
1. Kysy käyttäjältä ikä
2. Jos ikä on 18 tai enemmän, tulosta "Olet täysi-ikäinen"
3. Muuten tulosta "Olet alaikäinen"

**Esimerkki 1:**
```
Anna ikäsi: 20
Olet täysi-ikäinen
```

**Esimerkki 2:**
```
Anna ikäsi: 15
Olet alaikäinen
```

💡 **Vinkki:** Käytä vertailuoperaattoria `>=`

📝 **Tiedosto:** [Harjoitus 1/](Harjoitus%201/) | [harjoitus1.md](Harjoitus%201/harjoitus1.md) | [harjoitus1.py](Harjoitus%201/harjoitus1.py)

---

## Harjoitus 2: Arvosanan määrittäminen (⭐⭐ Helppo)

**Tavoite:** Harjoittele `if-elif-else`-rakennetta.

**Tehtävä:**
1. Kysy käyttäjältä kokeen pistemäärä (0-100)
2. Määritä arvosana seuraavasti:
   - 90-100: Kiitettävä
   - 80-89: Hyvä
   - 70-79: Tyydyttävä
   - 60-69: Välttävä
   - 0-59: Hylätty
3. Tulosta arvosana

**Esimerkki:**
```
Anna kokeen pisteet (0-100): 85
Arvosana: Hyvä
```

💡 **Vinkki:** Käytä `elif` useille vaihtoehdoille. Aloita suurimmasta!

📝 **Tiedosto:** [Harjoitus 2/](Harjoitus%202/) | [harjoitus2.md](Harjoitus%202/harjoitus2.md) | [harjoitus2.py](Harjoitus%202/harjoitus2.py)

---

## Harjoitus 3: Parillinen vai pariton? (⭐⭐ Keskitaso)

**Tavoite:** Harjoittele modulo-operaattoria (`%`) ehtolauseissa.

**Tehtävä:**
1. Kysy käyttäjältä kokonaisluku
2. Tarkista onko luku parillinen vai pariton
3. Tulosta tulos

**Esimerkki 1:**
```
Anna luku: 8
Luku 8 on parillinen
```

**Esimerkki 2:**
```
Anna luku: 7
Luku 7 on pariton
```

💡 **Vinkit:**
- Parillinen luku: `luku % 2 == 0`
- Pariton luku: `luku % 2 == 1` tai `luku % 2 != 0`

📝 **Tiedosto:** [Harjoitus 3/](Harjoitus%203/) | [harjoitus3.md](Harjoitus%203/harjoitus3.md) | [harjoitus3.py](Harjoitus%203/harjoitus3.py)

---

## Harjoitus 4: Lämpötilan luokittelu (⭐⭐⭐ Keskitaso)

**Tavoite:** Harjoittele monipuolisia ehtolauseita ja tulosteen muotoilua.

**Tehtävä:**
1. Kysy käyttäjältä lämpötila Celsius-asteina
2. Luokittele lämpötila:
   - Yli 25°C: "Helteinen"
   - 15-25°C: "Lämmin"
   - 5-14°C: "Viileä"
   - -5 - 4°C: "Kylmä"
   - Alle -5°C: "Hyytävä"
3. Tulosta luokitus ja sopiva neuvo

**Esimerkki:**
```
Anna lämpötila (°C): 18
Lämmin - Hyvä sää kävelylle!
```

💡 **Vinkki:** Käytä `elif`-rakenteita ja aloita suurimmasta lämpötilasta.

📝 **Tiedosto:** [Harjoitus 4/](Harjoitus%204/) | [harjoitus4.md](Harjoitus%204/harjoitus4.md) | [harjoitus4.py](Harjoitus%204/harjoitus4.py)

---

## Harjoitus 5: Kirjautuminen (⭐⭐⭐⭐ Haaste)

**Tavoite:** Harjoittele loogisia operaattoreita (`and`) ja sisäkkäisiä ehtolauseita.

**Tehtävä:**
1. Määritä oikea käyttäjätunnus ja salasana muuttujiin
2. Kysy käyttäjältä käyttäjätunnus ja salasana
3. Tarkista molemmat:
   - Jos molemmat oikein: "Kirjautuminen onnistui!"
   - Jos vain toinen oikein: kerro kumpi on väärin
   - Jos molemmat väärin: "Sekä käyttäjätunnus että salasana ovat väärin"

**Esimerkki 1:**
```
Anna käyttäjätunnus: admin
Anna salasana: salasana123
Kirjautuminen onnistui!
```

**Esimerkki 2:**
```
Anna käyttäjätunnus: admin
Anna salasana: väärä
Salasana on väärin
```

**Esimerkki 3:**
```
Anna käyttäjätunnus: väärä
Anna salasana: väärä
Sekä käyttäjätunnus että salasana ovat väärin
```

💡 **Vinkit:**
- Käytä `and` operaattoria: `if tunnus == oikea_tunnus and salasana == oikea_salasana:`
- Voit myös käyttää sisäkkäisiä if-lauseita

📝 **Tiedosto:** [Harjoitus 5/](Harjoitus%205/) | [harjoitus5.md](Harjoitus%205/harjoitus5.md) | [harjoitus5.py](Harjoitus%205/harjoitus5.py)

---

## Valmis?

Kun olet tehnyt harjoitukset, voit verrata vastauksiasi [Vastaukset](../Vastaukset/)-kansiossa oleviin mallivastauksiin.

💪 Muista: On täysin normaalia, että ratkaisusi näyttää erilaiselta kuin malliratkaisut. Tärkeintä on, että ohjelma toimii oikein!
