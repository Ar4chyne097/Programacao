from functions import geral

def test_critico():
    assert geral(temp=71, cpu=91, mem=91, disco=9) == "Servidor crítico"

def test_alerta():
    assert geral(temp=41, lat=101) == "Servidor em alerta"

def test_estavel():
    assert geral(temp=40, cpu=85, mem=90, lat=100, disco=11) == "Servidor estável"

def test_ERRO():
    assert geral(temp=None, cpu=None, mem=None, lat=None, disco=None) == "ERRO! Intentálo otra vez"