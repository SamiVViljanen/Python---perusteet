# Harjoitus 4: Arvauspeli
# Tavoite: Yhdistä while-silmukka, ehtolauseet ja laskuri

# 1. Määritä oikea luku (esim. 7)
oikea_luku = 7

# 2. Luo laskuri arvausten määrälle
yritykset = 0

# 3. Kysy ensimmäinen arvaus käyttäjältä
arvaus = int(input("Arvaa luku (1-10): "))
yritykset += 1

# 4. Tee while-silmukka, joka jatkuu niin kauan kuin arvaus on väärin
while arvaus != oikea_luku:
    # 5. (Yrityslaskuri kasvatettiin jo ylhäällä ja alhaalla)
    
    # 6. Tarkista onko arvaus liian pieni
    if arvaus < oikea_luku:
        print("Liian pieni!")
    
    # 7. Muuten jos arvaus on liian suuri
    else:
        print("Liian suuri!")
    
    # 8. Kysy uusi arvaus
    arvaus = int(input("Arvaa luku (1-10): "))
    yritykset += 1

# 9. Kun silmukka loppuu (arvaus oli oikein), tulosta onnistumisviesti ja yritysten määrä
print(f"Oikein! Käytit {yritykset} arvausta.")
