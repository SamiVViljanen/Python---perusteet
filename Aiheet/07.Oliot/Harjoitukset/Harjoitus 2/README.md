# Harjoitus 2: Dataclass (⭐⭐ Helppo)

## Tavoite
Harjoittele `@dataclass`-dekoraattorin käyttöä.

## Tehtävä
1. Tuo `dataclass` kirjastosta: `from dataclasses import dataclass`
2. Luo dataclass `Opiskelija` jolla on attribuutit:
   - `nimi: str`
   - `ikä: int`
   - `opiskelijanumero: str`
3. Luo 2-3 opiskelijaoliota
4. Tulosta oliot (dataclass tekee automaattisesti siistin tulostuksen!)

## Odotettu tuloste
```
Opiskelija(nimi='Anna', ikä=22, opiskelijanumero='12345')
Opiskelija(nimi='Matti', ikä=24, opiskelijanumero='67890')
```

## Vinkkejä
💡 Dataclass tekee `__init__`:n automaattisesti, ei tarvitse kirjoittaa!  
💡 Muista tyyppimerkinnät: `nimi: str`, `ikä: int`  
💡 `@dataclass` tulee luokan ylle

---

📝 **Tiedosto:** [harjoitus2.py](harjoitus2.py)
