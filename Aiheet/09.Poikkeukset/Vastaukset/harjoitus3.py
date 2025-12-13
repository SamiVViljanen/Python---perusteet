# Harjoitus 3: Finally-harjoitus

try:
    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))
    toimitus = input("Valitse toimitus (+, -, *, /): ")
    
    if toimitus == "+":
        tulos = luku1 + luku2
    elif toimitus == "-":
        tulos = luku1 - luku2
    elif toimitus == "*":
        tulos = luku1 * luku2
    elif toimitus == "/":
        tulos = luku1 / luku2
    else:
        print("Virheellinen toimitus!")
        tulos = None
    
    if tulos is not None:
        print(f"Tulos: {tulos}")
        
except ValueError:
    print("Virhe: Anna molemmat luvut numeroina!")
except ZeroDivisionError:
    print("Virhe: Et voi jakaa nollalla!")
finally:
    print("Kiitos laskimen käytöstä!")
