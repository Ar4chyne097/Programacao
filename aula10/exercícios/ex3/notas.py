def calcular_nota_para_conceito(nota: float):
    if nota < 0 or nota > 10.0:
        return "Nota Inválida"
    elif nota < 3.0:
        return "F"
    elif nota <= 4.9:
        return "D"
    elif nota <= 6.9:
        return "C"
    elif nota <= 8.9:
        return "B"
    else:
        return "A"