def aplicar_cupom(codigo: str, valor_compra: float):
    if codigo.lower() == "cupom10":
        return 0.10
    
    elif codigo.lower() == "cupom25" and valor_compra > 100.00:
        return 0.25
    
    elif codigo.lower() == "descontovip" and valor_compra > 500.00:
        return 0.35
    
    return 0.0