# MODUULI MITTAUSSANOMIEN KÄSITTELYYN

# TODO: Tee esimerkki siitä, miten rakennetaan sanoma.

# Sanoma koostuu alkumerkistä <, datasta, loppumerkistä > ja varmistussummasta.
# Varmistussumma lasketaan siten, että kirjainten ASCII-koodit
# lasketaan yhteen ja summasta otetaan jakojäännös (modulo) 127.
# Sanoman sisältö koostuu kentistä sivuA, sivuB, ristimitta ja virhe.
# Erottimena kenttien välillä on pystyviiva |

# TODO: Esimerkki, miten puretaan
# sanoman sisältämät tiedot tallennetaan avain-arvopariksi.
# Esim. {'seinä 1' : 'seinä 2' : 2500 ...}.
# Tietojen oikeellisuus tarkistetaan laskemalla varmistussumma
# uudelleen ja vertaamalla sitä sanoman mukana tulleeseen.

# Kirjastojen ja moduulien lataukset

# Funktio, jolla muodostetaan sanoman sisältö.

def muodosta_sanoma2(seina1, seina2, ristimitta, virhe):
    """Muodostaa merkkijonon sanomarakenteen mukaan.

    Args:
        seina1 (float): Ensimmäisen seinän pituus (mm)
        seina2 (float): Toisen seinän pituus (mm)
        ristimitta (float): Seinien välilnen ristimitta
        virhe (float): Lasketun ja mitatun ristimitan välinen ero

    Returns:
        str: Tiedot merkkijonoksi muutettuna. Tietojen välissä |
    """
    merkkijono = str(seina1) + '|' + str(seina2) + '|' + \
        str(ristimitta) + '|' + str(virhe) + '|'
    return merkkijono

# Tai

def muodosta_sanoma(seina1, seina2, ristimitta, virhe):
    """Muodostaa merkkijonon sanomarakenteen mukaan.

    Args:
        seina1 (float): Ensimmäisen seinän pituus (mm)
        seina2 (float): Toisen seinän pituus (mm)
        ristimitta (float): Seinien välilnen ristimitta
        virhe (float): Lasketun ja mitatun ristimitan välinen ero

    Returns:
        str: Tiedot merkkijonoksi muutettuna. Tietojen välissä |
    """
    merkkijono = f'{seina1}|{seina2}|{ristimitta}|{virhe}|'
    return merkkijono


def summaa_merkit(merkkijono):
    """Laskee merkkijonon kirjainten ASCII-arvot yhteen.

    Args:
        merkkijono (string): Merkkijono, jonka kirjaimista summa lasketaan

    Returns:
        integer: Kirjainten ASCII-koodien summa
    """
    summa = 0
    for kirjain in merkkijono:
        numeroarvo = ord(kirjain)
        summa += numeroarvo
    return summa


def laske_varmiste(summa):
    """Laskee modulo 127 tarkisteen.

    Args:
        summa (integer): Luku, josta tarkiste lasketaan

    Returns:
        integer: Jakojäännös 127:llä jaettaessa
    """
    varmiste = summa % 127
    return varmiste

def lopullinen_sanoma(sanoma, varmiste):
    """Koostaa lopullisen sanoman.

    Args:
        sanoma (string): Pituustiedot sisältävä merkkijono
        varmiste (integer): Varmiste

    Returns:
        string: Kokonainen sanoma, jossa alku- ja loppumerkit mukana
    """
    varmiste_str = str(varmiste)
    sanoma = '<' + sanoma + varmiste_str + '>'
    return sanoma


# TODO: Yhdistä kaikki yhteen sanomaan, eli alku- ja loppumerkit sekä varmiste tekstinä.
# TODO: Refaktoroi summa_merkit() ja laske_varmisteet() -funktiot yhdeksi funktioksi
# siten, että jakaja on funktion toisena argumenttina.


# Funktio hyödyntää aiemmin määriteltyjä funktioita.
def muodosta_varmiste2(merkit, jakaja):
    """Muodostaa merkkijonosta varmisteen käyttäjän määrittelemällä jakajalla.

    Args:
        merkit (string): Merkkijono, josta modulo lasketaan
        jakaja (integer): Jakaja

    Returns:
        string: jakojäännös merkkijonoksi muutettuna
    """
    summa = 0
    for kirjain in merkit:
        numeroarvo = ord(kirjain)
        summa += numeroarvo

    jakojaannos = summa % jakaja
    varmiste = str(jakojaannos)
    return varmiste

# Funktio hyödyntää aiemmin määriteltyjä funktioita.
def muodosta_varmiste(merkit, jakaja):
    summa = summaa_merkit(merkit)
    varmiste = str(summa % jakaja)
    return varmiste

# # Koodia voidaan edelleen hyödyntää.
# def muodosta_varmiste(merkit, jakaja):
#     return str(summaa_merkit(merkit) % jakaja)

if __name__ == "__main__":
    merkkijono = muodosta_sanoma(3000, 4000, 5003, 3)
    summa = summaa_merkit(merkkijono)
    print(merkkijono)
    print('Merkkien summa on:', summa)
    varmiste = laske_varmiste(summa)
    print('Modulo 127 varmiste on', varmiste)
    valmis_sanoma = lopullinen_sanoma(merkkijono, varmiste)
    print('Valmis sanoma näyttää tältä:', valmis_sanoma)

# if __name__ == "__main__":
#     print('Käytä ohjelmaa ajamalla sitä sovellus.py-tiedoston kautta.')
