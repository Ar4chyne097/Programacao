from functions import alzheimer

def test_espaco():
    for i in range(1, 50):
        assert alzheimer(i) == "Confortável"
    
def test_monitorar():
    for i in range(50, 85):
        assert alzheimer(i) == "Monitorar"
        
def test_critico():
    assert alzheimer(85) == "Crítica"
    assert alzheimer(90) == "Crítica"
    assert alzheimer(95) == "Crítica"
    assert alzheimer(100) == "Crítica"
    
def test_ERRO():
    assert alzheimer("CEBOLA PICADA") == "ERRO! Intentálo otra vez"