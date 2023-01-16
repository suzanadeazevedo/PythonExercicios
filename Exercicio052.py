#Números Primos
print('***********Descubra se o número é primo***********\n')

num =  int(input('Digite um número inteiro: '))
tot = 0

for c in range(1, num + 1):
    if num  % c ==0:
        print('\033[36m', end=' ')
        tot += 1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format(c), end =' ')
print('\n\033[m' 'O número {} foi divisível {} vezes'.format(num, tot))
if  tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele nao é primo')
