# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import csv

def lerArquivo():

    arquivo_selecionado = askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("Tabela de dados", "*.csv")]
    )

    if arquivo_selecionado:

        temperaturas_por_mes = {}

        with open(arquivo_selecionado, "r", encoding="utf-8") as dados:
            leitor = csv.reader(dados)
            next(leitor)

            for linha in leitor:
                id_mes = int(linha[0])
                temperatura = float(linha[2])

                if id_mes not in temperaturas_por_mes:
                    temperaturas_por_mes[id_mes] = []
                temperaturas_por_mes[id_mes].append(temperatura)

        print("Média de temperatura por mês:")
        for id_mes, temperaturas in temperaturas_por_mes.items():
            media = sum(temperaturas) / len(temperaturas)
            print(f"Mês {id_mes}: {media:.2f}°C")

    else:
        print("Nenhum arquivo selecionado.")

lerArquivo()

# from tkinter import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename
# import csv

# arquivo_selecionado = askopenfilename(
#     title="Selecione um arquivo",
#     filetypes=[("Tabela de dados", "*.csv")]
# )

# with open(arquivo_selecionado, "r") as dados:
#     leitor = csv.reader(dados)
#     next(leitor)

#     for linha in leitor:
#         id_mes = int(linha[0])
#         mes = linha[1]
#         temperatura = float(linha[2])

#         for id_mes in linha:
#             print(len(temperatura))

            # temperatura_media = temperatura

            # print(f"Mês: {mes} | Temperatura média: {temperatura_media}")


        # print(f"Mês: {mes} | Temperatura: {temperatura}\n")

# if arquivo_selecionado:
#     print(arquivo_selecionado)
# else:
#     print("Nenhum arquivo selecionado.")
