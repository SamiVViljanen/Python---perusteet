# Harjoitus 5: Main-funktio ja ohjelmarakenne (⭐⭐⭐⭐ Haaste)

## Tavoite
Harjoittele main()-funktion käyttöä ja ohjelmarakennetta.

## Tehtävä
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

## Odotettu toiminta
```
Anna lämpötila Celsiuksina: 25
25.0°C on 77.0°F

Anna lämpötila Fahrenheitina: 68
68.0°F on 20.0°C
```

## Vinkkejä
💡 Tee yksi funktio kerrallaan ja testaa!  
💡 main()-funktiossa kutsut molempia muuntofunktioita  
💡 Muista `if __name__ == "__main__":` -rakenne  
💡 Kaavat: F = C × 9/5 + 32 ja C = (F - 32) × 5/9

---

📝 **Tiedosto:** [harjoitus5.py](harjoitus5.py)
