"""Crie um programa onde o usuario possa digitar cinco valores númericos e cadastre-os em uma lista,
já na posiçã correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela"""

lista = []
for elemento in range(0,5):
    numero = (int(input('Digite um número inteiro: ')))
    if elemento == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos +=1

print(f'Números digitados {lista}')