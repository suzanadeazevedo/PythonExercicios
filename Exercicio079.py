"""Crie um ptograma onde o usuario possa digitar varios valores numericos e cadastre os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente"""
continuar = 'S'
numeros = []

while continuar == 'S':
    numero = int(input('Digite um número inteiro: '))


    if numero in numeros:
        print(f"Número já cadastrado")
    else:
        numeros.append(numero)
    continuar = str(input('Deseja continuar [S/N]')).strip().upper()


numeros.sort()
print(numeros)



