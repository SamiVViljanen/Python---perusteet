# Harjoitus 1: Math-moduulin käyttö
# Tavoite: Harjoittele sisäänrakennetun math-moduulin käyttöä

# 1. Tuo math-moduuli
import math

# 2. Kysy käyttäjältä luku
luku = float(input("Anna luku: "))

# 3. Laske neliöjuuri
neliojuuri = math.sqrt(luku)

# 4. Laske neliö (math.pow)
nelio = math.pow(luku, 2)

# 5. Pyöristä ylös (math.ceil)
ylos = math.ceil(luku)

# 6. Pyöristä alas (math.floor)
alas = math.floor(luku)

# 7. Tulosta tulokset
print(f"Neliöjuuri: {neliojuuri:.3f}")
print(f"Neliö: {nelio}")
print(f"Pyöristys ylös: {ylos}")
print(f"Pyöristys alas: {alas}")
