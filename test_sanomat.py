# SANOMAT.PY-MODUULIN TESTIT

# Moduulien ja kirjastojen lataukset
import sanomat

# ASCII-koodien summan testi.
def test_summaa_merkit():
    assert sanomat.summaa_merkit('3000|4000|5003|3|') == 1138

# Testataan parannettu varmisteenlaskentafunktio.
def test_muodosta_varmiste():
    merkit = '3000|4000|5003|3|'
    jakaja = 127
    assert sanomat.muodosta_varmiste(merkit, jakaja) == '122'

# Testataan yleiskäyttöinen sanomanmuodostusfunktio.

def test_luo_sanoma():
    mitatut_arvot = [3000, 4000, 5003, 3]
    assert sanomat.luo_sanoma(mitatut_arvot, '<', '>', '|', 127) == '<3000|4000|5003|3|122>'

def test_pura_sanoma():
    assert sanomat.pura_sanoma('<3000|4000|5003|3|122>', '<', '>', '|', 127) == [['3000', '4000', '5003', '3',], 0, 'Data OK']
    assert sanomat.pura_sanoma('3000|4000|5003|3|122>', '<', '>', '|', 127) == [[], 1, 'Sanoma vajaa, alkumerkki puuttuu.']
    assert sanomat.pura_sanoma('<3000|4000|5003|3|122', '<', '>', '|', 127) == [[], 2, 'Virhe sanoma vajaa, loppumerkki puuttuu.']
    assert sanomat.pura_sanoma('<122>', '<', '>', '|', 127) == [[], 3, 'Sanoma ei sisällä tarvittavaa dataa, viestissä ainoastaan varmiste.']
    assert sanomat.pura_sanoma('<3000|4000|5003|3|125>', '<', '>', '|', 127) == [[], 4, 'Sanoma vahingoittunut, varmistussumma ei täsmää.']
