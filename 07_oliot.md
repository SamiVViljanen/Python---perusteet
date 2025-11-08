# MIKSI KÄYTETÄÄN OLIOITA (CLASS/OBJECTS)?

Pythonissa oliot (classes, objects) ovat tapa **järjestää tietoa ja siihen liittyvää toimintaa yhteen paikkaan**.
Olioita käytetään, kun halutaan mallintaa asioita ohjelmassa samaan tapaan kuin oikeassa maailmassa:
esimerkiksi **auto, opiskelija, tuote tai aikaleima(timestamp)** voidaan kaikki esittää olioina.


# MITÄ OLIO TARKOITTAA?

Olio on ”**paketti**” jossa on:
-	tietoa (muuttujat eli attribuutit)
-	toimintaa (funktiot, eli metodit)

Voit ajatella luokkaa (class) kuin **kaavana** tai **muottina**, josta voidaan luoda monta samanlaista oliota – aivan kuten leipämuotti tekee monta samanlaista leipää.

HUOMIOITA:
•	**init** on olion alustaja (initializer), jota kutsutaan heti kun olio on luotu. Tekninen yksityiskohta: varsinaisen objektin luova funktio on new; init alustaa jo luodun instanssin. Opetuksessa init-termin käyttö on kuitenkin yleensä riittävä.

•	**self** ei ole Pythonin avainsana vaan konventio; se viittaa instanssiin, kun kutsutaan instanssimetodeja. Voit nimetä sen muullakin nimellä, mutta self on toimiva käytäntö ja sitä kannattaa käyttää.

•	**PEP8-tyyli**: luokkien nimet CamelCase, metodit ja muuttujat snake_case.

```Python
class CamelCase:

  def snake_case():
``` 
 
## _ESIMERKKI YKSINKERTAISESTA LUOKASTA_

```Python
class Auto:
  def __init__(self, merkki, vuosimalli):
    self.merkki = merkki
    self.vuosimalli = vuosimalli

  def aja(self):
    print(f"{self.merkki} vuodelta {self.vuosimalli} on nyt liikkeellä!")

auto1 = Auto("Volvo", 2015)
auto2 = Auto("Toyota", 2020)

auto1.aja()
auto2.aja()
```
 
Tulostaa:
```
Volvo vuodelta 2015 on nyt liikkeellä!
Toyota vuodelta 2020 on nyt liikkeellä!
```

# MITÄ TÄSSÄ TAPAHTUU?

-	**class Auto**: määrittää uuden luokan nimeltä Auto

-	**init** on erityinen rakentajafunktio (constructor), jota kutsutaan, kun luodaan uusi olio

-	**self** viittaa aina kyseiseen olioon itseensä

-	**auto1** ja **auto2** ovat _Auto_-luokan yksittäisiä ilmentymiä eli olioita 


# @DATACLASS – HELPPO TAPA LUODA OLIOITA

Pythonissa on valmiina @dataclass, joka tekee luokkien kirjoittamisesta helpompaa, jos ne sisältävät vain tietoa.
Dataclass luo automaattisesti mm. init, repr ja eq -metodit puolestasi:

```Python
from dataclasses import dataclass

@dataclass
class Henkilö:
  nimi: str
  ikä: int

henkilö1 = Henkilö("Maija", 25)
print(henkilö1)
```

Tulostaa:
```
Henkilö(nimi=’Maija’, ikä=25)
```

💡Et siis tarvitse erikseen __init__ -metodia – dataclass tekee sen automaattisesti!
 

# CLASS ESIMERKKI: TIMESTAMP
Tämä luokka mallintaa yksinkertaista aikaleimaa:

```Python
from datetime import datetime

class Timestamp:
  def __init__(self):
    self.aika = datetime.now()

  def näytä(self):
    print(f"Aikaleima: {self.aika}")

t.Timestamp()
t.näytä()
```
 
Tulostaa:
```
Aikaleima: 2025-11-08 21:08:26.755381   ( eli juuri sen hetkinen aika )
```

# MIKSI OLIOITA KANNATTAA KÄYTTÄÄ?

-	Yhdistää tiedon ja toiminnan samaan kokonaisuuteen

-	Tekee koodista uudelleenkäytettävää ja helposti laajennettavaa

-	Auttaa mallintamaan monimutkaisia asioita selkeästi

-	Vähentää virheitä ja parantaa koodin rakennetta suurissa projekteissa


# OLIOT, FUNKTIOT JA MODUULIT

| RAKENNE  | TARKOITUS   |
|-------------|-------------|
| Funktio (def)  | Suorittaa tietyn tehtävän|
| Class / olio   | Yhdistää tehtäviä ja tietoa yhteen pakettiin|
| Moduuli (tiedosto) | Kokoaa useita luokkia ja funktioita yhteen ohjelmaan|

 
# YHTEENVETO

**Oliot ovat ohjelmoinnin rakennuspalikoita**¸ joiden avulla:
-	Yhdistää tieto ja toiminta

-	hallitaan suuria kokonaisuuksia järkevästi

-	luodaan siistiä, ylläpidettävää ja laajennettavaa koodia

💡Muista: Luokka (class) on ohje – olio (object) on sen yksittäinen toteutus!
Käytä @Dataclass, kun haluat nopeasti ja helposti tietoa sisältävän olion ilman turhaa koodia


