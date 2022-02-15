# SANOMAT.PY-MODUULIN TESTIT

# Moduulien ja kirjastojen lataukset
import sanomat


# Testatataan, että sanoman erotinmerkit tulevat oikein Janin funktiolla.
def test_muodosta_sanoma():
    assert sanomat.muodosta_sanoma(3000, 4000, 5000, 0) == '3000|4000|5000|0|'


# Testatataan, että sanoman erotinmerkit tulevat oikein.
def test_muodosta_sanoma2():
    assert sanomat.muodosta_sanoma2(3000, 4000, 5000, 0) == '3000|4000|5000|0|'

# TODO: Luo testtit lopuille funktioille.

# ASCII-koodien summan testi.
def test_summaa_merkit():
    assert sanomat.summaa_merkit('3000|4000|5003|3|') == 1138

# Modulo 127 jakojäännöksen laskentatesti.
def test_laske_varmiste():
    assert sanomat.laske_varmiste(1138) == 122
    assert sanomat.laske_varmiste(127) == 0
    assert sanomat.laske_varmiste(128) == 1

# Testataan lopullisen sanoman muodostuminen.
def test_lopullinen_sanoma():
    assert sanomat.lopullinen_sanoma('3000|4000|5003|3|', 122) == '<3000|4000|5003|3|122>'

# Testataan parannettu varmisteenlaskentafunktio.
def test_muodosta_varmiste():
    merkit = '3000|4000|5003|3|'
    jakaja = 127
    assert sanomat.muodosta_varmiste(merkit, jakaja) == '122'
