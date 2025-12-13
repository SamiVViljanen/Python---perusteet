# Harjoitus 1: Ikärajan tarkistus - RATKAISU

# 1. Kysy käyttäjältä ikä
ika = int(input("Anna ikäsi: "))

# 2-3. Jos ikä on 18 tai enemmän, tulosta "Olet täysi-ikäinen", muuten "Olet alaikäinen"
if ika >= 18:
    print("Olet täysi-ikäinen")
else:
    print("Olet alaikäinen")
