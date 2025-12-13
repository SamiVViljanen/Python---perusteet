# Harjoitus 2: Fibonacci rekursiolla ⭐⭐

## Tehtävänanto

Fibonacci-luvut ovat: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34...`

Jokainen luku on kahden edellisen summa:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2)

Tee ohjelma, joka:
1. Toteuttaa rekursiivisen funktion `fibonacci(n)`
2. Laskee ensimmäiset 10 Fibonacci-lukua
3. Tulostaa ne muodossa: `F(0) = 0`, `F(1) = 1`, jne.

## Esimerkkitulostus

```
Fibonacci-luvut:
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
```

## Vinkit

- Rekursiivinen funktio:
  ```python
  def fibonacci(n):
      if n <= 0:
          return 0
      elif n == 1:
          return 1
      else:
          return fibonacci(n-1) + fibonacci(n-2)
  ```
- Tulosta for-silmukalla: `for i in range(10):`

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus2.py](harjoitus2.py)
