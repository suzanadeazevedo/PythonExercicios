somaidade = 0
mediaidade = 0
maior_idade_homem = 0
nome_homem= ''
tot_mulher_maior_de_vinte =0
for pessoa in range(1,5):
    print('---------{}ª PESSOA----------'.format(pessoa))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo =  str (input('Digite o sexo [F/M]: ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher_maior_de_vinte +=1

mediaidade = somaidade / 4
print('\n-------------------------------------------------------------------------------------------------------------------')
print('A media de idade do grupo é de {} anos'. format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maior_idade_homem, nome_homem))
print('Há {}  mulher(es) com menos de 20 anos'.format(tot_mulher_maior_de_vinte))
