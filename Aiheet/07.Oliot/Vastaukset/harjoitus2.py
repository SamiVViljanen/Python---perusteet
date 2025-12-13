# Harjoitus 2: Dataclass
# Tavoite: Harjoittele @dataclass-dekoraattorin käyttöä

# 1. Tuo dataclass kirjastosta
from dataclasses import dataclass

# 2. Määritä Opiskelija dataclass @dataclass-dekoraattorilla
@dataclass
class Opiskelija:
    # 3. Määritä attribuutit tyyppimerkinnöillä
    nimi: str
    ikä: int
    opiskelijanumero: str

# 4. Luo 2-3 opiskelijaoliota
opiskelija1 = Opiskelija("Anna", 22, "12345")
opiskelija2 = Opiskelija("Matti", 24, "67890")
opiskelija3 = Opiskelija("Liisa", 21, "11111")

# 5. Tulosta oliot
print(opiskelija1)
print(opiskelija2)
print(opiskelija3)
