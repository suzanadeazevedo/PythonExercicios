"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
no final mostre a matriz na tela, com a formatação correta
[0,0][0,1][0,2]
[1,0][1,1][2,2]
[2,0][2,1][2,2]
"""

"""estrutura_matriz = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
]"""
colunas = 3
matriz = []

for l in range(colunas):
    linha = []
    for c in range(colunas):
        numero = (int(input(f'Digite o número que ficara armazenado {l},{c}: ')))
        linha.append(numero)
    matriz.append(linha)
print(matriz)
print(50 * '_')
for l in range(colunas):
    for c in range(colunas):
        print(f'[{matriz[l][c]}]', end='')
    print()



"""Resolucao Guanabara 
matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
    matriz[l][c] = int(input(f'Digite o número que ficara armazenado {l},{c}: ' ))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()
"""