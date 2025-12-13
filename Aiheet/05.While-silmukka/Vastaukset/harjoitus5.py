# Harjoitus 5: Positiivisten lukujen summa
# Tavoite: Harjoittele while-silmukkaa ja gatherer-roolia

# 1. Luo kaksi laskuria: summa ja määrä
summa = 0
maara = 0

# 2. Kysy ensimmäinen luku käyttäjältä
luku = int(input("Anna luku: "))

# 3. Tee while-silmukka, joka jatkuu niin kauan kuin luku on positiivinen
while luku > 0:
    # 4. Lisää luku summaan (gatherer-rooli)
    summa += luku
    
    # 5. Kasvata määrälaskuria
    maara += 1
    
    # 6. Kysy uusi luku
    luku = int(input("Anna luku: "))

# 7. Kun silmukka loppuu, tulosta tulokset
print(f"Syötit {maara} positiivista lukua.")
print(f"Summa: {summa}")
