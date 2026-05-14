from functions import calorimetria

def test_temperatura():
    for i in range(20):
        assert calorimetria(i) == "Frio"
    
def test_ideal():
    for i in range(20,40):
        assert calorimetria(i) == "Ideal"
    
def test_alerta():
    for i in range(40,70):
        assert calorimetria(i) == "Alerta"
        
def test_critico():
    assert calorimetria(70) == "Risco crítico"
    assert calorimetria(80) == "Risco crítico"
    assert calorimetria(90) == "Risco crítico"
    assert calorimetria(100) == "Risco crítico"
    
def test_erro():
    assert calorimetria(-10) == "ERRO! Intentálo otra vez"