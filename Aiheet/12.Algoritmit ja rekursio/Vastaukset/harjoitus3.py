# Harjoitus 3: Faktorilaali

# 1. Toteuta faktiolaali rekursiivisesti
def faktiolaali_rekursio(n):
    """Laskee n! rekursiivisesti"""
    if n <= 1:
        return 1
    return n * faktiolaali_rekursio(n - 1)

# 2. Toteuta faktiolaali iteratiivisesti
def faktiolaali_silmukka(n):
    """Laskee n! silmukalla"""
    tulo = 1
    for i in range(1, n + 1):
        tulo *= i
    return tulo

# 3-5. Laske ja vertaile
print("=== Faktiolaalit ===\n")

# 5!
rek5 = faktiolaali_rekursio(5)
sil5 = faktiolaali_silmukka(5)
print(f"5! (rekursio): {rek5}")
print(f"5! (silmukka): {sil5}\n")

# 10!
rek10 = faktiolaali_rekursio(10)
sil10 = faktiolaali_silmukka(10)
print(f"10! (rekursio): {rek10}")
print(f"10! (silmukka): {sil10}\n")

print("Molemmat antavat saman tuloksen!")
