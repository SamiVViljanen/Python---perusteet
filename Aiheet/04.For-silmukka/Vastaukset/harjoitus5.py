# Harjoitus 5: Kertotaulu - RATKAISU

# 1. Kysy käyttäjältä luku
luku = int(input("Minkä luvun kertotaulu? "))

# 2. Tulosta kertotaulu 1-10
for i in range(1, 11):
    tulos = luku * i
    print(f"{luku} x {i} = {tulos}")
