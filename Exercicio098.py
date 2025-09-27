"""Faça um programa que tenha uma função chamada contador(),
que receba tres parametros: inicio, fim e passo e realize a contagem

Seu programa tem que realizar 3 contagens através da função criada:

A)De 1 a 10, de 1 em 1
B)De 10 até 0, de 2 em 2
c)Uma contagem personalizada, crescente, decrescente, positivo e negativo, caso zero contar positivo ou negativo de 1 em 1
"""
from time import sleep

def contador():
    print(50 * '-*')
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11,1):
        sleep(0.1)
        print(f'{i}, ', end='')
    print(' Fim')

    print(50 * '-*')

    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10,0,-2):
        sleep(0.1)
        print(f'{i}, ', end='')
    print(' Fim')

    print(50 * '-*')

    print('<<< --- AGORA É SUA VEZ --- >>>' )

    inicio = int(input('Digite o primeiro numero: '))
    fim = int(input('Digite o ultimo numero: '))
    passo = int(input('Digite o passo de contagem de numero positivo (para ordem crescente) ou negativo (para ordem decrescente): '))


    if passo == 0:
        passo = 1
        print('Você digitou 0 no passo, será contabilizado de 1 em 1')
        if fim  < 0 or fim < inicio:
            passo = -1
        if inicio < fim:
            passo = +1
        for i in range(inicio, fim, passo):
            sleep(0.5)
            print(f'{i}, ', end='')
        print('Fim')


    else:
        for i in range(inicio, fim, passo):
            sleep(0.5)
            print(f'{i}, ', end='')
        print('Fim')

contador()