"""Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionario.
No final, mostre o conteúdo na tela
ex:
Usuario digita o nome e a media, saida:
 'Nome é igual a Joaquim
 Média é igual a 4.5
 Situação  é igual a reprovado'
 """
aluno = dict()
aluno ['Nome'] = str(input('Nome do Aluno: '))
aluno ['Media'] = float (input(f'Média de {aluno["Nome"]}:  '))

if aluno['Media'] >=7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] <7:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('---'*30)

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
