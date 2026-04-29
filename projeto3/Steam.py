import os
import csv
from jogo import Jogo
from filaBacklog import FilaBacklog
from pilhaRecentes import PilhaRecente 

backlog = FilaBacklog()
recentes = PilhaRecente(limite=20)

catalogo = []
jogos_por_id = {}

arquivo = 'dataset.csv'

with open(arquivo, newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    cabeçalho = next(spamreader)
    print(f"Cabeçalho do CSV: {cabeçalho}")
    
    contador = 0

    for row in spamreader:
        try:
            id_jogo = int(row[0]) if row[0].isdigit() else contador
            titulo = row[1]
            console = row[2]
            genero = row[3]
            publisher = row[4]
            developer = row[5]
            critic_score = row[6]
            total_sales = row[7]
            na_sales = row[8]
            jp_sales = row[9]
            pal_sales = row[10]
            other_sales = row[11]
            release_date = row[12]

            #CRIAR OBJETO "JOGO"
            jogo = Jogo(
                id_jogo, titulo, console, genero, publisher, developer,
                critic_score, total_sales, na_sales, jp_sales, 
                pal_sales, other_sales, release_date
            )
            
            #ADICIONAR AO BACKLOG
            catalogo.append(jogo)
            jogos_por_id[id_jogo] = jogo
            contador += 1
        except Exception as e:
            print(f"ERRO: {e}")
            print(f"Linha problemática: {row}")

print(f"Total de jogos carregados: {len(catalogo)}")