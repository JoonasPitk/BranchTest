# MODUULI MITTAUSSANOMIEN KÄSITTELYYN

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

from posixpath import split


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
# Funktio saa parametrina mitat, jakajan ja erotinmerkin, alkumerkin ja loppumerkin.
# 

# Muodostetaan merkeistä varmiste valittua jakajaa käyttäen.
def muodosta_varmiste(merkit, jakaja):
    """Muodostaa merkkijonosta varmisteen käyttäjän määrittelemällä jakajalla.

    Args:
        merkit (string): Merkkijono, josta modulo lasketaan
        jakaja (integer): Jakaja

    Returns:
        string: jakojäännös merkkijonoksi muutettuna
    """
    return str(summaa_merkit(merkit) % jakaja)

if __name__ == "__main__":

    # Testataan sanoman muodostamista.
    merkkijono = muodosta_sanoma(3000, 4000, 5003, 3)
    summa = summaa_merkit(merkkijono)
    print(merkkijono)
    print('Merkkien summa on:', summa)
    varmiste = laske_varmiste(summa)
    print('Modulo 127 varmiste on', varmiste)
    valmis_sanoma = lopullinen_sanoma(merkkijono, varmiste)
    print('Valmis sanoma näyttää tältä:', valmis_sanoma)

    # Testataan sanoman purkamista.
    sanoman_pituus = len(valmis_sanoma) # Lasketaan sanoman kokonaispituus.
    ilman_merkkejä = valmis_sanoma[1:sanoman_pituus -1] # Sanoma ilman alku-ja loppumerkkejä.
    print('Sanoma ilman alku-ja loppumerkkejä on', ilman_merkkejä)
    paloteltu_sanoma = ilman_merkkejä.split('|') # Pilkotaan |-merkistä listaksi.
    print('Arvot listamuodossa ovat: ', paloteltu_sanoma)

    listan_pituus = len(paloteltu_sanoma)
    print('Listassa on', listan_pituus, 'jäsentä.')
    alkuperainen_tarkiste = paloteltu_sanoma[listan_pituus - 1] # Sanoman mukana tullut tarkiste.
    ilman_varmistetta = paloteltu_sanoma[0:listan_pituus - 1] # Listan jäsenet, ilman varmistussummaa.
    
    # Rakennetaan mitat sisältävä merkkijono uudelleen.
    uudelleen_str = ''
    for jasen in ilman_varmistetta:
        uudelleen_str = uudelleen_str + jasen + '|'
    print('Alkuperäinen tarkiste on', alkuperainen_tarkiste)

    # Verrataan alkuperäistä ja uudelleenlaskettua tarkistetta, jos sama sanoma on OK.
    uudelleenlaskettu_tarkiste = muodosta_varmiste(uudelleen_str, 127)
    print('Uudelleenlaskettuna se on', uudelleenlaskettu_tarkiste)
    if (alkuperainen_tarkiste) == muodosta_varmiste(uudelleen_str, 127):
        print('Sanoma vahingoittumaton, varmiste tarkistettu.')
    else:
        print('Sanoma muuttunut tiedonsiirrossa!')

    # TODO: Rakenna purkutestin perusteella funktio ja tee sille testi.
    # TODO: Refaktoroi koodia
    """
    paloteltu_sanoma = valmis_sanoma[1:len(valmis_sanoma)-1].split('|')

    [1:-1] tekee ton ilman len()

    ilman_varmistetta = f"{'|'.join(paloteltu_sanoma[0:-1])}|"
    """

# if __name__ == "__main__":
#     print('Käytä ohjelmaa ajamalla sitä sovellus.py-tiedoston kautta.')
