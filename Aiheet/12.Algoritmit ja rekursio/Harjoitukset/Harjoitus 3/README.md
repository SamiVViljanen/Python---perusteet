# Harjoitus 3: Faktorilaali ⭐⭐

## Tehtävänanto

**Faktiolaali** (kertoma) merkitään `n!` ja se tarkoittaa:
- `n! = n × (n-1) × (n-2) × ... × 2 × 1`
- Esim: `5! = 5 × 4 × 3 × 2 × 1 = 120`

Tee ohjelma, joka:
1. Toteuttaa faktiolaalin **rekursiivisesti**: `faktiolaali_rekursio(n)`
2. Toteuttaa faktiolaalin **iteratiivisesti** (silmukalla): `faktiolaali_silmukka(n)`
3. Laskee `5!` molemmilla tavoilla
4. Laskee `10!` molemmilla tavoilla
5. Tulostaa tulokset ja vertailee

## Esimerkkitulostus

```
=== Faktiolaalit ===

5! (rekursio): 120
5! (silmukka): 120

10! (rekursio): 3628800
10! (silmukka): 3628800

Molemmat antavat saman tuloksen!
```

## Vinkit

**Rekursiivinen:**
```python
def faktiolaali_rekursio(n):
    if n <= 1:
        return 1
    return n * faktiolaali_rekursio(n - 1)
```

**Iteratiivinen:**
```python
def faktiolaali_silmukka(n):
    tulo = 1
    for i in range(1, n + 1):
        tulo *= i
    return tulo
```

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus3.py](harjoitus3.py)
