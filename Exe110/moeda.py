"""Exercicio 110"""


def aumentar(valor=0, taxa=0, formato=False):
    res = valor + (valor * (taxa / 100))
    return res if format is False else moeda(res)


def diminuir(valor=0, taxa=0, formato=False):
    res = valor - (valor * (taxa / 100))
    return res if formato is False else moeda(res)


def dobro(valor=0, formato=False):
    res = valor * 2
    return res if not formato else moeda(res)


def metade(valor=0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)


def moeda(valor=0, moedaa='R$ ', formato=False):
    return f'{moedaa}{valor:>2.2f}'.replace('.', ',')


def resumo(valor=10, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Aumento de {taxaa}% : \t{aumentar(valor,taxaa,True)}')
    print(f'Redução de {taxar}% : \t{diminuir(valor, taxar, True)}')
    print('-' * 30)
