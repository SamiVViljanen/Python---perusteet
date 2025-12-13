# Harjoitus 5: Useita poikkeuksia

def lue_tiedosto(tiedostonimi):
    """
    Lukee tiedoston sisällön ja palauttaa sen merkkijonona.
    Palauttaa None jos lukeminen epäonnistuu.
    """
    try:
        with open(tiedostonimi, "r", encoding="utf-8") as f:
            sisältö = f.read()
            return sisältö
    except FileNotFoundError:
        print(f"Virhe: Tiedostoa '{tiedostonimi}' ei löydy.")
        return None
    except PermissionError:
        print(f"Virhe: Ei oikeuksia lukea tiedostoa '{tiedostonimi}'.")
        return None
    except UnicodeDecodeError:
        print(f"Virhe: Tiedoston '{tiedostonimi}' merkistö on virheellinen.")
        return None
    except Exception as e:
        print(f"Odottamaton virhe: {e}")
        return None


# Luo testiksi tiedosto
with open("testi.txt", "w", encoding="utf-8") as f:
    f.write("Tämä on testitiedosto.\n")
    f.write("Hienoa, että poikkeukset toimivat!")

# Testaa funktiota
print("=== Testi 1: Tiedosto löytyy ===")
sisältö = lue_tiedosto("testi.txt")
if sisältö:
    print("Tiedoston sisältö:")
    print(sisältö)

print("\n=== Testi 2: Tiedostoa ei löydy ===")
sisältö = lue_tiedosto("ei_ole.txt")

print("\n=== Testi 3: Tyhjä tiedostonimi ===")
sisältö = lue_tiedosto("")
