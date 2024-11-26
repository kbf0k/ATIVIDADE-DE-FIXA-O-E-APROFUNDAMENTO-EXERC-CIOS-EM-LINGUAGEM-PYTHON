# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves
def cidade_maior_temperatura(dados_climaticos):
    
    cidade_maior_temp = None
    maior_temp = float('-inf')
    
    for cidade, dados in dados_climaticos.items():
        if dados['temperatura'] > maior_temp:
            maior_temp = dados['temperatura']
            cidade_maior_temp = cidade
    
    return cidade_maior_temp

dados_climaticos = {
    'São Paulo': {'temperatura': 25, 'umidade': 60, 'velocidade do vento': 10},
    'Rio de Janeiro': {'temperatura': 30, 'umidade': 55, 'velocidade do vento': 12},
    'Curitiba': {'temperatura': 22, 'umidade': 65, 'velocidade do vento': 8},
    'Belo Horizonte': {'temperatura': 28, 'umidade': 50, 'velocidade do vento': 15}
}

cidade_com_maior_temp = cidade_maior_temperatura(dados_climaticos)
print(f'A cidade com a maior temperatura é: {cidade_com_maior_temp}')
