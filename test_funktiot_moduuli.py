# Yksikkötestit moduulille funktiot_moduuli.py

import funktiot_moduuli

def test_suorakulma():
    assert funktiot_moduuli.suorakulma(3, 4, 5) == 0.0
    assert round(funktiot_moduuli.suorakulma(10, 12, 14), 4) == -1.6205

if __name__ == "__main__":
    print('Käytä ohjelmaa ajamalla sitä sovellus.py-tiedoston kautta.')
    