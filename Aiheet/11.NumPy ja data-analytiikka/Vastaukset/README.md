# Vastaukset: NumPy ja data-analytiikka

Tässä kansiossa on ratkaisut NumPy-harjoituksiin.

---

## Harjoitus 1: NumPy-taulukon perusteet ⭐

**Tavoite:** Oppia luomaan NumPy-taulukoita ja tekemään perusoperaatioita.

### Ratkaisu

```python
import numpy as np

# 1. Luo taulukko
taulukko = np.array([10, 20, 30, 40, 50])

# 2. Tulosta taulukko
print(f"Alkuperäinen taulukko: {taulukko}")

# 3. Tulosta ensimmäinen ja viimeinen
print(f"Ensimmäinen: {taulukko[0]}")
print(f"Viimeinen: {taulukko[-1]}")

# 4. Kerro kahdella
kerrottu = taulukko * 2
print(f"Kerrottuna kahdella: {kerrottu}")

# 5. Luo toinen taulukko
taulukko2 = np.array([1, 2, 3, 4, 5])
print(f"Toinen taulukko: {taulukko2}")

# 6. Laske summa
summa = taulukko + taulukko2

# 7. Tulosta tulos
print(f"Summa: {summa}")
```

### Keskeiset oppipisteet

1. **NumPy-taulukon luominen:** `np.array([...])`
2. **Vektorisointi:** Operaatiot koskevat kaikkia alkioita kerralla
3. **Indeksointi:** Toimii kuten listoissa (`[0]`, `[-1]`)
4. **Alkioittainen laskenta:** `taulukko1 + taulukko2` laskee parisuunnassa

### Vaihtoehtoiset tavat

```python
# Luominen range-tyyppisesti
taulukko = np.arange(10, 60, 10)  # [10, 20, 30, 40, 50]

# Luominen linspace-funktiolla
taulukko = np.linspace(10, 50, 5)  # 5 arvoa välillä 10-50

# Koko taulukon skaalaus
kerrottu = taulukko * 2
# tai
kerrottu = np.multiply(taulukko, 2)
```

### Yleisiä virheitä

❌ **Virhe:** Tavallinen lista aritmetiikassa
```python
lista = [10, 20, 30]
lista * 2  # Toistaa listan: [10, 20, 30, 10, 20, 30]
```

✅ **Oikein:** NumPy-taulukko
```python
taulukko = np.array([10, 20, 30])
taulukko * 2  # Kertoo alkiot: [20, 40, 60]
```

---

## Harjoitus 2: Tilastofunktiot ⭐⭐

**Tavoite:** Oppia käyttämään NumPyn tilastofunktioita datan analysointiin.

### Ratkaisu

```python
import numpy as np

lampotilat_lista = [15.5, 18.2, 16.8, 20.1, 19.5, 17.3, 21.0]
lampotilat = np.array(lampotilat_lista)

print(f"Lämpötilat: {lampotilat}")

# Tilastot
keskiarvo = np.mean(lampotilat)
mediaani = np.median(lampotilat)
keskihajonta = np.std(lampotilat)
minimi = np.min(lampotilat)
maksimi = np.max(lampotilat)

print(f"Keskiarvo: {keskiarvo:.2f}°C")
print(f"Mediaani: {mediaani:.2f}°C")
print(f"Keskihajonta: {keskihajonta:.2f}°C")
print(f"Minimi: {minimi:.2f}°C")
print(f"Maksimi: {maksimi:.2f}°C")

# Suodatus
yli_18 = lampotilat > 18
paivien_maara = np.sum(yli_18)
print(f"Yli 18°C päiviä: {paivien_maara}")

lampimät_paivat = lampotilat[yli_18]
print(f"Lämpimät päivät: {lampimät_paivat}")
```

### Keskeiset oppipisteet

1. **Tilastofunktiot:** `mean()`, `median()`, `std()`, `min()`, `max()`
2. **Boolean-indeksointi:** `lampotilat > 18` luo True/False-taulukon
3. **Suodatus:** `lampotilat[lampotilat > 18]` palauttaa ehdot täyttävät
4. **Laskenta:** `np.sum(boolean_array)` laskee True-arvojen määrän

