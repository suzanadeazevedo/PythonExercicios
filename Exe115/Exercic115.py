from time import sleep
from Exe115.lib.interface import *
from Exe115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoas','Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        print('--->>> PROGRAMA ENCERRADO <<<---')
        break
    else:
        print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')
    sleep(1)