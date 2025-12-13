# Vastaukset: Funktioiden määrittäminen

Tässä kansiossa on kaikkien harjoitusten mallivastaukset sekä selitykset.

---

## Harjoitus 1: Ensimmäinen funktio ⭐

### Ratkaisu
[harjoitus1.py](harjoitus1.py)

```python
def tervehdi():
    print("Hei! Tervetuloa Python-ohjelmoinnin maailmaan!")

tervehdi()
tervehdi()
tervehdi()
```

### Selitys
- **def:** Avainsana funktion määrittämiseen (define)
- **tervehdi():** Funktion nimi + tyhjät sulut (ei parametreja)
- **Sisennys:** Funktion koodi sisennetään 4 välilyönnillä
- **Kutsuminen:** Kirjoita funktion nimi + sulut: `tervehdi()`

### Tärkeää
⚠️ Funktio **määritellään** kerran (def), mutta sitä voidaan **kutsua** monta kertaa!

### Opittavaa
✅ Funktion perusrakenne: `def nimi():`  
✅ Sisennys on tärkeä Python-ohjelmissa  
✅ Funktio suoritetaan vasta kun sitä kutsutaan  
💡 Funktio tekee koodista uudelleenkäytettävää!

---

## Harjoitus 2: Funktio yhdellä parametrilla ⭐⭐

### Ratkaisu
[harjoitus2.py](harjoitus2.py)

```python
def tervehdi_nimella(nimi):
    print(f"Hei, {nimi}! Kiva nähdä.")

tervehdi_nimella("Anna")
tervehdi_nimella("Matti")
tervehdi_nimella("Liisa")
```

### Selitys
- **Parametri:** `nimi` on muuttuja, joka ottaa vastaan arvon
- **Kutsu:** `tervehdi_nimella("Anna")` antaa parametrille arvon "Anna"
- **F-string:** `f"Hei, {nimi}!"` upottaa muuttujan arvon tekstiin

### Miten parametri toimii?
```python
tervehdi_nimella("Anna")  # nimi = "Anna"
# → Tulostaa: Hei, Anna! Kiva nähdä.

tervehdi_nimella("Matti") # nimi = "Matti"
# → Tulostaa: Hei, Matti! Kiva nähdä.
```

### Opittavaa
✅ Parametri otetaan vastaan suluissa: `def funktio(parametri):`  
✅ Parametri on muuttuja, joka saa arvon kutsussa  
✅ Sama funktio voidaan kutsua eri arvoilla  
💡 Parametrit tekevät funktioista joustavia!

---

## Harjoitus 3: Funktio return-arvolla ⭐⭐

### Ratkaisu
[harjoitus3.py](harjoitus3.py)

```python
def nelio(luku):
    return luku * luku

print(nelio(3))
print(nelio(5))
print(nelio(10))
```

### Selitys
- **return:** Palauttaa arvon takaisin kutsujalle
- **nelio(3):** Kutsuu funktiota, funktio palauttaa 9
- **print(nelio(3)):** Tulostaa palautetun arvon

### Return vs Print
❌ **VÄÄRIN (print funktion sisällä):**
```python
def nelio(luku):
    print(luku * luku)  # Funktio tulostaa, mutta ei palauta arvoa

tulos = nelio(3)  # tulos = None (ei palautusarvoa!)
```

✅ **OIKEIN (return):**
```python
def nelio(luku):
    return luku * luku  # Funktio palauttaa arvon

tulos = nelio(3)  # tulos = 9
print(tulos)      # Tulostaa: 9
```

### Vaihtoehtoinen tapa
```python
def nelio(luku):
    return luku * luku

# Voit tallentaa tuloksen muuttujaan:
tulos1 = nelio(3)
tulos2 = nelio(5)
tulos3 = nelio(10)

print(tulos1)  # 9
print(tulos2)  # 25
print(tulos3)  # 100
```

### Opittavaa
✅ `return` palauttaa arvon takaisin kutsujalle  
✅ `print` vain tulostaa, ei palauta arvoa  
✅ Palautettu arvo voidaan tallentaa muuttujaan tai tulostaa suoraan  
💡 Return tekee funktioista tehokkaita laskukoneita!

---

## Harjoitus 4: Funktio usealla parametrilla ⭐⭐⭐

### Ratkaisu
[harjoitus4.py](harjoitus4.py)

