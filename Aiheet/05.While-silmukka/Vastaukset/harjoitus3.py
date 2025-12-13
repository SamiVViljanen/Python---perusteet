# Harjoitus 3: Valikko break-komennolla
# Tavoite: Harjoittele while True ja break-komentoa

# 1. Tee ikuinen silmukka while True:
while True:
    # 2. Tulosta valikko
    print("1. Sano hei")
    print("2. Sano moi")
    print("0. Lopeta")
    
    # 3. Kysy käyttäjän valinta ja muunna se kokonaisluvuksi
    valinta = int(input("Valintasi: "))
    
    # 4. Jos valinta on 1, tulosta "Hei!"
    if valinta == 1:
        print("Hei!")
    
    # 5. Jos valinta on 2, tulosta "Moi!"
    elif valinta == 2:
        print("Moi!")
    
    # 6. Jos valinta on 0, tulosta "Näkemiin!" ja lopeta break-komennolla
    elif valinta == 0:
        print("Näkemiin!")
        break
    
    # 7. Lisää tyhjä rivi valikkojen väliin (print())
    print()
