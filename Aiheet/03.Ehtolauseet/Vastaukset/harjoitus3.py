# Harjoitus 3: Parillinen vai pariton? - RATKAISU

# 1. Kysy käyttäjältä kokonaisluku
luku = int(input("Anna luku: "))

# 2-3. Tarkista onko luku parillinen vai pariton ja tulosta tulos
if luku % 2 == 0:
    print(f"Luku {luku} on parillinen")
else:
    print(f"Luku {luku} on pariton")
