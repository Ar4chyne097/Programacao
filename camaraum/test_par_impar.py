from par_impar import eh_par

def test_numero_par():
    assert eh_par(4) is True
    assert eh_par(2) is True

def test_numero_impar():
    assert eh_par(5) is False