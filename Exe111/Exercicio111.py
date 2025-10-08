"""Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafio 107, 108, e 109 para o primeiro pacote e mantenha tudo funcionando"""

from Exe111.utilidadescev import moeda


num = float(input('Digite o preço: R$ '))
moeda.resumo(num)