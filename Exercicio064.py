print(90* '- ')
print( 18 * '-*' , '    Somador de números      ', 18* '-*')
print(90 * '- ')

valor =0
cont = 0
soma = 0
valor = int(input('Digite um numero inteiro ou 999 para parar: '))

while valor != 999:
    soma += valor
    cont += 1
    valor = int(input('Digite um numero inteiro ou 999 para parar: '))

#calculo =  soma -999
#print('Você digitou {} números e a soma entre eles foi igual a {}'.format(cont, calculo))

print('Você digitou {} números e a soma entre eles foi igual a {}'.format(cont, soma))