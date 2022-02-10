# MODUULI MITTAUSSANOMIEN KÄSITTELYYN

# TODO: tee esimerkki siitä, miten rakennetaan sanoma.

# Sanoma koostuu alkumerkistä <, datasta, loppumerkistä > ja varmistussummasta.
# Varmistussumma lasketaan siten, että kirjainten ASCII-koodit
# lasketaan yhteen ja summasta otetaan jakojäännös (modulo) 127.
# Sanoman sisältö koostuu kentistä sivuA, sivuB, ristimitta ja virhe.
# Erottimena kenttien välillä on pystyviiva |

# TODO: esimerkki, miten puretaan
# sanoman sisältämät tiedot tallennetaan avain-arvopariksi.
# Esim. {'seinä 1' : 'seinä 2' : 2500 ...}.
# Tietojen oikeellisuus tarkistetaan laskemalla varmistussumma
# uudelleen ja vertaamalla sitä sanoman mukana tulleeseen.

# Kirjastojen ja moduulien lataukset

# Funktio, jolla muodostetaan sanoman sisältö.
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
    merkkijono = str(seina1) + '|' + str(seina2) + '|' + \
        str(ristimitta) + '|' + str(virhe) + '|'
    return merkkijono


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
    merkkijono = f'{seina1}|{seina2}|{ristimitta}|{virhe}|'
    return merkkijono


def summaa_merkit(merkkijono):
    summa = 0
    for kirjain in merkkijono:
        numeroarvo = ord(kirjain)
        summa = summa + numeroarvo
    return summa


def laske_varmiste(summa):
    varmiste = summa % 127
    return varmiste

# TODO: Yhdistä kaikki yhteen sanomaan, eli alku- ja loppumerkit sekä varmiste tekstinä.
# TODO: Refaktoroi summa_merkit() ja laske_varmisteet() -funktiot yhdeksi funktioksi
# siten, että jakaja on funktion toisena argumenttina.

if __name__ == "__main__":
    merkkijono = muodosta_sanoma2(3000, 4000, 5003, 3)
    summa = summaa_merkit(merkkijono)
    print(merkkijono)
    print('Merkkien summa on:', summa)
    varmiste = laske_varmiste(summa)
    print('Modulo 127 varmiste on', varmiste)

# if __name__ == "__main__":
#     print('Käytä ohjelmaa ajamalla sitä sovellus.py-tiedoston kautta.')