### Vaihtoehtoiset tavat

```python
# Varianssi
varianssi = np.var(lampotilat)

# Prosenttipisteet (kvartiilit)
q1 = np.percentile(lampotilat, 25)
q3 = np.percentile(lampotilat, 75)

# Lukumäärä suoraan
paivien_maara = len(lampotilat[lampotilat > 18])

# Indeksit lämpimille päiville
lampimät_indeksit = np.where(lampotilat > 18)[0]
```

### Yleisiä virheitä

❌ **Virhe:** Käytetään Pythonin sum():ia
```python
keskiarvo = sum(lampotilat) / len(lampotilat)  # Toimii, mutta hidas
```

✅ **Oikein:** NumPyn mean()
```python
keskiarvo = np.mean(lampotilat)  # Optimoitu, nopea
```

---

## Harjoitus 3: Matriisioperaatiot ⭐⭐

**Tavoite:** Oppia käsittelemään 2D-taulukoita (matriiseja).

### Ratkaisu

```python
import numpy as np

# Matriisit
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

print("Matriisi A:")
print(A)
print("\nMatriisi B:")
print(B)

# Operaatiot
summa = A + B
print("\nA + B:")
print(summa)

erotus = A - B
print("\nA - B:")
print(erotus)

kerrottu = A * 3
print("\nA * 3:")
print(kerrottu)

transpoosi = A.T
print("\nA transpoosi:")
print(transpoosi)

# Matriisitulo
C = np.array([[1, 2], [3, 4], [5, 6]])
tulo = np.dot(A, C)
print("\nMatriisitulo A × C:")
print(tulo)
```

### Keskeiset oppipisteet

1. **2D-taulukko:** `np.array([[rivi1], [rivi2]])`
2. **Alkioittaiset operaatiot:** `+`, `-`, `*` toimivat parisuunnassa
3. **Transpoosi:** `.T` kääntää rivit sarakkeiksi
4. **Matriisitulo:** `np.dot(A, C)` tai `A @ C`
5. **Dimensiot:** A(m×n) × C(n×p) → tulos(m×p)

### Vaihtoehtoiset tavat

```python
# Matriisiluonti
A = np.array([[1, 2, 3], [4, 5, 6]])
# tai
A = np.zeros((2, 3))  # 2×3 nollamatriisi
A = np.ones((2, 3))   # 2×3 ykkösmatriisi
A = np.eye(3)         # 3×3 identiteettimatriisi

# Transpoosi
transpoosi = A.T
# tai
transpoosi = np.transpose(A)

# Matriisitulo
tulo = np.dot(A, C)
# tai (Python 3.5+)
tulo = A @ C
```

### Yleisiä virheitä

❌ **Virhe:** Alkioittainen kertolasku matriisitulona
```python
A * B  # Alkioittainen, ei matriisitulo!
```

✅ **Oikein:** Matriisitulo
```python
np.dot(A, B)  # tai A @ B
```

❌ **Virhe:** Väärät dimensiot
```python
A = np.array([[1, 2, 3]])  # 1×3
B = np.array([[4], [5]])    # 2×1
np.dot(A, B)  # Virhe: 3 ≠ 2
```

✅ **Oikein:** Yhteensopivat dimensiot
```python
A = np.array([[1, 2]])     # 1×2
B = np.array([[3], [4]])    # 2×1
np.dot(A, B)  # OK: 1×1 tulos
```

---

## Harjoitus 4: Datan analysointi ⭐⭐⭐

**Tavoite:** Analysoida 2D-dataa axis-parametrilla.

### Ratkaisu

