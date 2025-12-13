# Vastaukset: Algoritmit ja rekursio

Tässä kansiossa on ratkaisut algoritmien ja rekursion harjoituksiin.

---

## Harjoitus 1: Binäärihaku ⭐⭐

**Tavoite:** Oppia binäärihaku-algoritmi järjestetylle datalle.

### Ratkaisu

```python
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def binaarihaku(lista, etsittava):
    """
    Etsii luvun järjestetystä listasta binäärihaulla.
    Palauttaa indeksin jos löytyy, muuten -1.
    """
    vasen = 0
    oikea = len(lista) - 1
    
    while vasen <= oikea:
        keski = (vasen + oikea) // 2
        
        if lista[keski] == etsittava:
            return keski
        elif lista[keski] < etsittava:
            vasen = keski + 1
        else:
            oikea = keski - 1
    
    return -1

print(f"Lista: {lista}\n")

luku1 = 13
tulos1 = binaarihaku(lista, luku1)
print(f"Etsitään: {luku1}")
print(f"Löytyi indeksistä: {tulos1}\n")

luku2 = 8
tulos2 = binaarihaku(lista, luku2)
print(f"Etsitään: {luku2}")
print(f"Ei löytynyt ({tulos2})")
```

### Keskeiset oppipisteet

1. **Binäärihaku:** Puolittaa hakualueen joka kierroksella → O(log n)
2. **Järjestetty lista:** Binäärihaku vaatii että lista on järjestyksessä
3. **Keskikohta:** `(vasen + oikea) // 2`
4. **Hakualueen päivitys:** Liikuta `vasen` tai `oikea` keskikohdan mukaan

### Miten binäärihaku toimii?

Etsitään lukua 13 listasta `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]`:

```
Kierros 1: vasen=0, oikea=9, keski=4
  lista[4] = 9 < 13 → etsi oikealta
  vasen = 5

Kierros 2: vasen=5, oikea=9, keski=7
  lista[7] = 15 > 13 → etsi vasemmalta
  oikea = 6

Kierros 3: vasen=5, oikea=6, keski=5
  lista[5] = 11 < 13 → etsi oikealta
  vasen = 6

Kierros 4: vasen=6, oikea=6, keski=6
  lista[6] = 13 == 13 → LÖYTYI!
  Palauta 6
```

### Vaihtoehtoiset tavat

**Rekursiivinen binäärihaku:**
```python
def binaarihaku_rekursio(lista, etsittava, vasen=0, oikea=None):
    if oikea is None:
        oikea = len(lista) - 1
    
    if vasen > oikea:
        return -1
    
    keski = (vasen + oikea) // 2
    
    if lista[keski] == etsittava:
        return keski
    elif lista[keski] < etsittava:
        return binaarihaku_rekursio(lista, etsittava, keski + 1, oikea)
    else:
        return binaarihaku_rekursio(lista, etsittava, vasen, keski - 1)
```

**Pythonin bisect-moduuli:**
```python
import bisect

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
indeksi = bisect.bisect_left(lista, 13)
if indeksi < len(lista) and lista[indeksi] == 13:
    print(f"Löytyi: {indeksi}")
```

### Yleisiä virheitä

❌ **Virhe:** Järjestämätön lista
```python
lista = [5, 2, 9, 1, 7]
binaarihaku(lista, 7)  # Ei toimi! Pitää järjestää ensin
```

✅ **Oikein:**
```python
lista = [5, 2, 9, 1, 7]
lista.sort()  # [1, 2, 5, 7, 9]
binaarihaku(lista, 7)  # Nyt toimii
```

---

## Harjoitus 2: Fibonacci rekursiolla ⭐⭐

**Tavoite:** Oppia rekursion perusteita Fibonacci-lukujen avulla.

### Ratkaisu

```python
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

print("Fibonacci-luvut:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

### Keskeiset oppipisteet

1. **Perustapaukset:** F(0) = 0, F(1) = 1 (lopettavat rekursion)
2. **Rekursiivinen tapaus:** F(n) = F(n-1) + F(n-2)
3. **Kaksi kutsua:** Funktio kutsuu itseään kahdesti

### Miten rekursio toimii?

Lasketaan F(4):

```
fibonacci(4)
├─ fibonacci(3)
│  ├─ fibonacci(2)
│  │  ├─ fibonacci(1) → 1
│  │  └─ fibonacci(0) → 0
│  │  = 1
│  └─ fibonacci(1) → 1
│  = 2
└─ fibonacci(2)
   ├─ fibonacci(1) → 1
   └─ fibonacci(0) → 0
   = 1
