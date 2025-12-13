# Harjoitus 5: Kirjautuminen (⭐⭐⭐⭐ Haaste)

## Tavoite
Harjoittele loogisia operaattoreita (`and`) ja sisäkkäisiä ehtolauseita.

## Tehtävä
1. Määritä oikea käyttäjätunnus ja salasana muuttujiin
2. Kysy käyttäjältä käyttäjätunnus ja salasana
3. Tarkista molemmat:
   - Jos molemmat oikein: "Kirjautuminen onnistui!"
   - Jos vain toinen oikein: kerro kumpi on väärin
   - Jos molemmat väärin: "Sekä käyttäjätunnus että salasana ovat väärin"

## Esimerkki 1:
```
Anna käyttäjätunnus: admin
Anna salasana: salasana123
Kirjautuminen onnistui!
```

## Esimerkki 2:
```
Anna käyttäjätunnus: admin
Anna salasana: väärä
Salasana on väärin
```

## Esimerkki 3:
```
Anna käyttäjätunnus: väärä
Anna salasana: väärä
Sekä käyttäjätunnus että salasana ovat väärin
```

💡 **Vinkit:**
- Käytä `and` operaattoria: `if tunnus == oikea_tunnus and salasana == oikea_salasana:`
- Voit myös käyttää sisäkkäisiä if-lauseita

📝 **Tiedosto:** `harjoitus5.py`
