# Harjoitus 1: Binäärihaku

# 1. Luo järjestetty lista
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 2. Toteuta binäärihaku-funktio
def binaarihaku(lista, etsittava):
    """
    Etsii luvun järjestetystä listasta binäärihaulla.
    Palauttaa indeksin jos löytyy, muuten -1.
    """
    vasen = 0
    oikea = len(lista) - 1
    
    while vasen <= oikea:
        keski = (vasen + oikea) // 2
        
        if lista[keski] == etsittava:
            return keski
        elif lista[keski] < etsittava:
            vasen = keski + 1
        else:
            oikea = keski - 1
    
    return -1

# 3-5. Etsi ja tulosta
print(f"Lista: {lista}\n")

luku1 = 13
tulos1 = binaarihaku(lista, luku1)
print(f"Etsitään: {luku1}")
print(f"Löytyi indeksistä: {tulos1}\n")

luku2 = 8
tulos2 = binaarihaku(lista, luku2)
print(f"Etsitään: {luku2}")
print(f"Ei löytynyt ({tulos2})")
