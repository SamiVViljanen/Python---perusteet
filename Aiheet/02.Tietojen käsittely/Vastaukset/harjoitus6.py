# Harjoitus 6: Muuttujien roolit yhdistettynä - RATKAISU

# Gatherer - kerää summaa
summa = 0

# Most-recent holder - pitää muistissa suurinta lukua
suurin = None

# 1-5. Kysy viisi lukua
luku1 = int(input("Anna luku 1: "))
summa += luku1
suurin = luku1  # Ensimmäinen luku on aluksi suurin

luku2 = int(input("Anna luku 2: "))
summa += luku2
if luku2 > suurin:
    suurin = luku2

luku3 = int(input("Anna luku 3: "))
summa += luku3
if luku3 > suurin:
    suurin = luku3

luku4 = int(input("Anna luku 4: "))
summa += luku4
if luku4 > suurin:
    suurin = luku4

luku5 = int(input("Anna luku 5: "))
summa += luku5
if luku5 > suurin:
    suurin = luku5

# Transformation - muunna summa muotoiltuun muotoon
summa_muotoiltu = f"{summa:.2f}"

# Tulosta tulokset
print(f"Suurin luku: {suurin}")
print(f"Summa: {summa_muotoiltu}")
