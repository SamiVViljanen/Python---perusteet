# Harjoitus 5: Lineaarinen regressio ⭐⭐⭐⭐

## Tehtävänanto

Toteuta yksinkertainen lineaarinen regressio, joka ennustaa tenttipistemäärän opiskeluajan perusteella.

Data: opiskeluaika (tunnit) ja tenttipistemäärä (0-100):
```
opiskeluaika = [1, 2, 3, 4, 5, 6, 7, 8]
pisteet = [45, 51, 55, 60, 65, 70, 78, 82]
```

Lineaarisen regression kaava: `y = kx + b`
- k = kulmakerroin (slope)
- b = vakiotermi (intercept)

Laske k ja b käyttäen NumPy-funktioita:
- `k = np.cov(x, y)[0, 1] / np.var(x)`
- `b = np.mean(y) - k * np.mean(x)`

Tee ohjelma, joka:
1. Luo NumPy-taulukot datasta
2. Laskee korrelaatiokertoimen
3. Laskee regressiosuoran parametrit (k, b)
4. Ennustaa pistemäärän 10 tunnin opiskelulle
5. Visualisoi tulokset (tulosta alkuperäiset pisteet ja ennusteet)

## Esimerkkitulostus

```
Opiskeluajat: [1 2 3 4 5 6 7 8]
Pisteet: [45 51 55 60 65 70 78 82]

Korrelaatio: 0.99
Regressiosuora: y = 5.18x + 40.05

Ennuste 10 tunnille: 91.8 pistettä

Vertailu (tunnit → todellinen / ennuste):
1h → 45 / 45.2
2h → 51 / 50.4
3h → 55 / 55.6
4h → 60 / 60.8
5h → 65 / 66.0
6h → 70 / 71.2
7h → 78 / 76.4
8h → 82 / 81.5
```

## Vinkit

- Korrelaatio: `np.corrcoef(x, y)[0, 1]`
- Kovarianssi: `np.cov(x, y)[0, 1]`
- Varianssi: `np.var(x)`
- Ennuste: `y_pred = k * x + b`
- Pyöristys: `round(arvo, 1)` tai `f"{arvo:.1f}"`

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus5.py](harjoitus5.py)
