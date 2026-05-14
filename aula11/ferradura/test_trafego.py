from functions import analisar_trafego

def test_baixo():
    for i in range(90,100):
        assert analisar_trafego(i) == "Baixo Tráfego"
        
def test_moderado():
    assert analisar_trafego(100) == "Tráfego moderado"
    assert analisar_trafego(300) == "Tráfego moderado"
    assert analisar_trafego(499) == "Tráfego moderado"
    
def test_alto():
    for i in range(500,521):
        assert analisar_trafego(i) == "Tráfego alto"

def test_ERRO():
    assert analisar_trafego("OI") == "ERRO! Intentálo otra vez"
    assert analisar_trafego(-100) == "ERRO! Intentálo otra vez"