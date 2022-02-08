# Funktio tarkistaa, onko kulma suora.

def suorakulma(sivuA, sivuB, lavistaja):
    """Tarkistaa suorakulmaisuuden käyttäen Pythagoraan lausetta.

    Args:
        sivuA (float): Ensimmäisen seinän pituus
        sivuB (float): Toisen seinän pituus
        lavistaja (float): Huoneen lävistäjän pituus

    Returns:
        float: Lävistäjän pituusvirhe, 0 -> ei virhettä
    """
    if sivuA * sivuB * lavistaja <= 0:
        raise ValueError('Jokaisen mitan tulee olla suurempi kuin nolla!')
    try:
        A_nelio = sivuA * sivuA
        B_nelio = sivuB * sivuB
        l_nelio = lavistaja * lavistaja
        pitaisi_olla = A_nelio + B_nelio
        ero = l_nelio ** 0.5 - pitaisi_olla ** 0.5
    except:
        ero = 999
        print('Syötetty arvo on virheellinen.')
    finally:
        return ero

if __name__ == "__main__":
    print('Käytä ohjelmaa ajamalla sitä sovellus.py-tiedoston kautta.')
