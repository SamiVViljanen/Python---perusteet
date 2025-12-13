# Harjoitus 2: Fibonacci rekursiolla

# 1. Toteuta rekursiivinen Fibonacci-funktio
def fibonacci(n):
    """
    Laskee n:nnen Fibonacci-luvun rekursiivisesti.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 2-3. Laske ja tulosta ensimmäiset 10 Fibonacci-lukua
print("Fibonacci-luvut:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
