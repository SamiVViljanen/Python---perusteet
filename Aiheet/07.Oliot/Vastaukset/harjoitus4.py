# Harjoitus 4: Luokka laskurilla
# Tavoite: Harjoittele muuttuvaa tilaa oliossa

# 1. Määritä Laskuri-luokka
class Laskuri:
    # 2. __init__ metodi alustaa arvon nollaksi
    def __init__(self):
        self.arvo = 0
    
    # 3. Määritä kasvata metodi joka kasvattaa arvoa yhdellä
    def kasvata(self):
        self.arvo += 1
    
    # 4. Määritä vahenna metodi joka vähentää arvoa yhdellä
    def vahenna(self):
        self.arvo -= 1
    
    # 5. Määritä näytä metodi joka tulostaa arvon
    def näytä(self):
        print(f"Laskurin arvo: {self.arvo}")

# 6. Luo Laskuri-olio
laskuri = Laskuri()

# 7. Kasvata 3 kertaa
laskuri.kasvata()
laskuri.kasvata()
laskuri.kasvata()

# 8. Vähennä kerran
laskuri.vahenna()

# 9. Näytä tulos
laskuri.näytä()
