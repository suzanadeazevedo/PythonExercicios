"""Crie um programa onde o usuario possa digitar sete valores numéricos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
No final   mostre os valores pares e impares em ordem crescente
[[lista par],[lista impar]]
print[par]
print[impar]"""


numeros = []

for c in range(1,8):
  numeros.append(int(input(f'Digite o {c}º valor inteiro: ')))
print(f'Números digitados {numeros}')
print(50 * '_')

pares =[n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

pares.sort()
impares.sort()

print(f'Números digitados em ordem: {pares, impares}')
print(50 * '_')
print(f' Os valores pares digitados foram: {pares}')
print(f' Os valores pares digitados foram: {impares}')

"""Resolução Guanabara:
 num = [[],[]]
 valor = 0
 
 for c in range(1,8):
    valor = (int(input(f'Digite o {c}º valor inteiro: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f' Todos os valores: {num})

num[0].sort()
num[1].sort()

print(f' Os valores pares digitados foram: {num[0]}')
print(f' Os valores pares digitados foram: {num[1]}')
 
 """
