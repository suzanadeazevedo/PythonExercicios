from random import shuffle

print('*****    Sorteio da Ordem de Apresentação   *****')

primeiro = str (input('Digite o primeiro nome; '))
segundo = str  (input('Digite o segundo nome: '))
terceiro = str  (input('Digite o terceiro nome: '))
quarto = str  (input('Digite o quarto nome: '))

lista = [primeiro, segundo, terceiro, quarto]

shuffle(lista)

print(' A ordem de apresentação será:')
print (lista)