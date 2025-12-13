# Harjoitus 2: Salasanan tarkistus
# Tavoite: Harjoittele while-silmukkaa käyttäjän syötteen kanssa

# 1. Määritä oikea salasana
oikea_salasana = "python123"

# 2. Kysy ensimmäinen salasana käyttäjältä
salasana = input("Anna salasana: ")

# 3. Tee while-silmukka, joka toistuu niin kauan kuin salasana ei ole oikein
while salasana != oikea_salasana:
    # 4. Kysy salasana uudelleen
    salasana = input("Anna salasana: ")

# 5. Kun silmukka loppuu (salasana oli oikein), tulosta onnistumisviesti
print("Kirjautuminen onnistui!")
