"""Crie um programa que vai ler vários numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final  mostre o conteúdo das três listas geradas"""

continuar = 'S'
numeros = []


while continuar == 'S':
    numero = int(input('Digite um número inteiro: '))
    numeros.append(numero)

    continuar = str(input('Deseja continuar [S/N]')).strip().upper()

numeros.sort()
print(numeros)

pares =[n for n in numeros if n % 2 == 0]
print(f'Os numeros pares são: {pares}')

impares = [n for n in numeros if n % 2 != 0]
print(f'Os numeros impares são: {impares}')
