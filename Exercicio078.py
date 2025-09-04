"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final mostre qual foi o maior e o menor valor digitado e as suas  respectivas posições na lista """


valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um número inteiro: ')))
print(f'Números digitados {valores}')

maior_v= max(valores)
menor_v= min(valores)

print(f'O valor {maior_v} apareceu  na {valores.index(maior_v)+1}ª posição')
print(f'O valor {menor_v} apareceu  na {valores.index(menor_v)+1}ª posição')

