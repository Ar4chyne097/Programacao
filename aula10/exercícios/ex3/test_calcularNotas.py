from notas import calcular_nota_para_conceito

def test_A():
    calcular_nota_para_conceito(9.0) == "A"
    calcular_nota_para_conceito(9.1) == "A"
    calcular_nota_para_conceito(10.9) == "A"
    calcular_nota_para_conceito(10.0) == "A"

def test_B():
    calcular_nota_para_conceito(7.0) == "B"
    calcular_nota_para_conceito(7.2) == "B"
    calcular_nota_para_conceito(8.1) == "B"
    calcular_nota_para_conceito(8.9) == "B"

def test_C():
    calcular_nota_para_conceito(5.0) == "C"
    calcular_nota_para_conceito(5.1) == "C"
    calcular_nota_para_conceito(6.8) == "C"
    calcular_nota_para_conceito(6.9) == "C"

def test_D():
    calcular_nota_para_conceito(3.0) == "D"
    calcular_nota_para_conceito(4.0) == "D"
    calcular_nota_para_conceito(3.5) == "D"
    calcular_nota_para_conceito(4.9) == "D"

def test_F():
    calcular_nota_para_conceito(2.9) == "F"
    calcular_nota_para_conceito(2.4) == "F"
    calcular_nota_para_conceito(1.9) == "F"

def test_invalida():
    calcular_nota_para_conceito(-0.2)
    calcular_nota_para_conceito(-0.1)
    calcular_nota_para_conceito(10.1)
    calcular_nota_para_conceito(10.2)