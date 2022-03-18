n1 =float(input ('Digite a largura da parede: '))
n2 = float (input ('Digite a altura da parede: '))
total = n1 * n2
tinta =  total  / 2
print(' A parede tem {}m². Sera necessario {:.1f} lata de tinta.' .format(total, tinta))