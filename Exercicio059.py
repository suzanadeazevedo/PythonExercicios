from time import sleep
print(81 * '- ')
print( 20 * '-*' , '    CALCULADORA      ', 20 * '-*')
print(81 * '- ')

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo número: '))
opcao = 0


while opcao != 7:
    opcao = int(input(''' Escolha uma opção: 
    [ 1 ] Somar
    [ 2 ] Subtrair
    [ 3 ] Multiplicar
    [ 4 ] Dividir
    [ 5 ] Maior
    [ 6 ] Novos Numeros
    [ 7 ] Sair do Programa '''))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e  {} é igual a {}'. format(n1, n2, soma))
    elif opcao == 2:
        subtracao = n1 - n2
        print('A subtração entre {} e  {} é igual a {}'.format(n1, n2, subtracao))
    elif opcao == 3:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e  {} é igual a {}'.format(n1, n2, multiplicacao))
    elif opcao == 4:
        divisao = n1 / n2
        print('A divisão entre {} e  {} é igual a {}'.format(n1, n2, divisao))
    elif opcao == 5:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif opcao == 6:
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo número: '))
    print(60 * "-==")

print('Finalisando...')
sleep(1)
print('Obrigada por utilizar nosso software. Até breve ^^ ')







