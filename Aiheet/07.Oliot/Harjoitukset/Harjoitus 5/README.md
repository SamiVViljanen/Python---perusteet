# Harjoitus 5: Pankkitili-luokka (⭐⭐⭐⭐ Haaste)

## Tavoite
Yhdistä kaikki oppimasi ja luo käytännöllinen luokka.

## Tehtävä
1. Luo luokka `Pankkitili` joka `__init__`:ssä ottaa:
   - `omistaja` (merkkijono)
   - `saldo` (luku, oletusarvo 0)
2. Luo metodi `talleta(summa)` joka:
   - Lisää summan saldoon
   - Tulostaa: "Talletettiin [summa]€. Uusi saldo: [saldo]€"
3. Luo metodi `nosta(summa)` joka:
   - Tarkistaa onko saldoa tarpeeksi
   - Jos on: vähentää summan ja tulostaa uuden saldon
   - Jos ei: tulostaa "Ei tarpeeksi rahaa!"
4. Luo metodi `näytä_saldo()` joka tulostaa saldon

**Testaa:**
- Luo tili
- Talleta 100€
- Talleta 50€
- Nosta 30€
- Yritä nostaa 200€ (pitäisi epäonnistua)
- Näytä saldo

## Odotettu tuloste
```
Talletettiin 100€. Uusi saldo: 100€
Talletettiin 50€. Uusi saldo: 150€
Nostettiin 30€. Uusi saldo: 120€
Ei tarpeeksi rahaa!
Tilin saldo: 120€
```

## Vinkkejä
💡 `if self.saldo >= summa:` tarkistaa saldon riittävyyden  
💡 Muista `self.saldo += summa` ja `self.saldo -= summa`  
💡 Oletusarvo: `def __init__(self, omistaja, saldo=0):`

---

📝 **Tiedosto:** [harjoitus5.py](harjoitus5.py)
