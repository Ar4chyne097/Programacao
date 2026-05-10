def calcular_frete(kg: float):
    if kg <= 0.0:
        return 0
    elif kg <= 1.0:
        return 5.00
    elif kg <= 5.0:
        return 10.00
    
    return 18.00