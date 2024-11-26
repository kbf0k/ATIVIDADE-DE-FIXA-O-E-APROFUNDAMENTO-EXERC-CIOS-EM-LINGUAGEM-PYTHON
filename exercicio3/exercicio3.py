# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves
def calcular_poupanca_diaria(valor_diario):
    
    dias_no_ano = 365
    
    poupanca_anual = valor_diario * dias_no_ano
    
    return poupanca_anual

valor_diario = float(input("Informe o valor que você pretende economizar diariamente: R$ "))
poupanca_anual = calcular_poupanca_diaria(valor_diario)
print(f"Você poupará ao final de um ano: R$ {poupanca_anual:.2f}")
