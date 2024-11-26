# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves
import statistics as st

nivel_rio = []
mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

for i in mes:
    nivel = float(input(f'Digite qual o nível do rio do mês de {i}: '))
    nivel_rio.append(nivel)
print(f'A mediana dos rios é: {st.median(nivel_rio)}\nA média é: {st.mean(nivel_rio):.2f}')