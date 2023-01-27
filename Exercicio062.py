print(90* '- ')
print( 18 * '-*' , '    GERADOR DE PROGUESSÃO ARITMÉTICA      ', 18* '-*')
print(90 * '- ')

primeiro= int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
continuar = 10
while continuar !=  0:
    total = total + continuar
    while cont <=total:
        print ('{} → '.format(termo), end= '')
        termo+= razao
        cont +=1
    print('PAUSA')
    continuar =int(input('Quantos termos você quer mostrar a mais?'))
print('A progressão mostrou {} termos no total'.format(total))
print("FIM")