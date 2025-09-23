"""Aprimoreo DESAFIO 093 (gerenciador de aproveitamento de um jogador de futebol), para que ele funcione com varios jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""


time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}?: ')))
    jogador['gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar a cadastrar? (S ou N)')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO: ---> Por favor, responda apenas S ou N')
    if resposta == 'N':
         break

print(80 * '=-')
print('cod', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')
print()


print(80 * '**')
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(80 * '**')

while True:
    busca = int(input('Mostrar dados de qual jogador? (Digitar o cód, para encerrar o programa digite 999)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'---- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]} ----')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    ---> No jogo {i+1} fez {g} gols')
    print('---' * 30 )


print()
print('<<<--- Programa Encerrado --->>>')


