import random
print('***********************************')
print ('---------JOGO DE ADIVINHAÇÃO---------')
print('***********************************')
escolha = int(input('\nEscreva um número entre 0 e 5 para tentar adivinhar qual número o PC escolheu:'))
numeros =  [0, 1, 2, 3, 4 ,5]
sorteado = random.choice(numeros)

if sorteado == escolha:
    print('Parabéns você adivinhou \o/')
else:
    print('Você errou  :(')
    print('O número escolhido foi: {}'.format(sorteado))
    print('---FIM---')