```python
import numpy as np

arvosanat_lista = [
    [4, 5, 3],
    [5, 5, 4],
    [2, 3, 3],
    [4, 4, 5],
    [3, 4, 4]
]

arvosanat = np.array(arvosanat_lista)
print("Arvosanat:")
print(arvosanat)
print()

# Keskiarvot
opiskelija_ka = np.mean(arvosanat, axis=1)
kurssi_ka = np.mean(arvosanat, axis=0)

print(f"Opiskelijoiden keskiarvot: {opiskelija_ka}")
print(f"Kurssien keskiarvot: {kurssi_ka}")
print()

# Parhaat/huonoimmat
paras_indeksi = np.argmax(opiskelija_ka)
paras_ka = opiskelija_ka[paras_indeksi]
print(f"Paras opiskelija: {paras_indeksi + 1} (keskiarvo: {paras_ka:.2f})")

vaikein_indeksi = np.argmin(kurssi_ka)
vaikein_ka = kurssi_ka[vaikein_indeksi]
print(f"Vaikein kurssi: {vaikein_indeksi + 1} (keskiarvo: {vaikein_ka:.2f})")

# Viitosen saaneet
on_viitonen = np.any(arvosanat == 5, axis=1)
viitosen_saaneet = np.sum(on_viitonen)
print(f"Opiskelijoita joilla vähintään yksi 5: {viitosen_saaneet}")

# Kokonaiskeskiarvo
kokonais_ka = np.mean(arvosanat)
print(f"Kokonaiskeskiarvo: {kokonais_ka:.2f}")
```

### Keskeiset oppipisteet

1. **axis-parametri:**
   - `axis=0` → sarakkeet (pystysuunta)
   - `axis=1` → rivit (vaakasuunta)
   - `axis=None` → kaikki alkiot (oletus)

2. **Aggregaatiot:** `mean()`, `sum()`, `min()`, `max()` axis:n yli

3. **Indeksit:** `argmax()`, `argmin()` palauttavat indeksin

4. **Boolean-operaatiot:**
   - `np.any()` → onko yksikään True
   - `np.all()` → ovatko kaikki True

### Vaihtoehtoiset tavat

```python
# Kaikki viitosen saaneet (vaihtoehto)
viitosen_saaneet = 0
for opiskelija in arvosanat:
    if 5 in opiskelija:
        viitosen_saaneet += 1

# tai
viitosen_saaneet = sum(1 for row in arvosanat if 5 in row)

# Paras opiskelija (manuaalinen)
parhaat_ka = [sum(row)/len(row) for row in arvosanat]
paras_indeksi = parhaat_ka.index(max(parhaat_ka))
```

### Yleisiä virheitä

❌ **Virhe:** axis-parametri väärin
```python
# Halutaan opiskelijoiden keskiarvot (rivit)
np.mean(arvosanat, axis=0)  # Väärä! Antaa kurssien ka
```

✅ **Oikein:**
```python
np.mean(arvosanat, axis=1)  # Oikein! Rivien keskiarvot
```

**Muistisääntö:** axis=0 "poistaa" rivit (jättää sarakkeet), axis=1 "poistaa" sarakkeet (jättää rivit).

---

## Harjoitus 5: Lineaarinen regressio ⭐⭐⭐⭐

**Tavoite:** Toteuttaa yksinkertainen lineaarinen regressio NumPylla.

### Ratkaisu

```python
import numpy as np

opiskeluaika_lista = [1, 2, 3, 4, 5, 6, 7, 8]
pisteet_lista = [45, 51, 55, 60, 65, 70, 78, 82]

opiskeluaika = np.array(opiskeluaika_lista)
pisteet = np.array(pisteet_lista)

print(f"Opiskeluajat: {opiskeluaika}")
print(f"Pisteet: {pisteet}")
print()

# Korrelaatio
korrelaatio = np.corrcoef(opiskeluaika, pisteet)[0, 1]
print(f"Korrelaatio: {korrelaatio:.2f}")

# Regressioparametrit
k = np.cov(opiskeluaika, pisteet)[0, 1] / np.var(opiskeluaika)
b = np.mean(pisteet) - k * np.mean(opiskeluaika)
print(f"Regressiosuora: y = {k:.2f}x + {b:.2f}")
print()

# Ennuste
ennuste_10h = k * 10 + b
print(f"Ennuste 10 tunnille: {ennuste_10h:.1f} pistettä")
print()

# Vertailu
print("Vertailu (tunnit → todellinen / ennuste):")
for i in range(len(opiskeluaika)):
    todellinen = pisteet[i]
    ennuste = k * opiskeluaika[i] + b
    print(f"{opiskeluaika[i]}h → {todellinen} / {ennuste:.1f}")
```

