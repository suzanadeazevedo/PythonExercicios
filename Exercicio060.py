print(81 * '- ')
print( 20 * '-*' , '    CALCULO FATORIAL      ', 20 * '-*')
print(81 * '- ')

n1 = int(input('Digite o número para fatorar: '))
c = n1
fatorial = 1
print('Calculando {}! = '.format(n1), end='')
while c > 0:
    print('{}'. format(c), end ='')
    print(' x ' if c > 1 else ' = ', end = '' )
    fatorial *= c
    c  -= 1
print('{}'.format(fatorial))