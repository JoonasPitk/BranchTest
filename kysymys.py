# MODUULI ERI TYYPPISILLE KYSYMYKSILLE

# Kysytään käyttäjältä tietoja ja tarkistetaan tietojen oikeellisuus.
def kysy_liukuluku(kysymys):
    """Kysyy käyttäkäjältä liukuluvun ja tarkistaa oikeellisuuden.

    Args:
        kysymys (string): Kuvaruudulle tulostuva kysymys

    Returns:
        float: Käyttäjän syöttämä arvo liukuluvuksi muutettuna
    """
    vastaus = input(kysymys)
    try:
        arvo = float(vastaus)
    except:
        arvo = 0
        print('Syöttämäsi arvo ei ole luku.')
    finally:
        return arvo
