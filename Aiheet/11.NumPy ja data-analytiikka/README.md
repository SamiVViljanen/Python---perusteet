# NumPy ja data-analytiikan perusteet

## Sisällysluettelo
1. [Mikä on NumPy?](#mikä-on-numpy)
2. [NumPy:n asentaminen](#numpyn-asentaminen)
3. [NumPy-taulukot (arrays)](#numpy-taulukot-arrays)
4. [Taulukoiden operaatiot](#taulukoiden-operaatiot)
5. [Matriisioperaatiot](#matriisioperaatiot)
6. [Tilastolliset funktiot](#tilastolliset-funktiot)
7. [Data-analytiikan perusteet](#data-analytiikan-perusteet)
8. [Käytännön sovelluksia](#käytännön-sovelluksia)
9. [Yhteenveto](#yhteenveto)

---

Tässä oppaassa opit NumPy-kirjaston perusteet ja miten sitä käytetään data-analytiikassa.

## Mikä on NumPy?

**NumPy** (Numerical Python) on Pythonin kirjasto, joka on suunniteltu numeeriseen laskentaan. Se on **perusta** lähes kaikelle tieteelliselle laskennalle Pythonissa.

### Miksi käyttää NumPy:tä?

```python
# Tavallinen Python-lista
lista = [1, 2, 3, 4, 5]
# lista * 2  # Tämä vain monistaa listan! [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# NumPy-taulukko
import numpy as np
taulukko = np.array([1, 2, 3, 4, 5])
tulos = taulukko * 2  # Jokainen alkio kerrotaan 2:lla!
print(tulos)  # [2 4 6 8 10]
```

**NumPy:n edut:**
- ✅ **Nopeus** - 10-100x nopeampi kuin Python-listat
- ✅ **Vähemmän muistia** - tehokkaampi tallennustapa
- ✅ **Vektorisointi** - operaatiot koko taulukolle kerralla
- ✅ **Matriisioperaatiot** - lineaarialgebra helposti
- ✅ **Tilastofunktiot** - valmiit keskiarvo, mediaani, jne.

### Milloin käyttää NumPy:tä?

- 📊 Data-analytiikka ja tilastot
- 🔬 Tieteellinen laskenta
- 🤖 Koneoppiminen ja tekoäly
- 📈 Signaalinkäsittely
- 🎨 Kuvankäsittely
- 🧮 Matriisit ja lineaarialgebra

## NumPy:n asentaminen

NumPy täytyy asentaa erikseen, koska se ei kuulu Pythonin vakiokirjastoihin.

### Asennus

```bash
# Windows (PowerShell tai Command Prompt)
pip install numpy

# Mac/Linux
pip3 install numpy

# Tai Jos käytät Anacondaa
conda install numpy
```

### Tarkista asennus

```python
import numpy as np

print(np.__version__)  # Esim. 1.24.3
print("NumPy toimii!")
```

## NumPy-taulukot (arrays)

NumPy:n perusta on **array** (taulukko) - tehokas ja nopea tietorakenne numeroille.

### Taulukon luominen

```python
import numpy as np

# Listasta
lista = [1, 2, 3, 4, 5]
taulukko = np.array(lista)
print(taulukko)  # [1 2 3 4 5]

# Suoraan arvoista
taulukko = np.array([10, 20, 30, 40, 50])
print(taulukko)

# Tietotyypin määrittely
kokonaisluvut = np.array([1, 2, 3], dtype=int)
liukuluvut = np.array([1.0, 2.0, 3.0], dtype=float)

print(kokonaisluvut.dtype)  # int64 (tai int32)
print(liukuluvut.dtype)     # float64
```

### Erikoiset taulukot

```python
# Nollilla täytetty taulukko
nollat = np.zeros(5)
print(nollat)  # [0. 0. 0. 0. 0.]

# Ykkösillä täytetty taulukko
ykköset = np.ones(5)
print(ykköset)  # [1. 1. 1. 1. 1.]

# Lukualue
alue = np.arange(0, 10, 2)  # alku, loppu, askel
print(alue)  # [0 2 4 6 8]

# Tasavälinen lukualue
tasaväli = np.linspace(0, 10, 5)  # alku, loppu, montako lukua
print(tasaväli)  # [ 0.   2.5  5.   7.5 10. ]

# Satunnaiset luvut
satunnaiset = np.random.random(5)  # 0-1 välillä
print(satunnaiset)  # [0.5488135  0.71518937 0.60276338 ...]

# Satunnaiset kokonaisluvut
kokonaisluvut = np.random.randint(1, 100, size=5)  # 1-99 välillä
print(kokonaisluvut)  # [44 47 64 67 67]
```

### Kaksiulotteiset taulukot (matriisit)

```python
# 2D-taulukko (matriisi)
matriisi = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matriisi)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Muoto (shape)
print(matriisi.shape)  # (3, 3) - 3 riviä, 3 saraketta

# Koko
print(matriisi.size)   # 9 alkiota

# Ulottuvuudet
print(matriisi.ndim)   # 2 ulottuvuutta

# Erikoiset 2D-taulukot
nollat_2d = np.zeros((3, 4))  # 3 riviä, 4 saraketta
print(nollat_2d)

yksikkömatriisi = np.eye(3)  # Identiteettimatriisi
print(yksikkömatriisi)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

### Taulukon indeksointi

```python
taulukko = np.array([10, 20, 30, 40, 50])

# Yksittäinen alkio
print(taulukko[0])   # 10
print(taulukko[-1])  # 50

# Ositus (slicing)
print(taulukko[1:4])   # [20 30 40]
print(taulukko[:3])    # [10 20 30]
print(taulukko[2:])    # [30 40 50]

# 2D-indeksointi
matriisi = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matriisi[0, 0])    # 1 (rivi 0, sarake 0)
print(matriisi[1, 2])    # 6 (rivi 1, sarake 2)
print(matriisi[0])       # [1 2 3] (koko ensimmäinen rivi)
print(matriisi[:, 0])    # [1 4 7] (ensimmäinen sarake)
print(matriisi[0:2, 1:3]) # [[2 3]  (rivit 0-1, sarakkeet 1-2)
                          #  [5 6]]
```

## Taulukoiden operaatiot

### Perustoiminnot

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Yhteenlasku
print(a + b)  # [11 22 33 44 55]

# Vähennyslasku
print(b - a)  # [ 9 18 27 36 45]

# Kertolasku (alkioittain!)
print(a * b)  # [ 10  40  90 160 250]

# Jakolasku
print(b / a)  # [10. 10. 10. 10. 10.]

# Potenssi
print(a ** 2)  # [ 1  4  9 16 25]

# Neliöjuuri
print(np.sqrt(a))  # [1.         1.41421356 1.73205081 2.         2.23606798]
```

### Skalaarioperaatiot

```python
a = np.array([1, 2, 3, 4, 5])

# Lisää 10 jokaiseen
print(a + 10)  # [11 12 13 14 15]

# Kerro 2:lla
print(a * 2)   # [ 2  4  6  8 10]

# Jaa 2:lla
print(a / 2)   # [0.5 1.  1.5 2.  2.5]

# Potenssi
print(a ** 3)  # [  1   8  27  64 125]
```

### Vertailuoperaatiot

```python
a = np.array([1, 2, 3, 4, 5])

# Vertailu
print(a > 3)   # [False False False  True  True]
print(a == 3)  # [False False  True False False]
print(a <= 2)  # [ True  True False False False]

# Ehdollinen suodatus
suuremmat = a[a > 3]
print(suuremmat)  # [4 5]

# Monimutkainen ehto
valilla = a[(a >= 2) & (a <= 4)]
print(valilla)  # [2 3 4]
```

### Matemaattiset funktiot

```python
a = np.array([1, 4, 9, 16, 25])

# Neliöjuuri
print(np.sqrt(a))  # [1. 2. 3. 4. 5.]

# Luonnollinen logaritmi
print(np.log(a))

# Kymmenkantainen logaritmi
print(np.log10(a))

# Eksponenttifunktio
print(np.exp([1, 2, 3]))  # [2.71828183  7.3890561  20.08553692]

# Trigonometriset funktiot (radiaaneissa)
kulmat = np.array([0, np.pi/2, np.pi])
print(np.sin(kulmat))  # [0.0000000e+00 1.0000000e+00 1.2246468e-16]
print(np.cos(kulmat))  # [ 1.000000e+00  6.123234e-17 -1.000000e+00]

# Pyöristys
luvut = np.array([1.2, 2.5, 3.7, 4.9])
print(np.round(luvut))   # [1. 2. 4. 5.]
print(np.floor(luvut))   # [1. 2. 3. 4.]
print(np.ceil(luvut))    # [2. 3. 4. 5.]
```

## Matriisioperaatiot

### Matriisin luominen

```python
# 2x3 matriisi
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 3x2 matriisi
B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

print(f"A:n muoto: {A.shape}")  # (2, 3)
print(f"B:n muoto: {B.shape}")  # (3, 2)
```

### Matriisin transpoosi

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Transpoosi (rivit ↔ sarakkeet)
A_T = A.T
print(A_T)
# [[1 4]
#  [2 5]
#  [3 6]]

print(f"Alkuperäinen: {A.shape}")   # (2, 3)
print(f"Transpoosi: {A_T.shape}")   # (3, 2)
```

### Matriisien kertolasku

```python
# Matriisien kertolasku (lineaarialgebra)
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matriisitulo
C = np.dot(A, B)
# TAI
C = A @ B  # Python 3.5+

print(C)
# [[19 22]
#  [43 50]]

# HUOM: Eri kuin alkioittainen kertolasku!
alkioittain = A * B
print(alkioittain)
# [[ 5 12]
#  [21 32]]
```

### Determinantti ja käänteismatriisi

```python
A = np.array([
    [1, 2],
    [3, 4]
])

# Determinantti
det = np.linalg.det(A)
print(f"Determinantti: {det}")  # -2.0

# Käänteismatriisi
try:
    A_inv = np.linalg.inv(A)
    print("Käänteismatriisi:")
    print(A_inv)
    
    # Tarkistus: A * A^-1 = I (identiteettimatriisi)
    tarkistus = A @ A_inv
    print(np.round(tarkistus))  # [[1. 0.] [0. 1.]]
except np.linalg.LinAlgError:
    print("Matriisi ei ole kääntyvä")
```

### Ominaisarvot

```python
A = np.array([
    [1, 2],
    [2, 1]
])

# Ominaisarvot ja ominaisvektorit
ominaisarvot, ominaisvektorit = np.linalg.eig(A)

print("Ominaisarvot:", ominaisarvot)
print("Ominaisvektorit:")
print(ominaisvektorit)
```

## Tilastolliset funktiot

### Perustilastot

```python
data = np.array([12, 15, 18, 20, 22, 25, 28, 30, 35, 40])

# Keskiarvo
keskiarvo = np.mean(data)
print(f"Keskiarvo: {keskiarvo}")  # 24.5

# Mediaani
mediaani = np.median(data)
print(f"Mediaani: {mediaani}")  # 23.5

# Keskihajonta
keskihajonta = np.std(data)
print(f"Keskihajonta: {keskihajonta:.2f}")  # 8.46

# Varianssi
varianssi = np.var(data)
print(f"Varianssi: {varianssi:.2f}")  # 71.65

# Minimi ja maksimi
print(f"Minimi: {np.min(data)}")  # 12
print(f"Maksimi: {np.max(data)}")  # 40

# Summa
print(f"Summa: {np.sum(data)}")  # 245

# Kumulatiivinen summa
kum_summa = np.cumsum(data)
print(f"Kumulatiivinen summa: {kum_summa}")
```

### 2D-datan tilastot

```python
matriisi = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Kaikki alkiot
print(f"Keskiarvo (kaikki): {np.mean(matriisi)}")  # 5.0

# Riveittäin (axis=1)
rivien_ka = np.mean(matriisi, axis=1)
print(f"Rivien keskiarvot: {rivien_ka}")  # [2. 5. 8.]

# Sarakkeittain (axis=0)
sarakkeiden_ka = np.mean(matriisi, axis=0)
print(f"Sarakkeiden keskiarvot: {sarakkeiden_ka}")  # [4. 5. 6.]

# Muut funktiot toimivat samalla tavalla
print(f"Rivien summat: {np.sum(matriisi, axis=1)}")     # [ 6 15 24]
print(f"Sarakkeiden maks: {np.max(matriisi, axis=0)}")  # [7 8 9]
```

### Korrelaatio ja kovarianssi

```python
# Kaksi datasettiä
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Korrelaatiokerroin (-1 ... 1)
korrelaatio = np.corrcoef(x, y)
print("Korrelaatiomatriisi:")
print(korrelaatio)
# [[1.         0.82807867]
#  [0.82807867 1.        ]]

# Kovarianssi
kovarianssi = np.cov(x, y)
print("Kovarianssimatriisi:")
print(kovarianssi)
```

### Persentiilit

```python
data = np.array([12, 15, 18, 20, 22, 25, 28, 30, 35, 40])

# Kvartiilit
Q1 = np.percentile(data, 25)   # 1. kvartiili
Q2 = np.percentile(data, 50)   # Mediaani
Q3 = np.percentile(data, 75)   # 3. kvartiili

print(f"Q1 (25%): {Q1}")  # 18.75
print(f"Q2 (50%): {Q2}")  # 23.5
print(f"Q3 (75%): {Q3}")  # 29.25

# Kvartiiliväli (IQR)
IQR = Q3 - Q1
print(f"IQR: {IQR}")  # 10.5
```

## Data-analytiikan perusteet

### Datan lataaminen ja tallentaminen

```python
# Tallenna taulukko tiedostoon
data = np.array([1, 2, 3, 4, 5])
np.save('data.npy', data)  # NumPy-muoto (binääri)
np.savetxt('data.txt', data)  # Teksti

# Lataa taulukko
ladattu = np.load('data.npy')
ladattu_txt = np.loadtxt('data.txt')

# CSV-tiedosto
data_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
np.savetxt('data.csv', data_2d, delimiter=',')
ladattu_csv = np.loadtxt('data.csv', delimiter=',')
```

### Datan puhdistus

```python
# Data puuttuvilla arvoilla (NaN)
data = np.array([1.0, 2.0, np.nan, 4.0, 5.0, np.nan, 7.0])

# Tarkista puuttuvat arvot
on_nan = np.isnan(data)
print(f"NaN-indeksit: {on_nan}")  # [False False  True False False  True False]

# Poista NaN-arvot
puhdas_data = data[~np.isnan(data)]
print(f"Puhdas data: {puhdas_data}")  # [1. 2. 4. 5. 7.]

# Korvaa NaN-arvot keskiarvolla
keskiarvo = np.nanmean(data)  # Laskee keskiarvon ohittaen NaN
data_korjattu = np.where(np.isnan(data), keskiarvo, data)
print(f"Korjattu data: {data_korjattu}")
```

### Datan normalisointi

```python
data = np.array([10, 20, 30, 40, 50])

# Min-Max normalisointi (0-1 välille)
min_val = np.min(data)
max_val = np.max(data)
normalisoitu = (data - min_val) / (max_val - min_val)
print(f"Normalisoitu (0-1): {normalisoitu}")
# [0.   0.25 0.5  0.75 1.  ]

# Z-score normalisointi (keskiarvo=0, keskihajonta=1)
keskiarvo = np.mean(data)
keskihajonta = np.std(data)
z_score = (data - keskiarvo) / keskihajonta
print(f"Z-score: {z_score}")
# [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]
```

### Datan ryhmittely ja aggregointi

```python
# Opiskelijan pisteet eri kokeista
kokeet = np.array([
    [85, 90, 78],  # Opiskelija 1
    [92, 88, 95],  # Opiskelija 2
    [78, 85, 80],  # Opiskelija 3
    [95, 92, 98]   # Opiskelija 4
])

# Jokaisen opiskelijan keskiarvo
opiskelija_ka = np.mean(kokeet, axis=1)
print("Opiskelijoiden keskiarvot:", opiskelija_ka)
# [84.33 91.67 81.00 95.00]

# Jokaisen kokeen keskiarvo
koe_ka = np.mean(kokeet, axis=0)
print("Kokeiden keskiarvot:", koe_ka)
# [87.5  88.75 87.75]

# Paras tulos jokaisessa kokeessa
parhaat = np.max(kokeet, axis=0)
print("Parhaat tulokset:", parhaat)
# [95 92 98]

# Kuka sai parhaan kokonaispistemäärän?
kokonaispisteet = np.sum(kokeet, axis=1)
paras_opiskelija = np.argmax(kokonaispisteet)
print(f"Paras opiskelija: {paras_opiskelija + 1}")  # 4
```

## Käytännön sovelluksia

### Sovellus 1: Lämpötiladatan analyysi

```python
def analysoi_lämpötilat():
    """Analysoi lämpötiladata"""
    # Simuloidaan viikon lämpötilat (7 päivää)
    np.random.seed(42)  # Toistettavuus
    lämpötilat = np.random.normal(20, 5, 7)  # Keskiarvo 20, hajonta 5
    
    print("=== LÄMPÖTILAANALYYSI ===\n")
    
    päivät = ["Ma", "Ti", "Ke", "To", "Pe", "La", "Su"]
    
    print("Lämpötilat:")
    for i, (päivä, lämpö) in enumerate(zip(päivät, lämpötilat)):
        print(f"{päivä}: {lämpö:.1f}°C")
    
    print(f"\nKeskiarvo: {np.mean(lämpötilat):.1f}°C")
    print(f"Mediaani: {np.median(lämpötilat):.1f}°C")
    print(f"Keskihajonta: {np.std(lämpötilat):.1f}°C")
    print(f"Minimi: {np.min(lämpötilat):.1f}°C")
    print(f"Maksimi: {np.max(lämpötilat):.1f}°C")
    
    # Kuumimmat päivät
    kuuma_raja = np.mean(lämpötilat) + np.std(lämpötilat)
    kuumat_päivät = lämpötilat > kuuma_raja
    
    if np.any(kuumat_päivät):
        print(f"\nKuumat päivät (yli {kuuma_raja:.1f}°C):")
        for päivä, on_kuuma in zip(päivät, kuumat_päivät):
            if on_kuuma:
                print(f"  - {päivä}")

analysoi_lämpötilat()
```

### Sovellus 2: Opintosuoritusten tilastointi

```python
def analysoi_opintosuoritukset():
    """Analysoi opiskelijoiden suorituksia"""
    # Opiskelijat x Kurssit
    pisteet = np.array([
        [85, 90, 78, 92, 88],  # Opiskelija 1
        [92, 88, 95, 90, 94],  # Opiskelija 2
        [78, 85, 80, 75, 82],  # Opiskelija 3
        [95, 92, 98, 96, 93],  # Opiskelija 4
        [70, 75, 72, 78, 76],  # Opiskelija 5
    ])
    
    opiskelijat = ["Anna", "Pekka", "Liisa", "Matti", "Kaisa"]
    kurssit = ["Python", "Java", "C++", "SQL", "Web"]
    
    print("=== OPINTOSUORITUSTEN ANALYYSI ===\n")
    
    # Jokaisen opiskelijan keskiarvo
    print("Opiskelijoiden keskiarvot:")
    for nimi, ka in zip(opiskelijat, np.mean(pisteet, axis=1)):
        print(f"  {nimi}: {ka:.1f}")
    
    # Kurssien keskiarvot
    print("\nKurssien keskiarvot:")
    for kurssi, ka in zip(kurssit, np.mean(pisteet, axis=0)):
        print(f"  {kurssi}: {ka:.1f}")
    
    # Paras opiskelija
    paras_idx = np.argmax(np.mean(pisteet, axis=1))
    print(f"\n🏆 Paras keskiarvo: {opiskelijat[paras_idx]}")
    
    # Vaikein kurssi (alhaisin keskiarvo)
    vaikein_idx = np.argmin(np.mean(pisteet, axis=0))
    print(f"📚 Vaikein kurssi: {kurssit[vaikein_idx]}")
    
    # Yleinen tilasto
    print(f"\nYleinen keskiarvo: {np.mean(pisteet):.1f}")
    print(f"Keskihajonta: {np.std(pisteet):.1f}")
    print(f"Korkein pistemäärä: {np.max(pisteet)}")
    print(f"Alhaisin pistemäärä: {np.min(pisteet)}")

analysoi_opintosuoritukset()
```

### Sovellus 3: Yksinkertainen lineaarinen regressio

```python
def lineaarinen_regressio(x, y):
    """
    Laskee yksinkertaisen lineaarisen regression y = ax + b
    """
    n = len(x)
    
    # Laske kulmakerroin (a) ja vakiotermi (b)
    a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
        (n * np.sum(x**2) - np.sum(x)**2)
    b = (np.sum(y) - a * np.sum(x)) / n
    
    return a, b

# Esimerkki: Opiskeluaika vs. Pisteet
opiskeluaika = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # Tunnit
pisteet = np.array([45, 55, 60, 65, 75, 80, 85, 90])

a, b = lineaarinen_regressio(opiskeluaika, pisteet)

print("=== LINEAARINEN REGRESSIO ===\n")
print(f"Yhtälö: y = {a:.2f}x + {b:.2f}")
print(f"\nTulkinta:")
print(f"- Jokainen opiskelutunti nostaa pisteitä {a:.2f}")
print(f"- Ilman opiskelua pistemäärä olisi {b:.2f}")

# Ennuste
uusi_aika = 10
ennuste = a * uusi_aika + b
print(f"\nEnnuste: {uusi_aika}h opiskelulla → {ennuste:.1f} pistettä")

# Korrelaatio
korrelaatio = np.corrcoef(opiskeluaika, pisteet)[0, 1]
print(f"Korrelaatio: {korrelaatio:.3f}")
```

### Sovellus 4: Portfolion analyysi

```python
def analysoi_portfolio():
    """Analysoi sijoitusportfolion tuottoja"""
    # 5 osaketta, 12 kuukautta
    np.random.seed(42)
    
    # Simuloi kuukausittaiset tuotot (%)
    osakkeet = ["Apple", "Google", "Microsoft", "Amazon", "Tesla"]
    tuotot = np.random.normal(1.5, 3, (12, 5))  # Keskiarvo 1.5%, hajonta 3%
    
    print("=== PORTFOLIOANALYYSI ===\n")
    
    # Kokonaistuotto per osake
    kumulatiiviset = np.prod(1 + tuotot/100, axis=0) - 1
    print("Vuosituotto osakkeittain:")
    for osake, tuotto in zip(osakkeet, kumulatiiviset * 100):
        print(f"  {osake}: {tuotto:+.2f}%")
    
    # Keskimääräinen kuukausituotto
    print("\nKeskimääräinen kuukausituotto:")
    for osake, ka in zip(osakkeet, np.mean(tuotot, axis=0)):
        print(f"  {osake}: {ka:+.2f}%")
    
    # Volatiliteetti (riski)
    print("\nVolatiliteetti (keskihajonta):")
    for osake, vol in zip(osakkeet, np.std(tuotot, axis=0)):
        print(f"  {osake}: {vol:.2f}%")
    
    # Paras ja huonoin osake
    paras_idx = np.argmax(kumulatiiviset)
    huonoin_idx = np.argmin(kumulatiiviset)
    
    print(f"\n🏆 Paras osake: {osakkeet[paras_idx]}")
    print(f"📉 Huonoin osake: {osakkeet[huonoin_idx]}")
    
    # Hajautettu portfolio (tasapainossa)
    portfolio_tuotto = np.mean(kumulatiiviset) * 100
    print(f"\n💼 Tasapainoinen portfolion tuotto: {portfolio_tuotto:+.2f}%")

analysoi_portfolio()
```

### Sovellus 5: Kuvan käsittely matriiseilla

```python
def luo_yksinkertainen_kuva():
    """Luo ja käsittele yksinkertainen 'kuva' (matriisi)"""
    # 10x10 "kuva" (harmaasävy 0-255)
    kuva = np.random.randint(0, 256, (10, 10))
    
    print("=== KUVANKÄSITTELY ===\n")
    print("Alkuperäinen kuva (pieni osa):")
    print(kuva[:5, :5])  # Näytä vain kulma
    
    # Tilastot
    print(f"\nKirkkauden keskiarvo: {np.mean(kuva):.1f}")
    print(f"Minimi (tummin): {np.min(kuva)}")
    print(f"Maksimi (kirkkain): {np.max(kuva)}")
    
    # Kirkkauden säätö
    kirkkaampi = np.clip(kuva + 50, 0, 255)  # Lisää 50, pidä 0-255
    tummempi = np.clip(kuva - 50, 0, 255)
    
    print(f"\nKirkkaampi keskiarvo: {np.mean(kirkkaampi):.1f}")
    print(f"Tummempi keskiarvo: {np.mean(tummempi):.1f}")
    
    # Kontrasti
    kontrasti = (kuva - np.mean(kuva)) * 1.5 + np.mean(kuva)
    kontrasti = np.clip(kontrasti, 0, 255)
    
    print(f"Kontrastin lisäys tehty!")
    
    # Binäärikuva (kynnysarvo)
    kynnys = 128
    binääri = (kuva > kynnys) * 255
    print(f"\nBinäärikuva (kynnys {kynnys}): {np.sum(binääri > 0)} valkoista pikseliä")

luo_yksinkertainen_kuva()
```

## Yhteenveto

### Mitä opimme?

**NumPy-perusteet**
- `np.array()` - Luo taulukko
- `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()` - Erikoistaulukot
- Indeksointi ja ositus - kuten listat, mutta tehokkaammin
- Muoto (shape), koko (size), ulottuvuudet (ndim)

**Operaatiot**
- Aritmetiikka: `+`, `-`, `*`, `/`, `**`
- Vektorisointi: operaatiot koko taulukolle
- Vertailu: `>`, `<`, `==` → Boolean-taulukko
- Matemaattiset funktiot: `np.sqrt()`, `np.log()`, `np.sin()`

**Matriisit**
- 2D-taulukot: rivit ja sarakkeet
- Transpoosi: `.T`
- Matriisitulo: `np.dot()` tai `@`
- Lineaarialgebra: determinantti, käänteismatriisi, ominaisarvot

**Tilastot**
- Keskiarvot: `np.mean()`, `np.median()`
- Hajonnat: `np.std()`, `np.var()`
- Min/Max: `np.min()`, `np.max()`
- Korrelaatio: `np.corrcoef()`
- Persentiilit: `np.percentile()`

**Data-analytiikka**
- Datan lataaminen/tallentaminen
- Puuttuvat arvot (NaN)
- Normalisointi
- Aggregointi (axis)

### NumPy vs. Python-lista

| Ominaisuus | Python-lista | NumPy-array |
|-----------|--------------|-------------|
| **Nopeus** | Hidas | Nopea (10-100x) |
| **Muisti** | Enemmän | Vähemmän |
| **Operaatiot** | Rajoitetut | Laajat |
| **Tietotyypit** | Sekoitetut | Yhtenäinen |
| **Ulottuvuudet** | 1D | Moni-ulotteinen |
| **Käyttö** | Yleiskäyttö | Numeeriset laskelmat |

### Milloin käyttää NumPy:tä?

✅ **Käytä NumPy:tä kun:**
- Teet numeroiden kanssa paljon laskutoimituksia
- Tarvitset moniulotteisia taulukoita
- Haluat nopeutta ja tehokkuutta
- Teet tilastollista analyysiä
- Käsittelet matriiseja

❌ **Älä käytä NumPy:tä kun:**
- Käsittelet pääasiassa merkkijonoja
- Tarvitset dynaamista kokoa
- Data on epäyhtenäistä (eri tyyppejä)
- Yksinkertaiset operaatiot riittävät

### Tärkeimmät funktiot muistiin

```python
# Luonti
np.array([1, 2, 3])
np.zeros((3, 4))
np.arange(0, 10, 2)
np.random.random(5)

# Tilastot
np.mean(data)
np.median(data)
np.std(data)
np.min(data), np.max(data)

# Operaatiot
data + 10
data * 2
np.sqrt(data)
data[data > 5]

# Matriisit
matrix.T
np.dot(A, B) tai A @ B
np.linalg.inv(A)
```

### Jatkokehitys

Kun hallitset NumPy:n, voit oppia:
- **Pandas** - Datan käsittely ja analyysi (DataFrame)
- **Matplotlib** - Datan visualisointi
- **SciPy** - Tieteellinen laskenta
- **Scikit-learn** - Koneoppiminen

NumPy on pohja näille kaikille! 🚀

## Seuraavaksi
Siirry [Harjoitukset](Harjoitukset/)-kansioon ja tee luvun tehtävät.