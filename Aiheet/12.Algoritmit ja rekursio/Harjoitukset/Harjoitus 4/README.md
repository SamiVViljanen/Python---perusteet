# Harjoitus 4: Palindromi-tarkistus ⭐⭐⭐

## Tehtävänanto

**Palindromi** on sana tai lause, joka on sama molempiin suuntiin luettuna:
- `"saippuakivikauppias"` on palindromi
- `"anna"` on palindromi
- `"Python"` ei ole palindromi

Tee ohjelma, joka:
1. Toteuttaa rekursiivisen funktion `on_palindromi(s)`
2. Tarkistaa onko merkkijono palindromi
3. Testaa usealla eri sanalla:
   - `"saippuakivikauppias"`
   - `"anna"`
   - `"Python"`
   - `"Saippuakauppias"` (ei palindromi, iso S)
4. Tulostaa tulokset

## Esimerkkitulostus

```
Palindromit:

'saippuakivikauppias' → Palindromi ✓
'anna' → Palindromi ✓
'Python' → Ei palindromi ✗
'Saippuakauppias' → Ei palindromi ✗
```

## Vinkit

**Rekursiivinen lähestymistapa:**
1. **Perustapaus:** Jos merkkijono on 0-1 merkkiä → palindromi
2. **Tarkista:** Ensimmäinen == viimeinen?
   - Jos ei → ei palindromi
   - Jos kyllä → tarkista keskiosa rekursiivisesti

```python
def on_palindromi(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return on_palindromi(s[1:-1])
```

**Huomio:** Iso-/pienaakkoset: voit muuntaa pieniksi `s.lower()`

## Tiedosto

Kirjoita ratkaisusi tiedostoon [harjoitus4.py](harjoitus4.py)
