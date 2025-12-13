# Harjoitus 6: FizzBuzz (⭐⭐⭐⭐ Haaste)

## Tavoite
Yhdistä for-silmukka ja ehtolauseet (klassinen ohjelmointihaaste!).

## Tehtävä
1. Tulosta luvut 1-30
2. **MUTTA:**
   - Jos luku on jaollinen 3:lla, tulosta "Fizz"
   - Jos luku on jaollinen 5:llä, tulosta "Buzz"
   - Jos luku on jaollinen molemmilla (3 JA 5), tulosta "FizzBuzz"
   - Muuten tulosta luku normaalisti

## Esimerkki:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
...
```

💡 **Vinkit:**
- Tarkista ENSIN jaollisuus molemmilla (15)
- Sitten jaollisuus 3:lla
- Sitten jaollisuus 5:llä
- Käytä modulo-operaattoria: `luku % 3 == 0`

📝 **Tiedosto:** [Harjoitus 6](harjoitus6.py)
