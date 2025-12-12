# Harjoitus 3: Ostoslaskuri - RATKAISU

# 1. Kysy käyttäjältä kolmen tuotteen hinnat
tuote1 = float(input("Anna tuotteen 1 hinta: "))
tuote2 = float(input("Anna tuotteen 2 hinta: "))
tuote3 = float(input("Anna tuotteen 3 hinta: "))

# 2. Laske yhteishinta (gatherer)
yhteishinta = tuote1 + tuote2 + tuote3

# 3. Laske 24% ALV (transformation)
alv = yhteishinta * 0.24

# 4. Laske loppusumma (hinta + ALV)
loppusumma = yhteishinta + alv

# 5. Tulosta tulokset
print(f"Yhteishinta (ilman ALV): {yhteishinta:.2f}€")
print(f"ALV (24%): {alv:.2f}€")
print(f"Loppusumma: {loppusumma:.2f}€")
