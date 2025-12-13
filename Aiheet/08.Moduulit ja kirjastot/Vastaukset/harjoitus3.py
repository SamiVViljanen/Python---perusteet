# Harjoitus 3: Datetime ja ikälaskuri
# Tavoite: Harjoittele datetime-moduulin käyttöä

# 1. Tuo datetime-moduuli
import datetime

# 2. Kysy käyttäjältä syntymävuosi
syntymävuosi = int(input("Anna syntymävuosi: "))

# 3. Hae nykyinen vuosi
nykyinen_vuosi = datetime.date.today().year

# 4. Laske ikä
ikä = nykyinen_vuosi - syntymävuosi

# 5. Tulosta ikä
print(f"Olet {ikä}-vuotias.")

# 6. Hae ja tulosta nykyinen päivämäärä ja kellonaika
nyt = datetime.datetime.now()
print(f"Tänään on: {nyt}")
