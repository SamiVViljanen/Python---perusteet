# Funktioiden määrittäminen

## Sisällysluettelo
1. [Miksi funktioita määritetään?](#miksi-funktioita-määritetään)
2. [Main()-funktio](#main-funktio)
3. [Yhteenveto](#yhteenveto)

---

## Miksi funktioita määritetään?

Pythonissa funktioiden määrittäminen (def, tulee sanasta define) on tapa järjestää koodia:
-	selkeästi
-	tehokkaasti
-	uudelleenkäytettävästi


Esimerkiksi:

```Python
def summa(a, b):
  return a + b
```
 
Tämä määrittää ”ohjeen” tai ”pienen ohjelman”, joka voidaan suorittaa milloin tahansa vain kutsumalla sen nimi. Näin koodista tulee uudelleenkäytettävä.

Esimerkiksi:

```Python
def summa(a, b):    # funktio määritetään vain kerran
  return a + b

# Mutta sitä voidaan kutsua monta kertaa:
tulos1 = summa(5,3)
tulos2 = summa(10, 20)
tulos3 = summa(2, 7)
```

Funktiot myös pilkkovat monimutkaisen ohjelman pienempiin osiin¸ jolloin ohjelmasta tulee helpompi lukea ja testata. Kun koodi on jaettu pieniin osiin, virheitä on helpompi etsiä ja korjata.
 
## Main()-funktioPythonissa main()-funktiota käytetään usein ohjelman pääsisäänkäyntinä, eli se kertoo, mistä ohjelman varsinainen suoritus on tarkoitus alkaa.

Python ei kuitenkaan automaattisesti aloita suorittamista main()-funktiosta, vaan ohjelmoijat käyttävät sitä tapana selkeästi määrittää aloituskohta.

```Python
def main():
  print("Hei maailma!")

if __name__ == "__main__":
  main()
```

rivillä    if __name__ == ”__main__”:

Python tarkistaa:

-	Jos ohjelma ajetaan suoraan (esim.  python main.py tai Visual Studio Coden play-nappia painamalla), niin main() kutsutaan

-	Jos ohjelma tuodaan toisesta tiedostosta moduulina, main() ei käynnisty automaattisesti

**HUOM!** Älä suotta takerru moduuli asiaan, jos se tuntuu epäselvältä. Asiaa käydään myöhemmin tarkemmin läpi – halusin vain mainita sen, koska se on tärkeä syy, miksi tätä rakennetta käytetään.
 
## Yhteenveto

Funktiot ovat tapa jakaa koodi järkeviin, uudelleenkäytettäviin osiin. Ne tekevät ohjelmasta luettavamman, siistimmän ja helpommin ylläpidettävän.

main()-funktio on käytännön tapa kertoa:

”Tämä on ohjelman pääosa – tästä haluan suorittamisen alkavan!”

Tämä rakenne tekee koodista selkeän, turvallisen ja helpommin hallittavan, etenkin kun ohjelmat kasvavat pidemmiksi.

**def main()** ei siis ole pakollinen Pythonissa, mutta se on **vahva suositus** ja ammattikäytäntö.
