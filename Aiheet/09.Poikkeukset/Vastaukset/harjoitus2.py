# Harjoitus 2: Listan käsittely

lista = ["omena", "banaani", "päärynä", "appelsiini", "kiivi"]

print(f"Lista: {lista}")

try:
    indeksi = int(input("Anna indeksi (0-4): "))
    arvo = lista[indeksi]
    print(f"Arvo: {arvo}")
except ValueError:
    print("Virhe: Anna numero!")
except IndexError:
    print("Virhe: Indeksi on liian suuri! Käytä arvoja 0-4.")
