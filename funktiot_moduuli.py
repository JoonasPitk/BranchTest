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
    try:
        # Tuota virhe, jos joku luvuista on nolla (Raise).
        if sivuA * sivuB * lavistaja <= 0:
            raise ValueError('Jokaisen mitan tulee olla nollaa suurempi luku!')
        # Toinen tapa selvittää asia, jako nollalla -virhe.
        # luku = 1 / (sivuA * sivuB * lavistaja)
        A_nelio = sivuA * sivuA
        B_nelio = sivuB * sivuB
        l_nelio = lavistaja * lavistaja
        pitaisi_olla = A_nelio + B_nelio
        ero = l_nelio ** 0.5 - pitaisi_olla ** 0.5
    except:
        ero = 9999
        print('Syötetty arvo on virheellinen.')
    finally:
        return ero


if __name__ == "__main__":
    print('Käytä ohjelmaa ajamalla sitä sovellus.py-tiedoston kautta.')
