# Harjoitus 3: Metodi joka käyttää attribuutteja
# Tavoite: Harjoittele metodeja jotka käyttävät olion attribuutteja

# 1. Määritä Suorakulmio-luokka
class Suorakulmio:
    # 2. __init__ metodi ottaa leveyden ja korkeuden
    def __init__(self, leveys, korkeus):
        # 3. Tallenna parametrit self-muuttujiin
        self.leveys = leveys
        self.korkeus = korkeus
    
    # 4. Määritä laske_pinta_ala metodi joka palauttaa pinta-alan
    def laske_pinta_ala(self):
        return self.leveys * self.korkeus
    
    # 5. Määritä laske_piiri metodi joka palauttaa piirin
    def laske_piiri(self):
        return 2 * (self.leveys + self.korkeus)

# 6. Luo Suorakulmio-olio (esim. 5 x 10)
suorakulmio = Suorakulmio(5, 10)

# 7. Tulosta pinta-ala ja piiri
print(f"Pinta-ala: {suorakulmio.laske_pinta_ala()}")
print(f"Piiri: {suorakulmio.laske_piiri()}")
