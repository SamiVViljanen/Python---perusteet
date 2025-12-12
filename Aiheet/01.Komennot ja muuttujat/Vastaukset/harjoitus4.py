# Harjoitus 4: Sekuntien muunnos - RATKAISU

# 1. Kysy käyttäjältä sekuntien määrä
sekunnit = int(input("Anna sekuntien määrä: "))

# 2. Laske tunnit
tunnit = sekunnit // 3600

# 3. Laske minuutit (jäljelle jäävistä sekunneista)
jaannos_sekunneista = sekunnit % 3600  # Sekunnit tunnit vähennettynä
minuutit = jaannos_sekunneista // 60

# 4. Laske sekunnit (loppu)
loppu_sekunnit = jaannos_sekunneista % 60

# 5. Tulosta tulos muodossa: "X tuntia, Y minuuttia ja Z sekuntia"
print(f"{sekunnit} sekuntia on {tunnit} tuntia, {minuutit} minuuttia ja {loppu_sekunnit} sekuntia")
