"""Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""
import moeda

num = float(input('Digite o preço: R$ '))

print(f'Aumentado 10% de  {moeda.moeda(num)} é  {(moeda.aumentar(num, 10,True))}')
print(f'Diminuindo 13% de  {moeda.moeda(num)} é  {(moeda.diminuir(num, 13,True))}')
print(f'O dobro de  {moeda.moeda(num)} é  {(moeda.dobro(num, True))}')
print(f'A metade de  {moeda.moeda(num)} é  {(moeda.metade(num,True))}')

