import random

# Sorteio de um aluno em 4 alunos

print('********  Sorteio de alunos  *********')

primeiro = (input('Digite o primeiro nome: '))
segundo = (input('Digite o segundo nome: '))
terceiro = (input('Digite o terceiro nome: '))
quarto = (input('Digite o primeiro nome: '))
lista = [primeiro, segundo, terceiro, quarto]

sorteado = random.choice(lista)

print('Os nomes digitados foram: \n{} \n{}\n{}\n{} \n \n ***O nome sorteado foi: {}***'.format(primeiro, segundo, terceiro,
                                                                                         quarto, sorteado))
