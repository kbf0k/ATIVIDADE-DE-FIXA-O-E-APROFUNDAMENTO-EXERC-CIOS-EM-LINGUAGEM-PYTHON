# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves
def cadastra_produto():

    listas = []
    for i in range(1,6):
        nome_produto = input(f'Digite o nome do produto {i}: ')
        preco_produto = float(input(f'Digite o preço do produto {i}: '))
        quantidade_produto = int(input(f'Digite o quantidade do produto {i}: '))

        lista = {'Nome':nome_produto,
                 'Preço':preco_produto,
                 'Quantidade':quantidade_produto
                 }
        
        listas.append(lista)
        print('\nProdutos Cadastrados:')

        for i in listas:
            print(i)

cadastra_produto()