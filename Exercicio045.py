from random import randint
from time import sleep

print("=" * 45)
print("                              JOGO: JOKENPÔ")
print("=" * 45)

print(''' Escolha uma opção: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input("Qual é sua escolha: "))

if jogador <= -1 & jogador >= 4:
    print('Opção Invalida')
    breakpoint(exit())

print('-=' * 25)
print('O computador jogou: {}'.format(itens[computador]))
print('Você jogou: {}'.format(itens[jogador]))
print('-=' * 25)

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ')
sleep(1)

print('RESULTADO:')

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('\o/ Você ganhou \o/')
    elif jogador == 2:
        print('Você perdeu :(')



if computador == 1:
    if jogador == 0:
        print('Você perdeu :(')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('\o/ Você ganhou \o/')


if computador == 2:
    if jogador == 0:
        print('\o/ Você ganhou \o/')
    elif jogador == 1:
        print('Você perdeu :(')
    elif jogador == 2:
        print('Empate')


