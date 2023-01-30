contador_idade = contador_masculino = contador_feminino_menor_vinte = 0

while True:
    print(' CADASTRE UMA PESSOA')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        contador_idade += 1
    if sexo == 'M':
        contador_masculino += 1
    if sexo == 'F' and idade <= 20:
        contador_feminino_menor_vinte += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos{contador_idade}')
print(f'Total de {contador_masculino} homem(ns) cadastrados')
print(f'Total de {contador_feminino_menor_vinte} mulher(es) menores de 20 anos')
