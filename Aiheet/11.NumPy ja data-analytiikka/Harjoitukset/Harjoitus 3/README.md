# Harjoitus 3: Matriisioperaatiot ⭐⭐

## Tehtävänanto

Harjoittele 2D-taulukoiden (matriisien) käsittelyä.

Tee ohjelma, joka:
1. Luo kaksi 2×3 matriisia:
   - `A = [[1, 2, 3], [4, 5, 6]]`
   - `B = [[7, 8, 9], [10, 11, 12]]`
2. Tulostaa molemmat matriisit
3. Laskee matriisien summan (A + B)
4. Laskee matriisien erotuksen (A - B)
5. Kertoo matriisin A luvulla 3
6. Laskee matriisin A transpoosin
7. Luo 3×2 matriisin C ja laskee matriisitulon A × C

## Esimerkkitulostus

```
Matriisi A:
[[1 2 3]
 [4 5 6]]

Matriisi B:
[[ 7  8  9]
 [10 11 12]]

A + B:
[[ 8 10 12]
 [14 16 18]]

A - B:
[[-6 -6 -6]
 [-6 -6 -6]]

A * 3:
[[ 3  6  9]
 [12 15 18]]

A transpoosi:
[[1 4]
 [2 5]
 [3 6]]

Matriisitulo A × C:
[[...]]
```

## Vinkit

- 2D-taulukko: `np.array([[...], [...]])`
- Yhteen-/vähennyslasku: `A + B`, `A - B`
- Skalaarikertolasku: `A * 3`
- Transpoosi: `A.T` tai `np.transpose(A)`
- Matriisitulo: `np.dot(A, C)` tai `A @ C`
- Muista: matriisitulolle A(m×n) × C(n×p) → tulos(m×p)

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus3.py](harjoitus3.py)
