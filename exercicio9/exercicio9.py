# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves

def classificar_impacto(intensidade):
    if intensidade < 4:
        return "Baixo impacto"
    elif 4 <= intensidade <= 7:
        return "Médio impacto"
    else:
        return "Alto impacto"

tipos_desastres = [
    "Tremor de terra",
    "Tsunami",
    "Deslizamento",
    "Ciclone",
    "Tempestade",
    "Onda de Calor"
]

resultados = {}

print("Classificação de Desastres Naturais\n")
print("Insira a intensidade de cada tipo de desastre.\n")

for desastre in tipos_desastres:
    while True:
        try:
            intensidade = float(input(f"{desastre} (0-10): "))
            if 0 <= intensidade <= 10:
                resultados[desastre] = classificar_impacto(intensidade)
                break
            else:
                print("Por favor, insira um valor entre 0 e 10.")
        except ValueError:
            print("Inválido. Por favor, insira um número.")

print("\nImpactos causados:\n")
for desastre, impacto in resultados.items():
    print(f"{desastre}: {impacto}")