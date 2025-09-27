"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a area do terreno"""

def area():
    print('')
    print(15 * '-*', 'CALCULO DA AREA DO TERRENO',15 * '-*' )
    print('')
    largura = float(input('Digite a largura do terreno (metros): '))
    comprimento = float(input('Digite o comprimento do terreno (metros): '))
    calculo = comprimento * largura
    print(f'A área de um terreno de {largura} de largura x por {comprimento} de comprimento, é de {calculo} m²')

area()