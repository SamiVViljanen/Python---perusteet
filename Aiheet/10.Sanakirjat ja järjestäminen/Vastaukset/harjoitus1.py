# Harjoitus 1: Perus sanakirja

# Luo sanakirja 5 henkilöllä
henkilöt = {
    "Anna": 25,
    "Pekka": 30,
    "Liisa": 28,
    "Matti": 35,
    "Kaisa": 22
}

# Tulosta koko sanakirja
print("Kaikki henkilöt:")
print(henkilöt)

# Hae yhden henkilön ikä
print(f"\nAnnan ikä: {henkilöt['Anna']}")

# Lisää uusi henkilö
print("\nLisätään uusi henkilö...")
henkilöt["Ville"] = 27

# Tulosta päivitetty sanakirja
print("\nPäivitetyt henkilöt:")
print(henkilöt)
