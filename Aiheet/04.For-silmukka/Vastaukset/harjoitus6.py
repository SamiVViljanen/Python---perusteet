# Harjoitus 6: FizzBuzz - RATKAISU

# 1-2. Käy läpi luvut 1-30 ja tarkista ehdot
for i in range(1, 31):
    # Tarkista ensin jaollisuus molemmilla (3 JA 5)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Sitten jaollisuus 3:lla
    elif i % 3 == 0:
        print("Fizz")
    # Sitten jaollisuus 5:llä
    elif i % 5 == 0:
        print("Buzz")
    # Muuten tulosta luku
    else:
        print(i)
