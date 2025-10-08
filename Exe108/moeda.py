"""EXERCICIO 108"""


def aumentar(valor=0, taxa=0):
    res = valor + (valor * (taxa / 100))
    return res


def diminuir(valor=0, taxa=0):
    res = valor - (valor * (taxa / 100))
    return res


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2


def moeda(valor=0, moeda='R$ '):
    return f'{moeda}{valor:>2.2f}'.replace('.', ',')
