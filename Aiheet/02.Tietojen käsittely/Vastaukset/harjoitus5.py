# Harjoitus 5: Tulosteen muotoilu f-stringillä - RATKAISU

# 1. Kysy käyttäjältä nimi, ikä ja paino
nimi = input("Anna nimesi: ")
ika = int(input("Anna ikäsi: "))
paino = float(input("Anna painosi (kg): "))

# 2. Tulosta lause
print(f"Nimi: {nimi}, Ikä: {ika} vuotta, Paino: {paino} kg")

# 3. Tulosta ikä kuukausina ja paino pyöristettynä
ika_kuukausina = ika * 12
print(f"Ikä kuukausina: {ika_kuukausina}")
print(f"Paino pyöristettynä: {paino:.2f} kg")
