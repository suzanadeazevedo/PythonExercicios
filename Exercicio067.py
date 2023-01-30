print('TABUADA')
numero = 0
tabuada = 0
calculo = 0
while True:
    numero = int(input('Quer ver a tabuada de que número?: '))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
print('Não realizado tabuada de números negativos')

    #Metodo abaixo não funcionou, deixei para pesquisar o motivo
    # while tabuada < 10:
    #     tabuada += 1
    #     calculo = numero * tabuada
    #     print(f'{numero} x {tabuada} = {calculo}')