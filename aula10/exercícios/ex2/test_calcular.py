from frete import calcular_frete

def test_0kg():
    assert calcular_frete(0) == 0.00
    assert calcular_frete(-10) == 0.00

def test_1kg():
    assert calcular_frete(0.1) == 5.00
    assert calcular_frete(0.7) == 5.00
    assert calcular_frete(1) == 5.00

def test_5kg():
    assert calcular_frete(1.01) == 10.00
    assert calcular_frete(5) == 10.00

def test_10kg():
    assert calcular_frete(5.01) == 18.00
    assert calcular_frete(5.02) == 18.00
    assert calcular_frete(5.03) == 18.00
    assert calcular_frete(5.04) == 18.00
    assert calcular_frete(5.05) == 18.00