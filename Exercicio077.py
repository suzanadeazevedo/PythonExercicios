"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ('Suzana',
            'mapa',
            'python',
            'programacao',
            'pilar',
            'menino',
            'amigo',
            'animais',
            'sobrenome',
            'morango',
            'sol',
            'longe')
vogais = 'aeiou'

print(20 * '-')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vogais:', end='')
    for letra in palavra.lower():
        if letra in vogais:
            print(letra, end='' )
    print()

print(20 * '-')
