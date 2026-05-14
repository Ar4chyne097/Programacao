from functions import percentual_cpu

def test_Mirtilo():
    for i in range(1,39):
        assert percentual_cpu(i) == "Normal"
    
def test_alto():
    for i in range(40, 81):
        assert percentual_cpu(i) == "Alta"
        
def test_sobrecarga():
    assert percentual_cpu(85) == "Sobrecarga"
    assert percentual_cpu(90) == "Sobrecarga"
    assert percentual_cpu(95) == "Sobrecarga"
    assert percentual_cpu(100) == "Sobrecarga"
    
def test_ERRO():
    assert percentual_cpu(-55) == "ERRO! Intentálo otra vez"