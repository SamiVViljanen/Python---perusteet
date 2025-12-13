# Harjoitus 5: Eri import-muodot
# Tavoite: Ymmärrä eri tapoja tuoda moduuleja

# 1. MUOTO 1: import math
import math

# 2. MUOTO 2: from random import randint, choice
from random import randint, choice

# 3. MUOTO 3: import datetime as dt
import datetime as dt

# 4. Laske neliöjuuri 16:sta (käytä math.sqrt)
neliojuuri = math.sqrt(16)

# 5. Luo satunnainen luku 1-100 (käytä randint)
satunnainen_luku = randint(1, 100)

# 6. Valitse satunnainen väri (käytä choice)
varit = ["punainen", "sininen", "vihreä"]
satunnainen_vari = choice(varit)

# 7. Hae tämän päivän päivämäärä (käytä dt.date.today)
tanaan = dt.date.today()

# 8. Tulosta kaikki tulokset
print(f"Neliöjuuri 16:sta: {neliojuuri}")
print(f"Satunnainen luku: {satunnainen_luku}")
print(f"Satunnainen väri: {satunnainen_vari}")
print(f"Tänään: {tanaan}")
