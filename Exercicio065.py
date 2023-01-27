print(90 * '- ')
print(18 * '-*', '    Somador de números      ', 18 * '-*')
print(90 * '- ')

numero = 0
continuar = 'S'
soma = 0
cont = 0
maior_valor = 0
menor_valor = 0

while continuar == 'S':
    numero = int(input('Digite um número inteiro: '))
    continuar = str(input('Deseja continuar [S/N]')).strip().upper()
    soma += numero
    cont += 1
    if cont == 1:
        maior_valor = menor_valor = numero
    else:
        if numero > maior_valor:
            maior_valor = numero
        if numero < menor_valor:
            menor_valor = numero

media =  soma / cont
print('Você digitou {} números e a media entre eles foi igual a {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi  {}'.format(maior_valor, menor_valor))

