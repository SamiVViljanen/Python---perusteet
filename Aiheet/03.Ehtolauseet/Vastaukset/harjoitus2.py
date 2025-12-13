# Harjoitus 2: Arvosanan määrittäminen - RATKAISU

# 1. Kysy käyttäjältä kokeen pistemäärä
pisteet = int(input("Anna kokeen pisteet (0-100): "))

# 2-3. Määritä ja tulosta arvosana
if pisteet >= 90:
    print("Arvosana: Kiitettävä")
elif pisteet >= 80:
    print("Arvosana: Hyvä")
elif pisteet >= 70:
    print("Arvosana: Tyydyttävä")
elif pisteet >= 60:
    print("Arvosana: Välttävä")
else:
    print("Arvosana: Hylätty")
