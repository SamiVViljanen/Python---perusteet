# Harjoitus 1: Ensimmäinen luokka
# Tavoite: Harjoittele yksinkertaisen luokan määrittämistä

# 1. Määritä Koira-luokka
class Koira:
    # 2. __init__ metodi ottaa parametrit nimi ja rotu
    def __init__(self, nimi, rotu):
        # 3. Tallenna parametrit self-muuttujiin
        self.nimi = nimi
        self.rotu = rotu
    
    # 4. Määritä hauku-metodi
    def hauku(self):
        # 5. Tulosta tervehdys
        print(f"Hau hau! Minä olen {self.nimi}.")

# 6. Luo kaksi Koira-oliota
koira1 = Koira("Musti", "Sekarotuinen")
koira2 = Koira("Rekku", "Labradorinnoutaja")

# 7. Kutsu molempien hauku-metodia
koira1.hauku()
koira2.hauku()
