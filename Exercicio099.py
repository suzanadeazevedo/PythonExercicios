"""Faça um programa que tenha uma função chamada maior(),
que receba varios paramentros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é maior"""

def maior(*num):
    cont = maior = 0
    print(50 * '-*')
    for valor in num:
        print(f'{valor}, ', end='')

        if cont == 0:
            maior =  valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print('')
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor encontrado foi {maior} .')



maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
