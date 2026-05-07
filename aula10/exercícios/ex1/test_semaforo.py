from semaforo import acao_semaforo

def test_rojo():
    assert acao_semaforo("Vermelho") == "Pare"

def test_amarillo():
    assert acao_semaforo("Amarelo") == "Atenção"

def test_vierde():
    assert acao_semaforo("Verde") == "Siga"

def test_corErrada():
    assert acao_semaforo("Azul") == "Cor Inválida"
    assert acao_semaforo("Rosa") == "Cor Inválida"
    assert acao_semaforo("Violeta") == "Cor Inválida"