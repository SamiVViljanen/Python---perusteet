# Harjoitus 5: Kirjautuminen - RATKAISU

# 1. Määritä oikea käyttäjätunnus ja salasana
oikea_tunnus = "admin"
oikea_salasana = "salasana123"

# 2. Kysy käyttäjältä käyttäjätunnus ja salasana
tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

# 3. Tarkista molemmat
if tunnus == oikea_tunnus and salasana == oikea_salasana:
    print("Kirjautuminen onnistui!")
elif tunnus == oikea_tunnus and salasana != oikea_salasana:
    print("Salasana on väärin")
elif tunnus != oikea_tunnus and salasana == oikea_salasana:
    print("Käyttäjätunnus on väärin")
else:
    print("Sekä käyttäjätunnus että salasana ovat väärin")
