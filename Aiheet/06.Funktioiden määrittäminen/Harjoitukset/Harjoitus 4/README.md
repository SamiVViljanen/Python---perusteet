# Harjoitus 4: Funktio usealla parametrilla (⭐⭐⭐ Keskitaso)

## Tavoite
Harjoittele useita parametreja ja return-arvoa.

## Tehtävä
1. Määritä funktio `laske_summa(a, b, c)` joka ottaa kolme lukua
2. Funktio palauttaa lukujen summan
3. Määritä toinen funktio `laske_keskiarvo(a, b, c)` joka:
   - Kutsuu `laske_summa()`-funktiota
   - Palauttaa keskiarvon (summa / 3)
4. Testaa molempia funktioita luvuilla 10, 20, 30

## Odotettu tuloste
```
Summa: 60
Keskiarvo: 20.0
```

## Vinkkejä
💡 Funktio voi kutsua toista funktiota!  
💡 `keskiarvo = laske_summa(a, b, c) / 3`  
💡 Käytä f-stringiä tulostuksessa

---

📝 **Tiedosto:** [harjoitus4.py](harjoitus4.py)
