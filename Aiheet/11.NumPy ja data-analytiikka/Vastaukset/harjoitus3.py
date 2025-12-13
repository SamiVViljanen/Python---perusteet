import numpy as np

# 1. Luo matriisit
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

# 2. Tulosta matriisit
print("Matriisi A:")
print(A)
print("\nMatriisi B:")
print(B)

# 3. Laske A + B
summa = A + B
print("\nA + B:")
print(summa)

# 4. Laske A - B
erotus = A - B
print("\nA - B:")
print(erotus)

# 5. Kerro A luvulla 3
kerrottu = A * 3
print("\nA * 3:")
print(kerrottu)

# 6. Laske transpoosi
transpoosi = A.T
print("\nA transpoosi:")
print(transpoosi)

# 7. Luo C ja laske matriisitulo
C = np.array([[1, 2], [3, 4], [5, 6]])
tulo = np.dot(A, C)  # tai A @ C
print("\nMatriisitulo A × C:")
print(tulo)
