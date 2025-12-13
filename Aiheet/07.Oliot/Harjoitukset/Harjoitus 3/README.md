# Harjoitus 3: Metodi joka käyttää attribuutteja (⭐⭐ Keskitaso)

## Tavoite
Harjoittele metodeja jotka käyttävät olion attribuutteja.

## Tehtävä
1. Luo luokka `Suorakulmio` joka ottaa `__init__`:ssä:
   - `leveys` (luku)
   - `korkeus` (luku)
2. Luo metodi `laske_pinta_ala()` joka:
   - Palauttaa pinta-alan: `self.leveys * self.korkeus`
3. Luo metodi `laske_piiri()` joka:
   - Palauttaa piirin: `2 * (self.leveys + self.korkeus)`
4. Luo suorakulmio-olio (esim. 5 x 10) ja tulosta pinta-ala ja piiri

## Odotettu tuloste
```
Pinta-ala: 50
Piiri: 30
```

## Vinkkejä
💡 Metodit voivat käyttää `self.leveys` ja `self.korkeus` attribuutteja!  
💡 Muista `return` palauttaaksesi arvon  
💡 Tallenna metodin tulos muuttujaan ennen tulostusta

---

📝 **Tiedosto:** [harjoitus3.py](harjoitus3.py)