### Keskeiset oppipisteet

1. **Lineaarinen regressio:** y = kx + b
   - k = kulmakerroin (slope)
   - b = vakiotermi (intercept)

2. **Korrelaatio:** `np.corrcoef()` mittaa lineaarista yhteyttä (-1 ... 1)

3. **Kovarianssi:** `np.cov()` mittaa muuttujien yhteisvaihtelua

4. **Regressiokaavat:**
   - k = cov(x,y) / var(x)
   - b = mean(y) - k × mean(x)

5. **Ennustaminen:** Sijoita x regressiosuoraan

### Vaihtoehtoiset tavat

```python
# NumPy polyfit (yksinkertaisempi)
k, b = np.polyfit(opiskeluaika, pisteet, 1)
print(f"y = {k:.2f}x + {b:.2f}")

# Ennusteet kaikille
ennusteet = k * opiskeluaika + b

# Virheen laskenta (RMSE)
virheet = pisteet - ennusteet
rmse = np.sqrt(np.mean(virheet**2))
print(f"RMSE: {rmse:.2f}")

# R² (selitysaste)
ss_tot = np.sum((pisteet - np.mean(pisteet))**2)
ss_res = np.sum(virheet**2)
r2 = 1 - (ss_res / ss_tot)
print(f"R²: {r2:.3f}")
```

### Yleisiä virheitä

❌ **Virhe:** Sekoitetaan korrelaatio ja kulmakerroin
```python
# Korrelaatio ei ole sama kuin kulmakerroin!
k = np.corrcoef(x, y)[0, 1]  # Väärä!
```

✅ **Oikein:**
```python
k = np.cov(x, y)[0, 1] / np.var(x)  # Oikea kulmakerroin
```

❌ **Virhe:** np.cov() indeksointi väärin
```python
cov = np.cov(x, y)
k = cov  # Väärä! cov on 2×2 matriisi
```

✅ **Oikein:**
```python
cov_matrix = np.cov(x, y)
k = cov_matrix[0, 1] / np.var(x)  # Oikea kovarianssi
```

---

## NumPy-yhteenveto

### Tärkeimmät funktiot

**Taulukon luonti:**
- `np.array([...])` - listasta
- `np.zeros(shape)` - nollat
- `np.ones(shape)` - ykköset
- `np.arange(start, stop, step)` - väli
- `np.linspace(start, stop, num)` - tasavälinen

**Tilastot:**
- `np.mean()` - keskiarvo
- `np.median()` - mediaani
- `np.std()` - keskihajonta
- `np.var()` - varianssi
- `np.min()`, `np.max()` - ääriarvot
- `np.percentile()` - prosenttipiste

**Matriisit:**
- `.T` tai `np.transpose()` - transpoosi
- `np.dot(A, B)` tai `A @ B` - matriisitulo
- `+`, `-`, `*` - alkioittaiset operaatiot

**Suodatus ja haku:**
- `array > value` - boolean-taulukko
- `array[boolean]` - suodatus
- `np.where(condition)` - indeksit
- `np.argmax()`, `np.argmin()` - ääriarvon indeksi

**Aggregaatiot axis:n yli:**
- `np.sum(array, axis=0/1)` - summa
- `np.mean(array, axis=0/1)` - keskiarvo
- `np.any()`, `np.all()` - boolean-tarkistukset

### Miksi NumPy?

✅ **Nopeus:** 10-100× nopeampi kuin Pythonin listat  
✅ **Muisti:** Pienempi muistijalanjälki  
✅ **Kätevyys:** Vektorisointi ja matriisioperaatiot  
✅ **Ekosysteemi:** Pandas, Matplotlib, Scikit-learn käyttävät NumPyä

---

**Seuraavaksi:** [Algoritmit ja rekursio](../../12.Algoritmit%20ja%20rekursio/README.md)
