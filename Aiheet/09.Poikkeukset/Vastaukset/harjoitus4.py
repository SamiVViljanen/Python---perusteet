# Harjoitus 4: Else-lohko

try:
    ika = int(input("Anna ikäsi: "))
except ValueError:
    print("Virhe: Anna ikä numeroina!")
else:
    print(f"Ikäsi on {ika} vuotta.")
    
    if ika < 18:
        print("Olet alaikäinen.")
    else:
        print("Olet täysi-ikäinen.")
