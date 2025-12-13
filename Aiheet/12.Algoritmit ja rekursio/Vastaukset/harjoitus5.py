# Harjoitus 5: Hanoin tornit

# 1-2. Toteuta rekursiivinen Hanoin tornit -ratkaisu
def hanoin_tornit(n, lahde="A", kohde="C", apu="B"):
    """
    Ratkaisee Hanoin tornit -ongelman rekursiivisesti.
    Palauttaa siirtojen määrän.
    """
    if n == 1:
        print(f"Siirrä kiekko 1: {lahde} → {kohde}")
        return 1
    
    # Siirrä n-1 kiekkoa lähteestä apuun (käyttäen kohdetta apuna)
    siirrot = hanoin_tornit(n - 1, lahde, apu, kohde)
    
    # Siirrä suurin kiekko lähteestä kohteeseen
    print(f"Siirrä kiekko {n}: {lahde} → {kohde}")
    siirrot += 1
    
    # Siirrä n-1 kiekkoa avusta kohteeseen (käyttäen lähdettä apuna)
    siirrot += hanoin_tornit(n - 1, apu, kohde, lahde)
    
    return siirrot

# 3. Ratkaise 3 kiekolle
print("=== HANOIN TORNIT (3 kiekkoa) ===\n")
siirtoja = hanoin_tornit(3)
print(f"\nValmis! {siirtoja} siirtoa.")
