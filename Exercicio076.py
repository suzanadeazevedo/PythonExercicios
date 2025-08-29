"""Crie um programa que tenha uma tupla única com nomes de prodtos e seus respectivos preços, na sequencia.
No final mostre uma listagem de preços, organizando os dados em forma tabular"""
lista_produtos = (
    'Lápis', 1.75,
    'Borracha', 1.15,
    'Caderno 96f', 25.75,
    'Estojo', 18.99,
    'Caneta Bic cor', 3.99,
    'Livro Ditatico 1', 95.75,
    'Lápis de cor 36c', 69.99)

print(100 * '*')
print(f'{"LISTAGEM DE PREÇOS":^100}')
print(100 * '*')
for pos in range(0, len(lista_produtos)):
    if pos % 2 == 0:
        print(f'{lista_produtos[pos]:.<100} ', end=" ")
    else:
        print(f'R${lista_produtos[pos]:>7.2f}')

"""print(100 * '*')
print(f'{"LISTAGEM DE PREÇOS":^100}')  # centralizado
print(100 * '*')

for pos in range(0, len(lista_produtos), 2):
    nome = lista_produtos[pos]
    preco = lista_produtos[pos+1]
    print(f'{nome:.<80}R${preco:>8.2f}')"""