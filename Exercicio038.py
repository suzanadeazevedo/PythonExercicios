print('****   Comparação de Valores   ****')

first= float(input('Digite o primeiro número: '))
second=float(input('Digite o segundo número: '))

if first > second:
    print('O primeiro valor  digitado ({}) é maior do que o segundo ({})'. format(first, second))
elif second > first:
    print('O segundo valor digitado({}) é maior do que o primeiro ({})'.format(second, first))
else:
    print(' Não existe valor maior. O primeiro valor ({}) e o segundo ({}) são iguais'. format(first, second))