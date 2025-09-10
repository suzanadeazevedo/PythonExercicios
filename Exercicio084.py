"""Faça um proggrama que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas, peso maior
C) Uma listagem com as  pessoas mais leves, peso menor"""

pessoas = []
dados = []
continuar = 'S'
total_maior = total_menor = 0
maior_peso = menor_peso = 0


while continuar == 'S':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar [S/N]')).strip().upper()

print(50 * '_')
print(pessoas)
print(50 * '_')
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print(50 * '_')

print(f'O maior peso cadastrado foi {maior_peso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso cadastrado foi {menor_peso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end='')

