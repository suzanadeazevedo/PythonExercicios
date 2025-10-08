"""EXERCICIO 107 -  MODULOS

Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),dobro() e metade().
faça também um programa que importe esses modulos e use algumas dessas funções"""

def aumentar(valor, taxa):
     res = valor + (valor * (taxa/100))
     return res

def diminuir(valor, taxa):
    res = valor - (valor * (taxa / 100))
    return res

def dobro (valor):
    return valor * 2

def metade (valor):
    return valor / 2
