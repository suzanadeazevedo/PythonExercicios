"""Exercicio 109"""


def aumentar(valor=0, taxa=0, format=False):
    res = valor + (valor * (taxa / 100))
    return res if format is False else moeda(res)


def diminuir(valor=0, taxa=0, formato=False):
    res = valor - (valor * (taxa / 100))
    return res if formato is False else moeda(res)


def dobro(valor=0,formato=False):
    res = valor * 2
    return res  if not formato  else moeda(res)


def metade(valor=0,formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)


def moeda(valor=0, moeda='R$ ',formato=False):
    return f'{moeda}{valor:>2.2f}'.replace('.', ',')
