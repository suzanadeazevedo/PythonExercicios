"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""


def ficha(nomeJogador = ' ', golsMarcados = 0 ):
    nomeJogador=str(input('Digite o nome  do jogador: '))
    if nomeJogador == '':
        nomeJogador = '<desconhecido>'
    golsMarcados=str(input(f'Digite quantos gols o {nomeJogador} marcou: '))
    if golsMarcados.isnumeric():
        golsMarcados = int(golsMarcados)
    else:
        golsMarcados = 0
    print(f'O jogador {nomeJogador} fez {golsMarcados} gol(s) no campeonato')

ficha()
