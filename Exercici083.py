"""Crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta"""

expressao = str(input('Digite a expressão: '))

pilha= []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expressão esta certa')
else:
    print(f'Sua expressão esta errada')