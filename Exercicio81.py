"""Crie um programa que vai ler vários npumeros e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados
b) A lista de valores, ordenada de forma decrescente
c)Se o valor  5 foi digitado e esta ou não na lista"""

continuar = 'S'
numeros = []

while continuar == 'S':
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)

    continuar = str(input('Deseja continuar [S/N]')).strip().upper()

numeros.sort(reverse=True)
print(numeros)
print(f'Essa lista tem {len(numeros)} elementos')

if 5 in numeros:
    print(f'O valor 5 foi digitado e esta  na lista')
else:
    print(f'O valor 5 não foi digitado e não esta a lista')

