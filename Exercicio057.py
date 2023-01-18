#Programa que leia o sexo da pessoa, mas só aceita F ou M, se for diferente pedir pra digitar novamente

sexo = str(input('Digite o sexc da pessoa [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Valor invalido. Digite novamente o Sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} regitrado com sucesso'.format(sexo))