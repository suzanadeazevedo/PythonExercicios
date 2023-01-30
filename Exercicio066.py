n = 0
soma = 0
contador = 0

while True:
    n = int(input('Digite um número para somar ou 999 para encerrar: '))
    if n == 999:
        break
    soma += n
    contador += 1
# print('A soma vale {}'.format(soma))
print(f'Foram digitados {contador}')
print(f'A soma vale {soma}')