= 3
```

### Ongelmia naiivissa rekursiossa

❌ **Ongelma:** Paljon turhaa laskentaa!
- F(4) laskee F(2) **kahdesti**
- F(5) laskee F(3) kahdesti, F(2) **kolme kertaa**
- F(10) laskee F(2) **55 kertaa**!

Aikakompleksisuus: **O(2ⁿ)** - eksponentiaalinen, erittäin hidas.

### Vaihtoehtoiset tavat

**Memoization (muistaminen):**
```python
def fibonacci_memo(n, muisti=None):
    if muisti is None:
        muisti = {}
    
    if n in muisti:
        return muisti[n]
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    tulos = fibonacci_memo(n - 1, muisti) + fibonacci_memo(n - 2, muisti)
    muisti[n] = tulos
    return tulos

# Nyt O(n) - lineaarinen!
print(fibonacci_memo(100))  # Toimii nopeasti!
```

**Iteratiivinen (nopein):**
```python
def fibonacci_iter(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### Yleisiä virheitä

❌ **Virhe:** Unohtaa perustapaukset
```python
def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2)
# RecursionError: maximum recursion depth exceeded
```

✅ **Oikein:** Aina perustapaukset!
```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## Harjoitus 3: Faktorilaali ⭐⭐

**Tavoite:** Vertailla rekursiivista ja iteratiivista ratkaisua.

### Ratkaisu

```python
def faktiolaali_rekursio(n):
    """Laskee n! rekursiivisesti"""
    if n <= 1:
        return 1
    return n * faktiolaali_rekursio(n - 1)

def faktiolaali_silmukka(n):
    """Laskee n! silmukalla"""
    tulo = 1
    for i in range(1, n + 1):
        tulo *= i
    return tulo

print("=== Faktiolaalit ===\n")

rek5 = faktiolaali_rekursio(5)
sil5 = faktiolaali_silmukka(5)
print(f"5! (rekursio): {rek5}")
print(f"5! (silmukka): {sil5}\n")

rek10 = faktiolaali_rekursio(10)
sil10 = faktiolaali_silmukka(10)
print(f"10! (rekursio): {rek10}")
print(f"10! (silmukka): {sil10}\n")

print("Molemmat antavat saman tuloksen!")
```

### Keskeiset oppipisteet

1. **Sama tulos, eri toteutus:** Molemmat laskevat n!
2. **Rekursio:** Selkeämpi, mutta hitaampi ja käyttää enemmän muistia
3. **Iteraatio:** Nopeampi ja muistiystävällisempi

### Rekursio vs. iteraatio

| Ominaisuus | Rekursio | Iteraatio |
|-----------|----------|-----------|
| **Luettavuus** | Selkeämpi | Perinteinen |
| **Nopeus** | Hitaampi | Nopeampi |
| **Muisti** | Enemmän (call stack) | Vähemmän |
| **Virheet** | Stack overflow | Ääretön silmukka |

### Miten rekursio toimii? (5!)

```
faktiolaali_rekursio(5)
= 5 * faktiolaali_rekursio(4)
= 5 * (4 * faktiolaali_rekursio(3))
= 5 * (4 * (3 * faktiolaali_rekursio(2)))
= 5 * (4 * (3 * (2 * faktiolaali_rekursio(1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
```

### Vaihtoehtoiset tavat

**Pythonin math.factorial:**
```python
import math
print(math.factorial(5))  # 120
```

**Tail recursion (Python ei optimoi):**
```python
def faktiolaali_tail(n, acc=1):
    if n <= 1:
        return acc
    return faktiolaali_tail(n - 1, n * acc)
```

### Yleisiä virheitä

❌ **Virhe:** Väärä perustapaus
```python
def faktiolaali(n):
    if n == 0:  # Ei käsittele n=1 oikein
        return 1
    return n * faktiolaali(n - 1)
# faktiolaali(1) = 1 * faktiolaali(0) = 1 * 1 = 1 ✓ (toimii sattumalta)
```

✅ **Oikein:** n <= 1
```python
def faktiolaali(n):
    if n <= 1:
        return 1
    return n * faktiolaali(n - 1)
```

---

## Harjoitus 4: Palindromi-tarkistus ⭐⭐⭐

**Tavoite:** Käyttää rekursiota merkkijonon käsittelyyn.

### Ratkaisu

```python
def on_palindromi(s):
    """
    Tarkistaa rekursiivisesti onko merkkijono palindromi.
    """
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return on_palindromi(s[1:-1])

sanat = ["saippuakivikauppias", "anna", "Python", "Saippuakauppias"]

print("Palindromit:\n")
for sana in sanat:
    tulos = on_palindromi(sana)
    merkki = "✓" if tulos else "✗"
    tyyppi = "Palindromi" if tulos else "Ei palindromi"
    print(f"'{sana}' → {tyyppi} {merkki}")
```

### Keskeiset oppipisteet

1. **Rekursiivinen rakenne:** Tarkista reunat, sitten keskiosa
2. **Merkkijonon pilkkominen:** `s[1:-1]` poistaa ensimmäisen ja viimeisen
3. **Boolean-palautus:** True/False

### Miten rekursio toimii? ("anna")

```
on_palindromi("anna")
  s[0]='a', s[-1]='a' → OK
  → on_palindromi("nn")
      s[0]='n', s[-1]='n' → OK
      → on_palindromi("")
          len("") = 0 → True
      ← True
  ← True
← True
```

### Vaihtoehtoiset tavat

**Iteratiivinen (kaksi osoitinta):**
```python
def on_palindromi_iter(s):
    vasen, oikea = 0, len(s) - 1
    
    while vasen < oikea:
        if s[vasen] != s[oikea]:
            return False
        vasen += 1
        oikea -= 1
    
    return True
```

**Pythonic tapa:**
```python
def on_palindromi_pythonic(s):
    return s == s[::-1]
```

**Iso-/pienaakkoset huomioiden:**
```python
def on_palindromi_normalize(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return on_palindromi_normalize(s[1:-1])

print(on_palindromi_normalize("Saippuakauppias"))  # True
print(on_palindromi_normalize("A man a plan a canal Panama"))  # True
```

### Yleisiä virheitä

❌ **Virhe:** Unohtaa perustapauksen
```python
def on_palindromi(s):
    if s[0] != s[-1]:
        return False
    return on_palindromi(s[1:-1])
# IndexError: string index out of range (tyhjällä merkkijonolla)
```

✅ **Oikein:**
```python
def on_palindromi(s):
    if len(s) <= 1:  # Perustapaus!
        return True
    if s[0] != s[-1]:
        return False
    return on_palindromi(s[1:-1])
```

---

## Harjoitus 5: Hanoin tornit ⭐⭐⭐⭐

**Tavoite:** Ratkaista klassinen rekursiivinen ongelma.

### Ratkaisu

```python
def hanoin_tornit(n, lahde="A", kohde="C", apu="B"):
    """
    Ratkaisee Hanoin tornit -ongelman rekursiivisesti.
    Palauttaa siirtojen määrän.
    """
    if n == 1:
        print(f"Siirrä kiekko 1: {lahde} → {kohde}")
        return 1
    
    # Siirrä n-1 kiekkoa lähteestä apuun
    siirrot = hanoin_tornit(n - 1, lahde, apu, kohde)
    
    # Siirrä suurin kiekko lähteestä kohteeseen
    print(f"Siirrä kiekko {n}: {lahde} → {kohde}")
    siirrot += 1
    
    # Siirrä n-1 kiekkoa avusta kohteeseen
    siirrot += hanoin_tornit(n - 1, apu, kohde, lahde)
    
    return siirrot

print("=== HANOIN TORNIT (3 kiekkoa) ===\n")
siirtoja = hanoin_tornit(3)
print(f"\nValmis! {siirtoja} siirtoa.")
```

### Keskeiset oppipisteet

1. **Divide and conquer:** Jaa ongelma pienempiin osiin
2. **Kolme vaihetta:**
   - Siirrä n-1 kiekkoa apuun
   - Siirrä suurin kiekko kohteeseen
   - Siirrä n-1 kiekkoa kohteeseen
3. **Siirtojen määrä:** 2ⁿ - 1

### Miten Hanoin tornit toimii? (3 kiekkoa)

```
hanoin_tornit(3, A, C, B)
├─ hanoin_tornit(2, A, B, C)
│  ├─ hanoin_tornit(1, A, C, B)
│  │  → "Siirrä kiekko 1: A → C"
│  → "Siirrä kiekko 2: A → B"
│  └─ hanoin_tornit(1, C, B, A)
│     → "Siirrä kiekko 1: C → B"
→ "Siirrä kiekko 3: A → C"
└─ hanoin_tornit(2, B, C, A)
   ├─ hanoin_tornit(1, B, A, C)
   │  → "Siirrä kiekko 1: B → A"
   → "Siirrä kiekko 2: B → C"
   └─ hanoin_tornit(1, A, C, B)
      → "Siirrä kiekko 1: A → C"
```

### Siirtojen määrä

| Kiekkoja | Siirtoja | Kaava |
|----------|----------|-------|
| 1 | 1 | 2¹ - 1 |
| 2 | 3 | 2² - 1 |
| 3 | 7 | 2³ - 1 |
| 4 | 15 | 2⁴ - 1 |
| 5 | 31 | 2⁵ - 1 |
| 10 | 1023 | 2¹⁰ - 1 |
| 64 | 18,446,744,073,709,551,615 | 2⁶⁴ - 1 |

**Legenda:** 64 kiekkoa siirtäminen veisi ~585 miljardia vuotta (yksi siirto sekunnissa)!

### Vaihtoehtoiset tavat

**Ilman siirtojen laskentaa:**
```python
def hanoin_tornit_simple(n, lahde="A", kohde="C", apu="B"):
    if n == 1:
        print(f"Siirrä kiekko 1: {lahde} → {kohde}")
        return
    
    hanoin_tornit_simple(n - 1, lahde, apu, kohde)
    print(f"Siirrä kiekko {n}: {lahde} → {kohde}")
    hanoin_tornit_simple(n - 1, apu, kohde, lahde)
```

**Iteratiivinen (haastavampi):**
```python
def hanoin_tornit_iter(n):
    # Käyttää stackia simuloimaan rekursiota
    # Huomattavasti monimutkaisempi kuin rekursiivinen versio
    pass
```

### Yleisiä virheitä

❌ **Virhe:** Väärä parametrien järjestys
```python
def hanoin_tornit(n, lahde="A", kohde="C", apu="B"):
    if n == 1:
        print(f"Siirrä kiekko 1: {lahde} → {kohde}")
        return
    
    hanoin_tornit(n - 1, lahde, kohde, apu)  # VÄÄRIN! kohde ja apu väärinpäin
    print(f"Siirrä kiekko {n}: {lahde} → {kohde}")
    hanoin_tornit(n - 1, kohde, apu, lahde)  # VÄÄRIN!
```

✅ **Oikein:** Huomioi roolit (lähde, kohde, apu vaihtuvat)
```python
hanoin_tornit(n - 1, lahde, apu, kohde)  # kohde → apu
hanoin_tornit(n - 1, apu, kohde, lahde)  # apu → kohde
```

---

## Yhteenveto: Algoritmit ja rekursio

### Tärkeimmät algoritmit

**Binäärihaku**
- O(log n) - Logaritminen
- Vaatii järjestetyn listan
- Puolittaa hakualueen joka kierros

**Fibonacci**
- Klassinen rekursiivinen ongelma
- Naiivi O(2ⁿ) - hidas
- Memoization → O(n) - nopea

**Faktiolaali**
- Yksinkertainen rekursio
- Hyvä vertailu rekursio vs. iteraatio

**Palindromi**
- Merkkijonojen rekursiivinen käsittely
- Tarkista reunat → keskiosa

**Hanoin tornit**
- Divide and conquer
- 2ⁿ - 1 siirtoa
- Klassinen rekursio-esimerkki

### Rekursion muistilista

✅ **Aina tarvitset:**
1. **Perustapauksen** (base case) - milloin lopettaa
2. **Rekursiivisen tapauksen** - miten ongelma pienenee
3. **Edistymisen** - kohti perustapaus

✅ **Käytä rekursiota kun:**
- Ongelma on luonnostaan rekursiivinen
- Koodi on selkeämpi
- Puu-/graafirakenteet

❌ **Vältä kun:**
- Yksinkertainen silmukka riittää
- Suorituskyky kriittistä
- Stack overflow riski

### Aikakompleksisuudet

| Algoritmi | Aikakompleksisuus | Huomioita |
|-----------|-------------------|-----------|
| Lineaarihaku | O(n) | Ei vaadi järjestystä |
| Binäärihaku | O(log n) | Vaatii järjestyksen |
| Fibonacci (naiivi) | O(2ⁿ) | Erittäin hidas |
| Fibonacci (memo) | O(n) | Nopea |
| Faktiolaali | O(n) | Sekä rekursio että iteraatio |
| Hanoin tornit | O(2ⁿ) | Eksponentiaalinen |

---

**Vinkki:** Harjoittele algoritmeja paperilla ensin - piirrä kuvia, kirjoita pseudokoodia! 📝

**Seuraavaksi:** Jatka harjoittelua eri algoritmeilla ja rekursiivisilla ongelmilla! 🚀
