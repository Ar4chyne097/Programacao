from functions import eventos

def test_identificador():
    assert eventos("api.prod.example", "2021-05-20T14:30:00Z") == "api.prod.example2021-05-20T14:30:00Z"

def test_ERRO():
    assert eventos(1, 1) == "ERRO! Intentálo otra vez"
    assert eventos("-11", "-10") == "ERRO! Intentálo otra vez"