```python
def laske_summa(a, b, c):
    return a + b + c

def laske_keskiarvo(a, b, c):
    summa = laske_summa(a, b, c)
    return summa / 3

summa = laske_summa(10, 20, 30)
keskiarvo = laske_keskiarvo(10, 20, 30)

print(f"Summa: {summa}")
print(f"Keskiarvo: {keskiarvo}")
```

### Selitys
- **Useita parametreja:** Erotetaan pilkulla: `def funktio(a, b, c):`
- **Funktio kutsuu toista funktiota:** `laske_keskiarvo()` käyttää `laske_summa()`
- **Uudelleenkäyttö:** Ei tarvitse laskea summaa uudestaan!

### Miksi funktiot kutsuvat toisia funktioita?
```python
# Huono tapa (toistetaan sama laskenta):
def laske_keskiarvo(a, b, c):
    return (a + b + c) / 3  # Lasketaan summa uudestaan

# Hyvä tapa (uudelleenkäytetään olemassa olevaa funktiota):
def laske_keskiarvo(a, b, c):
    summa = laske_summa(a, b, c)  # Käytetään valmista funktiota
    return summa / 3
```

### Vaihtoehtoinen ratkaisu (kompaktimpi)
```python
def laske_summa(a, b, c):
    return a + b + c

def laske_keskiarvo(a, b, c):
    return laske_summa(a, b, c) / 3  # Ei tarvitse välimuuttujaa

print(f"Summa: {laske_summa(10, 20, 30)}")
print(f"Keskiarvo: {laske_keskiarvo(10, 20, 30)}")
```

### Opittavaa
✅ Useita parametreja erotetaan pilkulla  
✅ Funktiot voivat kutsua toisia funktioita  
✅ Uudelleenkäyttö vähentää toistoa ja virheitä  
💡 Jaa ongelma pieniin osiin → helpompi ymmärtää ja testata!

---

## Harjoitus 5: Main-funktio ja ohjelmarakenne ⭐⭐⭐⭐

### Ratkaisu
[harjoitus5.py](harjoitus5.py)

```python
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    # Celsius → Fahrenheit
    celsius = float(input("Anna lämpötila Celsiuksina: "))
    fahrenheit = celsius_fahrenheit(celsius)
    print(f"{celsius}°C on {fahrenheit}°F")
    print()
    
    # Fahrenheit → Celsius
    fahrenheit = float(input("Anna lämpötila Fahrenheitina: "))
    celsius = fahrenheit_celsius(fahrenheit)
    print(f"{fahrenheit}°F on {celsius}°C")

if __name__ == "__main__":
    main()
```

### Selitys
- **Muuntofunktiot:** `celsius_fahrenheit()` ja `fahrenheit_celsius()` tekevät laskut
- **main()-funktio:** Hallitsee ohjelman kulkua (input, output)
- **if __name__ == "__main__":** Varmistaa että main() ajetaan vain kun ohjelma suoritetaan suoraan

### Mikä on `if __name__ == "__main__"`?

Tämä rakenne:
1. ✅ **Suorittaa main()** kun ajat ohjelman (esim. `python harjoitus5.py`)
2. ❌ **Ei suorita main()** jos ohjelma tuodaan moduulina toiseen ohjelmaan

**Esimerkki:**
```python
# tiedosto: lampotila.py
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def main():
    print("Tämä on lämpötilalaskuri!")

if __name__ == "__main__":
    main()  # Ajetaan vain jos suoritetaan suoraan
```

Jos ajat `python lampotila.py`:
```
Tämä on lämpötilalaskuri!
```

Jos tuot toisessa ohjelmassa (`import lampotila`):
```python
# tiedosto: toinen.py
import lampotila

tulos = lampotila.celsius_fahrenheit(25)  # Toimii!
# main() ei aja automaattisesti → ei tulostuksia
```

### Miksi tämä on tärkeää?

✅ **Uudelleenkäytettävyys:** Funktiot voidaan käyttää muissa ohjelmissa ilman että main() sotkee  
✅ **Selkeys:** Näkyy selvästi mikä on "ohjelman pääosa"  
✅ **Ammattimainen:** Kaikki suuret Python-projektit käyttävät tätä rakennetta

### Ohjelmarakenne (hyvä käytäntö)

```python
# 1. FUNKTIOT (ensin kaikkien funktioiden määrittelyt)
def funktio1():
    pass

def funktio2():
    pass

def main():
    # Pääohjelma täällä
    pass

# 2. PÄÄOHJELMAN KÄYNNISTYS (lopussa)
if __name__ == "__main__":
    main()
```

