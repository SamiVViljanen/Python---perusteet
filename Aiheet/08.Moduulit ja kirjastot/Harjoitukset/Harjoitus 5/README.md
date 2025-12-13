# Harjoitus 5: Eri import-muodot (⭐⭐⭐⭐ Haaste)

## Tavoite
Ymmärrä eri tapoja tuoda moduuleja.

## Tehtävä
Luo ohjelma joka käyttää kaikkia import-muotoja:

1. **Muoto 1:** `import math`
   - Laske neliöjuuri luvusta 16

2. **Muoto 2:** `from random import randint, choice`
   - Luo satunnainen luku 1-100
   - Valitse satunnainen väri listasta `["punainen", "sininen", "vihreä"]`

3. **Muoto 3:** `import datetime as dt`
   - Tulosta nykyinen päivämäärä

4. Tulosta kaikki tulokset selkeästi

## Odotettu tuloste
```
Neliöjuuri 16:sta: 4.0
Satunnainen luku: 42
Satunnainen väri: sininen
Tänään: 2025-12-13
```

## Vinkkejä
💡 Kaikki importit tulevat tiedoston alkuun  
💡 Käytä oikeaa syntaksia jokaiselle muodolle  
💡 `choice()` vaatii listan parametrina  
💡 `dt.date.today()` koska käytit `as dt`

---

📝 **Tiedosto:** [harjoitus5.py](harjoitus5.py)
