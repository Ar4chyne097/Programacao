def calcular_bonus(salario_base: float, avaliacao: str):
    if avaliacao == "Excelente":
        return (salario_base * 1.20)

    elif avaliacao == "Bom":
        return (salario_base * 1.10)

    elif avaliacao == "Regular":
        return (salario_base * 1.02)

    elif avaliacao == "Ruim":
        return salario_base