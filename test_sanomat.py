# SANOMAT.PY-MODUULIN TESTIT

# Moduulien ja kirjastojen lataukset
import sanomat

# Testatataan, että sanoman erotinmerkit tulevat oikein Janin funktiolla.
def test_muodosta_sanoma():
    assert sanomat.muodosta_sanoma(3000, 4000, 5000, 0) == '3000|4000|5000|0|'

# Testatataan, että sanoman erotinmerkit tulevat oikein.
def test_muodosta_sanoma2():
    assert sanomat.muodosta_sanoma2(3000, 4000, 5000, 0) == '3000|4000|5000|0|'
