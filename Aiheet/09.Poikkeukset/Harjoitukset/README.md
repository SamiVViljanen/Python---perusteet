# Harjoitukset: Poikkeukset

Tässä kansiossa on harjoitustehtävät poikkeuksista ja virheiden käsittelystä.

## Harjoituslista

### [Harjoitus 1: Turvallinen jako](Harjoitus%201/README.md) ⭐
Tee ohjelma, joka kysyy kaksi lukua ja jakaa ne. Käsittele:
- ValueError (jos syöte ei ole luku)
- ZeroDivisionError (jos jakaja on 0)

### [Harjoitus 2: Listan käsittely](Harjoitus%202/README.md) ⭐⭐
Luo lista ja pyydä käyttäjää syöttämään indeksi. Tulosta kyseisen indeksin arvo. Käsittele:
- ValueError (ei numero)
- IndexError (indeksi liian suuri tai pieni)

### [Harjoitus 3: Finally-harjoitus](Harjoitus%203/README.md) ⭐⭐
Tee yksinkertainen laskin, joka tulostaa aina lopuksi "Kiitos laskimen käytöstä!" käyttäen finally-lohkoa.

### [Harjoitus 4: Else-lohko](Harjoitus%204/README.md) ⭐⭐⭐
Kysy käyttäjältä ikää. Jos syöte on validi:
- Tulosta ikä
- Tulosta onko käyttäjä alaikäinen vai täysi-ikäinen
- Käytä else-lohkoa normaalille toiminnalle

### [Harjoitus 5: Useita poikkeuksia](Harjoitus%205/README.md) ⭐⭐⭐⭐
Tee funktio joka lukee tiedoston ja palauttaa sen sisällön. Käsittele:
- FileNotFoundError
- PermissionError
- UnicodeDecodeError
- Muut virheet (Exception)

---

**Vinkki:** Muista käyttää try-except-rakennetta kaikissa harjoituksissa!

**Seuraavaksi:** Kun olet tehnyt harjoitukset, tarkista [Vastaukset](../Vastaukset/README.md)
