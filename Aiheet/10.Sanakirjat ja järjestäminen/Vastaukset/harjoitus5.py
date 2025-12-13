# Harjoitus 5: Sanalaskuri

# Kysy käyttäjältä lause
lause = input("Anna lause: ")

# Jaa sanoiksi ja muunna pieniksi kirjaimiksi
sanat = lause.lower().split()

# Laske sanat sanakirjaan
sanalaskuri = {}

for sana in sanat:
    # Poista välimerkit
    sana = sana.strip(".,!?;:")
    
    # Älä laske tyhjiä sanoja
    if sana:
        # Lisää tai kasvata lukumäärää
        sanalaskuri[sana] = sanalaskuri.get(sana, 0) + 1

# Järjestä yleisin ensin
järjestetty = sorted(sanalaskuri.items(), key=lambda x: x[1], reverse=True)

# Tulosta tulokset
print("\n=== SANALASKURI ===\n")

if järjestetty:
    yleisin_sana, yleisin_määrä = järjestetty[0]
    print(f"Yleisin sana: {yleisin_sana} ({yleisin_määrä} kertaa)\n")
    
    print("Kaikki sanat (yleisimmästä harvinaisimpaan):")
    for sana, määrä in järjestetty:
        print(f"{sana}: {määrä} kertaa")
    
    print(f"\nYhteensä {len(sanalaskuri)} erilaista sanaa.")
else:
    print("Ei sanoja laskettavaksi.")
