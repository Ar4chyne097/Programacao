from cupom import aplicar_cupom

def test_10():
    assert aplicar_cupom("cupom10", 10.00) == 0.1
    assert aplicar_cupom("CUPOM10", 365.00) == 0.1
    assert aplicar_cupom("cUpOm10", 289.00) == 0.1

def test_25():
    assert aplicar_cupom("cupom25", 121.00) == 0.25
    assert aplicar_cupom("CUPOM25", 529.00) == 0.25
    assert aplicar_cupom("CuPoM25", 144.00) == 0.25

def test_35():
    assert aplicar_cupom("descontovip", 576.00) == 0.35
    assert aplicar_cupom("DESCONTOVIP", 625.00) == 0.35
    assert aplicar_cupom("DeScOnToViP", 676.00) == 0.35
    assert aplicar_cupom("dEsCoNtOvIp", 729.00) == 0.35

def test_stenorhynchus():
    assert aplicar_cupom("Atirei_O_Pau_No_Gato", -10) == 0.00
    assert aplicar_cupom("Catapirambolas", 81) == 0.00