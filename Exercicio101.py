"""Crie um programa que tenha uma função chamada voto()
 que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
 indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""


def voto():
    from datetime import datetime
    ano = int(input('Digite em que ano você nasceu (quatro digitos): '))
    calculoIdade = datetime.now().year - ano

    if calculoIdade <= 15:
        print(f'Com {calculoIdade} anos: Voto NEGADO')
    elif calculoIdade >= 16 and calculoIdade <= 17:
        print(f'Com {calculoIdade} anos: Voto OPCIONAL')
    elif calculoIdade >= 18 and calculoIdade <= 69:
        print(f'Com {calculoIdade} anos: Voto OBRIGATORIO')
    else:
        print(f'Com {calculoIdade} anos: Voto OPCIONAL')

voto()