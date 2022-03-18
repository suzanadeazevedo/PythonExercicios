import math
print('Calcule o comprimento da hipotenusa\n')

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)

print('\n \nO comprimento do cateto oposto digitado foi {}\n O comprimento do cateto adjacente dijitado foi: {}\n O comprimento da hipotenusa é: {:.2f}'.format(oposto, adjacente, hipotenusa))
