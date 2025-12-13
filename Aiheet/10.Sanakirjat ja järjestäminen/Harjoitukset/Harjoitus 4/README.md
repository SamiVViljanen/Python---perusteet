# Harjoitus 4: Sanakirjan järjestäminen ⭐⭐⭐

## Tehtävänanto

Luo sanakirja, jossa on 6 tuotteen nimet ja hinnat.

**Tee seuraavat asiat:**
1. Luo sanakirja `tuotteet` (esim. "Maito": 1.50, "Leipä": 2.30, jne.)
2. Tulosta alkuperäinen sanakirja
3. Järjestä tuotteet hinnan mukaan (halvin ensin) ja tulosta
4. Järjestä tuotteet hinnan mukaan (kallein ensin) ja tulosta
5. Järjestä tuotteet nimen mukaan aakkosjärjestyksessä ja tulosta

## Esimerkkitulostus

```
Alkuperäinen sanakirja:
Maito: 1.50 €
Leipä: 2.30 €
Juusto: 4.50 €
Kahvi: 5.90 €
Mehu: 2.80 €
Voi: 3.20 €

=== HALVIN ENSIN ===
Maito: 1.50 €
Leipä: 2.30 €
Mehu: 2.80 €
Voi: 3.20 €
Juusto: 4.50 €
Kahvi: 5.90 €

=== KALLEIN ENSIN ===
Kahvi: 5.90 €
Juusto: 4.50 €
Voi: 3.20 €
Mehu: 2.80 €
Leipä: 2.30 €
Maito: 1.50 €

=== AAKKOSJÄRJESTYKSESSÄ ===
Juusto: 4.50 €
Kahvi: 5.90 €
Leipä: 2.30 €
Maito: 1.50 €
Mehu: 2.80 €
Voi: 3.20 €
```

## Vinkkejä

- Järjestä arvon mukaan: `sorted(tuotteet.items(), key=lambda x: x[1])`
- Laskeva järjestys: lisää `reverse=True`
- Järjestä avaimen mukaan: `sorted(tuotteet.items())` tai `sorted(tuotteet)`
- `.items()` palauttaa lista tuplista: `[("Maito", 1.50), ("Leipä", 2.30), ...]`
- Lambda `x[0]` = nimi, `x[1]` = hinta

## Aloita tästä

Avaa [harjoitus4.py](harjoitus4.py) ja aloita koodaaminen!
