import random
print('***********************************')
print ('---------JOGO DE ADIVINHAÇÃO---------')
print('***********************************')

escolha = int(input('\nEscreva um número entre 0 e 10 para tentar adivinhar qual número o PC escolheu:'))
numeros =  [ 1, 2, 3, 4 ,5, 6, 7 , 8, 9, 10]
sorteado = random.choice(numeros)
tentativas = 0

while sorteado != escolha:
    tentativas +=1
    if sorteado < escolha:
        escolha = int(input('Menos... Tente outra vez: '))
    else:
        escolha = int(input('Mais... tente outra vez: '))

print('Acertou na {}ª tentativa'.format(tentativas))
print('---FIM---')

'''Guanabara resolução:
from random import randint
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um numero entre 0 e 10)
print('Sera que você consegue adivinhar')
acertou = false
palpites +=1

while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    palpites +=1
    if jogador == computador
    acertou = true
    else: 
        if jogador < computador:
            print('Mais... tente outra vez')
        elif jogador > computador
            print('Menos... tente outra vez')
print('Acertou na {}ª tentativa. Parabens!!!').format(palpites)'''