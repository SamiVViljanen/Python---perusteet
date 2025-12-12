# Harjoitus 2: Lämpötilan muunnos - RATKAISU

# 1. Kysy käyttäjältä lämpötila Celsius-asteina
celsius = float(input("Anna lämpötila Celsius-asteina: "))

# 2. Muunna lämpötila Fahrenheit-asteiksi
fahrenheit = celsius * 9/5 + 32

# 3. Tulosta tulos yhden desimaalin tarkkuudella
print(f"{celsius:.1f}°C on {fahrenheit:.1f}°F")
