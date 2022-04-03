nome = str(input('Digite o seu nome completo: ')).strip()
print('O nome digitado foi: {}'. format(nome))

print('Nome em letras maiusculas: {}'.format(nome.upper()))
print('Nome em letras minusculas: {}'.format(nome.lower()))
print('Total de letras do nome: {}'.format(len(nome) - nome.count(' ')))
print('Total de letras do primeiro nome: {}'.format(nome.find(' ')))


print('\n\n******OUTRA FORMA DE MOSTRAR O TOTAL DO PRIMEIRO NOME*******')
fatiar = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(fatiar[0], len(fatiar[0])))