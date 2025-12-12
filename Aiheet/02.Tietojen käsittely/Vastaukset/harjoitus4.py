# Harjoitus 4: Merkkijonojen viipalointi ja indeksointi - RATKAISU

# 1. Kysy käyttäjältä sähköpostiosoite
email = input("Anna sähköpostiosoitteesi: ")

# 2. Tulosta käyttäjätunnus ja domain
osat = email.split('@')
kayttaja = osat[0]
domain = osat[1]
print(f"Käyttäjä: {kayttaja}")
print(f"Domain: {domain}")

# 3. Tulosta merkkijonon ensimmäinen ja viimeinen merkki
ensimmainen = email[0]
viimeinen = email[-1]
print(f"Ensimmäinen merkki: {ensimmainen}")
print(f"Viimeinen merkki: {viimeinen}")

# 4. Tulosta merkkijono käänteisenä
kaanteinen = email[::-1]
print(f"Käänteinen: {kaanteinen}")
