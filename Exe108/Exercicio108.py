"""Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado."""
import moeda

num = float(input('Digite o preço: R$ '))

print(f'Aumentado 10% de  {moeda.moeda(num)} é  {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Diminuindo 10% de  {moeda.moeda(num)} é  {moeda.moeda(moeda.diminuir(num, 10))}')
print(f'O dobro de  {moeda.moeda(num)} é  {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de  {moeda.moeda(num)} é  {moeda.moeda(moeda.metade(num))}')

#Primeira referencia de moeda é do modulo e o segundo moeda é da função