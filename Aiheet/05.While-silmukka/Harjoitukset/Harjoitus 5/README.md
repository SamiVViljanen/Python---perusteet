# Harjoitus 5: Positiivisten lukujen summa (⭐⭐⭐⭐ Haaste)

## Tavoite
Harjoittele while-silmukkaa ja gatherer-roolia.

## Tehtävä
1. Kysy käyttäjältä lukuja yksi kerrallaan
2. Laske positiivisten lukujen summa
3. Jos käyttäjä syöttää 0 tai negatiivisen luvun, lopeta kysely
4. Tulosta summa ja montako positiivista lukua syötettiin

## Odotettu toiminta
```
Anna luku: 5
Anna luku: 10
Anna luku: 3
Anna luku: 7
Anna luku: 0
Syötit 4 positiivista lukua.
Summa: 25
```

## Vinkkejä
💡 Kaksi laskuria: `summa = 0` ja `maara = 0`  
💡 Ehto: `while luku > 0:` TAI `while True:` + `if luku <= 0: break`  
💡 Muista kysyä ensimmäinen luku ENNEN silmukkaa!  
💡 Gatherer-rooli: `summa += luku` ja `maara += 1`

---

📝 **Tiedosto:** [harjoitus5.py](harjoitus5.py)
