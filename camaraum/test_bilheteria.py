from bilheteria import definir_preco_ingresso, PRECO_INTEIRA, PRECO_MEIA, PRECO_ISENTO

def test_ingressoInfantil():
    for i in range(1,3):
        assert definir_preco_ingresso(i) == PRECO_ISENTO

def test_ingressoJovem():
    for i in range(4,19):
        assert definir_preco_ingresso(i) == PRECO_MEIA

def test_ingressoIdoso():
    assert definir_preco_ingresso(60) == PRECO_MEIA
    assert definir_preco_ingresso(75) == PRECO_MEIA
    assert definir_preco_ingresso(80) == PRECO_MEIA

def test_ingressoAdulto():
    for i in range(19,60):
        assert definir_preco_ingresso(i) == PRECO_INTEIRA