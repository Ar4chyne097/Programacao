from bonus import calcular_bonus

def test_excelente():
    assert calcular_bonus(100.00,"Excelente") == 120.00

def test_bom():
    assert calcular_bonus(100.00, "Bom") == 110.00

def test_regular():
    assert calcular_bonus(100.00, "Regular") == 102.00

def test_ruim():
    assert calcular_bonus(100.00, "Ruim") == 100.00

def test_caranguejeiro():
    assert calcular_bonus(-5, "Catapimbas") == 0.00