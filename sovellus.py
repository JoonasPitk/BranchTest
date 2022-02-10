# PÄÄOHJELMA

# KIRJASTOJEN JA MODUULIEN LATAUS

# Otetaan käyttöön Windows-äänikirjasto (pythonin sisäänrakennettu).
# import winsound

# Otetaan käyttöön oma funktiomoduuli.
import funktiot_moduuli

# Otetaan käyttöön oma kysymysmoduuli.
import kysymys


def select_case(sanakirja, avain, oletus):
    """Muiden ohjelmointikielten Select-Case-rakennetta vastaava funktio.

    Args:
        sanakirja (dict): Avain-arvo-parit
        avain (any): Hakuavain
        oletus (any): Arvo, jos hakuavainta ei löydy

    Returns:
        any: Hakuavainta vastaava arvo tai oletus, mikäli hakuavainta ei löytynyt
    """
    arvo = sanakirja.get(avain, oletus)
    return arvo


# Varsinainen pääohjelma alkaa tästä.
huoneraja_arvot = {
    'MH': 30,
    'K': 20,
    'KPH': 5,
    'WC': 5,
    'OH': 20,
}

# Lista mittaustuloksista, joka tyhjä ennen silmukkaa.
mittaustulokset = []

# Ikuinen silmukka.
while True:
    # Tätä toistetaan, kunnes käyttäjä sulkee ohjelman.
    seina1 = kysymys.kysy_liukuluku('Anna ensimmäisen seinän pituus (mm): ')
    seina2 = kysymys.kysy_liukuluku('Anna toisen seinän pituus (mm): ')
    lavistaja = kysymys.kysy_liukuluku('Anna huoneen ristimitta (mm): ')
    # Kysytään huonetyyppi.
    huone = input('Mikä huone on kyseessä? ').upper()
    mittaustulokset.append(seina1)
    mittaustulokset.append(seina2)
    mittaustulokset.append(lavistaja)

    # Haetaan raja-arvo sanakirjasta. Oletusarvo 50 mm.
    raja_arvo = select_case(huoneraja_arvot, huone, 50)

    # Ilmoitetaan ero ja suurin sallittu poikkeama.
    ero = funktiot_moduuli.suorakulma(seina1, seina2, lavistaja)
    print('Ero suorakulmaan oli', ero, '\nSuurin sallittu on', raja_arvo)
    print()

    # Kysytään käyttäjältä, haluaako jatkaa.
    lopetetaan = input('Paina L, jos haluat lopettaa: ').upper()
    if lopetetaan == 'L':
        break

# Ohjelman suoritus päättyy.

# Kysytään mittaajan ja työmaan tiedot.
# tyomaa = input(
#     'Minkä tyyppinen työmaa oli (kerrostalo, rivitalo, tai OK-talo): ').lower()

# Ilmoitetaan, montako senttiä mittauksessa saa olla virhettä IF-rankenteen avulla.

# if tyomaa == 'kerrostalo':
#     print('Enimmäisvirhe saa olla 10 mm.')
# elif tyomaa == 'rivitalo':
#     print('Enimmäisvirhe saa olla 20 mm.')
# else:
#     print('Maksimivirhe saa olla 50 mm.')

print('Enimmäisero', huone, 'on', raja_arvo, 'mm')

mittauksia = len(mittaustulokset)
print('Kiitos tästä päivästä. Teit', mittauksia, 'mittausta.')

# Tulosteaan ruudulle kaikki mittaustulokset.
print('Päivän mittaukset alla:')
for mittaus in mittaustulokset:
    print(mittaus)
