"""Crie um proggrama que gerencie o  aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feios em cada partida.
No final td sera guardado em um dicionario, incluindo o total de gols, feitos durante o campeonato.
Saida é um jogador individual"""

jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))

for c in range(0,tot):
    partidas.append(int(input(f'  Quantos gols na partida {c}?: ')))

jogador['gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print('')
print(80 * '-=')
print('')
print(jogador)
print('')
print(80 * '-=')
for k, v in jogador.items():
    print(f'---> {k} : {v}')
print(80 * '-=')
print('')

print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas')

for  i, v in enumerate(jogador['gols']):
    print(f'    ---> Na partida {i}, fez {v} gols. ')
print(f'Foi um total de  {jogador["Total"]} gols')
