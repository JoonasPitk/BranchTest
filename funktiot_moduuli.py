# X-funktio tarkistaa, onko kulma suora.
# TODO: Lisää funktioon virheen laskenta millimetreinä.
def suorakulma(sivuA, sivuB, lavistaja):
    """Tarkistaa suorakulmaisuuden käyttäen Pythagoraan lausetta.

    Args:
        sivuA (float): Ensimmäisen sivun pituus
        sivuB (float): Toisen sivun pituus
        lavistaja (float): Lävistäjän pituus

    Returns:
        boolean: TRUE -> suorakulma
    """
    A_nelio = sivuA * sivuA
    B_nelio = sivuB * sivuB
    l_nelio = lavistaja * lavistaja
    # FIXME: Jos antaa arvoksi kirjaimen: kaatuu.
    if A_nelio + B_nelio == l_nelio:
        suora = True
    else:
        suora = False
    return suora


# Testataan, että toimii. Poista tämä myöhemmin!

if __name__ == "__main__":
    # Testi, jossa kulma on suora.
    vastaus = suorakulma(3, 4, 5)
    print(vastaus)

    # Testi, jossa kulma ei ole suora.
    vastaus = suorakulma(3, 4, 6)
    print(vastaus)
