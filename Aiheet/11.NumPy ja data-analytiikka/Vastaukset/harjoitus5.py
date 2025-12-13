import numpy as np

# Data
opiskeluaika_lista = [1, 2, 3, 4, 5, 6, 7, 8]
pisteet_lista = [45, 51, 55, 60, 65, 70, 78, 82]

# 1. Luo NumPy-taulukot
opiskeluaika = np.array(opiskeluaika_lista)
pisteet = np.array(pisteet_lista)

print(f"Opiskeluajat: {opiskeluaika}")
print(f"Pisteet: {pisteet}")
print()

# 2. Laske korrelaatiokerroin
korrelaatio = np.corrcoef(opiskeluaika, pisteet)[0, 1]
print(f"Korrelaatio: {korrelaatio:.2f}")

# 3. Laske regressiosuoran parametrit
k = np.cov(opiskeluaika, pisteet)[0, 1] / np.var(opiskeluaika)
b = np.mean(pisteet) - k * np.mean(opiskeluaika)
print(f"Regressiosuora: y = {k:.2f}x + {b:.2f}")
print()

# 4. Ennusta 10 tunnin opiskelulle
ennuste_10h = k * 10 + b
print(f"Ennuste 10 tunnille: {ennuste_10h:.1f} pistettä")
print()

# 5. Tulosta vertailu
print("Vertailu (tunnit → todellinen / ennuste):")
for i in range(len(opiskeluaika)):
    todellinen = pisteet[i]
    ennuste = k * opiskeluaika[i] + b
    print(f"{opiskeluaika[i]}h → {todellinen} / {ennuste:.1f}")
