# Harjoitus 4: Sanakirjan järjestäminen

# Luo sanakirja tuotteista ja hinnoista
tuotteet = {
    "Maito": 1.50,
    "Leipä": 2.30,
    "Juusto": 4.50,
    "Kahvi": 5.90,
    "Mehu": 2.80,
    "Voi": 3.20
}

# Tulosta alkuperäinen sanakirja
print("Alkuperäinen sanakirja:")
for tuote, hinta in tuotteet.items():
    print(f"{tuote}: {hinta:.2f} €")

# Järjestä hinnan mukaan (halvin ensin)
print("\n=== HALVIN ENSIN ===")
halvin_ensin = sorted(tuotteet.items(), key=lambda x: x[1])
for tuote, hinta in halvin_ensin:
    print(f"{tuote}: {hinta:.2f} €")

# Järjestä hinnan mukaan (kallein ensin)
print("\n=== KALLEIN ENSIN ===")
kallein_ensin = sorted(tuotteet.items(), key=lambda x: x[1], reverse=True)
for tuote, hinta in kallein_ensin:
    print(f"{tuote}: {hinta:.2f} €")

# Järjestä aakkosjärjestyksessä
print("\n=== AAKKOSJÄRJESTYKSESSÄ ===")
aakkosissa = sorted(tuotteet.items())
for tuote, hinta in aakkosissa:
    print(f"{tuote}: {hinta:.2f} €")
