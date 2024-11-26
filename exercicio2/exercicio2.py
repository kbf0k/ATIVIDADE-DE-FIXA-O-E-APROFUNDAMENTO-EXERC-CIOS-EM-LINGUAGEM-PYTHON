# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves
def filtrar_eventos_catastroficos(eventos):
    
    eventos_filtrados = []

    for evento in eventos:
        if evento['intensidade'] > 7:
            eventos_filtrados.append(evento)
    
    return eventos_filtrados

eventos_catastroficos = [
    {'tipo': 'enchente', 'intensidade': 6},
    {'tipo': 'furacão', 'intensidade': 9},
    {'tipo': 'enchente', 'intensidade': 8},
    {'tipo': 'furacão', 'intensidade': 5},
    {'tipo': 'enchente', 'intensidade': 10}
]

eventos_filtrados = filtrar_eventos_catastroficos(eventos_catastroficos)
print('Eventos com intensidade maior que 7:')
for evento in eventos_filtrados:
    print(evento)
