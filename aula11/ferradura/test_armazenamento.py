from functions import estoque

def test_estocamento():
    for i in range(400, 500):
        assert estoque(i) == "Seguro"

def test_monitorar():
    assert estoque(500) == "Monitorar"
    assert estoque(1000) == "Monitorar"
    assert estoque(1500) == "Monitorar"
    assert estoque(1999) == "Monitorar"

def test_upgrade():
    assert estoque(2000) == "Upgrade necessário"
    assert estoque(2100) == "Upgrade necessário"
    assert estoque(2200) == "Upgrade necessário"
    assert estoque(2300) == "Upgrade necessário"
    assert estoque(2400) == "Upgrade necessário"

def test_ERRO():
    assert estoque("CEBOLINHA") == "ERRO! Intentálo otra vez"