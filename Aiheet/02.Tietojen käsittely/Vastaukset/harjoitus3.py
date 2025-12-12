# Harjoitus 3: Lukujen pyöristäminen - RATKAISU

import math

# 1. Kysy käyttäjältä tuotteen hinta
hinta = float(input("Anna tuotteen hinta: "))

# 2. Pyöristä hinta lähimpään kokonaislukuun
pyoristetty = round(hinta)
print(f"Pyöristetty: {pyoristetty}")

# 3. Pyöristä hinta ylöspäin ja alaspäin
ylos = math.ceil(hinta)
alas = math.floor(hinta)
print(f"Ylös: {ylos}")
print(f"Alas: {alas}")

# 4. Pyöristä hinta kahden desimaalin tarkkuudella
kahden_desimaalin = round(hinta, 2)
print(f"Kahden desimaalin tarkkuudella: {kahden_desimaalin}")
