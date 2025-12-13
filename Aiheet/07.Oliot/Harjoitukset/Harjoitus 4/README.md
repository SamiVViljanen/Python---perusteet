# Harjoitus 4: Luokka laskurilla (⭐⭐⭐ Keskitaso)

## Tavoite
Harjoittele muuttuvaa tilaa oliossa.

## Tehtävä
1. Luo luokka `Laskuri` joka `__init__`:ssä:
   - Alustaa `self.arvo = 0`
2. Luo metodi `kasvata()` joka:
   - Kasvattaa `self.arvo`-muuttujaa yhdellä
3. Luo metodi `vahenna()` joka:
   - Vähentää `self.arvo`-muuttujaa yhdellä
4. Luo metodi `näytä()` joka:
   - Tulostaa nykyisen arvon
5. Testaa: luo laskuri, kasvata 3 kertaa, vähennä kerran, näytä tulos

## Odotettu tuloste
```
Laskurin arvo: 2
```

## Vinkkejä
💡 Olio "muistaa" arvonsa kutsujen välillä!  
💡 `self.arvo += 1` kasvattaa arvoa  
💡 `self.arvo -= 1` vähentää arvoa  
💡 Ei tarvitse parametreja `kasvata()` ja `vahenna()` metodeissa

---

📝 **Tiedosto:** [harjoitus4.py](harjoitus4.py)
