# Harjoitus 5: BMI-laskuri - RATKAISU

# 1. Kysy käyttäjältä paino (kg)
paino = float(input("Anna painosi (kg): "))

# 2. Kysy käyttäjältä pituus (cm)
pituus_cm = float(input("Anna pituutesi (cm): "))

# 3. Muunna pituus metreiksi
pituus_m = pituus_cm / 100

# 4. Laske BMI
bmi = paino / (pituus_m ** 2)

# 5. Tulosta BMI yhden desimaalin tarkkuudella
print(f"BMI-indeksisi on {bmi:.1f}")