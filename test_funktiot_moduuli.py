# Yksikkötestit moduulille funktiot_moduuli.py

import funktiot_moduuli

def test_suorakulma():
    assert funktiot_moduuli.suorakulma(3, 4, 5) == 0.0
    assert round(funktiot_moduuli.suorakulma(10, 12, 14), 4) == -1.6205
    