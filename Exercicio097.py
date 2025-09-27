"""Faça um programa que tenha uma função escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel da linha"""

def escreva(msg):
    print('~' * (len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))

escreva('Suzana Lopes de Azevedo')
escreva('CURSO EM VIDEO')
escreva('Gustavo Guanabara é um ótimo professor')
escreva('Olá')