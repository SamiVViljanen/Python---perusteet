# Harjoitus 4: Palindromi-tarkistus

# 1. Toteuta rekursiivinen palindromi-tarkistus
def on_palindromi(s):
    """
    Tarkistaa rekursiivisesti onko merkkijono palindromi.
    """
    # Perustapaus: 0-1 merkkiä on aina palindromi
    if len(s) <= 1:
        return True
    
    # Tarkista ensimmäinen vs. viimeinen
    if s[0] != s[-1]:
        return False
    
    # Rekursiivinen tapaus: tarkista keskiosa
    return on_palindromi(s[1:-1])

# 2-4. Testaa eri sanoilla
sanat = ["saippuakivikauppias", "anna", "Python", "Saippuakauppias"]

print("Palindromit:\n")
for sana in sanat:
    tulos = on_palindromi(sana)
    merkki = "✓" if tulos else "✗"
    tyyppi = "Palindromi" if tulos else "Ei palindromi"
    print(f"'{sana}' → {tyyppi} {merkki}")
