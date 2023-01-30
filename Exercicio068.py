from random import randint

print(90 * '- ')
print(18 * '-*', '   JOGO PAR OU IMPAR      ', 18 * '-*')
print(90 * '- ')
contador = 0

while True:
    escolha = int(input('DIgite um número: '))
    computador = randint(0, 11)
    total = escolha + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?: [P/I]')).strip().upper()[0]
    print(f'Você jogou {escolha} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU ')
            contador = + 1
        else:
            print('Você PERDEU :(')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            contador = + 1
        else:
            print('Você PERDEU :(')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER! Você venceu {contador} vezes')
