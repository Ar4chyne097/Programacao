from functions import poupa_tempo

def test_detran():
    assert poupa_tempo("1914-07-28", 4) == "Certificado expirado"
    assert poupa_tempo("1939-09-01", 6) == "Certificado expirado"
    
def test_quase():
    assert poupa_tempo("2021-05-13", 5) == "Certificado expira em breve"
    assert poupa_tempo("2021-06-10", 5) == "Certificado expira em breve"

def test_certin():
    assert poupa_tempo("2026-01-09", 10) == "Certificado válido"
    assert poupa_tempo("2026-02-10", 9) == "Certificado válido"
    
def test_ERRO():
    assert poupa_tempo(1, "R") == "ERRO! Intentálo otra vez"
    assert poupa_tempo("R", -5) == "ERRO! Intentálo otra vez"