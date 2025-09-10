"""Crie um progama que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a media  de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente"""

pessoas = list()
dados = []
continuar = 'S'


while continuar == 'S':
    dados.append(str(input('Nome do Aluno: ')))
    dados.append(float(input('1ª Nota: ')))
    dados.append(float(input('2ª Nota: ')))
    media = (dados[1] + dados [2]) / 2
    dados.append(media)

    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar [S/N]')).strip().upper()

print(50 * '_')
print(f'{"Nº ":<4} {"NOME: ":<10} {"MÉDIA: ":>8}')
print(50 * '_')
for i,  a in enumerate(pessoas):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')

while True:
    print(50 * '_')
    notas_individual = int(input('Mostrar nota do aluno? (Para sair digite: 404) '))
    if notas_individual == 404:
        print('Programa Finalizado')
        break
    if notas_individual <= len(pessoas) -1:
        print(f'As notas de: {pessoas[notas_individual] [0]}, são: Nota 1:  {pessoas[notas_individual][1]} , Nota 2:{pessoas[notas_individual][2]}')
print('Programa Encerrado')


"""print('> EXERCÍCIO 089 DE PYTHON <\n')
dados = []
while True:
	cont = ' '
	nome = str(input('nome: '))
	nota1 = float(input('nota 1: '))
	nota2 = float(input('nota 2: '))
	media = (nota1 + nota2) / 2 
	dados.append([nome, [nota1, nota2], media])
	cont = str(input('\nQuer continuar? [s/n]: ')).strip()
	if cont == 'n':
		break
#(not important)
print('---' * 11)
print(f'{"Nº":<4} {"Nome":<10} {"Média":>8}')
print('---' * 11)
# nome e média geral
for e, d in enumerate(dados):
	print(f'{e:<4} {d[0]:<10} {d[2]:>8.1f}')
print('---' * 11)

while True:
	opc = int(input('\nMostrar nota de qual aluno? (999 interrompe o programa) '))
	#nome e nota individual
	if opc <= len(dados)-1:
		print(f'\nNotas de {dados[opc][0]}: {dados[opc][1]}')
		print('---' * 11)
	if opc == 999:
		print('\n> Volte Sempre <')
		break"""