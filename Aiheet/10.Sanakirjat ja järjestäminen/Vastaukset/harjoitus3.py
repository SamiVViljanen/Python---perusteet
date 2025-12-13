# Harjoitus 3: Tuplat ja järjestäminen

# Luo lista tuplista
henkilöt = [
    ("Anna", 25),
    ("Pekka", 30),
    ("Liisa", 22),
    ("Matti", 35),
    ("Kaisa", 28)
]

# Tulosta alkuperäinen lista
print("Alkuperäinen lista:")
print(henkilöt)

# Järjestä iän mukaan (nuorin ensin)
iän_mukaan = sorted(henkilöt, key=lambda x: x[1])
print("\nJärjestetty iän mukaan (nuorin ensin):")
print(iän_mukaan)

# Järjestä nimen mukaan
nimen_mukaan = sorted(henkilöt)  # tai sorted(henkilöt, key=lambda x: x[0])
print("\nJärjestetty nimen mukaan:")
print(nimen_mukaan)
