"""Faça um programa que tenha uma lista chamada numeros(),
duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear 5 números e vai coloca-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior"""
from random import randint
import random
from time import sleep

def sorteio(lista):
    print(40 * '-', 'SORTEANDO CINCO VALORES DA LISTA',40 * '-')
    for cont in range(0,5):
        n= randint(1,20)
        lista.append(n)
        print(f'{n}, ', end='', flush=True)
        sleep(0.3)
    print('')
    print('Sorteio dos números realizado')
    print(100 * '-')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma +=valor
    print(f'Somando os valores pares de {lista}, temos o resultado: {soma}')

numeros = list()

sorteio(numeros)
somaPar(numeros)