### Vaihtoehtoinen ratkaisu (ilman main)

```python
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Suoraan "roskakoodina" (ei suositella)
celsius = float(input("Anna lämpötila Celsiuksina: "))
fahrenheit = celsius_fahrenheit(celsius)
print(f"{celsius}°C on {fahrenheit}°F")
```

❌ Tämä toimii, mutta:
- Ei selkeä rakenne
- Vaikea uudelleenkäyttää
- Ei ammattimainen

### Opittavaa
✅ main()-funktio on ohjelman "pääsisäänkäynti"  
✅ `if __name__ == "__main__":` suorittaa main():n vain suorassa ajossa  
✅ Funktiot ylhäällä, main()-kutsu alhaalla = selkeä rakenne  
✅ Jaa vastuu: muuntofunktiot laskevat, main() hallitsee I/O  
💡 Tämä on ammattimainen tapa kirjoittaa Python-ohjelmia!

---

## Yhteenveto: Funktioiden tärkeimmät osat

### 1. Funktion määrittely
```python
def funktio_nimi(parametri1, parametri2):
    # Koodia täällä
    return arvo
```

### 2. Funktion kutsuminen
```python
tulos = funktio_nimi(arvo1, arvo2)
```

### 3. Return vs Print
- **return:** Palauttaa arvon → voidaan käyttää muualla
- **print:** Tulostaa näytölle → ei voi käyttää muualla

### 4. Main-rakenne
```python
def main():
    # Pääohjelma

if __name__ == "__main__":
    main()
```

---

## Yleisiä virheitä

### 1. Unohdetaan return
❌ **VÄÄRIN:**
```python
def nelio(luku):
    luku * luku  # Ei palauta mitään!

tulos = nelio(5)  # tulos = None
```

✅ **OIKEIN:**
```python
def nelio(luku):
    return luku * luku

tulos = nelio(5)  # tulos = 25
```

### 2. Kutsutaan funktiota ennen määrittelyä
❌ **VÄÄRIN:**
```python
tervehdi()  # NameError: name 'tervehdi' is not defined

def tervehdi():
    print("Hei!")
```

✅ **OIKEIN:**
```python
def tervehdi():  # Määrittely ensin
    print("Hei!")

tervehdi()  # Kutsu vasta tämän jälkeen
```

### 3. Väärä määrä parametreja
❌ **VÄÄRIN:**
```python
def summa(a, b):
    return a + b

tulos = summa(5)  # TypeError: missing 1 required positional argument
```

✅ **OIKEIN:**
```python
def summa(a, b):
    return a + b

tulos = summa(5, 3)  # Molemmat parametrit annettu
```

### 4. Print return:n sijaan
❌ **VÄÄRIN:**
```python
def kertoma(a, b):
    print(a * b)  # Tulostaa, mutta ei palauta

tulos = kertoma(3, 4)  # Tulostaa 12, mutta tulos = None
```

✅ **OIKEIN:**
```python
def kertoma(a, b):
    return a * b  # Palauttaa arvon

tulos = kertoma(3, 4)  # tulos = 12
print(tulos)  # Tulostaa 12
```

---

## Vinkkejä

💡 **Nimeäminen:** Käytä kuvaavia nimiä: `laske_summa` parempi kuin `f1`  
💡 **Yksi tehtävä:** Yksi funktio tekee yhden asian hyvin  
💡 **Testaa erikseen:** Testaa jokainen funktio erikseen ennen kuin yhdistät  
💡 **Kommentit:** Kirjoita mitä funktio tekee, etenkin jos se on monimutkainen  
💡 **Main viimeisenä:** Määrittele kaikki funktiot ennen main():ia

---

## Funktioiden hyödyt

✅ **Uudelleenkäyttö:** Kirjoita kerran, käytä monta kertaa  
✅ **Selkeys:** Koodi on helpompi lukea ja ymmärtää  
✅ **Testattavuus:** Voit testata pienä osia erikseen  
✅ **Ylläpito:** Muutokset tarvitsee tehdä vain yhteen paikkaan  
✅ **Yhteistyö:** Eri ihmiset voivat työstää eri funktioita

---

Hienoa työtä! Olet nyt oppinut funktioiden perusteet. 🎉

➡️**Seuraavaksi:** [Aihe 07 - Oliot](../../07.Oliot/)
