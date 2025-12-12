# Harjoitus 2: Tyypin muunnokset - RATKAISU

# 1. Kysy käyttäjältä ikä ja tallenna merkkijonona
ika_str = input("Anna ikäsi: ")

# 2. Muunna ikä kokonaisluvuksi ja tulosta ikä kuukausina
ika = int(ika_str)
kuukaudet = ika * 12
print(f"Olet {kuukaudet} kuukautta vanha!")

# 3. Kysy käyttäjältä tuotteen hinta merkkijonona
hinta_str = input("Anna tuotteen hinta: ")

# 4. Muunna liukuluvuksi ja kerro 2
hinta = float(hinta_str)
kahden_hinta = hinta * 2

# 5. Tulosta tulokset
print(f"Kahden tuotteen hinta: {kahden_hinta}€")
