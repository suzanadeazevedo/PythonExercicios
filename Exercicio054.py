from datetime import date

print('Grupo de Nascimento de sete pessoas :: Maiores e Menores de idade')
year = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    birth = int(input('Em que ano a {}ª pessoa nasceu: '.format(pessoa)))
    age = year - birth
    if age >= 18:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todos temos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo temos {} pessoas menores de idade'.format(totmenor))
