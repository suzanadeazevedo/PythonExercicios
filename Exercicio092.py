"""Crie  um programa  que leia o nome, ano de nascimento e carteira de trabalho e casdastre-os (com idade atual) em um dicionario,
se por acaso o CTPS for diferente de zero, o dicionario receberá também o ano de contratação e salario.
Calcule e acrescente, alem da idade, com quantos anos vai se aposentar, depoiss de 35 anos de contribuição"""

from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite o ano de nascimento (4 digitos): '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Numero da Carteira de Trabalho, se não tiver CTPS digite 0: '))

if dados['CTPS'] != 0:
    dados['Contratacao'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salario atual: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (( dados['Contratacao'] + 35) - datetime.now().year)

print(50 * '-= ')
print('')

for k,v in dados.items():
    print(f' - {k}: {v}')