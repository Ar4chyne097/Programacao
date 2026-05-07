def acao_semaforo(str):
    if str.lower() == "vermelho":
        return "Pare"
    elif str.lower() == "amarelo":
        return "Atenção"
    elif str.lower() == "verde":
        return "Siga"
    return "Cor Inválida"