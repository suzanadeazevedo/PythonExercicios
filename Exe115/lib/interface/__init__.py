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


def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('Digite o número da opção desejada: ')
    return  opc