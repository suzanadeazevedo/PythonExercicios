print( "="*40)
print("                ÍNDICE DE MASSA CORPORAL")
print( "="*40)

altura = (float(input('Digite a sua altura em metros: ')))
peso = float(input('Digite o seu peso'))
print( 'Altura informada: {}\nPeso informado: {}'.format(altura, peso))

imc = peso / (altura ** 2)
print('Seu IMC é de: {:.1f}'.format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc <= 25:
    print("Você está no peso ideal")
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print("Você está com obesidade")
else:
    print("Você está com obesidade mórbida")

