"""Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),dobro() e metade().
faça também um programa que importe esses modulos e use algumas dessas funções"""
import moeda

num = float(input(' Digite o preço: R$ '))

print(f'Aumentado 10% de R$ {num} é R$ {moeda.aumentar(num, 10)}')
print(f'Diminuindo 10% de R$ {num} é R$ {moeda.diminuir(num, 10)}')
print(f'O dobro de R$ {num} é R$ {moeda.dobro(num)}')
print(f'A metade de R$ {num} é R$ {moeda.metade(num)}')

