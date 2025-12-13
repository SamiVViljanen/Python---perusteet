import numpy as np

# 1. Luo taulukko
taulukko = np.array([10, 20, 30, 40, 50])

# 2. Tulosta taulukko
print(f"Alkuperäinen taulukko: {taulukko}")

# 3. Tulosta ensimmäinen ja viimeinen
print(f"Ensimmäinen: {taulukko[0]}")
print(f"Viimeinen: {taulukko[-1]}")

# 4. Kerro kahdella
kerrottu = taulukko * 2
print(f"Kerrottuna kahdella: {kerrottu}")

# 5. Luo toinen taulukko
taulukko2 = np.array([1, 2, 3, 4, 5])
print(f"Toinen taulukko: {taulukko2}")

# 6. Laske summa
summa = taulukko + taulukko2

# 7. Tulosta tulos
print(f"Summa: {summa}")
