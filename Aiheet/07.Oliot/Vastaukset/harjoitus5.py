# Harjoitus 5: Pankkitili-luokka
# Tavoite: Yhdistä kaikki oppimasi ja luo käytännöllinen luokka

# 1. Määritä Pankkitili-luokka
class Pankkitili:
    # 2. __init__ metodi ottaa omistajan ja saldon (oletusarvo 0)
    def __init__(self, omistaja, saldo=0):
        # 3. Tallenna parametrit
        self.omistaja = omistaja
        self.saldo = saldo
    
    # 4. Määritä talleta metodi joka lisää summan saldoon
    def talleta(self, summa):
        self.saldo += summa
        print(f"Talletettiin {summa}€. Uusi saldo: {self.saldo}€")
    
    # 5. Määritä nosta metodi joka tarkistaa saldon ja vähentää summan
    def nosta(self, summa):
        if self.saldo >= summa:
            self.saldo -= summa
            print(f"Nostettiin {summa}€. Uusi saldo: {self.saldo}€")
        else:
            print("Ei tarpeeksi rahaa!")
    
    # 6. Määritä näytä_saldo metodi
    def näytä_saldo(self):
        print(f"Tilin saldo: {self.saldo}€")

# 7. Luo Pankkitili-olio
tili = Pankkitili("Matti Meikäläinen")

# 8. Testaa metodeja
tili.talleta(100)
tili.talleta(50)
tili.nosta(30)
tili.nosta(200)  # Tämän pitäisi epäonnistua
tili.näytä_saldo()
