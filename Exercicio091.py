"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
Guarde esses resultados em um dicionnario.
No final, coloque esse dicionario em ordem, sabend0 que o vencedor tirou o maior número no dado
O porgrama joga sozinho"""

from random import  randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)
        }
ranking = list()

print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('')
print('-='*10, 'RANKING',10*'=-')
print('')

for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

