from functions import latido

def test_lataria():
    for i in range(1,10):
        assert latido(i) == "Excelente"
    
def test_boa():
    for i in range(10,40):
        assert latido(i) == "Boa"
    
def test_regular():
    for i in range(40,100):
        assert latido(i) == "Regular"
    
def test_ruim():
    assert latido(100.0) == "Ruim"
    assert latido(100.1) == "Ruim"
    assert latido(100.2) == "Ruim"
    assert latido(100.3) == "Ruim"
    
def test_ERRO():
    assert latido("GOIABADA") == "ERRO! Intentálo otra vez"