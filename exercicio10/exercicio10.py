# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves

import matplotlib.pyplot as plt

def gerar_grafico_temperaturas(temperaturas_maximas, temperaturas_minimas, dias):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(dias, temperaturas_maximas, width=0.3, label="Temperatura Máxima", align="center", color="orange")
    ax.bar(dias, temperaturas_minimas, width=0.3, label="Temperatura Mínima", align="edge", color="lightblue")

    ax.set_title('Temperaturas dos Últimos 7 Dias')
    ax.set_xlabel('')
    ax.set_ylabel('Temperatura (°C)')

    ax.legend()

    plt.tight_layout()
    plt.show() 
dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
temperaturas_maximas = []
temperaturas_minimas = []

print("Temperaturas nos últimos 7 dias\n")

for dia in dias:
    temp_max = float(input(f"Temperatura máxima de {dia}: "))
    temp_min = float(input(f"Temperatura mínima de {dia}: "))
    
    temperaturas_maximas.append(temp_max)
    temperaturas_minimas.append(temp_min)
gerar_grafico_temperaturas(temperaturas_maximas, temperaturas_minimas, dias)