# Algoritmit ja rekursio

## Sisällysluettelo
1. [Mikä on algoritmi?](#mikä-on-algoritmi)
2. [Pseudokoodi](#pseudokoodi)
3. [Algoritmin tehokkuus](#algoritmin-tehokkuus)
4. [Yleiset algoritmit](#yleiset-algoritmit)
5. [Rekursio](#rekursio)
6. [Rekursio vs. iteraatio](#rekursio-vs-iteraatio)
7. [Rekursiiviset algoritmit](#rekursiiviset-algoritmit)
8. [Käytännön sovelluksia](#käytännön-sovelluksia)
9. [Yhteenveto](#yhteenveto)

---

Tässä oppaassa opit, mitä algoritmit ovat, miten kirjoittaa pseudokoodia ja miten rekursio toimii.

## Mikä on algoritmi?

**Algoritmi** on selkeä, vaiheittainen ohje ongelman ratkaisemiseen. Se on kuin resepti: lista askeleista, jotka vievät haluttuun lopputulokseen.

### Esimerkkejä algoritmeista

**Algoritmi 1: Kahvin keitto**
1. Mittaa vettä
2. Kaada vesi keittiomeen
3. Lisää kahvijauheet
4. Kytke virta päälle
5. Odota kunnes kahvi on valmis
6. Kaada kupiin

**Algoritmi 2: Suurimman luvun etsiminen**
1. Aloita ensimmäisestä luvusta
2. Oleta, että se on suurin
3. Käy läpi loput luvut
4. Jos löydät suuremman, päivitä suurin
5. Palauta suurin luku

### Hyvän algoritmin ominaisuudet

✅ **Selkeä** - Jokainen askel on yksiselitteinen
✅ **Äärellinen** - Algoritmi päättyy jossain vaiheessa
✅ **Tehokas** - Ratkaisee ongelman järkevästi
✅ **Oikea** - Antaa oikean tuloksen kaikilla syötteillä
✅ **Yleinen** - Toimii kaikilla sallituilla syötteillä

### Yksinkertainen esimerkki Pythonilla

```python
def etsi_suurin(luvut):
    """
    Algoritmi suurimman luvun etsimiseen listasta
    """
    # Askel 1: Tarkista että lista ei ole tyhjä
    if not luvut:
        return None
    
    # Askel 2: Oleta ensimmäinen suurimmaksi
    suurin = luvut[0]
    
    # Askel 3: Käy läpi loput luvut
    for luku in luvut[1:]:
        # Askel 4: Päivitä jos löydät suuremman
        if luku > suurin:
            suurin = luku
    
    # Askel 5: Palauta tulos
    return suurin

# Testaus
lista = [3, 7, 2, 9, 1, 5]
print(f"Suurin luku: {etsi_suurin(lista)}")  # 9
```

## Pseudokoodi

**Pseudokoodi** on algoritmin kuvaus, joka näyttää ohjelmointikieleltä mutta ei ole sitä. Se on "välimuoto" luonnollisen kielen ja ohjelmointikielen välillä.

### Miksi käyttää pseudokoodia?

- 📝 Suunnittele algoritmi ennen koodaamista
- 🤝 Kommunikoi ideoita muille ohjelmoijille
- 🌍 Kieliriippumaton - toimii kaikilla kielillä
- 🧠 Keskity logiikkaan, ei syntaksiin

### Pseudokoodin säännöt

1. **Ei tarkkaa syntaksia** - vapaamuotoinen
2. **Selkeä rakenne** - sisennys ja lohkot
3. **Yksinkertainen** - ei kaikkia yksityiskohtia
4. **Looginen** - helppo muuttaa ohjelmakoodiksi

### Esimerkki 1: Luvun parillisuu

```
PSEUDOKOODI:
-----------
FUNKTIO onko_parillinen(luku)
    JOS luku % 2 == 0 NIIN
        PALAUTA tosi
    MUUTEN
        PALAUTA epätosi
LOPPU
```

**Python-koodi:**
```python
def onko_parillinen(luku):
    if luku % 2 == 0:
        return True
    else:
        return False
```

### Esimerkki 2: Keskiarvon laskeminen

```
PSEUDOKOODI:
-----------
FUNKTIO laske_keskiarvo(luvut)
    summa ← 0
    määrä ← luvut.pituus
    
    JOKAISELLE luku JOUKOSSA luvut
        summa ← summa + luku
    LOPPU
    
    keskiarvo ← summa / määrä
    PALAUTA keskiarvo
LOPPU
```

**Python-koodi:**
```python
def laske_keskiarvo(luvut):
    summa = 0
    määrä = len(luvut)
    
    for luku in luvut:
        summa = summa + luku
    
    keskiarvo = summa / määrä
    return keskiarvo
```

### Esimerkki 3: Binäärihaku

```
PSEUDOKOODI:
-----------
FUNKTIO binäärihaku(lista, etsittävä)
    vasen ← 0
    oikea ← lista.pituus - 1
    
    WHILE vasen <= oikea:
        keski ← (vasen + oikea) / 2
        
        JOS lista[keski] == etsittävä NIIN
            PALAUTA keski
        MUUTEN JOS lista[keski] < etsittävä NIIN
            vasen ← keski + 1
        MUUTEN
            oikea ← keski - 1
        LOPPU
    LOPPU
    
    PALAUTA -1  // Ei löytynyt
LOPPU
```

**Python-koodi:**
```python
def binäärihaku(lista, etsittävä):
    vasen = 0
    oikea = len(lista) - 1
    
    while vasen <= oikea:
        keski = (vasen + oikea) // 2
        
        if lista[keski] == etsittävä:
            return keski
        elif lista[keski] < etsittävä:
            vasen = keski + 1
        else:
            oikea = keski - 1
    
    return -1  # Ei löytynyt
```

### Pseudokoodin avainsanat

| Pseudokoodi | Python | Merkitys |
|------------|--------|----------|
| `FUNKTIO` | `def` | Funktion määrittely |
| `JOS ... NIIN` | `if` | Ehtolause |
| `MUUTEN JOS` | `elif` | Vaihtoehtoinen ehto |
| `MUUTEN` | `else` | Muuten |
| `WHILE` | `while` | Toistorakenne |
| `JOKAISELLE` | `for` | Silmukka |
| `PALAUTA` | `return` | Palauta arvo |
| `←` | `=` | Sijoitus |
| `==` | `==` | Vertailu |
| `JA` | `and` | Looginen ja |
| `TAI` | `or` | Looginen tai |

## Algoritmin tehokkuus

Algoritmin **tehokkuus** tarkoittaa, kuinka nopeasti se toimii ja paljonko se käyttää muistia.

### Aikakompleksisuus (Big O)

**Big O -notaatio** kuvaa algoritmin suoritusajan kasvua syötteen koon kasvaessa.

#### Yleiset kompleksisuusluokat

| Notaatio | Nimi | Esimerkki | Selitys |
|----------|------|-----------|---------|
| `O(1)` | Vakio | Indeksihaku | Aika ei riipu syötteen koosta |
| `O(log n)` | Logaritminen | Binäärihaku | Puolittaa ongelman joka kierroksella |
| `O(n)` | Lineaarinen | Lineaarihaku | Käy läpi kaikki alkiot kerran |
| `O(n log n)` | Linearitminen | Merge sort | Tehokas järjestäminen |
| `O(n²)` | Neliöllinen | Kupla järjestäminen | Sisäkkäiset silmukat |
| `O(2ⁿ)` | Eksponentiaalinen | Fibonacci (naiivi) | Erittäin hidas |

### Esimerkki: Eri hakualgoritmit

```python
import time

def lineaarihaku(lista, etsittävä):
    """O(n) - Lineaarinen aikakompleksisuus"""
    for i, alkio in enumerate(lista):
        if alkio == etsittävä:
            return i
    return -1

def binäärihaku(lista, etsittävä):
    """O(log n) - Logaritminen aikakompleksisuus
    HUOM: Vaatii järjestetyn listan!"""
    vasen, oikea = 0, len(lista) - 1
    
    while vasen <= oikea:
        keski = (vasen + oikea) // 2
        
        if lista[keski] == etsittävä:
            return keski
        elif lista[keski] < etsittävä:
            vasen = keski + 1
        else:
            oikea = keski - 1
    
    return -1

# Testaus
lista = list(range(1, 1000001))  # Miljoona lukua

# Lineaarihaku
alku = time.time()
lineaarihaku(lista, 999999)
print(f"Lineaarihaku: {time.time() - alku:.4f}s")

# Binäärihaku
alku = time.time()
binäärihaku(lista, 999999)
print(f"Binäärihaku: {time.time() - alku:.6f}s")
# Binäärihaku on PALJON nopeampi!
```

### Käytännön vertailu

```python
def vertaa_kompleksisuutta():
    """Havainnollistaa eri aikakompleksisuuksia"""
    n_arvot = [10, 100, 1000]
    
    print("Operaatioiden määrä eri algoritmeilla:\n")
    print(f"{'n':>6} {'O(1)':>10} {'O(log n)':>10} {'O(n)':>10} {'O(n log n)':>15} {'O(n²)':>10}")
    print("-" * 70)
    
    for n in n_arvot:
        import math
        o_1 = 1
        o_log_n = int(math.log2(n))
        o_n = n
        o_n_log_n = int(n * math.log2(n))
        o_n2 = n * n
        
        print(f"{n:>6} {o_1:>10} {o_log_n:>10} {o_n:>10} {o_n_log_n:>15} {o_n2:>10}")

vertaa_kompleksisuutta()
```

**Tulostus:**
```
Operaatioiden määrä eri algoritmeilla:

     n       O(1)   O(log n)       O(n)      O(n log n)       O(n²)
----------------------------------------------------------------------
    10          1          3         10              33        100
   100          1          6        100             664      10000
  1000          1          9       1000            9965    1000000
```

## Yleiset algoritmit

### 1. Etsimisalgoritmit

#### Lineaarihaku (Linear Search)

```python
def lineaarihaku(lista, etsittävä):
    """
    Käy läpi listan alkio kerrallaan
    Aikakompleksisuus: O(n)
    """
    for i in range(len(lista)):
        if lista[i] == etsittävä:
            return i  # Palauta indeksi
    return -1  # Ei löytynyt

# Esimerkki
lista = [5, 2, 8, 1, 9, 3]
print(lineaarihaku(lista, 8))  # 2
print(lineaarihaku(lista, 7))  # -1
```

#### Binäärihaku (Binary Search)

```python
def binäärihaku(lista, etsittävä):
    """
    Puolittaa hakualueen joka kierroksella
    Aikakompleksisuus: O(log n)
    VAATII: Järjestetyn listan!
    """
    vasen = 0
    oikea = len(lista) - 1
    
    while vasen <= oikea:
        keski = (vasen + oikea) // 2
        
        if lista[keski] == etsittävä:
            return keski
        elif lista[keski] < etsittävä:
            vasen = keski + 1  # Etsi oikealta puolelta
        else:
            oikea = keski - 1  # Etsi vasemmalta puolelta
    
    return -1

# Esimerkki (TÄYTYY olla järjestyksessä!)
lista = [1, 2, 3, 5, 8, 9]
print(binäärihaku(lista, 8))  # 4
print(binäärihaku(lista, 7))  # -1
```

### 2. Järjestämisalgoritmit

#### Kuplajärjestäminen (Bubble Sort)

```python
def kuplajärjestäminen(lista):
    """
    Vertailee vierekkäisiä alkioita ja vaihtaa ne tarvittaessa
    Aikakompleksisuus: O(n²)
    Hidas, mutta yksinkertainen
    """
    n = len(lista)
    
    # Ulompi silmukka: n kierrosta
    for i in range(n):
        # Sisempi silmukka: vertailee vierekkäisiä
        for j in range(0, n - i - 1):
            # Jos vasen > oikea, vaihda
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

# Esimerkki
lista = [64, 34, 25, 12, 22, 11, 90]
print(kuplajärjestäminen(lista))
# [11, 12, 22, 25, 34, 64, 90]
```

#### Yhdistämisjärjestäminen (Merge Sort)

```python
def yhdistämisjärjestäminen(lista):
    """
    Jakaa listan pienempiin osiin ja yhdistää ne järjestyksessä
    Aikakompleksisuus: O(n log n)
    Tehokas ja vakaa
    """
    if len(lista) <= 1:
        return lista
    
    # Jaa kahtia
    keski = len(lista) // 2
    vasen = yhdistämisjärjestäminen(lista[:keski])
    oikea = yhdistämisjärjestäminen(lista[keski:])
    
    # Yhdistä järjestyksessä
    return yhdistä(vasen, oikea)

def yhdistä(vasen, oikea):
    """Yhdistää kaksi järjestettyä listaa"""
    tulos = []
    i = j = 0
    
    # Vertaile ja lisää pienempi
    while i < len(vasen) and j < len(oikea):
        if vasen[i] <= oikea[j]:
            tulos.append(vasen[i])
            i += 1
        else:
            tulos.append(oikea[j])
            j += 1
    
    # Lisää loput
    tulos.extend(vasen[i:])
    tulos.extend(oikea[j:])
    
    return tulos

# Esimerkki
lista = [64, 34, 25, 12, 22, 11, 90]
print(yhdistämisjärjestäminen(lista))
# [11, 12, 22, 25, 34, 64, 90]
```

### 3. Muut algoritmit

#### Kahden luvun summa (Two Sum)

```python
def kahden_summa(luvut, tavoite):
    """
    Etsi kaksi lukua, jotka summautuvat tavoitteeseen
    Aikakompleksisuus: O(n)
    """
    nähty = {}  # Tallennetaan nähty: indeksi
    
    for i, luku in enumerate(luvut):
        tarvitaan = tavoite - luku
        
        if tarvitaan in nähty:
            return [nähty[tarvitaan], i]
        
        nähty[luku] = i
    
    return None  # Ei löytynyt

# Esimerkki
luvut = [2, 7, 11, 15]
tavoite = 9
print(kahden_summa(luvut, tavoite))  # [0, 1] (2 + 7 = 9)
```

## Rekursio

**Rekursio** tarkoittaa, että funktio kutsuu **itseään**. Se on tehokas tapa ratkaista ongelmia, jotka voidaan jakaa pienempiin samantyyppisiin ongelmiin.

### Rekursion periaate

```python
def rekursiivinen_funktio(parametri):
    # TÄRKEÄ: Perustapaus (base case)
    if tapauksen_lopetus:
        return tulos
    
    # Rekursiivinen tapaus
    return rekursiivinen_funktio(pienempi_parametri)
```

### Yksinkertainen esimerkki: Laskuri

```python
def laske_alas(n):
    """Laskee alaspäin nollaan"""
    # Perustapaus: lopeta kun 0
    if n <= 0:
        print("Valmis!")
        return
    
    # Tulosta ja kutsu itseään pienemmällä luvulla
    print(n)
    laske_alas(n - 1)

laske_alas(5)
# 5
# 4
# 3
# 2
# 1
# Valmis!
```

### Miten rekursio toimii?

```python
def faktiolaali(n):
    """
    Laskee kertoman: n! = n × (n-1) × (n-2) × ... × 1
    Esim: 5! = 5 × 4 × 3 × 2 × 1 = 120
    """
    # Perustapaus
    if n <= 1:
        return 1
    
    # Rekursiivinen tapaus
    return n * faktiolaali(n - 1)

print(faktiolaali(5))  # 120
```

**Mitä tapahtuu?**
```
faktiolaali(5)
= 5 * faktiolaali(4)
= 5 * (4 * faktiolaali(3))
= 5 * (4 * (3 * faktiolaali(2)))
= 5 * (4 * (3 * (2 * faktiolaali(1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
```

### Fibonacci-luvut rekursiivisesti

```python
def fibonacci(n):
    """
    Fibonacci-luvut: 0, 1, 1, 2, 3, 5, 8, 13, 21...
    Jokainen luku on kahden edellisen summa
    """
    # Perustapaukset
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Rekursiivinen tapaus
    return fibonacci(n - 1) + fibonacci(n - 2)

# Ensimmäiset 10 Fibonacci-lukua
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

### Rekursion visualisointi

```python
def fibonacci_debug(n, sisennys=0):
    """Fibonacci debug-tulosteilla"""
    print("  " * sisennys + f"fibonacci({n})")
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_debug(n - 1, sisennys + 1) + fibonacci_debug(n - 2, sisennys + 1)

fibonacci_debug(4)
# fibonacci(4)
#   fibonacci(3)
#     fibonacci(2)
#       fibonacci(1)
#       fibonacci(0)
#     fibonacci(1)
#   fibonacci(2)
#     fibonacci(1)
#     fibonacci(0)
```

### Rekursion sudenkuopp

```python
# ❌ HUONO: Ei perustapaus → ääretön rekursio!
def huono_funktio(n):
    return huono_funktio(n - 1)  # Stack overflow!

# ❌ HUONO: Ei edisty kohti perustapaus
def huono_fibonacci(n):
    if n == 0:
        return 0
    return huono_fibonacci(n + 1)  # n kasvaa, ei laske!

# ✅ HYVÄ: Selkeä perustapaus ja edistyminen
def hyvä_faktiolaali(n):
    if n <= 1:  # Perustapaus
        return 1
    return n * hyvä_faktiolaali(n - 1)  # Kohti perustapaus
```

## Rekursio vs. iteraatio

Sama ongelma voidaan ratkaista **rekursiivisesti** tai **iteratiivisesti** (silmukalla).

### Esimerkki: Summan laskeminen

#### Rekursiivinen versio

```python
def summa_rekursio(n):
    """Laskee 1 + 2 + 3 + ... + n"""
    if n <= 0:
        return 0
    return n + summa_rekursio(n - 1)

print(summa_rekursio(5))  # 15 (1+2+3+4+5)
```

#### Iteratiivinen versio

```python
def summa_iteraatio(n):
    """Laskee 1 + 2 + 3 + ... + n"""
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

print(summa_iteraatio(5))  # 15
```

### Vertailu

| Ominaisuus | Rekursio | Iteraatio |
|-----------|----------|-----------|
| **Luettavuus** | Usein selkeämpi | Voi olla monimutkainen |
| **Nopeus** | Hitaampi (funktiokutsut) | Nopeampi |
| **Muisti** | Enemmän (call stack) | Vähemmän |
| **Virheet** | Stack overflow riski | Ääretön silmukka riski |
| **Käyttö** | Puu-/rekursiiviset rakenteet | Yksinkertaiset silmukat |

### Milloin käyttää rekursiota?

✅ **Käytä rekursiota kun:**
- Ongelma on luonnostaan rekursiivinen (puut, graafit)
- Koodi on selkeämpi rekursiolla
- Suorituskyky ei ole kriittinen
- Datamäärä on pieni/keskikokoinen

❌ **Älä käytä rekursiota kun:**
- Yksinkertainen silmukka riittää
- Suorituskyky on kriittistä
- Datamäärä on erittäin suuri
- Riski stack overflow -virheestä

## Rekursiiviset algoritmit

### 1. Binäärihaku rekursiivisesti

```python
def binäärihaku_rekursio(lista, etsittävä, vasen=0, oikea=None):
    """Binäärihaku rekursiivisella toteutuksella"""
    if oikea is None:
        oikea = len(lista) - 1
    
    # Perustapaus: ei löytynyt
    if vasen > oikea:
        return -1
    
    keski = (vasen + oikea) // 2
    
    # Perustapaus: löytyi!
    if lista[keski] == etsittävä:
        return keski
    
    # Rekursiiviset tapaukset
    elif lista[keski] < etsittävä:
        return binäärihaku_rekursio(lista, etsittävä, keski + 1, oikea)
    else:
        return binäärihaku_rekursio(lista, etsittävä, vasen, keski - 1)

# Esimerkki
lista = [1, 3, 5, 7, 9, 11, 13, 15]
print(binäärihaku_rekursio(lista, 9))   # 4
print(binäärihaku_rekursio(lista, 10))  # -1
```

### 2. Suurin yhteinen tekijä (Euklides)

```python
def syt(a, b):
    """
    Eukleideen algoritmi suurimman yhteisen tekijän laskemiseen
    Esim: syt(48, 18) = 6
    """
    # Perustapaus
    if b == 0:
        return a
    
    # Rekursiivinen tapaus
    return syt(b, a % b)

print(syt(48, 18))  # 6
print(syt(100, 35))  # 5
```

**Miten toimii?**
```
syt(48, 18)
= syt(18, 48 % 18)  # 48 % 18 = 12
= syt(18, 12)
= syt(12, 18 % 12)  # 18 % 12 = 6
= syt(12, 6)
= syt(6, 12 % 6)    # 12 % 6 = 0
= syt(6, 0)
= 6
```

### 3. Potenssilasku

```python
def potenssi(kantaluku, eksponentti):
    """
    Laskee kantaluku^eksponentti rekursiivisesti
    Esim: potenssi(2, 5) = 32
    """
    # Perustapaus
    if eksponentti == 0:
        return 1
    
    # Rekursiivinen tapaus
    return kantaluku * potenssi(kantaluku, eksponentti - 1)

print(potenssi(2, 5))   # 32
print(potenssi(3, 4))   # 81
```

### 4. Listan summa

```python
def lista_summa(lista):
    """Laskee listan summan rekursiivisesti"""
    # Perustapaus: tyhjä lista
    if not lista:
        return 0
    
    # Rekursiivinen tapaus: ensimmäinen + loput
    return lista[0] + lista_summa(lista[1:])

print(lista_summa([1, 2, 3, 4, 5]))  # 15
```

### 5. Merkkijonon kääntäminen

```python
def käännä_merkkijono(s):
    """Kääntää merkkijonon rekursiivisesti"""
    # Perustapaus: tyhjä tai yhden merkin merkkijono
    if len(s) <= 1:
        return s
    
    # Rekursiivinen tapaus: viimeinen + käännetty alku
    return s[-1] + käännä_merkkijono(s[:-1])

print(käännä_merkkijono("Python"))  # nohtyP
```

### 6. Palindromi-tarkistus

```python
def on_palindromi(s):
    """Tarkistaa onko merkkijono palindromi rekursiivisesti"""
    # Poista välilyönnit ja muunna pieniksi
    s = s.lower().replace(" ", "")
    
    # Perustapaus: 0-1 merkkiä on aina palindromi
    if len(s) <= 1:
        return True
    
    # Tarkista että ensimmäinen == viimeinen
    if s[0] != s[-1]:
        return False
    
    # Rekursiivinen tapaus: tarkista keskiosa
    return on_palindromi(s[1:-1])

print(on_palindromi("saippuakivikauppias"))  # True
print(on_palindromi("Python"))               # False
print(on_palindromi("Anna"))                 # True
```

## Käytännön sovelluksia

### Sovellus 1: Hakemistorakenne

```python
import os

def tulosta_hakemisto(polku, sisennys=0):
    """
    Tulostaa hakemiston sisällön rekursiivisesti
    """
    try:
        # Listaa kaikki tiedostot ja kansiot
        for kohde in os.listdir(polku):
            kohde_polku = os.path.join(polku, kohde)
            
            # Tulosta sisennyksellä
            print("  " * sisennys + "📁 " + kohde if os.path.isdir(kohde_polku) else "  " * sisennys + "📄 " + kohde)
            
            # Jos kansio, tulosta sen sisältö rekursiivisesti
            if os.path.isdir(kohde_polku):
                tulosta_hakemisto(kohde_polku, sisennys + 1)
    
    except PermissionError:
        print("  " * sisennys + "❌ Ei oikeuksia")

# Käyttö
# tulosta_hakemisto(".")
```

### Sovellus 2: Hanoin tornit

```python
def hanoin_tornit(n, lähde="A", kohde="C", apu="B"):
    """
    Klassinen Hanoin tornit -ongelma
    Siirrä n kiekkoa lähteestä kohteeseen käyttäen apua
    """
    if n == 1:
        print(f"Siirrä kiekko 1: {lähde} → {kohde}")
        return
    
    # Siirrä n-1 kiekkoa lähteestä apuun
    hanoin_tornit(n - 1, lähde, apu, kohde)
    
    # Siirrä suurin kiekko lähteestä kohteeseen
    print(f"Siirrä kiekko {n}: {lähde} → {kohde}")
    
    # Siirrä n-1 kiekkoa avusta kohteeseen
    hanoin_tornit(n - 1, apu, kohde, lähde)

print("=== HANOIN TORNIT (3 kiekkoa) ===\n")
hanoin_tornit(3)
```

**Tulostus:**
```
=== HANOIN TORNIT (3 kiekkoa) ===

Siirrä kiekko 1: A → C
Siirrä kiekko 2: A → B
Siirrä kiekko 1: C → B
Siirrä kiekko 3: A → C
Siirrä kiekko 1: B → A
Siirrä kiekko 2: B → C
Siirrä kiekko 1: A → C
```

### Sovellus 3: Permutaatiot

```python
def permutaatiot(lista):
    """
    Luo kaikki permutaatiot (järjestysvaihdot) listasta
    Esim: [1, 2, 3] → [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    """
    # Perustapaus: tyhjä tai yksi alkio
    if len(lista) <= 1:
        return [lista]
    
    tulos = []
    
    # Ota jokainen alkio vuorollaan ensimmäiseksi
    for i in range(len(lista)):
        # Nykyinen alkio
        nykyinen = lista[i]
        
        # Loput alkiot
        loput = lista[:i] + lista[i+1:]
        
        # Rekursiivisesti permutaatiot lopuista
        for p in permutaatiot(loput):
            tulos.append([nykyinen] + p)
    
    return tulos

# Esimerkki
perm = permutaatiot([1, 2, 3])
print(f"Permutaatioita: {len(perm)}")
for p in perm:
    print(p)
```

### Sovellus 4: Labyrintin ratkaisu

```python
def ratkaise_labyrintti(labyrintti, x, y, polku=None):
    """
    Ratkaisee labyrintin rekursiivisesti (backtracking)
    0 = seinä, 1 = käytävä, 2 = maali
    """
    if polku is None:
        polku = []
    
    # Tarkista rajat
    if x < 0 or x >= len(labyrintti) or y < 0 or y >= len(labyrintti[0]):
        return None
    
    # Tarkista onko seinä tai jo käyty
    if labyrintti[x][y] == 0 or (x, y) in polku:
        return None
    
    # Lisää nykyinen kohta polkuun
    polku = polku + [(x, y)]
    
    # Tarkista onko maali
    if labyrintti[x][y] == 2:
        return polku
    
    # Kokeile kaikkia suuntia
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # oikea, alas, vasen, ylös
        ratkaisu = ratkaise_labyrintti(labyrintti, x + dx, y + dy, polku)
        if ratkaisu:
            return ratkaisu
    
    return None

# Esimerkki
labyrintti = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 2]
]

polku = ratkaise_labyrintti(labyrintti, 0, 0)
if polku:
    print("Ratkaisu löytyi!")
    print(f"Polku ({len(polku)} askelta): {polku}")
else:
    print("Ei ratkaisua")
```

### Sovellus 5: Fibonacci tehokkaasti (memoization)

```python
def fibonacci_memo(n, muisti=None):
    """
    Fibonacci memoization-tekniikalla
    Tallentaa lasketut arvot välttääkseen uudelleenlaskemisen
    """
    if muisti is None:
        muisti = {}
    
    # Tarkista onko jo laskettu
    if n in muisti:
        return muisti[n]
    
    # Perustapaukset
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Laske ja tallenna
    tulos = fibonacci_memo(n - 1, muisti) + fibonacci_memo(n - 2, muisti)
    muisti[n] = tulos
    
    return tulos

# Vertailu: naiivi vs. memoization
import time

# Naiivi (hidas)
alku = time.time()
print(f"Fibonacci(35) naiivi: {fibonacci(35)}")
print(f"Aika: {time.time() - alku:.4f}s")

# Memoization (nopea)
alku = time.time()
print(f"Fibonacci(35) memo: {fibonacci_memo(35)}")
print(f"Aika: {time.time() - alku:.6f}s")
```

## Yhteenveto

### Mitä opimme?

**Algoritmit**
- Vaiheittainen ohje ongelman ratkaisemiseen
- Hyvä algoritmi on selkeä, äärellinen, tehokas ja oikea
- Esimerkkejä: haku, järjestäminen, summa

**Pseudokoodi**
- Kieliriippumaton tapa kuvata algoritmia
- Keskittyy logiikkaan, ei syntaksiin
- Helppo muuttaa ohjelmakoodiksi

**Aikakompleksisuus**
- Big O -notaatio kuvaa algoritmin tehokkuutta
- O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- Valitse tehokas algoritmi suurille datamäärille

**Rekursio**
- Funktio kutsuu itseään
- Vaatii perustapauksen (base case)
- Hyödyllinen puu- ja graafiongelmiin
- Voi olla hitaampi kuin iteraatio

### Tärkeät algoritmit muistiin

| Algoritmi | Aikakompleksisuus | Käyttö |
|-----------|-------------------|--------|
| **Lineaarihaku** | O(n) | Järjestämätön data |
| **Binäärihaku** | O(log n) | Järjestetty data |
| **Kuplajärjestäminen** | O(n²) | Pieni data, opetus |
| **Merge Sort** | O(n log n) | Suuri data |
| **Rekursio** | Vaihtelee | Puu/graafirakenteet |

### Rekursion muistilista

✅ **Tarvitset:**
1. **Perustapauksen** - Milloin lopettaa?
2. **Rekursiivisen tapauksen** - Miten ongelma pienenee?
3. **Edistymisen** - Kohti perustapaus

✅ **Hyvä käyttää kun:**
- Ongelma on luonnostaan rekursiivinen
- Koodi on selkeämpi
- Datamäärä ei ole valtava

❌ **Vältä kun:**
- Yksinkertainen silmukka riittää
- Suorituskyky on kriittistä
- Riski stack overflow -virheelle

### Harjoitustehtäviä

1. **Binäärihaku**: Toteuta binäärihaku sekä iteratiivisesti että rekursiivisesti

2. **Fibonacci vertailu**: Vertaa naiivia ja memoization-Fibonacci-toteutuksia

3. **Palindromi**: Tarkista onko merkkijono palindromi (sekä iteratiivisesti että rekursiivisesti)

4. **Järjestäminen**: Toteuta yksinkertainen järjestämisalgoritmi

5. **Summa**: Laske listan summa kolmella tavalla: silmukka, rekursio, sum()-funktio

6. **Potenssilasku**: Tee tehokas potenssilaskualgoritmi O(log n) kompleksisuudella

7. **Permutaatiot**: Generoi kaikki permutaatiot annetusta listasta

Muista: Paras algoritmi riippuu ongelmasta - ei ole yhtä "parasta" ratkaisua kaikkeen! 🚀

## Seuraavaksi
Siirry [Harjoitukset](Harjoitukset/)-kansioon ja tee luvun tehtävät.