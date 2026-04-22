def especialidad_top(consultas):
    cont = {}
    
    for consulta in consultas:
        esp = consulta['especialidade']
        
        if esp not in cont:
            cont[esp] = 0
        
        cont[esp] += 1
        
    maior = ''
    maxValor = -1
    
    for e in cont:
        if cont[e] > maxValor:
            maxValor = cont[e]
            maior = e
    
    return maior

def main():
    consultas = [
        {'paciente': 'Ana', 'especialidade': 'Cardiologia'},
        {'paciente': 'Carlos', 'especialidade': 'Ortopedia'},
        {'paciente': 'Beatriz', 'especialidade': 'Cardiologia'},
        {'paciente': 'João', 'especialidade': 'Cardiologia'},
    ]
    
    resultado = especialidad_top(consultas)
    print(f'Especialidade mais frequente: {resultado}')
    
main()