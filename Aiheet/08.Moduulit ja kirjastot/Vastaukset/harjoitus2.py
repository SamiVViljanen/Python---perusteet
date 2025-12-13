# Harjoitus 2: Random-moduuli ja arvauspeli
# Tavoite: Harjoittele random-moduulin käyttöä

# 1. Tuo random-moduuli
import random

# 2. Luo satunnainen luku 1-20
oikea_luku = random.randint(1, 20)

# 3. Tee while-silmukka joka jatkuu kunnes käyttäjä arvaa oikein
while True:
    # 4. Kysy käyttäjältä arvaus
    arvaus = int(input("Arvaa luku 1-20: "))
    
    # 5. Vertaa arvausta
    if arvaus == oikea_luku:
        print(f"Oikein! Luku oli {oikea_luku}.")
        break
    elif arvaus < oikea_luku:
        print("Liian pieni!")
    else:
        print("Liian suuri!")
