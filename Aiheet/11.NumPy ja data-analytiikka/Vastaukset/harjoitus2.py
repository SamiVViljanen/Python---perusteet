import numpy as np

# Lämpötiladata
lampotilat_lista = [15.5, 18.2, 16.8, 20.1, 19.5, 17.3, 21.0]

# 1. Luo NumPy-taulukko
lampotilat = np.array(lampotilat_lista)
print(f"Lämpötilat: {lampotilat}")

# 2. Laske ja tulosta tilastot
keskiarvo = np.mean(lampotilat)
mediaani = np.median(lampotilat)
keskihajonta = np.std(lampotilat)
minimi = np.min(lampotilat)
maksimi = np.max(lampotilat)

print(f"Keskiarvo: {keskiarvo:.2f}°C")
print(f"Mediaani: {mediaani:.2f}°C")
print(f"Keskihajonta: {keskihajonta:.2f}°C")
print(f"Minimi: {minimi:.2f}°C")
print(f"Maksimi: {maksimi:.2f}°C")

# 3. Laske kuinka monta päivää yli 18°C
yli_18 = lampotilat > 18
paivien_maara = np.sum(yli_18)
print(f"Yli 18°C päiviä: {paivien_maara}")

# 4. Tulosta lämpimät päivät
lampimät_paivat = lampotilat[yli_18]
print(f"Lämpimät päivät: {lampimät_paivat}")
