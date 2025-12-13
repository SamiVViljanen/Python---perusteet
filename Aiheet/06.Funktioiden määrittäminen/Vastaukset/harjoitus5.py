# Harjoitus 5: Main-funktio ja ohjelmarakenne
# Tavoite: Harjoittele main()-funktion käyttöä ja ohjelmarakennetta

# 1. Määritä funktio celsius_fahrenheit(celsius) joka muuntaa Celsius → Fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

# 2. Määritä funktio fahrenheit_celsius(fahrenheit) joka muuntaa Fahrenheit → Celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# 3. Määritä main()-funktio joka kysyy käyttäjältä lämpötiloja ja muuntaa ne
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

# 4. Kutsu main-funktiota if __name__ == "__main__": -rakenteella
if __name__ == "__main__":
    main()
