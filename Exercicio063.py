print(90* '- ')
print( 18 * '-*' , '    SEQUENCIA DE FIBONACCI      ', 18* '-*')
print(90 * '- ')

termos= int(input('Quantos termos você quer mostrar: '))
a= 0
b=1
print(90 * '- ')
print('{} → {}'.format(a, b), end='')

cont =3

while cont <= termos:
   c = a + b
   print(' → {}'.format(c), end='')
   a = b
   b = c
   cont += 1
print(' → FIM')
