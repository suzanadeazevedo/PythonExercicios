"""Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estao na tupla"""

import random

gerar_numeros = tuple (random.randint (1,100)
                                            for _ in range(5))
print(f'Tupla Gerada: {gerar_numeros}')

ordenar_tupla = tuple(sorted(gerar_numeros))
print(f'Tupla Ordernada: {ordenar_tupla}')
print(f'Menor número: {ordenar_tupla[0]}')
print(f'Maior número: {ordenar_tupla[4]}')

print(f'Resolução Guanabara: O maior valor sorteado foi {max(gerar_numeros)}')
print(f'Resolução Guanabara: O menor valor sorteado foi {min(gerar_numeros)}')

