"""Desenvolva um programa que leia quatro valores pelo teclado e guarde os em uma tupla. No final mostre:
1 Quantas vezzes aparece o valor 9
2 Em que posição foi digitado o primeiro valor 3
3 Quais foram os números pares"""
num =(int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite um  ultimo número: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu  {num.count(9)}')

if 3 in num:
    print(f'O valor 3 apareceu  na {num.index(3)+1}ª posição')
else:
    print(f'O valor 3 apareceu  não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end= ' ')
for n in num:
    if n % 2 == 0:
       print(f'{n},', end = ' ')
