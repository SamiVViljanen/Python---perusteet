# Harjoitus 5: Hanoin tornit ⭐⭐⭐⭐

## Tehtävänanto

**Hanoin tornit** on klassinen rekursiivinen ongelma:

- On 3 pylvästä: A, B, C
- Pylväässä A on n kiekkoa (pienimmästä suurimpaan)
- **Tavoite:** Siirrä kaikki kiekot pylvääseen C
- **Säännöt:**
  - Siirrä yksi kiekko kerrallaan
  - Suurempi kiekko ei saa olla pienemmän päällä

**Rekursiivinen ratkaisu:**
1. Siirrä n-1 kiekkoa lähteestä apuun (käyttäen kohdetta apuna)
2. Siirrä suurin kiekko lähteestä kohteeseen
3. Siirrä n-1 kiekkoa avusta kohteeseen (käyttäen lähdettä apuna)

Tee ohjelma, joka:
1. Toteuttaa rekursiivisen funktion `hanoin_tornit(n, lahde, kohde, apu)`
2. Tulostaa jokaisen siirron
3. Ratkaisee ongelman 3 kiekolla

## Esimerkkitulostus

```
=== HANOIN TORNIT (3 kiekkoa) ===

Siirrä kiekko 1: A → C
Siirrä kiekko 2: A → B
Siirrä kiekko 1: C → B
Siirrä kiekko 3: A → C
Siirrä kiekko 1: B → A
Siirrä kiekko 2: B → C
Siirrä kiekko 1: A → C

Valmis! 7 siirtoa.
```

## Vinkit

```python
def hanoin_tornit(n, lahde="A", kohde="C", apu="B"):
    if n == 1:
        print(f"Siirrä kiekko 1: {lahde} → {kohde}")
        return 1
    
    # Siirrä n-1 kiekkoa lähteestä apuun
    siirrot = hanoin_tornit(n - 1, lahde, apu, kohde)
    
    # Siirrä suurin kiekko lähteestä kohteeseen
    print(f"Siirrä kiekko {n}: {lahde} → {kohde}")
    siirrot += 1
    
    # Siirrä n-1 kiekkoa avusta kohteeseen
    siirrot += hanoin_tornit(n - 1, apu, kohde, lahde)
    
    return siirrot
```

**Siirtojen määrä:** n kiekolle tarvitaan `2ⁿ - 1` siirtoa
- 3 kiekkoa → 7 siirtoa
- 4 kiekkoa → 15 siirtoa

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus5.py](harjoitus5.py)
