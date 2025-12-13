# Harjoitus 4: Oma moduuli
# Tavoite: Luo oma moduuli ja käytä sitä

# 1. Tuo geometria-moduuli
import geometria

# 2. Kysy käyttäjältä säde
säde = float(input("Anna ympyrän säde: "))

# 3. Laske pinta-ala käyttäen geometria-moduulia
pinta_ala = geometria.ympyrän_pinta_ala(säde)

# 4. Laske piiri käyttäen geometria-moduulia
piiri = geometria.ympyrän_piiri(säde)

# 5. Tulosta tulokset
print(f"Pinta-ala: {pinta_ala:.2f}")
print(f"Piiri: {piiri:.2f}")
