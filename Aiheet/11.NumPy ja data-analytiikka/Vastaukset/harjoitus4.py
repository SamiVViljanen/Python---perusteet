import numpy as np

# Arvosanadata
arvosanat_lista = [
    [4, 5, 3],
    [5, 5, 4],
    [2, 3, 3],
    [4, 4, 5],
    [3, 4, 4]
]

# 1. Luo NumPy-taulukko
arvosanat = np.array(arvosanat_lista)
print("Arvosanat:")
print(arvosanat)
print()

# 2. Laske opiskelijoiden keskiarvot (rivit)
opiskelija_ka = np.mean(arvosanat, axis=1)
print(f"Opiskelijoiden keskiarvot: {opiskelija_ka}")

# 3. Laske kurssien keskiarvot (sarakkeet)
kurssi_ka = np.mean(arvosanat, axis=0)
print(f"Kurssien keskiarvot: {kurssi_ka}")
print()

# 4. Etsi paras opiskelija
paras_indeksi = np.argmax(opiskelija_ka)
paras_ka = opiskelija_ka[paras_indeksi]
print(f"Paras opiskelija: {paras_indeksi + 1} (keskiarvo: {paras_ka:.2f})")

# 5. Etsi vaikein kurssi
vaikein_indeksi = np.argmin(kurssi_ka)
vaikein_ka = kurssi_ka[vaikein_indeksi]
print(f"Vaikein kurssi: {vaikein_indeksi + 1} (keskiarvo: {vaikein_ka:.2f})")

# 6. Laske kuinka monella on vähintään yksi 5
on_viitonen = np.any(arvosanat == 5, axis=1)
viitosen_saaneet = np.sum(on_viitonen)
print(f"Opiskelijoita joilla vähintään yksi 5: {viitosen_saaneet}")

# 7. Laske kokonaiskeskiarvo
kokonais_ka = np.mean(arvosanat)
print(f"Kokonaiskeskiarvo: {kokonais_ka:.2f}")
