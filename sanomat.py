# MODUULI MITTAUSSANOMIEN KÄSITTELYYN

# Sanoma koostuu alkumerkistä <, datasta, loppumerkistä > ja varmistussummasta.
# Varmistussumma lasketaan siten, että kirjainten ASCII-koodit
# lasketaan yhteen ja summasta otetaan jakojäännös (modulo) 127.
# Sanoman sisältö koostuu kentistä sivuA, sivuB, ristimitta ja virhe.
# Erottimena kenttien välillä on pystyviiva |

# Sanoman sisältämät tiedot tallennetaan avain-arvopariksi.
# Esim. {'seinä 1' : 'seinä 2' : 2500 ...}.
# Tietojen oikeellisuus tarkistetaan laskemalla varmistussumma
# uudelleen ja vertaamalla sitä sanoman mukana tulleeseen.

# Kirjastojen ja moduulien lataukset


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


# Muodostetaan merkeistä modulo-varmiste valittua jakajaa käyttäen.
def muodosta_varmiste(merkit, jakaja):
    return str(summaa_merkit(merkit) % jakaja)


# Yleispätevä funktio sanoman muodostamiseen.
def luo_sanoma(arvot, alkumerkki, loppumerkki, erotin, jakaja):
    """ Muodostaa sanoman, joka koostuu alkumerkistä, arvoista, varmistussummasta\n
    ja loppumerkistä. Arvojen välillä on haluttu erotinmerkki.

    Args:
        arvot (list): Sanomaan sisällöksi halutut arvot
        alkumerkki (string): Merkki, jolla ilmaistaan sanoman alku
        loppumerkki (string): Merkki, jolla ilmaistaan sanoman päättyminen
        erotin (string): Arvojen välille tuleva välimerkki
        jakaja (int): Jakojäännöksen laskennassa käytettävä jakaja

    Returns:
        string: Valmis sanoma 
    """
    sanoma = ''  # Alustetaan sanoma tyhjäksi.

    # Luetaan listan arvot ja muutetaan merkkijonoksi sekä lisätään erotinmerkki.
    for arvo in arvot:
        sanoma += str(arvo) + erotin

    # Lisätään sanomaan alkumerkki, varmiste ja loppumerkki.
    sanoma = alkumerkki + sanoma + \
        muodosta_varmiste(sanoma, jakaja) + loppumerkki
    return sanoma
    

def pura_sanoma(sanoma, alkumerkki, loppumerkki, erotin, jakaja):
    """Purkaa sanoman, kun sille kerrotaan muodostussäännöt.

    Args:
        sanoma (string): Vastaanotettu sanoma
        alkumerkki (string): Sanoman aloittava erikoismerkki
        loppumerkki (string): Sanoman päättävä erikoismerkki
        erotin (string): Kenttien välinen erotinmerkki
        jakaja (int): Modulotarkistuksen jakaja

    Returns:
        list: Lista arvoista (string), virhekoodi (integer), virhesanoma (string)
    """
    arvot = []  # Alustetaan arvoksi tyhjä lista.
    osat = []  # Alustetaan sanoman osat tyhjäksi listaksi.
    virhekoodi = 0 # Normaalitilanteen virhekoodi.
    virhesanoma ='Data OK' # Normaalitilanteen virhesanoma.

    # Varmistetaan, että ensimmäinen merkki on alkumerkki.
    if sanoma[0] == alkumerkki:

        # Varmistetaan, että viimeinen merkki on loppumerkki.
        if sanoma[-1] == loppumerkki:
            sanoma = sanoma[1:-1]  # Poistetaan alku- ja loppumerkit.

            # Muodostetaan osat jakamalla sanoma erottimen kohdalta.
            osat = sanoma.split(erotin)

            # Osia pitää ollä vähintään 2: arvo ja varmistussumma.
            if len(osat) >= 2:
                # Luetaan varmiste ja muutetaan se kokonaisluvuksi.
                alkuperainen_varmiste = int(osat[-1])
                # Muodostetaan arvoista ja erottimesta sanoman arvot sisältävä osa.
                arvo_osat = f"{'|'.join(osat[0:-1])}|"
                # Lasketaan varmiste uudelleen.
                laskettu_varmiste = int(muodosta_varmiste(arvo_osat, jakaja))

                # Varmistetaan, että alkuperäinen ja uudelleenlaskettu varmiste ovat samat.
                if alkuperainen_varmiste == laskettu_varmiste:
                    arvot = (osat[0:-1])  # Muodostetaan arvoluettelo.

                else:
                    virhekoodi = 4
                    virhesanoma = 'Sanoma vahingoittunut, varmistussumma ei täsmää.'
            
            else:
                virhekoodi = 3
                virhesanoma = 'Sanoma ei sisällä tarvittavaa dataa, viestissä ainoastaan varmiste.'
        
        else:
            virhekoodi = 2
            virhesanoma = 'Virhe sanoma vajaa, loppumerkki puuttuu.'
    
    else:
        virhekoodi = 1
        virhesanoma = 'Sanoma vajaa, alkumerkki puuttuu.'

    # Palautetaan arvot.
    return [arvot, virhekoodi, virhesanoma]


if __name__ == "__main__":
    sanoma = luo_sanoma([3000, 4000, 5000, 0], '<', '>', '|', 127)
    print(sanoma)
