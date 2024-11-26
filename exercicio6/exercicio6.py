# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves
def calcula_media_temperatura():
    cidade = {'Caçapava':23.2,
              'São José dos Campos':45.2,
              'Taubaté':34.23,
              'Pindamongaba':35.6,
              'Jacaréi':34.5 }
    
    for nome, temperatura in cidade.items():
        print(f'{nome}: {temperatura}°C')
    print(f'A média das temperaturas é: {sum(cidade.values())/len(cidade):.2f}')
calcula_media_temperatura()