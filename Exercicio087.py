"""Aprimoreo desafio anterios, mostrado no final:
A) A soma  de todos os valores pares digitados.
B) A soma dos valores da terceira coluna
C) O maior valor da segunda  linha"""

colunas = 3
matriz = []
soma_par = maior_numero = soma_coluna = 0

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
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]

    print()

print(50 * '_')
print(f'Soma dos valores pares: {soma_par}')
for l in range(colunas):
    soma_coluna +=matriz[l][2]
print(f'Soma dos valores da terceira coluna: {soma_coluna}')
for c in range(colunas):
    if c  == 0:
        maior_numero =matriz[1][c]
    elif matriz[1][c] > maior_numero:
        maior_numero = matriz[1][c]
print(f'O maior número da segunda linha é: {maior_numero}')


