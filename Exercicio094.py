"""Crie um programa que leia o nome, o sexo e a idade de varias pessoas, gurdando os dados  de cada pessoa  em um dicionario e todos os dicionarios em uma LISTA.
No final mostre:
A)Quantas pessoas foram cadastradas.
B)A média de idade do grupo.
C)Uma lista com todas as mulheres.
D)Uma lista com todas as pessoas  com idade acima da média"""

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['Nome'] =  str(input('Nome: '))
    while True:
        pessoa['Sexo'] =  str(input('Sexo (M ou F):  ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO: ---> Por favor, digite apenas M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa ['Idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar a cadastrar? (S ou N)')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO: ---> Por favor, responda apenas S ou N')
    if resposta =='N':
        break

print('')
print(80 * '-=')
print('')

print(f'Ao todo foram cadastradas {len(galera)} pessoas cadastradas.')

media = soma / len(galera)

print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')

for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}, ', end='')
print()

print('Lista das pessoas com idade acima da media: ', end='')
for p in galera:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<FINALIZADO>>>')



