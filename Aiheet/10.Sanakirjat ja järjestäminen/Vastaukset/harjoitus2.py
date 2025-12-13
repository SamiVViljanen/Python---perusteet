# Harjoitus 2: Sanakirjan läpikäynti

# Luo sanakirja opiskelijoiden pisteistä
pisteet = {
    "Anna": 92,
    "Pekka": 78,
    "Liisa": 45,
    "Matti": 88,
    "Kaisa": 79
}

print("=== OPISKELIJOIDEN TULOKSET ===\n")

# Laske keskiarvo
keskiarvo = sum(pisteet.values()) / len(pisteet)
print(f"Keskiarvo: {keskiarvo:.1f} pistettä\n")

# Etsi paras suoritus
paras_nimi = max(pisteet, key=pisteet.get)
paras_pisteet = pisteet[paras_nimi]
print(f"Paras suoritus: {paras_nimi} ({paras_pisteet} pistettä)\n")

# Käy läpi kaikki opiskelijat
print("Yksittäiset tulokset:")
for nimi, pistemäärä in pisteet.items():
    tila = "Hyväksytty" if pistemäärä >= 50 else "Hylätty"
    print(f"{nimi}: {pistemäärä} pistettä - {tila}")
