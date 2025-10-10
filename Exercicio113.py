"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')
            continue #continue volta pro while
        except (KeyboardInterrupt):
            print('\n\033[0;31m!Usuário preferiu não digitar o número!.\033[m')
            return 0

        else:
            return n


def leiaFloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')
            continue #continue volta pro while
        except (KeyboardInterrupt):
            print('\n\033[0;31m!Usuário preferiu não digitar o número!.\033[m')
            return 0

        else:
            return n


numInt = leiaInt('Digite um numero inteiro: ')
numFloat= leiaFloat('Digite um numero real: ')

print(f'O valor inteiro digitado foi: {numInt}\nO valor real digitado foi: {numFloat}')
