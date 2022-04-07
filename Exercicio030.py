print('O número é par ou impar?')

numero = int(input('Digite um número inteiro: '))
calculo = numero % 2
par= calculo == 0
print('O número digitado foi: {}'.format(numero))
if par:
    print('Este número é par')
else:
    print('Este numero é impar')