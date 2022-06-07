from datetime import date

print('------------------ALISTAMENTO--------------------')
birth = int(input('Digite o ano completo de seu nascimento (Exemplo: 1998):  '))
year=date.today().year
age= year - birth

if age == 18:
    print('Você tem {} anos e precisa se alistar esse ano'. format(age))
elif age > 18:
    print('Você tem {} anos e e ja deve ter se alistado em {} anos'. format(age, (age -18)))
    print('O ano do seu alistamento foi: {}'.format(birth + 18))
elif age < 18:
    time = (18 - age)
    print(' Você tem {} anos e falta {} anos para se alistar'.format(age,time))
    print('O ano do seu alistamento será: {}'. format(year + time))