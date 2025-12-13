# Harjoitus 1: Turvallinen jako

try:
    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))
    tulos = luku1 / luku2
    print(f"Tulos: {tulos}")
except ValueError:
    print("Virhe: Anna molemmat luvut numeroina!")
except ZeroDivisionError:
    print("Virhe: Et voi jakaa nollalla!")
