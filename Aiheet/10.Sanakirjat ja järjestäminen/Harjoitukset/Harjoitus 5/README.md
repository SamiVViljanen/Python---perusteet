# Harjoitus 5: Sanalaskuri ⭐⭐⭐⭐

## Tehtävänanto

Kysy käyttäjältä lause ja laske kuinka monta kertaa kukin sana esiintyy.

**Tee seuraavat asiat:**
1. Kysy käyttäjältä lause
2. Jaa lause sanoiksi (`.split()`)
3. Muunna sanat pieniksi kirjaimiksi
4. Laske kuinka monta kertaa kukin sana esiintyy (käytä sanakirjaa)
5. Järjestä sanat esiintymismäärän mukaan (yleisin ensin)
6. Tulosta tulokset

**Bonustehtävä:**
- Poista välimerkit sanoista (`.strip(".,!?")`)
- Älä laske tyhjiä sanoja

## Esimerkkitulostus

```
Anna lause: Python on loistava kieli. Python on helppo oppia. Python on suosittu.

=== SANALASKURI ===

Yleisin sana: python (3 kertaa)

Kaikki sanat (yleisimmästä harvinaisimpaan):
python: 3 kertaa
on: 3 kertaa
loistava: 1 kertaa
kieli: 1 kertaa
helppo: 1 kertaa
oppia: 1 kertaa
suosittu: 1 kertaa

Yhteensä 7 erilaista sanaa.
```

## Vinkkejä

- Jaa sanoiksi: `sanat = lause.split()`
- Pieniksi kirjaimiksi: `sana.lower()`
- Poista välimerkit: `sana.strip(".,!?")`
- Laske sanoja:
  ```python
  sanalaskuri = {}
  for sana in sanat:
      if sana in sanalaskuri:
          sanalaskuri[sana] += 1
      else:
          sanalaskuri[sana] = 1
  ```
  TAI
  ```python
  sanalaskuri[sana] = sanalaskuri.get(sana, 0) + 1
  ```
- Järjestä: `sorted(sanalaskuri.items(), key=lambda x: x[1], reverse=True)`

## Aloita tästä

Avaa [harjoitus5.py](harjoitus5.py) ja aloita koodaaminen!
