"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
import math


def fatorial(number=0, show = False):
    from math import factorial
    number = int(input('Digite o numero para calcular fatorial: '))
    result = math.factorial(number)

    calculo = " x ".join(str(i) for i in range(1, number + 1))

    print(f'Resultado do fatorial {number} é: {result}')
    if show:
        print(f"Fatorial em passos: {number}! = {calculo} = {result}")



fatorial(show=True)


"""Resolução do Guanabara:

def fatorial(n, show=False)
    f = 1
    for c in range(n,  0, -1):
        if show:
            print(f'{c} x  ', end ='')
            if c> 1:
                print (' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))

"""

