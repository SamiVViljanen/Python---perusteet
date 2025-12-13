# Harjoitus 4: Funktio usealla parametrilla
# Tavoite: Harjoittele useita parametreja ja return-arvoa

# 1. Määritä funktio laske_summa(a, b, c) joka palauttaa summan
def laske_summa(a, b, c):
    return a + b + c

# 2. Määritä funktio laske_keskiarvo(a, b, c) joka käyttää laske_summa()-funktiota
def laske_keskiarvo(a, b, c):
    summa = laske_summa(a, b, c)
    return summa / 3

# 3. Testaa molempia funktioita luvuilla 10, 20, 30
summa = laske_summa(10, 20, 30)
keskiarvo = laske_keskiarvo(10, 20, 30)

print(f"Summa: {summa}")
print(f"Keskiarvo: {keskiarvo}")
