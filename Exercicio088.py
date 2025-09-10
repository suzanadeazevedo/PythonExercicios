"""Faça  um programa que ajude o jogadorda Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta"""

import random


lista = list()
matriz = list()

print (100*' ')
print (100*'-')
print (f'{"PALPITES MEGA-SENA":^100}')
print (100*'-')
print (100*' ')

qnt_jogos = (int(input('Quantos jogos deseja fazer: ')))
for jogos in range(qnt_jogos):

    for contador in range(6):
        sorteio_numeros = random.randint(0, 61)
        if  sorteio_numeros  not in lista:
            lista.append(sorteio_numeros)
    matriz.append(lista[:])
    lista.clear()
for indice, linha in enumerate(matriz):
    linha.sort()
    print(f'Jogo {indice+1}: {linha}')
print('-='*5, '<BOA SORTE!>', '-='*5)


"""---------------------------------------------------------
Resolução linhas finais minha, antes da correção do Guanabara, ultimo for foi modificado para mostrar o numero do jogo para usuario:
for item in matriz:
    item.sort()
    print(f'{item}')
    ------------------------------------------------
    """



"""GPT(sugeriu mudar meu código):
import random

matriz = list()

qnt_jogos = int(input('Quantos jogos deseja fazer: '))
for jogos in range(qnt_jogos):
    # random.sample pega 6 números únicos de 1 a 60
    lista = random.sample(range(1, 61), 6)
    lista.sort()          # organiza os números
    matriz.append(lista)

for item in matriz:
    print(item)"""


"""Guanabara:

import random
lista = list()
jogos = list()

print('-'*30)
print('           JOGA NNA MEGA SENA            ')
print('-'*30)

quant = int(input('Quantos jogos você quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 0
    while true:
        num = randint(1,60)
            if num not in lista:
                lista.append(num)
                cont +=1
            if cont >=:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot +=1
        print('-='*3,f'SORTEANDO {quant} JOGOS ', '-='*3)
        
for indice, linha in enumerate(jogos):
        print(f'Jogo {indice+1}: {linha}')
print('-='*5, '<BOA SORTE!>', '-='*5)
        """


