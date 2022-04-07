print('Será que fui multado???')

velocidade = float(input('Digite a velocidade (km) que o carro passou no radar: '))
multa = float (velocidade - 80) * 7
if velocidade<=80:
    print('Você não foi multado')
else:
    print('Você foi multado em: R$ {:.2f}'.format(multa))
    print('O limite de velocidade é 80 km. Cada 1 km acima  da velocidade você é multado em R$ 7,00')
