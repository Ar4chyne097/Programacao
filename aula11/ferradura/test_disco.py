from functions import locadora

def test_cd():
    for i in range(20):
        assert locadora(i) == "Crítico"

def test_atencao():
    for i in range(20, 40):
        assert locadora(i) == "Atenção"

def test_seguro():
    assert locadora(40) == "Seguro"
    assert locadora(50) == "Seguro"
    assert locadora(60) == "Seguro"
    assert locadora(70) == "Seguro"
    assert locadora(80) == "Seguro"
    
def test_ERRO():
    assert locadora(-55) == "ERRO! Intentálo otra vez"
    assert locadora("OI :3") == "ERRO! Intentálo otra vez"