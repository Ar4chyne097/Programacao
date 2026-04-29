from jogo import Jogo
from datetime import datetime

class SessaoJogo:
    def __init__(self, jogo, tempo_jogado, tempo_total=0.0, data_sessao =''):
        self.jogo = jogo
        self.tempo_jogado = tempo_jogado
        self.tempo_total = tempo_total

        if data_sessao == '':
            self.data_sessao = datetime.now().strftime('%Y-%m-%d')
        else:
            self.data_sessao = data_sessao

        self.status = self.definir_status()
    
    def definir_status(self):
        if self.tempo_total < 2:
            return "Iniciado"
        elif self.tempo_total >= 2 and self.tempo_total <= 10:
            return "Em Andamento"
        elif self.tempo_total > 10 and self.tempo_total <= 20:
            return "Muito Jogado"
        elif self.tempo_total > 20:
            return "Concluído Simbolicamente"

    def exibir(self):
        print(f'Jogo: {self.jogo}')
        print(f'Tempo da Sessão: {self.tempo_jogado}')
        print(f'Tempo Total: {self.tempo_total}')
        print(f'Data: {self.data_sessao}')
        print(f'Status: {self.status}')

    def historico(self):
        resultado = f'{self.jogo.id};{self.jogo.titulo};{self.tempo_jogado:.2f};{self.data_sessao};{self.tempo_total};{self.status}'
        return resultado